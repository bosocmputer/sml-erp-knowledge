# sml-knowledge

คลังความรู้ระบบ SML ERP (SMLSoft) แบบ markdown — เปิดเป็น vault ใน [Obsidian](https://obsidian.md) ได้ทันที (Open folder as vault) และให้ Claude Code อ่านผ่าน skill `sml-erp`

เริ่มที่ [00-Index.md](00-Index.md)

## โครงสร้าง

| โฟลเดอร์ | เนื้อหา |
|---|---|
| `01-Architecture` | สถาปัตยกรรมและโมเดลเอกสาร |
| `02-Database` | รูปแบบ DB และ `schema/` (generated) |
| `03-Reference` | ตารางอ้างอิง เช่น trans_flag (generated) |
| `04-Menu` | ผังเมนู (generated) |
| `05-Modules` | โมดูล/โปรเจกต์ (generated) |
| `06-sml_mcp_ai` | โปรเจกต์ MCP server |
| `07-Product` | ไอเดีย product, ตลาด, use case |
| `08-Reports` | แค็ตตาล็อกรายงาน (generated) |
| `scripts` | ตัวสร้างไฟล์ generated |

## กติกา

- ไฟล์ที่มี tag `generated` ห้ามแก้ด้วยมือ — แก้ script แล้วรันใหม่
- ห้ามใส่รหัสผ่าน, token หรือข้อมูลส่วนบุคคลของลูกค้า (ชื่อ, เบอร์, ยอดรายลูกค้า) ลงใน vault
- ลิงก์ระหว่างโน้ตใช้ `[[ชื่อไฟล์]]` (Obsidian wikilink)
- ระบุวันที่และที่มาเมื่อบันทึกข้อเท็จจริงที่อาจเปลี่ยน และแยก "ยืนยันแล้ว" กับ "สมมติฐาน"

## สร้างไฟล์ generated ใหม่

```bash
python3 scripts/gen_menu.py            # ~/dev/smlerp/SMLAccount/menu.json → 04-Menu/menu-tree.md
python3 scripts/gen_modules.py         # ~/dev/smlerp → 05-Modules/modules.md
python3 scripts/gen_menu_map.py        # เมนู → คลาสหน้าจอ → 04-Menu/menu-map.{md,json}, screen-classes.md
python3 scripts/gen_module_notes.py    # 05-Modules/module-*.md (รันหลัง gen_menu_map)
export PGHOST=... PGPORT=... PGUSER=... PGPASSWORD=...
scripts/gen_schema.sh kbyt             # → 02-Database/schema/
python3 scripts/gen_reports.py aoy     # → 08-Reports/reports.md (อ่าน sml_fastreport, เก็บแค่ชื่อตาราง)
```

`03-Reference/trans_flag.md` สกัดจาก `SMLERPGlobal/_global.cs` ฟังก์ชัน `_transFlag()`
