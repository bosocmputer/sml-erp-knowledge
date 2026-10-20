#!/usr/bin/env python3
"""Generate 03-Reference/company-options.md: company options (`_g.g._companyProfile._xxx`) that change program behavior.

For each option used in code: Thai meaning (matched to a column in the data dictionary, usually erp_option /
erp_company_profile), how many places use it, and which projects. Run gen_dictionary.py first.

Usage: python3 scripts/gen_options.py [path/to/smlerp]
"""
import collections
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
OPT_RE = re.compile(r"_companyProfile\._([a-z_0-9]+)")


def main():
    dic = json.loads((VAULT / "02-Database/dictionary.json").read_text(encoding="utf-8"))
    pref = ["erp_option", "erp_company_profile"]
    col = {}
    for t in sorted(dic, key=lambda t: (t["table"] not in pref, t["table"])):
        for f in t["fields"]:
            col.setdefault(f["name"], (t["table"], f["thai"]))
    uses = collections.Counter()
    projects = collections.defaultdict(collections.Counter)
    for p in ERP.rglob("*.cs"):
        src = p.read_text(encoding="utf-8-sig", errors="ignore")
        for m in (x for x in OPT_RE.finditer(src) if not x.group(1).endswith("_")):
            uses[m.group(1)] += 1
            projects[m.group(1)][p.relative_to(ERP).parts[0]] += 1
    L = ["---", "tags: [sml, reference, options, generated]", "---", "# ตัวเลือกบริษัทที่เปลี่ยนพฤติกรรมโปรแกรม (`_companyProfile`)", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_options.py` — ค่าโหลดตอน login ด้วย `_g.g._companyProfileLoad()` (`SMLERPGlobal/_global.cs`) จาก `erp_company_profile`, `erp_option` และตารางตั้งค่าอื่น",
         "> ความหมายจับคู่จากชื่อคอลัมน์ใน [[dictionary-index]] (อาจไม่ตรง 100% ถ้าชื่อซ้ำกับตารางอื่น) · กลับไป [[00-Index]]", "",
         "**ผลต่อการวิเคราะห์ข้อมูล:** ร้านแต่ละร้านตั้งค่าไม่เหมือนกัน → พฤติกรรม (GL realtime, คำนวณต้นทุน, ยอดติดลบ, รันเลขเอกสาร ฯลฯ) ต่างกัน ควรอ่านค่าจาก DB ของร้านก่อนสรุป", "",
         f"ทั้งหมด {len(uses)} ตัวเลือก", "", "| ตัวเลือก | ความหมาย | ตาราง | จุดที่ใช้ | โปรเจกต์หลัก |", "|---|---|---|---|---|"]
    for name, n in uses.most_common():
        table, thai = col.get(name, ("", ""))
        top = ", ".join(f"{k} ({v})" for k, v in projects[name].most_common(3))
        L.append(f"| `{name}` | {thai} | {table} | {n} | {top} |")
    (VAULT / "03-Reference/company-options.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"options={len(uses)} matched={sum(1 for k in uses if k in col)}")


if __name__ == "__main__":
    main()
