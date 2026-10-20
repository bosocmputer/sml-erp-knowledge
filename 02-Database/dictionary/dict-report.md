---
tags: [sml, dictionary, report, generated]
module: Report
---
# พจนานุกรม: Report — รายงาน

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#resource_report]] | Resource Report / Resource Report | 308 |
| [[#resource_report_bank]] | รายงานเช็คเงินสดธนาคาร / Report Bank | 19 |
| [[#resource_report_color]] | resource_report_color / resource_report_color | 23 |
| [[#resource_report_column]] | resource_report_column / resource_report_column | 64 |
| [[#resource_report_form]] | Resource Report Form / Resource Report Form | 42 |
| [[#resource_report_ic_column]] | ic_report_column  | 55 |
| [[#resource_report_ic_report_name]] | ic_report_name  | 29 |
| [[#resource_report_name]] | resource_report_name / resource_report_name | 31 |
| [[#resource_report_vat]] | รายงานภาษีมูลค่าเพิ่ม / Vat Report | 103 |

## resource_report

**Resource Report** — Resource Report · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `from_item_code` | จากรหัสสินค้า *(resource only)* | From Item | char |  |
| `to_item_code` | ถึงรหัสสินค้า *(resource only)* | To Item | char |  |
| `order_by_item` | เรียงตามรหัสสินค้า *(resource only)* | Order by Item | char |  |
| `order_by_wh` | เรียงตามคลังสินค้า *(resource only)* | Order by WH | char |  |
| `order_by_group` | เรียงตามกลุ่มสินค้า *(resource only)* | Order_by ฌroup | char |  |
| `order_by_brand` | เรียงตามยี่ห้อสินค้า *(resource only)* | Order by Brand | char |  |
| `order_by_format` | เรียงตามรูปแบบสินค้า *(resource only)* | Order by Format | char |  |
| `order_by_type` | เรียงตามชนิดสินค้า *(resource only)* | Order by Type | char |  |
| `order_by_category` | เรียงตามหมวดสินค้า *(resource only)* | Order by Category | char |  |
| `print_report_at_date` | พิมพ์รายงานย้อนหลัง ณ วันที่ *(resource only)* | Print Report at Date | char |  |
| `displpay_item_balance_equal_zero` | แสดงยอดคงเหลือสินค้าที่มีเท่ากับศูนย์ *(resource only)* | displpay Item balance equal Zero | char |  |
| `display_item_in_warehouse` | แสดงเฉพาะรายการสินค้าที่มีในคลัง *(resource only)* | Display Item in Warehouse | char |  |
| `display_amount_item` | แสดงยอดยกมา,ยอดยกไป *(resource only)* | Display amount Iitem | char |  |
| `print_all` | พิมพ์รายการทั้งหมด *(resource only)* | Print all | char |  |
| `display_lot_item` | แสดง Lot สินค้า *(resource only)* | Display Lot Item | char |  |
| `display_warehouse` | แสดงคลังสินค้า *(resource only)* | Display Warehouse | char |  |
| `display_shelf` | แสดงที่เก็บสินค้า *(resource only)* | Display Shelf | char |  |
| `display_only_total_price` | แสดงเฉพาะยอดรวม *(resource only)* | Display Only Total Price | char |  |
| `from_date` | จากวันที่ *(resource only)* | From Date | char |  |
| `to_date` | ถึงวันที่ *(resource only)* | To Date | char |  |
| `from_date_end_insulance` | จากวันที่หมดประกัน *(resource only)* | From Date end Insulance | char |  |
| `to_date_end_insulance` | ถึงวันที่หมดประกัน *(resource only)* | To Date end Insulance | char |  |
| `status_item` | สถานะสินค้า *(resource only)* | Status Item | char |  |
| `from_serail_no` | จาก Serail No *(resource only)* | From Serail No | char |  |
| `to_serail_no` | ถึง Serail No *(resource only)* | To Serail No | char |  |
| `from_department` | จากแผนก *(resource only)* | From Department | char |  |
| `to_department` | ถึงแผนก *(resource only)* | To Department | char |  |
| `from_warehouse` | จากคลัง *(resource only)* | From Warehouse | char |  |
| `to_warehouse` | ถึงคลัง *(resource only)* | To Warehouse | char |  |
| `from_docno` | จากเลขที่เอกสาร *(resource only)* | From Doc No | char |  |
| `to_docno` | ถึงเลขที่เอกสาร *(resource only)* | To Doc No | char |  |
| `from_docdate` | จากวันที่เอกสาร *(resource only)* | From Document Date | char |  |
| `to_docdate` | ถึงวันที่เอกสาร *(resource only)* | To Document Date | char |  |
| `from_group` | จากกลุ่มสินค้า *(resource only)* | From Group | char |  |
| `to_group` | ถึงกลุ่มสินค้า *(resource only)* | To Group | char |  |
| `from_type` | จากชนิดสินค้า *(resource only)* | From Type | char |  |
| `to_type` | ถึงชนิดสินค้า *(resource only)* | To Type | char |  |
| `from_category` | จากหมวดสินค้า *(resource only)* | From Category | char |  |
| `to_category` | ถึงหมวดสินค้า *(resource only)* | To Category | char |  |
| `from_format` | จากรูปแบบสินค้า *(resource only)* | From Format | char |  |
| `to_format` | ถึงรูปแบบสินค้า *(resource only)* | To Format | char |  |
| `from_brand` | จากยี่ห้อสินค้า *(resource only)* | From Brand | char |  |
| `to_brand` | ถึงยี่ห้อสินค้า *(resource only)* | To Brand | char |  |
| `display_serial` | แสดง Serial *(resource only)* | Display Serial | char |  |
| `from_allocation` | จากการจัดสรร *(resource only)* | From Allocation | char |  |
| `to_allocation` | ถึงการจัดสรร *(resource only)* | To Allocation | char |  |
| `total_item` | รวมรายการสินค้า *(resource only)* | Total Item | char |  |
| `print_by_format_revue` | พิมพ์ตามรูปแบบข้อกำหนดของกรมสรรพากร *(resource only)* | Print by Format Revue | char |  |
| `averrage` | แบบเฉลี่ย *(resource only)* | Average | char |  |
| `fifo` | แบบ fifo *(resource only)* | Fifo | char |  |
| `standard` | แบบมาตรฐาน *(resource only)* | Standard | char |  |
| `panel_costs` | ต้นทุนแผง *(resource only)* | Panel Costs | char |  |
| `not_display_amount_balance_item` | ไม่แสดงจำนวน ต้นทุน มูลค่า คงเหลือ สินค้า *(resource only)* | Not Display Amount Balance Item | char |  |
| `display_serial_emei` | แสดง Serial / Emei *(resource only)* | Display Serial / Emei | char |  |
| `display_report_movement_by_date` | แสดงรายงานเคลื่อนไหวตามวันที่ *(resource only)* | Display Report Movement by Date | char |  |
| `print_total_warehouse` | พิมพ์คลังรวม *(resource only)* | Print Total Warehouse | char |  |
| `print_split_warehouse` | พิมพ์แยกคลัง *(resource only)* | Print Split Warehouse | char |  |
| `display_item_name2` | แสดงชื่อสินค้า 2 *(resource only)* | Display Item Name 2 | char |  |
| `display_item_balance_now_minus_cheque_item` | แสดงยอดคงเหลือปัจจุบันหัก ยอดใบสั่งจ่ายสินค้า *(resource only)* | Display Item Balance Now Minus  Cheque Item | char |  |
| `display_report_by_group_item` | แสดงสินค้าตามกลุ่มสินค้า *(resource only)* | Display Report by Group Item | char |  |
| `from_payable` | จากรหัสเจ้าหนี้ *(resource only)* | From Payable | char |  |
| `to_payable` | ถึงรหัสเจ้าหนี้ *(resource only)* | To Payable | char |  |
| `from_sale_person` | จากรหัสพนักงานขาย *(resource only)* | From Sale Person | char |  |
| `to_sale_person` | ถึงรหัสพนักงานขาย *(resource only)* | To Sale Person | char |  |
| `not_list_account` | ไม่แสดงรายชื่อบัญชี *(resource only)* | Not Display List Account | char |  |
| `from_period ` | จากงวดที่ *(resource only)* | From Period | char |  |
| `to_period` | ถึงงวดที่ *(resource only)* | To Period | char |  |
| `payable_according_new_page` | ขึ้นหน้าใหม่ตามเจ้าหนี้ *(resource only)* | Payable According to a New Page | char |  |
| `balance_at_date` | ยอดคงเหลือ ณ วันที่ *(resource only)* | Balance At Date | char |  |
| `from_bill` | จากวันที่ออกบิล *(resource only)* | From Bill | char |  |
| `to_bill` | ถึงวันที่ออกบิล *(resource only)* | To Bill | char |  |
| `from_due_date` | จากวันที่ครบกำหนด *(resource only)* | From Due Date | char |  |
| `to_due_date` | ถึงวันที่ครบกำหนด *(resource only)* | To Due Date | char |  |
| `display_only_total_amount` | แสดงเฉพาะยอดรวม *(resource only)* | Display Only Total Amount | char |  |
| `from_amount ` | จากจำนวนเงิน *(resource only)* | From Amount | char |  |
| `to_amount ` | ถึงจำนวนเงิน *(resource only)* | To Amount | char |  |
| `from_credit_day` | จากเครดิต(วัน) *(resource only)* | From Credit (Day) | char |  |
| `to_credit_day` | ถึงเครดิต(วัน) *(resource only)* | To Credit (Day) | char |  |
| `not_total_lift_zero` | ไม่แสดงรายการยอดยกไปเท่ากับศูนย์ *(resource only)* | Not Display Total raised to Equal zero | char |  |
| `from_bill_of_landing_place` | จากเลขที่ใบรับวางบิล *(resource only)* | From Bill of Landing Place | char |  |
| `to_bill_of_landing_place` | ถึงเลขที่ใบรับวางบิล *(resource only)* | To Bill of Landing Place | char |  |
| `from_invoice` | จากเลขที่ใบส่งของ *(resource only)* | From Invoice | char |  |
| `to_invoice` | ถึงเลขที่ใบส่งของ *(resource only)* | To Invoice | char |  |
| `from_invoice_date` | จากวันที่ใบส่งของ *(resource only)* | From Invoice Date | char |  |
| `to_invoice_date` | ถึงวันที่ใบส่งของ *(resource only)* | To Invoice Date | char |  |
| `from_project` | จากโครงการ *(resource only)* | From Project | char |  |
| `to_project` | ถึงโครงการ *(resource only)* | To Project | char |  |
| `from_currency` | จากสกุลเงิน *(resource only)* | From Currency | char |  |
| `to_currency` | ถึงสกุลเงิน *(resource only)* | To Currency | char |  |
| `annual_period` | ประจำงวดที่ *(resource only)* | Annual Period | char |  |
| `order_by` | เรียงตาม *(resource only)* | Order By | char |  |
| `display_cost_unit` | แสดงต้นทุน / หน่วย *(resource only)* | Display Cost Unit | char |  |
| `item_code` | รหัสสินค้า *(resource only)* | Item Code | char |  |
| `item_warehouse_code` | รหัสคลังสินค้า *(resource only)* | Item Warehouse Code | char |  |
| `item_group_code` | รหัสกลุ่มสินค้า *(resource only)* | Item Group Code | char |  |
| `item_type_code` | รหัสประเภทสินค้า *(resource only)* | Item Type Code | char |  |
| `item_brand_code` | รหัสยี่ห้อสินค้า *(resource only)* | Item Brand Code | char |  |
| `from_shelf` | จากที่เก็บ *(resource only)* | From Shelf | char |  |
| `to_shelf` | ถึงที่เก็บ *(resource only)* | To Shelf | char |  |
| `from_widen` | จากผู้เบิก *(resource only)* | From Widen | char |  |
| `to_widen` | ถึงผู้เบิก *(resource only)* | To Widen | char |  |
| `print_all_wh_and_other_wh` | พิมพ์คลังรวมและคลังอื่น ๆ *(resource only)* | Print All Wh and Other Wh | char |  |
| `from_date_import` | จากวันที่รับเข้า *(resource only)* | From Date Import | char |  |
| `to_date_import` | ถึงวันที่รับเข้า *(resource only)* | To Date Import | char |  |
| `from_status_item` | จากสถานะสินค้า *(resource only)* | From Status Item | char |  |
| `to_status_item` | ถึงสถานะสินค้า *(resource only)* | To Status Item | char |  |
| `from_end_date` | จากวันที่ครบกำหนด *(resource only)* | From End Date | char |  |
| `to_end_date` | ถึงวันที่ครบกำหนด *(resource only)* | To End Date | char |  |
| `all` | ทั้งหมด *(resource only)* | All | char |  |
| `in_hand` | ในมือ *(resource only)* | In Hand | char |  |
| `up_money_already` | ขึ้นเงินแล้ว *(resource only)* | Up Money Already | char |  |
| `cancel` | ยกเลิก *(resource only)* | Cancel | char |  |
| `from_daily_day` | จากสมุดรายวัน *(resource only)* | From Daily Day | char |  |
| `to_daily_day` | ถึงสมุดรายวัน *(resource only)* | To Daily Day | char |  |
| `from_sale_office` | จากสำนักงานขาย *(resource only)* | From Sale Office | char |  |
| `to_sale_office` | ถึงสำนักงานขาย *(resource only)* | To Sale Office | char |  |
| `cheque_deposit_bank` | เช็คฝากธนาคาร *(resource only)* | Cheque Deposit Bank | char |  |
| `cheque_pass` | เช็คผ่าน *(resource only)* | Cheque Pass | char |  |
| `cheque_return` | เช็คคืน *(resource only)* | Cheque Return | char |  |
| `cheque_cancel` | เช็คยกเลิก *(resource only)* | Cheque Cancel | char |  |
| `sale_fall_cheque` | ขายลดเช็ค *(resource only)* | Sale Fall Cheque | char |  |
| `cheque_return_bank` | เช็คคืนฝากธนาคาร *(resource only)* | Cheque Return Bank | char |  |
| `from_book_code` | จากรหัสสมุด *(resource only)* | From Book Code | char |  |
| `to_book_code` | ถึงรหัสสมุด *(resource only)* | To Book Code | char |  |
| `from_book_no` | จากเลขที่สมุด *(resource only)* | From Book No | char |  |
| `to_book_no` | ถึงเลขที่สมุด *(resource only)* | To Book No | char |  |
| `date` | วันที่ *(resource only)* | Date | char |  |
| `warehouse` | คลังสินค้า *(resource only)* | Warehouse | char |  |
| `date_import` | วันที่รับ *(resource only)* | Date Import | char |  |
| `department` | แผนก *(resource only)* | Department | char |  |
| `widen` | ผู้เบิก *(resource only)* | Widen | char |  |
| `allocation` | การจัดสรร *(resource only)* | Allocation | char |  |
| `in_stock` | ในสต๊อก *(resource only)* | In Stock | char |  |
| `widen_already` | เบิกแล้ว *(resource only)* | Widen Already | char |  |
| `sale_already` | ขายแล้ว *(resource only)* | Sale Already | char |  |
| `from_unit` | จากหน่วยนับ *(resource only)* | From Unit | char |  |
| `to_unit` | ถึงหน่วยนับ *(resource only)* | To Unit | char |  |
| `cheque_in_hand` | เช็คในมือ *(resource only)* | Cheque In Hand | char |  |
| `select_status_cheque` | เลือกสถานะเช็ค *(resource only)* | Select Status Cheque | char |  |
| `from_ar` | จากลูกหนี้ *(resource only)* | From Ar | char |  |
| `to_ar` | ถึงลูกหนี้ *(resource only)* | To Ar | char |  |
| `ar` | ลูกหนี้ *(resource only)* | Ar | char |  |
| `from_date_import_cheque` | จากวันที่รับเช็ค *(resource only)* | From Date Import Cheque | char |  |
| `to_date_import_cheque` | ถึงวันที่รับเช็ค *(resource only)* | To Date Import Cheque | char |  |
| `from_customer_code` | จากรหัสลูกค้า *(resource only)* | From Customer Code | char |  |
| `to_customer_code` | ถึงรหัสลูกค้า *(resource only)* | To Customer Code | char |  |
| `docno` | เอกสารเลขที่ *(resource only)* | Docno | char |  |
| `book_deposit` | สมุดเงินฝาก *(resource only)* | Book Deposit | char |  |
| `employee_by_customer` | พนักงานที่ระบุตามลูกค้า *(resource only)* | Employee by Customer | char |  |
| `employee_by_invoice` | พนักงานที่ระบุตาม Invoice ขาย *(resource only)* | Employee by Invoice | char |  |
| `select_status_card` | เลือกสถานะบัตรเครดิต *(resource only)* | Select Status Card | char |  |
| `from_license_sale` | จากเลขที่ใบขาย *(resource only)* | From License Sale | char |  |
| `to_license_sale` | ถึงเลขที่ใบขาย *(resource only)* | To License Sale | char |  |
| `from_number` | จากจำนวน *(resource only)* | From Number | char |  |
| `to_number` | ถึงจำนวน *(resource only)* | To Number | char |  |
| `from_payment` | จากวิธีรับชำระ *(resource only)* | From Payment | char |  |
| `to_payment` | ถึงวิธีรับชำระ *(resource only)* | To Payment | char |  |
| `category_sale` | ประเภทการขาย *(resource only)* | Category Sale | char |  |
| `print_balance_at_date` | พิมพ์ยอดคงเหลือ ณ วันที่ *(resource only)* | Print Balance at Date | char |  |
| `sell_cash` | ขายสินค้าเงินสด *(resource only)* | Sell Cash | char |  |
| `sell_credit` | ขายสินค้าเงินเชื่อ *(resource only)* | Sell Credit | char |  |
| `cash_sale_service` | ขายสินค้าเงินสด (สินค้าบริการ) *(resource only)* | Cash Sale Service | char |  |
| `cash_sale_credit` | ขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* | Cash Sale Credit | char |  |
| `show_number_of_quote_by_date` | แสดงจำนวนใบเสนอราคาตามวันที่ ที่กำหนด *(resource only)* | Show Number of Quote by Date | char |  |
| `custom_code` | รหัสลูกค้า *(resource only)* | Custom Code | char |  |
| `from_account_book_code` | จากรหัสสมุดบัญชี *(resource only)* | From Account Book Code | char |  |
| `to_account_book_code` | ถึงรหัสสมุดบัญชี *(resource only)* | To Account Book Code | char |  |
| `from_number_check_credit_card` | จากเลขที่เช็ค/บัตรเครดิต *(resource only)* | From Number Check / Credit Card | char |  |
| `to_number_check_credit_card` | ถึงเลขที่เช็ค/บัตรเครดิต *(resource only)* | To Number Check / Credit Card | char |  |
| `from_cash_sub_code` | จากรหัสเงินสดย่อย *(resource only)* | From Cash Sub Code | char |  |
| `to_cash_sub_code` | ถึงรหัสเงินสดย่อย *(resource only)* | To Cash Sub Code | char |  |
| `from_cost_date` | จากวันที่ค่าใช้จ่าย *(resource only)* | From Cost Date | char |  |
| `to_cost_date` | ถึงวันที่ค่าใช้จ่าย *(resource only)* | To Cost Date | char |  |
| `from_staff_code` | จากรหัสพนักงาน *(resource only)* | From Staff Code | char |  |
| `to_staff_code` | ถึงรหัสพนักงาน *(resource only)* | To Staff Code | char |  |
| `conditions` | เงื่อนไข *(resource only)* | Conditions | char |  |
| `all_print` | พิมพ์ทั้งหมด *(resource only)* | All Print | char |  |
| `print_only_to_pay` | พิมพ์เฉพาะที่ยังไม่จ่าย *(resource only)* | Print Only To Pay | char |  |
| `to_pay_particular_type` | พิมพ์เฉพาะที่จ่ายแล้ว *(resource only)* | To Pay Particular Type | char |  |
| `year` | ปี *(resource only)* | Year | char |  |
| `monthly` | ประจำเดือน *(resource only)* | Monthly | char |  |
| `from_address_book` | จากเลขที่สมุด *(resource only)* | From Address Book | char |  |
| `to_address_book` | ถึงเลขที่สมุด *(resource only)* | To Address Book | char |  |
| `at_date` | ณ วันที่ *(resource only)* | At Date | char |  |
| `from_project_account_code` | จากรหัสผังบัญชี *(resource only)* | From Project Account Code | char |  |
| `to_project_account_code` | ถึงรหัสผังบัญชี *(resource only)* | To Project Account Code | char |  |
| `show_products_by_name_daily` | แสดงชื่อสินค้าตามรายวัน *(resource only)* | Show Products by Name Daily | char |  |
| `from_allocation_code` | จากรหัสการจัดสรร *(resource only)* | From Allocation Code | char |  |
| `to_allocation_code` | ถึงรหัสการจัดสรร *(resource only)* | To Allocation Code | char |  |
| `from_customer_group` | จากกลุ่มลูกค้า *(resource only)* | From Customer Group | char |  |
| `to_customer_group` | ถึงกลุ่มลูกค้า *(resource only)* | To Customer Group | char |  |
| `from_dept_group` | From Dept Group *(resource only)* | From Dept Group | char |  |
| `to_dept_group` | To Dept Group *(resource only)* | To Dept Group | char |  |
| `from_check_product_returns_debt` | จากเลขที่ใบรับคืนสินค้า/ลดหนี้ *(resource only)* | From Check Product Returns / Debt Reduction | char |  |
| `to_check_product_returns_debt` | ถึงเลขที่ใบรับคืนสินค้า/ลดหนี้ *(resource only)* | To Check Product Returns / Debt Reduction | char |  |
| `from_month` | จากเดือน *(resource only)* | From Month | char |  |
| `to_month` | ถึงเดือน *(resource only)* | To Month | char |  |
| `order_quantity` | เรียงตามปริมาณ *(resource only)* | Order Quantity | char |  |
| `order_value` | เรียงตามมูลค่า *(resource only)* | Order Value | char |  |
| `sort_by` | เรียงจาก *(resource only)* | Sort by | char |  |
| `from_large_to_small` | เรียงจากมากไปน้อย *(resource only)* | From Large to Small | char |  |
| `from_small_to_large` | เรียงจากน้อยไปมาก *(resource only)* | From Small to Large | char |  |
| `from_sale_date` | จากวันที่ขาย *(resource only)* | From Sale Date | char |  |
| `to_sale_date` | ถึงวันที่ขาย *(resource only)* | To Sale Date | char |  |
| `from_date_of_purchase` | จากวันที่ซื้อ *(resource only)* | From Date of Purchase | char |  |
| `to_date_of_purchase` | ถึงวันที่ซื้อ *(resource only)* | To Date of Purchase | char |  |
| `from_card_purchase` | จากเลขที่ใบซื้อ *(resource only)* | From Card Purchase | char |  |
| `to_card_purchase` | ถึงเลขที่ใบซื้อ *(resource only)* | To Card Purchase | char |  |
| `from_booking_id` | From Booking ID *(resource only)* | From Booking ID | char |  |
| `to_booking_id` | To Booking ID *(resource only)* | To Booking ID | char |  |
| `select_ap_code` | เลือกรหัสเจ้าหนี้ *(resource only)* | Select Ap Code | char |  |
| `ap_balance_amount` | ยอดเจ้าหนี้คงค้าง *(resource only)* | Balance | char |  |
| `none_select` | None select *(resource only)* | None select | char |  |
| `balance_date` | ยอดคงเหลือ ณ. วันที่ *(resource only)* | Balance Date | char |  |
| `from_credit_number` | จากหมายเลขบัตรเครดิต *(resource only)* | From  Credit Card | char |  |
| `to_credit_number` | ถึงหมายเลขบัตรเครดิต *(resource only)* | To  Credit Card | char |  |
| `from_check_number` | จากเลขที่เช็ค *(resource only)* | From Check Number | char |  |
| `to_check_number` | ถึงเลขที่เช็ค *(resource only)* | To Check Number | char |  |
| `item_status` | สถานะสินค้า *(resource only)* | Item Status | char |  |
| `item_status_new` | สินค้าใหม่ *(resource only)* | New Item | char |  |
| `item_status_old` | สินค้าเก่า *(resource only)* | Old Item | char |  |
| `sort_order_by` | เรียงตาม *(resource only)* | Order By | char |  |
| `process_date` | ประมวล ณ วันที่ *(resource only)* | Process Date | char |  |
| `from_job` | จากงาน *(resource only)* | From Job | char |  |
| `to_job` | ถึงงาน *(resource only)* | To Job | char |  |
| `from_petty_cash_code` | จากรหัสเงินสดย่อย *(resource only)* | From Petty Cash Code | char |  |
| `to_petty_cash_code` | ถึงรหัสเงินสดย่อย *(resource only)* | To Petty Cash Code | char |  |
| `display_detail` | แสดงรายละเอียด *(resource only)* | Display Detail | char |  |
| `sum_all_item` | รวมทั้งสิ้น *(resource only)* | Sum All Item | char |  |
| `sum_item_list` | รายการ *(resource only)* | Item | char |  |
| `must_set_condition` | ยังไม่ได้กำหนดเงื่อนไข *(resource only)* | Must set condition | char |  |
| `search_ap` | ค้นหาเจ้าหนี้ *(resource only)* | Search Supplier | char |  |
| `search_ar` | ค้นหาลูกหนี้ *(resource only)* | Search Customer | char |  |
| `show_cancel_document` | แสดงเอกสารที่ถูกยกเลิก *(resource only)* | Show Cancel Document | char |  |
| `new_page_by_ar_code` | ขึ้นหน้าใหม่ทุกครั้งตามลูกค้า *(resource only)* |  | char |  |
| `movement_only` | แสดงเฉพาะที่มีรายการเคลื่อนไหว *(resource only)* |  | char |  |
| `from_ap` | จากรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `to_ap` | ถึงรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `count_day_from` | จากจำนวนวัน *(resource only)* |  | char |  |
| `count_day_to` | ถึงจำนวนวัน *(resource only)* |  | char |  |
| `from_bank_book_code` | จากรหัสสมุดธนาคาร *(resource only)* |  | char |  |
| `to_bank_book_code` | ถึงรหัสสมุดธนาคาร *(resource only)* |  | char |  |
| `status_approve` | ผลการตัดสินใจ *(resource only)* |  | char |  |
| `wait_approve` | รอการอนุมัติ *(resource only)* |  | char |  |
| `cancel_approve` | ไม่อนุมัติ *(resource only)* |  | char |  |
| `overcome_approve` | อนุมัติแล้ว *(resource only)* |  | char |  |
| `from_approve` | จากเลขที่ใบขออนุมัติ *(resource only)* |  | char |  |
| `to_approve` | ถึงเลขที่ใบขออุนมัติ *(resource only)* |  | char |  |
| `vat_display_type` | การแสดงยอด *(resource only)* |  | char |  |
| `vat_display_type_1` | ตามการบันทึก *(resource only)* |  | char |  |
| `vat_display_type_2` | แสดงตัวเลขแบบแยกนอกทั้งหมด *(resource only)* |  | char |  |
| `vat_display_type_3` | แสดงตัวเลขแบบรวมในทั้งหมด *(resource only)* |  | char |  |
| `cashier_check` | แยกตามพนักงานเก็บเงิน *(resource only)* |  | char |  |
| `cashier_select` | เลือกพนักงานเก็บเงิน *(resource only)* |  | char |  |
| `show_barcode` | แสดง Barcode *(resource only)* |  | char |  |
| `select_ap` | เลือกเจ้าหนี้ *(resource only)* |  | char |  |
| `selear_ar` | เลือกลูกหนี้ *(resource only)* |  | char |  |
| `show_pos_only` | แสดงเฉพาะรายการ POS *(resource only)* |  | char |  |
| `from_bill_no` | จากเลขที่บิล *(resource only)* |  | char |  |
| `to_bill_no` | ถึงเลขที่บิล *(resource only)* |  | char |  |
| `bill_no` | เลขที่บิล *(resource only)* |  | char |  |
| `bill_date` | วันที่ออกบิล *(resource only)* |  | char |  |
| `from_receive_date` | จากวันที่รับชำระ *(resource only)* |  | char |  |
| `to_receive_date` | ถึงวันที่รับชำระ *(resource only)* |  | char |  |
| `from_receive_no` | จากใบรับเลขที่ *(resource only)* |  | char |  |
| `to_receive_no` | ถึงใบรับเลขที่ *(resource only)* |  | char |  |
| `ar_type` | ประเภทลูกหนี้ *(resource only)* |  | char |  |
| `from_time` | จากเวลา *(resource only)* |  | char |  |
| `to_time` | ถึงเวลา *(resource only)* |  | char |  |
| `cash_sale` | ขายเงินสด *(resource only)* |  | char |  |
| `credit_sale` | ขายเงินเชื่อ *(resource only)* |  | char |  |
| `show_only` | แสดงรายการ *(resource only)* |  | char |  |
| `show_sale_only` | แสดงเฉพาะรายการหลังร้าน *(resource only)* |  | char |  |
| `month_jan` | ม.ค. *(resource only)* | Jan | char |  |
| `month_feb` | ก.พ. *(resource only)* | Feb | char |  |
| `month_mar` | มี.ค. *(resource only)* | Mar | char |  |
| `month_apr` | เม.ย. *(resource only)* | Apr | char |  |
| `month_may` | พ.ค. *(resource only)* | May | char |  |
| `month_jun` | มิ.ย. *(resource only)* | Jun | char |  |
| `month_jul` | ก.ค. *(resource only)* | Jul | char |  |
| `month_aug` | ส.ค. *(resource only)* | Aug | char |  |
| `month_sep` | ก.ย. *(resource only)* | Sep | char |  |
| `month_oct` | ต.ค. *(resource only)* | Oct | char |  |
| `month_nov` | พ.ย. *(resource only)* | Nov | char |  |
| `month_dec` | ธ.ค. *(resource only)* | Dec | char |  |
| `cheque_change` | เช็คเปลี่ยน *(resource only)* |  | char |  |
| `total_debt_balance` | ยอดหนี้คงค้าง *(resource only)* |  | char |  |
| `overdue` | เกินกำหนดชำระ *(resource only)* |  | char |  |
| `ondue` | ยังไม่ถึงกำหนดชำระ *(resource only)* |  | char |  |
| `debt_value` | รวมมูลค่าหนี้ *(resource only)* |  | char |  |
| `total` | รวม *(resource only)* |  | char |  |
| `ar_code` | รหัสลูกหนี้ *(resource only)* |  | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* |  | char |  |
| `amount` | จำนวน *(resource only)* |  | char |  |
| `balance_first` | ยอดยกมา *(resource only)* |  | char |  |
| `balance_end` | ยอดยกไป *(resource only)* |  | char |  |
| `sum_request` | ยอดเบิก *(resource only)* |  | char |  |
| `sum_return` | ยอดคืน *(resource only)* |  | char |  |
| `sum_pay` | ยอดตัดจ่าย *(resource only)* |  | char |  |
| `sum_receive` | ยอดรับ *(resource only)* |  | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `show_non_counting_have_stock` | แสดงสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ *(resource only)* |  | char |  |
| `show_remark` | แสดงหมายเหตุ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `show_balance_only` | แสดงเฉพาะที่มียอดคงเหลือ *(resource only)* |  | char |  |
| `from_branch_code` | จากสาขา *(resource only)* |  | char |  |
| `to_branch_code` | ถึงสาขา *(resource only)* |  | char |  |

## resource_report_bank

**รายงานเช็คเงินสดธนาคาร** — Report Bank

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `title_credit_receive` | Title\t: รายงานรายการรับบัตรเครดิต *(resource only)* |  | char |  |
| `title_credit_payment` | Title\t: รายงานรายการจ่ายบัตรเครดิต *(resource only)* |  | char |  |
| `title_chq_receive` | Title\t: รายงานทะเบียนเช็ครับ *(resource only)* |  | char |  |
| `title_chq_payment` | Title\t: รายงานทะเบียนเช็คจ่าย *(resource only)* |  | char |  |
| `page_no` | Page No. : *(resource only)* | Page No. : | char |  |
| `printed_by` | Printed By\t: *(resource only)* | Printed By\t: | char |  |
| `prited_date` | Printed Date : *(resource only)* | Printed Date : | char |  |
| `date_credit_receive` | วันที่รับบัตร *(resource only)* |  | char |  |
| `date_credit_payment` | วันที่จ่ายบัตร *(resource only)* |  | char |  |
| `date_chq_receive` | วันที่รับเช็ค *(resource only)* |  | char |  |
| `date_chq_payment` | วันที่จ่ายเช็ค *(resource only)* |  | char |  |
| `doc_ref` | เลขที่เอกสารอ้างอิง *(resource only)* |  | char |  |
| `credit_card_no` | เลขที่บัตรเครดิต *(resource only)* |  | char |  |
| `chq_no` | เลขที่เช็ค *(resource only)* |  | char |  |
| `remark` | หมายเหตุ/รายละเอียด *(resource only)* |  | char |  |
| `amount` | จำนวนเงิน *(resource only)* |  | char |  |
| `included` | รวม *(resource only)* |  | char |  |
| `item` | รายการ *(resource only)* |  | char |  |
| `total` | จำนวนเงินรวม *(resource only)* |  | char |  |

## resource_report_color

**resource_report_color** — resource_report_color

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_color_base_code` | รหัสสี Base *(resource only)* |  | char |  |
| `ic_color_base` | สี Base *(resource only)* |  | char |  |
| `sale_qty` | จำนวน(สี Base) *(resource only)* |  | char |  |
| `sale_amount` | ยอดขาย(สี Base) *(resource only)* |  | char |  |
| `sale_cost` | ต้นทุน(สี Base) *(resource only)* |  | char |  |
| `sale_profit` | กำไร(สี Base) *(resource only)* |  | char |  |
| `sale_qty_1` | จำนวน(สีผสม) *(resource only)* |  | char |  |
| `sale_amount_1` | ยอดขาย(สีผสม) *(resource only)* |  | char |  |
| `sale_cost_1` | ต้นทุน(สีผสม) *(resource only)* |  | char |  |
| `ic_code` | รหัสสินค้า *(resource only)* |  | char |  |
| `ic_name` | รายละเอียดสินค้า *(resource only)* |  | char |  |
| `ic_unit` | หน่วยนับ *(resource only)* |  | char |  |
| `doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `ar_code` | รหัสลูกค้า *(resource only)* |  | char |  |
| `ar_detail` | รายละเอียดลูกค้า *(resource only)* |  | char |  |
| `amount_net` | ยอดขายรวม *(resource only)* |  | char |  |
| `cost_net` | ต้นทุนรวม *(resource only)* |  | char |  |
| `profit_lost_amount` | กำไรสุทธิ *(resource only)* |  | char |  |
| `profit_lost_persent` | กำไรสุทธิ(%) *(resource only)* |  | char |  |
| `ic_color_mixed` | สีผสม *(resource only)* |  | char |  |
| `color_qty` | จำนวน *(resource only)* |  | char |  |
| `sale_profit_1` | กำไร(สีผสม) *(resource only)* |  | char |  |

## resource_report_column

**resource_report_column** — resource_report_column

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | Supplier Code | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* | Supplier Name | char |  |
| `tax_id` | เลขประจำตัวผู้เสียภาษี *(resource only)* | Tax ID | char |  |
| `address` | ที่อยู่ *(resource only)* | Address | char |  |
| `telephone` | โทรศัพท์ *(resource only)* | Telephone | char |  |
| `fax` | โทรสาร *(resource only)* | Fax | char |  |
| `email` | อีเมล์ *(resource only)* | Email | char |  |
| `doc_date` | เอกสารวันที่ *(resource only)* | Document Date | char |  |
| `doc_no` | เอกสารเลขที่ *(resource only)* | Document No | char |  |
| `remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `total_amount` | มุลค่าสุทธิ *(resource only)* | Total Amount | char |  |
| `balance_amount` | ยอดเงินคงเหลือ *(resource only)* | Balance Amount | char |  |
| `doc_ref` | เอกสารอ้างอิง *(resource only)* | Document Reference | char |  |
| `total_before_vat` | ยอดก่อนภาษี *(resource only)* | Total Before Vat | char |  |
| `total_discount` | ส่วนลด *(resource only)* | Total Discount | char |  |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม *(resource only)* | TotalVat Value | char |  |
| `total_net_value` | มูลค่าทั้งสิ้น *(resource only)* | Total Net Value | char |  |
| `doc_ref_no` | เอกสารอ้างอิงเลขที่ *(resource only)* | Document Reference No | char |  |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ *(resource only)* | Document Reference Date | char |  |
| `due_date` | วันที่ครบกำหนด *(resource only)* | Due Date | char |  |
| `sum_value` | มูลค่าสินค้า *(resource only)* | Sum Value | char |  |
| `sum_debt_value` | รวมมูลค่า *(resource only)* | Sum Debt Value | char |  |
| `total_pay_money` | ยอดชำระ *(resource only)* | Total Pay Money | char |  |
| `sum_pay_money` | ยอดตัดจ่าย *(resource only)* | Sum Pay Money | char |  |
| `sum_debt_balance` | ยอดหนี้คงเหลือ *(resource only)* | Sum Debt Balance | char |  |
| `ar_code` | รหัสลูกหนี้ *(resource only)* | Customer Code | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* | Customer Name | char |  |
| `sum_tax_value` | มูลค่าภาษี *(resource only)* | Sum Tax Value | char |  |
| `process_date` | ประมวลผล ณ วันที่ *(resource only)* | Process Date | char |  |
| `from_ap_code` | จากเจ้าหนี้ *(resource only)* | From Customer | char |  |
| `from_ar_code` | จากลูกหนี้ *(resource only)* | From Supplier | char |  |
| `to_ap_code` | ถึงเจ้าหนี้ *(resource only)* | To Customer | char |  |
| `to_ar_code` | ถึงลูกหนี้ *(resource only)* | To Supplier | char |  |
| `order_by_due_date` | เริ่มจากวันถึงกำหนด *(resource only)* | Order By Due Date | char |  |
| `order_by_doc_date` | เริ่มจากวันที่เอกสาร *(resource only)* | Order By Doc Date | char |  |
| `show_debt_balance` | แสดงเฉพาะที่มียอดหนี้ *(resource only)* | Show Debt Balance | char |  |
| `show_chq` | แสดงรายละเอียดเช็ค *(resource only)* | Show cheque | char |  |
| `from_period_1` | ช่วงที่ 1 *(resource only)* | From period 1 | char |  |
| `from_period_2` | ช่วงที่ 2 *(resource only)* | From period 2 | char |  |
| `from_period_3` | ช่วงที่ 3 *(resource only)* | From period 3 | char |  |
| `from_period_4` | ช่วงที่ 4 *(resource only)* | From period 4 | char |  |
| `from_period_5` | มากกว่า *(resource only)* | More Than | char |  |
| `from_date` | จากวันที *(resource only)* | From Date | char |  |
| `to_date` | ถึงวันที่ *(resource only)* | To Date | char |  |
| `to_period_1` | ถึงช่วงที่ 1 *(resource only)* | To period 1 | char |  |
| `to_period_2` | ถึงช่วงที่ 2 *(resource only)* | To period 2 | char |  |
| `to_period_3` | ถึงช่วงที่ 3 *(resource only)* | To period 3 | char |  |
| `to_period_4` | ถึงช่วงที่ 4 *(resource only)* | To period 4 | char |  |
| `to_period_5` | มากกว่า *(resource only)* | More Than | char |  |
| `no_period` | ไม่อยู่ในช่วง *(resource only)* | No Period | char |  |
| `period_no` | ช่วง *(resource only)* | Period No | char |  |
| `day` | วัน *(resource only)* | Day | char |  |
| `order_by` | เรียงจาก *(resource only)* | Order By | char |  |
| `cn_balance` | ยอดลดหนี้ *(resource only)* | CN Blance | char |  |
| `amount` | ยอดเงินล่วงหน้า *(resource only)* | Amount | char |  |
| `sum_cash` | ยอดเงินสด *(resource only)* | Cash | char |  |
| `sum_chq` | ยอดเช็ค *(resource only)* | Cheque | char |  |
| `sum_transfer` | ยอดเงินโอน *(resource only)* | Transfer | char |  |
| `sum_credit` | ยอดบัตรเครดิต *(resource only)* | Credit | char |  |
| `sum_total` | ยอดเงินรวม *(resource only)* | Total | char |  |
| `detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `sum_pay_vat` | ภาษี ณ ที่จ่าย *(resource only)* | Pay Vat | char |  |
| `difference` | ผลต่าง *(resource only)* | Difference | char |  |
| `sum_debt_remain` | ยอดคงค้าง *(resource only)* | Sum Debt Remain | char |  |

## resource_report_form

**Resource Report Form** — Resource Report Form

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `report_title_receipt` | ใบเสร็จรับเงิน/ใบกำกับภาษี *(resource only)* | RECEIPT/TAX INVOICE | char |  |
| `report_doc_no` | เลขที่ *(resource only)* | Document No | char |  |
| `report_doc_date` | วันที่ *(resource only)* | Document Date | char |  |
| `report_tax_person` | เลขประจำตัวผู้เสียภาษี *(resource only)* | Tax ID / BR No. | char |  |
| `report_customer` | ลูกค้า *(resource only)* | Customer | char |  |
| `report_sale_man` | พนักงานขาย *(resource only)* | Sale Man | char |  |
| `report_credit` | เครดิต *(resource only)* | Credit | char |  |
| `report_credit_day` | วัน *(resource only)* | Days | char |  |
| `report_due_date` | วันครบกำหนด *(resource only)* | Due Date | char |  |
| `report_remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `report_item_code` | รหัสสินค้า *(resource only)* | Item Code | char |  |
| `report_description` | รายการ *(resource only)* | Description | char |  |
| `report_amount` | จำนวน *(resource only)* | Amount | char |  |
| `report_price_unit` | ราคาขายต่อหน่วย *(resource only)* | Selling Price/Unit | char |  |
| `report_discount` | ส่วนลด *(resource only)* | Discount | char |  |
| `report_total_amount` | จำนวนเงิน *(resource only)* | Total Amount | char |  |
| `report_sum_price` | รวมราคาทั้งสิ้น *(resource only)* | Sum Price | char |  |
| `report_sum_discount` | หักส่วนลด *(resource only)* | Sum Discount | char |  |
| `report_sum_price_discount` | ยอดหลังหักส่วนลด *(resource only)* | Sum Discount Amount | char |  |
| `report_sum_deposit` | หักเงินมัดจำ *(resource only)* | Sum Deposit | char |  |
| `report_sum_deposit_discount` | ยอดหลังหักเงินมัดจำ *(resource only)* | Sum Deposit Amount | char |  |
| `report_vat_amount` | ภาษีมูลค่าเพิ่ม *(resource only)* | Sum Vat | char |  |
| `report_sale_detail` | ชำระเงินโดย *(resource only)* | Sale Detail | char |  |
| `report_money_cash` | เงินสด: *(resource only)* | Cash | char |  |
| `report_money_cheque` | เช็ค: *(resource only)* | Cheque | char |  |
| `report_money_amount` | จำนวนเงิน *(resource only)* | Amount | char |  |
| `report_money_cheque_no` | เลขที่เช็ค *(resource only)* | Cheque No. | char |  |
| `report_money_by` | ผู้รับเงิน *(resource only)* | By | char |  |
| `report_money_date` | วันที่ *(resource only)* | Date | char |  |
| `report_money_bank` | ธนาคาร *(resource only)* | Bank Name | char |  |
| `report_sum_total_amount` | รวมเงินทั้งสิ้น *(resource only)* | Sum Total Amount | char |  |
| `report_money_remark` | ใบเสร็จรับเงินฉบับนี้จะสมบูรณ์ต่อเมื่อบริษัทฯ ได้เรียกเก็บเงินตามเช็คเรียบร้อยแล้วเท่านั้น *(resource only)* | ใบเสร็จรับเงินฉบับนี้จะสมบูรณ์ต่อเมื่อบริษัทฯ ได้เรียกเก็บเงินตามเช็คเรียบร้อยแล้วเท่านั้น | char |  |
| `report_address` | ที่อยู่ *(resource only)* | Address | char |  |
| `report_item_description` | รายการสินค้า *(resource only)* | Item Description | char |  |
| `report_item_unit` | หน่วย *(resource only)* | Unit | char |  |
| `report_qty` | จำนวน *(resource only)* | Qty | char |  |
| `report_price` | ราคาขาย *(resource only)* | Price | char |  |
| `report_discount_sale` | ส่วนลดการค้า *(resource only)* | Discount | char |  |
| `report_price_item_other` | ราคาสินค้า/สินค้าบริการ *(resource only)* | Sum Item Price | char |  |
| `report_total_sum_amount` | จำนวนเงินรวมทั้งสิ้น *(resource only)* | Sum Total Amount | char |  |
| `report_cus_approval` | ผู้อนุมัติ *(resource only)* | Customer | char |  |
| `report_number_remark` | ยอดเงินเป็นตัวหนังสือ *(resource only)* | ยอดเงินเป็นตัวหนังสือ | char |  |

## resource_report_ic_column

**ic_report_column**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code` | รหัสสินค้า *(resource only)* | Item Code | char |  |
| `item_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `unit_standard` | หน่วยนับ(มาตรฐาน) *(resource only)* | Unit Standard | char |  |
| `item_type` | ประเภทสินค้า *(resource only)* | Item Type | char |  |
| `cost_type` | ประเภทต้นทุน *(resource only)* | Cost Type | char |  |
| `tax_type` | ประเภทภาษี *(resource only)* | Tax Type | char |  |
| `item_pattern` | รูปบบสินค้า *(resource only)* | Item Pattern | char |  |
| `unit` | หน่วยนับ *(resource only)* | Unit | char |  |
| `warehouse` | คลัง *(resource only)* | Warehouse | char |  |
| `shelf` | พื้นที่เก็บ *(resource only)* | Shelf | char |  |
| `cost` | ต้นทุน *(resource only)* | Cost | char |  |
| `color_mixing_code` | รหัสสูตรสีผสม *(resource only)* | Color Mixing Code | char |  |
| `color_mixing_name` | ชื่อสูตรสีผสม *(resource only)* | Color Mixing Name | char |  |
| `qty` | จำนวน *(resource only)* | Qty | char |  |
| `price` | ราคา *(resource only)* | Price | char |  |
| `total_price` | มูลค่า *(resource only)* | total_price | char |  |
| `set_item_code` | รหัสสูตรสินค้าชุด *(resource only)* | Set Item Code | char |  |
| `set_item_name` | ชื่อสินค้าชุด *(resource only)* | Set Item Name | char |  |
| `item_name_th` | ชื่อสินค้า(ไทย) *(resource only)* | Item Name TH | char |  |
| `item_name_eng` | ชื่อสินค้า(อังกฤษ) *(resource only)* | Item Name ENG | char |  |
| `split_tax_price` | ราคาแยกภาษี *(resource only)* | Split Tax Price | char |  |
| `include_tax_price` | ราคารวมภาษี *(resource only)* | Include Tax Price | char |  |
| `date_begin` | วันที่เริ่ม *(resource only)* | Date Begin | char |  |
| `date_end` | วันที่สิ้นสุด *(resource only)* | Date End | char |  |
| `condition` | เงื่อนไข *(resource only)* | Condition | char |  |
| `doc_date` | วันที่เอกสาร *(resource only)* | Doc Date | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* | Doc No | char |  |
| `import_first_date` | รับเข้าครั้งแรก(วัน) *(resource only)* | Import First Date | char |  |
| `import_last_date` | รับเข้าล่าสุด(วัน) *(resource only)* | Import Last Date | char |  |
| `pay_last_date` | จ่ายครั้งล่าสุด(วัน) *(resource only)* | Pay Last Date | char |  |
| `different_day` | ต่างกัน(วัน) *(resource only)* | Different Day | char |  |
| `item_group` | กลุ่มสินค้า *(resource only)* | item_group | char |  |
| `customer_code` | รหัสลูกค้า *(resource only)* | Customer Code | char |  |
| `customer_name` | ชื่อลูกค้า *(resource only)* | Customer Name | char |  |
| `from_warehouse` | จากคลัง *(resource only)* | From Warehouse | char |  |
| `to_warehouse` | เข้าคลัง *(resource only)* | To Warehouse | char |  |
| `from_shelf` | จากที่เก็บ *(resource only)* | From Shelf | char |  |
| `to_shelf` | เข้าที่เก็บ *(resource only)* | To Shelf | char |  |
| `ref_doc_no` | เลขที่เอกสารอ้างอิง *(resource only)* | Ref Doc No | char |  |
| `ref_doc_date` | วันที่เอกสารอ้างอิง *(resource only)* | Ref Doc Date | char |  |
| `remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `from_day` | จากจำนวน(วัน) *(resource only)* | From Day | char |  |
| `to_day` | ถึงจำนวน(วัน) *(resource only)* | To Day | char |  |
| `sale` | ขาย *(resource only)* | Sale | char |  |
| `refunded` | รับคืน *(resource only)* | Refunded | char |  |
| `net` | สุทธิ *(resource only)* | Net | char |  |
| `department` | แผนก *(resource only)* | Department | char |  |
| `balance_qty` | ยอดคงเหลือ *(resource only)* |  | char |  |
| `warehouse_name` | ชื่อคลัง *(resource only)* |  | char |  |
| `unit_standard_name` | ชื่อหน่วยมาตรฐาน *(resource only)* |  | char |  |
| `last_buy` | วันที่ซื้อล่าสุด *(resource only)* |  | char |  |
| `last_sale` | วันที่ขายล่าสุด *(resource only)* |  | char |  |
| `day_count` | จำนวนวัน *(resource only)* |  | char |  |
| `day_count_word` | จำนวนวัน *(resource only)* |  | char |  |
| `shelf_name` | ชื่อพื้นที่เก็บ *(resource only)* |  | char |  |

## resource_report_ic_report_name

**ic_report_name**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_detail` | รายงานรายละเอียดสินค้า *(resource only)* | IC Detail | char |  |
| `ic_barcode` | รายงานบาร์โค้ดสินค้า *(resource only)* | IC Barcode | char |  |
| `ic_color_mixing` | รายงานสูตรผสมสี *(resource only)* | IC Color Mixing | char |  |
| `ic_item_set` | รายงานสินค้าชุด *(resource only)* | IC Item Set | char |  |
| `ic_sale_price` | รายงานราคาขายสินค้า *(resource only)* | IC Sale Price | char |  |
| `ic_purcharse_price` | รายงานราคาซื้อสินค้า *(resource only)* | IC Purcharse Price | char |  |
| `ic_giveaway` | รายงานของแถม *(resource only)* | IC Giveaway | char |  |
| `ic_balance_bring` | รายงานสินค้าและวัตถุดิบ  คงเหลือยกมา *(resource only)* | IC Balance Bring | char |  |
| `ic_import_item_ready` | รายงานรับสินค้าสำเร็จรูป *(resource only)* | IC Import Item Ready | char |  |
| `ic_transfer_item_and_material` | รายงานโอนสินค้าและวัตถุดิบ *(resource only)* | IC Transfer Item and Material | char |  |
| `ic_withdraw_item` | รายงานเบิกสินค้า *(resource only)* | IC Withdraw Item | char |  |
| `ic_item_return` | รายงานรับคืนเบิกสินค้า *(resource only)* | IC Item Return | char |  |
| `ic_implement_item_over` | รายงานปรับปรุงสต๊อกสินค้าและวัตถุดิบ (เกิน) *(resource only)* | IC Implement Item Over | char |  |
| `ic_implement_item_minus` | รายงานปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) *(resource only)* | IC Implement Item Minus | char |  |
| `ic_balance` | รายงานยอดคงเหลือสินค้า *(resource only)* | IC Balance | char |  |
| `ic_none_transfer` | รายงานสินค้าไม่มีการคเลื่อนไหว *(resource only)* | IC None Transfer | char |  |
| `ic_info_stk_movement_sum` | รายงานสรุปเคลื่อนไหวปริมาณสินค้า *(resource only)* | IC Info Stk Movement Sum | char |  |
| `ic_transfer` | รายงานสรุปเคลื่อนไหวสินค้า *(resource only)* | IC Transfer | char |  |
| `ic_status` | รายงานสถานะสินค้า *(resource only)* | IC Status | char |  |
| `ic_info_stk_movement` | รายงานบัญชีคุมพิเสษสินค้า *(resource only)* | IC Info Stk Movement | char |  |
| `ic_info_stk_profit` | รายงานกำไรขั้นต้นตามสินค้า *(resource only)* | IC Snfo Stk Profit | char |  |
| `cancel_implement_item_over` | รายงานยกเลิกปรับปรุงสต๊อกสินค้าและวัตถุดิบ (เกิน) *(resource only)* | Cancel Implement Item Over | char |  |
| `cancel_implement_item_minus` | รายงานยกเลิกปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) *(resource only)* | Cancel Implement Item Minus | char |  |
| `ic_transfer_by_qty` | รายงานสรุปเคลื่อนไหวสินค้าตามปริมาณ *(resource only)* | IC Transfer by Qty | char |  |
| `cancel_ic_import_item_ready` | รายงานยกเลิกรับสินค้าสำเร็จรูป *(resource only)* | Cancel IC Import Item Ready | char |  |
| `cancel_ic_transfer` | รายงานยกเลิกโอนสินค้าและวัตถุดิบ *(resource only)* | Cancel IC Transfer | char |  |
| `cancel_ic_withdraw_item` | รายงานยกเลิกเบิกสินค้า *(resource only)* | Cancel IC Withdraw Item | char |  |
| `cancel_ic_item_return` | รายงานยกเลิกรับคืนเบิกสินค้า *(resource only)* | Cancel IC Item Return | char |  |
| `ic_info_stk_reorder` | รายงานสินค้าที่ถึงจุดสั่ง *(resource only)* | IC Info Stk Reorder | char |  |

## resource_report_name

**resource_report_name** — resource_report_name

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_detail` | รายงานรายละเอียดเจ้าหนี้ *(resource only)* | AP Detail | char |  |
| `ap_early_debt_setup` | รายงานเอกสารตั้งหนี้ยกมา *(resource only)* | AP Debt | char |  |
| `ap_early_debt_setup_cancel` | รายงานยกเลิกเอกสารตั้งหนี้ยกมา *(resource only)* | AP Cancel Debt | char |  |
| `ap_early_debt_increase` | รายงานเอกสารเพิ่มหนี้ยกมา *(resource only)* | AP Debt Increase | char |  |
| `ap_early_debt_increase_cancel` | รายงานยกเลิกเอกสารเพิ่มหนี้ยกมา *(resource only)* | AP Cancel Debt Increase | char |  |
| `ap_early_debt_decrease` | รายงานเอกสารลดหนี้ยกมา *(resource only)* | AP Debt Decrease | char |  |
| `ap_early_debt_decrease_cancel` | รายงานยกเลิกเอกสารลดหนี้ยกมา *(resource only)* | AP Cancel Debt Decrease | char |  |
| `ap_billing` | รายงานใบรับวางบิล *(resource only)* | AP Billing | char |  |
| `ap_billing_cancel` | รายงานยกเลิกใบรับวางบิล *(resource only)* | AP Cancel Billing | char |  |
| `ap_payment` | รายงานการจ่ายชำระหนี้ *(resource only)* | AP Payment | char |  |
| `ap_payment_cancel` | รายงานยกเลิกการจ่ายชำระหนี้ *(resource only)* | AP Cancel Payment | char |  |
| `ap_movement` | รายงานเคลื่อนไหวเจ้าหนี้ *(resource only)* | AP Movement | char |  |
| `ap_status` | รายงานสถานะเจ้าหนี้ *(resource only)* | AP Status | char |  |
| `ap_aging` | รายงานอายุเจ้าหนี้ *(resource only)* | AP Period | char |  |
| `ap_not_movement` | รายงานเจ้าหนี้ที่ไม่มีการเคลื่อนไหว *(resource only)* | AP Not Movement | char |  |
| `ap_payment_daily` | รายงานการจ่ายเงินประจำวัน *(resource only)* | AP Payment Daily | char |  |
| `ar_detail` | รายงานรายละเอียดลูกหนี้ *(resource only)* | AR Detail | char |  |
| `ar_early_debt_setup` | รายงานเอกสารตั้งหนี้ยกมา *(resource only)* | AR Debt | char |  |
| `ar_early_debt_setup_cancel` | รายงานยกเลิกเอกสารตั้งหนี้ยกมา *(resource only)* | AR Cancel Debt | char |  |
| `ar_early_debt_increase` | รายงานเอกสารเพิ่มหนี้ยกมา *(resource only)* | AR Debt Increase | char |  |
| `ar_early_debt_increase_cancel` | รายงานยกเลิกเอกสารเพิ่มหนี้ยกมา *(resource only)* | AR Cancel Debt Increase | char |  |
| `ar_early_debt_decrease` | รายงานเอกสารลดหนี้ยกมา *(resource only)* | AR Debt Decrease | char |  |
| `ar_early_debt_decrease_cancel` | รายงานยกเลิกเอกสารลดหนี้ยกมา *(resource only)* | AR Cancel Debt Decrease | char |  |
| `ar_billing` | รายงานใบวางบิล *(resource only)* | AR Billing | char |  |
| `ar_billing_cancel` | รายงานยกเลิกใบวางบิล *(resource only)* | AR Cancel Billing | char |  |
| `ar_receipt` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน *(resource only)* | AR Receipt | char |  |
| `ar_receipt_cancel` | รายงานยกเลิกชำระหนี้/ออกใบเสร็จรับเงิน *(resource only)* | AR Cancel Receipt | char |  |
| `ar_status` | รายงานสถานะลูกหนี้ *(resource only)* | AR Status | char |  |
| `ar_aging` | รายงานอายุลูกหนี้ *(resource only)* | AR Aging | char |  |
| `ar_movement` | รายงานเคลื่อนไหวลูกหนี้ *(resource only)* | AR Movement | char |  |
| `ar_receipt_daily` | รายงานการรับเงินประจำวัน *(resource only)* | AR Receipt Daily | char |  |

## resource_report_vat

**รายงานภาษีมูลค่าเพิ่ม** — Vat Report

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `report_name` | ชื่อรายงาน *(resource only)* |  | char |  |
| `date_begin` | จากวันที่ *(resource only)* |  | char |  |
| `date_end` | ถึงวันที่ *(resource only)* |  | char |  |
| `date_type` | เงื่อนไขวัน *(resource only)* |  | char |  |
| `vat_type` | ประเภทภาษี *(resource only)* |  | char |  |
| `sort_by` | เรียงตาม *(resource only)* |  | char |  |
| `vat_month` | เดือนภาษี *(resource only)* |  | char |  |
| `vat_year` | ปีภาษี *(resource only)* |  | char |  |
| `address` | ที่อยู่ *(resource only)* |  | char |  |
| `by_vat_date` | วันที่ใบกำกับภาษี *(resource only)* |  | char |  |
| `by_doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `by_due_date` | วันที่ยื่น *(resource only)* |  | char |  |
| `order_by_doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `order_by_vat_date` | วันที่ใบกำกับภาษี *(resource only)* |  | char |  |
| `order_by_vat_no` | เลขที่ใบกำกับภาษี *(resource only)* |  | char |  |
| `order_by_doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `month_january` | มกราคม *(resource only)* |  | char |  |
| `month_february` | กุมภาพันธ์ *(resource only)* |  | char |  |
| `month_march` | มีนาคม *(resource only)* |  | char |  |
| `month_april` | เมษายน *(resource only)* |  | char |  |
| `month_may` | พฤษภาคม *(resource only)* |  | char |  |
| `month_june` | มิถุนายน *(resource only)* |  | char |  |
| `month_july` | กรกฎาคม *(resource only)* |  | char |  |
| `month_august` | สิงหาคม *(resource only)* |  | char |  |
| `month_september` | กันยายน *(resource only)* |  | char |  |
| `month_october` | ตุลาคม *(resource only)* |  | char |  |
| `month_november` | พฤศจิกายน *(resource only)* |  | char |  |
| `month_december` | ธันวาคม *(resource only)* |  | char |  |
| `cust_address` | ที่อยู่ *(resource only)* |  | char |  |
| `cust_taxno` | เลขประจำตัวผู้เสียภาษี *(resource only)* |  | char |  |
| `cust_status` | ชนิดเจ้าหนี้ *(resource only)* |  | char |  |
| `compamy_name` | ชื่อบริษัท *(resource only)* |  | char |  |
| `pang_no` | Page No. *(resource only)* |  | char |  |
| `business_name` | ชื่อผู้ประกอบการ *(resource only)* |  | char |  |
| `workplace` | ชื่อสถานที่ประกอบการ *(resource only)* |  | char |  |
| `tax_number` | เลขที่ผู้เสียภาษี *(resource only)* |  | char |  |
| `title` | Title *(resource only)* |  | char |  |
| `printed_by` | Printed By *(resource only)* |  | char |  |
| `printed_date` | Printed Date *(resource only)* |  | char |  |
| `number` | ลำดับที่ *(resource only)* |  | char |  |
| `ar_name` | ชื่อผู้มีเงินได้ *(resource only)* |  | char |  |
| `d_m_y` | วันเดือนปี *(resource only)* |  | char |  |
| `amount` | จำนวนเงิน *(resource only)* |  | char |  |
| `tax` | ภาษี *(resource only)* |  | char |  |
| `conditions` | เงื่อนไข *(resource only)* |  | char |  |
| `pay` | ที่จ่าย *(resource only)* |  | char |  |
| `status_pay` | ประเภทเงินได้ที่จ่าย *(resource only)* |  | char |  |
| `tax_rate` | อัตราภาษี *(resource only)* |  | char |  |
| `now_pay` | ที่จ่ายในครั้งนี้ *(resource only)* |  | char |  |
| `now_sent` | ที่นำส่งในครั้งนี้ *(resource only)* |  | char |  |
| `ap_name` | ชื่อผู้หักเงินได้ *(resource only)* |  | char |  |
| `ap_address` | ที่อยู่ผู้หักเงินได้ *(resource only)* |  | char |  |
| `ar_address` | ที่อยู่ผู้มีเงินได้ *(resource only)* |  | char |  |
| `day_get` | วันที่ได้รับ *(resource only)* |  | char |  |
| `status_get` | ประเภทเงินได้ที่ได้รับ *(resource only)* |  | char |  |
| `included` | รวม *(resource only)* |  | char |  |
| `item` | รายการ *(resource only)* |  | char |  |
| `total` | รวมทั้งหมด *(resource only)* |  | char |  |
| `headquarters_branch` | [ ]สำนักงานใหญ่ [ ]สาขา *(resource only)* |  | char |  |
| `purchase_name` | ชื่อผู้ซื้อสินค้า/ผู้รับบริการ *(resource only)* |  | char |  |
| `value_products` | มูลค่าสินค้า *(resource only)* |  | char |  |
| `remark` | หมายเหตุ *(resource only)* |  | char |  |
| `vol_no` | เล่มที่/เลขที่ *(resource only)* |  | char |  |
| `exception_tax` | ยอดยกเว้นภาษี *(resource only)* |  | char |  |
| `tax_zero` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `services` | บริการ *(resource only)* |  | char |  |
| `vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `sales_tax` | ภาษีขาย *(resource only)* |  | char |  |
| `purchase_tax` | ภาษีซื้อ *(resource only)* |  | char |  |
| `balance` | ยอดคงเหลือ *(resource only)* |  | char |  |
| `show_remark` | แสดงหมายเหตุ *(resource only)* |  | char |  |
| `report_vat_sale_1` | รายงานภาษีขาย *(resource only)* |  | char |  |
| `report_vat_sale_2` | รายงานภาษีขาย (แบบมียอดรวม) *(resource only)* |  | char |  |
| `report_vat_sale_3` | รายงานภาษีขายยื่นเพิ่มเติม *(resource only)* |  | char |  |
| `report_vat_type` | ประเภทรายงาน *(resource only)* |  | char |  |
| `format_number_0` | รูปแบบตัวเลขกรณีติดลบ *(resource only)* |  | char |  |
| `format_number_1` | เครื่องหมายลบ *(resource only)* |  | char |  |
| `format_number_2` | วงเล็บกรณีติดลบ *(resource only)* |  | char |  |
| `vat_group` | รหัสกลุ่มภาษี *(resource only)* |  | char |  |
| `report_vat_buy_1` | รายงานภาษีซื้อ *(resource only)* |  | char |  |
| `report_vat_buy_2` | รายงานภาษีซื้อ (แบบมียอดรวม) *(resource only)* |  | char |  |
| `report_vat_buy_3` | รายงานภาษีซื้อขอคืนไม่ได้ *(resource only)* |  | char |  |
| `report_vat_buy_4` | รายงานภาษีซื้อยื่นเพิ่มเติม *(resource only)* |  | char |  |
| `report_vat_buy_5` | รายงานภาษีซื้อเรียงตามเลขที่ออกใหม่ *(resource only)* |  | char |  |
| `report_vat_buy_6` | รายงานภาษีซื้อแบบมีมาษีซื้อเฉลี่ย *(resource only)* |  | char |  |
| `show_full_invoice_doc_no` | แสดงเลขที่ใบกำกับภาษีอย่างเต็มออกแทน *(resource only)* |  | char |  |
| `full_invoice_doc_no` | เลขที่ใบกำกับภาษีอย่างเต็ม *(resource only)* |  | char |  |
| `wht_doc_no` | เลขที่หนังสือรับรอง *(resource only)* |  | char |  |
| `show_vat_amount_only` | แสดงเฉพาะรายการที่มียอดภาษี *(resource only)* |  | char |  |
| `show_doc_no` | แสดงเลขที่เอกสาร *(resource only)* |  | char |  |
| `branch_code` | สาขา *(resource only)* |  | char |  |
| `report_vat_all` | ทุกประเภท *(resource only)* |  | char |  |
| `report_vat_only` | เฉพาะรายการภาษี *(resource only)* |  | char |  |
| `report_vat_no` | เฉพาะรายการภาษีไม่คิดภาษี *(resource only)* |  | char |  |
| `from_doc_type` | จากประเภทเอกสาร *(resource only)* |  | char |  |
| `to_doc_type` | ถึงประเภทเอกสาร *(resource only)* |  | char |  |
| `doc_type` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `show_except_vat_amount` | แสดงรายการยกเว้นภาษี *(resource only)* |  | char |  |
| `show_sum_by_date` | แสดงยอดรวมแต่ละวัน *(resource only)* |  | char |  |
| `show_sum_on_footer_page` | แสดงยอดรวมแต่ละหน้า *(resource only)* |  | char |  |
| `cust_code` | ลูกหนี้/เจ้าหนี้ *(resource only)* |  | char |  |
| `tax_doc_no` | เลขที่ใบกำกับ *(resource only)* |  | char |  |
| `due_date` | วันที่ครบกำหนด *(resource only)* |  | char |  |

