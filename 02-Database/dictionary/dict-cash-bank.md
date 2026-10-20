---
tags: [sml, dictionary, cash-bank, generated]
module: Cash_Bank
---
# พจนานุกรม: Cash_Bank — เงินสด/ธนาคาร

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#cb_chq_list]] | ข้อมูลเช็ค / Chq List | 56 |
| [[#cb_credit_card]] | บัตรเครดิต / Credit Card | 35 |
| [[#cb_petty_cash]] | วงเงินสดย่อย / Petty Cash | 10 |
| [[#cb_resource]] | รายละเอียดข้อความ / Cash andamp; Bank Resource | 43 |
| [[#cb_trans]] | รายวันทั้งหมด / Cash and Bank Transection | 58 |
| [[#cb_trans_detail]] | รายละเอียดรายวัน / Cash And Bank Transection Detail | 70 |
| [[#erp_bank]] | ธนาคาร / Bank List | 6 |
| [[#erp_bank_branch]] | สาขาธนาคาร / Bank Branch | 6 |
| [[#erp_book_bank_trans_type]] | ตัวย่อในสมุดเงินฝาก / Book Bank Trans Type | 5 |
| [[#erp_pass_book]] | สมุดธนาคาร / Pass Book | 22 |
| [[#erp_pass_book_type]] | ประเภทสมุดบัญชีธนาคาร / Pass Book Type | 6 |

## cb_chq_list

**ข้อมูลเช็ค** — Chq List · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `chq_get_date` | วันที่รับ/จ่ายเช็ค | Chq Get Date | smalldatetime | ✓ |
| `chq_type` | ประเภทเช็ค | Chq Type | smallint | ✓ |
| `chq_number` | เลขที่เช็ค | Chq Number | varchar(100) | ✓ |
| `chq_due_date` | วันที่บนเช็ค | Chq Due Date | smalldatetime | ✓ |
| `chq_description` | รายละเอียดเช็ค | Chq Description | varchar(255) | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Document Ref | varchar(25) | ✓ |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) | ✓ |
| `pass_book_code` | สมุดธนาคาร | Pass Book Code | varchar(25) | ✓ |
| `bank_code` | ธนาคาร | Bank | varchar(25) | ✓ |
| `bank_branch` | สาขาธนาคาร | Bank Branch | varchar(100) | ✓ |
| `bank_description` | รายละเอียดธนาคาร | Bank Description | varchar(255) | ✓ |
| `amount` | จำนวนเงิน | Amount | float | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `owner_name` | ชื่อเจ้าของเช็ค | Owner Name | varchar(100) | ✓ |
| `person_code` | ผู้รับ/จ่ายเช็ค | Person Code | varchar(25) | ✓ |
| `side_code` | รหัสฝ่าย | Side Code | varchar(25) | ✓ |
| `department_code` | รหัสแผนก | department Code | varchar(25) | ✓ |
| `ap_ar_code` | รหัสเจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `ap_ar_name` | ชื่อเจ้าหนี้/ลูกหนี้ *(resource only)* | AP/AR Name | varchar(100) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | guid_code | guid_code | varchar(35) | ✓ |
| `chq_on_hand` | เช็คในมือ *(resource only)* | Chq on Hand | char |  |
| `chq_commit` | เช็คนำฝาก *(resource only)* | Chq Commit | char |  |
| `chq_pass` | เช็คผ่าน *(resource only)* | Chq Pass | char |  |
| `chq_return` | เช็ครับคืน *(resource only)* | Chq Return | char |  |
| `chq_cancel` | เช็คยกเลิก *(resource only)* | Chq Cancel | char |  |
| `chq_sale` | เช็คขายลด *(resource only)* | Chq Sale | char |  |
| `chq_commit_again` | เช็คคืนนำเข้าใหม่ *(resource only)* | Chq Commit Again | char |  |
| `chq_payment` | เช็คจ่าย *(resource only)* | Chq Payment | char |  |
| `chq_change` | เช็คเปลี่ยน *(resource only)* | Chq Change | char |  |
| `chq_cash` | เช็คเงินสด *(resource only)* | Cash | char |  |
| `chq_acc_pay` | เช็คเข้าบัญชี *(resource only)* | Account Payee | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | AP Code | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* | AP Name | char |  |
| `ar_code` | รหัสลูกหนี้ *(resource only)* | AR Code | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* | AR Name | char |  |
| `date_pay` | วันที่จ่ายเช็ค *(resource only)* |  | char |  |
| `date_receive` | วันที่รับเช็ค *(resource only)* |  | char |  |
| `trans_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | รายวันระบบ |  | smallint | ✓ |
| `no_approved` | เลขที่อนุมัติ |  | varchar(100) | ✓ |
| `credit_card_type` | ประเภทบัตรเครดิต |  | varchar(25) | ✓ |
| `charge` | ยอด Charge |  | float | ✓ |
| `sum_amount` | รวมทั้งสิ้น |  | float | ✓ |
| `ap_ar_type` | (1=ลูกหนี้,2=เจ้าหนี้) |  | smallint | ✓ |
| `credit_card_number` | เลขที่บัตรเครดิต *(resource only)* |  | char |  |
| `credit_card_date` | วันที่รับ *(resource only)* |  | char |  |
| `doc_line_number` | Line |  | smallint | ✓ |
| `external_chq` | เช็คนอกเขต |  | smallint | ✓ |
| `chq_area_type` | การเรียกเก็บ *(resource only)* |  | char |  |
| `cheque_internal` | เช็คในเขต *(resource only)* |  | char |  |
| `cheque_external` | เช็คนอกเขต *(resource only)* |  | char |  |
| `chequq_draft` | ดราฟต์ *(resource only)* |  | char |  |
| `balance_amount` | มูลค่าคงเหลือ *(resource only)* |  | char |  |
| `user_code` | พนักงาน *(resource only)* |  | char |  |

index: `cb_chq_list_chq_number_idx`(chq_number), `cb_chq_list_doc_ref_idx`(doc_ref), `cb_chq_list_line_number_idx`(doc_line_number), `cb_chq_list_chq_type_status_idx`(chq_type,status)

## cb_credit_card

**บัตรเครดิต** — Credit Card · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Trans Type | smallint | ✓ |
| `credit_get_date` | วันที่รับบัตร | Credit Get Date | smalldatetime | ✓ |
| `credit_card_type` | ประเภทบัตรเครดิต | Credit Card Type | varchar(25) | ✓ |
| `credit_card_no` | เลขที่บัตรเครดิต | Credit Card No | varchar(25) |  |
| `credit_card_code` | รหัสท้ายบัตร | Credit Card Code | varchar(25) | ✓ |
| `owner_name` | ชื่อเจ้าของบัตร | Owner Name | varchar(100) | ✓ |
| `credit_money` | วงเงินเครดิต | Credit Money | float | ✓ |
| `credit_card_expire` | วันที่บัตรหมดอายุ | Credit Card Expire | smalldatetime | ✓ |
| `credit_due_date` | วันที่ครบกำหนด | Credit Due Date | smalldatetime | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) |  |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) | ✓ |
| `pass_book_code` | สมุดธนาคาร | Pass Book Code | varchar(25) | ✓ |
| `bank_code` | ธนาคาร | Bank | varchar(25) | ✓ |
| `bank_branch` | สาขาธนาคาร | Bank Branch | varchar(100) | ✓ |
| `bank_description` | รายละเอียดธนาคาร | Bank Description | varchar(255) | ✓ |
| `amount` | จำนวนเงิน | Amount | float | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `person_code` | ผู้รับบัตร | Person_Code | varchar(25) | ✓ |
| `ar_code` | รหัสลูกค้า | AR Code | varchar(25) | ✓ |
| `ar_name` | ชื่อลูกค้า *(resource only)* | AR Name | varchar(100) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `credit_card_on_hand` | บัตรในมือ *(resource only)* | Credit Card on Hand | char |  |
| `credit_card_honor` | ขึ้นเงินแล้ว *(resource only)* | Credit Card Honor | char |  |
| `credit_card_cancel` | ยกเลิก *(resource only)* | Credit Card Cancel | char |  |
| `credit_type_visa` | วีซ่าการ์ด *(resource only)* | Visa | char |  |
| `credit_type_master` | มาสเตอร์การ์ด *(resource only)* | Master | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | AP Code | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* | AP Name | char |  |
| `date_cut` | วันที่ตัดบัตร | Date Cut | smalldatetime | ✓ |
| `no_approved` | เลขที่อนุมัติ | No. approved. | varchar(255) | ✓ |
| `sum_amount` | จำนวนเงินสุทธิ | Sum Amount | float | ✓ |
| `charge` | ยอด Charge | Charge | float | ✓ |
| `trans_flag` | รายวันระบบ |  | smallint | ✓ |

index: `cb_credit_card_PK_CODE`(credit_card_no,doc_ref)

## cb_petty_cash

**วงเงินสดย่อย** — Petty Cash · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสวงเงินสดย่อย | Code | varchar(25) |  |
| `name_1` | ชื่อวงเงินสดย่อย | Name | varchar(100) |  |
| `name_2` | ชื่อวงเงินสดย่อย (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `credit_money` | ยอดวงเงิน | Credit Money | float | ✓ |
| `balance_money` | ยอดวงเงินคงเหลือ | Balance Money | float | ✓ |
| `chart_of_account` | รหัสผังบัญชี | Chart of Account | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |

index: `cb_petty_cash_PK_CODE`(code)

## cb_resource

**รายละเอียดข้อความ** — Cash andamp; Bank Resource · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_name` | ชื่อลูกหนี้ *(resource only)* | AR Name | char |  |
| `ar_name` | ชื่อเจ้าหนี้ *(resource only)* | AP Name | char |  |
| `account_type_asset` | สินทรัพย์ *(resource only)* | Asset | char |  |
| `account_type_debt` | หนี้สิน *(resource only)* | Debt | char |  |
| `account_type_capital` | ทุน *(resource only)* | Capital | char |  |
| `account_type_income` | รายได้ *(resource only)* | Income | char |  |
| `account_type_expense` | ค่าใช้จ่าย *(resource only)* | Expense | char |  |
| `chq_on_hand` | เช็คในมือ *(resource only)* | Chq on Hand | char |  |
| `chq_commit` | เช็คนำฝาก *(resource only)* | Chq Commit | char |  |
| `chq_pass` | เช็คผ่าน *(resource only)* | Chq Pass | char |  |
| `chq_return` | เช็ครับคืน *(resource only)* | Chq Return | char |  |
| `chq_cancel` | เช็คยกเลิก *(resource only)* | Chq Cancel | char |  |
| `chq_sale` | เช็คขายลด *(resource only)* | Chq Sale | char |  |
| `chq_commit_again` | เช็คคืนนำเข้าใหม่ *(resource only)* | Chq Commit Again | char |  |
| `chq_payment` | เช็คจ่าย *(resource only)* | Chq Payment | char |  |
| `chq_change` | เช็คเปลี่ยน *(resource only)* | Chq Change | char |  |
| `chq_cash` | เช็คเงินสด *(resource only)* | Cash | char |  |
| `chq_acc_pay` | เช็คเข้าบัญชี *(resource only)* | Account Payee | char |  |
| `credit_card_on_hand` | บัตรในมือ *(resource only)* | Credit Card on Hand | char |  |
| `credit_card_honor` | ขึ้นเงินแล้ว *(resource only)* | Credit Card Honor | char |  |
| `credit_card_cancel` | ยกเลิก *(resource only)* | Credit Card Cancel | char |  |
| `cash` | เงินสด *(resource only)* | Cash | char |  |
| `cheque` | เช็ค *(resource only)* | Cheque | char |  |
| `transfer_money` | เงินโอน *(resource only)* | Transfer Money | char |  |
| `doc_date` | วันที่ *(resource only)* |  | char |  |
| `doc_time` | เวลา *(resource only)* |  | char |  |
| `ref_1` | อ้างอิง *(resource only)* |  | char |  |
| `amount_in` | ฝาก *(resource only)* |  | char |  |
| `amount_out` | ถอน *(resource only)* |  | char |  |
| `amount_balance` | คงเหลือ *(resource only)* |  | char |  |
| `remark` | หมายเหตุ *(resource only)* |  | char |  |
| `date_from` | จากวันที่ *(resource only)* |  | char |  |
| `date_to` | ถึงวันที่ *(resource only)* |  | char |  |
| `book_no` | สมุดบัญชี *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `doc_type` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `remark1` | ชื่อลูกค้า/เจ้าหนี้ *(resource only)* |  | char |  |
| `amount_2` | จำนวนเงิน *(resource only)* | Amount | char |  |
| `branch_code` | สาขา *(resource only)* |  | char |  |
| `book_number` | หมายเลขสมุด *(resource only)* |  | char |  |
| `book_name` | ชื่อบัญชี *(resource only)* |  | char |  |
| `bank_code` | ธนาคาร *(resource only)* |  | char |  |
| `bank_branch` | สาขา *(resource only)* |  | char |  |

## cb_trans

**รายวันทั้งหมด** — Cash and Bank Transection · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `total_amount` | รวมยอดเงิน | Total Amount | float | ✓ |
| `total_fee_amount` | ค่าธรรมเนียม | Total Fee Amount | float | ✓ |
| `total_other_amount` | ปัดเศษ (ลด) | Total Other Amount | float | ✓ |
| `total_tax_at_pay` | ภาษีหัก ณ ที่จ่าย | Total Tax At Pay | float | ✓ |
| `total_net_amount` | ยอดรวมทั้งสิ้น | Total Net Amount | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `tax_at_pay_out` | ภาษีถูกหัก ณ ที่จ่าย *(resource only)* |  | char |  |
| `cash_amount` | เงินสด |  | float | ✓ |
| `amount_deposit_out` | รวมจ่ายเงินล่วงหน้า *(resource only)* |  | float |  |
| `chq_amount` | เช็ค |  | float | ✓ |
| `tranfer_amount` | เงินโอน |  | float | ✓ |
| `card_amount` | บัตรเครดิต |  | float | ✓ |
| `total_amount_pay` | รวมจ่าย |  | float | ✓ |
| `total_income_amount` | ปัดเศษ |  | float | ✓ |
| `amount_deposit_return` | รวมเงินรับคืน *(resource only)* |  | char |  |
| `deposit_amount` | ตัดเงินล่วงหน้า |  | float | ✓ |
| `advance_amount` | ตัดเงินมัดจำ |  | float | ✓ |
| `petty_cash_amount` | เงินสดย่อย |  | float | ✓ |
| `amount_deposit_in` | รวมเงินรับล่วงหน้า *(resource only)* |  | char |  |
| `amount_deposit_return_1` | รวมเงินคืน *(resource only)* |  | char |  |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `ap_ar_name` | รายละเอียดเจ้าหนี้/ลูกหนี้ *(resource only)* |  | char |  |
| `ap_ar_code` | รหัสเจ้าหนี้/ลูกหนี้ |  | varchar(25) | ✓ |
| `pay_type` | 1=รับ,2=จ่าย |  | smallint | ✓ |
| `doc_format_code` | doc_format_code |  | varchar(25) | ✓ |
| `pay_cash_amount` | จ่ายเงิน |  | float | ✓ |
| `money_change` | เงินทอน |  | float | ✓ |
| `coupon_amount` | ชำระด้วยคูปอง |  | float | ✓ |
| `point_amount` | ชำระด้วยแต้ม |  | float | ✓ |
| `point_qty` | ใช้แต้มจำนวน |  | float | ✓ |
| `point_rate` | แต้มต่อบาท |  | float | ✓ |
| `total_credit_charge` | ค่า Charge บัตรเครดิต |  | float | ✓ |
| `branch_code` | รหัสสาขา |  | varchar(25) | ✓ |
| `cashier_code` | Cashier |  | varchar(25) | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `discount_amount` | ส่วนลดชำระเงิน |  | float | ✓ |
| `total_income_other` | รายได้อื่น |  | float | ✓ |
| `total_expense_other` | รายจ่ายอื่น |  | float | ✓ |
| `total_extract` | หักอื่น ๆ *(resource only)* |  | char |  |
| `total_pay_other` | จ่ายอื่น ๆ *(resource only)* |  | char |  |
| `total_receive_other` | รับอื่น ๆ *(resource only)* |  | char |  |
| `total_other_currency` | สกุลเงินอื่น ๆ | Other Currency | float | ✓ |
| `receive_money` | รับเงิน *(resource only)* |  | char |  |
| `is_doc_copy` | เป็นเอกสารออกแทน |  | smallint | ✓ |
| `wallet_amount` | Wallet Payment | Wallet Payment | float | ✓ |
| `total_other_currency_charge` | ยอด Charge สกุลเงิน |  | float | ✓ |

index: `cb_trans_PK_CODE`(doc_no,trans_flag), `ap_ar_code`(ap_ar_code), `cb_trans_doc_no_trans_flag_trans_type_idx`(doc_no,trans_flag,trans_type)

## cb_trans_detail

**รายละเอียดรายวัน** — Cash And Bank Transection Detail · edition: `CB`

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

index: `idx_chq_trans_detail_trans_number`(trans_number), `idx_chq_trans_detail_doc_type`(doc_type), `idx_chq_trans_detail_doc_date`(doc_date), `idx_chq_trans_detail_doc_time`(doc_time), `idx_chq_trans_detail_doc_date_time`(doc_date,doc_time), `idx_chq_trans_detail_trans_flag`(trans_flag), `idx_chq_trans_detail_doc_no`(doc_no), `idx_cb_trans_detail_trans_flag_doc_no_doc_type`(trans_flag,doc_no,doc_type), `cb_trans_detail_doc_no_trans_flag_trans_type_doc_type_idx`(doc_no,trans_flag,trans_type,doc_type)

## erp_bank

**ธนาคาร** — Bank List · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Bank Code | varchar(25) |  |
| `name_1` | ชื่อ | Bank Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Bank Name (English) | varchar(100) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `chq_income_account_code` | บัญชีเช็ครับล่วงหน้า |  | varchar(25) | ✓ |

index: `erp_bank_PK_CODE`(code)

## erp_bank_branch

**สาขาธนาคาร** — Bank Branch · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ(ภาษาไทย) | Name TH | varchar(100) | ✓ |
| `name_2` | ชื่อ(ภาษาอังกฤษ) | Name EN | varchar(100) | ✓ |
| `bank_code` | ธนาคาร | Bank | varchar(25) |  |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | GUID | varchar(35) | ✓ |

index: `erp_bank_branch_PK_PRIMARY`(code,bank_code)

## erp_book_bank_trans_type

**ตัวย่อในสมุดเงินฝาก** — Book Bank Trans Type · edition: `All`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | Guid | varchar(35) | ✓ |

index: `erp_book_bank_trans_type_PK_PRIMARY`(code)

## erp_pass_book

**สมุดธนาคาร** — Pass Book · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสสมุด | Book Code | varchar(25) |  |
| `bank_code` | รหัสธนาคาร | Bank Code | varchar(25) |  |
| `bank_branch` | สาขาธนาคาร | Bank Branch | varchar(100) | ✓ |
| `book_type` | ประเภทสมุด | Book Type | varchar(25) |  |
| `book_number` | หมายเลขสมุด | Book Number | varchar(25) |  |
| `tax_number` | เลขประจำตัวผู้เสียภาษี | Tax Number | varchar(25) | ✓ |
| `name_1` | ชื่อเจ้าของบัญชี | Owner Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Owner Name (English) | varchar(100) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | tinyint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `account_code_1` | ผังบัญชีสมุดเงินฝาก | Plan account passbook | varchar(25) | ✓ |
| `account_code_2` | ผังบัญชีเช็คจ่ายล่วงหน้า | Accounts paid in advance. | varchar(25) | ✓ |
| `chq_fee_rate` | อัตราค่าธรรมเนียมเช็คนอกเขต |  | float | ✓ |
| `chq_fee_rate_amount` | ต่อมูลค่าเช็ค(บาท) |  | float | ✓ |
| `min_chq_fee_rate` | อัตราค่าธรรมเนียมขั้นต่ำเช็คนอกเขต |  | float | ✓ |
| `min_chq_fee_amount` | ต่อมูลค่าเช็ค(บาท) |  | float | ✓ |
| `max_chq_fee_rate` | อัตราค่าธรรมเนียมขั้นสูงสุดเช็คนอกเขต |  | float | ✓ |
| `max_chq_fee_amount` | ต่อมูลค่าเช็ค(บาท) |  | float | ✓ |
| `mobile_use` | แสดงบน Mobile Sale |  | int | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |
| `singhaonline_use` | ใช้รับชำระเงิน Singha Online |  | int | ✓ |

index: `erp_pass_book_PK_CODE`(code)

## erp_pass_book_type

**ประเภทสมุดบัญชีธนาคาร** — Pass Book Type · edition: `CB`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `erp_pass_book_type_PK_CODE`(code)

