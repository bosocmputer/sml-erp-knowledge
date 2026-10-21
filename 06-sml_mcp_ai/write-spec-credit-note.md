---
tags: [sml, sml_mcp_ai, write-spec, credit-note]
status: verified-runtime รอบ 4 สำหรับรับคืนจากขายเงินเชื่อ (inquiry_type 0) · ประเภทอื่น from-code
source: DB aoy/kbgtest/samai/debug_kbgds_data1 (2026-10-21, นับ/โครงสร้างเท่านั้น) + smlerp _icTransScreenTopControl.cs, SMLProcess/_docFlowThread.cs, smljavaws2 SMLICProcess.java + query จริงที่ capture ได้จากเอกสารอื่น
---
# สเปกการบันทึก: รับคืนสินค้า / ลดหนี้ (trans_flag 48)

กลับไป [[00-Index]] · บิลขาย [[write-spec-sale-invoice]] · รับชำระ [[write-spec-receipt]] · ยกเลิก [[write-spec-cancel]]

> ✅ รอบ 4 ยืนยันรับคืนจากขายเงินเชื่อ 2 ใบ (§0) · ⚠️ ประเภทอื่นยังเป็นข้อมูลจากแถวที่บันทึกไว้แล้ว + โค้ด

## 1. ประเภท (`inquiry_type`) — ป้ายจาก `SMLERPTemplate/smldatabase.xml`, ลำดับจาก `_icTransScreenTopControl.cs` ~1712
| ค่า | ความหมาย | กระทบสต็อก | นับในยอดลูกหนี้ |
|---|---|---|---|
| 0 | รับคืนจากขายเงินเชื่อ | ✅ | ✅ (หัก) |
| 1 | รับคืนจากขายเงินสด | ✅ | — (คืนเงินผ่าน `cb_trans`) |
| 2 | ลดหนี้จากขายเงินเชื่อ (ไม่กระทบสต๊อก) | — | ✅ (หัก) |
| 3 | ลดหนี้จากขายเงินสด (ไม่กระทบสต๊อก) | — | — |
| 4 | รับคืนจากขายสินค้าเงินเชื่อ (สินค้าบริการ) | (สูตรสต็อกตัดเฉพาะ `inquiry_type > 1` ⇒ 4 ถูกตัดออก) | ✅ (หัก) |
| 5 | รับคืนจากขายสินค้าเงินสด (สินค้าบริการ) | ถูกตัดออกเหมือน 4 | — |
- "กระทบสต็อก": สูตรยอดคงเหลือ `and not (trans_flag = 48 and inquiry_type > 1)` ([[stock-cost]]) · "นับในยอดลูกหนี้": SQL ยอดลูกหนี้จริง `trans_flag=48 and inquiry_type in (0,2,4)` ([[write-spec-sale-invoice]] §1.3, [[write-spec-receipt]] §1)
- การใช้จริง: aoy 0 = 7, 1 = 16 · kbgtest 0 = 4,715, 1 = 109, 2 = 18,592, 3 = 44, 4 = 2, 5 = 1 · samai 0 = 2,551, 1 = 330, 2 = 151

## 2. ตารางที่มีแถว (จากข้อมูลที่โปรแกรมบันทึกไว้)
| ตาราง | สิ่งที่เห็น | aoy (23 ใบ) | kbgtest (23,463) | samai (3,032) |
|---|---|---|---|---|
| `ic_trans` | หัว; **`doc_ref` ส่วนใหญ่ว่าง** (การอ้างบิลอยู่ที่บรรทัด) | doc_ref 0 | 91 (82 ชี้ไป 44) | 2,949 (46 ชี้ไป 44) |
| `ic_trans_detail` | **`calc_flag = 1`** (สต็อกเข้า) ทุกบรรทัด; อ้างบิลด้วย **`doc_ref_type = 1`, `ref_doc_no` = เลขบิล, `ref_row`** | 23 ใบ, `1/ref` ทุกบรรทัด | 1/ref 47,269 · 0/ref 25 · 0/noref 41 | 1/ref 3,372 · 0/noref 921 · 0/ref 62 |
| `ap_ar_trans_detail` | ตารางเอกสารอ้างอิง: **`bill_type = 1`**, `billing_no` = เลขบิล, `sum_debt_amount` = ยอด CN | 23 (bill_type 1) | 23,444 (bill_type 1: 29,561 แถว, 93: 183) | 2,709 |
| `cb_trans` | **เฉพาะคืนเงินสด** (`inquiry_type` 1): `pay_type = 2` (บิลขาย/รับชำระใช้ 1) | 16 | 155 | 330 |
| `gl_journal_vat_sale` | ภาษีขายฝั่งลดหนี้; `is_add = 0` ทุกแถว; `vat_calc` = **−1** ส่วนใหญ่ (CN26100001 เป็น 1 — ยังไม่ทราบเหตุ); `ref_doc_no`/`ref_vat_no` ว่างใน aoy | 22 | 23,459 | 1,881 |
- ต้นทุนของบรรทัด CN (`sum_of_cost`) มีค่า (เช่น 149.53, 300.08) ⇒ ถูกคำนวณโดย worker เหมือนบิลขาย
- `doc_reason` ว่างทุกใบในทุกร้าน (โค้ดใส่ `doc_reason` จาก combobox เมื่อ `_myGlobal._isVatPresent` — `_icTransControl.cs` ~14953 กลุ่ม case ลดหนี้)

## 3. ผลต่อเอกสารต้นทาง (doc flow, `_docFlowThread.cs` ~141)
- บิลขาย 44 ที่ถูกบรรทัด 46/48 (`last_status=0`) อ้าง `ref_doc_no` → **`used_status = 1`** (ยืนยัน aoy: INV26090002/03/04 `used_status=1`)
- 44, 46, **48** ที่ถูกใบวางบิล 235 / รับชำระ 239 อ้าง → `used_status_2 = 1` (CN ถูกนำไปหักในใบรับชำระได้ — ในใบรับชำระ CN ปรากฏเป็นยอดติดลบ [[write-spec-receipt]] §1)
- บิลที่ `used_status=1` แล้ว **ยกเลิกด้วย 45 ไม่ได้** ([[write-spec-cancel]] A.1)

## 4. งานสต็อก
- flag 48 อยู่ใน `_stockBalanceFlag` (`SMLICProcess.java`) → `_process_stock_balance(items,"48")` คำนวณ `balance_qty` ใหม่ + คิว `process` 'IC' (from-code)
- ยกเลิก CN (49) → `_processThread` แปลงเป็น 48 ก่อนเรียก (เหมือนยกเลิกบิล)

## 5. สำหรับ sml_mcp_ai
- `commit_credit_note` เปิดได้**เฉพาะรับคืนจากขายเชื่อ (inquiry_type 0)** ตาม §0 · ประเภท 1–5 ยังไม่เปิดจนกว่าจะ capture (โดยเฉพาะ 2 = ลดหนี้ไม่กระทบสต็อก)
- `preview_credit_note` ทำได้แล้ว (อ่านอย่างเดียว): ตรวจบิลต้นทาง `last_status=0`, จำนวนรับคืนต่อบรรทัด ≤ จำนวนขายที่ยังไม่ถูกคืน, เลือก `inquiry_type` ให้ตรงกับประเภทบิล (เชื่อ 0/2/4, สด 1/3/5)

## 6. ยังไม่ทราบ
- ลำดับ SQL และคอลัมน์ครบชุดของ `ic_trans`/`ic_trans_detail`/`ap_ar_trans_detail`/`cb_trans`/`gl_journal_vat_sale` ตอนบันทึก 48
- `vat_calc` 1 กับ −1 ต่างกันอย่างไร
- `ap_ar_trans_detail.bill_type = 1` ในใบลดหนี้หมายถึงอะไร (ใบสั่งขายใช้ 3, ใบรับชำระใช้ trans_flag ของบิล)
- จำนวนรับคืนเกินจำนวนขายถูกห้ามด้วยตัวเลือกใด (`check_qty_over_doc_ref` = 0 ใน aoy)

## 0. ยืนยันจากรอบ 4: รับคืนจากขายเงินเชื่อ (CN26100002 16:17:27, CN26100003 16:19:53 — อ้าง BF-INV26100035 ทั้งสองใบ)
**Transaction เดียว:** `ic_trans` (38 คอลัมน์) → `ic_trans_detail` ต่อบรรทัด (62 คอลัมน์) → `ap_ar_trans_detail` (14 คอลัมน์) → `gl_journal_vat_sale` (29 คอลัมน์) → `COMMIT` — **ไม่มี `cb_trans`** (ขายเชื่อ) และไม่มี `ic_trans_shipment`
- `ic_trans`: `trans_type=2, trans_flag=48, doc_format_code='CN', tax_doc_no=tax_doc_date=<เลข/วันที่ CN>, doc_ref=null, sale_code, inquiry_type=0, vat_type, credit_day/date, vat_rate, total_value, total_discount, total_before_vat, total_vat_value, total_after_vat, total_except_vat, total_amount, remark_2..5, is_pos=0, …` และ **3 คอลัมน์เฉพาะใบลดหนี้**:
  | คอลัมน์ | CN26100002 | CN26100003 | ความหมาย (จากค่าจริง 2 ใบ) |
  |---|---|---|---|
  | `ref_amount` | 318.00 | 18.00 | มูลค่าบิลก่อนลดครั้งนี้ (หักใบลดหนี้ก่อนหน้าแล้ว) |
  | `ref_diff` | 300.00 | 18.00 | ยอดลดครั้งนี้ |
  | `ref_new_amount` | 18.00 | 0 | มูลค่าบิลหลังลด |
- `ic_trans_detail`: **`calc_flag=1`**, `doc_ref_type=1`, `ref_doc_no=<บิล>`, **`ref_row=<line_number ของบรรทัดบิล>`** (0 และ 1), `price_mode/price_type=null`, `set_ref_price=0`
- `ap_ar_trans_detail` (14): `calc_flag=-1, trans_type=2, trans_flag=48, doc_date, doc_no, bill_type=1, billing_no=<บิล>, billing_date, sum_debt_value, sum_debt_balance, sum_debt_amount, final_amount, sum_before_vat, line_number`
  | คอลัมน์ | CN26100002 | CN26100003 | ความหมาย |
  |---|---|---|---|
  | `sum_debt_value` | 318 | 318 | มูลค่าบิลเดิม |
  | `sum_debt_balance` | 318 | 18 | มูลค่าคงเหลือก่อนลดครั้งนี้ (= `ref_amount`) |
  | `sum_debt_amount` | 300 | 18 | ยอดลดครั้งนี้ (= `ref_diff`) |
  | `final_amount` | 18 | 0 | มูลค่าหลังลด (= `ref_new_amount`) |
  | `sum_before_vat` | 297.20 | 297.20 | ฐานภาษีของบิลเดิม (318 / 1.07) |
- `gl_journal_vat_sale`: **`vat_calc=-1`** ทั้ง 2 ใบ (ฐาน/ภาษี 280.37/19.63 และ 16.82/1.18), `vat_number`=เลข CN, `ref_doc_no/ref_vat_no` = null
- หลัง commit (CN26100002): `logs` → สต็อกของสินค้าที่รับคืน (flag 48: `balance_qty`, ค้างทุกแบบ) → คิว `process` → doc flow: **บิล `used_status=1`** (16:17:31) + reset `last_status` ของ 44 และ 48 → worker คำนวณต้นทุน (`sum_of_cost` ของบรรทัด CN26100002 = 149.53)
- รอบ 4 ผู้ใช้เลือก inquiry 0 ทั้งสองใบ (แผนเดิมให้ใบที่ 2 เป็น inquiry 2) ⇒ **ลดหนี้ไม่กระทบสต็อก (2) ยังไม่ได้ยืนยัน**
