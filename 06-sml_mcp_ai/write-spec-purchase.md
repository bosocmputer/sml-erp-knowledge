---
tags: [sml, sml_mcp_ai, write-spec, purchase, verified-runtime]
status: verified-runtime (ซื้อเงินเชื่อไม่อ้างเอกสาร 1 ใบ รอบ 1; ใบสั่งซื้อ → ซื้อเงินเชื่อ รอบ 5.5) / from-code (ส่วนที่ระบุ)
source: capture aoy-run1 (PU26100001, 09:01–09:03) + DB aoy + smlerp SMLInventoryControl/_icTransControl.cs, _processThread.cs + smljavaws2 SMLICProcess.java
---
# สเปกการบันทึก: ซื้อสินค้าและค่าบริการ (trans_flag 12)

กลับไป [[00-Index]] · ฝั่งขายเทียบ [[write-spec-sale-invoice]] · สต็อก [[stock-cost]] · เจ้าหนี้ [[write-spec-ap-payment]]

> **ขอบเขต:** ซื้อ**เงินเชื่อ** (`inquiry_type=0`) ไม่อ้างใบสั่งซื้อ สินค้า 1 รายการ — PU26100001
> **ยังไม่ครอบคลุม:** ซื้อเงินสด (มี `cb_trans`?), ซื้อจากใบสั่งซื้อ (6), ซื้อพาเชียล (310/315), ส่งคืน/ลดหนี้ซื้อ (16/14), ค่าใช้จ่ายแฝง (`hidden_cost_1`), ภาษีนำเข้า, ล็อต/serial ตอนรับ

## 0. ลำดับเหตุการณ์จริง
| เวลา | ขั้น | transaction |
|---|---|---|
| 09:01:44.072–.281 | `erp_doc_format code='PU'` → `select doc_no from ic_trans where (doc_date >= '<ต้นปี>') and doc_no like ? AND trans_flag = 12 and trans_type = 1 …` | อ่าน |
| 09:01:44.497 | **ตรวจเลขใบกำกับซื้อซ้ำต่อผู้ขาย:** `select vat_doc_no from gl_journal_vat_buy where upper(vat_doc_no)=? and trans_flag=12 and upper(ap_code)=?` | อ่าน |
| 09:01:44–56 | ผู้ขาย: `ap_supplier` + `ap_supplier_detail` (`credit_day`, `set_tax_type`, `tax_type`, `tax_rate`, `discount_bill`, `discount_item`, `lead_time`) | อ่าน |
| 09:02:04 | สแกนบาร์โค้ด → `select ic_code, unit_code from ic_inventory_barcode where barcode=?` → คลังเริ่มต้น `ic_inventory_detail.start_purchase_wh, start_purchase_shelf, start_purchase_unit, discount, is_hold_purchase` + `ap_supplier_detail.discount_item` + คลังของผู้ใช้ `erp_user.ic_wht, ic_shelf` → `ic_unit_use.stand_value, divide_value` | อ่าน |
| 09:02:16–17 | `erp_company_profile`, `erp_option` | อ่าน |
| **09:02:17.897–.924** | **`BEGIN` → `ic_trans` → `ic_trans_detail` → `delete cb_trans_detail …` → `gl_journal_vat_buy` → `COMMIT`** | **1 transaction** |
| 09:02:18 | `logs` / `erp_logs` | แยก |
| 09:02:46 | พิมพ์ | อ่าน (block) |
| 09:02:48 | doc flow + `_process_stock_balance(item,"12")` + คิว `process` | หลาย transaction |

## 1. Transaction หลัก
### 1.1 `ic_trans` (38 คอลัมน์)
`trans_type=1` (ซื้อ), `trans_flag=12`, `status=0`, `doc_date`, `doc_time` (เวลาเปิดเอกสาร 09:01), `doc_no`, `doc_format_code='PU'`, **`cust_code` = รหัสผู้ขาย** (ใช้ช่องเดียวกับลูกค้า), `doc_ref`, `doc_ref_date`, `inquiry_type=0`, `vat_type=1`, `tax_doc_date`, **`tax_doc_no` = เลขใบกำกับของผู้ขาย** (ใบนี้ผู้ใช้ปล่อยค่า default = เลข PU), `wh_from`, `location_from`, `credit_day`, `credit_date`, `vat_rate`, `total_value` 260, `remark`, `discount_word`, `total_discount`, `advance_amount`, `total_before_vat` 242.99, `total_vat_value` 17.01, `total_after_vat`, `total_except_vat`, `total_amount` 260, `delivery_date`, `remark_2..5`, **`is_manual_vat=0`**, `is_pos=0`, `creator_code`, `create_datetime`
- ต่างจากบิลขาย: ไม่มี `contactor`, `sale_code`, `sale_group`, `send_*`, `cashier_code`, `user_approve`; มี `wh_from`, `location_from`, `delivery_date`, `is_manual_vat`

### 1.2 `ic_trans_detail` (59 คอลัมน์ ต่อบรรทัด)
ชุดเดียวกับบิลขาย ([[write-spec-sale-invoice]] §2.2) แต่ **`trans_type=1`, `calc_flag=1`** (สต็อกเข้า), `price_mode`/`price_type` = null, ไม่มี `set_ref_line`/`set_ref_qty`/`set_ref_price`
- ต้นทุนของบรรทัดซื้อ: worker (09:02:58) เขียน `update ic_trans_detail set sum_of_cost=242.99, sum_of_cost_1=242.99, average_cost=242.99, average_cost_1=242.99, profit_lost_cost_amount=0.0 where roworder=?` (= ราคาก่อน VAT) แล้ว `update ic_inventory set average_cost=225.64` (ถัวเฉลี่ยใหม่ของสินค้า) → `delete from process where roworder=?` → ตามด้วย `WITH COST_DATA AS (…)` (ยังไม่ได้ไล่ว่าอัปเดตอะไร)

### 1.3 `gl_journal_vat_buy` (32 คอลัมน์)
`book_code='', vat_calc=1, trans_type=1, trans_flag=12, doc_date, doc_no, ap_code, ref_doc_date, ref_doc_no, ref_vat_date, ref_vat_no, vat_date, vat_doc_no (= tax_doc_no), vat_new_number, vat_effective_period (10), vat_effective_year (2569 พ.ศ.), vat_description, vat_group, vat_base_amount (242.99), vat_rate (7.00), vat_amount (17.01), vat_total_amount (260.00), vat_except_amount_1 (0), vat_average (0), vat_type (0), is_add (0), ap_name, tax_no, branch_type (0), branch_code, manual_add (0), line_number (0)`
- ชื่อคอลัมน์ต่างจาก `gl_journal_vat_sale` (เช่น `vat_doc_no` แทน `vat_number`, `vat_base_amount` แทน `base_caltax_amount`, มี `vat_total_amount`, `vat_average`)

### 1.4 สิ่งที่**ไม่มี**ในซื้อเงินเชื่อ
`cb_trans` (ไม่จ่ายเงิน), `ap_ar_trans_detail` (ไม่อ้างเอกสาร), `ic_trans_shipment`, `ap_ar_trans`, GL (ไม่เปิด realtime)
- ⇒ **ยอดเจ้าหนี้คำนวณจากเอกสาร** แบบเดียวกับฝั่งลูกหนี้ ดู [[write-spec-ap-payment]]

## 2. หลัง commit
1. `logs`/`erp_logs` (`screen_code=12`)
2. พิมพ์ (block)
3. doc flow: reset `last_status` ของ 12 (`ic_trans_detail`, `ap_ar_trans_detail`) — ไม่มีเอกสารต้นทาง
4. `_process_stock_balance(item,"12")`: flag 12 อยู่ใน `_stockBalanceFlag` (เงื่อนไขค้างรับใน `SMLICProcess.java` รันเมื่อ flag อยู่ใน `_stockAccruedIn` **หรือ** `_stockBalanceFlag`) → `balance_qty` (CTE `stock`), `accrued_in_qty` (CTE `accin` — ค้างรับจากใบสั่งซื้อ 6), ค้างจอง/ส่ง → คิว `process` 'IC'
5. worker: ต้นทุนเฉลี่ยใหม่ + ล็อต (ถ้าสินค้าเป็น FIFO/lot)

## 3. สำหรับ sml_mcp_ai
- `preview_purchase`: ตรวจผู้ขาย (`ap_supplier`), สินค้า/หน่วย/คลัง (ค่าเริ่มต้นจาก `ic_inventory_detail.start_purchase_*`), **ตรวจเลขใบกำกับซ้ำต่อผู้ขาย** (ข้อ 0), คำนวณ VAT แบบหัวจากยอดรวม
- `commit_purchase`: transaction เดียว ข้อ 1.1–1.3 + SQL สต็อกส่วนที่ 1 (flag 12) + คิว `process` 'IC' + `logs`; หลัง commit `erp_logs`
- `is_hold_purchase` ของสินค้า (ระงับซื้อ) — ยังไม่ได้ไล่ว่าโปรแกรมห้ามหรือเตือน → ให้ preview ปฏิเสธไว้ก่อนจนกว่าจะยืนยัน

## 4. ยังไม่ทราบ
- ซื้อเงินสด: ตาราง `cb_trans` (`pay_type`?) — ยังไม่มี capture
- ซื้อจากใบสั่งซื้อ (6): `doc_ref_type` ของบรรทัด, `ap_ar_trans_detail.bill_type`, ผลต่อ `accrued_in_qty` และสถานะใบสั่งซื้อ
- `is_manual_vat=1` (แก้ VAT เอง) เขียนอะไรเพิ่ม
- `is_hold_purchase` ทำงานอย่างไร

## 5. ยืนยันจากรอบ 5.5: ใบสั่งซื้อ → ซื้อเงินเชื่อ (PO26100001 12:16:19, PU26100002 12:17:43 วันที่ 2026-10-26)
ผู้ขาย `AL-2604-0001` · 2 บรรทัด: `ZZTEST-0001` ชิ้น 2 × 10, `AH-0001` กล่อง 1 × 100 · ภาษีรวมใน 120 (ก่อนภาษี 112.15 + 7.85)

**ใบสั่งซื้อ (6, เมนู ซื้อ › ใบสั่งซื้อ)** — transaction เดียว: `ic_trans` → `ic_trans_detail` ต่อบรรทัด → `COMMIT` (ไม่มี `ap_ar_trans_detail`, `gl_journal_vat_buy`, `cb_trans`)
- `ic_trans` (40 คอลัมน์): `trans_type=1, trans_flag=6, doc_format_code='PO', cust_code, inquiry_type=0, vat_type=1, user_request=<ผู้ใช้>, approve_code=null, expire_day=0, expire_date, credit_day/date, send_day/date, total_*`, `doc_ref=null`
- `ic_trans_detail`: `trans_flag=6, calc_flag=1, doc_ref_type=0, ref_doc_no=null, **ref_row=-1**`, `wh_code/shelf_code` ตามค่าเริ่มต้น, `stand_value/divide_value=1`, `price_exclude_vat`, `sum_amount_exclude_vat`
- หลัง commit: ซ่อม `accrued_in_qty` (ค้างรับ) ของสินค้า + **ใส่คิว `process` 'IC'** แล้วคำนวณต้นทุนใหม่ทันที (ต้นทุนไม่เปลี่ยนเพราะใบสั่งซื้อไม่อยู่ในสูตร)

**ซื้อเงินเชื่อจากใบสั่งซื้อ (12, เมนู ซื้อ › ซื้อสินค้า/ตั้งหนี้, ประเภท "1.ซื้อสินค้าเงินเชื่อ" = `inquiry_type 0`)** — transaction เดียวกับ §1 + 1 ตาราง:
- `ic_trans`: เหมือน §1.1 (`doc_ref=null`, `tax_doc_no=<เลข PU>`, `advance_amount=0`, `is_manual_vat=0`)
- `ic_trans_detail`: **`ref_doc_no=<เลข PO>`, `ref_row=<line_number ของบรรทัด PO>` (0, 1)**, `doc_ref_type=0`, `hidden_cost_1=0`
- **`ap_ar_trans_detail` 1 แถว (แท็บเอกสารอ้างอิง):** `calc_flag=1, trans_type=1, trans_flag=12, doc_date, doc_no=<PU>, billing_no=<PO>, billing_date, remark, line_number=0` — ต่างจาก §1.4 (ซื้อไม่อ้างเอกสารไม่มีแถวนี้)
- `gl_journal_vat_buy`: `vat_calc=1`, ฐาน 112.15 ภาษี 7.85 รวม 120
- หลัง commit (~14 วินาทีหลัง commit — งานหลังบันทึกเริ่มหลังปิดหน้าพิมพ์): ซ่อมค้างรับ/จอง/ส่ง → คิว `process` → **doc flow: `PO26100001` `used_status=1, doc_success=1`** (รับครบทุกบรรทัด) → worker: เพิ่มล็อต `ic_trans_detail_lot` (lot `00016` ของ AH-0001), `ic_trans_detail.sum_of_cost/average_cost` ของบรรทัดซื้อ = ราคาก่อนภาษี (93.46, 18.69 → 9.35/ชิ้น), `ic_inventory.average_cost` AH-0001 228.39 → 227.30, ZZTEST-0001 0 → 9.35
- ตรวจ DB หลังบันทึก: `balance_qty` ZZTEST-0001 0 → 2, AH-0001 121 → 122 · `accrued_in_qty` = 0 ทั้งคู่ (รับครบ)
- **สำหรับ sml_mcp_ai:** ซื้ออ้างใบสั่งซื้อต้องเขียน `ref_doc_no` + `ref_row` ทุกบรรทัด **และ** แถว `ap_ar_trans_detail` อ้าง PO ไม่งั้นสถานะใบสั่งซื้อ/ค้างรับจะไม่ถูกปิด

## 6. ยืนยันจากรอบ 6.5 (2026-10-26): ซื้อเงินสด, ใบสั่งซื้อ, ซื้ออ้างใบสั่งซื้อรับบางส่วน
### 6.1 ซื้อเงินสด (PU00010002, 14:43:32) — ประเภท "2.ซื้อสินค้าเงินสด" = `inquiry_type 1`
- Transaction: `ic_trans` → `ic_trans_detail` → **`cb_trans`** (`doc_format_code='PU', pay_type=2, trans_type=1, trans_flag=12, total_amount = cash_amount = total_net_amount = total_amount_pay = 30`) → cleanup `cb_trans_detail` เลขว่าง (2 ครั้ง) → `COMMIT` · ไม่มี `cb_trans_detail` (เงินสดอย่างเดียว)
- ⚠️ **ใบนี้ออกเลขตอนวันที่เอกสารยังว่าง** (SQL หาเลข `doc_date >= '1900-01-01' and doc_no like 'PU0001%'` ⇒ `PU00010002` ต่อจาก `PU00010001` ของเดือน 4) และผลที่ตามมาในตาราง:
  - `ic_trans.doc_date='2026-10-26'` ถูกต้อง แต่ **`tax_doc_no=null`, `tax_doc_date=null`, `credit_date='1800-01-01'`**
  - **ไม่มี `gl_journal_vat_buy`** ⇒ ภาษีซื้อ 1.96 ไม่เข้ารายงานภาษีซื้อ
  - เทียบใน AOY: ใบซื้อปกติ 45 ใบ (เชื่อ 16, สด 29) มี `tax_doc_no` และ `gl_journal_vat_buy` ครบ · ใบ `PU0001…` 2 ใบ (PU00010001 เดือน 4, PU00010002) ไม่มีทั้งคู่ และ `credit_date` < 1900 ทั้งคู่
  - ⇒ **เลขเอกสารรูปแบบ `<รหัส>0001…` = สัญญาณว่าเอกสารถูกบันทึกโดยวันที่ว่างตอนออกเลข และอาจขาดข้อมูลภาษี** (เคย 3 ครั้ง: SIC00010001, PU00010001, PU00010002) — หน้าจอเคยแสดงช่องวันที่ไม่ครบ (`/2569`, `)`) ในรอบ 5.8 และ 6.3
### 6.2 ใบสั่งซื้อ (PO26100002, 14:45:05) — เหมือน §5
### 6.3 ซื้อเงินเชื่ออ้างใบสั่งซื้อ รับ 1 จาก 2 (PU26100003, 14:49:59)
- เหมือน §5: `ref_doc_no='PO26100002', ref_row=0`, แถวอ้างอิง `ap_ar_trans_detail billing_no=PO` + **แถวว่าง line 1 (`billing_no=null`) ค้างในฐาน** (เหมือนบิลขายอ้างใบจอง [[write-spec-sale-invoice]] §7)
- doc flow: **PO26100002 `used_status=1`, `doc_success=0`** (ยังรับไม่ครบ) · `ZZTEST-0001`: `balance_qty` 0 → 3 (ซื้อสด) → 4, **`accrued_in_qty`=1** (ค้างรับ), `average_cost` 9.35

## 7. ยืนยันจากรอบ 9.1: ส่งคืนสินค้าซื้อ (PT26100001 อ้าง PU26100002 คืน ZZTEST-0001 1 ชิ้น 10 บาท, 11:11:05 วันที่ 2026-10-27) — ใบแรกของ AOY
เมนู ซื้อ › ส่งคืนสินค้า/ราคาผิด (3.17) · ประเภท "1.ลดหนี้เจ้าหนี้, ลดสินค้า" = **`inquiry_type 0`**
- **Transaction (รูปแบบเดียวกับใบลดหนี้ขาย 48):** `ic_trans` → `ic_trans_detail` → `ap_ar_trans_detail` (+ แถวว่าง line 1) → `gl_journal_vat_buy` → `COMMIT`
- `ic_trans`: `trans_type=1, trans_flag=16, doc_format_code='PT', tax_doc_no=<PT>, inquiry_type=0, vat_type=1, total_amount=10, total_before_vat=9.35, total_vat_value=0.65, **ref_amount=120, ref_diff=10, ref_new_amount=110**`
- `ic_trans_detail`: **`calc_flag=-1`**, `doc_ref_type=1`, `ref_doc_no='PU26100002'`, `ref_row=0`, คลัง/ที่เก็บ/หน่วย, `qty=1, price=10`
- `ap_ar_trans_detail`: `calc_flag=-1, trans_type=1, trans_flag=16, bill_type=1, billing_no=<PU>, sum_debt_value=120, sum_debt_balance=120, sum_debt_amount=10, final_amount=110, sum_before_vat=112.15`
- **`gl_journal_vat_buy`: `vat_calc=-1`**, ฐาน 9.35 ภาษี 0.65
- ตรวจ DB: `ZZTEST-0001.balance_qty` 3 → 2 · PU26100002 `used_status=1` · ไม่มี `cb_trans` (ใบซื้อเชื่อ)
