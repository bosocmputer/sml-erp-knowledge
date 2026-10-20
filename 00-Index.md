---
tags: [sml, index]
---
# คลังความรู้ SML ERP

จุดเริ่มต้นของ vault นี้ อ่านจากบนลงล่างถ้าเพิ่งเริ่ม

## ระบบ SML ทำงานอย่างไร
- [[login-flow]] — เปิดโปรแกรม → หน้า Login → เลือก database → หน้าหลัก (ไล่โค้ดทีละขั้น)
- เอกสารเดิมใน repo: `~/dev/smlerp/SMLDocs/` (`transflag_transtype.md`, `Database.md` เป็น DBML, `MultiCurrency/`, `Report/`)
- [[document-engine]] — หน้าจอเอกสารกลาง `_icTransControl`: ขั้นตอนบันทึก, ตารางที่เขียน, transaction, GL, ต้นทุน
- [[architecture]] — client C# WinForms ↔ SMLJavaWebService (Tomcat) ↔ PostgreSQL, โมเดลเอกสาร ic_trans, โฟลว์ขาย/ซื้อ/คลัง, ข้อสังเกตความปลอดภัย
- [[modules]] — โปรเจกต์ที่ SMLAccount / SMLAccountPOSProfessional ใช้ พร้อมจำนวนหน้าจอ *(generated)*
- [[menu-map]] — เมนูปลายทาง 990 รายการ → คลาสหน้าจอ, control ที่ใช้, trans_flag (จับคู่ได้ 932) *(generated, raw: `04-Menu/menu-map.json`)*
- [[screen-classes]] — คลาสหน้าจอจัดกลุ่มตาม base class *(generated)*
- [[menu-tree]] — เมนูทั้งหมด 1,121 รายการจาก menu.json *(generated)*
- [[trans_flag]] — เลข trans_flag → ประเภทเอกสาร 203 ค่า *(generated)*

## Database
- [[database-layout]] — รูปแบบ DB ต่อกิจการ (`smlerpmain<provider>`, `<db>`, `_images`, `_logs`) และสถานะ DB สำเนา
- [[sql-capture-aoy]] — ขั้นตอนทดสอบเก็บ SQL กับชุด AOY ทีละขั้น
- [[sql-capture-runbook]] — วิธีเปิด log SQL บน DB สำเนาเพื่อ map เมนู → SQL
- [[schema-index]] — ตาราง/คอลัมน์ทั้งหมด 599 ตารางของ `kbyt` แยกตาม prefix *(generated)*

## sml_mcp_ai และ product
- [[mcp-project]] — MCP server ที่มีอยู่, tool ที่ครอบคลุม, ช่องว่าง, ความเสี่ยง
- [[product-ideas]] — ตลาด, pain point, persona, use case, ไอเดีย product 10 ข้อ

## ยังไม่ได้ทำ (งานถัดไป)
- รายการรายงาน (SMLERP*Report, SMLFastReport) และฟอร์มพิมพ์ (SMLFormDesign)
- POS: โฟลว์ขายหน้าร้าน กะ แคชเชียร์ (SMLPOSClient, SMLPOSControl, ตาราง `pos_*`)
- ยืนยันว่าเลข edition ใน menu.json เลขใดคือ SMLAccountPOS
- ยืนยันความหมาย trans_flag กับข้อมูลจริง และตรวจว่า field POS/ล็อตมีค่าจริง
