---
tags: [sml, index]
---
# คลังความรู้ SML ERP

จุดเริ่มต้นของ vault นี้ อ่านจากบนลงล่างถ้าเพิ่งเริ่ม · ความครบถ้วนดู [[00-Completeness]]

## ระบบ SML ทำงานอย่างไร
- [[login-flow]] — เปิดโปรแกรม → หน้า Login → เลือก database → หน้าหลัก (ไล่โค้ดทีละขั้น)
- เอกสารเดิมใน repo: `~/dev/smlerp/SMLDocs/` (`transflag_transtype.md`, `Database.md` เป็น DBML, `MultiCurrency/`, `Report/`)
- [[data-model]] — เอกสารแต่ละกลุ่มเก็บตารางไหน เชื่อมกันอย่างไร (ยืนยันกับข้อมูล AOY)
- [[server-layout]] — บริการ SML บน server จริง (docker compose, ตัวไหนรันอยู่, ไฟล์ config ใน `tomcat/temp`, โหมดคิวต้นทุน)
- [[runtime-verified]] — **ยืนยันจากการรันจริง (เฟส 2)**: ลำดับ SQL จริงของบิลขาย ยกเลิก POS ซื้อ, คิวต้นทุน `process`, เงื่อนไขรายงานยอดขาย
- [[document-engine]] — หน้าจอเอกสารกลาง `_icTransControl`: ขั้นตอนบันทึก, ตารางที่เขียน, transaction, GL, ต้นทุน
- [[pricing-vat-gl]] — ลำดับการหาราคา 7 แหล่ง, รูปแบบคำส่วนลด, ประเภทภาษี, การลงบัญชีอัตโนมัติจากรูปแบบเอกสาร
- [[stock-cost]] — สูตรยอดคงเหลือ/ค้างรับ/ค้างส่ง/ค้างจอง และวิธีคิดต้นทุน 5 แบบ (cost_type 0–4)
- [[pos-client]] — หน้าจอขายหน้าร้าน: บันทึกบิล, การรับเงิน, โต๊ะ, `pos_log`, พักบิล
- [[webservice-api]] — SMLJavaWebService: REST 23 endpoint + SOAP 178 method *(generated)*
- [[print-forms]] — ฟอร์มพิมพ์เอกสาร: ตาราง formdesign, การผูกกับรูปแบบเอกสาร, ตัวออกแบบ/พิมพ์
- [[architecture]] — client C# WinForms ↔ SMLJavaWebService (Tomcat) ↔ PostgreSQL, โมเดลเอกสาร ic_trans, โฟลว์ขาย/ซื้อ/คลัง, ข้อสังเกตความปลอดภัย
- [[modules]] — โปรเจกต์ที่ SMLAccount / SMLAccountPOSProfessional ใช้ พร้อมจำนวนหน้าจอ *(generated)*
- [[menu-map]] — เมนูปลายทาง 990 รายการ → คลาสหน้าจอ, control ที่ใช้, trans_flag (จับคู่ได้ 932) *(generated, raw: `04-Menu/menu-map.json`)*
- [[screen-classes]] — คลาสหน้าจอจัดกลุ่มตาม base class *(generated)*
- [[menu-tree]] — เมนูทั้งหมด 1,121 รายการจาก menu.json *(generated)*
- [[doc-flow-rules]] — กฎสายเอกสาร 67 ประเภท: ยกเลิกด้วยอะไร ถูกใช้ต่อโดยเอกสารไหน, used_status / doc_success *(generated)*
- [[gl-action-codes]] — รหัสการกระทำ GL 554 รายการใน 48 กลุ่มเอกสาร (ยอดขาย, VAT, เงินสด, บัตร, ส่วนลด, ต้นทุน …) *(generated)*
- [[company-options]] — ตัวเลือกบริษัท 266 ตัวที่เปลี่ยนพฤติกรรมโปรแกรม (GL realtime, ต้นทุน, ทศนิยม, หลายสกุลเงิน …) *(generated)*
- [[enums]] — enum 102 ชุด: รหัสตัวเลขในคอลัมน์ → ความหมาย (ประเภทภาษี, สถานะเช็ค, ต้นทุน …) *(generated)*
- [[trans_flag]] — เลข trans_flag → ประเภทเอกสาร 203 ค่า *(generated)*

## โมดูลและรายงาน
- [[modules-index]] — โน้ต 1 ไฟล์ต่อเมนูหลัก (ขาย, ซื้อ, สินค้า, ลูกหนี้, เจ้าหนี้, เงินสด/ธนาคาร, บัญชี, POS …) *(generated + สรุป)*
- [[reports]] — FastReport 562 ตัว (ตารางที่อ่าน, หมวด report_type) + รายงานในโค้ด 335 เมนู *(generated)*
- [[code-reports]] — เครื่องมือรายงานในโค้ด: 151 reportEnum → ตาราง/เอกสาร/เมนู *(generated)*

## Database
- [[tenants-overview]] — **ทุกร้านบน server ทดสอบ**: provider → database, ขนาด/ธุรกรรม, trans_flag ที่ใช้, ตารางเทียบตัวเลือกร้านที่มีผลต่อการบันทึก
- [[database-layout]] — รูปแบบ DB ต่อกิจการ (`smlerpmain<provider>`, `<db>`, `_images`, `_logs`) และสถานะ DB สำเนา
- [[aoy-settings]] — ค่าตั้งค่าจริงของร้าน AOY: ตัวเลือกที่เปลี่ยนพฤติกรรม + ผังลงบัญชี 12 รูปแบบเอกสาร (verified)
- [[phase2-tcpdump]] — **เฟส 2**: ดักจับ SQL จริงด้วย tcpdump + ตัวแปลง `scripts/parse_pg_pcap.py`
- [[sql-capture-aoy]] — ขั้นตอนทดสอบเก็บ SQL กับชุด AOY ทีละขั้น
- [[sql-capture-runbook]] — วิธีเปิด log SQL บน DB สำเนาเพื่อ map เมนู → SQL
- [[dictionary-index]] — **พจนานุกรมข้อมูล**: 520 ตาราง 9,988 คอลัมน์ พร้อมความหมายไทย/อังกฤษ แยก 25 โมดูล *(generated, raw: `02-Database/dictionary.json`)*
- [[schema-index]] — ตาราง/คอลัมน์ทั้งหมด 599 ตารางของ `kbyt` แยกตาม prefix *(generated)*

## sml_mcp_ai และ product
- [[mcp-project]] — MCP server ที่มีอยู่, tool ที่ครอบคลุม, ช่องว่าง, ความเสี่ยง
- [[adr-001-write-path]] — **ADR-001**: sml_mcp_ai บันทึกเอกสารแบบผสม (เขียนเอกสารเอง + คิวต้นทุนของ SML) + preview/ยืนยันสำหรับ AI
- [[write-spec-sale-order]] — **สเปกการบันทึกใบสั่งขาย (36)**: ลำดับ SQL จริง, คอลัมน์ที่ต้องใส่, เลขที่, ตรวจวงเงิน, งานหลังบันทึก, สิ่งที่ sml_mcp_ai ต้องทำ
- [[write-spec-sale-invoice]] — **สเปกการบันทึกบิลขาย (44)**: ขายสด/ขายเชื่อจากใบสั่งขาย, ตารางที่เขียน, สูตรยอดลูกหนี้จริง, งานหลังบันทึก
- [[write-spec-cancel]] — **ยกเลิกบิลขาย (45)** verified + ยกเลิกใบสั่งขาย (37) จากโค้ด/ข้อมูล; ผลต่อ GL ของบิลที่ยกเลิก
- [[write-spec-receipt]] — **รับชำระหนี้ (239)**: สูตรยอดค้างรายบิลจริง, `bill_type`, ตารางที่เขียน, `used_status_2`
- [[write-spec-credit-note]] — **รับคืน/ลดหนี้ (48)** จากโค้ด + ข้อมูลจริง (ยังไม่มี capture — ห้ามเปิดเขียน)
- [[nexflow-lessons]] — บทเรียนจาก Nexflow (Shopee/TikTok → SML): route ขาย/ยกเลิก/ลดหนี้/รับชำระ, Document Profile V1, กับดักของ SML, รูปแบบ idempotency
- [[bybos-callers-and-gap-plan]] — ใครเรียก sml-api-bybos (Nexflow, billflow, paperless), การยิง processstockrequest, ช่องว่างที่เหลือ + แผน
- [[write-api-comparison]] — เทียบ sml-api-bybos (Go) กับ SMLJavaRESTService3 (Java) สำหรับ MCP เขียนข้อมูล + ช่องว่างที่ต้องเติม
- [[product-ideas]] — ตลาด, pain point, persona, use case, ไอเดีย product 10 ข้อ

## ยังไม่ได้ทำ (งานถัดไป)
ดูรายการล่าสุดที่ [[00-Completeness]]
