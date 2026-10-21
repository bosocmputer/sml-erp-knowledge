---
tags: [sml, write-api, comparison]
source: ~/dev_bos/sml-api-bybos (Go, commit 22ab47c 2026-10-07), ~/dev/smljavarestservice3 (Java, commit 1b416aa 2026-05-07), เทียบกับ [[runtime-verified]]
status: from-code (static), เกณฑ์จาก verified-runtime
date: 2026-10-21
---
# เทียบช่องทางเขียนข้อมูลลง SML: sml-api-bybos vs SMLJavaRESTService3

กลับไป [[00-Index]] · MCP [[mcp-project]] · flow จริง [[runtime-verified]] · เครื่องยนต์เอกสาร [[document-engine]]

> เทียบจากโค้ด (static) กับลำดับ SQL ที่โปรแกรม SML ทำจริง (ดักจับ 2026-10-21) — **ยังไม่ได้ดักจับ SQL ของทั้งสอง service ขณะรันจริง**

## ภาพรวม
| | **sml-api-bybos** (Go) | **SMLJavaRESTService3** (Java, ของ SMLSoft) |
|---|---|---|
| ขอบเขตเขียน | ใบสั่งขาย (36), ขาย (44), ยกเลิกขาย (45), ลดหนี้ (48), ใบสั่งซื้อ (6), รับชำระหนี้ (239), สินค้า, ลูกค้า, ผู้จำหน่าย, ล็อกเอกสาร, รูปเอกสาร | ขาย, ขาย POS, ใบสั่งขาย, ใบจอง (salereserved), รับชำระ (ARPaymentService), สินค้า (ละเอียดมาก: barcode, หน่วย, ชุด, สูตรราคา, ขนาด/สี), ลูกค้า, mobile sales/ตะกร้า |
| Transaction | ✅ `pool.Begin` → Commit/Rollback ทั้งใบ | ❌ ไม่พบ `setAutoCommit(false)` → เสี่ยงเขียนครึ่งใบถ้าพังกลางทาง |
| กันซ้ำ/แข่งกัน | ✅ idempotent (void/cancel/receipt), `pg_advisory` lock, `FOR UPDATE`, preview ก่อนเขียน | ❌ ไม่พบ |
| Auth | ✅ API key + tenant header + allow-list tenant | ⚠️ ไม่พบระบบ API key; มี endpoint `/common/_query`, `/_queryInsertOrUpdate` รับ SQL ดิบ |
| เลขที่เอกสาร | ✅ รันจาก `erp_doc_format` (`/ic/doc-no/next`) | ✅ (ตามแต่ละ service) |
| `logs` / `erp_logs` | ✅ (document profile: `logs` + reconcile `erp_logs`) | ❌ ไม่พบ |
| VAT / shipment | ✅ `gl_journal_vat_sale`, `ic_trans_shipment` (document profile) | ✅ `gl_journal_vat_sale/buy`, `ic_trans_shipment` |
| **คิวต้นทุน `process`** | ❌ **ไม่พบ** → ต้นทุน/ล็อก/`average_cost` ไม่ถูกคำนวณจนกว่ามีเอกสารอื่นของสินค้านั้นจากโปรแกรม SML | ✅ `insert into process (process_name, wherein)` (SMLICProcess / SMLTrans) |
| ยอดค้าง `book_out_qty` / `accrued_*` | ❌ ไม่พบ | ✅ พบ (SMLICProcess) |
| doc flow สถานะต้นทาง (`used_status`, `doc_success`, `used_status_2`) | ⚠️ บางส่วน (void/cancel ตั้ง `used_status`/`last_status`); **ไม่พบ** การตั้งสถานะใบสั่งขายเมื่อเปิดบิล และ `used_status_2` ของบิลเมื่อรับชำระ | ⚠️ พบอ้างถึง `used_status`/`doc_success` 9 ไฟล์ (ยังไม่ได้ไล่ว่าครบตามกฎ [[doc-flow-rules]] ไหม) |
| ขายเงินสด (`cb_trans`) | ❌ ไม่พบในบิลขาย (บิลเป็นแบบตั้งลูกหนี้ `ap_ar_trans_detail`) | ✅ `cb_trans`, `cb_trans_detail`, เช็ค `cb_chq_list` |
| เอกสารทดสอบ/สัญญา | ✅ OpenAPI, test หลายไฟล์, README ละเอียด | ⚠️ หลายเวอร์ชันปนกัน (SMLJavaRESTService, 3, 5), README สั้น |

## เทียบกับ flow จริงทีละเอกสาร (สิ่งที่โปรแกรม SML ทำ → แต่ละ service ทำไหม)
| ขั้นของโปรแกรม SML (บิลขาย) | bybos | Java |
|---|---|---|
| `insert ic_trans` + `ic_trans_detail` | ✅ | ✅ |
| `insert cb_trans` (เงินสด) / `ap_ar_trans_detail` (เชื่อ) | เชื่อ ✅ / เงินสด ❌ | ✅ / ✅ |
| `insert gl_journal_vat_sale` | ✅ (profile) | ✅ |
| `insert ic_trans_shipment` | ✅ (profile) | ✅ |
| `insert logs` + `erp_logs` | ✅ | ❌ |
| doc flow สถานะเอกสารต้นทาง | ⚠️ | ⚠️ |
| `insert process` (คิวต้นทุน) + ยอดค้าง | ❌ | ✅ |
| ทั้งหมดใน transaction เดียว | ✅ | ❌ |

## อัปเดต (2026-10-21)
ช่องว่างเรื่อง **คิวต้นทุนและยอดค้าง ถูกแก้ที่ฝั่งผู้เรียก** (billflow/Nexflow เรียก `SMLJavaWebService/rest/v1/processstockrequest` หลังสร้างเอกสาร) — ช่องว่างที่เหลือจริงคือ **doc flow สถานะเอกสารต้นทาง** ดู [[bybos-callers-and-gap-plan]]

## สรุปความเห็น
- **sml-api-bybos สมบูรณ์กว่าในด้าน "ความปลอดภัยของการเขียน"** (transaction, idempotent, lock, auth, log, preview, เอกสารประกอบ) และออกแบบมาเพื่อ AI/ระบบภายนอกเรียกใช้ → **เหมาะเป็นฐานของ MCP เขียนข้อมูล**
- **SMLJavaRESTService3 สมบูรณ์กว่าในด้าน "ผลข้างเคียงทางธุรกิจหลังบันทึก"** (คิวต้นทุน, ยอดค้าง, เช็ค, ขายเงินสด, POS) แต่ไม่มี transaction/log/auth ที่ดี
- **ช่องว่างที่ควรเติมใน bybos ก่อนใช้กับ MCP เขียนข้อมูล** (เรียงตามผลกระทบ):
  1. `insert into process` ต่อสินค้าที่เกี่ยวข้อง (ไม่งั้นต้นทุน/กำไร/ล็อกไม่อัปเดต) — ทำตามรูปแบบใน [[runtime-verified]] ข้อ 1
  2. ยอดค้าง `book_out_qty` / `accrued_in_qty` / `accrued_out_qty` (ใบสั่งขาย/ใบสั่งซื้อ)
  3. doc flow: ตั้ง `used_status` / `doc_success` ของใบสั่งขายเมื่อเปิดบิล และ `used_status_2` ของบิลเมื่อรับชำระ ตาม [[doc-flow-rules]]
  4. ขายเงินสด (`cb_trans`/`cb_trans_detail`) ถ้าต้องการ
  5. ตรวจตัวเลือกร้าน (เช่น `gl_process_realtime`) — ถ้าร้านเปิด GL realtime โปรแกรม SML จะลง GL ทันที แต่ API ไม่ทำ (ร้านต้องสั่งประมวลผล GL เอง)
- **วิธียืนยัน:** ดักจับ SQL ขณะเรียก bybos สร้างเอกสารชนิดเดียวกับที่โปรแกรมทำใน [[runtime-verified]] แล้วเทียบตารางต่อตาราง (ใช้ [[phase2-tcpdump]] เดิม, กรองตาม client IP ของ bybos)

## ข้อสังเกตด้านความปลอดภัย (ไม่เกี่ยวกับการเลือก แต่ควรรู้)
- SMLJavaRESTService3 มี endpoint รัน SQL ดิบ (`/_query`, `/_queryInsertOrUpdate`) — ถ้าเปิดสู่ภายนอก เสี่ยงแบบเดียวกับ SMLJavaWebService ดู [[architecture]]
- README ของทั้งสองโปรเจกต์มีตัวอย่างรหัสผ่าน DB — อย่าคัดลอกเข้า vault
