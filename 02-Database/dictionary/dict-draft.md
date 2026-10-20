---
tags: [sml, dictionary, draft, generated]
module: Draft
---
# พจนานุกรม: Draft — ร่างเอกสาร

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ap_ar_trans_detail_draft]] | รายการอ้างอิง(ร่าง) / AP AR Trans Detail Draft | 73 |
| [[#cb_trans_detail_draft]] | รายละเอียดการจ่ายเงิน (แบบร่าง) / CB Trans Detrail Draft | 70 |
| [[#erp_request_order]] | รายการขออนุมัติ / Request Order | 7 |
| [[#ic_trans_detail_draft]] | รายละเอียดรายวัน(ร่าง) / IC Trans Detail Draft | 191 |
| [[#ic_trans_draft]] | รายวัน(ร่าง) / IC Trans Draft | 343 |

## ap_ar_trans_detail_draft

**รายการอ้างอิง(ร่าง)** — AP AR Trans Detail Draft

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(255) | ✓ |
| `billing_no` | เอกสารเลขที่ | Billing No | varchar(25) | ✓ |
| `billing_date` | เอกสารวันที่ | Billing Date | smalldatetime | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `sum_debt_value` | รวมมูลค่า | Sum Value | float | ✓ |
| `sum_tax_value` | มูลค่าภาษี | Sum Tax Value | float | ✓ |
| `sum_debt_amount` | จำนวนเงิน | Sum Debt Amount | float | ✓ |
| `sum_discount` | ส่วนลด | Sum Discount | float | ✓ |
| `sum_after_discount` | ยอดหนี้หลังหักส่วนลด | Sum After Discount | float | ✓ |
| `sum_pay_money_cash` | รับ/จ่ายชำระหนี้ (เงินสด) | Sum Pay Money (Cash) | float | ✓ |
| `sum_pay_money_chq` | รับ/จ่ายชำระหนี้ (เช็ค) | Sum Pay Money (Cheque) | float | ✓ |
| `sum_pay_money_credit` | รับ/จ่ายชำระหนี้ (บัตรเครดิต) | Sum Pay Money (Credit Card) | float | ✓ |
| `sum_pay_money_transfer` | รับ/จ่ายชำระหนี้ (เงินโอน) | Sum Pay Money (Transfer) | float | ✓ |
| `sum_debt_balance` | ยอดหนี้คงเหลือ | Sum Debt Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | smallint | ✓ |
| `doc_ref_requisition` | เลขที่ใบเบิกสินค้า *(resource only)* |  | char |  |
| `doc_ref_purchase` | เลขที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_ref_purchase_date` | วันที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_ref_requisition_date` | วันที่ใบเบิกสินค้า *(resource only)* |  | char |  |
| `doc_ref_purchase_order` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_purchase_order_date` | วันที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ *(resource only)* |  | char |  |
| `bill_type` | ประเภทรายวัน | Bill Type | smallint | ✓ |
| `doc_ref_quotation` | เลขที่ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_ref_quotation_date` | วันที่ใบเสนอราคา *(resource only)* |  | char |  |
| `sum_pay_money` | ยอดชำระ | Pay Money | float | ✓ |
| `sum_before_vat` | ยอดก่อนภาษี | Sum Debt Tax | float | ✓ |
| `doc_ref_debt_billing_ap` | เลขใบรับวางบิล (เจ้าหนี้) *(resource only)* |  | char |  |
| `doc_ref_debt_billing_ar` | ใบวางบิล (ลูกหนี้) *(resource only)* |  | char |  |
| `sum_value` | มูลค่าสินค้า |  | float | ✓ |
| `balance_ref` | ยอดคงเหลือ |  | float | ✓ |
| `vat_rate` | อัตราภาษี |  | float | ✓ |
| `sum_pay_money_1` | จำนวนเงินวางบิล *(resource only)* |  | char |  |
| `description` | รายละเอียด *(resource only)* |  | char |  |
| `bill_type_name` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `doc_ref_pr_approval` | เลขที่ใบอนุมัติเสนอซื้อ *(resource only)* |  | char |  |
| `ref_amount_debit` | มูลค่าเพิ่มหนี้ *(resource only)* |  | char |  |
| `ref_amount_credit` | มูลค่าลดหนี้ *(resource only)* |  | char |  |
| `final_amount` | มูลค่าที่ถูกต้อง |  | float | ✓ |
| `last_status` | สถานะล่าสุด |  | smallint | ✓ |
| `calc_flag` | (1,-1) |  | smallint | ✓ |
| `doc_ref_partial` | เลขที่ใบรับ *(resource only)* |  | char |  |
| `doc_ref_partial_date` | วันที่ใบรับ *(resource only)* |  | char |  |
| `ref_doc_no` | เลขที่เอกสารอ้างอิงบิล |  | varchar(255) | ✓ |
| `ref_doc_date` | วันที่เอกสารอ้างอิงบิล |  | smalldatetime | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `doc_ref_po_requrest` | เลขที่ใบเสนอซื้อ *(resource only)* |  | char |  |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `doc_ref_pre_requisition` | เลขที่ใบขอเบิก *(resource only)* |  | char |  |
| `doc_ref_product_deposit` | เลขที่ใบฝากสินค้า *(resource only)* |  | char |  |
| `bill_tax_no` | เลขที่ใบกำกับภาษี |  | varchar(255) | ✓ |
| `bill_tax_date` | วันที่ใบกำกับภาษี |  | smalldatetime | ✓ |
| `receipt_doc_no` | เลขที่ใบเสร็จ *(resource only)* |  | char |  |
| `receipt_doc_date` | วันที่ใบเสร็จ *(resource only)* |  | char |  |
| `sum_debt_amount_2` | จำนวนเงิน |  | float | ✓ |
| `balance_ref_2` | ยอดคงเหลือ |  | float | ✓ |
| `sum_pay_money_2` | ยอดชำระ |  | float | ✓ |
| `lost_profit_exchange_amount` | กำไรขาดทุนจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `exchange_rate_old` | อัตราแลกเปลี่ยนเดิม |  | float | ✓ |

## cb_trans_detail_draft

**รายละเอียดการจ่ายเงิน (แบบร่าง)** — CB Trans Detrail Draft

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `trans_number` | เลขที่เช็ค | Chq Number | varchar(100) | ✓ |
| `chq_ref` | อ้างอิงเช็คเลขที่ | Chq Reference | varchar(25) | ✓ |
| `credit_card_no` | เลขที่บัตรเครดิต *(resource only)* | Credit Card No | varchar(25) |  |
| `petty_cash_code` | รหัสเงินสดย่อย *(resource only)* | Petty Cash Code | varchar(25) |  |
| `pass_book_code` | สมุดเงินฝาก | Pass Book Code | varchar(25) | ✓ |
| `bank_code` | รหัสธนาคาร | Bank Code | varchar(25) | ✓ |
| `bank_branch` | สาขาธนาคาร | Bank Branch | varchar(100) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `amount` | จำนวนเงิน | Amount | float | ✓ |
| `fee_amount` | ค่าธรรมเนียม | Fee Amount | float | ✓ |
| `other_amount` | ค่าใช้จ่ายอื่นๆ | Other Amount | float | ✓ |
| `tax_at_pay` | ภาษีหัก ณ ที่จ่าย | Tax At Pay | float | ✓ |
| `sum_amount` | ยอดเงินรวม | Sum Amount | float | ✓ |
| `period_number` | งวดที่ | Period Number | tinyint | ✓ |
| `approve_code` | กลุ่มผู้อนุมัติ | Approve User GRoup | varchar(100) | ✓ |
| `approve_date` | วันที่อนุมัติ | Approve Date | smalldatetime | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | smallint | ✓ |
| `description` | รายละเอียด *(resource only)* | description | varchar(100) |  |
| `chq_date` | วันที่ออกเช็ค/รับเช็ค |  | smalldatetime | ✓ |
| `chq_due_date` | วันที่บนเช็ค |  | smalldatetime | ✓ |
| `no_approved` | เลขที่อนุมัติ |  | varchar(25) | ✓ |
| `credit_card_type` | ประเภทบัตรเครดิต |  | varchar(25) | ✓ |
| `charge` | ยอด Charge |  | float | ✓ |
| `chq_number` | เลขที่เช็ค *(resource only)* |  | char |  |
| `doc_type` | 1=เงินโอน,2=เช็ค,3=บัตรเครดิต,4=เงินสดย่อย,5=เงินล่วงหน้า,9=คูปอง,11=จ่ายอื่น,12=รับอื่น,19=สกุลเงินอื่น,21=eWallet |  | smallint | ✓ |
| `deposit_no` | เลขที่เงินล่วงหน้า *(resource only)* |  | char |  |
| `advance_no` | เลขที่เงินมัดจำ *(resource only)* |  | char |  |
| `deposit_amount` | ยอดเงินล่วงหน้า *(resource only)* |  | char |  |
| `advance_amount` | ยอดเงินมัดจำ *(resource only)* |  | char |  |
| `balance_amount` | ยอดคงเหลือ |  | float | ✓ |
| `deposit_pay` | ยอดตัดเงินล่วงหน้า *(resource only)* |  | char |  |
| `advance_pay` | ยอดตัดเงินมัดจำ *(resource only)* |  | char |  |
| `doc_date_ref` | วันที่อ้างอิง |  | smalldatetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `trans_number_type` | ประเภท (1=รับ,2=จ่าย) |  | smallint | ✓ |
| `ap_ar_type` | (1=ลูกหนี้,2=เจ้าหนี้) |  | smallint | ✓ |
| `ap_ar_code` | รหัสเจ้าหนี้/ลูกหนี้ |  | varchar(25) | ✓ |
| `last_status` | สถานะ |  | smallint | ✓ |
| `coupon_number` | เลขที่คูปอง *(resource only)* |  | smallint |  |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `transfer_date` | วันที่โอน *(resource only)* |  | char |  |
| `chq_amount` | มูลค่าเช็ค *(resource only)* | Cheque Amount | char |  |
| `external_chq` | การเรียกเก็บ |  | smallint | ✓ |
| `internal_cheque` | เช็คในเขต *(resource only)* |  | char |  |
| `external_cheque` | เช็คนอกเขต *(resource only)* |  | char |  |
| `chq_on_hand` | ประเภทเช็ค |  | smallint | ✓ |
| `new_chq` | เช็คฉบับใหม่ *(resource only)* |  | char |  |
| `old_chq` | ตัดยอดจากฉบับเดิม *(resource only)* |  | char |  |
| `income_code` | รหัสรายได้ *(resource only)* |  | char |  |
| `expense_code` | รหัสค่าใช้จ่าย *(resource only)* |  | char |  |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `currency_name` | ชื่อสกุลเงิน *(resource only)* | Currency Name | char |  |
| `is_doc_copy` | เป็นเอกสารออกแทน |  | smallint | ✓ |
| `transection_number` | เลขที่รายการ *(resource only)* |  | char |  |
| `ref1` | เลขที่อ้างอิง 1 |  | varchar(50) | ✓ |
| `ref2` | เลขที่อ้างอิง 2 |  | varchar(50) | ✓ |
| `sum_amount_2` | รวมจำนวนเงิน |  | float | ✓ |
| `ar_name` | ลูกค้า *(resource only)* |  | char |  |
| `lost_profit_exchange_amount` | กำไรขาดทุนจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `exchange_rate_old` | อัตราแลกเปลี่ยนเดิม |  | float | ✓ |
| `amount_2` | จำนวนเงิน |  | float | ✓ |
| `charge_2` | ยอด Charge |  | float | ✓ |

## erp_request_order

**รายการขออนุมัติ** — Request Order

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | Flag |  | smallint |  |
| `trans_type` | Type |  | smallint |  |
| `doc_no` | Ref No |  | varchar(50) |  |
| `req_datetime` | Request Datatime |  | datetime |  |
| `approve_code` | OTP |  | varchar(50) |  |
| `send_success` | Send Success |  | smallint | ✓ |
| `cust_code` | Cust Code |  | varchar(50) | ✓ |

## ic_trans_detail_draft

**รายละเอียดรายวัน(ร่าง)** — IC Trans Detail Draft

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `cust_code` | ลูกหนี้/เจ้าหนี้ | AP/AR Code | varchar(25) | ✓ |
| `inquiry_type` | ประเภทการซื้อ | Inquiry Type | smallint | ✓ |
| `item_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `item_name` | ชื่อสินค้า | Item Name | varchar(255) | ✓ |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `cost` | ต้นทุน *(resource only)* | Cost | float |  |
| `qty` | จำนวน | Qty | float | ✓ |
| `price` | ราคา | Price | float | ✓ |
| `discount` | ส่วนลด | Discount | varchar(25) | ✓ |
| `sum_of_cost` | รวมต้นทุน | Sum of Cost | float | ✓ |
| `sum_amount` | รวมมูลค่า | Sum Amount | float | ✓ |
| `due_date` | วันที่ต้องการ | Due Date | smalldatetime | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |
| `ref_doc_no` | อ้างอิง | Ref Doc No | varchar(25) | ✓ |
| `ref_doc_date` | อ้างอิง วันที่ | Ref Date | smalldatetime | ✓ |
| `ref_line_number` | อ้างอิง บรรทัด | Ref Line Number | int | ✓ |
| `ref_cust_code` | อ้างอิง เจ้าหนี้/ลูกหนี้ | Ref Cust Code | varchar(25) | ✓ |
| `branch_code` | สาขา | Branch Code | varchar(25) | ✓ |
| `wh_code` | คลัง | Warehouse | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ | Shelf | varchar(25) | ✓ |
| `wh_code_2` | คลัง | Warehouse | varchar(25) | ✓ |
| `shelf_code_2` | พื้นที่เก็บ | Shelf | varchar(25) | ✓ |
| `department_code` | แผนกที่ขออนุมัติ | Department Code | varchar(25) | ✓ |
| `approval_qty` | จำนวนอนุมัติ *(resource only)* | Approval Qty | float |  |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `cancel_qty` | จำนวนยกเลิก | Cancel Qty | float | ✓ |
| `total_qty` | จำนวนคงเหลือ | Total Qty | float | ✓ |
| `stand_value` | ตัวตั้ง | Stand Value | float | ✓ |
| `divide_value` | ตัวหาร | Divide Value | float | ✓ |
| `ratio` | อัตราส่วน | Ratio | float | ✓ |
| `dimension` | มิติ *(resource only)* | Dime | char |  |
| `ic_pattern` | รูปแบบสินค้า | Pattern | varchar(25) | ✓ |
| `ic_color` | สีสินค้า | Color | varchar(25) | ✓ |
| `ic_size` | ขนาดสินค้า | Size | varchar(25) | ✓ |
| `approval_unit` | หน่วยนับที่ใช้ *(resource only)* | Unit Use | varchar(25) |  |
| `extra` | เพิ่มเติม *(resource only)* | Extra | char |  |
| `priority_level` | ความสำคัญ | Priority | int | ✓ |
| `priority_level_1` | ปรกติ *(resource only)* | Normal | char |  |
| `priority_level_2` | ด่วน *(resource only)* | Level 1 | char |  |
| `priority_level_3` | ด่วนมาก *(resource only)* | Level 2 | char |  |
| `priority_level_4` | ด่วนมากพิเศษ *(resource only)* | Level 3 | char |  |
| `check_stock_1` | ยอดที่ตรวจนับได้ *(resource only)* |  | char |  |
| `check_stock_2` | ผลต่าง *(resource only)* |  | char |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* |  | char |  |
| `wh_name` | ชื่อคลัง *(resource only)* |  | char |  |
| `shelf_name` | ชื่อพื้นที่เก็บ *(resource only)* |  | char |  |
| `unit_type` | ประเภทหน่วยนับ *(resource only)* |  | char |  |
| `calc_flag` | บวกหรือลบ (1=บวก,-1=ลบ) |  | int | ✓ |
| `last_status` | สถานะล่าสุด (0=Normal,1=ยกเลิก) |  | int | ✓ |
| `wh_name_out` | จากคลัง *(resource only)* |  | char |  |
| `shelf_name_out` | จากที่เก็บ *(resource only)* |  | char |  |
| `wh_name_in` | เข้าคลัง *(resource only)* |  | char |  |
| `shelf_name_in` | เข้าที่เก็บ *(resource only)* |  | char |  |
| `doc_ref_requisition` | เลขที่ใบเบิก *(resource only)* |  | char |  |
| `wh_name_2` | ชื่อคลัง *(resource only)* |  | char |  |
| `shelf_name_2` | ชื่อพื้นที่เก็บ *(resource only)* |  | char |  |
| `set_ref_line` | บรรทัดอ้างอิง (สินค้าชุด) |  | varchar(40) | ✓ |
| `set_ref_price` | ราคาอ้างอิง (สินค้าชุด) |  | float | ✓ |
| `set_ref_qty` | จำนวนอ้างอิง (สินค้าชุด) |  | float | ✓ |
| `item_type` | ประเภทสินค้า |  | int | ✓ |
| `doc_ref_purchase_order` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_sale_order` | เลขที่ใบเสนอราคา *(resource only)* |  | char |  |
| `vat_type` | ประเภทภาษี (0=แยกนอก,1=รวมใน,2=อัตรา 0) |  | int | ✓ |
| `doc_ref_purchase` | เลขที่ใบซื้อสินค้า/สินค้าบริการ *(resource only)* |  | char |  |
| `doc_ref_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `item_code_main` | สินค้าหลัก |  | varchar(25) | ✓ |
| `ref_row` | ref_row |  | smallint | ✓ |
| `ref_guid` | ref_guid |  | varchar(40) | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `is_permium` | 1=ของแถม |  | smallint | ✓ |
| `is_get_price` | ให้ดึงราคาขาย (1=ดึง) |  | smallint | ✓ |
| `average_cost` | ราคาทุนเฉลี่ย |  | float | ✓ |
| `sum_amount_exclude_vat` | รวมมูลค่า |  | float | ✓ |
| `doc_date_calc` | วันที่สำหรับคำนวณ |  | smalldatetime | ✓ |
| `doc_time_calc` | เวลาสำหรับคำนวณ |  | varchar(5) | ✓ |
| `profit` | กำไรขั้นต้น *(resource only)* |  | char |  |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |
| `price_exclude_vat` | ราคาไม่รวมภาษี |  | float | ✓ |
| `ar_detail` | รายละเอียดลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `ap_detail` | รายละเอียดเจ้าหนี้ *(resource only)* |  | char |  |
| `vat_type_word` | ประเภทภาษี *(resource only)* |  | char |  |
| `user_approve` | รหัสผู้อนุมัติ |  | varchar(25) | ✓ |
| `price_type` | ประเภทราคา |  | smallint | ✓ |
| `price_mode` | กลุ่มราคา |  | smallint | ✓ |
| `approval_price` | ราคาอนุมัติ *(resource only)* |  | float |  |
| `temp_float_1` | ตัวเลข 1 |  | float | ✓ |
| `temp_float_2` | ตัวเลข 2 |  | float | ✓ |
| `temp_string_1` | ตัวอักษร 1 |  | varchar(25) | ✓ |
| `po_qty` | จำนวนสั่งซื้อ *(resource only)* |  | char |  |
| `po_qty_2` | จำนวนสั่งซื้อคงเหลือ *(resource only)* |  | char |  |
| `doc_ref_receive_no` | เลขที่ใบรับ *(resource only)* |  | char |  |
| `approval_sum_amount` | มูลค่าอนุมัติ *(resource only)* |  | char |  |
| `approval_discount` | ส่วนลดอนุมัติ *(resource only)* |  | char |  |
| `expense_code` | รหัสค่าใช้จ่าย *(resource only)* |  | char |  |
| `expense_name` | ชื่อค่าใช้จ่าย *(resource only)* |  | char |  |
| `detail` | คำอธิบายรายการ *(resource only)* |  | char |  |
| `amount2` | จำนวนเงิน *(resource only)* |  | char |  |
| `average_cost_stand` | หน่วยต้นทุนตัวตั้ง *(resource only)* |  | char |  |
| `average_cost_div` | หน่วยต้นทุนตัวหาร *(resource only)* |  | char |  |
| `serial_number` | หมายเลขเครื่อง *(resource only)* |  | char |  |
| `income_code` | รหัสรายได้ *(resource only)* |  | char |  |
| `income_name` | ชื่อรายได้ *(resource only)* |  | char |  |
| `is_serial_number` | มีหมายเลขเครื่อง |  | smallint | ✓ |
| `cash_sub_code` | รหัสเงินสดย่อย *(resource only)* |  | char |  |
| `cash_sub_name` | ชื่อเงินสดย่อย *(resource only)* |  | char |  |
| `book_bank_code` | สมุดเงินฝาก *(resource only)* |  | char(25) |  |
| `bank_name` | ธนาคาร |  | varchar(25) | ✓ |
| `bank_branch` | สาขา |  | varchar(25) | ✓ |
| `chq_number` | เลขที่เช็ค |  | varchar(100) | ✓ |
| `chq_flag` | สถานะ *(resource only)* |  | smallint |  |
| `expense` | ค่าใช้จ่าย *(resource only)* |  | char |  |
| `credit_card_no` | เลขที่บัตรเครดิต *(resource only)* |  | char |  |
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `discount_number` | หมายเลขส่วนลด |  | smallint | ✓ |
| `price_changed` | มีการแก้ไขราคา |  | smallint | ✓ |
| `discount_changed` | มีการแก้ไขส่วนลด |  | smallint | ✓ |
| `price_default` | ราคาเริ่มต้น |  | float | ✓ |
| `tax_type` | ประเภทภาษี (0=มีภาษี,1=ยกเว้น) |  | smallint | ✓ |
| `is_pos` | จาก POS |  | smallint | ✓ |
| `auto_create` | สร้างโดยโปรแกรม |  | smallint | ✓ |
| `date_expire` | หมดอายุ |  | smalldatetime | ✓ |
| `hidden_cost_1` | ต้นทุนแฝงบริหาร |  | float | ✓ |
| `hidden_cost_1_exclude_vat` | ต้นทุนแฝงบริหารไม่รวมภาษี |  | float | ✓ |
| `hidden_cost_2` | ต้นทุนแฝงบัญชี |  | float | ✓ |
| `hidden_cost_2_exclude_vat` | ต้นทุนแฝงบัญชีไม่รวมภาษี |  | float | ✓ |
| `sum_of_cost_1` | ต้นทุนรวมต้นทุนแฝงบริหาร |  | float | ✓ |
| `hidden_cost_1_name_1` | ทุนแฝง *(resource only)* |  | char |  |
| `average_cost_1` | ราคาทุนเฉลี่ยแฝง |  | float | ✓ |
| `hidden_cost_1_name_2` | รายได้แฝง *(resource only)* |  | char |  |
| `doc_ref_partial` | ใบรับสินค้า *(resource only)* |  | char |  |
| `sale_code` | รหัสพนักงานขาย |  | varchar(25) | ✓ |
| `sale_group` | กลุ่มพนักงานขาย |  | varchar(25) | ✓ |
| `date_due` | วันครบกำหนด |  | datetime | ✓ |
| `lot_number_1` | เลข LOT |  | varchar(50) | ✓ |
| `item_name_en` | ชื่อสินค้า (อังกฤษ) *(resource only)* |  | char |  |
| `unit_name_en` | หน่วยนับ (อังกฤษ) *(resource only)* |  | char |  |
| `item_code_2` | รหัสสินค้า |  | varchar(25) | ✓ |
| `book_bank_code_out` | จากสมุดเงินฝาก *(resource only)* |  | char |  |
| `book_bank_code_in` | เข้าสมุดเงินฝาก *(resource only)* |  | char |  |
| `bank_name_2` | ธนาคาร |  | varchar(25) | ✓ |
| `bank_branch_2` | สาขา |  | varchar(25) | ✓ |
| `use_expire` | ใช้ระบบวันหมดอายุ *(resource only)* |  | char |  |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `price_base` | ราคากลาง |  | float | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `fee_amount` | ค่าธรรมเนียม |  | float | ✓ |
| `transfer_amount` | ยอดโอนเงิน |  | float | ✓ |
| `price_set_ratio` | อัตราส่วนราคาสินค้าชุด |  | float | ✓ |
| `print_qty` | จำนวนพิมพ์ *(resource only)* |  | char |  |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |
| `mfn_code` | รหัสผู้ผลิต |  | varchar(50) | ✓ |
| `mfn_name` | ผู้ผลิต |  | varchar(255) | ✓ |
| `start_qty` | จำนวนเริ่มต้น *(resource only)* |  | char |  |
| `end_qty` | จำนวนสินสุด *(resource only)* |  | char |  |
| `department` | แผนก *(resource only)* |  | char |  |
| `allocate` | การจัดสรร *(resource only)* |  | char |  |
| `project` | โครงการ *(resource only)* |  | char |  |
| `price_2` | ราคา | Price | float | ✓ |
| `sum_amount_2` | รวมมูลค่า | Sum Amount | float | ✓ |
| `price_guid` | Price Guid |  | varchar(55) | ✓ |
| `discount_amount_2` | มูลค่าส่วนลด |  | float | ✓ |
| `is_lock_cost` | กำหนดต้นทุนเอง | Lock Cost | smallint | ✓ |
| `sum_of_cost_fix` | ต้นทุน |  | float | ✓ |
| `profit_lost_cost_amount` | กำไรขาดทุน | Profit Lost Cost Amount | float | ✓ |
| `is_doc_copy` | เป็นเอกสารที่ออกแทน |  | smallint | ✓ |
| `bat_date` | bat date | bat date | smalldatetime | ✓ |
| `bat_number` | bat number | bat number | varchar(255) | ✓ |
| `product_year` | ปีที่ผลิต |  | varchar(10) | ✓ |
| `product_week` | สัปดาห์ที่ผลิต |  | varchar(10) | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน |  | float | ✓ |
| `qty_2` | จำนวนขาย |  | float | ✓ |
| `unit_code_2` | หน่วยช่วยขาย |  | varchar(25) | ✓ |
| `total_size` | รวมหน่วยนับ 2 |  | float | ✓ |
| `unit_size` | ขนาดสินค้า |  | float | ✓ |
| `unit_name_2` | ชื่อหน่วยนับ 2 *(resource only)* |  | char |  |
| `exchange_rate_old` | อัตราแลกเปลี่ยนเดิม |  | float | ✓ |
| `total_packaging_qty` | จำนวน Packaging *(resource only)* |  | char |  |
| `promotion_code` | รหัสโปรโมชั่น |  | varchar(50) | ✓ |
| `lab_no` | Lab No. *(resource only)* |  | char |  |

## ic_trans_draft

**รายวัน(ร่าง)** — IC Trans Draft

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Doc Reference | varchar(255) | ✓ |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ | Doc Reference Date | smalldatetime | ✓ |
| `tax_doc_no` | เลขที่ใบกำกับ | Tax No | varchar(25) | ✓ |
| `tax_doc_date` | วันที่ใบกำกับ | Tax Date | smalldatetime | ✓ |
| `inquiry_type` | ประเภทรายการ | Inquiry Type | smallint | ✓ |
| `vat_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `cust_code` | ลูกหนี้/เจ้าหนี้ | AP/AR Code | varchar(25) | ✓ |
| `contactor` | ผู้ติดต่อ | Contactor | varchar(25) | ✓ |
| `branch_code` | สาขา | Branch Code | varchar(25) | ✓ |
| `project_code` | โครงการ | Project Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | Department | varchar(25) | ✓ |
| `sale_area_code` | เขตการขาย | Sale Area | varchar(25) | ✓ |
| `sale_code` | พนักงานขาย | Sale | varchar(25) | ✓ |
| `send_type` | ประเภทการส่ง | Sending Type | smallint | ✓ |
| `send_day` | รับ/ส่ง ภายใน(วัน) | Send/Receive Day | int | ✓ |
| `send_date` | วันที่รับ/ส่งสินค้า | Send Date | smalldatetime | ✓ |
| `expire_date` | วันที่หมดอายุ | Expire Date | smalldatetime | ✓ |
| `credit_day` | วันเครดิต | Credit Day | int | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `answer_type` | ลูกค้าตอบกลับ | Answer Type | smallint | ✓ |
| `transport_value` | ค่าขนส่ง | Transport Value | float | ✓ |
| `discount_word` | ส่วนลด | Discount | varchar(25) | ✓ |
| `vat_rate` | อัตราภาษี | Vat Rate | float | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `total_cost` | ต้นทุนสินค้า | Total Cost | float | ✓ |
| `total_value` | มูลค่าสินค้า | Total Value | float | ✓ |
| `total_discount` | มูลค่าส่วนลด | Total Discount | float | ✓ |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `total_after_vat` | มูลค่าหลังคิดภาษี | Total After Vat | float | ✓ |
| `total_except_vat` | มูลค่ายกเว้นภาษี | Total Except Vat | float | ✓ |
| `total_amount` | มูลค่าสุทธิ | Total Net Value | float | ✓ |
| `balance_amount` | ยอดเงินคงเหลือ | Balance Amount | float | ✓ |
| `adjust_reason` | เหตุผลการปรับปรุง | Adjust Reason | varchar(25) | ✓ |
| `approve_code` | กลุ่มผู้อนุมัติ | Approve User Group | varchar(25) | ✓ |
| `approve_date` | วันที่อนุมัติ | Approve Date | smalldatetime | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `ar_code` | รหัสลูกค้า/ลูกหนี้ *(resource only)* | Ar Code | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | Ap Code | char |  |
| `user_request` | ผู้ขออนุมัติ | User Request | varchar(25) | ✓ |
| `expire_day` | จำนวนวันหมดอายุ | Expire Day | int | ✓ |
| `send_mail` | แจ้งส่งทาง อีเมล์ | Warning Email | smallint | ✓ |
| `send_sms` | แจ้งส่งทาง SMS | Warning SMS | smallint | ✓ |
| `doc_ref_trans` | อ้างอิงเอกสาร | Ref | varchar(25) | ✓ |
| `doc_ref_requisition` | เลขที่ใบเบิก *(resource only)* | Ref Requisition No | char |  |
| `condition_pack_1` | แยกตามหน่วยนับ *(resource only)* | Pack | char |  |
| `doc_ref_check_stock` | เลขที่ใบขอตรวจนับ *(resource only)* |  | char |  |
| `doc_ref_transfer_out` | เลขที่ใบโอนออก *(resource only)* |  | char |  |
| `zero_vat` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `exc_vat` | ยกเว้นภาษี *(resource only)* |  | char |  |
| `normal_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `exclude_vat` | ภาษีแยกนอก *(resource only)* |  | char |  |
| `include_vat` | ภาษีรวมใน *(resource only)* |  | char |  |
| `credit_date` | วันที่ครบกำหนด |  | smalldatetime | ✓ |
| `ownreceive` | รับเอง *(resource only)* |  | char |  |
| `sendto` | ส่งให้ *(resource only)* |  | char |  |
| `total_before_vat` | ยอดก่อนภาษี |  | float | ✓ |
| `credit_purchase` | ซื้อสินค้าเงินเชื่อ *(resource only)* |  | char |  |
| `cash_purchase` | ซื้อสินค้าเงินสด *(resource only)* |  | char |  |
| `credit_purchase_service` | ซื้อสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_purchase_service` | ซื้อสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_purchase_other` | ค่าใช้จ่ายเงินเชื่อ *(resource only)* |  | char |  |
| `cash_purchase_other` | ค่าใช้จ่ายเงินสด *(resource only)* |  | char |  |
| `credit_purchase_service_other` | ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_purchase_service_other` | ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_sale` | ขายเงินเชื่อ *(resource only)* |  | char |  |
| `cash_sale` | ขายเงินสด *(resource only)* |  | char |  |
| `credit_sale_service` | ขายสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_sale_service` | ขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_sale_other` | รายได้เงินเชื่อ *(resource only)* |  | char |  |
| `cash_sale_other` | รายได้เงินสด *(resource only)* |  | char |  |
| `credit_sale_service_other` | รายได้เงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_sale_service_other` | รายได้เงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `job_code` | งาน | Job | varchar(25) | ✓ |
| `delivery_date` | วันที่ส่งของ | Date of delivery | smalldatetime | ✓ |
| `deposit_no` | เลขที่ใบจ่ายเงินล่วงหน้า *(resource only)* | Deposit No | varchar(25) |  |
| `pay_amount` | เงินชำระ | Pay amount | float | ✓ |
| `money` | จำนวนเงินคืน | Money | float | ✓ |
| `sum_pay_money_cash` | รับ/จ่ายชำระหนี้ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq` | รับ/จ่ายชำระหนี้ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit` | รับ/จ่ายชำระหนี้ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer` | รับ/จ่ายชำระหนี้ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_cash_in` | รับชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_in` | รับชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_in` | รับชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_in` | รับชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_cash_out` | จ่ายชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_out` | จ่ายชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_out` | จ่ายชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_out` | จ่ายชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_diff` | ผลต่างยอดชำระ | Diff | float | ✓ |
| `ret_cash` | รับคืนจากขายเงินสด *(resource only)* |  | char |  |
| `ret_credit` | รับคืนจากขายเงินเชื่อ *(resource only)* |  | char |  |
| `ret_cash_1` | ลดหนี้จากขายเงินสด (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `ret_credit_1` | ลดหนี้จากขายเงินเชื่อ (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `ret_cash_service` | รับคืนจากขายสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_service` | รับคืนจากขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_other` | ลดหนี้รายได้เงินเชื่อ *(resource only)* |  | char |  |
| `ret_cash_other` | ลดหนี้รายได้เงินสด *(resource only)* |  | char |  |
| `ret_cash_service_other` | ลดหนี้รายได้เงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_service_other` | ลดหนี้รายได้เงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_credit` | เพิ่มหนี้จากการขายเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_credit_1` | เพิ่มหนี้จากการขายเงินเชื่อ (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `invoice_add_credit_service` | เพิ่มหนี้จากการขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_credit_other` | เพิ่มหนี้จากรายได้อื่นเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_credit_service_other` | เพิ่มหนี้จากรายได้อื่นเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `reduction_expense_other_credit` | ลดหนี้ค่าใช้จ่ายเงินเชื่อ *(resource only)* | Reduce debt Expenditures on credit | char |  |
| `reduction_expense_other_cash` | ลดหนี้ค่าใช้จ่ายเงินสด *(resource only)* | Reduce debt Cash expenditures | char |  |
| `reduction_expense_other_credit_service` | ลดหนี้ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* | Reduce debt Expenditures on credit (service) | char |  |
| `reduction_expense_other_cash_service` | ลดหนี้ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* | Reduce debt Cash expenditures (service) | char |  |
| `invoice_add_expense_other_credit` | เพิ่มหนี้ค่าใช้จ่ายเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_expense_other_cash` | เพิ่มหนี้ค่าใช้จ่ายเงินสด *(resource only)* |  | char |  |
| `invoice_add_expense_other_credit_service` | เพิ่มหนี้ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_expense_other_cash_service` | เพิ่มหนี้ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `currency_money` | ยอดคงเหลือ(ตามสกุลเงิน) | Currency Money | float | ✓ |
| `total_debt_amount` | ยอดหนี้รวมภาษี | Total Debt Amount | float | ✓ |
| `sale_name` | ชื่อพนักงานขาย *(resource only)* | Sale Name | char |  |
| `buy_deposit` | เลขที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `buy_deposit2` | เลขที่ใบจ่ายมัดจำ *(resource only)* |  | char |  |
| `sell_deposit` | เลขที่ใบรับล่วงหน้า *(resource only)* |  | char |  |
| `sell_deposit2` | เลขที่ใบรับมัดจำ *(resource only)* |  | char |  |
| `pay_deposit_buy` | จำนวนจ่ายเงินล่วงหน้า *(resource only)* |  | char |  |
| `pay_deposit_buy2` | จำนวนเงินจ่ายมัดจำ *(resource only)* |  | char |  |
| `pay_deposit_sell` | จำนวนเงินรับล่วงหน้า *(resource only)* |  | char |  |
| `pay_deposit_sell2` | จำนวนเงินรับมัดจำ *(resource only)* |  | char |  |
| `deposit_buy` | จ่ายคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `deposit_buy2` | จ่ายคืนเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_sell` | รับคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `deposit_sell2` | รับคืนเงินมัดจำ *(resource only)* |  | char |  |
| `po_debt_balance` | ตั้งหนี้ยกมา *(resource only)* | OP Debt Balance | char |  |
| `po_cn_balance` | ลดหนี้ยกมา *(resource only)* | PO CN Balance | char |  |
| `po_purchase` | ซื้อสินค้า *(resource only)* | PO Purchase | char |  |
| `po_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | PO Addition Debt | char |  |
| `so_billing` | บิลขาย *(resource only)* | SO Billing | char |  |
| `so_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | SO Addition Debt | char |  |
| `so_debt_balance` | ตั้งหนี้ *(resource only)* | SO Debt Balance | char |  |
| `so_cn_balance` | ลดหนี้ *(resource only)* | SO CN Balance | char |  |
| `sale_type` | ประเภทการขาย *(resource only)* |  | char |  |
| `payable_add_type` | ประเภทการส่งคืน *(resource only)* |  | char |  |
| `payable_add_type_1` | เพิ่มหนี้เจ้าหนี้, เพิ่มสินค้า *(resource only)* |  | char |  |
| `payable_add_type_2` | เพิ่มหนี้เจ้าหนี้, ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `payable_sub_type_1` | ลดหนี้เจ้าหนี้, ลดสินค้า *(resource only)* |  | char |  |
| `payable_sub_type_2` | ลดหนี้เจ้าหนี้, ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `doc_no_po` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_date_po` | วันที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `cancel_type` | ประเภทการยกเลิก |  | int | ✓ |
| `cancel_type_1` | ยกเลิกทั้งหมด *(resource only)* |  | char |  |
| `cancel_type_2` | ยกเลิกรายสินค้า *(resource only)* |  | char |  |
| `last_status` | สถานะ |  | smallint | ✓ |
| `used_status` | มีการอ้างอิงแล้ว |  | smallint | ✓ |
| `doc_success` | สิ้นสุด |  | smallint | ✓ |
| `doc_advance_in_no` | เลขที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_in_date` | วันที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `doc_purchase_no` | เลขที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_purchase_date` | วันที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_purchase_debit_no` | ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_purchase_debit_date` | วันที่เพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_purchase_credit_no` | ใบลดหนี้ *(resource only)* |  | char |  |
| `doc_purchase_credit_date` | วันที่ลดหนี้ *(resource only)* |  | char |  |
| `doc_quotation_no` | ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_quotation_date` | วันที่ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_inquiry_no` | เลขที่ใบสั่งจอง *(resource only)* |  | char |  |
| `doc_inquiry_date` | วันที่ใบสั่งจอง *(resource only)* |  | char |  |
| `doc_saleorder_no` | เลขที่ใบสั่งขาย *(resource only)* |  | char |  |
| `doc_saleorder_date` | วันที่ใบสั่งขาย *(resource only)* |  | char |  |
| `doc_advance_so_no` | เลขที่ใบรับเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_date` | วันที่ใบรับเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_return_no` | เลขที่ใบคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_return_date` | วันที่ใบคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_invoice_no` | เลขที่ใบขายสินค้า/บริการ *(resource only)* |  | char |  |
| `doc_invoice_date` | วันที่ใบขายสินค้า/บริการ *(resource only)* |  | char |  |
| `doc_ar_debit_note_no` | เลขที่ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_ar_debit_note_date` | วันที่ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_ar_credit_note_no` | เลขที่ใบลดหนี้ *(resource only)* |  | char |  |
| `doc_ar_credit_note_date` | วันที่ใบลดหนี้ *(resource only)* |  | char |  |
| `sale_add_type` | ประเภทการเพิ่มหนี้ *(resource only)* |  | char |  |
| `total_manual` | บันทึกยอดรวมเอง |  | smallint | ✓ |
| `total_after_discount` | มูลค่าหลังหักส่วนลด *(resource only)* |  | char |  |
| `cust_name` | ชื่อลูกหนี้/เจ้าหนี้ *(resource only)* |  | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `sum_total` | ยอดรวม *(resource only)* |  | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* |  | char |  |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `tab_more` | เพิ่มเติม *(resource only)* |  | char |  |
| `on_hold` | ระงับชั่วคราว |  | smallint | ✓ |
| `extra_word` | ข้อความเพิ่มเติม |  | varchar(100) | ✓ |
| `transport_code` | ขนส่งโดย |  | varchar(25) | ✓ |
| `purchase_name` | ผู้สั่งซื้อ *(resource only)* |  | char |  |
| `tab_pay_out` | รายละเอียดการจ่ายเงิน *(resource only)* |  | char |  |
| `tab_pay_in` | รายละเอียดการรับเงิน *(resource only)* |  | char |  |
| `want_day` | ต้องการภายใน (วัน) |  | smallint | ✓ |
| `want_date` | ต้องการภายใน (วันที่) |  | smalldatetime | ✓ |
| `deposit_day` | ระยะเวลาภายใน (วัน) |  | smallint | ✓ |
| `deposit_date` | ระยะเวลาภายใน (วันที่) |  | smalldatetime | ✓ |
| `remark2` | หมายเหตุ *(resource only)* |  | char |  |
| `tab_wht_in` | ภาษีหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `tab_wht_out` | ภาษีถูกหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `tab_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `sale_group` | กลุ่มพนักงานขาย |  | varchar(25) | ✓ |
| `doc_po_request` | เลขที่ใบเสนอซื้อ *(resource only)* |  | char |  |
| `not_approve_1` | ไม่อนุมัติ |  | smallint | ✓ |
| `user_approve` | ผู้อนุมัติ |  | varchar(25) | ✓ |
| `user_cancel` | ผู้ยกเลิก *(resource only)* |  | char |  |
| `sale_return_type` | ประเภทการรับคืน *(resource only)* |  | char |  |
| `approve_status` | สถานะการอนุมัติ |  | smallint | ✓ |
| `expire_status` | สถานะหมดอายุ |  | smallint | ✓ |
| `sum_pay_rounding` | ปัดเศษ *(resource only)* |  | char |  |
| `sum_petty_cash` | เงินสดย่อย *(resource only)* |  | char |  |
| `sum_deposit` | เงินรับล่วงหน้า *(resource only)* |  | char |  |
| `sum_advance` | เงินมัดจำ *(resource only)* |  | float |  |
| `sum_used` | ยอดเงินนำไปใช้ *(resource only)* |  | char |  |
| `advance_amount` | ตัดเงินมัดจำ |  | float | ✓ |
| `tab_advance` | เงินมัดจำ *(resource only)* |  | char |  |
| `doc_ref_name_1` | เลขที่ใบรับคืนจ่ายเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_ref_name_2` | เลขที่ใบรับคืนเงินมัดจำ *(resource only)* |  | char |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `tab_pay` | รายละเอียดการจ่าย *(resource only)* |  | char |  |
| `tab_wht` | ภาษีหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `used_status_2` | สถานะ 2 |  | smallint | ✓ |
| `remark_2` | หมายเหตุ 2 |  | varchar(255) | ✓ |
| `remark_3` | หมายเหตุ 3 |  | varchar(255) | ✓ |
| `return_type` | ประเภทการลดหนี้ *(resource only)* |  | char |  |
| `ref_amount` | มูลค่าเอกสารเดิม |  | float | ✓ |
| `ref_new_amount` | มูลค่าที่ถูกต้อง |  | float | ✓ |
| `ref_diff` | ผลต่าง |  | float | ✓ |
| `sum_point` | แต้ม |  | float | ✓ |
| `cashier_code` | Cashier |  | varchar(25) | ✓ |
| `is_pos` | จากระบบ POS |  | smallint | ✓ |
| `pos_id` | หมายเลขเครื่อง POS |  | varchar(25) | ✓ |
| `member_code` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `doc_no_guid` | เลขที่เอกสารเปรียบเทียบ |  | varchar(25) | ✓ |
| `pos_bill_type` | 0=อย่างย่อ,1=อย่างเต็ม |  | smallint | ✓ |
| `pos_bill_change` | 0=ปรกติ,1=ใบแทน |  | smallint | ✓ |
| `doc_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `doc_type_purchase` | ซื้อสินค้า *(resource only)* |  | char |  |
| `doc_type_finish_good` | รับสินค้าสำเร็จรูป *(resource only)* |  | char |  |
| `wh_in_1` | รับจากใบสั่งซื้อ *(resource only)* |  | char |  |
| `wh_in_2` | รับจากการซื้อ *(resource only)* |  | char |  |
| `wh_in_3` | รับจากการเพิ่มหนี้ *(resource only)* |  | char |  |
| `wh_in` | ประเภทเอกสารรับ *(resource only)* |  | char |  |
| `wh_out_1` | ส่งคืนจากใบรับสินค้า (คลัง) *(resource only)* |  | char |  |
| `wh_out_2` | ส่งคืนจากใบส่งคืน (บัญชี) *(resource only)* |  | char |  |
| `wh_out_3` | ส่งคืนจากใบลดหนี้ (บัญชี) *(resource only)* |  | char |  |
| `wh_out` | ประเภทเอกสารออก *(resource only)* |  | char |  |
| `wh_in_4` | รับสินค้าสำเร็จรูป *(resource only)* |  | char |  |
| `wh_in_5` | รับคืนวัตถุดิบ *(resource only)* |  | char |  |
| `recheck_count_day` | เตือนย้อนหลัง (วัน) |  | float | ✓ |
| `recheck_count` | เปิดระบบเตือนตรวจนับซ้ำ |  | smallint | ✓ |
| `wh_from` | คลัง |  | varchar(25) | ✓ |
| `location_from` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `wh_to` | คลังปลายทาง |  | varchar(25) | ✓ |
| `location_to` | ที่เก็บปลายทาง |  | varchar(25) | ✓ |
| `auto_create` | สร้างโดยโปรแกรม |  | smallint | ✓ |
| `payable_sub_type_1_1` | ส่งคืนสินค้า *(resource only)* |  | char |  |
| `payable_sub_type_1_2` | ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `payable_sub_type_3` | ส่งคืนเงินสด *(resource only)* |  | char |  |
| `payable_sub_type_4` | ราคาผิดเงินสด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `invoice_add_cash_other` | เพิ่มหนี้รายได้อื่นๆ เงินสด *(resource only)* |  | char |  |
| `invoice_add_cash_service_other` | เพิ่มหนี้รายได้อื่นๆเงินสด (ค่าบริการ) *(resource only)* |  | char |  |
| `total_dept_amount` | ยอดตั้งหนี้ *(resource only)* |  | char |  |
| `debt_reduction_amount` | ยอดลดหนี้ *(resource only)* |  | char |  |
| `increase_the_debt_amount` | ยอดเพิ่มหนี้ *(resource only)* |  | char |  |
| `pay_debt_amount` | ยอดจ่ายชำระ *(resource only)* |  | char |  |
| `due_day_over` | เกินกำหนด *(resource only)* |  | char |  |
| `send_to_pick_and_pack` | สั่งจัดสินค้า |  | smallint | ✓ |
| `tab_gl` | GL *(resource only)* | GL | char |  |
| `cust_name_en` | ชื่อลูกค้า (อังกฤษ) *(resource only)* |  | char |  |
| `service_charge_word` | Service Charge |  | varchar(25) | ✓ |
| `total_service_charge` | มูลค่า Service Charge |  | float | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(255) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `deposit_doc` | เลขที่ใบรับเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_doc_date` | วันที่ใบรับเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_return_doc` | เลขที่ใบคืนเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_return_doc_date` | วันที่ใบคืนเงินมัดจำ *(resource only)* |  | char |  |
| `table_number` | หมายเลขโต๊ะ |  | varchar(25) | ✓ |
| `period_guid` | GUID กะ |  | varchar(50) | ✓ |
| `branch_code_to` | ถึงสาขา | To Branch | varchar(25) | ✓ |
| `allocate_code_to` | ถึงการจัดสรร |  | varchar(25) | ✓ |
| `project_code_to` | ถึงโครงการ |  | varchar(25) | ✓ |
| `job_code_to` | ถึงงาน |  | varchar(25) | ✓ |
| `side_code_to` | ถึงฝ่าย |  | varchar(25) | ✓ |
| `department_code_to` | ถึงแผนก |  | varchar(25) | ✓ |
| `point_telephone` | หมายเลขโทรศัพท์ |  | varchar(25) | ✓ |
| `sum_point_2` | ยอดแต้มสะสมระบบกลาง |  | float | ✓ |
| `tab_shipment` | การจัดส่ง *(resource only)* |  | char |  |
| `remark_4` | หมายเหตุ 4 |  | varchar(255) | ✓ |
| `remark_5` | หมายเหตุ 5 |  | varchar(255) | ✓ |
| `tab_vat_buy` | ภาษีซื้อ *(resource only)* |  | char |  |
| `tab_vat_sale` | ภาษีขาย *(resource only)* |  | char |  |
| `is_manual_vat` | บันทึกรายการภาษีเอง |  | smallint | ✓ |
| `pass_book_code` | สมุดเงินฝาก |  | varchar(25) | ✓ |
| `total_amount_2` | มูลค่าสุทธิ(สกุลเงิน) |  | float | ✓ |
| `sender_code` | พนักงานขนส่ง |  | varchar(25) | ✓ |
| `is_cancel` | เอกสารยกเลิก |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิกเอกสาร |  | varchar(255) | ✓ |
| `cancel_datetime` | เวลายกเลิกเอกสาร |  | datetime | ✓ |
| `deposit_payment_cash` | จ่ายมัดจำเงินสด *(resource only)* |  | char |  |
| `deposit_payment_credit` | จ่ายมัดจำเงินเชื่อ *(resource only)* |  | char |  |
| `user_request_transfer` | ผู้ขอโอน *(resource only)* |  | char |  |
| `is_hold` | ระงับเอกสาร |  | smallint | ✓ |
| `auto_approved` | อนุมัติโดยอัตโนมัติ |  | smallint | ✓ |
| `pos_transfer` | โอนมาจากPOS |  | smallint | ✓ |
| `doc_close` | ปิดเอกสาร |  | smallint | ✓ |
| `ref_doc_type` | ประเภทเอกสาร |  | varchar(50) | ✓ |
| `is_arm` | ARM *(resource only)* | ARM | char |  |
| `adjust_normal` | ปรับปรุงสินค้า *(resource only)* |  | char |  |
| `adjust_stock_balance` | ปรับปรุงยกมาสินค้า *(resource only)* |  | char |  |
| `adjust_end_product` | ปรับปรุงปิดสินค้า *(resource only)* |  | char |  |
| `is_doc_copy` | เป็นเอกสารที่ออกแทน |  | smallint | ✓ |
| `doc_reason` | เหตุผล |  | varchar(500) | ✓ |
| `cn_reason` | เหตุผลการลดหนี้ *(resource only)* |  | char |  |
| `dn_reason` | เหตุผลการเพิ่มหนี้ *(resource only)* |  | char |  |
| `no_tax` | ไม่กระทบภาษี *(resource only)* |  | char |  |
| `doc_format_code_adjust` | รหัสเอกสารปรับปรุงเพิ่ม *(resource only)* |  | char |  |
| `deposit_balance` | เงินมัดจำคงเหลือ *(resource only)* |  | char |  |
| `discount_word_2` | ส่วนลด(สกุลเงิน) |  | varchar(50) | ✓ |
| `total_discount_2` | มูลค่าส่วนลด(สกุลเงิน) |  | float | ✓ |
| `total_value_2` | มูลค่าสินค้า(สกุลเงิน) |  | float | ✓ |
| `total_amout_old` | มูลค่าสุทธิเดิม |  | float | ✓ |
| `lost_profit_exchange_amount` | ผลต่างจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `expense` | ค่าใช้จ่าย *(resource only)* |  | char |  |
| `inquiry_type_product` | สินค้า *(resource only)* |  | char |  |
| `inquiry_type_service` | บริการ *(resource only)* |  | char |  |
| `delivery_on` | วันที่สินค้าถึงร้าน *(resource only)* |  | char |  |
| `total_cheque_amount` | รวมมูลค่าเช็ค *(resource only)* |  | char |  |
| `doc_copy_reason_type` | ประเภทการออกเอกสารแทน |  | smallint | ✓ |
| `bank_code` | ธนาคาร *(resource only)* |  | char |  |
| `bank_branch` | สาขาธนาคาร *(resource only)* |  | char |  |
| `is_lab_cut` | บันทึกการตัด Lab *(resource only)* |  | char |  |

