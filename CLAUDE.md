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

## กฎสำคัญ: ห้ามเดา
- ทุกข้อความที่เป็นข้อเท็จจริงของ SML ต้องมาจาก **โค้ด** (smlerp, smljavaws2 — ระบุไฟล์/ฟังก์ชัน), **การรันจริง** (ดักจับ SQL, ระบุรอบ) หรือ **ข้อมูลจริง** (query แบบสรุป, ระบุ database/วันที่)
- ถ้ายังไม่รู้ ให้เขียนว่า **"ยังไม่ทราบ"** พร้อมสิ่งที่ต้องตรวจ — ห้ามใช้คำคาดเดา เช่น "น่าจะ", "อาจ", "คาดว่า"
- ข้อมูลจากโปรเจกต์อื่น (Nexflow, billflow, bybos ฯลฯ) เป็น **ตัวอย่างอ้างอิง** ต้องติดป้ายและไม่ใช้แทนสเปกจาก SML
- ตัวเลข % ใน [[00-Completeness]] เป็นการประเมิน ระบุไว้ชัดแล้วว่าเป็นการประเมิน

## กฎ: เตือนก่อนใช้เรื่องที่ยังไม่ได้ทดสอบ
- ก่อนตอบ ออกแบบ หรือเขียนโค้ดที่แตะเรื่องใน **`00-Unverified.md`** ต้องบอกผู้ใช้ก่อนว่าเรื่องนั้นยังเป็น `from-code` / `from-data` / `ยังไม่ทราบ` และเสนอขั้นทดสอบจากคอลัมน์ "วิธียืนยัน"
- ห้ามให้ sml_mcp_ai **เขียน**ข้อมูลในเรื่องที่ยังไม่ verified-runtime
- เมื่อทดสอบยืนยันแล้ว: อัปเดตสเปก, ย้ายเรื่องออกจาก `00-Unverified.md`, บันทึกรอบใน `01-Architecture/runtime-verified.md`

## ระดับความเชื่อมั่น
frontmatter `status`: `verified-runtime` (เห็น SQL จริงจาก capture) > `verified-on-aoy` / `from-data` (ยืนยันกับข้อมูลจริง) > `from-code` (อ่านจากโค้ด) > ไม่ระบุ — บอกผู้ใช้เสมอว่าข้อมูลมาจากระดับไหน

## กติกา
- ไฟล์ tag `generated` แก้ผ่าน `scripts/` แล้วรันใหม่ (ดู README.md)
- ห้ามใส่รหัสผ่าน host หรือข้อมูลส่วนบุคคลของลูกค้าลง vault; query DB เฉพาะแบบสรุป (count/group by)
- เรียนรู้อะไรใหม่ → อัปเดตโน้ตที่เกี่ยวข้อง ใส่วันที่/ที่มา และลิงก์ `[[...]]`
