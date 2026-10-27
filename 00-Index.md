---
tags: [sml, index]
---
# คลังความรู้ SML ERP

จุดเริ่มต้นของ vault นี้ อ่านจากบนลงล่างถ้าเพิ่งเริ่ม · ความครบถ้วนดู [[00-Completeness]] · รีวิวช่องว่าง [[00-Gap-Review]] · ⚠️ **ยังไม่ได้ทดสอบ [[00-Unverified]]**

## ระบบ SML ทำงานอย่างไร
- [[login-flow]] — เปิดโปรแกรม → หน้า Login → เลือก database → หน้าหลัก (ไล่โค้ดทีละขั้น)
- เอกสารเดิมใน repo: `~/dev/smlerp/SMLDocs/` (`transflag_transtype.md`, `Database.md` เป็น DBML, `MultiCurrency/`, `Report/`)
- [[data-model]] — เอกสารแต่ละกลุ่มเก็บตารางไหน เชื่อมกันอย่างไร (ยืนยันกับข้อมูล AOY)
- [[permissions]] — **สิทธิ์ผู้ใช้ SML**: user_level, สิทธิ์เมนู (XML ใน `sml_permissions_*`, กลุ่ม OR ผู้ใช้), สิทธิ์ธุรกิจใน `erp_user(_group)`
- [[cash-bank]] — **เงินสด/ธนาคาร**: `pay_type`, `cb_trans_detail.doc_type` 11 ช่องทาง, สถานะเช็คจากเอกสารเช็ค, ภาษีหัก ณ ที่จ่าย
- [[tax-period]] — **รายงานภาษีขาย/ซื้อ (กรองเอกสารยกเลิกต่างกัน), งวดบัญชี, ล็อกวันที่/เลขที่**
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
- [[menu-map]] — เมนูปลายทาง 990 รายการ → คลาสหน้าจอ, control ที่ใช้, trans_flag (จับคู่ได้ 932) + **เลขเมนู X.Y.Z ตามรุ่น** Acc/Pro/AccPOS/AccPOSPro *(generated, raw: `04-Menu/menu-map.json`)*
- [[menu-map-pos]] — ตระกูล SMLPOS (POS, Lite, TomYumGoong, TomYumGoongPro, Coffee) เมนูปลายทาง 654 รายการ + เลขเมนูตามรุ่น *(generated, raw: `04-Menu/menu-map-pos.json`)*
- [[screen-classes]] — คลาสหน้าจอจัดกลุ่มตาม base class *(generated)*
- [[menu-tree]] — เมนูทั้งหมด 1,121 รายการจาก menu.json *(generated)*
- [[doc-flow-rules]] — กฎสายเอกสาร 67 ประเภท: ยกเลิกด้วยอะไร ถูกใช้ต่อโดยเอกสารไหน, used_status / doc_success *(generated)*
- [[gl-action-codes]] — รหัสการกระทำ GL 554 รายการใน 48 กลุ่มเอกสาร (ยอดขาย, VAT, เงินสด, บัตร, ส่วนลด, ต้นทุน …) *(generated)*
- [[company-options]] — ตัวเลือกบริษัท 266 ตัวที่เปลี่ยนพฤติกรรมโปรแกรม (GL realtime, ต้นทุน, ทศนิยม, หลายสกุลเงิน …) *(generated)*
- [[enums]] — enum 102 ชุด: รหัสตัวเลขในคอลัมน์ → ความหมาย (ประเภทภาษี, สถานะเช็ค, ต้นทุน …) *(generated)*
- [[trans_flag]] — เลข trans_flag → ประเภทเอกสาร 203 ค่า *(generated)*

## โมดูลและรายงาน
- [[modules-index]] — โน้ต 1 ไฟล์ต่อเมนูหลัก (ขาย, ซื้อ, สินค้า, ลูกหนี้, เจ้าหนี้, เงินสด/ธนาคาร, บัญชี, POS …) *(generated + สรุป)*
- [[report-formulas]] — **สูตรรายงานหลัก** (ยอดขาย, ลูกหนี้/เจ้าหนี้คงค้าง, อายุหนี้, สินค้าคงเหลือ, ภาษี) พร้อมสถานะยืนยัน
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
- [[team-review-2026-10-22-prod]] — **ประชุมทีมจำลอง: sml_mcp_ai พร้อม prod แค่ไหน** (ข้อเท็จจริง, โหวต 9 ญัตติ, เฟส 0–4)
- [[team-review-2026-10-22-prod-plan]] — **ประชุมทีมจำลองครั้งที่ 2: แผน prod + ติดตั้งบน 192.168.2.109** (แผนงานใน smlmcpconnect/task.md)
- [[team-review-2026-10-22-support-use]] — **ประชุมทีมจำลองครั้งที่ 3: ใช้ vault กับพนักงาน support ได้ไหม** (ทดสอบคำถาม 12 ข้อ, โหวต 6 ญัตติ)
- [[team-review-2026-10-26-sml-team-kb]] — **ประชุมทีมจำลองครั้งที่ 4: ตรวจชุด KB ที่ทีม SML ส่งมา** (ตรวจกับโค้ด 11 ข้อ, พบ vault ผิด 2 จุด, โหวต 7 ญัตติ)
- [[write-spec-sale-order]] — **สเปกการบันทึกใบสั่งขาย (36)**: ลำดับ SQL จริง, คอลัมน์ที่ต้องใส่, เลขที่, ตรวจวงเงิน, งานหลังบันทึก, สิ่งที่ sml_mcp_ai ต้องทำ
- [[write-spec-sale-invoice]] — **สเปกการบันทึกบิลขาย (44)**: ขายสด/ขายเชื่อจากใบสั่งขาย, ตารางที่เขียน, สูตรยอดลูกหนี้จริง, งานหลังบันทึก
- [[write-spec-cancel]] — **ยกเลิกบิลขาย (45)** verified + ยกเลิกใบสั่งขาย (37) จากโค้ด/ข้อมูล; ผลต่อ GL ของบิลที่ยกเลิก
- [[write-spec-receipt]] — **รับชำระหนี้ (239)**: สูตรยอดค้างรายบิลจริง, `bill_type`, ตารางที่เขียน, `used_status_2`
- [[write-spec-credit-note]] — **รับคืน/ลดหนี้ (48)** จากโค้ด + ข้อมูลจริง (ยังไม่มี capture — ห้ามเปิดเขียน)
- [[write-spec-master-product]] — **ข้อมูลหลักสินค้า/หน่วยนับ/บาร์โค้ด**: ตาราง, unique, ค่ารหัส, การบันทึก/แก้/ลบ, งานซ่อมข้อมูลหลังบันทึก, ความผิดปกติในข้อมูลจริง
- [[write-spec-master-customer]] — **ข้อมูลลูกค้าและผู้ขาย**: สร้าง/แก้ไข `ar_customer(_detail)` (verified รอบ 6.2), `ap_supplier(_detail)` (รอบ 7.5), แก้ไข = ลบตารางลูกแล้วใส่ใหม่
- [[write-spec-inventory]] — **เอกสารสินค้า/คลัง**: โอน 72+70 (verified รอบ 10.1); ปรับปรุง/เบิก/ตรวจนับ รอทดสอบรอบ 10
- [[write-spec-purchase]] — **ซื้อเงินเชื่อ (12)** verified: ตาราง, ตรวจใบกำกับซื้อซ้ำต่อผู้ขาย, ต้นทุนหลังซื้อ
- [[write-spec-ap-payment]] — **จ่ายชำระ (19) + สูตรยอดเจ้าหนี้ค้าง** จากโค้ดร่วมกับฝั่งลูกหนี้ (ยังไม่มี capture การบันทึก)
- [[write-spec-billing-note]] — **ใบวางบิล (235)**: โครงสร้างจากข้อมูลจริง, ใบรับชำระอ้างผ่าน `detail.doc_ref`, กฎสถานะ
- [[nexflow-lessons]] — บทเรียนจาก Nexflow (Shopee/TikTok → SML): route ขาย/ยกเลิก/ลดหนี้/รับชำระ, Document Profile V1, กับดักของ SML, รูปแบบ idempotency
- [[bybos-callers-and-gap-plan]] — ใครเรียก sml-api-bybos (Nexflow, billflow, paperless), การยิง processstockrequest, ช่องว่างที่เหลือ + แผน
- [[write-api-comparison]] — เทียบ sml-api-bybos (Go) กับ SMLJavaRESTService3 (Java) สำหรับ MCP เขียนข้อมูล + ช่องว่างที่ต้องเติม
- [[product-ideas]] — ตลาด, pain point, persona, use case, ไอเดีย product 10 ข้อ

## ยังไม่ได้ทำ (งานถัดไป)
ดูรายการล่าสุดที่ [[00-Completeness]]

## Support (สำหรับพนักงาน support)
- [[faq]] — **คำถามที่พบบ่อย** 22 ข้อ: อาการ → สาเหตุ → วิธีแก้ → ผลต่อบัญชี พร้อมระดับความเชื่อมั่น
- [[error-messages]] — **ข้อความที่โปรแกรมแสดง** 851 ข้อความ (generated จากโค้ด) พร้อมหน้าจอ/เมนูที่ขึ้น
- [[support-set]] — **นโยบายชุด support** (โน้ตที่ให้/ไม่ให้, การแปลงตอน export) + `scripts/export_support.py` + skill `sml-support` (`09-Support/skill/`)
