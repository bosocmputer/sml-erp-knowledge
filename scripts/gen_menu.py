#!/usr/bin/env python3
"""Generate 04-Menu/menu-tree.md from smlerp/SMLAccount/menu.json.

Usage: python3 scripts/gen_menu.py [path/to/menu.json]
"""
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp/SMLAccount/menu.json"
OUT = VAULT / "04-Menu/menu-tree.md"


def tags(tag):
    return [t for t in re.findall(r"&([^&]+)&", tag or "")]


def walk(nodes, depth, lines, stats):
    for n in nodes:
        t = tags(n.get("Tag"))
        words = [x for x in t if not x.isdigit() and x != "line"]
        nums = [x for x in t if x.isdigit()]
        kids = n.get("Children") or []
        stats["total"] += 1
        if not kids:
            stats["leaf"] += 1
        meta = []
        if words:
            meta.append("tag: " + ", ".join(words))
        if nums:
            meta.append("edition: " + ",".join(nums))
        suffix = f" — `{n.get('Name')}`" + (f" ({'; '.join(meta)})" if meta else "")
        lines.append("  " * depth + f"- {n.get('Text', '').strip()}{suffix}")
        walk(kids, depth + 1, lines, stats)


def main():
    menu = json.loads(SRC.read_text(encoding="utf-8-sig"))
    lines, stats = [], {"total": 0, "leaf": 0}
    walk(menu, 0, lines, stats)
    header = [
        "---",
        "tags: [sml, menu, generated]",
        "---",
        "# ผังเมนู SML Account (menu.json)",
        "",
        f"> สร้างอัตโนมัติด้วย `scripts/gen_menu.py` จาก `{SRC}` — อย่าแก้ไฟล์นี้ด้วยมือ",
        "",
        f"เมนูหลัก {len(menu)} กลุ่ม, ทั้งหมด {stats['total']} รายการ, เมนูปลายทาง {stats['leaf']} รายการ",
        "",
        "ความหมาย tag: คำ (`so`, `po`, `ar`, `gl`, `pos`, `config`, `fastreport` …) ใช้ใน `SMLAccount/_mainForm.cs` เพื่อส่งเมนูไปยังโมดูลที่เปิดหน้าจอ;"
        " ตัวเลข (`edition`) คือรหัส edition ที่เห็นเมนูนี้ (ยืนยันจาก `SMLERPTemplate/_templateMainForm.cs`) — **12 = SMLAccountPOS** (ตัวเปิด SMLAccountPOSProfessional ใช้ค่านี้) รายการเลขทั้งหมดดู [[menu-map]]",
        "",
        "สิทธิ์การเห็นเมนูต่อผู้ใช้/กลุ่มมาจาก `smlerpmain<provider>` (`sml_permissions_user`, `sml_permissions_group`) ผ่าน `_hideNode()`",
        "",
    ]
    OUT.write_text("\n".join(header + lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({stats['total']} items)")


if __name__ == "__main__":
    main()
