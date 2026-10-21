---
tags: [sml, nexflow, write-api, lessons]
source: ~/dev_bos/Nexflow (README, CONTEXT, AGENTS.md §3–5, docs/sml-document-profile-v1.md, docs/sml-sales-document-profile-evidence.md, docs/shopee-auto-sml-cancel-runbook.md, backend settlement/stock-recalc code) — อ่านอย่างเดียว
status: evidence from Nexflow docs (verified by Nexflow team on AOY 2026-09) + cross-check with [[runtime-verified]]
date: 2026-10-21
---
# บทเรียนจาก Nexflow (marketplace → SML) สำหรับ MCP เขียนข้อมูล

กลับไป [[00-Index]] · ผู้เรียก bybos [[bybos-callers-and-gap-plan]] · เทียบ API [[write-api-comparison]]

> ⚠️ ข้อมูลในโน้ตนี้ **อ้างจากเอกสารของโปรเจกต์ Nexflow** (ตัวอย่างอ้างอิง ไม่ใช่สเปกหลัก) — ส่วนที่เราไม่ได้ตรวจซ้ำเองจาก smlerp/การรันจริง ให้ถือเป็น "หลักฐานรอง" จนกว่าจะยืนยัน; ส่วนที่ตรวจซ้ำแล้วระบุไว้ว่า "รวมกับที่เราดักจับได้เอง"

## Nexflow ทำอะไร
รับคำสั่งซื้อ Shopee / TikTok (Open API, realtime) และ Excel (Shopee, Lazada, TikTok) → จับคู่ SKU แบบ deterministic (ไม่ใช้ AI) → ประกอบบิล → ส่งเข้า SML ผ่าน **sml-api-bybos** ตาม route ที่ตั้งในหน้า Channel Settings → สั่งคำนวณสต็อก → แจ้ง LINE (ไม่มีข้อมูลผู้ซื้อ)
- ขาย: production ใช้ route `saleinvoice` / `SI` (flag 44)
- ยกเลิก (Shopee `CANCELLED`, TikTok): route เลือกได้ **45 ยกเลิกบิล (void)** หรือ **48 ลดหนี้/รับคืน (credit note)**
- รับชำระ: จาก **settlement** ของ marketplace (ยอดบิล − ค่าธรรมเนียม − ค่าส่ง ± ปรับปรุง − คืนเงิน = ยอดเข้าบัญชี) → `/ar/receipts` 1 ใบต่อรอบ settlement หลังคนยืนยัน (TikTok Finance ทำมือโดยตั้งใจ)

## 1. ตาราง route ที่ทีม Nexflow ยืนยันจากเอกสารที่ SML สร้างเอง (AOY, 2026-09-03)
| Route | Flag | ตารางหลัก | อัปเดตเอกสารต้นทาง | log |
|---|---:|---|---|---|
| ใบสั่งขาย | 36 | `ic_trans`, `ic_trans_detail` (calc_flag **+1**), `ic_trans_shipment` | — | screen 36, `menu_so_sale_order` |
| ยกเลิกใบสั่งขาย | 37 | `ic_trans`, `ic_trans_detail` (calc_flag −1, `cancel_type=2`, `ref_doc_no`, `ref_line_number`) | **36: `used_status=1`** | screen 37, menu ว่าง |
| ขาย | 44 | `ic_trans`, `ic_trans_detail` (calc_flag −1), `gl_journal_vat_sale`, `ic_trans_shipment` | — | screen 44, `menu_so_invoice` |
| ยกเลิกบิล | 45 | **หัวเอกสารอย่างเดียว** `ic_trans` | **44: หัว+รายการ `last_status=1`** | screen 45, `menu_so_invoice_cancel` |
| ลดหนี้/รับคืน | 48 | `ic_trans`, `ic_trans_detail` (calc_flag +1), `gl_journal_vat_sale`, `ap_ar_trans_detail` | **44: `used_status=1`** | screen 48, `menu_so_credit_note` |

ทุก route ต้องมี `logs` 1 แถว + `${tenant}_logs.erp_logs` 1 แถว (function_code 1)
**รวมกับที่เราดักจับได้เอง** ([[runtime-verified]]): บิล 44 ที่อ้างใบสั่งขาย → 36 ได้ `used_status`/`doc_success`; ใบเสร็จ 239 → 44 ได้ `used_status_2 = 1`

## 2. รายละเอียดระดับ field ที่ทำให้เอกสาร "ครบเหมือน SML สร้าง" (Document Profile V1)
- หัวบิลแบบ VAT รวมใน: `vat_type=1`, `vat_rate=7`, `tax_doc_no=doc_no`, `tax_doc_date=doc_date`, `send_date`, `credit_date` = doc_date
- **ทะเบียนภาษีขาย `gl_journal_vat_sale` ใช้ `vat_type=0` เสมอ** แม้หัวบิลเป็น 1 (กับดักสำคัญ); `vat_effective_period` = เดือนของ `vat_date`, `vat_effective_year` = ปี ค.ศ. + 543; `period_number` ปล่อยว่าง
- ตาราง VAT: แยกนอก (0) / รวมใน (1) = มีแถวยอดไม่เป็นศูนย์; อัตราศูนย์ (2) = แถวยอดศูนย์ และหัว `before/vat/after = 0/0/0` ขณะ `total_value = total_amount`
- `erp_logs.data_new` เป็น JSON 11 ส่วน: `screentop, screendetail, screenbottom, screenmore, screenshipment, screenvatsale, screengltop, screengldetail, screenpay, screenpaydeposit, screenwithholdingtax`
- **ห้ามสร้าง GL เอง** — เลขบัญชี/ต้นทุนต้องมาจาก SML (ประมวลผลรายวัน) ดู [[pricing-vat-gl]]
- ลดหนี้: `ref_amount`/`ref_diff` = `total_value` ของบิลต้นทาง; ยอดหนี้ใน AP/AR = `total_amount` (รวม VAT)
- golden fixture (ไม่มี PII): `sml-api-bybos/internal/handlers/compat/testdata/sml_sales_document_profile_v2_golden.json`

## 3. รูปแบบวิศวกรรมที่ควรใช้ซ้ำใน MCP เขียนข้อมูล
1. **บันทึก doc_no + payload ก่อนยิง SML** แล้ว retry ด้วยข้อมูลเดิมเท่านั้น (ไม่ออกเลขใหม่)
2. **idempotency ด้วย hash ของ payload** (tenant + trans_flag + doc_no); เลขซ้ำแต่ hash ต่าง → 409 `doc_no_payload_mismatch`
3. retry เฉพาะ timeout / connection / 429 / 5xx ที่ 1, 5, 15 นาที สูงสุด 3 ครั้ง; ทำทีละร้าน (serialize ต่อ shop) + lease กู้งานหลัง restart
4. **คำนวณสต็อกเป็นงานแยกที่คงทน** — ถ้าล้มเหลว retry เฉพาะ processstockrequest ไม่ส่งเอกสารซ้ำ แล้ว**ตรวจผล** (balance + evidence)
5. **preview ก่อนเขียน** และ **fail-closed** ด้วย feature flag ต่อ tenant; ไม่ backfill ย้อนหลังโดยไม่ได้อนุมัติ
6. แยกสถานะ `core_status` (เอกสารเกิดแล้ว) กับ `profile_status` (ตารางประกอบครบ) — ซ่อมส่วนที่ขาดได้โดยไม่สร้างเอกสารซ้ำ
7. ไม่ใส่ข้อมูลผู้ซื้อ (ชื่อ เบอร์ ที่อยู่) ใน log / telemetry / LINE

## 4. กับดักของ SML ที่เจอจริง (จาก AGENTS.md ของ Nexflow)
- **SML Java อ่าน body เป็น Latin-1 เสมอ** (ไม่สน charset) → ต้อง escape ตัวอักษรไทยเป็น `\uXXXX` ก่อนส่งเข้า service Java (bybos เป็น Go ไม่มีปัญหานี้)
- **รูปแบบเลขที่ `prefix-YYYY` / `prefix-YY` ทำให้เอกสารไม่แสดงใน SML UI** → ใช้ `YYMM####` ไม่มีขีดก่อนปี เช่น `BF-SO260400001`
- SML ปฏิเสธ `unit_code = ""` → ต้องมีหน่วยสำรอง
- สร้างลูกค้าผ่าน API เดิมต้องใช้ ~25 field และเจอ NPE → สร้างใน SML UI แล้วดึงมา
- สินค้าไม่พบใน product lookup คืน `{"data": null}` ไม่ใช่ error

## 5. ประโยชน์ต่อเรา (สรุป)
| ใช้กับ | ได้อะไร |
|---|---|
| vault / ความเข้าใจ SML | ยืนยันกฎสายเอกสารของการยกเลิก 37/45/48 และรายละเอียด VAT register เพิ่มจากที่เราดักจับ |
| sml_mcp_ai (เขียนข้อมูล) | ไม่ต้องออกแบบใหม่ — **เรียก bybos + ใช้ Document Profile V1 + รูปแบบ idempotency/retry/stock-recalc ของ Nexflow**; tool ของ MCP ควรเป็นแบบ preview → ยืนยัน → สร้าง |
| product ไอเดีย | settlement → ใบเสร็จ อัตโนมัติ, แจ้งเตือน LINE แบบไม่มี PII, ตัวตามคำสั่งซื้อ marketplace → SML ดู [[product-ideas]] |
| ช่องว่างใน bybos | doc flow ของ 36→44 และ 239→44 ยังไม่มีทั้งใน bybos และ Nexflow (Nexflow ไม่ได้เปิดบิลจากใบสั่งขาย) ดู [[bybos-callers-and-gap-plan]] |
