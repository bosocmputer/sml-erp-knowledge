---
tags: [sml, sml_mcp_ai, write-spec, sale-invoice, verified-runtime]
status: verified-runtime (สร้างใบใหม่: ขายสด, ขายเชื่อที่ดึงจากใบสั่งขาย, ขายเชื่อไม่อ้างเอกสาร + ส่วนลดท้ายบิล % รอบ 6.1) / from-code (ส่วนที่ระบุ)
source: capture aoy-run1 (INV26100001 ขายสด 08:55–08:57) + aoy-run2 (INV26100002 ขายเชื่อจาก SO26100001 09:46–09:47) + แถวจริงใน aoy + smlerp SMLInventoryControl/_icTransControl.cs + smljavaws2 SMLICProcess.java
---
# สเปกการบันทึก: บิลขาย / ขายสินค้าและบริการ (trans_flag 44)

กลับไป [[00-Index]] · ใบสั่งขาย [[write-spec-sale-order]] · การตัดสินใจ [[adr-001-write-path]] · สต็อก [[stock-cost]] · สายเอกสาร [[doc-flow-rules]]

> **ขอบเขต:** สร้างบิลขาย**ใบใหม่**ผ่านหน้าจอขาย (ไม่ใช่ POS — POS มี `is_pos=1` และเส้นทางต่างกัน ดู [[pos-client]])
> - **ขายสด** (`inquiry_type=1`) ไม่อ้างเอกสาร — INV26100001
> - **ขายเชื่อ** (`inquiry_type=0`) ดึงจากใบสั่งขาย — INV26100002
> **ยังไม่ครอบคลุม:** ขายเชื่อที่ไม่อ้างเอกสาร, ดึงจากใบเสนอราคา/ใบจอง, รับชำระด้วยบัตร/เช็ค/โอน/มัดจำ, ส่วนลดท้ายบิล, ภาษีหัก ณ ที่จ่าย, หลายสกุลเงิน, แก้ไข/ลบ, GL realtime (ไม่มี tenant ไหนเปิด) — ยกเลิกบิล (45) แยกเป็นสเปกของตัวเอง
> ค่าที่เป็นชื่อ/ที่อยู่/รหัสลูกค้าไม่คัดลอกลง vault

## 0. ลำดับเหตุการณ์จริง

| # | ขายสด (run1) | ขายเชื่อจาก SO (run2) | ขั้น | transaction |
|---|---|---|---|---|
| 1 | 08:55:38 | 09:46:30 | อ่าน `erp_doc_format` (`INV`) → หาเลขที่ล่าสุด → **ตรวจเลขใบกำกับซ้ำ** `select vat_number from gl_journal_vat_sale where upper(vat_number)=?` | อ่าน |
| 2 | — | 09:46:42–49 | เลือกใบสั่งขายของลูกค้า: `ic_trans where trans_flag=36 and cust_code=? and doc_success=0 and last_status=0` → อ่านหัว/`ic_trans_shipment`/บรรทัด → คำนวณจำนวนคงเหลือที่ยังดึงได้ต่อบรรทัด | อ่าน |
| 3 | — (ไม่เกิด: ขายสด) | 09:46:52.280 | **ดึงยอดวงเงินและยอดลูกหนี้** (SQL ในข้อ 1.3) — เฉพาะขายเชื่อ | อ่าน |
| 4 | | 09:46:52.55–.85 | อ่าน `erp_company_profile`, `erp_option`, สิทธิ์ผู้ใช้, `erp_thai_qr_config`, `erp_option_etax_inet`, `erp_option_mobillyst` | อ่าน |
| 5 | 08:56:46.363–.549 | 09:46:52.969–53.041 | **`BEGIN` → ตารางในข้อ 2 → `COMMIT`** | **1 transaction** |
| 6 | 08:56:46.769 / 47.114 | 09:46:53.165 / .263 | `logs` (DB ร้าน) / `erp_logs` (DB `_logs`) | แยก |
| 7 | 08:57:14 | 09:47:24 | พิมพ์ฟอร์ม (`form_code` ของ INV = `INV0018,INV0001`) — block จนปิดหน้าพิมพ์ | อ่าน |
| 8 | 08:57:24 | 09:47:26–27 | thread `_processThread._run`: doc flow → `_updateDateTimeForCalc` → `_process_stock_balance(items,"44")` | หลาย transaction |
| 9 | 08:57:28–29 | — | โปรแกรมที่เปิดอยู่หยิบคิว `process` → เขียนต้นทุนลงบรรทัดขาย | แยก |

## 1. ก่อนเขียน

### 1.1 เลขที่เอกสาร / เลขใบกำกับ
- AOY: `erp_doc_format where code='INV'` → `format='@YYMM####'`, `screen_code='SI'`, `gl_book='A0004'`, `tax_format` ว่าง → `doc_no` = `tax_doc_no` = INV26100001
- หาเลขที่: `select doc_no from ic_trans where (doc_date >= '<ต้นปี>') and doc_no like 'INV2610%' AND trans_flag = 44 and trans_type = 2 order by doc_no desc limit 1` → +1 (ไม่มีล็อก; unique `(doc_no, trans_flag)` กันซ้ำ เหมือน [[write-spec-sale-order]])
- ตรวจเลขใบกำกับไม่ซ้ำใน `gl_journal_vat_sale.vat_number` (ตัวพิมพ์ใหญ่)

### 1.2 ดึงจากใบสั่งขาย (ขายเชื่อ run2)
- เลือกได้เฉพาะใบสั่งขายที่ `doc_success=0` และ `last_status=0` ของลูกค้าคนเดียวกัน
- บรรทัดบิลที่ดึงมา: `doc_ref_type = 3`, `ref_doc_no` = เลขใบสั่งขาย, `ref_row` = `line_number` ของบรรทัดต้นทาง; `price_mode`/`price_type` = null (ไม่ได้หาราคาใหม่)
- **หัวบิล `doc_ref` = null** — การอ้างอิงอยู่ที่บรรทัด + แถว `ap_ar_trans_detail` (ข้อ 2.4)

### 1.3 ยอดลูกหนี้ / วงเงิน (SQL จริง 09:46:52.280)
`ar_customer_detail.credit_money`, `credit_money_max`, `credit_status`, `close_reason*`, `close_credit_date` และ **`balance_end` คำนวณสดจากเอกสาร** (ทุกตัว `last_status=0`, ไม่นับใบที่กำลังบันทึก `doc_no != ?`):

| บวก/ลบ | เอกสาร |
|---|---|
| + `total_amount` | `ic_trans` trans_flag 44, 418, 250 ที่ `inquiry_type in (0,2)` (ขายเชื่อ) |
| + `total_amount` | `ic_trans` trans_flag 93, 99 |
| + `total_amount` | `ic_trans` trans_flag 46, 95, 101 (เพิ่มหนี้) |
| − `total_amount` | `ic_trans` trans_flag 48 ที่ `inquiry_type in (0,2,4)` (ลดหนี้) |
| − `total_amount` | `ic_trans` trans_flag 97, 103, 252 |
| − `total_net_value` | `ap_ar_trans` trans_flag 239 (รับชำระหนี้) |

⇒ **ไม่มีตาราง "ตั้งลูกหนี้" แยก** — ยอดค้างของลูกค้า = ผลรวมเอกสารข้างบน
- การตัดสินใจหลังได้ยอด (`_creditMoneySaleCheck`, `_icTransControl.cs` ~11784): ทำเฉพาะขายเชื่อ (`inquiry_type=0`) ที่มีรหัสลูกค้า; เทียบ `total_amount > credit_money − balance` เมื่อร้านเปิด `warning_credit_money` / `lock_credit_money` (หรือ `credit_status=2` + `request_ar_credit`) → เตือน / ห้ามบันทึก / ขออนุมัติ — **from-code** (AOY ปิดทั้งสองตัว จึงเห็นแค่ query ไม่เห็นผลการตัดสิน) · ร้านที่เปิดดู [[tenants-overview]] §4

## 2. Transaction หลัก (ข้อ 5)

| ตาราง | ขายสด | ขายเชื่อจาก SO |
|---|---|---|
| `ic_trans` (42 คอลัมน์) | ✅ | ✅ |
| `ic_trans_detail` (62 คอลัมน์ ต่อบรรทัด) | ✅ | ✅ |
| `ap_ar_trans_detail` (เอกสารอ้างอิง) | — | ✅ 1 แถวต่อเอกสารที่อ้าง |
| `cb_trans` (31 คอลัมน์, การรับเงิน) | ✅ | — |
| `delete from cb_trans_detail where trans_number is null or trans_number=''` | ✅ (2 ครั้ง) | ✅ (1 ครั้ง) |
| `gl_journal_vat_sale` (29 คอลัมน์, ภาษีขาย) | ✅ | ✅ |
| `ic_trans_shipment` (19 คอลัมน์) | ✅ | ✅ |

ลำดับใน transaction: `ic_trans` → `ic_trans_detail`… → (`ap_ar_trans_detail`) → (`cb_trans`) → `delete cb_trans_detail …` → `gl_journal_vat_sale` → `ic_trans_shipment`

### 2.1 `ic_trans` — ต่างจากใบสั่งขายอย่างไร
ใช้ชุดเดียวกับ [[write-spec-sale-order]] §2.1 ยกเว้น:
- **เพิ่ม:** `tax_doc_date`, `tax_doc_no` (= doc_date, doc_no), `advance_amount` (0), `cashier_code` (ผู้ใช้), `user_approve` (null)
- **ไม่มี:** `expire_day`, `expire_date`
- ค่าจริง: `trans_flag=44`, `doc_format_code='INV'`, `inquiry_type` 1 (สด) / 0 (เชื่อ), `vat_type=1`, `vat_rate=7.00`
- VAT หัวคิดจากยอดรวม: ขายสด 590 → `total_before_vat` 551.40, `total_vat_value` 38.60 (ผลรวมบรรทัด 280.37+271.03 = 551.40 / 19.63+18.97 = 38.60); ขายเชื่อ 600 → 560.75 / 39.25 (ผลรวมบรรทัด 560.74 / 39.26)

### 2.2 `ic_trans_detail` — ต่างจากใบสั่งขาย
- **`calc_flag = -1`** (สต็อกออก; ใบสั่งขายเป็น 1)
- **เพิ่ม:** `hidden_cost_1` (0), `date_expire` (null) → 62 คอลัมน์
- `doc_date_calc`/`doc_time_calc` = doc_date/doc_time; `line_number` เริ่ม 0
- ดึงจาก SO: `doc_ref_type=3`, `ref_doc_no`, `ref_row` (ข้อ 1.2)
- **ต้นทุน (`sum_of_cost`, `average_cost` ฯลฯ) ไม่ได้ใส่ตอน insert** — worker เติมทีหลัง (ข้อ 3.4)

### 2.3 `cb_trans` (ขายสดเท่านั้น — สร้างเมื่อ `_payControl.Enabled`, `_icTransControl.cs` ~15781)
`doc_format_code, doc_no, doc_date, doc_time, ap_ar_code, pay_type (1), trans_type (2), trans_flag (44), remark, total_amount, cash_amount, total_credit_charge, total_income_amount, total_expense_other, petty_cash_amount, deposit_amount, pay_cash_amount, total_tax_at_pay, money_change, chq_amount, tranfer_amount, card_amount, coupon_amount, point_qty, point_rate, point_amount, discount_amount, total_income_other, wallet_amount, total_net_amount, total_amount_pay`
- INV26100001: `total_amount = cash_amount = total_net_amount = total_amount_pay = 590.00`, ช่องอื่น 0
- รับด้วยเงินสดอย่างเดียว → ไม่มีแถว `cb_trans_detail` (ช่องทางบัตร/เช็ค/โอนจะอยู่ในตารางนั้น — ยังไม่ได้ดักจับ)

### 2.4 `ap_ar_trans_detail` (ขายที่อ้างเอกสาร)
`calc_flag=-1, trans_type=2, trans_flag=44, doc_date, doc_no, bill_type=3, billing_no=<เลขใบสั่งขาย>, billing_date, ref_doc_no=null, ref_doc_date=null, remark, line_number=0`
- **นี่คือตาราง "เอกสารอ้างอิง" ของบิล** (หน้าจอโหลดกลับด้วย `_loadDataToScreen` → `_icTransRef._transGrid`, ~บรรทัด 9752) **ไม่ใช่การตั้งลูกหนี้** — `bill_type` = ประเภทเอกสารที่อ้าง (3 = ใบสั่งขาย ตรงกับ `doc_ref_type`)
- ระบบอื่นใช้แถวนี้ไล่สายเอกสาร (เช่น query ของ sml-api-bybos join `ap_ar_trans_detail.billing_no` ระหว่าง 36 → 44)

### 2.5 `gl_journal_vat_sale` (ทุกบิลที่มี VAT)
`book_code='', vat_calc=1, trans_type=2, trans_flag=44, doc_date, doc_no, ar_code, ref_doc_date, ref_doc_no, ref_vat_date, ref_vat_no, vat_date (= doc_date), vat_number (= tax_doc_no), vat_effective_period (10 = เดือน), vat_effective_year (2569 = **ปี พ.ศ.**), description, tax_group, base_caltax_amount (= total_before_vat), tax_rate (7.00), amount (= total_vat_value), except_tax_amount (0), vat_type (**0** ทั้งที่หัวบิล `vat_type=1`), is_add (0), ar_name, tax_no, branch_type (0), branch_code, manual_add (0), line_number (0)`

### 2.6 `ic_trans_shipment` — เหมือน [[write-spec-sale-order]] §2.3 (`trans_flag=44`)

## 3. หลัง commit
1. `logs` และ `erp_logs` — รูปแบบเดียวกับ [[write-spec-sale-order]] §3 (`screen_code=44`)
2. **doc flow** (`SMLProcess._docFlow._processAll`):
   - ตัวบิลเอง: `update ic_trans_detail set last_status=0 … trans_flag in (44)`, เหมือนกันกับ `ap_ar_trans_detail`, `update cb_trans set status=0 where doc_no=? and trans_flag=44 and status<>0`, `update cb_trans_detail set last_status=0 …`
   - **เอกสารต้นทาง (ขายจาก SO):** `update ic_trans set used_status=1, doc_success=1 where roworder=<ใบสั่งขาย>` แล้ว reset `last_status` ของบรรทัด 36 (ยืนยันใน DB: SO26100001 `used_status=1, doc_success=1`)
   - ล้าง `cb_chq_list` ที่ไม่มีที่มา (ทำทุกครั้ง)
3. **`_process_stock_balance(items,"44")`**: flag 44 อยู่ใน `_stockBalanceFlag` → ปรับ `item_type` → **`balance_qty`** (CTE `stock` ตามสูตรใน [[stock-cost]]) → `accrued_in_qty` → **`book_out_qty`/`accrued_out_qty`** (ค้างส่งของใบสั่งขายลดลงเพราะถูกดึงแล้ว) → คิว `process` 'IC'
4. **ต้นทุน** (worker 08:57:28–29, ขายสด): `update ic_trans_detail set sum_of_cost=?, sum_of_cost_1=?, average_cost=?, average_cost_1=?, profit_lost_cost_amount=0 where roworder=?`, `update ic_inventory set average_cost=?`, ล็อต `ic_trans_detail_lot` (สินค้า FIFO), `delete from process where roworder=?` — **กำไรของบิลจะถูกต้องหลังขั้นนี้เท่านั้น** และขั้นนี้ต้องมีโปรแกรม SML เปิดอยู่ ([[stock-cost]] § ใครเป็นคนหยิบคิว)
5. serial number: ชุด `UPDATE ic_trans_serial_number …` / `ic_serial` (ทำทุกครั้ง ไม่เกี่ยวถ้าสินค้าไม่มี serial)

**สิ่งที่ไม่เกิด** (AOY, `gl_process_realtime=0`): ไม่มี `ap_ar_trans` หัว, ไม่มี `gl_journal`/`gl_journal_detail` (GL มาจากการประมวลผล batch ภายหลัง [[pricing-vat-gl]])

## 4. สำหรับ sml_mcp_ai
- `preview_sale_invoice`: เหมือน [[write-spec-sale-order]] §4 + ตรวจเลขใบกำกับซ้ำ + คำนวณ `balance_end` ด้วยสูตรข้อ 1.3 แล้วใช้กฎวงเงินตามตัวเลือกร้าน + (ถ้าอ้าง SO) ตรวจ SO `doc_success=0`, `last_status=0`, ลูกค้าตรงกัน และจำนวนไม่เกินคงเหลือ
- `commit_sale_invoice` (transaction เดียว): ตารางข้อ 2 ตามประเภทการขาย → doc flow ของ SO ต้นทาง (ข้อ 3.2) → SQL ส่วนที่ 1 ของสต็อก (ข้อ 3.3) → คิว `process` 'IC' → `logs`; หลัง commit `erp_logs`
- ต้นทุน: สถานะ `cost_status` (pending จนแถวคิวหาย + `sum_of_cost` มีค่า) — ถ้าร้านไม่มีคนเปิดโปรแกรม ต้องใช้ทางสำรอง ([[adr-001-write-path]])
- ห้ามเขียน `ap_ar_trans_detail` สำหรับบิลขายเชื่อที่ไม่ได้อ้างเอกสาร (โปรแกรมไม่ได้ทำ — ยอดลูกหนี้มาจาก `ic_trans` อยู่แล้ว)

## 5. ยังไม่ทราบ
- ขายเชื่อที่ไม่อ้างเอกสาร: ยังไม่ได้เห็น SQL จริง (ขายสดที่ไม่อ้างเอกสารไม่มี `ap_ar_trans_detail` — ขายเชื่อยังไม่ได้ยืนยัน)
- ~~`gl_journal_vat_sale.vat_type = 0` ขณะที่หัวบิล `vat_type = 1`~~ → ตอบแล้ว: ในตารางภาษี 0 = ภาษีถึงกำหนด, 1 = ยังไม่ถึงกำหนด (คนละความหมายกับหัวบิล) [[tax-period]] §2
- ~~`delete from cb_trans_detail where trans_number is null or ''` มาจากไหน~~ → คำสั่งสุดท้ายของ `_payControl._queryInsert` ([[cash-bank]] §1); ยังไม่ทราบว่าทำไมรันในบิลขายเชื่อ (ไม่มีการรับเงิน) ด้วย
- ช่องทางรับเงินอื่น (บัตร/เช็ค/โอน/คูปอง/คะแนน/มัดจำ) และ `cb_trans_detail`
- `tax_format` ที่ไม่ว่าง (ร้านที่ใช้เลขใบกำกับแยกจากเลขบิล)
- ค่า default ของคอลัมน์ที่ไม่ได้ใส่ และข้อ 5 อื่น ๆ ใน [[write-spec-sale-order]]

## 6. ยืนยันจากรอบ 6.1: ขายเชื่อไม่อ้างเอกสาร + ส่วนลดท้ายบิล 5% (INV26100003, 13:43:56 วันที่ 2026-10-26)
ลูกค้า `AB-2605-0002` · `ZZTEST-0001` 1 × 20 + `AH-0001` 1 × 240 = 260 · ส่วนลด `5%` · ภาษีรวมใน · รูปแบบเลข `INV`
- **Transaction เดียว:** `ic_trans` (43 คอลัมน์) → `ic_trans_detail` × 2 → cleanup `cb_trans_detail` เลขว่าง → `gl_journal_vat_sale` → `ic_trans_shipment` → `COMMIT` · **ไม่มี `cb_trans`/`cb_trans_detail`** (เชื่อ) และ**ไม่มี `ap_ar_trans_detail`** (ไม่อ้างเอกสาร)
- **ส่วนลดท้ายบิลเก็บที่หัวเท่านั้น:** `discount_word='5%'` (ข้อความตามที่พิมพ์), `total_discount=13.00`, `total_value=260` (ก่อนลด), `total_after_vat = total_amount = 247.00`, `total_before_vat=230.84`, `total_vat_value=16.16` ⇒ **ภาษีคิดจากยอดหลังหักส่วนลด** (247 / 1.07)
- **บรรทัดไม่ถูกกระจายส่วนลด:** `discount=null`, `discount_amount=0`, `sum_amount` 20 / 240, `sum_amount_exclude_vat` 18.69 / 224.30 (รวม 242.99 ≠ 230.84 ของหัว) ⇒ รายงานที่รวมยอดจากบรรทัดจะได้ยอดก่อนหักส่วนลดท้ายบิล
- `gl_journal_vat_sale`: `vat_calc=1`, ฐาน 230.84, ภาษี 16.16
- บรรทัด: `ref_row=-1`, `doc_ref_type=0`, `calc_flag=-1` · `price_mode/price_type` '-1' (ZZTEST ไม่มีสูตรราคา) / '6' + `set_ref_price=300` (AH-0001) — เหมือนใบสั่งขาย [[write-spec-sale-order]] §6.4
- `cashier_code=<ผู้ใช้>`, `advance_amount=0`, `send_type=0`
- หลัง commit (~11 วินาที): doc flow reset `last_status` → worker ต้นทุน: ล็อต + `sum_of_cost` ต่อบรรทัด (ZZTEST 9.35, AH-0001 149.54 — ต้นทุนบรรทัด AH-0001 มาจากล็อต ไม่ใช่ `average_cost` 227.30 ของสินค้า)
- ตรวจ DB: `balance_qty` ZZTEST-0001 2 → 1, AH-0001 123 → 122 · บิล `used_status=0, last_status=0`
- **สำหรับ sml_mcp_ai:** ส่วนลดท้ายบิลส่ง `discount_word` (ข้อความ เช่น `5%` หรือตัวเลข) + `total_discount` ที่คำนวณแล้ว และคำนวณภาษีจากยอดหลังลด · ไม่ต้องกระจายลงบรรทัด (โปรแกรมไม่ทำ)

## 7. ยืนยันจากรอบ 6.4: ใบเสนอราคา → ใบสั่งจอง → ขายเชื่อ (QT26100001 14:34:45, BS26100001 14:35:52, INV26100005 14:37:05 วันที่ 2026-10-26)
ลูกค้า `ZZCUST-0001` · `AH-0001` 1 กล่อง × 240 ภาษีรวมใน ทุกใบ

| ใบ | ตาราง (transaction เดียว) | บรรทัด `ic_trans_detail` | แถวอ้างอิง `ap_ar_trans_detail` |
|---|---|---|---|
| **ใบเสนอราคา 30** (เมนู ขาย › ใบเสนอราคา) | `ic_trans` (40 คอลัมน์: `user_request`, `approve_code=null`, `expire_day/date`, `credit_day=30` จากลูกค้า) + `ic_trans_detail` | **ไม่มีคอลัมน์ `wh_code/shelf_code`, `doc_ref_type`, `ref_doc_no`**, `ref_row=-1`, `calc_flag=1`, `set_ref_price=300` | — |
| **ใบสั่งจอง 34** (ขาย › ใบสั่งซื้อ/สั่งจอง อ้าง QT) | `ic_trans` + `ic_trans_detail` + `ap_ar_trans_detail` + `ic_trans_shipment` | `doc_ref_type=0`, **`ref_doc_no='QT26100001'`, `ref_row=-1`** (ไม่ใส่เลขบรรทัดต้นทาง), มี `wh_code/shelf_code`, `price_mode/price_type=null` | `calc_flag=1, trans_flag=34, billing_no='QT26100001'` (ไม่มี `bill_type`) |
| **ขายเชื่อ 44** (อ้าง BS) | เหมือน §6 + `ap_ar_trans_detail` | **`doc_ref_type=2`** (จากใบจอง), `ref_doc_no='BS26100001'`, **`ref_row=0`** | `calc_flag=-1, trans_flag=44, **bill_type=2**, billing_no='BS26100001'` + **แถวว่าง 2 แถว** (line 1, 2: `bill_type=0`, `billing_no=null`) ที่ไม่ถูกลบ |

- doc flow: หลังบันทึกใบจอง QT26100001 `used_status=1, doc_success=1` · หลังบันทึกบิล BS26100001 `used_status=1, doc_success=1` · บิล `used_status=0`
- ค่า `doc_ref_type` / `bill_type` ตรงกับที่ vault บันทึกไว้จากโค้ด: บิลอ้างใบจอง = 2 ([[write-spec-sale-order]] §1)
- **แถวว่างใน `ap_ar_trans_detail`:** transaction ของบิลนี้**ไม่มี** cleanup `delete from ap_ar_trans_detail where sum_debt_amount=0 … billing_no is null` (ต่างจากใบรับ/จ่ายชำระ) ⇒ เหลือแถว `trans_flag=44, billing_no=null` ในฐาน (AOY มี 2 แถวแบบนี้ = ของใบนี้) — query ที่นับแถว `ap_ar_trans_detail` ของบิลต้องกรอง `billing_no is not null`
- สต็อก AH-0001: 122 → 121, `book_out_qty` (ค้างจอง) สุดท้าย 0 (ใบจองปิดแล้ว)
- **สำหรับ sml_mcp_ai:** บิลอ้างใบจองต้องเขียน `doc_ref_type=2`, `ref_doc_no`, `ref_row` และแถวอ้างอิง `bill_type=2` · ใบจองอ้างใบเสนอราคาใช้ `ref_row=-1` ได้ (โปรแกรมทำแบบนั้น) — ไม่ต้องเขียนแถวว่าง
