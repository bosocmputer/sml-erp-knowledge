#!/usr/bin/env python3
"""Extract PostgreSQL statements from a tcpdump capture (no tshark/scapy needed).

Reads a classic libpcap file (tcpdump -w), link types Ethernet (1), Linux SLL (113) or SLL2 (276), IPv4/TCP.
Reassembles client->server TCP payload per connection, parses the PostgreSQL frontend protocol
(StartupMessage, Query 'Q', Parse 'P') and prints statements in time order with the database name.

Marker convention: before each test step search a product with text like ZZMARK-01 in the SML program;
the statement containing "ZZMARK" starts a new segment.

Outputs (to --out directory, NOT the vault — statements may contain business data):
  statements.tsv    time, db, conn, kind, sql (raw)
  segments.md       per marker segment: statements normalized (literals -> ?), and tables written/read

Usage:
  python3 scripts/parse_pg_pcap.py capture.pcap --db aoy --db smlerpmainaoy --out ~/sml-sqllog/aoy-run1
"""
import argparse
import collections
import datetime
import pathlib
import re
import struct

WRITE_RE = re.compile(r"^\s*(insert\s+into|update|delete\s+from)\s+([a-z_0-9.\"]+)", re.I)
READ_RE = re.compile(r"\b(?:from|join)\s+([a-z_][a-z0-9_]*)", re.I)


def read_pcap(path):
    data = pathlib.Path(path).read_bytes()
    magic = data[:4]
    if magic in (b"\xd4\xc3\xb2\xa1", b"\x4d\x3c\xb2\xa1"):
        endian = "<"
    elif magic in (b"\xa1\xb2\xc3\xd4", b"\xa1\xb2\x3c\x4d"):
        endian = ">"
    else:
        raise SystemExit("not a classic pcap file (use tcpdump -w, not pcapng)")
    nano = magic in (b"\x4d\x3c\xb2\xa1", b"\xa1\xb2\x3c\x4d")
    linktype = struct.unpack(endian + "I", data[20:24])[0]
    off = 24
    while off + 16 <= len(data):
        ts_s, ts_frac, incl, _orig = struct.unpack(endian + "IIII", data[off:off + 16])
        off += 16
        pkt = data[off:off + incl]
        off += incl
        ts = ts_s + ts_frac / (1e9 if nano else 1e6)
        yield ts, linktype, pkt


def ip_payload(linktype, pkt):
    if linktype == 1:  # Ethernet
        eth_type, start = struct.unpack("!H", pkt[12:14])[0], 14
        if eth_type == 0x8100:
            eth_type, start = struct.unpack("!H", pkt[16:18])[0], 18
    elif linktype == 113:  # Linux cooked SLL
        eth_type, start = struct.unpack("!H", pkt[14:16])[0], 16
    elif linktype == 276:  # SLL2
        eth_type, start = struct.unpack("!H", pkt[0:2])[0], 20
    else:
        return None
    if eth_type != 0x0800:
        return None
    return pkt[start:]


def parse_tcp(ip):
    ihl = (ip[0] & 0x0F) * 4
    if ip[9] != 6:
        return None
    src, dst = ".".join(map(str, ip[12:16])), ".".join(map(str, ip[16:20]))
    tcp = ip[ihl:]
    sport, dport, seq = struct.unpack("!HHI", tcp[:8])
    doff = (tcp[12] >> 4) * 4
    flags = tcp[13]
    total = struct.unpack("!H", ip[2:4])[0]
    if total == 0 or total > len(ip):  # TSO/GRO packets captured before segmentation carry total length 0
        total = len(ip)
    payload = ip[ihl + doff:total]
    return src, sport, dst, dport, seq, flags, payload


class Stream:
    def __init__(self):
        self.segments = {}  # seq -> (ts, bytes)
        self.db = ""

    def add(self, ts, seq, payload):
        if payload and seq not in self.segments:
            self.segments[seq] = (ts, payload)

    def ordered(self):
        """Yield (ts, bytes) in sequence order, dropping retransmitted overlaps."""
        if not self.segments:
            return
        seqs = sorted(self.segments)
        expected = seqs[0]
        for s in seqs:
            ts, p = self.segments[s]
            if s + len(p) <= expected:
                continue
            if s < expected:
                p = p[expected - s:]
            yield ts, p
            expected = max(expected, s) + len(p)


def pg_messages(chunks):
    """Parse frontend messages from ordered (ts, bytes) chunks."""
    buf, ts_at, first = b"", [], True
    for ts, p in chunks:
        buf += p
        ts_at.append((len(buf), ts))
        while True:
            if first:
                if len(buf) < 8:
                    break
                ln, code = struct.unpack("!II", buf[:8])
                if code == 80877103:  # SSLRequest
                    buf = buf[8:]
                    continue
                if len(buf) < ln:
                    break
                body = buf[8:ln]
                buf = buf[ln:]
                first = False
                parts = body.split(b"\x00")
                params = dict(zip(parts[0::2], parts[1::2]))
                yield ts, "startup", {k.decode(errors="ignore"): v.decode(errors="ignore") for k, v in params.items() if k}
                continue
            if len(buf) < 5:
                break
            typ = chr(buf[0])
            ln = struct.unpack("!I", buf[1:5])[0]
            if ln < 4 or ln > 200_000_000:
                return  # lost sync
            if len(buf) < 1 + ln:
                break
            body = buf[5:1 + ln]
            buf = buf[1 + ln:]
            if typ == "Q":
                yield ts, "query", body.rstrip(b"\x00").decode("utf-8", errors="replace")
            elif typ == "P":
                name, _, rest = body.partition(b"\x00")
                sql = rest.split(b"\x00")[0]
                yield ts, "parse", sql.decode("utf-8", errors="replace")


def normalize(sql):
    s = re.sub(r"'(?:[^']|'')*'", "?", sql)
    s = re.sub(r"\b\d+(?:\.\d+)?\b", "?", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcap")
    ap.add_argument("--db", action="append", default=[], help="database name(s) to keep (default: all)")
    ap.add_argument("--port", type=int, default=5432)
    ap.add_argument("--include-unknown", action="store_true",
                    help="keep connections whose StartupMessage was not captured (db shown as '?')")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    streams = {}   # (4-tuple, n) -> Stream; a new SYN on a reused 4-tuple starts a new connection
    current = {}   # 4-tuple -> n
    for ts, lt, pkt in read_pcap(a.pcap):
        ip = ip_payload(lt, pkt)
        if not ip:
            continue
        t = parse_tcp(ip)
        if not t:
            continue
        src, sport, dst, dport, seq, flags, payload = t
        if dport == a.port:  # client -> server
            tup = (src, sport, dst, dport)
            if flags & 0x02:  # SYN: new connection (source ports get reused)
                if tup in current and streams[(tup, current[tup])].segments:
                    current[tup] += 1
                current.setdefault(tup, 0)
            n = current.setdefault(tup, 0)
            streams.setdefault((tup, n), Stream()).add(ts, seq, payload)
    rows = []
    keep = {d.lower() for d in a.db}
    for i, (key, st) in enumerate(sorted(streams.items(), key=lambda kv: min(kv[1].segments) if kv[1].segments else 0)):
        db = "?"
        for ts, kind, val in pg_messages(st.ordered()):
            if kind == "startup":
                db = val.get("database", "?")
                continue
            if keep and db.lower() not in keep and not (db == "?" and a.include_unknown):
                continue
            rows.append((ts, db, f"{key[0][0]}:{key[0][1]}#{key[1]}", kind, val))
    rows.sort()
    out = pathlib.Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "statements.tsv", "w", encoding="utf-8") as f:
        for ts, db, conn, kind, sql in rows:
            t = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S.%f")
            f.write(f"{t}\t{db}\t{conn}\t{kind}\t{sql.replace(chr(9), ' ').replace(chr(10), ' ')}\n")
    seg, segs = "(ก่อน marker แรก)", collections.OrderedDict()
    for ts, db, conn, kind, sql in rows:
        m = re.search(r"ZZMARK[-_]?\w*", sql, re.I)
        if m:
            seg = m.group(0).upper()
            segs.setdefault(seg, [])
            continue
        segs.setdefault(seg, []).append((ts, db, sql))
    L = [f"# SQL ตาม marker ({a.pcap})", "", "> ค่าตัวอักษร/ตัวเลขถูกแทนด้วย `?` · ไฟล์ดิบอยู่ที่ statements.tsv (มีข้อมูลจริง ห้ามใส่ vault)", ""]
    for name, items in segs.items():
        writes = collections.Counter()
        reads = collections.Counter()
        for _, db, sql in items:
            m = WRITE_RE.match(sql)
            if m:
                writes[f"{m.group(1).split()[0].lower()} {m.group(2).strip(chr(34))}"] += 1
            for t in READ_RE.findall(sql):
                reads[t.lower()] += 1
        L += [f"## {name} — {len(items)} คำสั่ง", "", "**เขียน:** " + (", ".join(f"`{k}` ×{v}" for k, v in writes.most_common()) or "-"),
              "", "**อ่าน:** " + (", ".join(f"`{k}` ×{v}" for k, v in reads.most_common(25)) or "-"), "", "```sql"]
        seen = set()
        for _, db, sql in items:
            n = normalize(sql)
            if n in seen:
                continue
            seen.add(n)
            L.append(f"-- [{db}] " + n[:2000])
        L += ["```", ""]
    (out / "segments.md").write_text("\n".join(L), encoding="utf-8")
    print(f"streams={len(streams)} statements={len(rows)} segments={len(segs)} -> {out}")


if __name__ == "__main__":
    main()
