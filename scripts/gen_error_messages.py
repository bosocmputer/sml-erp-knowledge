#!/usr/bin/env python3
"""Generate 09-Support/error-messages.md (+ .json): every message box the smlerp client can show.

For each `MessageBox.Show(...)` and `_displayWarning(n, ...)` call in smlerp (C#), extract the message text
(string literals, `_resource("code")` resolved through MyLib/_smlResourceManager.cs, variables shown as {…}),
the icon (Error/Warning/Information/Question), the source file:line and enclosing method, and the menus whose
screen class or embedded control lives in that file (from 04-Menu/menu-map.json). Messages are grouped by text
so support staff can search for the exact wording a shop sees.

Usage: python3 scripts/gen_error_messages.py [path/to/smlerp]
"""
import collections
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
OUT_MD = VAULT / "09-Support/error-messages.md"
OUT_JSON = VAULT / "09-Support/error-messages.json"

RES_RE = re.compile(r'^\s*_resourceList\.Add\(new _languageClass\("((?:[^"\\]|\\.)*)",\s*"((?:[^"\\]|\\.)*)",\s*"((?:[^"\\]|\\.)*)"')
VAR_RE = re.compile(r'(?:string|String)\s+(\w+)\s*=\s*([^;\n]+);')
METHOD_RE = re.compile(r'^\s*(?:public|private|protected|internal)[^;=()]*?\s(\w+)\s*\([^;]*$')
ICONS = ["Error", "Warning", "Information", "Question", "Asterisk", "Exclamation", "Hand", "Stop"]
ICON_TH = {"Error": "ผิดพลาด", "Hand": "ผิดพลาด", "Stop": "ผิดพลาด", "Warning": "เตือน", "Exclamation": "เตือน",
           "Information": "แจ้ง", "Asterisk": "แจ้ง", "Question": "ถาม"}
# _displayWarning(mode, message): resource key for the default text and icon (MyLib/_global.cs ~3627)
DISPLAY_WARNING = {0: ("delete_success", "Information"), 1: ("save_success", "Information"),
                   2: ("data_not_complete", "Error"), 3: ("warning1", "Asterisk"), 4: ("warning2", "Information")}


def unescape(s):
    return (s.replace('\\n', '\n').replace('\\t', ' ').replace('\\"', '"').replace("\\'", "'")
             .replace('\\\\', '\\'))


def load_resources():
    res = {}
    f = ERP / "MyLib/_smlResourceManager.cs"
    for line in f.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        m = RES_RE.match(line)
        if m:
            res[m.group(1)] = unescape(m.group(2))
    return res


def call_args(src, start):
    """Return the text inside the parentheses that open at src[start] (balanced, string aware)."""
    depth, i, n = 0, start, len(src)
    while i < n:
        c = src[i]
        if c == '"':
            verbatim = i > 0 and src[i - 1] == '@'
            i += 1
            while i < n:
                if verbatim and src[i] == '"' and i + 1 < n and src[i + 1] == '"':
                    i += 2
                    continue
                if not verbatim and src[i] == '\\':
                    i += 2
                    continue
                if src[i] == '"':
                    break
                i += 1
        elif c == "'":
            i += 3 if i + 1 < n and src[i + 1] != '\\' else 4
            continue
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return src[start + 1:i]
        i += 1
    return None


def split_top(args):
    parts, depth, cur, i = [], 0, [], 0
    while i < len(args):
        c = args[i]
        if c == '"':
            j = i + 1
            verbatim = i > 0 and args[i - 1] == '@'
            while j < len(args):
                if not verbatim and args[j] == '\\':
                    j += 2
                    continue
                if args[j] == '"':
                    break
                j += 1
            cur.append(args[i:j + 1])
            i = j + 1
            continue
        if c in '([{':
            depth += 1
        elif c in ')]}':
            depth -= 1
        if c == ',' and depth == 0:
            parts.append(''.join(cur))
            cur = []
        else:
            cur.append(c)
        i += 1
    parts.append(''.join(cur))
    return [p.strip() for p in parts]


TOKEN_RE = re.compile(r'''(?:MyLib\._myGlobal\.)?_resource\(\s*"((?:[^"\\]|\\.)*)"\s*(?:,[^()]*)?\)|(?:MyLib\._myGlobal\.)?_resource\(\s*(\w+)\s*\)|@?"((?:[^"\\]|\\.|"")*)"|[A-Za-z_][\w.\[\]]*(?:\([^()]*\))?''')


def to_text(expr, res, local=None):
    """Turn a C# string expression into display text; non-literal parts become {…}."""
    out, last_var = [], False
    for m in TOKEN_RE.finditer(expr):
        rkey, rvar, lit = m.group(1), m.group(2), m.group(3)
        tok = m.group(0)
        if rkey is not None:
            out.append(res.get(rkey, unescape(rkey)))
            last_var = False
        elif rvar is not None and local and rvar in local:
            out.append(res.get(local[rvar], local[rvar]))
            last_var = False
        elif lit is not None:
            out.append(unescape(lit.replace('""', '"')))
            last_var = False
        elif tok in ('MyLib._myGlobal', 'String.Format', 'string.Format', 'ToString', 'Environment.NewLine'):
            continue
        elif tok.startswith(('MyLib._myGlobal._resource', '_resource')):
            continue
        elif tok == 'Environment.NewLine' or tok.endswith('NewLine'):
            out.append('\n')
        elif local and tok in local:
            out.append(local[tok])
            last_var = False
        else:
            if not last_var:
                out.append('{…}')
            last_var = True
    text = ''.join(out)
    text = re.sub(r'[ \t]+', ' ', text).strip()
    return text


def menu_index():
    rows = json.loads((VAULT / "04-Menu/menu-map.json").read_text(encoding="utf-8"))
    by_file = collections.defaultdict(list)
    by_class = collections.defaultdict(list)
    for r in rows:
        label = ' › '.join(r.get('path', []) + [r.get('text', '')])
        if r.get('file'):
            by_file[r['file']].append(label)
        for e in r.get('embedded', []) or []:
            by_class[e.split('.')[-1]].append(label)
    return by_file, by_class


def main():
    res = load_resources()
    by_file, by_class = menu_index()
    msgs = collections.defaultdict(lambda: {"icons": collections.Counter(), "locs": [], "menus": collections.Counter(), "keys": set()})
    total_calls = 0
    for p in sorted(ERP.rglob("*.cs")):
        rel = p.relative_to(ERP).as_posix()
        if '/obj/' in rel or rel.endswith('.Designer.cs') or 'Web References' in rel:
            continue
        src = p.read_text(encoding="utf-8-sig", errors="ignore")
        if 'MessageBox.Show(' not in src and '_displayWarning(' not in src:
            continue
        lines = src.splitlines()
        local = {}
        for vm in VAR_RE.finditer(src):
            t = to_text(vm.group(2), res)
            if t and '{…}' not in t:
                local[vm.group(1)] = t
        offsets = [0]
        for ln in lines:
            offsets.append(offsets[-1] + len(ln) + 1)
        menus = list(by_file.get(rel, [])) + list(by_class.get(p.stem, []))
        for kind, pat in (("box", r'MessageBox\.Show\('), ("warn", r'_displayWarning\(')):
            for m in re.finditer(pat, src):
                start = m.end() - 1
                lineno = next(i for i in range(len(offsets)) if offsets[i + 1] > m.start()) + 1
                line_txt = lines[lineno - 1].lstrip()
                if line_txt.startswith('//') or 'public static DialogResult _displayWarning' in line_txt:
                    continue
                args = call_args(src, start)
                if args is None:
                    continue
                parts = split_top(args)
                if not parts or not parts[0]:
                    continue
                total_calls += 1
                icon = next((ic for ic in ICONS if f"MessageBoxIcon.{ic}" in args), "")
                keys = set(re.findall(r'_resource\(\s*"([^"]+)"', parts[0]))
                if kind == "warn":
                    try:
                        mode = int(parts[0])
                    except ValueError:
                        continue
                    key, icon = DISPLAY_WARNING.get(mode, (None, ""))
                    if key is None:
                        continue
                    extra = to_text(parts[1], res, local) if len(parts) > 1 and parts[1] not in ('null', '""') else ''
                    text = res.get(key, key) + ((' ' + extra) if extra and mode == 2 else '')
                    if mode != 2 and extra and extra != '{…}':
                        text = extra
                    keys = {key}
                else:
                    text = to_text(parts[0], res, local)
                if not text or set(text) <= set('{…} \n'):
                    continue
                meth = ''
                for k in range(lineno - 1, max(0, lineno - 400), -1):
                    mm = METHOD_RE.match(lines[k - 1])
                    if mm:
                        meth = mm.group(1)
                        break
                e = msgs[text]
                e["icons"][icon] += 1
                e["locs"].append(f"{rel}:{lineno}" + (f" `{meth}`" if meth else ""))
                e["keys"] |= keys
                for mn in menus:
                    e["menus"][mn] += 1
    data = []
    for text, e in msgs.items():
        project = collections.Counter(l.split('/')[0] for l in e["locs"]).most_common(1)[0][0]
        data.append({"text": text, "count": len(e["locs"]), "icon": e["icons"].most_common(1)[0][0],
                     "resource_keys": sorted(e["keys"]), "project": project, "locations": e["locs"][:5],
                     "menus": [m for m, _ in e["menus"].most_common(3)], "menu_count": len(e["menus"])})
    data.sort(key=lambda d: (d["project"], -d["count"], d["text"]))
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    by_proj = collections.defaultdict(list)
    for d in data:
        by_proj[d["project"]].append(d)

    def cell(s):
        return s.replace('|', '\\|').replace('\n', '<br>')

    L = ["---", "tags: [sml, support, generated, error-messages]", "status: from-code", "---",
         "# ข้อความที่โปรแกรม SML แสดง (MessageBox)", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_error_messages.py` จากโค้ด smlerp — ห้ามแก้มือ (แก้ที่ script แล้วรันใหม่)",
         "> กลับไป [[00-Index]] · คำถามที่พบบ่อย [[faq]] · ใช้ร่วมกับ [[menu-map]]", "",
         "**วิธีใช้:** ค้นด้วยข้อความที่ร้านเห็นบนหน้าจอ (Ctrl+F หรือถาม AI) — คอลัมน์ \"ที่โค้ด\" บอกหน้าจอ/ฟังก์ชันที่แสดงข้อความ, "
         "\"เมนู\" คือเมนูที่ใช้หน้าจอหรือ control นั้น (ข้อความใน control กลางเช่น `_icTransControl` ขึ้นได้ในหลายเมนู)", "",
         "⚠️ **ระดับ from-code:** ได้มาจากการอ่านโค้ด ยังไม่ได้ยืนยันว่าทุกข้อความขึ้นจริงในทุก edition; `{…}` = ค่าที่โปรแกรมแทรกตอนแสดง (เลขที่, ชื่อ, ข้อความจาก server); "
         "ข้อความผ่าน `_resource()` บางตัวอาจถูกแปลใหม่จากตาราง `sml_resource` ของร้าน", "",
         f"รวม {len(data):,} ข้อความ (ครอบคลุม {sum(d['count'] for d in data):,} จาก {total_calls:,} จุดในโค้ด) · คำแปลรหัส (`warningNN` ฯลฯ) จาก `MyLib/_smlResourceManager.cs` {len(res)} รายการ", "",
         "จุดที่ไม่อยู่ในรายการ = ข้อความที่สร้างตอนรันทั้งก้อน (เช่น `MessageBox.Show(__result)` ที่แสดงข้อความ error จาก web service/PostgreSQL หรือ `ex.Message`) — ดูส่วน \"ข้อความจาก server\" ด้านล่าง", "",
         "## ข้อความจาก server / database ที่โปรแกรมแปลให้ (`MyLib/_global.cs` `_errorText`)", "",
         "| ข้อความที่ร้านเห็น | สาเหตุ (ข้อความ PostgreSQL ที่ตรวจพบ) |", "|---|---|",
         "| เลขที่เอกสารซ้ำ | `duplicate key value violates unique constraint` + `ic_trans_ic_trans_pk_primary` (unique `doc_no, trans_flag` ดู [[write-spec-sale-order]] §1) |",
         "| เลขที่ เอกสารหัก ณ ที่จ่าย ซ้ำ | duplicate key + `gl_wht_list_gl_wht_list_doc_no` |",
         "| รหัสซ้ำ | duplicate key อื่น ๆ (เช่น บาร์โค้ดซ้ำ — unique `ic_inventory_barcode.barcode` ดู [[write-spec-master-product]]) |", "",
         "## สารบัญตามโปรเจกต์ (โมดูลในโค้ด)", ""]
    for proj in sorted(by_proj, key=lambda k: -len(by_proj[k])):
        L.append(f"- [[#{proj}]] ({len(by_proj[proj])})")
    L.append("")
    for proj in sorted(by_proj, key=lambda k: -len(by_proj[k])):
        L += [f"## {proj}", "", "| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |", "|---|---|---|---|---|"]
        for d in by_proj[proj]:
            locs = '<br>'.join(cell(x) for x in d["locations"][:2])
            menus = '<br>'.join(cell(x) for x in d["menus"]) + (f"<br>(+{d['menu_count'] - 3} เมนู)" if d["menu_count"] > 3 else '')
            keys = (' `' + ','.join(d['resource_keys']) + '`') if d['resource_keys'] and all(not re.search(r'[ก-๙]', k) for k in d['resource_keys']) else ''
            L.append(f"| {cell(d['text'])}{keys} | {ICON_TH.get(d['icon'], '')} | {d['count']} | {locs} | {menus} |")
        L.append("")
    OUT_MD.write_text('\n'.join(L) + '\n', encoding="utf-8")
    print(f"{len(data)} messages ({sum(d['count'] for d in data)} calls kept) from {total_calls} calls -> {OUT_MD.relative_to(VAULT)}")


if __name__ == "__main__":
    main()
