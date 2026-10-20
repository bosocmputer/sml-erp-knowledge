#!/usr/bin/env python3
"""Generate 03-Reference/gl-action-codes.md: GL auto-posting action codes per document group.

Source: smlerp/SMLERPGL/_process/_transProcess.cs — inside the posting loop the code switches on the
document type (grouped by #region) and then on the action code (erp_doc_format_gl.condition_number);
the `case N: // comment` comments name what amount each code posts.

Usage: python3 scripts/gen_gl_actions.py [path/to/smlerp]
"""
import collections
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
SRC = ERP / "SMLERPGL/_process/_transProcess.cs"


def main():
    region = "(ไม่มี region)"
    groups = collections.OrderedDict()
    doc_types = collections.defaultdict(set)
    for line in SRC.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        m = re.search(r"#region\s+(.+)", line)
        if m:
            region = m.group(1).strip()
            continue
        m = re.search(r"case _g\.g\._transControlTypeEnum\.([^\s:]+)\s*:", line)
        if m:
            doc_types[region].add(m.group(1))
            continue
        m = re.search(r"case\s+(\d+)\s*:\s*//\s*(.+)", line)
        if m:
            groups.setdefault(region, collections.OrderedDict()).setdefault(int(m.group(1)), m.group(2).strip())
    L = ["---", "tags: [sml, reference, gl, generated]", "status: from-code", "---", "# รหัสการกระทำ GL อัตโนมัติ (condition_number / action_code)", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_gl_actions.py` จาก comment ใน `SMLERPGL/_process/_transProcess.cs` — เลขเดียวกันอาจหมายถึงยอดต่างกันในแต่ละกลุ่มเอกสาร ให้ดูตามกลุ่ม",
         "> ใช้คู่กับ `erp_doc_format_gl` (บัญชีเดบิต/เครดิตต่อรหัส) ดู [[pricing-vat-gl]] · กลับไป [[00-Index]]", ""]
    for region, codes in groups.items():
        types = sorted(doc_types.get(region, []))
        L += [f"## {region}", ""]
        if types:
            L += ["ประเภทเอกสาร: " + ", ".join(types[:12]) + (" …" if len(types) > 12 else ""), ""]
        L += ["| รหัส | ยอดที่ลงบัญชี |", "|---|---|"] + [f"| {c} | {t} |" for c, t in sorted(codes.items())] + [""]
    (VAULT / "03-Reference/gl-action-codes.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"regions={len(groups)} codes={sum(len(v) for v in groups.values())}")


if __name__ == "__main__":
    main()
