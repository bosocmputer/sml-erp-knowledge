---
tags: [sml, sml_mcp_ai, write-spec, master, customer, verified-runtime]
status: verified-runtime รอบ 6.2 (สร้างลูกค้า + แก้ไข 3 ครั้ง) · รอบ 7.5 (สร้างผู้ขาย + แก้ไข 1 ครั้ง)
source: capture aoy-run6-2 (2026-10-26 13:46–13:49) + DB aoy + smlerp SMLERPTemplate/smldatabase.xml
---
# สเปกการบันทึก: ข้อมูลลูกค้า (ลูกหนี้) `ar_customer` / `ar_customer_detail`

กลับไป [[00-Index]] · สินค้า [[write-spec-master-product]] · ล็อกเอกสาร [[document-engine]] · ยังไม่ได้ทดสอบ [[00-Unverified]]

> หน้าจอ: ลูกหนี้ › ข้อมูลลูกหนี้ › กำหนดลูกหนี้ (`menu_ar_detail`, `SMLERPAR._ar`, เลขเมนู 7.1.1 ในรุ่น AccountPOSPro) · วันเครดิตอยู่แท็บ "รายละเอียดเพิ่มเติม"

## 1. สร้างลูกค้าใหม่ (13:47:45) — transaction เดียว
1. `insert into ar_customer (code, name_1, name_eng_1, address, province, amper, tambon, zip_code, country, telephone, fax, sms_phonenumber, email, ar_type, website, prefixname, price_level, first_name, last_name, birth_day, register_date, remark, ar_status, status, create_code, create_datetime=now())`
   - ค่าที่ได้: `price_level=0`, **`ar_status=1`** (ชนิดลูกค้า — ผู้ใช้เลือก "นิติบุคคล"; ร้าน AOY มี 0 = 12 ราย, 1 = 4 ราย), `status=0`, ช่องที่ไม่กรอก = null
2. `insert into ar_customer_detail (ar_code, tax_id='', card_id='', branch_type='0', branch_code='')` — **แถว detail แบบสั้น 5 คอลัมน์** (วันเครดิตยังไม่มี)
3. `COMMIT` → `master_logs` (`function_code=1` เพิ่ม, `menu_name='menu_ar_detail'`, `code`, `name_1`)
- ไม่มีตารางอื่น (ไม่สร้างผู้ติดต่อ, รายการสินค้าตามลูกค้า, cashier list)

## 2. แก้ไขลูกค้า (13:48:09, 13:48:21, 13:48:37 — ผู้ใช้เปิดแก้แล้วบันทึก 3 ครั้ง)
1. เปิด: **ล็อก** `update ar_customer set guid_code=<GUID> where code=?`
2. Transaction:
   - `delete from ar_contactor where ar_code=?`
   - `delete from ar_item_by_customer where ar_code=?`
   - `delete from ar_customer_cashier_list where ar_code=?`
   - `delete from ar_customer_detail where ar_code=?`
   - `update ar_customer set <ทุกคอลัมน์ของหัว> where code=?` (ไม่แตะ `create_*`)
   - `insert into ar_customer_detail` **แบบเต็ม 43 คอลัมน์**: `area_code, sale_code, trade_license, vat_license, tax_id, card_id, branch_type, branch_code, sale_type, set_tax_type, tax_type, tax_rate, account_code, discount_item, discount_bill, logistic_area, ap_code_ref, latitude, longitude, credit_money, credit_money_max, **credit_day**, credit_date, close_credit_date, disable_auto_close_credit, past_due_day, close_reason, close_over_credit_warning, credit_status, pay_bill_date, keep_chq_date, shipping_type, dimension_1..5, group_main, group_sub_1..4`
   - `COMMIT`
3. `master_logs` (`function_code=2` แก้ไข) → ปลดล็อก `guid_code=null`
- `credit_day` = 0 → 30 → 30.00 ตามที่ผู้ใช้แก้ · `close_credit_date` ครั้งแรกเป็น `'2026-10-30'` แล้วครั้งสุดท้ายเป็น null (ค่าในหน้าจอ) · `tax_id` จาก `''` (ตอนสร้าง) เป็น null (ตอนแก้)
- **แก้ไข = ลบตารางลูกทั้ง 4 แล้วใส่ใหม่** ⇒ ผู้ติดต่อ/รายการสินค้าตามลูกค้า/cashier list ที่ไม่อยู่ในหน้าจอตอนบันทึกจะหาย (รูปแบบเดียวกับบาร์โค้ด [[write-spec-master-product]] §6.1)

## 3. สำหรับ sml_mcp_ai
- สร้างลูกค้า: insert `ar_customer` + `ar_customer_detail` ใน transaction เดียว (ขั้นต่ำ 5 คอลัมน์ detail) + `master_logs`
- แก้ไข: ต้องอ่านตารางลูกทั้ง 4 แล้วเขียนกลับครบ (หรือ update เฉพาะคอลัมน์ ซึ่งต่างจากโปรแกรม — ตัดสินใน ADR) และล็อก/ปลดล็อก `guid_code`
- วันเครดิต/วงเงินอยู่ที่ `ar_customer_detail` ไม่ใช่ `ar_customer`

## 4. ยังไม่ทราบ
- ค่าอื่นของ `ar_status` นอกจาก 0/1 และป้ายบนจอ
- ลบลูกค้า, ลูกค้าที่มีเอกสารแล้วเปลี่ยนรหัส

## 5. ผู้ขาย (เจ้าหนี้) — ยืนยันจากรอบ 7.5 (ZZSUP-0001 สร้าง 15:26:48, แก้ไข 15:27:24 วันที่ 2026-10-26)
หน้าจอ: เจ้าหนี้ › ข้อมูลเจ้าหนี้ › กำหนดเจ้าหนี้ (`menu_ap_detail`, `SMLERPAP._ap`, เลขเมนู 6.1.1)
- **สร้าง:** `insert into ap_supplier (code, prefixname, firstname, lastname, name_eng_1, name_1, address, province, amper, tambon, zip_code, country, telephone, fax, email, ap_type, website, remark, status=0, ap_status=1, create_code, create_datetime=now())` → `insert into ap_supplier_detail (ap_code, tax_id='', card_id='', branch_type='0', branch_code='')` → `COMMIT` → `master_logs` (`function_code=1`, `menu_name=''`)
  - `firstname` = `name_1` (โปรแกรมคัดลอกชื่อให้) · `ap_status=1` ตามที่เลือกนิติบุคคล (เหมือน `ar_status`)
- **แก้ไข:** ล็อก `ap_supplier.guid_code` → transaction: **`update ap_supplier` ก่อน** → `delete ap_supplier_detail` → `insert ap_supplier_detail` (29 คอลัมน์: `staff_pay_code, payment_way, pay_bill_way, pay_condition, credit_purchase='0', discount_item, discount_bill, **credit_day='30'** (ส่งเป็นข้อความ), tax_id, card_id, branch_type, branch_code, set_tax_type, tax_type, tax_rate, shipping_type, account_code, lead_time, dimension_1..5, group_main, group_sub_1..4`) → `delete ap_contactor` → `delete ap_item_by_supplier` → `COMMIT` → ปลดล็อก
- ต่างจากลูกค้า: ลำดับ (ผู้ขาย update หัวก่อนลบลูก, ลูกค้าลบลูกก่อน) · ตารางลูก 3 ตาราง (`ap_supplier_detail`, `ap_contactor`, `ap_item_by_supplier`) — ไม่มี cashier list · ไม่มี `master_logs` ตอนแก้ไขในรอบนี้
- วันเครดิตอยู่ใน `ap_supplier_detail.credit_day` (แก้จากหน้าจอกำหนดเจ้าหนี้ได้)
