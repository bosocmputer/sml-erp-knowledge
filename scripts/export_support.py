#!/usr/bin/env python3
"""Export the support set of this vault into a separate Obsidian folder (policy: 09-Support/support-set.md).

Copies only allow-listed notes, then on the copies:
- replaces tenant/shop database names with "ร้านทดสอบ" and IP addresses with "<ip ภายใน>"
- drops lines about internal products/other projects (sml_mcp_ai, Nexflow, bybos, openclaw, loyalty)
- replaces capture file names (aoy-runN) with "การทดสอบภายใน"
- turns [[links]] to notes outside the set into plain text
- aborts (exit 2) if internal hosts/paths/credentials remain
Also writes README.md, MANIFEST.md and copies the support skill to skill/sml-support/SKILL.md.

Usage: python3 scripts/export_support.py [output_dir]   (default ~/dev/sml-knowledge-support)
"""
import pathlib
import re
import shutil
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else pathlib.Path.home() / "dev/sml-knowledge-support"
MARKER = ".sml-support-export"

ALLOW = [
    "09-Support/faq.md", "09-Support/error-messages.md", "09-Support/error-messages.json",
    "04-Menu/menu-map.md", "04-Menu/menu-map-pos.md", "04-Menu/menu-tree.md", "05-Modules/*.md",
    "03-Reference/trans_flag.md", "03-Reference/doc-flow-rules.md", "03-Reference/company-options.md",
    "03-Reference/enums.md", "03-Reference/gl-action-codes.md",
    "01-Architecture/stock-cost.md", "01-Architecture/pricing-vat-gl.md", "01-Architecture/tax-period.md",
    "01-Architecture/permissions.md", "01-Architecture/cash-bank.md", "01-Architecture/document-engine.md",
    "01-Architecture/pos-client.md", "01-Architecture/print-forms.md", "01-Architecture/data-model.md",
    "08-Reports/report-formulas.md", "08-Reports/reports.md",
    "02-Database/dictionary/*.md",
    "00-Unverified.md",
]
SKILL_SRC = VAULT / "09-Support/skill/sml-support/SKILL.md"

TENANTS = ["debug_kbgds_data1", "thao_auto", "ploy_test", "kbyt_v", "cus_ms", "akabeko", "kbgtest", "wawacrm",
           "samai", "kbyt", "aoy", "AOY", "Aoy",
           # provider / data codes as stored in sml_database_list (upper case)
           "DEBUG_KBGDS_DATA1", "THAO_AUTO", "PLOY_TEST", "KBYT_V", "CUS_MS", "CUSMS", "AKABEKO", "KBGTEST", "WAWACRM",
           "SAMAI", "KBYT", "NEXT"]
TENANT_RE = re.compile(r"\bsmlerpmain[a-z]+\b|\b(?:" + "|".join(map(re.escape, TENANTS)) + r")\b")
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?\b")
DROP_LINE_RE = re.compile(r"(?i)sml_mcp_ai|smlmcpconnect|nexflow|bybos|openclaw|loyalty")
CAPTURE_RE = re.compile(r"\baoy-run\d+(?:-all)?\b|การทดสอบภายใน-run\d+")
LINK_RE = re.compile(r"\[\[([^\]|#]*)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
# site-specific terms (host names, user names) live in scripts/.export-forbidden (one regex per line, git-ignored)
# because the vault repo is public; the generic ones stay here
_LOCAL_FORBIDDEN = pathlib.Path(__file__).with_name(".export-forbidden")
_extra = [ln.strip() for ln in _LOCAL_FORBIDDEN.read_text().splitlines()
          if ln.strip() and not ln.startswith("#")] if _LOCAL_FORBIDDEN.exists() else []
FORBIDDEN = [re.compile(p, re.I) for p in (r"/home/", r"sshpass", r"PGPASSWORD", r"\.pgpass", r"sml-sqllog",
                                           r"trycloudflare", *_extra)]
VERSION_LIKE = re.compile(r"^\d+\.\d+\.\d+$")
# menu numbers such as "1.10.1.7" or "5.1 Acc/Pro · 6.1 AccPOS/AccPOSPro" look like IPs; keep them only in table cells
# of the generated menu notes (menu-map*.md, 05-Modules/*.md)
MENU_NOTE_RE = re.compile(r"^(04-Menu/menu-map[\w-]*\.md|05-Modules/[^/]+\.md)$")
MENU_NUM_CELL = re.compile(r"^\d+(?:\.\d+)+(?: [A-Za-z/]+)?(?: · \d+(?:\.\d+)+(?: [A-Za-z/]+)?)*$")


def collect():
    files = []
    for pat in ALLOW:
        matches = sorted(VAULT.glob(pat))
        if not matches:
            sys.exit(f"allow-list entry not found: {pat}")
        files += [m for m in matches if m.is_file()]
    return files


def transform(text, names, stats, rel=""):
    lines, out = text.split("\n"), []
    for ln in lines:
        if DROP_LINE_RE.search(ln):
            stats["dropped_lines"] += 1
            continue
        out.append(ln)
    text = "\n".join(out)

    def ip_sub(m):
        if VERSION_LIKE.match(m.group(0)):
            return m.group(0)
        stats["ip"] += 1
        return "<ip ภายใน>"
    if MENU_NOTE_RE.match(rel):
        def line_sub(ln):
            if "|" not in ln:
                return IP_RE.sub(ip_sub, ln)
            return "|".join(c if MENU_NUM_CELL.match(c.strip()) else IP_RE.sub(ip_sub, c) for c in ln.split("|"))
        text = "\n".join(line_sub(ln) for ln in text.split("\n"))
    else:
        text = IP_RE.sub(ip_sub, text)
    text, n = CAPTURE_RE.subn("การทดสอบภายใน", text)
    stats["capture"] += n
    text, n = TENANT_RE.subn("ร้านทดสอบ", text)
    stats["tenant"] += n

    def link_sub(m):
        target, head, alias = m.group(1), m.group(2) or "", m.group(3)
        if target == "" or target in names:
            return m.group(0)
        stats["links"] += 1
        return f"{alias or target} (เอกสารภายในทีม dev)"
    return LINK_RE.sub(link_sub, text)


README = """# ชุดความรู้ SML สำหรับพนักงาน support

ชุดนี้สร้างอัตโนมัติจากคลังความรู้ของทีม dev (`scripts/export_support.py`) — **ห้ามแก้ในชุดนี้ และห้ามแจกต่อสาธารณะ**

## เริ่มที่ไหน
1. ร้านแจ้งข้อความบนหน้าจอ → ค้นใน [[error-messages]] (Ctrl+F ด้วยข้อความที่ร้านเห็น)
2. อาการ/ปัญหาที่พบบ่อย → [[faq]]
3. หาเมนู/หน้าจอ → [[menu-map]] (SMLAccount ตระกูล Account/AccountPOS) หรือ [[menu-map-pos]] (ตระกูล SMLPOS) — ร้านบอกเลขเมนู ให้ถามรุ่นโปรแกรมก่อน เพราะเลขต่างกันตามรุ่น
4. เรื่องที่ยังไม่ได้ทดสอบ (ต้องส่งต่อ dev) → [[00-Unverified]]

## ระดับความเชื่อมั่น
- ✅ ยืนยันแล้ว = เห็นจากการทดสอบโปรแกรมจริงหรือข้อมูลจริง
- 🔶 จากโค้ด = อ่านจากโค้ด ยังไม่ได้ทดสอบ — บอกร้านว่า "ตามโครงสร้างโปรแกรม" และส่งต่อ dev ถ้าไม่ตรง
- คำว่า "ร้านทดสอบ" ในเอกสาร = ร้านตัวอย่างที่ทีม dev ใช้ทดสอบ (ไม่ใช่ร้านของลูกค้าที่แจ้งปัญหา)
- "(เอกสารภายในทีม dev)" = อ้างถึงเอกสารที่ไม่ได้อยู่ในชุดนี้ ถ้าต้องการรายละเอียดให้ถามทีม dev

## ใช้กับ AI
คัดลอกโฟลเดอร์ `skill/sml-support` ไปที่ `~/.claude/skills/` แล้วตั้งค่าโฟลเดอร์ชุดนี้ตามคำแนะนำใน SKILL.md
"""


def main():
    if OUT == VAULT or VAULT in OUT.parents or OUT in (pathlib.Path.home(), pathlib.Path("/")):
        sys.exit(f"refusing output dir {OUT}")
    if OUT.exists():
        if not (OUT / MARKER).exists() and any(OUT.iterdir()):
            sys.exit(f"{OUT} exists and was not created by this script (no {MARKER}); choose another dir")
        shutil.rmtree(OUT)
    files = collect()
    names = {f.stem for f in files if f.suffix == ".md"} | {"README"}
    stats = {"dropped_lines": 0, "ip": 0, "capture": 0, "tenant": 0, "links": 0}
    problems = []
    OUT.mkdir(parents=True)
    (OUT / MARKER).write_text("generated by sml-knowledge/scripts/export_support.py\n", encoding="utf-8")
    for f in files:
        rel = f.relative_to(VAULT)
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = transform(f.read_text(encoding="utf-8"), names, stats, rel.as_posix())
        for pat in FORBIDDEN:
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                problems.append(f"{rel}:{line}: {m.group(0)}")
        dst.write_text(text, encoding="utf-8")
    if SKILL_SRC.exists():
        (OUT / "skill/sml-support").mkdir(parents=True)
        shutil.copy2(SKILL_SRC, OUT / "skill/sml-support/SKILL.md")
    (OUT / "README.md").write_text(README, encoding="utf-8")
    manifest = ["# MANIFEST", "", f"exported {len(files)} files", "",
                "| แปลง | จำนวน |", "|---|---|"] + [f"| {k} | {v} |" for k, v in stats.items()] + ["", "## files", ""] + \
               [f"- {f.relative_to(VAULT)}" for f in files]
    (OUT / "MANIFEST.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    if problems:
        print("FORBIDDEN content found — export aborted (fix the source notes):", file=sys.stderr)
        print("\n".join(problems[:50]), file=sys.stderr)
        shutil.rmtree(OUT)
        sys.exit(2)
    print(f"exported {len(files)} files to {OUT} | " + ", ".join(f"{k}={v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
