---
tags: [sml, dictionary, wms, generated]
module: WMS
---
# พจนานุกรม: WMS — คลังสินค้า WMS

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#erp_package_reason]] | เหตุผลการเบิกภาชนะ / ERP Package Reason | 4 |
| [[#ic_inventory_package]] | ภาชนะบรรจุสินค้า / IC Inventory Package | 6 |
| [[#ic_package_trans]] | รายวันภาชนะ / IC Package Trans | 12 |
| [[#ic_package_trans_detail]] | รายละเอียดรายวันภาชนะ / IC Package Trans Detail | 10 |
| [[#ic_wms_trans]] | รายวันทั้งหมด / IC - Transection | 262 |
| [[#ic_wms_trans_detail]] | รายละเอียดรายวัน / IC - Transection Detail | 168 |
| [[#wms_boxes]] | wms_boxes / wms_boxes | 7 |
| [[#wms_boxes_detail]] | wms_boxes_detail / wms_boxes_detail | 8 |
| [[#wms_boxes_lot_detail]] | wms_boxes_lot_detail / wms_boxes_lot_detail | 8 |
| [[#wms_boxes_trans]] | wms_boxes_trans / wms_boxes_trans | 6 |
| [[#wms_boxes_trans_detail]] | wms_boxes_trans_detail / wms_boxes_trans_detail | 5 |
| [[#wms_boxes_trans_lot]] | wms_boxes_trans_lot / wms_boxes_trans_lot | 6 |
| [[#wms_cart]] | wms cart / Table 432 | 16 |
| [[#wms_cart_detail]] | wms_cart_detail / Table 433 | 10 |
| [[#wms_cart_lot]] | WMS Cart Lot  | 5 |
| [[#wms_cart_ref]] | wms_cart_ref  | 3 |
| [[#wms_cart_serial]] | wms_cart_serial  | 4 |
| [[#wms_job]] | wms_job / wms_job | 17 |
| [[#wms_job_detail]] | wms_job_detail / wms_job_detail | 11 |
| [[#wms_job_lot_detail]] | wms_job_lot_detail / wms_job_lot_detail | 9 |
| [[#wms_location]] | wms_location / wms_location | 4 |
| [[#wms_pracel]] | wms_pracel  | 5 |
| [[#wms_product_adj_stock]] | wms_product_adj_stock / wms_product_adj_stock | 10 |
| [[#wms_product_adj_stock_detail]] | wms_product_adj_stock_detail / wms_product_adj_stock_detail | 10 |
| [[#wms_product_adj_stock_lot_detail]] | wms_product_adj_stock_lot_detail / wms_product_adj_stock_lot_detail | 10 |
| [[#wms_product_out]] | wms_product_out  | 17 |
| [[#wms_product_out_detail]] | wms_product_out_detail / Table 439 | 15 |
| [[#wms_product_out_lot_detail]] | wms_product_out_lot_detail  | 13 |
| [[#wms_product_out_ref]] | wms_product_out_ref / Table 438 | 3 |
| [[#wms_product_out_serial_detail]] | wms_product_out_serial_detail  | 5 |
| [[#wms_product_receive]] | wms_product_receive / Table 431 | 17 |
| [[#wms_product_receive_detail]] | wms_product_receive_detail  | 14 |
| [[#wms_product_receive_lot_detail]] | wms_product_receive_lot_detail  | 13 |
| [[#wms_product_receive_ref]] | wms_product_receive_ref  | 3 |
| [[#wms_product_receive_serial_detail]] | wms_product_receive_serial_detail  | 10 |
| [[#wms_product_trans]] | wms_product_trans / wms_product_trans | 11 |
| [[#wms_product_trans_lot]] | wms_product_trans_lot / wms_product_trans_lot | 11 |
| [[#wms_serial_master]] | wms_serial_master / wms_serial_master | 10 |
| [[#wms_workers]] | wms_workers / wms_workers | 5 |

## erp_package_reason

**เหตุผลการเบิกภาชนะ** — ERP Package Reason

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(50) |  |
| `name_1` | ชื่อ |  | varchar(255) |  |
| `name_2` | ชื่อ (อังกฤษ) |  | varchar(255) | ✓ |
| `guid_code` | GUID Code |  | varchar(50) | ✓ |

## ic_inventory_package

**ภาชนะบรรจุสินค้า** — IC Inventory Package

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `code` | รหัสภาชนะ |  | varchar(50) |  |
| `name_1` | ชื่อ *(resource only)* |  | char |  |
| `stand_value` | ตัวตั้ง |  | float | ✓ |
| `divide_value` | ตัวหาร |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |

## ic_package_trans

**รายวันภาชนะ** — IC Package Trans

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `trans_type` | ระบบรายวัน |  | smallint |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `cust_code` | รหัสลูกค้า |  | varchar(50) | ✓ |
| `doc_ref_no` | เลขที่เอกสารอ้างอิง |  | varchar(50) | ✓ |
| `doc_ref_date` | วันที่เอกสารอ้างอิง |  | smalldatetime | ✓ |
| `doc_time` | เวลา |  | varchar(25) | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(50) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(50) | ✓ |
| `lastedit_datetime` | เวลาแก้ไขเอกสารล่าสุด |  | datetime | ✓ |

## ic_package_trans_detail

**รายละเอียดรายวันภาชนะ** — IC Package Trans Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `trans_type` | ระบบรายวัน |  | smallint |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `item_code` | รหัสสินค้า/ภาชนะ |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า/ภาชนะ |  | varchar(500) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `stand_value` | อัตราส่วนตัวตั้ง |  | float | ✓ |
| `divide_value` | อัตราส่วนตัวหาร |  | float | ✓ |

## ic_wms_trans

**รายวันทั้งหมด** — IC - Transection · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Doc Reference | varchar(25) | ✓ |
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
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `is_cancel` | ยกเลิกเอกสาร |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิก |  | varchar(255) | ✓ |
| `cancel_datetime` | วันเวลายกเลิก |  | datetime | ✓ |

index: `ic_wms_trans_IC_wms_TRANS_PK_PRIMARY`(doc_no,trans_flag), `PK_ic_wms_trans_last_status`(last_status), `PK_ic_wms_trans_used_status`(used_status), `ic_wms_trans_cust_code`(cust_code), `ic_wms_trans_total_amount`(total_amount), `PK_wms_used_status_2`(used_status_2), `ic_wms_trans_doc_success`(doc_success), `ic_wms_trans_trans_flag`(trans_flag), `ic_wms_trans_not_approve_1`(not_approve_1), `ic_wms_trans_on_hold`(on_hold), `ic_wms_trans_approve_status`(approve_status), `ic_wms_trans_expire_status`(expire_status), `ic_wms_trans_is_pos`(is_pos), `ic_wms_trans_pos_bill_type`(pos_bill_type), `ic_wms_trans_pos_bill_change`(pos_bill_change), `ic_wms_trans_auto_create`(auto_create), `ic_wms_trans_advance_amount`(advance_amount), `ic_wms_trans_advance_pos_id`(pos_id), `ic_wms_trans_due_date`(due_date)

## ic_wms_trans_detail

**รายละเอียดรายวัน** — IC - Transection Detail · edition: `SMLERP`

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
| `line_number` | บรรทัด | Line Number | smallint | ✓ |
| `ref_doc_no` | อ้างอิง | Ref Doc No | varchar(25) | ✓ |
| `ref_doc_date` | อ้างอิง วันที่ | Ref Date | smalldatetime | ✓ |
| `ref_line_number` | อ้างอิง บรรทัด | Ref Line Number | smallint | ✓ |
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
| `bank_name` | ธนาคาร *(resource only)* |  | char |  |
| `bank_branch` | สาขา *(resource only)* |  | char |  |
| `chq_number` | เลขที่เช็ค |  | varchar(25) | ✓ |
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
| `lot_number_1` | เลข LOT |  | varchar(25) | ✓ |
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
| `mfn_name` | ผู้ผลิต |  | varchar(255) | ✓ |
| `start_qty` | จำนวนเริ่มต้น *(resource only)* |  | char |  |
| `end_qty` | จำนวนสินสุด *(resource only)* |  | char |  |
| `department` | แผนก *(resource only)* |  | char |  |
| `allocate` | การจัดสรร *(resource only)* |  | char |  |
| `project` | โครงการ *(resource only)* |  | char |  |
| `price_guid` | Price GUID |  | varchar(50) | ✓ |

index: `ic_wms_trans_detail_trans_type`(trans_type), `ic_wms_trans_detail_trans_flag`(trans_flag), `ic_wms_trans_detail_cust_code`(cust_code), `ic_wms_trans_detail_item_code`(item_code), `ic_wms_trans_detail_doc_no`(doc_no), `ic_wms_trans_detail_process_cost`(doc_date,doc_time,doc_no,line_number), `ic_wms_trans_detail_last_status`(last_status), `ic_wms_trans_detail_doc_date`(doc_date), `ic_wms_trans_detail_doc_time`(doc_time), `ic_wms_trans_detail_doc_date_and_time`(doc_date,doc_time), `ic_wms_trans_detail_docno_trans_flag`(doc_no,trans_flag), `ic_wms_trans_detail_process_cost_2`(doc_date_calc,doc_time_calc,trans_flag,doc_no,line_number), `ic_wms_trans_detail_doc_date_and_time_2`(doc_date_calc,doc_time_calc), `ic_wms_trans_detail_doc_date_2`(doc_date_calc), `ic_wms_trans_detail_doc_time_2`(doc_time_calc), `ic_wms_trans_detail_taxtype`(tax_type), `ic_wms_trans_detail_icpos`(is_pos), `ic_wms_trans_detail_barcode_1`(barcode), `ic_wms_trans_detail_barcode_2`(barcode,cust_code), `ic_wms_trans_detail_auto_create`(auto_create), `ic_wms_trans_detail_stand_value`(stand_value), `ic_wms_trans_detail_divide_value`(divide_value), `ic_wms_trans_detail_item_type`(item_type), `ic_wms_trans_detail_is_serial_number`(is_serial_number), `ic_wms_trans_detail_vat_type`(vat_type), `ic_wms_trans_detail_barcode_3`(barcode,cust_code,doc_date,doc_time), `ic_wms_trans_detail_ref_doc_no`(ref_doc_no), `ic_wms_trans_detail_inquiry_type`(inquiry_type), `ic_wms_trans_detail_line_number`(line_number), `ic_wms_trans_detail_whcode`(wh_code), `ic_wms_trans_detail_selfcode`(shelf_code), `ic_wms_trans_detail_whcode_shelfcode`(wh_code,shelf_code), `ic_wms_trans_detail_unit_code`(unit_code)

## wms_boxes

**wms_boxes** — wms_boxes

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | Code |  | varchar(50) |  |
| `wide` | Wide |  | float | ✓ |
| `long` | Long |  | float | ✓ |
| `high` | Height |  | float | ✓ |
| `image_src` | Image Source |  | image | ✓ |
| `status` | Status |  | smallint | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_boxes_detail

**wms_boxes_detail** — wms_boxes_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `box_code` | Box Code |  | varchar(50) |  |
| `ref_doc_no` | Ref Doc No |  | varchar(50) | ✓ |
| `is_from_cart` | Is From Cart |  | smallint |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `qty` | Qty |  | float |  |
| `unit_code` | Unit code |  | varchar(50) |  |
| `status` | Status |  | smallint | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |

## wms_boxes_lot_detail

**wms_boxes_lot_detail** — wms_boxes_lot_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `box_code` | Box Code |  | varchar(50) |  |
| `ref_doc_no` | Ref Doc No |  | varchar(50) | ✓ |
| `is_from_cart` | Is From Cart |  | smallint |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(255) |  |
| `qty` | Qty |  | float | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |
| `status` | Status |  | smallint | ✓ |

## wms_boxes_trans

**wms_boxes_trans** — wms_boxes_trans

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_guid` | Trans GUID |  | varchar(50) |  |
| `from_box_code` | From Box Code |  | varchar(50) | ✓ |
| `from_shelf_code` | From Shelf Code |  | varchar(50) | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |
| `to_shelf_code` | To Shelf Code |  | varchar(50) | ✓ |
| `created_at` | Create At |  | datetime | ✓ |

## wms_boxes_trans_detail

**wms_boxes_trans_detail** — wms_boxes_trans_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_guid` | Trans GUID |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `qty` | Qty |  | float |  |
| `unit_code` | Unit Code |  | varchar(50) | ✓ |
| `created_at` | Create At |  | datetime | ✓ |

## wms_boxes_trans_lot

**wms_boxes_trans_lot** — wms_boxes_trans_lot

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_guid` | Trans GUID |  | varchar(50) |  |
| `ref_doc_no` | Ref Doc No |  | varchar(50) | ✓ |
| `item_code` | Item Code |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(255) |  |
| `qty` | Qty |  | float |  |
| `created_at` | Created At |  | datetime | ✓ |

## wms_cart

**wms cart** — Table 432

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_guid` | Cart GUID |  | varchar(50) |  |
| `receive_doc_no` | เลขที่ใบรับ |  | varchar(50) | ✓ |
| `ref_doc_no` | เอกสารอ้างอิง |  | varchar(50) | ✓ |
| `creator_code` | ผู้สร้าง |  | varchar(50) | ✓ |
| `create_datetime` | วัน/เวลาสร้าง |  | datetime | ✓ |
| `last_update_datetime` | วัน/เวลา แก้ไขล่าสุด |  | datetime | ✓ |
| `last_update_user_code` | ผู้แก้ไขล่าสุด |  | varchar(50) | ✓ |
| `device_id` | Device ID |  | varchar(150) | ✓ |
| `remark` | หมายเหตุ |  | varchar(1000) | ✓ |
| `supplier_code` | รับสินค้าจาก |  | varchar(50) | ✓ |
| `cart_type` | ประเภทตระกร้า |  | smallint | ✓ |
| `box_code` | รหัส Box |  | varchar(50) | ✓ |
| `warehouse_code` | Warehouse |  | varchar(50) | ✓ |
| `shelf_code` | Shelf |  | varchar(50) | ✓ |
| `branch_code` | Branch Code |  | varchar(50) | ✓ |
| `worker_code` | Worker Code |  | varchar(100) | ✓ |

## wms_cart_detail

**wms_cart_detail** — Table 433

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_guid` | Cart GUID |  | varchar(50) |  |
| `ref_doc_no` | เอกสารอ้างอิง |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `price` | ราคา |  | float | ✓ |
| `sum_amount` | มูลค่า |  | float | ✓ |
| `discount` | ส่วนลด |  | varchar(100) | ✓ |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |

## wms_cart_lot

**WMS Cart Lot**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_guid` | Cart GUID |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) | ✓ |
| `lot_number` | Lot Number |  | varchar(50) | ✓ |
| `qty` | Qty |  | int | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |

## wms_cart_ref

**wms_cart_ref**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_guid` | Cart GUID |  | varchar(50) |  |
| `ref_doc_no` | Doc No Ref |  | varchar(25) | ✓ |
| `line_order` | Line order |  | smallint | ✓ |

## wms_cart_serial

**wms_cart_serial**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_guid` | Cart GUID |  | varchar(50) |  |
| `item_code` | item code |  | varchar(50) |  |
| `serial_number` | Serial Number |  | varchar(255) | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |

## wms_job

**wms_job** — wms_job

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `from_shelf` | From Shelf |  | varchar(50) | ✓ |
| `to_shelf` | To Shelf |  | varchar(50) | ✓ |
| `worker_code` | Worker Code |  | varchar(50) | ✓ |
| `job_date` | Job Date |  | smalldatetime |  |
| `job_time` | Job Time |  | varchar(20) |  |
| `remark` | Remark |  | varchar(255) | ✓ |
| `last_update_date_time_now` | Last Update |  | datetime | ✓ |
| `status` | Status |  | smallint | ✓ |
| `job_name` | Job Name |  | varchar(255) | ✓ |
| `is_readed` | Is Readed |  | boolean | ✓ |
| `job_code` | Job Code |  | varchar(50) | ✓ |
| `job_type` | Job Type |  | varchar(10) | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |
| `box_type` | Box Type |  | varchar(10) | ✓ |
| `ref_doc_no` | Ref Doc No |  | varchar(50) | ✓ |
| `is_manual` | Is Manual |  | smallint | ✓ |

## wms_job_detail

**wms_job_detail** — wms_job_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `job_code` | Job Code |  | varchar(50) |  |
| `box_code` | Box Code |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `unit_code` | Unit Code |  | varchar(50) |  |
| `qty` | Qty |  | float |  |
| `from_shelf` | From Shelf |  | varchar(50) | ✓ |
| `to_shelf` | To Shelf |  | varchar(50) | ✓ |
| `created_at` | Created At |  | datetime | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |
| `item_name` | Item Name |  | varchar(250) | ✓ |
| `last_update_date_time_now` | แก้ไขล่าสุด |  | datetime | ✓ |

## wms_job_lot_detail

**wms_job_lot_detail** — wms_job_lot_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `job_code` | Job Code |  | varchar(50) |  |
| `box_code` | Box Code |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(50) |  |
| `qty` | Qty |  | float |  |
| `from_shelf` | From Shelf |  | varchar(50) | ✓ |
| `to_shelf` | To Shelf |  | varchar(50) | ✓ |
| `created_at` | Created At |  | datetime | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |

## wms_location

**wms_location** — wms_location

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | Code |  | varchar(50) |  |
| `branch_code` | Branch Code |  | varchar(50) | ✓ |
| `warehouse_code` | Warehouse Code |  | varchar(50) | ✓ |
| `status` | Status |  | smallint | ✓ |

## wms_pracel

**wms_pracel**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `pracel_guid` |  |  | char |  |
| `ref_doc_no` |  |  | char |  |
| `cust_code` |  |  | char |  |
| `address` |  |  | char |  |
| `cust_name` |  |  | char |  |

## wms_product_adj_stock

**wms_product_adj_stock** — wms_product_adj_stock

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Doc No |  | varchar(50) |  |
| `doc_date` | Doc Date |  | smalldatetime |  |
| `doc_time` | Doc Time |  | varchar(20) |  |
| `doc_type` | Doc Type |  | varchar(15) | ✓ |
| `remark` | Remark |  | varchar(255) | ✓ |
| `create_datetime` | Create Date Time |  | datetime | ✓ |
| `creator_code` | Creator Code |  | varchar(50) | ✓ |
| `last_update_datetime` | Last Update Date Time |  | datetime | ✓ |
| `last_update_user_code` | Last Update User Code |  | varchar(50) | ✓ |
| `status` | Status |  | smallint | ✓ |

## wms_product_adj_stock_detail

**wms_product_adj_stock_detail** — wms_product_adj_stock_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Doc No |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `unit_code` | Unit Code |  | varchar(50) |  |
| `box_code` | Box Code |  | varchar(50) |  |
| `shelf_code` | Shelf Code |  | varchar(50) |  |
| `qty` | Qty |  | float | ✓ |
| `current_qty` | Current Qty |  | float | ✓ |
| `diff_qty` | Diff Qty |  | float | ✓ |
| `last_update_datetime` | Last Update |  | datetime | ✓ |
| `last_update_date_time_now` | Last Update Now |  | datetime | ✓ |

## wms_product_adj_stock_lot_detail

**wms_product_adj_stock_lot_detail** — wms_product_adj_stock_lot_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Doc No |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(255) | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |
| `qty` | Qty |  | float |  |
| `current_qty` | Current Qty |  | float | ✓ |
| `diff_qty` | Diff Qty |  | float | ✓ |
| `last_update_datetime` | Last Update |  | datetime | ✓ |
| `last_update_date_time_now` | Last Update Now |  | datetime | ✓ |

## wms_product_out

**wms_product_out**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Generate Doc No |  | varchar(50) |  |
| `doc_date` | วันที่สร้างเอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `warehouse_code` | คลังสินค้า |  | varchar(32) | ✓ |
| `branch_code` | สาขา |  | varchar(32) | ✓ |
| `customer_code` | จ่ายสินค้าให้กับ |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(50) | ✓ |
| `last_update_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `last_update_user_code` | ผู้แก้ไขล่าสุด |  | varchar(50) | ✓ |
| `total_amount` | รวมมูลค่า |  | float | ✓ |
| `ref_doc_no` | Ref Doc No |  | varchar(50) | ✓ |
| `doc_type` | Doc Type |  | smallint | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_out_detail

**wms_product_out_detail** — Table 439

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(20) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า |  | varchar(255) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `discount` | ส่วนลด |  | varchar(100) | ✓ |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |
| `sum_amount` | รวมมูลค่า |  | float | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |
| `last_update_datetime` | แก้ไขล่าสุด |  | datetime | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_out_lot_detail

**wms_product_out_lot_detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_out_doc` | ref_out_doc |  | varchar |  |
| `ref_out_date` | ref_out_date |  | smalldatetime | ✓ |
| `item_code` | item_code |  | varchar |  |
| `lot_number` | lot_number |  | varchar |  |
| `product_week` | product_week |  | smallint | ✓ |
| `product_year` | product_year |  | smallint | ✓ |
| `mfd_date` | mfd_date |  | smalldatetime | ✓ |
| `mfd_name` | mfd_name |  | varchar(255) | ✓ |
| `expire_date` | expire_date |  | smalldatetime | ✓ |
| `qty` | qty |  | smallint | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_out_ref

**wms_product_out_ref** — Table 438

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่ใบรับสินค้า |  | varchar(50) |  |
| `ref_doc_no` | เอกสารอ้างอิง |  | varchar(50) |  |
| `line_order` | ลำดับ |  | smallint |  |

## wms_product_out_serial_detail

**wms_product_out_serial_detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_out_doc` | ref_out_doc |  | varchar(50) |  |
| `ref_out_date` | ref_out_date |  | smalldatetime |  |
| `item_code` | item_code |  | varchar(50) | ✓ |
| `serial_number` | serial_number |  | varchar(255) | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |

## wms_product_receive

**wms_product_receive** — Table 431

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Generate Doc No |  | varchar(50) |  |
| `doc_date` | วันที่สร้างเอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `warehouse_code` | คลังสินค้า |  | varchar(32) | ✓ |
| `branch_code` | สาขา |  | varchar(32) | ✓ |
| `supplier_code` | รับสินค้าจาก |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(50) | ✓ |
| `last_update_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `last_update_user_code` | ผู้แก้ไขล่าสุด |  | varchar(50) | ✓ |
| `total_amount` | รวมมูลค่า |  | float | ✓ |
| `ref_doc_no` | ref_doc_no |  | varchar(50) | ✓ |
| `doc_type` | doc_type |  | smallint | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_receive_detail

**wms_product_receive_detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(20) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า |  | varchar(255) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `discount` | ส่วนลด |  | varchar(100) | ✓ |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |
| `sum_amount` | รวมมูลค่า |  | float | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_receive_lot_detail

**wms_product_receive_lot_detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_rec_doc` | ref_rec_doc |  | varchar(50) |  |
| `ref_rec_date` | ref_rec_date |  | smalldatetime | ✓ |
| `item_code` | item_code |  | varchar(50) |  |
| `lot_number` | lot_number |  | varchar(255) |  |
| `product_week` | product_week |  | smallint | ✓ |
| `product_year` | product_year |  | smallint | ✓ |
| `mfd_date` | mfd_date |  | smalldatetime | ✓ |
| `mfd_name` | mfd_name |  | varchar(255) | ✓ |
| `expire_date` | expire_date |  | smalldatetime | ✓ |
| `qty` | qty |  | smallint | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |
| `box_code` | Box Code |  | varchar(50) | ✓ |
| `shelf_code` | Shelf Code |  | varchar(50) | ✓ |

## wms_product_receive_ref

**wms_product_receive_ref**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่ใบรับสินค้า |  | varchar(50) |  |
| `ref_doc_no` | เอกสารอ้างอิง |  | varchar(50) |  |
| `line_order` | ลำดับ |  | smallint |  |

## wms_product_receive_serial_detail

**wms_product_receive_serial_detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_rec_doc` | ref_rec_doc |  | varchar(50) |  |
| `ref_rec_date` | ref_rec_date |  | smalldatetime |  |
| `item_code` | item_code |  | varchar(50) |  |
| `serial_number` | serial_number |  | varchar(255) |  |
| `product_week` | product_week |  | smallint | ✓ |
| `product_year` | product_year |  | smallint | ✓ |
| `mfd_date` | mfd_date |  | smalldatetime | ✓ |
| `mfd_name` | mfd_name |  | varchar(255) | ✓ |
| `expire_date` | expire_date |  | smalldatetime | ✓ |
| `last_update_date_time_now` | last_update_date_time_now |  | datetime | ✓ |

## wms_product_trans

**wms_product_trans** — wms_product_trans

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_doc_no` | Ref Doc No |  | varchar(50) |  |
| `from_box_code` | From Box Code |  | varchar(50) | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |
| `from_shelf_code` | From Shelf Code |  | varchar(50) | ✓ |
| `to_shelf_code` | To Shelf Code |  | varchar(50) | ✓ |
| `item_code` | Item Code |  | varchar(50) | ✓ |
| `unit_code` | Unit Code |  | varchar(50) | ✓ |
| `qty` | Qty |  | float | ✓ |
| `created_at` | Created At |  | datetime | ✓ |
| `ref_doc_type` | Ref Doc Type |  | varchar(50) | ✓ |
| `trans_guid` | Trans GUID |  | varchar(50) | ✓ |

## wms_product_trans_lot

**wms_product_trans_lot** — wms_product_trans_lot

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_doc_no` | Ref Doc No |  | varchar(50) |  |
| `item_code` | Item Code |  | varchar(50) |  |
| `unit_code` | Unit Code |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(255) |  |
| `qty` | Qty |  | float |  |
| `created_at` | Created At |  | datetime | ✓ |
| `from_box_code` | From Box Code |  | varchar(50) | ✓ |
| `to_box_code` | To Box Code |  | varchar(50) | ✓ |
| `from_shelf_code` | From Shelf Code |  | varchar(50) | ✓ |
| `to_shelf_code` | To Shelf Code |  | varchar(50) | ✓ |
| `trans_guid` | Trans GUID |  | varchar(50) | ✓ |

## wms_serial_master

**wms_serial_master** — wms_serial_master

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ref_rec_doc` | Ref Rec Doc |  | varchar(50) |  |
| `ref_rec_date` | Ref Rec Date |  | smalldatetime | ✓ |
| `item_code` | Item Code |  | varchar(50) | ✓ |
| `product_week` | Product Week |  | smallint | ✓ |
| `product_year` | Product Year |  | smallint | ✓ |
| `mfd_date` | Mfd Date |  | smalldatetime | ✓ |
| `mfd_name` | Mfd Name |  | varchar(255) | ✓ |
| `expire_date` | Expire Date |  | smalldatetime | ✓ |
| `serial_number` | Serial Number |  | varchar(255) | ✓ |
| `last_update_date_time_now` | Last Update Now |  | datetime | ✓ |

## wms_workers

**wms_workers** — wms_workers

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | Code |  | varchar(50) |  |
| `name_1` | Name 1 |  | varchar(255) | ✓ |
| `description` | Description |  | varchar(255) | ✓ |
| `user_code` | User Code |  | varchar(50) | ✓ |
| `status` | Status |  | smallint | ✓ |

