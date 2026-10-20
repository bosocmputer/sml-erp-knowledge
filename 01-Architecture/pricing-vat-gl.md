---
tags: [sml, pricing, discount, vat, gl, core]
source: SMLInventoryControl/_findPriceClass.cs, _findPriceCenter.cs, _icTransItemGridControl.cs, MyLib/_global.cs, SMLERPGlobal/_docFormatGeneralLedgerControl.cs, SMLERPGL/_transProcessUserControl.cs, SMLERPGL/_process/_transProcess.cs
status: from-code
date: 2026-10-20
---
# ราคา ส่วนลด ภาษี และการลงบัญชีอัตโนมัติ

กลับไป [[00-Index]] · หน้าจอเอกสาร [[document-engine]] · ตัวเลือก [[company-options]] · รหัส [[enums]]

## 1. หาราคาขาย (`_findPriceClass._findPriceByItem`)
ค้นทั้งหมดในครั้งเดียว แล้วเลือกตามลำดับ — เจออันแรกที่ตรงเงื่อนไขก็ใช้:

| ลำดับ | แหล่งราคา | ตาราง |
|---|---|---|
| 1 | ราคาตามลูกค้า | `ic_inventory_price` (price_mode ลูกค้า, cust_code) |
| 2 | ราคาตามกลุ่มลูกค้า (รวม cust_group_2 จาก `ar_customer_detail`) | `ic_inventory_price` |
| 3 | ราคาขายทั่วไป (เรียงตาม price_mode ให้ราคาที่กำหนดเองก่อน) | `ic_inventory_price` |
| 4 | ราคามาตรฐาน (ยืน) | `ic_inventory_price` |
| 5 | ราคาตามสูตร: ระดับราคาลูกค้า `ar_customer.price_level` (1–9) → `ic_inventory_price_formula.price_1..9` | `ic_inventory_price_formula` |
| 6 | ราคาตาม Barcode | `ic_inventory_barcode.price, price_2, price_3 …` |
| 7 | (ตัวเลือก `get_last_price_type`) 1 = ราคาขายล่าสุดของลูกค้า, 2 = ราคาขายเฉลี่ย | `ic_trans_detail` |

เงื่อนไขทุกแหล่ง: วันที่อยู่ในช่วง `from_date..to_date`, จำนวนอยู่ในช่วง `from_qty..to_qty`, ประเภทขาย `sale_type` (0 ขายเชื่อ/1 ขายสด) และหน่วยนับ
- POS ใช้ `_findPricePOS(...)` (มี priceNumber, ราคาพนักงาน, posId)
- `_findPriceCenter` = ราคาจาก **ศูนย์ราคากลาง** ผ่าน REST (`SMLJavaRESTService/service/pricelist/barcodeprice`) สำหรับร้านที่ตั้งค่า
- ขายต่ำกว่าทุน/ต่ำกว่าราคามาตรฐาน → เตือน/ขอรหัสอนุมัติ (`warning_price_3`, เก็บผู้อนุมัติใน `ic_trans_detail.user_approve`)

## 2. ส่วนลด (`MyLib._myGlobal._calcAfterDiscount`)
`discount` เป็น **ข้อความ** หลายขั้นคั่นด้วย `,` คิดทีละขั้นต่อเนื่อง:
- `10%` = ลด 10% ของยอดคงเหลือ ณ ขั้นนั้น
- `50` = ลด 50 บาท
- `@5` = ลด 5 บาท **ต่อหน่วย** (คูณจำนวน)
- เช่น `10%,5` = ลด 10% แล้วลดต่ออีก 5 บาท
- ปัดเศษแต่ละขั้นตามทศนิยม `item_amount_decimal` เว้นแต่เปิด `discount_step_round_off` (ไม่ปัดเศษในการลดต่อเนื่อง)
- `calc_item_price_discount` (OEM SINGHA): ลดที่ราคาต่อหน่วยก่อนแล้วคูณจำนวน; ปกติ = คูณจำนวนก่อนแล้วลดจากยอด
- ส่วนลดท้ายบิลอยู่ที่ระดับเอกสาร (`ic_trans.discount_word`, `total_discount`) และกลุ่มส่วนลด `ic_trans_discount_group`; โปรโมชั่น POS `ic_trans_detail_promotion`

## 3. ภาษีมูลค่าเพิ่ม
- `ic_trans.vat_type` ตาม `_vatTypeEnum`: **0 = ภาษีแยกนอก, 1 = ภาษีรวมใน, 2 = ยกเว้นภาษี** (3 = ไม่กระทบภาษี ใช้ภายใน)
- อัตราจาก `erp_option.vat_rate` (ตัวเลือก `vat_rate`) — **อย่าฮาร์ดโค้ด 7%**
- ยอดในหัวเอกสาร: `total_value` (มูลค่าสินค้า), `total_discount`, `total_before_vat`, `total_vat_value`, `total_except_vat` (ยอดยกเว้นภาษี), `total_amount` (ยอดสุทธิ)
- รายการ: `price` กับ `price_exclude_vat`, `sum_amount` กับ `sum_amount_exclude_vat`; รายการที่ยกเว้นภาษีกำหนดที่สินค้า (`ic_inventory.tax_type`)
- รายงานภาษีซื้อ/ขายอ่านจาก `gl_journal_vat_buy` / `gl_journal_vat_sale` ที่สร้างพร้อมเอกสาร (บิล POS = ใบกำกับภาษีอย่างย่อ, `pos_bill_type`: 0 อย่างย่อ / 1 อย่างเต็ม)

## 4. ลงบัญชีอัตโนมัติ (GL Auto)
- **รูปแบบเอกสาร** `erp_doc_format` (code → `screen_code` ประเภทเอกสาร, `gl_book` สมุดรายวัน, `gl_description` คำอธิบายที่มีตัวแปรเช่น `&AR_NAME&`, รูปแบบเลขที่ `format`, ฟอร์มพิมพ์ `form_code`)
- **ผังการเชื่อมบัญชี** `erp_doc_format_gl` ต่อรูปแบบเอกสาร: แต่ละบรรทัด = `condition_number` (รหัสการกระทำ เช่น ยอดขาย, ภาษีขาย, เงินสด, บัตร, เช็ค, ส่วนลด, ต้นทุนขาย) + `account_code_debit` / `account_code_credit` + `condition_case`
- **แม่แบบ** โหลดจาก master server ของ SML (`ws.smlaccount.com`, DB `SMLMASTER`, ตาราง `gl_doc_format` กรองตาม screen_code) มาเติมให้ร้าน — ถ้าร้านใช้ระบบสินค้าแบบ **periodic** (`inventory_gl_post = 0`) จะตัดบรรทัด action 101, 103 (ต้นทุนขาย/สินค้า) ออก
- **ตอนประมวลผล** (`_transProcessUserControl._processGLByTrans` → `SMLERPGL/_process/_transProcess.cs`): เลือกรูปแบบเอกสารของใบนั้น → วนบรรทัด `erp_doc_format_gl` → `switch` ตามประเภทเอกสาร × รหัสการกระทำ เพื่อเลือกยอด (เช่น cash_amount, card_amount, chq_amount, point_amount, coupon_amount, total_vat_value, total_discount, ต้นทุน) → เขียน `gl_journal`, `gl_journal_detail` (+ การกระจาย `gl_journal_depart_list`, `_job_list`, `_side_list`, `_allocate_list`)
- รันทันทีหลังบันทึกเมื่อเปิด `gl_process_realtime` หรือรันย้อนหลังเป็นชุดจากเมนูประมวลผล GL
- `gl_journal_detail.journal_type = 1` = ยอดยกมา (รายงานงบใช้แยกยอดยกมากับยอดระหว่างงวด) ดู `SMLProcess/_glProcess.cs`

## ยังไม่ได้ไล่
- (เสร็จแล้ว) รหัสการกระทำแยกตามกลุ่มเอกสาร ดู [[gl-action-codes]]
- สูตรภาษีละเอียดระดับบรรทัด (การปัดเศษ VAT รวมใน)
