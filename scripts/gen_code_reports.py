#!/usr/bin/env python3
"""Generate 08-Reports/code-reports.md: report engine in code (SMLERPReportTool) — reportEnum -> tables / doc types / menus.

Parses SMLERPReportTool/_reportTrans.cs, _reportCashBankTrans.cs, _reportArApTrans.cs (and any other _report*.cs there):
for each `case _reportEnum.X:` segment, collects tables referenced (`_g.d.<table>._table`) and document types.
Menus come from 04-Menu/menu-map.json (report_enum column). Run gen_menu_map.py first.

Usage: python3 scripts/gen_code_reports.py [path/to/smlerp]
"""
import collections
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
TOOL = ERP / "SMLERPReportTool"
FLAGS = dict(re.findall(r"^\| (\d+) \| (.+?) \|$", (VAULT / "03-Reference/trans_flag.md").read_text(encoding="utf-8"), flags=re.M))
NAME_TO_FLAG = {v: k for k, v in FLAGS.items()}
CASE_RE = re.compile(r"case\s+(?:SMLERPReportTool\.)?_reportEnum\.([^\s:]+)\s*:")


def main():
    info = collections.defaultdict(lambda: {"tables": collections.Counter(), "flags": set(), "files": set()})
    for p in sorted(TOOL.glob("_report*.cs")):
        src = re.sub(r"(?m)^\s*//.*$", "", p.read_text(encoding="utf-8-sig", errors="ignore"))
        parts = CASE_RE.split(src)
        pending = []
        for i in range(1, len(parts), 2):
            label, seg = parts[i], parts[i + 1]
            pending.append(label)
            body = seg.split("break;")[0] if "break;" in seg else seg[:4000]
            tables = re.findall(r"_g\.d\.(\w+)\._table", body)
            flags = {NAME_TO_FLAG.get(e) for e in re.findall(r"_transControlTypeEnum\.([^\s;,)]+)", body)} - {None}
            flags |= set(re.findall(r"trans_flag\s*(?:=|in)\s*\(?\s*(\d+)", body))
            if tables or flags or "break;" in seg or "return" in body:
                for lbl in pending:
                    d = info[lbl]
                    d["tables"].update(tables)
                    d["flags"] |= flags
                    d["files"].add(p.name)
                pending = []
    menus = collections.defaultdict(list)
    for r in json.loads((VAULT / "04-Menu/menu-map.json").read_text(encoding="utf-8")):
        for e in r.get("report_enum", []):
            menus[e].append(f"{r['text']} (`{r['name']}`)")
    L = ["---", "tags: [sml, reports, generated]", "status: from-code", "---", "# รายงานที่เขียนในโค้ด (SMLERPReportTool)", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_code_reports.py` — เครื่องมือ `_reportTrans` / `_reportCashBankTrans` / `_reportArApTrans` รับ `reportEnum` + ประเภทเอกสาร แล้วสร้าง query ตามกรณี",
         "> ตาราง = ตารางที่อ้างในโค้ดกรณีนั้น (static) · กลับไป [[reports]] · [[00-Index]]", "",
         "**ยืนยันจากการรันจริง:** รายงานการขายสินค้าและบริการใช้เงื่อนไข `trans_flag=44 and last_status=0 and (coalesce(doc_ref,'')='' or is_pos=1) and is_doc_copy<>1` ดู [[runtime-verified]]", "",
         f"ทั้งหมด {len(info)} reportEnum", "", "| reportEnum | เมนู | trans_flag | ตาราง | ไฟล์ |", "|---|---|---|---|---|"]
    for name in sorted(info):
        d = info[name]
        fl = ", ".join(sorted(d["flags"], key=lambda x: int(x)))
        tb = ", ".join(t for t, _ in d["tables"].most_common(8))
        mn = "; ".join(menus.get(name, [])[:3])
        L.append(f"| {name} | {mn} | {fl} | {tb} | {', '.join(sorted(d['files']))} |")
    (VAULT / "08-Reports/code-reports.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"reportEnums={len(info)} with menus={sum(1 for n in info if n in menus)}")


if __name__ == "__main__":
    main()
