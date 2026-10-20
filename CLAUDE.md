# คู่มือสำหรับ AI agent ที่ใช้ vault นี้

vault นี้อธิบายระบบ SML ERP (SMLSoft) — ตอบเป็นภาษาไทย

## หาข้อมูลอย่างไร (เรียงจากเร็วไปละเอียด)
1. `00-Index.md` — แผนที่ทั้ง vault
2. เมนู/หน้าจอ: ค้น `04-Menu/menu-map.json` (1 แถวต่อเมนูปลายทาง: `name`, `text`, `path`, `class`, `file`, `embedded`, `trans_flag`, `tables`) เช่น
   `python3 -c "import json;[print(r) for r in json.load(open('04-Menu/menu-map.json')) if 'ลูกหนี้' in ''.join(r['path'])]"`
3. ประเภทเอกสาร: `03-Reference/trans_flag.md`; เก็บที่ตารางไหน: `01-Architecture/data-model.md`
4. ตาราง/คอลัมน์: `grep -rn "## <table>" 02-Database/schema/`
5. รายงาน: `08-Reports/reports.md` (FastReport + ตารางที่อ่าน)
6. ความหมายคอลัมน์: `02-Database/dictionary.json` หรือ `02-Database/dictionary/dict-<module>.md`; รหัสตัวเลข: `03-Reference/enums.md`
7. กฎ: สายเอกสาร `03-Reference/doc-flow-rules.md`, ตัวเลือกร้าน `03-Reference/company-options.md`, สต็อก/ต้นทุน `01-Architecture/stock-cost.md`, ราคา/ส่วนลด/VAT/GL `01-Architecture/pricing-vat-gl.md`
8. วิธีทำงานของหน้าจอหลัก: `01-Architecture/document-engine.md`, `pos-client.md`, `login-flow.md`, `print-forms.md`; API: `webservice-api.md`
9. โค้ดจริง: `~/dev/smlerp` (C#), `~/dev/smljavaws2` (Java) — คอลัมน์ `file` ใน menu-map ชี้ path

## ระดับความเชื่อมั่น
frontmatter `status`: `verified-on-aoy` (ยืนยันกับข้อมูลจริง) > `from-code` (อ่านจากโค้ด) > ไม่ระบุ — บอกผู้ใช้เสมอว่าข้อมูลมาจากระดับไหน

## กติกา
- ไฟล์ tag `generated` แก้ผ่าน `scripts/` แล้วรันใหม่ (ดู README.md)
- ห้ามใส่รหัสผ่าน host หรือข้อมูลส่วนบุคคลของลูกค้าลง vault; query DB เฉพาะแบบสรุป (count/group by)
- เรียนรู้อะไรใหม่ → อัปเดตโน้ตที่เกี่ยวข้อง ใส่วันที่/ที่มา และลิงก์ `[[...]]`
