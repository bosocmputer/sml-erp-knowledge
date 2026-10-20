---
tags: [sml, dictionary, pos, generated]
module: POS
---
# พจนานุกรม: POS — POS

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#POSCashierSettle]] | รายการส่งเงินของพนักงาน / รายการส่งเงินของพนักงาน | 52 |
| [[#POSConfig]] | กำหนด config ระบบ POS / กำหนด config ระบบ POS | 147 |
| [[#POS_ID]] | รหัสเครื่อง POS / รหัสเครื่อง POS | 55 |
| [[#chef_master]] | ผู้ปรุงอาหาร / Chef Master | 5 |
| [[#chef_master_item]] | รายการอาหารของพ่อครัว / Chef Master Item | 3 |
| [[#coupon_list]] | ทะเบียนคูปอง / Table 270 | 14 |
| [[#ic_promotion_formula]] | Promotion / Table 262 | 29 |
| [[#ic_promotion_formula_action]] | ผลที่ได้ / Table 296 | 6 |
| [[#ic_promotion_formula_condition]] | เงื่อนไข / Table 281 | 24 |
| [[#ic_promotion_formula_group_qty]] | จำนวนตามกลุ่ม / Table 299 | 4 |
| [[#ic_promotion_formula_price_discount]] | ราคา/ส่วนลด / Table 282 | 10 |
| [[#ic_trans_discount_group]] | รายละเอียดการลดตามกลุ่ม / ic_trans_discount_group | 8 |
| [[#kitchen_command]] | คำสั่งพิเศษ / Table 311 | 5 |
| [[#kitchen_master]] | ครัว/บาร์น้ำ / Table 276 | 45 |
| [[#kitchen_master_item]] | รายการอาหารในครัว / Table 278 | 3 |
| [[#kitchen_master_order_id]] | เชื่อมครัวกับเครื่องสั่งอาหาร / Table 277 | 4 |
| [[#kitchen_master_pos_id]] | เชื่อมครัวกับเครื่อง POS / Kitchen Master POS ID | 4 |
| [[#kitchen_print_cancel_copy]] | พิมพ์สำเนารายการยกเลิกอาหาร / Kitchen Print Cancel Copy | 5 |
| [[#kitchen_print_copy]] | พิมพ์สำเนาห้องครัว/บาร์น้ำ / Kitchen Print Copy | 5 |
| [[#order_checker]] | ตรวจสอบรายการอาหาร / order_checker | 8 |
| [[#order_device_id]] | รหัสเครื่องสั่งอาหาร  | 29 |
| [[#pos_log]] | ประวัติการใช้งาน POS / POS Log | 7 |
| [[#pos_period]] | กะการทำงาน / Table 269 | 10 |
| [[#pos_point_condition]] | เงื่อนไขการให้แต้ม / Table 267 | 4 |
| [[#pos_point_period]] | กำหนดอัตราแต้มสะสม / Table 268 | 5 |
| [[#pos_point_special_day]] | กำหนดวันพิเศษ / Table 268 | 13 |
| [[#pos_resource]] | pos_resource / pos_resource | 10 |
| [[#pos_settle_bill_cancel]] | รายการส่งเงินบิลยกเลิก / POS Settle Bill Cancel | 10 |
| [[#pos_settle_bill_discount]] | รายละเอียดการส่งบิลส่วนลด / POS Setttle Bill Discount | 11 |
| [[#pos_settle_group_discount]] | รายละเอียดส่วนลดตามกลุ่ม / pos_settle_group_discount | 9 |
| [[#pos_slip_campaign]] | POS Slip Campaign / POS Slip Campaign | 11 |
| [[#pos_slip_campaign_brand]] | Pos Slip Campaign Brand / Pos Slip Campaign Brand | 4 |
| [[#pos_slip_campaign_category]] | Pos Slip Campaign Category / Pos Slip Campaign Category | 4 |
| [[#pos_slip_campaign_group]] | Pos Slip Campaign Group / Pos Slip Campaign Group | 8 |
| [[#pos_slip_campaign_items]] | POS Slip Campaign Items / POS Slip Campaign Items | 5 |
| [[#pos_sync_device]] | Table 308 / Table 308 | 12 |
| [[#pos_view_column]] | รายละเอียดหน้าจอค้นหา / View column | 11 |
| [[#pos_view_table]] | รายละเอียดการแสดงผลแต่ละหน้าจอ / View by Table | 8 |
| [[#printer_order_check]] | จุดพิมพ์ใบเช็ครายการสั่งอาหาร / Printer Order Check | 9 |
| [[#printer_order_check_table]] | กำหนดโต๊ะพิมพ์ใบเช็ครายการสั่งอาหาร / กำหนดโต๊ะพิมพ์ใบเช็ครายการสั่งอาหาร | 4 |
| [[#table_master]] | โต๊ะอาหาร / Table 271 | 17 |
| [[#table_order]] | รายการที่สั่ง / Table 273 | 34 |
| [[#table_order_cancel]] | รายละเอียดการยกเลิก คืนอาหาร / table_order_cancel | 20 |
| [[#table_order_doc]] | รายการเอียดใบสั่งอาหาร / Table 274 | 16 |
| [[#table_order_log]] | table_order_log / table_order_log | 5 |
| [[#table_trans]] | รายวันโต๊ะ / Table 279 | 21 |
| [[#wallet_payments]] | Wallet Payments / Wallet Payments | 13 |

## POSCashierSettle

**รายการส่งเงินของพนักงาน** — รายการส่งเงินของพนักงาน

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `DocNo` | เลขที่เอกสาร |  | varchar(25) | ✓ |
| `DocDate` | วันที่เอกสาร |  | datetime | ✓ |
| `CashierCode` | รหัสพนักงานขาย |  | varchar(25) | ✓ |
| `MACHINECODE` | รหัสเครื่องPOS |  | varchar(10) | ✓ |
| `POS_ID` | เลขที่เครื่อง |  | varchar(30) | ✓ |
| `CashAmount` | เงินสด |  | float | ✓ |
| `CreditCardAmount` | บัตรเครดิต |  | float | ✓ |
| `CoupongAmount` | คูปอง |  | float | ✓ |
| `ChqAmount` | เช็ค |  | float | ✓ |
| `TransferAmount` | เงินโอน |  | float | ✓ |
| `manager_code` | รหัสผู้จัดการ |  | varchar(25) | ✓ |
| `trans_type` | 1=รับเงินทอน,2=ส่งเงิน |  | smallint | ✓ |
| `manager_password` | รหัสผ่านผู้จัดการ *(resource only)* |  | varchar |  |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `total_amount` | ยอดขายทั้งสิ้น |  | float | ✓ |
| `total_cancel` | ยอดขายยกเลิก |  | float | ✓ |
| `total_balance` | ยอดขายสุทธิ |  | float | ✓ |
| `total_diff` | ยอดปัดเศษ |  | float | ✓ |
| `total_credit_card` | ยอดบัตรเครดิต |  | float | ✓ |
| `total_coupon` | ยอดบัตรส่วนลด |  | float | ✓ |
| `total_cash` | ยอดเงินสด |  | float | ✓ |
| `total_sum` | รวมมูลค่าต้องนำส่ง |  | float | ✓ |
| `sum_amount` | รวมมูลค่านำส่ง |  | float | ✓ |
| `total_in` | ยอดเงินทอน |  | float | ✓ |
| `total_out` | ยอดนำส่งเงินสด |  | float | ✓ |
| `begin_date` | วันที่เปิดกะ |  | datetime | ✓ |
| `begin_time` | เวลาเปิดกะ |  | varchar(25) | ✓ |
| `end_date` | วันที่ปิดกะ |  | datetime | ✓ |
| `end_time` | เวลาปิดกะ |  | varchar(25) | ✓ |
| `begin_user_code` | รหัสพนักงานเปิดกะ |  | varchar(25) | ✓ |
| `end_user_code` | รหัสพนักงานปิดกะ |  | varchar(25) | ✓ |
| `cashier_password` | รหัสผ่านพนักงานขาย *(resource only)* |  | char |  |
| `total_out_credit` | ยอดนำส่งบัตรเครดิต |  | float | ✓ |
| `total_out_coupon` | ยอดนำส่งคูปอง |  | float | ✓ |
| `guid_code` | GUID | GUID | varchar(35) | ✓ |
| `total_point` | ยอดแต้ม | Point Amount | float | ✓ |
| `total_advance` | หักเงินมัดจำ |  | float | ✓ |
| `total_after_advance` | ยอดขายหักเงินมัดจำ |  | float | ✓ |
| `deposit_cash_amount` | ยอดเงินมัดจำ |  | float | ✓ |
| `deposit_credit_amount` | ยอดบัตรเครดิตเงินมัดจำ |  | float | ✓ |
| `deposit_return_cash_amount` | ยอดคืนเงินมัดจำ |  | float | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `sale_credit_amount` | ยอดขายเงินเชื่อ |  | float | ✓ |
| `order_amount` | ยอดค้างเช็คบิล |  | float | ✓ |
| `total_credit_charge` | ยอด Charge บัตรเครดิต |  | float | ✓ |
| `total_service_amount` | ยอดรวม Service Charge |  | float | ✓ |
| `total_vat_amount` | ยอดรวมภาษีมูลค่าเพิ่ม |  | float | ✓ |
| `transfer_amount` | ยอดเงินโอน |  | float | ✓ |
| `wallet_amount` | ยอด Wallet |  | float | ✓ |
| `total_currency_amount` | ยอดเงินสกุลอื่น |  | float | ✓ |
| `total_currency_charge_amount` | ยอด Charge สกุลเงินอื่น ๆ |  | float | ✓ |

## POSConfig

**กำหนด config ระบบ POS** — กำหนด config ระบบ POS

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cust_code_default` | ลูกค้าเริ่มต้น |  | varchar(25) | ✓ |
| `cust_code_default_POS` | ลูกค้าเริ่มต้นแยกตามจุดขาย |  | smallint | ✓ |
| `cust_code_digest` | แยกตามจุดขาย *(resource only)* |  | char |  |
| `cust_code_not_digest` | ไม่แยกตามจุดขาย *(resource only)* |  | char |  |
| `Is_Member` | ใช้ระบบสมาชิก |  | smallint | ✓ |
| `use_member_system` | ใช้ระบบสมาชิก *(resource only)* |  | char |  |
| `not_use_member_system` | ไม่ใช้ระบบสมาชิก *(resource only)* |  | char |  |
| `Member_discount` | ส่วนลดของสมาชิก |  | varchar(10) | ✓ |
| `MaxPosMoney` | จำนวนเงินสูงสุดในเครื่องPOS |  | float | ✓ |
| `RoundChangeDecimal` | ใช้ระบบปัดเศษสตางค์ |  | smallint | ✓ |
| `actual_round_decimal` | ปัดตามจริง *(resource only)* |  | char |  |
| `table_round_decimal` | ปัดตามตาราง *(resource only)* |  | char |  |
| `FormatRound` | รูปแบบการปัดเศษ |  | varchar(100) | ✓ |
| `pos_terminal_id` | รหัสเครื่อง Point Of Sale *(resource only)* |  | char |  |
| `pos_type_slip` | ชนิดของ Slip *(resource only)* |  | char |  |
| `pos_slip_no_print` | ไม่พิมพ์ Slip *(resource only)* |  | char |  |
| `pos_slip_roll` | Slip แบบเป็นม้วน *(resource only)* |  | char |  |
| `pos_slip_fix` | ที่มีรูปแบบแน่นอน *(resource only)* |  | char |  |
| `pos_type_printer` | ชนิดเครื่องพิมพ์ *(resource only)* |  | char |  |
| `pos_printer_dotmatrix` | Dotmatrix Printer *(resource only)* |  | char |  |
| `pos_printer_thermal` | Thermal Printer *(resource only)* |  | char |  |
| `pos_port_printer` | Printer Port *(resource only)* |  | char |  |
| `pos_cash_drawer` | ลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `pos_use_cash_drawer` | ใช้ลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `pos_nouse_cash_drawer` | ไม่ใช้ลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `pos_cash_drawer_port` | Port ลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `tab_posClientConfig` | กำหนดค่า Point Of Sale *(resource only)* |  | char |  |
| `tab_posScreenConfig` | กำหนดจอแสดงผล *(resource only)* |  | char |  |
| `pos_printer_name` | Printer Name *(resource only)* |  | char |  |
| `pos_slip_header_font` | รูปแบบตัวอักษรส่วนหัวใบเสร็จ *(resource only)* |  | char |  |
| `pos_slip_detail_font` | รูปแบบตัวอักษรส่วนรายละเอียดใบเสร็จ *(resource only)* |  | char |  |
| `pos_slip_footer_font` | รูปแบบตัวอักษรส่วนท้ายใบเสร็จ *(resource only)* |  | char |  |
| `tab_posSlipFontConfig` | ใบเสร็จและการพิมพ์ *(resource only)* |  | char |  |
| `tab_pos_sound` | กำหนดเสียงและการเตือน *(resource only)* |  | char |  |
| `use_sound_scan_barcode` | ใช้เสียงอ่าน Barcode *(resource only)* |  | char |  |
| `sound_on_scan_barcode` | เสียงอ่าน Barcode *(resource only)* |  | char |  |
| `use_sound_on_already_item` | ใช้เสียงเมื่อซื้อสินค้าเดิม *(resource only)* |  | char |  |
| `sound_on_already_item` | เสียงเมื่อซื้อสินค้าเดิม *(resource only)* |  | char |  |
| `use_sound_on_open_cash_drawer` | ใช้เสียงเมื่อเปิดลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `sound_on_open_cash_drawer` | เสียงเมื่อเปิดลิ้นชักเก็บเงิน *(resource only)* |  | char |  |
| `use_sound_on_already_barcode` | ใช้เสียงเมื่อป้อน Barcode ซ้ำ *(resource only)* |  | char |  |
| `sound_on_already_barcode` | เสียงเมื่อป้อน Barcode ซ้ำ *(resource only)* |  | char |  |
| `use_sound_on_not_found_barcode` | ใช้เสียงเมื่อไม่พบรหัส Barcode *(resource only)* |  | char |  |
| `sound_on_not_found_barcode` | เสียงเมื่อไม่พบรหัส Barcode *(resource only)* |  | char |  |
| `use_sound_on_selected_member` | ใช้เสียงเมื่อเลือกสมาชิก *(resource only)* |  | char |  |
| `sound_on_selected_member` | เสียงเมื่อเลือกสมาชิก *(resource only)* |  | char |  |
| `use_sound_on_change_seller` | ใช้เสียงเมื่อเปลี่ยนพนักงานขาย *(resource only)* |  | char |  |
| `sound_on_change_seller` | เสียงเมื่อเปลี่ยนพนักงานขาย *(resource only)* |  | char |  |
| `use_sound_on_close_selling` | ใช้เสียงเมื่อปิดการขายและคิดเงิน *(resource only)* |  | char |  |
| `sound_on_close_selling` | เสียงเมื่อปิดการขายและคิดเงิน *(resource only)* |  | char |  |
| `use_sound_amount` | ใช้ระบบพูดจำนวนเงิน *(resource only)* |  | char |  |
| `pos_change_price_config` | อนุญาติให้แก้ไขราคา |  | smallint | ✓ |
| `pos_change_discount_config` | อนุญาติให้แก้ไขส่วนลด |  | smallint | ✓ |
| `pos_config_number` | ลำดับที่ |  | smallint | ✓ |
| `pos_header` | ข้อความหัวใบเสร็จ |  | varchar(1000) | ✓ |
| `pos_footer` | ข้อความท้ายใบเสร็จ |  | varchar(1000) | ✓ |
| `pos_bill_type` | รูปแบบใบเสร็จ |  | varchar(1000) | ✓ |
| `slip_code` | รหัสแบบฟอร์ม *(resource only)* |  | char |  |
| `full_invoice_print_type` | การพิมพ์ใบกำกับภาษีอย่างเต็ม *(resource only)* |  | char |  |
| `full_invoice_print_type_standrad` | แบบมาตรฐาน *(resource only)* |  | char |  |
| `full_invoice_print_type_formdesign` | เลือกจากแบบฟอร์ม *(resource only)* |  | char |  |
| `form_code` | รหัสแบบฟอร์ม *(resource only)* |  | char |  |
| `full_invoice_printer_name` | Printer Name *(resource only)* |  | char |  |
| `show_short_description` | ไม่แสดงคำอธิบายสัญลักษณ์ |  | smallint | ✓ |
| `show_tax_detail` | ไม่แสดงรายละเอียดภาษี |  | smallint | ✓ |
| `pos_slip_print_copy` | พิมพ์สำเนาใบเสร็จ *(resource only)* |  | char |  |
| `pos_slip_print_copy_number` | จำนวนสำเนาที่พิมพ์ *(resource only)* |  | char |  |
| `pos_print_method` | วิธีการพิมพ์ *(resource only)* |  | smallint |  |
| `pos_print_driver_method` | พิมพ์ผ่าน Windows Driver *(resource only)* |  | char |  |
| `pos_print_direct_method` | พิมพ์ตรงไปยังเครื่องพิมพ์ (Direct Print) *(resource only)* |  | char |  |
| `pos_print_tcp_ip_method` | พิมพ์ผ่าน TCP/IP *(resource only)* |  | char |  |
| `pos_slip_width` | ความกว้าง SLIP *(resource only)* |  | char |  |
| `pos_search_basket` | ใช้ระบบตระกร้า *(resource only)* |  | char |  |
| `pos_ask_before_print` | ใช้ระบบถามก่อนพิมพ์ใบเสร็จ *(resource only)* |  | char |  |
| `pos_delay_change_money_screen` | เวลาในการแสดงจอเงินทอน(วินาที) *(resource only)* |  | char |  |
| `pos_manualClose_change_money_screen` | ยกเลิกระบบปิดจอทอนเงินอัตโนมัติ *(resource only)* |  | char |  |
| `pos_no_print_barcode_slip` | ไม่พิมพ์บาร์โค๊ดในใบเสร็จ *(resource only)* |  | char |  |
| `pos_cancel_bill` | อนุญาติให้ยกเลิกใบเสร็จ |  | smallint | ✓ |
| `pos_cancel_bill_other_date` | ห้ามยกเลิกใบเสร็จข้ามวัน |  | smallint | ✓ |
| `warning_not_open_period` | เตือนเมื่อไม่มีการเปิดกะ |  | smallint | ✓ |
| `tab_pos_display` | กำหนดการแสดงผล *(resource only)* |  | char |  |
| `pos_search_minibox` | ใช้การค้นหาสินค้าด้วยจอเล็ก *(resource only)* |  | char |  |
| `pos_search_result_items` | จำนวนรายการค้าหาสินค้าต่อหน้า *(resource only)* |  | char |  |
| `pos_close_discount_bill` | ปิดช่องส่วนลดท้ายบิล |  | smallint | ✓ |
| `drawer_codes` | คำสั่งเปิดลิ้นชัก |  | varchar(100) | ✓ |
| `balance_control` | ห้ามขายสินค้าติดลบ |  | smallint | ✓ |
| `barcode_picture` | แสดงรูปภาพจากบาร์โค้ด | Show picture according Barcode | smallint | ✓ |
| `print_item_set_detail` | สินค้าในราคาสูตรไม่พิมพ์ในใบกำกับภาษีอย่างย่อ |  | smallint | ✓ |
| `pos_cashdrawer_open_password` | ถามรหัสผ่านทุกครั้งที่เปิดลิ้นชัก |  | smallint | ✓ |
| `pos_multilanguage_slip` | ใช้ระบบพิมพ์ใบเสร็จหลายภาษา |  | smallint | ✓ |
| `pos_show_total_balance` | เช็คสิทธิ์แสดงยอดขาย POS |  | smallint | ✓ |
| `printer_manual_feed` | ใช้เครื่องพิมพ์แบบฉีกมือ |  | smallint | ✓ |
| `warning_select_cust` | เลือกลูกค้าทุกครั้งก่อนขาย |  | smallint | ✓ |
| `pos_check_send_money` | ปิดระบบตรวจสอบยอดค้างส่งเงิน |  | smallint | ✓ |
| `pos_send_deposit_money` | ใช้ระบบส่งเงินมัดจำ |  | smallint | ✓ |
| `disable_cancel_order_outshift` | ห้ามยกเลิกบิลหลังปิดกะ |  | smallint | ✓ |
| `tab_customerDisplay` | Customer Display *(resource only)* |  | char |  |
| `use_customer_display` | ใช้จอ Customer Display *(resource only)* |  | char |  |
| `customer_display_port` | Port *(resource only)* |  | char |  |
| `customer_display_baudrate` | Baud Rate *(resource only)* |  | char |  |
| `customer_display_parity` | Parity *(resource only)* |  | char |  |
| `customer_display_databit` | Data Bits *(resource only)* |  | char |  |
| `customer_diaplay_charcont` | จำนวนตัวอักษร/บรรทัด *(resource only)* |  | char |  |
| `android_customer_display` | Android Customer Display *(resource only)* |  | char |  |
| `weight_scale_prefix` | Prefix เครื่องชั่งน้ำหนัก |  | varchar(10) | ✓ |
| `weight_prefix_start` | ตำแหน่ง Prefix เริ่มต้น |  | smallint | ✓ |
| `weight_prefix_stop` | ตำแหน่ง Prefix สิ้นสุด |  | smallint | ✓ |
| `weight_ic_code_start` | ตำแหน่งรหัสสินค้าเริ่มต้น |  | smallint | ✓ |
| `weight_ic_code_stop` | ตำแหน่งรหัสสินค้าสิ้นสุด |  | smallint | ✓ |
| `weight_price_start` | ตำแหน่งราคาเริ่มต้น |  | smallint | ✓ |
| `weight_price_stop` | ตำแหน่งราคาสิ้นสุด |  | smallint | ✓ |
| `pos_bill_credit_type` | รูปแบบใบเสร็จ(ขายเชื่อ) |  | varchar(1000) | ✓ |
| `use_item_set` | อนุญาติให้ขายสินค้าชุด |  | smallint | ✓ |
| `no_print_slip` | ไม่พิมพ์ใบเสร็จ |  | smallint | ✓ |
| `check_status_drawer` | ตรวจสอบการเปิดลิ้นชักเก็บเงิน |  | smallint | ✓ |
| `check_remove_item` | ห้ามลบรายการสินค้า |  | smallint | ✓ |
| `vat_type` | ประเภทภาษี |  | smallint | ✓ |
| `vat_type_include` | ภาษีรวมใน *(resource only)* |  | char |  |
| `vat_type_exclude` | ภาษีแยกนอก *(resource only)* |  | char |  |
| `vat_type_zero` | ภาษีศูนย์ *(resource only)* |  | char |  |
| `service_charge_rate` | Service Charge (%) |  | float | ✓ |
| `lock_edit_order` | ห้ามแก้ไขรายการหลังปิดโต๊ะ |  | smallint | ✓ |
| `point_member_only` | สะสมแต้มเฉพาะสมาชิกเท่านั้น |  | smallint | ✓ |
| `check_member_expire` | ใช้ระบบตรวจสอบวันหมดอายุสมาชิก |  | smallint | ✓ |
| `check_float_money` | เตือนเมื่อไม่มีการบันทึกรับเงินทอน |  | smallint | ✓ |
| `print_sale_daily_item` | สรุปรายการขายสินค้าในใบส่งเงิน |  | smallint | ✓ |
| `show_item_location_on_only` | แสดงเฉพาะสินค้าที่มีในคลังและที่เก็บเท่านั้น |  | smallint | ✓ |
| `change_money_currency` | สกุลเงินสำหรับทอนเงิน |  | varchar(25) | ✓ |
| `disable_sale_no_price` | ห้ามขายสินค้าราคาศูนย์ |  | smallint | ✓ |
| `disable_print_cancel_doc` | ไม่พิมพ์เอกสารยกเลิกใบเสร็จ *(resource only)* |  | char |  |
| `weight_qty_start` | ตำแหน่งจำนวนเริ่มต้น |  | smallint | ✓ |
| `weight_qty_stop` | ตำแหน่งจำนวนสิ้นสุด |  | smallint | ✓ |
| `max_change_money` | ทอนเงินสูงสุด |  | float | ✓ |
| `weight_scale_price_digit_power` | ตัวคูณหลักมูลค่าจากเครื่องชั่ง |  | smallint | ✓ |
| `select_credit_type_only` | ใช้การเลือกประเภทบัตรเครดิตเท่านั้น |  | smallint | ✓ |
| `connect_edc` | เชื่อมต่อกับเครื่องรูดบัตร *(resource only)* |  | char |  |
| `connect_edc_port` | Port เครื่องรูดบัตร *(resource only)* |  | char |  |
| `cashloop_id` | รหัสเครื่องจัดการเงินสด |  | varchar(25) | ✓ |
| `cashloop_use` | ใช้เครื่องจัดการเงินสด Creatus |  | smallint | ✓ |
| `tiger_use` | ใช้เครื่องจัดการเงินสด Tiger |  | smallint | ✓ |
| `tiger_app_id` | tiger app id |  | varchar(255) | ✓ |
| `tiger_x_api_key` | tiger x-api-key |  | varchar(255) | ✓ |
| `tiger_end_point` | tiger end point |  | varchar(255) | ✓ |
| `connect_edc_ktb` | เชื่อมต่อเครื่องรูดบัตร กรุงไทย *(resource only)* |  | char |  |
| `connect_edc_ktb_port` | Port เครื่องรูดบัตร กรุงไทย *(resource only)* |  | char |  |
| `alcohore_sell_time_range` | ช่วงเวลาขายเครื่องดื่มแอลกอฮอล์ |  | varchar(500) | ✓ |
| `check_alcoholic_sell` | ตรวจสอบช่วงเวลาขายเครื่องดื่มแอลกอฮอล์ |  | smallint | ✓ |

## POS_ID

**รหัสเครื่อง POS** — รหัสเครื่อง POS

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `MACHINECODE` | รหัสเครื่องPOS |  | varchar(10) |  |
| `pos_id` | เลขที่เครื่อง |  | varchar(30) |  |
| `status` | สถานะ |  | smallint |  |
| `guid_code` | GUID |  | varchar(35) | ✓ |
| `pos_config_number` | ลำดับที่ค่าเริ่มต้น |  | smallint | ✓ |
| `price_number` | ลำดับราคา |  | smallint | ✓ |
| `doc_format` | รูปแบบเลขที่เอกสารใบกำกับภาษีแบบย่อ |  | varchar(50) | ✓ |
| `doc_format_vat_full` | รูปแบบเลขที่เอกสารใบกำกับภาษีแบบเต็ม |  | varchar(50) | ✓ |
| `doc_format_cancel` | รูปแบบเลขที่เอกสารยกเลิก |  | varchar(50) | ✓ |
| `doc_format_fillmoney` | รูปแบบเลขที่เอกสารเติมเงิน |  | varchar(50) | ✓ |
| `doc_format_cashierSettle` | รูปแบบเลขที่เอกสารบันทึกส่งเงิน |  | varchar(50) | ✓ |
| `pos_ic_wht` | คลังสินค้า |  | varchar(25) | ✓ |
| `pos_ic_shelf` | ที่เก็บสินค้า |  | varchar(25) | ✓ |
| `pos_type_invoice` | ชนิดใบกำกับที่พิมพ์ |  | smallint | ✓ |
| `pos_semi_invoice` | ใบกำกับภาษีอย่างย่อ *(resource only)* |  | char |  |
| `pos_full_invoice` | ใบกำกับภาษีอย่างเต็ม *(resource only)* |  | char |  |
| `pos_save_e_journal` | บันทึก e-Journal |  | smallint | ✓ |
| `slip_number` | ลำดับที่ใบกำกับภาษีอย่างย่อ |  | smallint | ✓ |
| `close_form_number` | ลำดับฟอร์มปิดโต๊ะ |  | smallint | ✓ |
| `doc_running_inv` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_running_vat_full` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_running_cancel` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_running_fillmoney` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_running_cashierSettle` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `doc_format_deposit` | รหัสเอกสารเงินมัดจำ |  | varchar(50) | ✓ |
| `doc_running_deposit` | เลขที่เอกสารเงินมัดจำเริ่มต้น |  | varchar(100) | ✓ |
| `doc_format_deposit_return` | รหัสเอกสารคืนเงินมัดจำ |  | varchar(50) | ✓ |
| `doc_running_deposit_return` | เลขที่เอกสารคืนเงินมัดจำเริ่มต้น |  | varchar(100) | ✓ |
| `doc_format_deposit_cancel` | รหัสเอกสารยกเลิกเงินมัดจำ |  | varchar(25) | ✓ |
| `branch_code` | สาขา |  | varchar(10) | ✓ |
| `doc_format_deposit_return_cancel` | รหัสเอกสารยกเลิกคืนเงินมัดจำ |  | varchar(25) | ✓ |
| `use_credit_sale` | อนุญาติให้ขายเงินเชื่อ |  | smallint | ✓ |
| `show_order_detail` | แสดงรายละเอียดการสั่งอาหาร |  | smallint | ✓ |
| `show_in_copy` | แสดงเฉพาะในสำเนาใบเสร็จ |  | smallint | ✓ |
| `no_remark_sendmoney` | ไม่แสดงข้อความท้ายใบสงเงิน |  | smallint | ✓ |
| `pos_header` | ข้อความหัวใบเสร็จ |  | varchar(1000) | ✓ |
| `doc_format_credit` | รูปแบบเลขที่เอกสารขายเชื่อ |  | varchar(50) | ✓ |
| `doc_running_credit` | เลขที่เอกสารเริ่มต้น |  | varchar(100) | ✓ |
| `doc_format_code_credit` | รหัสเอกสาร(ขายเชื่อ) |  | varchar(10) | ✓ |
| `doc_format_code_inv` | รหัสเอกสารใบกำกับภาษีแบบย่อ *(resource only)* |  | char |  |
| `doc_format_code_tax_inv` | รหัสเอกสารใบกำกับภาษีแบบเต็ม |  | varchar(50) | ✓ |
| `doc_format_code_doc_cancel` | รหัสเอกสารยกเลิก |  | varchar(50) | ✓ |
| `doc_format_code_fill_money` | รหัสเอกสารรับเงินทอน |  | varchar(50) | ✓ |
| `doc_format_code_send_money` | รหัสเอกสารส่งเงิน |  | varchar(50) | ✓ |
| `doc_format_template` | รูปแบบเอกสาร *(resource only)* |  | char |  |
| `department_code` | แผนก |  | varchar(50) | ✓ |
| `bcel_mcid` | BCEL MCID |  | varchar(255) | ✓ |
| `bcel_mcc` | BCEL MCC |  | varchar(255) | ✓ |
| `close_check_credit_sale_customer` | ปิดตรวจสอบลูกค้าเงินเชื่อ |  | smallint | ✓ |
| `order_of_sales_summary` | ลำดับที่ใบสรุปยอดขาย |  | smallint | ✓ |
| `sml_kbank_qr_api_config` | SML QR KBank |  | smallint | ✓ |
| `sml_kbank_qr_credit` | KBank QR Code Credit Card |  | smallint | ✓ |
| `sml_kbank_qr_api_token` | Connection Token |  | varchar(255) | ✓ |
| `sml_kbank_qr_api_uat_mode` | UAT Mode |  | smallint | ✓ |

## chef_master

**ผู้ปรุงอาหาร** — Chef Master

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `chef_code` | รหัสผู้ปรุงอาหาร |  | varchar(25) |  |
| `chef_name` | ชื่อผู้ปรุงอาหาร |  | varchar(255) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `tab_chefmasteritem` | รายการอาหาร *(resource only)* |  | char |  |
| `guid_code` | guid_code |  | varchar(35) | ✓ |

## chef_master_item

**รายการอาหารของพ่อครัว** — Chef Master Item

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `chef_code` | Chef Code |  | varchar(25) |  |
| `item_code` | รหัสอาหาร/เครื่องดื่ม |  | varchar(25) |  |
| `item_name` | ชื่ออาหาร/เครื่องดื่ม *(resource only)* |  | char |  |

index: `chef_master_item_PK_PRIMARY`(chef_code,item_code)

## coupon_list

**ทะเบียนคูปอง** — Table 270

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `number` | หมายเลขคูปอง |  | varchar(25) |  |
| `amount` | มูลค่า |  | float | ✓ |
| `last_status` | ยกเลิก |  | smallint | ✓ |
| `date` | วันที่ออกคูปอง |  | datetime | ✓ |
| `date_expire` | วันที่หมดอายุ |  | datetime | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `balance_amount` | มูลค่าคงเหลือ |  | float | ✓ |
| `guid_code` | GUID |  | varchar(35) | ✓ |
| `coupon_type` | ประเภทคูปอง | Coupon Type | smallint | ✓ |
| `coupon_discount_amount` | ลดตามมูลค่า *(resource only)* | Discount Amount | char |  |
| `coupon_discount_percent` | ลดตามเปอร์เซ็นต์ *(resource only)* | Discount Percent | char |  |
| `single_use` | ใช้งานเพียงครั้งเดียว | Single Use | smallint | ✓ |
| `cust_code` | รหัสลูกค้า | Customer Code | varchar(50) | ✓ |
| `coupon_group` | กลุ่มคูปอง | Coupon Group | varchar(25) | ✓ |

index: `coupon_list_PK_PRIMARY_coupon_number`(number)

## ic_promotion_formula

**Promotion** — Table 262

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโปรโมชั่น |  | varchar(25) |  |
| `name_1` | ชื่อโปรโมชั่น |  | varchar(100) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `order_number` | ลำดับความสำคัญ |  | smallint | ✓ |
| `guid_code` | guid |  | varchar(35) | ✓ |
| `cust_code_condition` | ใช้เงื่อนไขรหัสลูกค้า |  | smallint | ✓ |
| `cust_group_condition` | ใช้เงื่อนไขกลุ่มลูกค้า |  | smallint | ✓ |
| `case_number` | ประเภทโปรโมชั้น |  | smallint | ✓ |
| `case_1` | ส่วนลดตามจำนวนเต็ม *(resource only)* |  | char |  |
| `case_0` | ประเภทโปรโมชั่น *(resource only)* |  | char |  |
| `case_2` | ส่วนลดสินค้าจัดชุด *(resource only)* |  | char |  |
| `case_3` | ส่วนลดสินค้าจัดชุด (รวมกลุ่ม) *(resource only)* |  | char |  |
| `case_4` | ของแถมสินค้าจัดชุด *(resource only)* |  | char |  |
| `member_condition` | เงื่อนไขสมาชิก |  | smallint | ✓ |
| `all_member_condition` | ทั้งหมด *(resource only)* |  | char |  |
| `for_member_only` | ลูกค้าสมาชิก *(resource only)* |  | char |  |
| `for_non_member_only` | ลูกค้าทั่วไป *(resource only)* |  | char |  |
| `auto_change_unitcode` | ปรับหน่วยนับอัตโนมัติ |  | smallint | ✓ |
| `lock_promotion` | แบบเฉพาะ |  | smallint | ✓ |
| `lock_promotion_1` | ทุกเครื่องในระบบ *(resource only)* |  | char |  |
| `lock_promotion_2` | ตามรหัสเครื่อง POS *(resource only)* |  | char |  |
| `lock_code_list` | รหัสเครื่อง POS |  | varchar(1000) | ✓ |
| `is_no_discount` | ไม่นำมูลค่าสินค้าไปคิดส่วนลด |  | smallint | ✓ |
| `from_date` | ตั้งแต่วันที่ |  | datetime | ✓ |
| `to_date` | ถึงวันที่ |  | datetime | ✓ |
| `use_date_range` | ใช้ระบบโปรโมชั่นตามวันที่ |  | smallint | ✓ |
| `case_5` | ของแถมสินค้าตามมูลค่า *(resource only)* |  | char |  |
| `item_normal_price` | เฉพาะสินค้าราคาปรกติ |  | smallint | ✓ |
| `lock_day` | เฉพาะวัน |  | varchar(1000) | ✓ |

index: `ic_promotion_formula_PK_code`(code)

## ic_promotion_formula_action

**ผลที่ได้** — Table 296

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโปรโมชั้น |  | varchar(25) | ✓ |
| `qty_from` | จากจำนวน |  | float | ✓ |
| `qty_to` | ถึงจำนวน |  | float | ✓ |
| `action_command` | คำสั่ง |  | varchar(255) | ✓ |
| `action_1` | ให้ส่วนลด *(resource only)* |  | char |  |
| `qty_1` | จำนวนเต็ม *(resource only)* |  | char |  |

index: `ic_promotion_formula_action_idx`(code)

## ic_promotion_formula_condition

**เงื่อนไข** — Table 281

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโปรโมชั่น |  | varchar(25) |  |
| `condition_case` | เงื่อนไข (1=ใช้,0=ยกเว้น) |  | smallint | ✓ |
| `line_number` | บรรทัดที่ |  | smallint |  |
| `condition_from` | จาก |  | varchar(50) | ✓ |
| `condition_to` | ถึง |  | varchar(50) | ✓ |
| `condition_value_from` | จาก |  | float | ✓ |
| `condition_value_to` | ถึง |  | float | ✓ |
| `condition_type` | 1=Barcode,2=สินค้า,3=กลุ่มสินค้า,5=กลุ่มลูกค้า |  | smallint | ✓ |
| `condition_name_item` | เงื่อนไขสินค้า *(resource only)* |  | char |  |
| `condition_name_item_code` | เงื่อนไขรหัสสินค้า *(resource only)* |  | char |  |
| `condition_name_item_group` | เงื่อนไขกลุ่มสินค้า *(resource only)* |  | char |  |
| `condition_name_cust` | เงื่อนไขลูกค้า *(resource only)* |  | char |  |
| `condition_name_cust_group` | เงื่อนไขกลุ่มลูกค้า *(resource only)* |  | char |  |
| `condition_barcode` | Barcode *(resource only)* |  | char(50) |  |
| `condition_unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `condition_value_qty_from` | จากจำนวน |  | char | ✓ |
| `condition_value_qty_to` | ถึงจำนวน *(resource only)* |  | char |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `item_group_code` | กลุ่มสินค้า *(resource only)* |  | char |  |
| `item_group_name` | ชื่อกลุ่มสินค้า *(resource only)* |  | char |  |
| `item_code` | รหัสสินค้า *(resource only)* |  | char |  |
| `unit_type` | ประเภทหน่วยนับ |  | smallint | ✓ |
| `condition_group` | กลุ่ม |  | smallint | ✓ |

index: `ic_promotion_formula_condition_pk`(code)

## ic_promotion_formula_group_qty

**จำนวนตามกลุ่ม** — Table 299

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโปรโมชั่น |  | varchar(25) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `group_number` | กลุ่มที่ |  | smallint | ✓ |
| `group_amount` | มูลค่าสินค้า |  | float | ✓ |

index: `ic_promotion_formula_group_qty_idx`(code)

## ic_promotion_formula_price_discount

**ราคา/ส่วนลด** — Table 282

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `item_unit` | หน่วย |  | varchar(25) | ✓ |
| `qty_start` | จำนวนเริ่มต้น |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `discount` | ส่วนลด |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char | ✓ |
| `unit_type` | ประเภทหน่วยนับ |  | smallint | ✓ |
| `code` | รหัสโปรโมชั่น |  | varchar(25) | ✓ |
| `line_number` | บรรทัดที่ |  | smallint | ✓ |
| `qty_end` | จำนวนสิ้นสุด |  | float | ✓ |

## ic_trans_discount_group

**รายละเอียดการลดตามกลุ่ม** — ic_trans_discount_group

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `discount_group_code` | รหัสกลุ่มส่วนลด |  | varchar(25) | ✓ |
| `discount_group_name` | ชื่อกลุ่มส่วนลด |  | varchar(255) | ✓ |
| `discount_word` | ส่วนลด |  | varchar(100) | ✓ |
| `group_amount` | มูลค่าตามกลุ่ม |  | float | ✓ |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |

index: `doc_no_doc_date_trans_flag`(doc_no,doc_date,trans_flag)

## kitchen_command

**คำสั่งพิเศษ** — Table 311

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสาร |  | varchar(50) | ✓ |
| `doc_date` | วันที่ |  | varchar(50) | ✓ |
| `doc_time` | เวลา |  | varchar(20) | ✓ |
| `doc_type` | ประเภทเอกสาร(0=order,1=cancel) |  | smallint | ✓ |
| `kitchen_data` | data |  | text(5000) | ✓ |

## kitchen_master

**ครัว/บาร์น้ำ** — Table 276

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | code | varchar(25) |  |
| `name_1` | ชื่อ | name | varchar(100) |  |
| `guid_code` | guid |  | varchar(35) | ✓ |
| `printer_name` | ชื่อเครื่องพิมพ์/IP |  | varchar(100) | ✓ |
| `printer_mode` | ประเภทการพิมพ์ |  | smallint | ✓ |
| `printer_mode_1` | ผ่าน Windows Driver *(resource only)* |  | char |  |
| `printer_mode_2` | พิมพ์ตรงไปยังเครื่องพิมพ์ (Direct) *(resource only)* |  | char |  |
| `printer_mode_3` | พิมพ์ผ่าน TCP/IP *(resource only)* |  | char |  |
| `print_to_kitchen` | พิมพ์ใบสั่งอาหาร |  | smallint | ✓ |
| `print_summery` | พิมพ์ใบสั่งอาหารแบบรวม |  | smallint | ✓ |
| `served_control` | ใช้ระบบควบคุมการเสิร์ฟ |  | smallint | ✓ |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `tab_print_option` | ตัวเลือกการพิมพ์ *(resource only)* |  | char |  |
| `slip_header_font` | รูปแบบตัวอักษรหัวกระดาษ |  | varchar(255) | ✓ |
| `slip_sub_header_font` | รูปแบบตัวอักษรหัวข้อย่อยกระดาษ |  | varchar(255) | ✓ |
| `slip_detail_font` | รูปแบบตัวอักษรรายการอาหาร |  | varchar(255) | ✓ |
| `last_member_code` | สมาชิกล่าสุด |  | varchar(25) | ✓ |
| `printer_manual_feed` | ใช้เครื่องพิมพ์แบบฉีกกระดาษ |  | smallint | ✓ |
| `printer_slip_width` | ความกว้างกระดาษ (Point) |  | float | ✓ |
| `barcode_print` | พิมพ์ Barcode Checker |  | smallint | ✓ |
| `print_order_for_check` | พิมพ์ ใบเช็ครายการสั่งอาหาร |  | smallint | ✓ |
| `print_order_per_unit` | พิมพ์ใบสั่งอาหารแบบกระจายจำนวน |  | smallint | ✓ |
| `kitchen_ready` | พร้อมพิมพ์ |  | smallint | ✓ |
| `print_tableopen` | พิมพ์ใบเปิดโต๊ะ |  | smallint | ✓ |
| `tab_packing_pos` | จุดพิมพ์ใบสั่งจัด *(resource only)* |  | char |  |
| `print_order_number_barcode` | พิมพ์บาร์โค๊ดเลขที่ใบสั่งจัด |  | smallint | ✓ |
| `print_barcode` | พิมพ์บาร์โค๊ดสินค้า |  | smallint | ✓ |
| `print_copy` | พิมพ์สำเนา |  | smallint | ✓ |
| `print_copy_mode` | ประเภทการพิมพ์ |  | smallint | ✓ |
| `print_copy_name` | ชื่อเครื่องพิมพ์ |  | varchar(255) | ✓ |
| `print_number_order_check` | พิมพ์ลำดับใบเช็ครายการสั่งอาหาร |  | smallint | ✓ |
| `print_language_index` | ภาษาที่พิมพ์ |  | smallint | ✓ |
| `print_thai` | ภาษาไทย *(resource only)* |  | char |  |
| `print_english` | English *(resource only)* |  | char |  |
| `print_malayu` | Malayu *(resource only)* |  | char |  |
| `print_chainese` | Chainese *(resource only)* |  | char |  |
| `print_india` | India *(resource only)* |  | char |  |
| `print_lao` | Lao *(resource only)* |  | char |  |
| `no_price_print` | ไม่พิมพ์ราคาสินค้า |  | smallint | ✓ |
| `speech_serial` | หมายเลขเครื่องพูดรายการอาหาร |  | varchar(25) | ✓ |
| `no_number_order_for_check` | ไม่แสดงลำดับรายการในใบสรุป |  | smallint | ✓ |
| `tab_print_copy` | สำเนาการพิมพ์ *(resource only)* |  | char |  |
| `tab_cancel_copy` | สำเนาการยกเลิกรายการ *(resource only)* |  | char |  |
| `hide_table_footer_bill` | ไม่แสดงหมายเลขโต๊ะท้ายใบสั่งอาหาร |  | smallint | ✓ |
| `hide_repeat_order_bill` | ไม่แสดงจำนวนครั้งที่สั่งเพิ่ม |  | smallint | ✓ |

index: `kitchen_master_kitchen_master_pk`(code)

## kitchen_master_item

**รายการอาหารในครัว** — Table 278

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `kitchen_code` | รหัสครัว |  | varchar(25) |  |
| `food_code` | รหัสอาหาร/เครื่องดื่ม |  | varchar(25) |  |
| `food_name` | ชื่ออาหาร/เครื่องดื่ม *(resource only)* |  | char |  |

index: `kitchen_master_item_kitchen_master_item_pk`(kitchen_code,food_code)

## kitchen_master_order_id

**เชื่อมครัวกับเครื่องสั่งอาหาร** — Table 277

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `kitchen_code` | รหัสครัว |  | varchar(25) |  |
| `order_device` | รหัสจุดสั่งอาหาร |  | varchar(25) |  |
| `selected` | เลือกใช้ *(resource only)* |  | char |  |
| `order_device_name` | ชื่อจุดสั่งอาหาร *(resource only)* |  | char |  |

index: `kitchen_master_order_id_kitchen_master_order_id_pk`(kitchen_code,order_device)

## kitchen_master_pos_id

**เชื่อมครัวกับเครื่อง POS** — Kitchen Master POS ID

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `kitchen_code` | รหัสครัว |  | varchar(25) |  |
| `pos_id` | รหัสเครื่อง POS |  | varchar(25) |  |
| `selected` | เลือกใช้ |  | smallint |  |
| `pos_number` | เลขเครื่อง POS *(resource only)* |  | char |  |

## kitchen_print_cancel_copy

**พิมพ์สำเนารายการยกเลิกอาหาร** — Kitchen Print Cancel Copy

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `kitchen_code` | รหัสครัว | Kitchen Code | varchar(25) |  |
| `print_mode` | ประเภทการพิมพ์ |  | smallint | ✓ |
| `print_name` | ชื่อเครื่องพิมพ์ |  | varchar(250) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |

## kitchen_print_copy

**พิมพ์สำเนาห้องครัว/บาร์น้ำ** — Kitchen Print Copy

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `kitchen_code` | รหัสครัว |  | varchar(25) |  |
| `print_mode` | ประเภทการพิมพ์ |  | smallint | ✓ |
| `print_name` | ชื่อเครื่องพิมพ์ | Printer Name | varchar(250) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `line_number` | Line Number | Line Number | smallint | ✓ |

## order_checker

**ตรวจสอบรายการอาหาร** — order_checker

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `guid_line` | GUID Line |  | varchar(50) |  |
| `guid_confirm` | GUID Confirm |  | varchar(50) |  |
| `cofirm_date` | Confirm Date |  | datetime | ✓ |
| `confirm_time` | Confirm Time |  | varchar(10) | ✓ |
| `confirm_status` | Confirm Status |  | smallint | ✓ |
| `order_qty` | Order Qty |  | float | ✓ |

index: `idx_guid_confirm`(guid_confirm), `idx_guid_line`(guid_line), `idx_order_checker_doc_date`(doc_date), `idx_confirm_status`(confirm_status)

## order_device_id

**รหัสเครื่องสั่งอาหาร**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `device_id` | รหัสจุดสั่งอาหาร |  | varchar(10) |  |
| `device_name` | ชื่อจุดสั่งอาหาร |  | varchar(50) |  |
| `doc_format_order` | รูปแบบเอกสารใบสั่ง |  | varchar(255) | ✓ |
| `device_status` | สถานะ |  | smallint |  |
| `guid_code` | guid |  | varchar(50) | ✓ |
| `price_number` | ลำดับราคา |  | smallint | ✓ |
| `print_orderdetail_onclose` | พิมพ์ใบแสดงรายการปิดโต๊ะ *(resource only)* |  | char |  |
| `printer_mode` | ประเภทการพิมพ์ *(resource only)* |  | char |  |
| `printer_mode_1` | ผ่าน Windows Driver *(resource only)* |  | char |  |
| `printer_mode_2` | พิมพ์ตรงไปยังเครื่องพิมพ์ (Direct Print) *(resource only)* |  | char |  |
| `printer_mode_3` | พิมพ์ผ่าน TCP/IP *(resource only)* |  | char |  |
| `printer_name` | ชื่อเครื่องพิมพ์/IP *(resource only)* |  | char |  |
| `close_form_number` | ลำดับฟอร์มปิดโต๊ะ |  | smallint | ✓ |
| `tab_order_device_config` | กำหนดคุณสมบัติเครื่องสั่งอาหาร *(resource only)* |  | char |  |
| `pos_slip_header_font` | รูปแบบตัวอักษรส่วนหัวใบเสร็จ *(resource only)* |  | char |  |
| `pos_slip_detail_font` | รูปแบบตัวอักษรส่วนรายละเอียดใบเสร็จ *(resource only)* |  | char |  |
| `pos_slip_footer_font` | รูปแบบตัวอักษรส่วนท้ายใบเสร็จ *(resource only)* |  | char |  |
| `tab_pos_slip_font_config` | ใบเสร็จและการพิมพ์ *(resource only)* |  | char |  |
| `pos_config_number` | ลำดับที่ค่าเริ่มต้น |  | smallint | ✓ |
| `device_disable_password` | ปิดระบบถามรหัสผ่าน |  | smallint | ✓ |
| `device_android` | เป็นเครื่อง Android |  | smallint | ✓ |
| `printer_manual_feed` | ใช้เครื่องพิมพ์แบบฉีกมือ *(resource only)* |  | char |  |
| `pos_slip_width` | ความกว้างหน้ากระดาษ *(resource only)* |  | char |  |
| `print_from_center` | ใช้ระบบพิมพ์จากส่วนกลาง |  | smallint | ✓ |
| `remark_print` | แสดงหมายเหตุในรายการปิดโต๊ะ *(resource only)* |  | char |  |
| `summary_detail_font_name` | ตัวอักษรหน้าจอสรุปรายการ *(resource only)* |  | char |  |
| `device_html` | ใชระบบ Browser |  | smallint | ✓ |
| `user_access` | รหัสพนักงานที่ใช้ได้ |  | varchar(255) | ✓ |
| `is_dot_printer` | เป็นเครื่องพิมพ์ Dotmatrix *(resource only)* | Dotmatrix Printer | char |  |

## pos_log

**ประวัติการใช้งาน POS** — POS Log

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `user_code` | รหัสพนักงาน |  | varchar(25) |  |
| `datetime` | DateTime |  | datetime |  |
| `command` | คำสั่ง |  | varchar(255) |  |
| `message` | ข้อความ |  | varchar(500) | ✓ |
| `approve_code` | รหัสผู้อนุมัติ |  | varchar(25) |  |
| `amount` | มูลค่าสินค้า |  | float | ✓ |
| `command_type` | ประเภท Command |  | varchar(50) | ✓ |

## pos_period

**กะการทำงาน** — Table 269

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `machine_code` | รหัสเครื่อง |  | varchar(10) | ✓ |
| `begin_date` | วันที่เปิดกะ |  | datetime | ✓ |
| `begin_time` | เวลาเปิดกะ |  | varchar(10) | ✓ |
| `end_date` | วันที่ปิดกะ |  | datetime | ✓ |
| `end_time` | เวลาปิดกะ |  | varchar(10) | ✓ |
| `period_status` | สถานะ (0=เปิดใช้,1=ปิดแล้ว) |  | smallint | ✓ |
| `begin_user_code` | รหัสพนักงานเปิดกะ |  | varchar(25) | ✓ |
| `end_user_code` | รหัสพนักงานปิดกะ |  | varchar(25) | ✓ |
| `password` | รหัสผ่าน *(resource only)* |  | char |  |
| `period_guid` | GUID |  | varchar(50) | ✓ |

## pos_point_condition

**เงื่อนไขการให้แต้ม** — Table 267

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `birth_month` | ซื้อในเดือนเกินได้แต้มคูณ (เท่า) |  | float | ✓ |
| `birth_day` | ซื้อในวันเกินได้แต้มคูณ (เท่า) |  | float | ✓ |
| `birth_month_use` | ใช้ระบบคูณแต้มในเดือนเกิด |  | smallint | ✓ |
| `birth_day_use` | ใช้ระบบคูณแต้มในวันเกิด |  | smallint | ✓ |

## pos_point_period

**กำหนดอัตราแต้มสะสม** — Table 268

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `from_date` | จากวันที่ |  | datetime | ✓ |
| `to_date` | ถึงวันที่ |  | datetime | ✓ |
| `amount` | จำนวนเงินต่อหนึ่งแต้ม |  | float | ✓ |
| `point_value` | มูลค่าต่อหนึ่งแต้ม |  | float | ✓ |
| `point_value_condition` | เงื่อนไขมูลค่าต่อแต้ม |  | varchar(1000) | ✓ |

## pos_point_special_day

**กำหนดวันพิเศษ** — Table 268

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `from_date` | จากวันที่ |  | datetime | ✓ |
| `to_date` | ถึงวันที่ |  | datetime | ✓ |
| `multiply_point` | คูณแต้ม |  | float | ✓ |
| `description` | รายละเอียด |  | varchar(100) | ✓ |
| `day_1` | จันทร์ |  | smallint | ✓ |
| `day_2` | อังคาร |  | smallint | ✓ |
| `day_3` | พุธ |  | smallint | ✓ |
| `day_4` | พฤหัสบดี |  | smallint | ✓ |
| `day_5` | ศุกร์ |  | smallint | ✓ |
| `day_6` | เสาร์ |  | smallint | ✓ |
| `day_7` | อาทิตย์ |  | smallint | ✓ |
| `day_0` | ทุกวัน |  | smallint | ✓ |
| `order_condition` | ลำดับ |  | smallint | ✓ |

## pos_resource

**pos_resource** — pos_resource

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่ *(resource only)* |  | char |  |
| `doc_time` | เวลา *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `sale_code` | รหัสพนักงาน *(resource only)* |  | char |  |
| `pos_id` | เลขเครื่อง *(resource only)* |  | char |  |
| `doc_amount` | ยอดขาย *(resource only)* |  | char |  |
| `point_add` | แต้มเพิ่ม *(resource only)* |  | char |  |
| `point_use` | ใช้แต้ม *(resource only)* |  | char |  |
| `point_balance` | แต้มคงเหลือ *(resource only)* |  | char |  |
| `branch_code` | สาขา *(resource only)* |  | char |  |

## pos_settle_bill_cancel

**รายการส่งเงินบิลยกเลิก** — POS Settle Bill Cancel

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `pos_id` | รหัสเครื่อง POS |  | varchar(50) |  |
| `ref_doc_no` | เอกสารอ้างอิง |  | varchar(50) |  |
| `ref_doc_date` | เอกสารอ้างอิงวันที่ |  | smalldatetime | ✓ |
| `ref_amount` | มูลค่า |  | float |  |
| `period_guid` | GUID |  | varchar(50) |  |
| `invoice_doc_no` | เลขที่ใบเสร็จรับเงิน/ใบกำกับภาษี |  | varchar(50) |  |
| `invoice_doc_date` | วันที่ใบเสร็จรับเงิน/ใบกำกับภาษี |  | smalldatetime | ✓ |

## pos_settle_bill_discount

**รายละเอียดการส่งบิลส่วนลด** — POS Setttle Bill Discount

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขทีเอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `pos_id` | รหัสเครื่อง POS |  | varchar(50) |  |
| `ref_doc_no` | เลขที่เอกสารอ้างอิง |  | varchar(50) |  |
| `ref_doc_date` | วันที่เอกสารอ้างอิง |  | smalldatetime |  |
| `sum_amount` | มูลค่าสินค้า |  | float |  |
| `discount_amount` | ยอดส่วนลด |  | float |  |
| `total_amount` | มูลค่าสุทธิ |  | float |  |
| `period_guid` | GUID |  | varchar(50) | ✓ |
| `discount_item` | ส่วนลดรวมต่อรายการ |  | float | ✓ |

## pos_settle_group_discount

**รายละเอียดส่วนลดตามกลุ่ม** — pos_settle_group_discount

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `pos_id` | รหัสเครื่อง POS |  | varchar(50) |  |
| `discount_group_code` | รหัสกลุ่มส่วนลด |  | varchar(50) | ✓ |
| `discount_group_amount` | มูลค่าตามกลุ่มส่วนลด |  | float | ✓ |
| `discount_group_discount` | ส่วนลดรวม |  | float | ✓ |
| `discount_group_name` | ชื่อกลุ่มส่วนลด *(resource only)* |  | char |  |
| `line_number` | LineNumber |  | smallint |  |

index: `doc_no_doc_date`(doc_no,doc_date)

## pos_slip_campaign

**POS Slip Campaign** — POS Slip Campaign

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสแคมเปญ |  | varchar(255) |  |
| `name_1` | ชื่อแคมเปญ |  | varchar(255) |  |
| `guid_code` | GUID |  | varchar(50) | ✓ |
| `enable` | สถานะ |  | smallint | ✓ |
| `date_begin` | วันที่เริ่ม |  | smalldatetime | ✓ |
| `time_begin` | เวลา |  | varchar(10) | ✓ |
| `date_end` | วันที่สิ้นสุด |  | smalldatetime | ✓ |
| `time_end` | เวลา |  | varchar(10) | ✓ |
| `sale_amount` | มูลค่าสินค้า |  | float | ✓ |
| `display_wording` | ข้อความที่ต้องการแสดง |  | text | ✓ |
| `bill_limit` | จำกัดต่อบิล |  | float | ✓ |

index: `pos_slip_campaign_PK_code`(code)

## pos_slip_campaign_brand

**Pos Slip Campaign Brand** — Pos Slip Campaign Brand

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `campaign_code` | รหัสแคมเปญ |  | varchar(50) | ✓ |
| `code` | รหัส |  | varchar(50) | ✓ |
| `name_1` | ชื่อ *(resource only)* |  | varchar(50) |  |
| `line_number` | line number |  | smallint | ✓ |

## pos_slip_campaign_category

**Pos Slip Campaign Category** — Pos Slip Campaign Category

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `campaign_code` | รหัสแคมเปญ |  | varchar(50) | ✓ |
| `code` | รหัส |  | varchar(50) | ✓ |
| `name_1` | ชื่อ *(resource only)* |  | char |  |
| `line_number` | line number |  | smallint | ✓ |

## pos_slip_campaign_group

**Pos Slip Campaign Group** — Pos Slip Campaign Group

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `campaign_code` | รหัสแคมเปญ |  | varchar(50) | ✓ |
| `group_main` | รหัสกลุ่มหลัก |  | varchar(50) | ✓ |
| `group_sub1` | รหัสกลุ่มย่อย |  | varchar(50) | ✓ |
| `group_sub2` | รหัสกลุ่มย่อย2 |  | varchar(50) | ✓ |
| `line_number` | line number |  | smallint | ✓ |
| `group_main_name` | ชื่อกลุ่มหลัก *(resource only)* |  | char |  |
| `group_sub1_name` | ชื่อกลุ่มย่อย *(resource only)* |  | char |  |
| `group_sub2_name` | ชื่อกลุ่มย่อย2 *(resource only)* |  | char |  |

## pos_slip_campaign_items

**POS Slip Campaign Items** — POS Slip Campaign Items

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `campaign_code` | รหัสเคมเปญ |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `unit_code` | หน่วยนับ |  | varchar(50) |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `line_number` | Line Number |  | smallint | ✓ |

## pos_sync_device

**Table 308** — Table 308

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `command` | command |  | varchar(255) | ✓ |
| `command_guid` | guid |  | varchar(50) | ✓ |
| `last_status` | status |  | smallint | ✓ |
| `cust_code` | รหัสสมาชิก |  | varchar(50) | ✓ |
| `food_discount` | ส่วนลดค่าอาหาร |  | varchar(50) | ✓ |
| `is_promotion` | มี Promotion |  | smallint | ✓ |
| `total_discount` | ส่วนลด |  | varchar(100) | ✓ |
| `sale_code` | รหัสพนักงาน |  | varchar(50) | ✓ |
| `table_number` | เลขที่โต๊ะ |  | varchar(50) | ✓ |
| `result1` | result 1 |  | varchar(10000) | ✓ |
| `result2` | result 2 |  | varchar(10000) | ✓ |
| `service_charge` | Service Charge |  | varchar(100) | ✓ |

index: `pos_sync_device_guid`(command_guid), `pos_sync_device_last_status`(last_status)

## pos_view_column

**รายละเอียดหน้าจอค้นหา** — View column · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `screen_group` | กลุ่มหน้าจอ | Screen group | int | ✓ |
| `screen_code` | รหัสหน้าจอ | Screen code | varchar(50) |  |
| `column_number` | ลำดับที่ | Column number | int | ✓ |
| `column_name` | ชื่อ | Column name | varchar(255) | ✓ |
| `column_name_2` | ชื่อ (ภาษาอังกฤษ) | Column name eng | varchar(255) | ✓ |
| `column_field_name` | ชื่อข้อมูล | Column field name | varchar(500) | ✓ |
| `column_field_sort` | ชื่อข้อมูลเพื่อเรียง | Column field for sort | varchar(500) | ✓ |
| `column_width` | ความกว้าง | Column width | int | ✓ |
| `column_type` | ประเภท | Column type | int | ✓ |
| `column_align` | จัดช่อง | Column align | int | ✓ |
| `column_format` | รูปแบบ | Column format | varchar(255) | ✓ |

## pos_view_table

**รายละเอียดการแสดงผลแต่ละหน้าจอ** — View by Table · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `screen_code` | รหัสหน้าจอ | Screen code | varchar(50) |  |
| `name_1` | ชื่อหน้าจอ | Screen name | varchar(255) |  |
| `name_2` | ชื่อหน้าจอ (ภาษาอังกฤษ) | Screen 2 | varchar(255) | ✓ |
| `table_name` | ชื่อตารางข้อมูลหลัก | Table name | varchar(255) | ✓ |
| `table_list` | ชื่อตารางข้อมูลที่เกี่ยวข้อง | Table list | varchar(255) | ✓ |
| `sort` | ชื่อข้อมูลที่จะเรียง | Sort | varchar(255) | ✓ |
| `filter` | เงื่อนไขการแสดงผล | Filter | varchar(255) | ✓ |
| `width_persent` | ความกว้างเป็นเปอร์เซ็นต์ | Width by persent | int | ✓ |

index: `pos_view_table_PK_CODE`(screen_code)

## printer_order_check

**จุดพิมพ์ใบเช็ครายการสั่งอาหาร** — Printer Order Check

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโซน |  | varchar(25) |  |
| `name_1` | ชื่อโซน |  | varchar(255) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `printer_name` | ชื่อเครื่องพิมพ์/IP |  | varchar(100) | ✓ |
| `print_mode` | ประเภทการพิมพ์ |  | smallint | ✓ |
| `print_mode_1` | ผ่าน Windows Driver *(resource only)* |  | char |  |
| `print_mode_2` | พิมพ์ตรงไปยังเครื่องพิมพ์ (Direct) *(resource only)* |  | char |  |
| `print_mode_3` | พิมพ์ผ่าน TCP/IP *(resource only)* |  | char |  |
| `guid_code` | GUID |  | varchar(50) | ✓ |

## printer_order_check_table

**กำหนดโต๊ะพิมพ์ใบเช็ครายการสั่งอาหาร** — กำหนดโต๊ะพิมพ์ใบเช็ครายการสั่งอาหาร

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `zone_code` | รหัสโซน |  | varchar(25) |  |
| `table_number` | หมายเลขโต๊ะ |  | varchar(25) |  |
| `line_number` | บรรทัด |  | smallint | ✓ |
| `table_name` | ชื่อโต๊ะ *(resource only)* |  | char |  |

## table_master

**โต๊ะอาหาร** — Table 271

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `number` | หมายเลขโต๊ะ |  | varchar(25) |  |
| `name_1` | ชื่อโต๊ะ |  | varchar(50) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid |  | varchar(35) | ✓ |
| `level_1` | ลำดับที่ 1 |  | varchar(50) | ✓ |
| `level_2` | ลำดับที่ 2 |  | varchar(50) | ✓ |
| `level_3` | ลำดับที่ 3 |  | varchar(50) | ✓ |
| `level_4` | ลำดับที่ 4 |  | varchar(50) | ✓ |
| `open_date` | วันที่เปิดโต๊ะ |  | datetime | ✓ |
| `open_time` | เวลาเปิดโต๊ะ |  | varchar(5) | ✓ |
| `trans_guid` | รายวันโต๊ะล่าสุด |  | varchar(50) | ✓ |
| `priority` | ลำดับความสำคัญ |  | smallint | ✓ |
| `last_member_code` | สมาชิกล่าสุด |  | varchar(25) | ✓ |
| `last_discount` | ส่วนลดล่าสุด |  | varchar(50) | ✓ |
| `last_service_charge` | Service Charge ล่าสุด |  | varchar(50) | ✓ |
| `table_qrcode` | QRCODE |  | varchar(50) | ✓ |
| `table_barcode` | Barcode |  | varchar(25) | ✓ |

index: `table_master_table_master_PRIMARY`(number), `table_master_barcode`(table_barcode), `table_master_idx1`(number,trans_guid)

## table_order

**รายการที่สั่ง** — Table 273

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `table_number` | เลขที่โต๊ะ |  | varchar(25) |  |
| `item_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `doc_no` | เลขที่ใบสั่ง |  | varchar(25) |  |
| `price` | ราคา |  | float | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `discount_word` | ส่วนลด |  | varchar(25) | ✓ |
| `discount_amount` | ส่วนลด |  | float | ✓ |
| `sum_amount` | ยอดรวม |  | float | ✓ |
| `guid_line` | guid |  | varchar(50) | ✓ |
| `last_status` | 0=ปรกติ,1=ยกเลิก,2=ปิดโต๊ะแล้ว |  | smallint | ✓ |
| `count_number` | ลำดับ *(resource only)* |  | char |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `qty_send` | เสิร์ฟ |  | smallint | ✓ |
| `order_type` | ประเภท |  | smallint | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `doc_date` | วันที่ |  | datetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `line_number` | Line |  | smallint | ✓ |
| `trans_guid` | trans_guid |  | varchar(50) | ✓ |
| `kitchen_code` | รหัสครัว |  | varchar(25) | ✓ |
| `qty_cancel` | ยกเลิก |  | float | ✓ |
| `qty_balance` | คงเหลือ |  | float | ✓ |
| `as_item_name` | ชื่อสินค้าพิเศษ |  | varchar(255) | ✓ |
| `confirm_guid` | confirm_guid |  | varchar(50) | ✓ |
| `confirm_status` | สถานะ |  | smallint | ✓ |
| `new_guid_line` | new_guid_line *(resource only)* |  | char |  |
| `isspeech` | พูดแล้ว |  | smallint | ✓ |
| `order_number_barcode` | Order Number Barcode |  | varchar(25) | ✓ |
| `old_qty` | จำนวนก่อนแก้ไข *(resource only)* |  | char |  |
| `old_price` | ราคาก่อนแก้ไข *(resource only)* |  | char |  |
| `old_doc_no` | เลขที่เอกสารเดิม |  | varchar(25) | ✓ |
| `topping_list` | เพิ่ม Topping |  | varchar(255) | ✓ |

index: `table_order_number`(table_number), `guid_line_idx`(guid_line), `table_order_idx1`(table_number,last_status), `table_order_item_code_unit`(item_code,unit_code), `table_order_doc_no`(doc_no)

## table_order_cancel

**รายละเอียดการยกเลิก คืนอาหาร** — table_order_cancel

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `table_number` | เลขที่โต๊ะ |  | varchar(25) |  |
| `guid_line` | อ้างอิง |  | varchar(50) |  |
| `qty` | จำนวนยกเลิก |  | float | ✓ |
| `remark` | หมายเหตุ |  | varchar(100) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `line_number` | line |  | smallint | ✓ |
| `price` | ราคา |  | float | ✓ |
| `sum_amount` | มูลค่า |  | float | ✓ |
| `qty_order` | จำนวนที่สั่ง *(resource only)* |  | char |  |
| `qty_balance` | จำนวนคงเหลือ *(resource only)* |  | char |  |
| `qty_cancel` | จำนวนยกเลิกแล้ว *(resource only)* |  | char |  |
| `cancel_guid` | guid การยกเลิก |  | varchar(50) | ✓ |
| `doc_date` | doc_date |  | datetime | ✓ |
| `doc_time` | doc_time |  | varchar(25) | ✓ |
| `sale_code` | รหัสพนักงาน |  | varchar(25) | ✓ |
| `sale_name` | ชื่อพนักงาน *(resource only)* |  | char |  |
| `cancel_flag` | ประเภทรายการ | 0=ยกเลิก,1=ย้ายโต๊ะ | smallint | ✓ |
| `table_number_2` | หมายเลขโต๊ะปลายทาง |  | varchar(50) | ✓ |

index: `table_number`(table_number), `item_code_unit_cancel_flag`(item_code,unit_code,cancel_flag)

## table_order_doc

**รายการเอียดใบสั่งอาหาร** — Table 274

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่ใบสั่ง |  | varchar(25) |  |
| `doc_date` | วันที่ |  | datetime |  |
| `doc_time` | เวลา |  | varchar(5) |  |
| `table_number` | เลขโต๊ะ |  | varchar(25) |  |
| `sale_code` | รหัสผู้สั่ง |  | varchar(25) | ✓ |
| `order_status` | สถานะ |  | smallint | ✓ |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `sum_amount` | รวมเงิน |  | float | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `trans_guid` | trans_guid |  | varchar(50) | ✓ |
| `last_status` | 0=ปรกติ,1=ยกเลิก,2=ปิดโต๊ะแล้ว |  | smallint | ✓ |
| `device_type` | 0=Windows,1=Android |  | smallint | ✓ |
| `order_number_barcode` | Order Number Barcode |  | varchar(25) | ✓ |
| `cashier_doc_no` | เลขที่ใบเสร็จ |  | varchar(25) | ✓ |
| `cashier_doc_date` | วันที่ใบเสร็จ |  | smalldatetime | ✓ |

index: `table_order_doc_table_order_doc_pk`(doc_no), `table_order_doc_idx1`(table_number), `table_order_doc_idx2`(table_number,last_status)

## table_order_log

**table_order_log** — table_order_log

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `date_time` | date_time |  | datetime |  |
| `command1` | command1 |  | varchar(255) |  |
| `message` | message |  | varchar(1000) |  |
| `sale_code` | sale_code |  | varchar(25) | ✓ |
| `qty` | qty |  | float | ✓ |

## table_trans

**รายวันโต๊ะ** — Table 279

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_guid` | เลขที่เอกสาร |  | varchar(50) |  |
| `open_doc_date` | วันที่เปิดโต๊ะ |  | datetime |  |
| `open_doc_time` | เวลาเปิดโต๊ะ |  | varchar(5) |  |
| `open_sale_code` | ผู้เปิดโต๊ะ |  | varchar(25) |  |
| `close_doc_date` | วันที่ปิดโต๊ะ |  | datetime | ✓ |
| `close_doc_time` | เวลาปิดโต๊ะ |  | varchar(5) | ✓ |
| `close_sale_code` | ผู้ปิดโต๊ะ |  | varchar(25) | ✓ |
| `cashier_doc_date` | วันที่รับเงิน |  | datetime | ✓ |
| `cashier_doc_time` | เวลารับเงิน |  | varchar(5) | ✓ |
| `cashier_sale_code` | ผู้รับเงิน |  | varchar(25) | ✓ |
| `cashier_doc_no` | เลขที่ใบเสร็จ |  | varchar(50) | ✓ |
| `table_number` | รหัสโต๊ะ |  | varchar(25) | ✓ |
| `table_number_2` | รหัสโต๊ะ |  | varchar(25) | ✓ |
| `cust_code` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `food_discount` | ส่วนลดอาหาร |  | varchar(25) | ✓ |
| `total_discount` | ส่วนลดทั้งบิล |  | varchar(25) | ✓ |
| `print_count` | จำนวนครั้งที่พิมพ์ |  | smallint | ✓ |
| `ispromotion_process` | ใช้การประมวลผล Promotion |  | smallint | ✓ |
| `service_charge` | Service Charge |  | varchar(25) | ✓ |
| `customer_count` | จำนวนลูกค้า |  | smallint | ✓ |
| `discount_group` | ส่วนลดตามกลุ่ม |  | varchar(500) | ✓ |

index: `table_trans_table_trans_pk`(trans_guid), `table_trans_idx1`(trans_guid,table_number)

## wallet_payments

**Wallet Payments** — Wallet Payments

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `wallet_code` | Wallet Code |  | varchar(25) |  |
| `qr_code` | QR Code |  | varchar(255) |  |
| `ref1` | Ref1 |  | varchar(50) |  |
| `ref2` | Ref2 |  | varchar(50) |  |
| `approve_status` | Approve Status |  | smallint | ✓ |
| `approve_code` | Approve Code |  | varchar(100) | ✓ |
| `approve_date` | Approve Date |  | datetime | ✓ |
| `create_date` | Create Date |  | datetime | ✓ |
| `user_code` | User Code |  | varchar(50) | ✓ |
| `computer_name` | Computer Name |  | varchar(50) | ✓ |
| `pos_id` | POS ID |  | varchar(50) | ✓ |
| `amount` | Amount |  | float | ✓ |
| `transection_id` | Transection ID |  | varchar(255) | ✓ |

