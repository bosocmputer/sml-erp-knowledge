#!/usr/bin/env python3
"""Generate 03-Reference/enums.md: every `enum` declared in the shared global libraries.

Enums give the meaning of numeric codes stored in columns (vat type, status, payment type ...).
Member value = explicit `= n` if present, otherwise its 0-based position (C# default).

Usage: python3 scripts/gen_enums.py [path/to/smlerp]
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
PROJECTS = ["SMLERPGlobal", "MyLib", "SMLERPControl", "SMLInventoryControl", "SMLPOSControl", "SMLERPReportTool", "SMLProcess"]
ENUM_RE = re.compile(r"\benum\s+(\w+)\s*\{(.*?)\}", re.S)


def strip(src):
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"//[^\n]*", "", src)


def main():
    out = ["---", "tags: [sml, reference, enums, generated]", "---", "# Enum (รหัสตัวเลข → ความหมาย)", "",
           "> สร้างอัตโนมัติด้วย `scripts/gen_enums.py` จากโค้ด — ค่าเป็นลำดับเริ่ม 0 ถ้าไม่ได้กำหนด `= n` (กติกา C#)",
           "> ใช้ตีความคอลัมน์ตัวเลขใน DB เช่น ประเภทภาษี/สถานะ — ยืนยันกับโค้ดที่เขียนคอลัมน์นั้นก่อนสรุป", "",
           "trans_type ใน ic_trans / ic_trans_detail (จาก SMLDocs): 1 = เจ้าหนี้, 2 = ลูกหนี้, 3 = สินค้า · trans_flag ดู [[trans_flag]] · กลับไป [[00-Index]]", ""]
    total = 0
    for proj in PROJECTS:
        for p in sorted((ERP / proj).rglob("*.cs")):
            if p.name.lower().endswith(".designer.cs"):
                continue
            src = strip(p.read_text(encoding="utf-8-sig", errors="ignore"))
            for m in ENUM_RE.finditer(src):
                name, body = m.group(1), m.group(2)
                if name == "_transControlTypeEnum":
                    continue  # covered by trans_flag.md
                members, pos = [], 0
                for raw in body.split(","):
                    raw = re.sub(r"\[[^\]]*\]", "", raw).strip()
                    if not raw:
                        continue
                    mm = re.match(r"([^\s=]+)\s*(?:=\s*([-\w.]+))?", raw)
                    if not mm:
                        continue
                    if mm.group(2) and re.fullmatch(r"-?\d+", mm.group(2)):
                        pos = int(mm.group(2))
                    members.append(f"{pos}={mm.group(1)}")
                    pos += 1
                if not members:
                    continue
                total += 1
                out += [f"## {name}", "", f"`{p.relative_to(ERP).as_posix()}`", "", ", ".join(members[:80]) + (" …" if len(members) > 80 else ""), ""]
    (VAULT / "03-Reference/enums.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"enums={total}")


if __name__ == "__main__":
    main()
