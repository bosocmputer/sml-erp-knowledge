---
tags: [sml, write-api, bybos, plan]
source: ~/dev_bos/Nexflow (f65adcc 2026-10-20), ~/dev_bos/billflow (5178373 2026-10-08), ~/dev_bos/paperless-v2, ~/dev_bos/sml-api-bybos, ~/dev/smljavaws2 RequestStockProcess.java, smlerp SMLProcess/_docFlowThread.cs, runtime capture aoy-run1..3
status: from-code + verified-runtime (SQL templates)
date: 2026-10-21
---
# ใครใช้ sml-api-bybos อย่างไร และแผนเติมช่องว่างก่อนทำ MCP เขียนข้อมูล

กลับไป [[00-Index]] · เทียบ API [[write-api-comparison]] · flow จริง [[runtime-verified]] · กฎสายเอกสาร [[doc-flow-rules]]

> **ยังไม่ได้แก้โค้ดใด ๆ** — เอกสารนี้เป็นข้อเท็จจริงจากการอ่านโค้ด + แผน

## 1. โปรเจกต์ที่เรียก sml-api-bybos
| โปรเจกต์ | ใช้ endpoint หลัก | ลักษณะ |
|---|---|---|
| **Nexflow** (Shopee/TikTok/Lazada → SML) | sale-invoices (+cancel/void), sale-orders (+void), purchase-orders, products, ar/receipts, stock-capabilities, stock-balances/batch, stock-demand-evidence/batch | ใช้มากที่สุด, มี document profile, worker คำนวณสต็อกแบบ durable + ตรวจผล |
| **billflow** (บิลจาก email/marketplace → SML) | products, purchase-orders (+doc-ref), sale-orders, sale-invoices, ar/receipts, ap/suppliers, doc-formats | ยิงคำนวณสต็อกแบบ background goroutine |
| **paperless-v2** | auth/sml/login, tenants/readiness, documents/images, documents/lock, document-candidates | ไม่สร้างเอกสารขาย/ซื้อ — เก็บรูปและล็อกเอกสาร |
| `_server_sml_api_main` | ar/receipts(+candidates), sale-orders, doc-no/next, erp masters | สำเนา/ตัวอย่างฝั่ง server (ไม่มี git history) |

## 2. การ "ยิง process" — ทำที่ฝั่งผู้เรียก ไม่ใช่ใน bybos
หลัง bybos สร้างเอกสารสำเร็จ ทั้ง **billflow** และ **Nexflow** เรียก **SMLJavaWebService** โดยตรง:
```
POST {SML_WEBSERVICE}/SMLJavaWebService/rest/v1/processstockrequest
{ "providerCode": "<provider>", "databaseName": "<db>", "itemCode": ["A","B", …] }
```
- client: `Nexflow/backend/internal/services/sml/stock_request_client.go` — แบ่งชุดละ 100 รหัส, dedupe, รวม error ทุกชุด, ไม่ส่ง header ของ bybos
- **billflow** `handlers/bills.go triggerStockRecalculation`: goroutine จำกัดพร้อมกัน 3 งาน, บันทึก audit `sml_stock_recalc_failed` + คำแนะนำถ้าล้มเหลว
- **Nexflow** `services/stockrecalc/worker.go`: job ถาวร (ทุก 10 วินาที), หลังเรียกแล้ว **ตรวจยอดคงเหลือ** ผ่าน bybos `/ic/stock-balances/batch` และตรวจ **demand evidence** (`/ic/stock-demand-evidence/batch`, schema `stock-demand-evidence-v1` + fingerprint) ก่อนปล่อยการจองสต็อกฝั่ง Nexflow; ใช้ซ้ำกับการยกเลิก TikTok/Shopee

**ฝั่ง server (`smljavaws2/StockProcess/RequestStockProcess.java`)**: สำหรับแต่ละรหัส → `SMLICProcess._process_stock_cost(db, code, 0, "", "")` (ต้นทุน+ล็อต, เขียนลง DB) แล้ว `_process_stock_balance("SMLX", db, codes, "*", false)` (ยอดคงเหลือ + ค้างรับ/ค้างส่ง/ค้างจอง) → ตอบ `ok` — **ทำแบบ synchronous** ใช้แทนคิว `process` ของโปรแกรมได้
- ⚠️ endpoint นี้ **ไม่ตรวจสิทธิ์** (ใช้ GUID ตายตัว `SMLX`) — ต้องเรียกจากเครือข่ายภายในเท่านั้น ดู [[architecture]]

## 3. สถานะช่องว่างที่ระบุใน [[write-api-comparison]] (อัปเดต)
| ช่องว่าง | สถานะจริง | หมายเหตุ |
|---|---|---|
| ต้นทุน/ล็อก/`average_cost` | ✅ **ปิดแล้วโดยผู้เรียก** (processstockrequest) | ไม่ใช่ใน bybos → ทุก client ต้องทำเอง (MCP ก็ต้องทำ) |
| ยอดคงเหลือ, ค้างรับ/ส่ง/จอง | ✅ ปิดโดยผู้เรียก (`_process_stock_balance "*"`) | ถูกต้องเมื่อรายการส่ง `ref_doc_no` + `doc_ref_type` (bybos รองรับ field นี้แล้ว; 2 = จากใบจอง, 3 = จากใบสั่งขาย ตามสูตรที่ดักจับได้) |
| **doc flow สถานะเอกสารต้นทาง** | ❌ **ยังไม่มีใครทำ** | ใบสั่งขายที่ถูกเปิดบิลไม่ได้ `used_status`/`doc_success`; บิลที่ถูกรับชำระผ่าน API ไม่ได้ `used_status_2`; โปรแกรม SML ทำฝั่ง client (C#) จึงไม่มีบริการไหนรันให้ |
| `logs` / `erp_logs` | ✅ bybos (document profile) | |
| GL | ⚠️ ไม่มีใครลง GL | ปกติถ้าร้านตั้ง `gl_process_realtime = 0` (ประมวลผลภายหลังจากเมนู) แต่ถ้าร้านเปิด realtime เอกสารจาก API จะไม่มี GL จนกว่าสั่งประมวลผล |
| ขายเงินสด (`cb_trans`) | ❌ บิลผ่าน API เป็นแบบตั้งลูกหนี้ | รับเงินภายหลังด้วย `/ar/receipts` |

## 4. แผน (ยังไม่ลงมือ — รอยืนยัน)

### งาน A — doc flow ใน bybos (สำคัญที่สุด)
ทำใน transaction เดียวกับการสร้างเอกสาร โดยพอร์ตกฎจาก `_docFlowThread.cs` เฉพาะประเภทที่ API สร้าง:
1. **บิลขาย 44 อ้างอิงใบสั่งขาย 36 / ใบจอง 34:** หลัง insert บิล → คำนวณต่อใบต้นทาง `used_status = (มีรายการอ้างอิง ref_doc_no)`, `doc_success = (ยอดที่ถูกใช้ ≥ ยอดสั่ง)` โดยใช้ `sum(qty * stand_value/divide_value)` และ `last_status = 0` ตามกฎใน [[doc-flow-rules]]
2. **รับชำระ 239:** `update ic_trans set used_status_2 = 1 where trans_flag in (44,46,48) and doc_no in (select billing_no from ap_ar_trans_detail where … last_status = 0)` และตั้งกลับเป็น 0 เมื่อใบเสร็จถูกยกเลิก (คัดจาก `_docFlowThread.cs` บรรทัด ~147–150)
3. **ยกเลิก/ลดหนี้** (มีบางส่วนแล้ว) — ตรวจให้ครบตามกฎ cancel ของแต่ละประเภท
4. **ใบสั่งซื้อ 6** — ถ้าวันหน้ามีรับสินค้าจาก PO ผ่าน API
- ทดสอบ: unit test ต่อกฎ + integration test บนสำเนา AOY (สร้าง SO → บิลจาก SO → ตรวจ `used_status/doc_success`; บิล → ใบเสร็จ → ตรวจ `used_status_2`)

### งาน B — รวมจุดเรียก processstockrequest ไว้ที่เดียว (ตัดสินใจเชิงสถาปัตยกรรม)
- **ทางเลือก 1 (คงเดิม):** ผู้เรียกแต่ละราย (billflow, Nexflow, MCP) เรียกเอง — ง่าย แต่ซ้ำโค้ดและ MCP ต้องทำเองด้วย
- **ทางเลือก 2 (แนะนำ):** เพิ่มใน bybos แบบ **outbox** — บันทึกงานคำนวณสต็อก (รหัสสินค้า) ใน transaction เดียวกับเอกสาร แล้ว worker ใน bybos เรียก processstockrequest พร้อม retry/backoff และสถานะให้ผู้เรียกถามได้ → MCP/billflow/Nexflow ไม่ต้องรู้ URL ของ SMLJavaWebService
- **ทางเลือก 3:** เขียนคิว `process` แบบเดียวกับโปรแกรม (`insert into process (process_name='IC', wherein=รหัส)`) ให้ web service หยิบเอง — ใกล้กับโปรแกรมที่สุด แต่**ไม่รวม** การคำนวณยอดค้าง (`_process_stock_balance`) ที่โปรแกรมสั่งแยก ต้องตรวจเพิ่ม
- ไม่ว่าทางไหน: ห้ามทำซ้ำซ้อนกับ Nexflow worker ที่มีอยู่ (ถ้าย้ายเข้า bybos ต้องมี flag ปิดฝั่ง Nexflow/billflow)

### งาน C — ความเข้ากันได้กับตัวเลือกร้าน
- `GET /capabilities` (มีแล้ว) เพิ่มรายงานค่า `gl_process_realtime`, `inventory_gl_post`, `disable_ic_cost_process` ของ tenant เพื่อให้ client/MCP รู้ว่าต้องสั่ง GL/ต้นทุนเองหรือไม่

### งาน D — ยืนยันด้วยการรันจริง
- ดักจับ SQL (ตาม [[phase2-tcpdump]]) ขณะ bybos สร้าง SO → บิลจาก SO → ใบเสร็จ บนสำเนา AOY แล้วเทียบตารางต่อตารางกับ [[runtime-verified]] ข้อ 7 และ 11
- ตรวจหลัง processstockrequest: `sum_of_cost` มีค่า, `balance_qty` ตรงสูตร, `book_out_qty`/`accrued_out_qty` ถูกต้อง

### ลำดับที่แนะนำ
D (เก็บหลักฐานก่อนแก้) → A → C → B (ต้องคุยการแบ่งหน้าที่กับ Nexflow/billflow ก่อน) → จากนั้นค่อยเพิ่ม tool เขียนข้อมูลใน sml_mcp_ai ที่เรียก bybos (ไม่เขียน SQL เอง)

## SQL ต้นแบบจากโปรแกรมจริง (ใช้อ้างอิงตอนพอร์ต)
- คิว: `delete from process where process_name='IC' and wherein in (…)` + `insert into process (process_name, wherein) (select 'IC', code from ic_inventory where code in (…))`
- ค้างจอง (book_out): CTE `bookout` = ยอดใบจอง 34 − ยอดที่ถูกอ้างอิงโดย (44 หรือ 36 ที่ `doc_ref_type = 2`) − ยกเลิกจอง 39 (`cancel_type = 2`) แยกต่อใบ ไม่ติดลบ
- ค้างส่ง (accrued_out): CTE `accout` = ยอดใบสั่งขาย 36 − ยอดที่ถูกอ้างอิงโดย 44 ที่ `doc_ref_type = 3` − ยกเลิกสั่งขาย 37 (`cancel_type = 2`)
- ยอดคงเหลือ: ดู [[stock-cost]]
