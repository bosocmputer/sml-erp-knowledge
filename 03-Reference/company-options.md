---
tags: [sml, reference, options, generated]
---
# ตัวเลือกบริษัทที่เปลี่ยนพฤติกรรมโปรแกรม (`_companyProfile`)

> สร้างอัตโนมัติด้วย `scripts/gen_options.py` — ค่าโหลดตอน login ด้วย `_g.g._companyProfileLoad()` (`SMLERPGlobal/_global.cs`) จาก `erp_company_profile`, `erp_option` และตารางตั้งค่าอื่น
> ความหมายจับคู่จากชื่อคอลัมน์ใน [[dictionary-index]] (อาจไม่ตรง 100% ถ้าชื่อซ้ำกับตารางอื่น) · กลับไป [[00-Index]]

**ผลต่อการวิเคราะห์ข้อมูล:** ร้านแต่ละร้านตั้งค่าไม่เหมือนกัน → พฤติกรรม (GL realtime, คำนวณต้นทุน, ยอดติดลบ, รันเลขเอกสาร ฯลฯ) ต่างกัน ควรอ่านค่าจาก DB ของร้านก่อนสรุป

ทั้งหมด 266 ตัวเลือก

| ตัวเลือก | ความหมาย | ตาราง | จุดที่ใช้ | โปรเจกต์หลัก |
|---|---|---|---|---|
| `item_amount_decimal` | จุดทศนิยม (มูลค่าสินค้า) | erp_option | 911 | SMLERPReportTool (234), SMLERPARReport (121), SMLERPAPReport (96) |
| `multi_currency` | ใช้ระบบหลายสกุลเงิน (Multi-Currency) | erp_option | 333 | SMLInventoryControl (155), SMLAPARControl (89), SMLERPGL (56) |
| `item_qty_decimal` | จุดทศนิยม (จำนวนสินค้า) | erp_option | 297 | SMLERPICReport (184), SMLERPReportTool (51), SMLERPCASHBANKReport (22) |
| `item_price_decimal` | จุดทศนิยม (ราคาสินค้า) | erp_option | 228 | SMLERPICReport (71), SMLERPReportTool (48), SMLInventoryControl (28) |
| `branch` | สาขา | erp_company_profile | 162 | SMLInventoryControl (83), SMLAPARControl (21), SMLERPGL (20) |
| `active` | ติดต่อ | ap_ar_resource | 132 | SMLDataCenterSync (92), SMLPosClient (10), SMLERPGlobal (9) |
| `change_branch_code` | อนุญาติให้เปลี่ยนสาขาได้ | erp_user | 125 | SMLInventoryControl (77), SMLAPARControl (20), SMLERPAP (15) |
| `disable_item_cost` | ไม่แสดงต้นทุนสินค้า | erp_option | 83 | SMLERPControl (45), SMLERPICInfo (25), SMLERPICReport (10) |
| `vat_rate` | อัตราภาษีมูลค่าเพิ่ม | erp_option | 77 | SMLPosClient (55), SMLInventoryControl (9), SMLAPARControl (6) |
| `mobillyst_tms_config` |  |  | 54 | SMLERPSO (36), SMLERPGlobal (14), SMLTransportLabel (4) |
| `use_barcode` | ใช้ระบบ Barcode | erp_option | 53 | SMLInventoryControl (43), SMLTransferDataPOS (7), SMLERPIC (2) |
| `discount_step_round_off` | ไม่ปัดเศษในการลดต่อเนื่อง | erp_option | 52 | SMLInventoryControl (20), SMLERPGL (13), SMLPosClient (11) |
| `inet_etax_access_token` |  |  | 50 | SMLETaxInvoice (34), SMLInventoryControl (7), SMLAPARControl (6) |
| `show_branch_doc_only` | แสดงเอกสารเฉพาะสาขา | erp_option | 47 | SMLInventoryControl (38), SMLAPARControl (6), SMLERPGlobal (1) |
| `inet_etax_uat_mode` |  |  | 46 | SMLETaxInvoice (34), SMLInventoryControl (6), SMLAPARControl (4) |
| `gl_no_decimal` | จุดทศนิยม (บัญชี) | erp_option | 44 | SMLERPGL (24), SINGHAReport (10), SMLAPARControl (6) |
| `use_department` | ใช้ระบบแยกแผนก | erp_option | 34 | SMLERPGL (17), SMLInventoryControl (10), SMLAPARControl (5) |
| `branch_code` | สาขาลำดับที่ | erp_company_profile | 33 | SMLERPGL (8), SMLERPControl (7), SMLERPGlobal (5) |
| `report` |  |  | 32 | SMLReport (26), SMLERPGlobal (6) |
| `home_currency` | สกุลเงินหลัก | erp_option | 30 | SMLERPARInfo (11), SMLInventoryControl (8), SMLAPARControl (6) |
| `report_webservice_url` | Report Web Service URL | erp_option | 29 | SMLERPGL (26), SMLFastReport (2), SMLERPGlobal (1) |
| `perm_wh_shelf` | ใช้คลังที่เก็บตามสิทธิพนักงาน | erp_option | 29 | SMLERPAP (12), SMLInventoryControl (7), SMLERPControl (4) |
| `column_price_enable` | เปิดช่องบันทึกราคาทั้งหมด | erp_option | 28 | SMLInventoryControl (19), SMLTransferDataPOS (7), SMLERPGlobal (1) |
| `hidden_cost_1` | ต้นทุนแฝงบริหาร | as_trans_detail | 28 | SMLInventoryControl (27), SMLERPGlobal (1) |
| `use_allocate` | ใช้ระบบการจัดสรรค์ | erp_option | 27 | SMLERPGL (17), SMLInventoryControl (6), SMLAPARControl (3) |
| `manual_total_enable` |  |  | 27 | SMLInventoryControl (25), SMLERPGlobal (1), SMLPPControl (1) |
| `use_unit` | ใช้ระบบแยกหน่วยงาน | erp_option | 25 | SMLERPGL (15), SMLInventoryControl (6), SMLAPARControl (3) |
| `use_project` | ใช้ระบบแยกโครงการ | erp_option | 25 | SMLERPGL (15), SMLInventoryControl (6), SMLAPARControl (3) |
| `use_job` | ใช้ระบบแยกงาน | erp_option | 23 | SMLERPGL (13), SMLInventoryControl (6), SMLAPARControl (3) |
| `discount_type` | ประเภทส่วนลด | ic_inventory_barcode_price | 23 | SMLERPGL (14), SMLPosClient (3), SMLInventoryControl (2) |
| `use_compare_unit` | ใช้ระบบหน่วยช่วยขาย | erp_option | 22 | SMLInventoryControl (21), SMLERPGlobal (1) |
| `gl_trans_type` | โอน GL | erp_option | 20 | SMLERPGL (19), SMLERPGlobal (1) |
| `use_expire` | ใช้ระบบวันหมดอายุ | erp_option | 20 | SMLInventoryControl (18), SMLERPGlobal (1), SMLPPControl (1) |
| `request_credit_type` | วิธีอนุมัติวงเงิน | erp_option | 20 | SMLInventoryControl (17), SMLERPControl (2), SMLERPGlobal (1) |
| `hidden_income_1` |  |  | 19 | SMLInventoryControl (8), SMLTransferDataPOS (8), SMLPPControl (2) |
| `promotion_fixed_unitcode` | โปรโมชั่นสินค้าเจาะจงหน่วยนับ | erp_option | 19 | SMLProcess (17), SMLERPGlobal (1), SMLPosClient (1) |
| `discount_vat_type` | การคำนวณภาษีกรณีมีส่วนลดท้ายรายการ | erp_option | 18 | SMLERPGL (11), SMLInventoryControl (2), SMLProcess (2) |
| `inet_etax_pdf_attacth` |  |  | 18 | SMLETaxInvoice (16), SMLERPGlobal (1), SMLPosClient (1) |
| `use_quality_control_system` | ใช้ระบบตรวจสอบคุณภาพสินค้า | erp_option | 18 | SMLInventoryControl (17), SMLERPGlobal (1) |
| `inet_etax_uat_email_to` |  |  | 17 | SMLETaxInvoice (16), SMLERPGlobal (1) |
| `sale_shift_id` | รหัสรอบการขาย | erp_option | 17 | SMLPosClient (9), SMLERPConfig (3), SMLERPControl (2) |
| `enable_all_ic_wh_shelf` | เปิดใช้ทุกคลังที่เก็บสินค้า | erp_option | 16 | SMLInventoryControl (6), SMLERPGlobal (4), SMLERPControl (2) |
| `ic_price_formula_control` | ห้ามขายสินค้าต่ำกว่าราคากลาง | erp_option | 16 | SMLInventoryControl (8), SMLPosClient (6), SMLERPGlobal (1) |
| `process_serial_device` | หมายเลขเครื่องประมวลผล | erp_option | 15 | SMLERPTemplate (10), SMLAccount (2), SMLPOS (2) |
| `warning_price_3` | ใช้ระบบรหัสผ่านแก้ไขราคา | erp_option | 13 | SMLPOSControl (7), SMLInventoryControl (5), SMLERPGlobal (1) |
| `gl_process_realtime` | ประมวลผล GL ทันทีหลังเพิ่มข้อมูล | erp_option | 12 | SMLAPARControl (6), SMLInventoryControl (5), SMLERPGlobal (1) |
| `sync_start_date` | วันที่เริ่มต้น sync | erp_option | 11 | SMLDataCenterSync (10), SMLERPGlobal (1) |
| `stock_reserved_control_location` | ใช้ระบบจองตามที่เก็บสินค้า | erp_option | 11 | SMLInventoryControl (10), SMLERPGlobal (1) |
| `calc_item_price_discount` | ใช้ระบบคำนวณราคาสินค้ากับส่วนลดก่อน | erp_option | 11 | SMLInventoryControl (7), SMLERPGlobal (1), SMLProcess (1) |
| `balance_control_type` | ประเภทห้ามสินค้าติดลบ | erp_option | 10 | SMLInventoryControl (9), SMLERPGlobal (1) |
| `save_user_order` | ใช้ระบบจำพนักงานสั่งอาหาร | erp_option | 10 | SMLPOSControl (7), SMLPOS (2), SMLERPGlobal (1) |
| `productlotbyyear` | ใช้ระบบ Lot กำหนดเองตามปี | erp_option | 10 | SMLERPControl (5), SMLERPIC (2), SMLERPICInfo (2) |
| `use_sale_shift` | ใช้ระบบรอบการขาย | erp_option | 10 | SMLERPConfig (5), SMLERPControl (3), SMLERPGlobal (1) |
| `use_point_center` | ใช้ระบบสะสมแต้มจากส่วนกลาง | erp_option | 9 | SMLDataCenterSync (4), SMLPosClient (3), SMLERPGlobal (1) |
| `customer_by_branch` | ใช้ระบบแสดงลูกค้าตามสาขา | erp_option | 9 | SMLERPControl (6), SMLInventoryControl (2), SMLERPGlobal (1) |
| `use_credit_pay_bill_calc` | ใช้ระบบคำนวณวันครบกำหนดชำระบิล | erp_option | 8 | SMLInventoryControl (4), SMLAPARControl (3), SMLERPGlobal (1) |
| `disable_auto_stock_process` | ปิดระบบคำณวนอัตโนมัติ | erp_option | 8 | SMLInventoryControl (3), SMLProcess (2), SMLAPARControl (1) |
| `wallet_lugent_store_id` | Store ID | erp_option | 8 | SMLAPARControl (7), SMLERPGlobal (1) |
| `wallet_lugent_terminal_id` | Terminal ID | erp_option | 8 | SMLAPARControl (7), SMLERPGlobal (1) |
| `wallet_lugent_merchant_name` | Merchant Nme | erp_option | 8 | SMLAPARControl (7), SMLERPGlobal (1) |
| `sr_ss_credit_check` | ตรวจสอบวงเงินรวมรายการสั่งขาย/สั่งจอง | erp_option | 8 | SMLInventoryControl (6), SMLERPARInfo (1), SMLERPGlobal (1) |
| `fix_item_set_price` | ใช้ระบบกำหนดราคาสินค้าชุด | erp_option | 8 | SMLInventoryControl (6), SMLERPGlobal (1), SMLPosClient (1) |
| `request_ar_credit` | ใช้ระบบขออนุมัติวงเงินเครดิต | erp_option | 8 | SMLInventoryControl (6), SMLERPGlobal (1), SMLAccount (1) |
| `wallet_lugent_access_code` | Access Code | erp_option | 7 | SMLAPARControl (6), SMLERPGlobal (1) |
| `wallet_lugent_biller_id` | Biller ID | erp_option | 7 | SMLAPARControl (6), SMLERPGlobal (1) |
| `sync_wbservice_url` |  |  | 7 | SMLInventoryControl (2), SMLProcess (2), SMLERPIC (2) |
| `ic_stock_control` | ห้ามขายสินค้าติดลบ | erp_option | 7 | SMLInventoryControl (6), SMLERPGlobal (1) |
| `deposit_format_from_pos` | ใช้ระบบ running เอกสารเงินมัดจำจาก POS | erp_option | 7 | SMLInventoryControl (3), SMLAPARControl (2), SMLERPGlobal (1) |
| `use_order_checker` | ใช้ระบบ Checker อาหาร | erp_option | 7 | SMLPOSControl (5), SMLERPGlobal (1), SMLPosClient (1) |
| `stock_accured_level` | ประเภทห้ามขายเกินค้างส่ง | erp_option | 7 | SMLInventoryControl (6), SMLERPGlobal (1) |
| `sml_kbank_qr_api_token` | Connection Token | erp_option | 6 | SMLAPARControl (4), SMLERPGlobal (1), SMLPosClient (1) |
| `sml_kbank_qr_api_uat_mode` | UAT Mode | erp_option | 6 | SMLAPARControl (4), SMLERPGlobal (1), SMLPosClient (1) |
| `warning_department` | เตือนไม่บันทึกแผนก | erp_option | 6 | SMLAPARControl (3), SMLInventoryControl (2), SMLERPGlobal (1) |
| `disabled_edit_doc_no_doc_date` |  |  | 6 | SMLAPARControl (2), SMLInventoryControl (2), SMLERPGlobal (1) |
| `disable_edit_doc_no_doc_date_user` | ห้ามแก้ไขวันที่และเลขที่เอกสาร | erp_user | 6 | SMLAPARControl (2), SMLInventoryControl (2), SMLERPGlobal (1) |
| `company_biller_id` | Biller ID | erp_thai_qr_config | 6 | SMLAPARControl (5), SMLERPGlobal (1) |
| `ref_1_format` | รูปแบบ Ref1 | erp_thai_qr_config | 6 | SMLAPARControl (2), SMLPosClient (2), SMLERPGlobal (1) |
| `ref_2_format` | รูปแบบ Ref2 | erp_thai_qr_config | 6 | SMLAPARControl (2), SMLPosClient (2), SMLERPGlobal (1) |
| `print_packing_pos_order` | ใช้ระบบพิมพ์ใบสั่งจัด | erp_option | 6 | SMLPosClient (4), SMLERPGlobal (1), SMLPOSControl (1) |
| `print_invoice_one_time` | พิมพ์ใบเสร็จครั้งเดียว | erp_option | 6 | SMLInventoryControl (5), SMLERPGlobal (1) |
| `enable_sml_kbank_api` | เปิดใช้งาน SML QR Kbank | erp_option | 5 | SMLAPARControl (3), SMLERPGlobal (1), SMLPosClient (1) |
| `gen_doc_no_auto` | สร้างเลขที่อัตโนมัติหลังบันทึกข้อมูล | erp_option | 5 | SMLAPARControl (2), SMLInventoryControl (2), SMLERPGlobal (1) |
| `wallet_bcel_contact` | Contact | erp_option | 5 | SMLAPARControl (4), SMLERPGlobal (1) |
| `promp_pay_wallet_id` | Promp-Pay Wallet ID | erp_thai_qr_config | 5 | SMLAPARControl (4), SMLERPGlobal (1) |
| `currency_exchange_decimal` | จุดทศนิยม (อัตราแลกเปลี่ยน) | erp_option | 5 | SMLERPGlobal (5) |
| `sync_product` | แลกเปลี่ยนรหัสสินค้า | erp_option | 5 | SMLInventoryControl (2), SMLERPIC (2), SMLERPGlobal (1) |
| `warning_low_cost` | เตือนเมื่อขายต่ำกว่าทุน | erp_option | 5 | SMLInventoryControl (4), SMLERPGlobal (1) |
| `sync_database_name` | ชื่อฐานข้อมูลแลกเปลี่ยนสินค้า | erp_option | 5 | SMLProcess (4), SMLERPGlobal (1) |
| `warning_discount_1` | ใช้ระบบรหัสผ่านแก้ไขส่วนลด | erp_option | 5 | SMLInventoryControl (4), SMLERPGlobal (1) |
| `orders_speech_format` | รูปแบบการพูด | erp_option | 5 | SMLPOS (2), SMLPOSControl (2), SMLERPGlobal (1) |
| `lock_change_customer` | ห้ามเปลี่ยนรหัสลูกค้า | erp_option | 5 | SMLInventoryControl (4), SMLERPGlobal (1) |
| `hide_pr_amount` | ปิดช่องราคาเสนอซื้อ | erp_option | 5 | SMLInventoryControl (4), SMLERPGlobal (1) |
| `withdraw_enable_amount` | เปิดช่องบันทึกมูลค่าเบิก | erp_option | 5 | SMLERPGlobal (5) |
| `use_notification_debt_product_receipt` | ใช้ระบบแจ้งเตือนการมัดจำหน้าตั้งหนี้จากการรับสินค้า | erp_option | 5 | SMLInventoryControl (2), SMLAPARControl (2), SMLERPGlobal (1) |
| `cn_coupon_only` | ใช้ระบบคูปองรับคืนสินค้า | erp_option | 4 | SMLInventoryControl (2), SMLAPARControl (1), SMLERPGlobal (1) |
| `warning_branch_input` | เตือนเมื่อไม่กำหนดสาขา | erp_option | 4 | SMLAPARControl (2), SMLERPGlobal (1), SMLInventoryControl (1) |
| `ar_credit_chq_outstanding` | วงเงินเครดิตรวมเช็คคงค้าง | erp_option | 4 | SMLERPARInfo (1), SMLERPGlobal (1), SMLERPControl (1) |
| `credit_sale_include_deposit` | วงเงินเครดิตรวมรายการมัดจำ | erp_option | 4 | SMLInventoryControl (2), SMLERPARInfo (1), SMLERPGlobal (1) |
| `voucher_form_code` | รหัสแบบฟอร์ม Voucher | erp_option | 4 | SMLERPGL (3), SMLERPGlobal (1) |
| `inventory_gl_post` | การ Post บัญชีสินค้า | erp_option | 4 | SMLERPGlobal (2), SMLInventoryControl (1), SMLERPIC (1) |
| `user_warehouse` |  |  | 4 | SMLFastReport (2), SMLERPGlobal (1), SMLDataTransfer (1) |
| `user_location` |  |  | 4 | SMLFastReport (2), SMLERPGlobal (1), SMLDataTransfer (1) |
| `branch_name` | ชื่อสาขา | sync_branch_list | 4 | SMLERPGlobal (2), SMLERPTemplate (2) |
| `wht_rate` | อัตราภาษีหัก ณ. ที่จ่าย | erp_option | 4 | SMLERPGLControl (3), SMLERPGlobal (1) |
| `accrued_control` | อนุญาติให้ขายสินค้าค้างส่ง | ic_inventory_detail | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `count_stock_sum` | ตรวจนับสินค้าแบบรวมจำนวน | erp_option | 4 | SMLInventoryControl (2), SMLERPGlobal (1), SMLERPICReport (1) |
| `auto_insert_time` | เปลี่ยนเวลาเมื่อเพิ่มข้อมูลรายวัน | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `barcode_picture` | แสดงรูปภาพสินค้าแยกตามบาร์โค๊ด | erp_option | 4 | SMLInventoryControl (2), SMLERPGlobal (1), SMLERPControl (1) |
| `issue_stock_control` | ห้ามเบิกสินค้าติดลบ | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `default_sale_type` | ประเภทการขาย(เริ่มต้น) | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `sale_order_banalce_control` | ไม่ตรวจสอบยอดคงเหลือในระบบสั่งขาย | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `check_lot_auto` | ตรวจสอบ LOT อัตโนมัติ | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `digital_barcode_scale` | ใช้ระบบอ่านบาร์โค๊ดจากเครื่องชั่ง | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `warning_reorder_point` | เตือนสินค้าถึงจุดสั่งซื้อ | erp_option | 4 | SMLERPGlobal (1), SMLAccount (1), SMLERPTemplate (1) |
| `phone_number_approve` | หมายเลขโทรศัทพ์ขออนุมัติวงเงิน | erp_option | 4 | SMLInventoryControl (2), SMLERPGlobal (1), SMLERPControl (1) |
| `ref_po_approve` | อ้างอิงเอกสารสั่งซื้อที่อนุมัติแล้วเท่านั้น | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `sml_eorder_api_key` | SML E-Order API Key | erp_option | 4 | SMLERPTemplate (3), SMLERPGlobal (1) |
| `check_status_sr_print` | ตรวจสอบสถานะการพิมพ์ใบสั่งจอง | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `use_price_center` | ใช้ระบบราคาจากส่วนกลาง | erp_option | 4 | SMLInventoryControl (2), SMLERPGlobal (1), SMLPosClient (1) |
| `pr_disable_price` | เสนอซื้อห้ามกำหนดราคา | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `show_serial_tire` | แสดงระบบ Serial ยางรถยนต์ | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `receive_more_po` | อนุญาติให้รับสินค้ามากกว่าใบสั่งซื้อได้ | erp_option | 4 | SMLProcess (2), SMLERPGlobal (1), SMLInventoryControl (1) |
| `approve_order_so_befor_print` | อนุมัติใบสั่งซื้อก่อนพิมพ์ | erp_option | 4 | SMLInventoryControl (3), SMLERPGlobal (1) |
| `user_barcode_clearance` | เปิดใช้งาน barcode ลดราคา | erp_option | 4 | SMLPosClient (2), SMLERPGlobal (1), SMLInventoryControl (1) |
| `home_currency_name` |  |  | 4 | SMLERPGlobal (2), SMLERPGL (2) |
| `search_cheque_other_cust_code` | ค้นหาเช็คฉบับเก่าไม่ตรวจสอบลูกหนี้/เจ้าหนี้ | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `input_credit_card_charge` | เปิดช่องบันทึกยอดชาร์จบัตรเครดิต | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `running_doc_no_only` | เลขที่เอกสารให้เลือกจากประเภทเอกสารเท่านั้น | erp_option | 3 | SMLAPARControl (1), SMLERPGlobal (1), SMLInventoryControl (1) |
| `sale_order_edit` |  |  | 3 | SMLAPARControl (1), SMLERPGlobal (1), SMLInventoryControl (1) |
| `close_ar_status_auto` | ปิดสถานะเครดิตลูกหนี้อัตโนมัติ | erp_option | 3 | SMLAPARControl (1), SMLERPGlobal (1), SMLAccount (1) |
| `open_cash_drawer_after_sale` | เปิดลิ้นชักเก็บเงินหลังทำการขาย | erp_option | 3 | SMLAPARControl (1), SMLERPGlobal (1), SMLInventoryControl (1) |
| `wallet_notification_server_url` | Payment Notificaton Service URL | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `wallet_bcel_mcid` | MCID | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `wallet_bcel_mcc` | MCC | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `sml_kbank_qr_credit` | KBank QR Code Credit Card | erp_option | 3 | SMLAPARControl (1), SMLERPGlobal (1), SMLPosClient (1) |
| `wallet_bcel_merchant_name` | Merchant Name | erp_option | 3 | SMLAPARControl (2), SMLERPGlobal (1) |
| `prompt_pay_book_code` | สมุดดงินฝาก prompt pay | erp_thai_qr_config | 3 | SMLERPGlobal (2), SMLPosClient (1) |
| `purchase` |  |  | 3 | SMLERPGlobal (3) |
| `printer` |  |  | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `use_doc_group` | ใช้กลุ่มเอกสาร | erp_option | 3 | SMLERPGlobal (1), SMLInventoryControl (1), SMLAPARControl (1) |
| `balance_control` | ห้ามขายสินค้าติดลบ | POSConfig | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `cost_by_warehouse` |  |  | 3 | SMLERPICInfo (2), SMLERPGlobal (1) |
| `transfer_stock_control` | ห้ามโอนสินค้าติดลบ | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `doc_sale_tax_number_fixed` | ใบกับกับภาษีขายให้ตรงกับเลขที่เอกสาร | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `use_serial_no_duplicate` | อนุญาติให้บันทึก Serial No ซ้ำ | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `lock_low_cost` | ห้ามขายสินค้าต่ำกว่าทุน | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `add_item_color` | เพิ่มสูตรสี | erp_option | 3 | SMLERPIC (2), SMLERPGlobal (1) |
| `sync_provider_code` | รหัสผู้ให้บริการแลกเปลี่ยนสินค้า | erp_option | 3 | SMLProcess (2), SMLERPGlobal (1) |
| `lock_credit_money` | ห้ามขายเกินวงเงินเครดิต | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `find_lot_auto` | ใช้ระบบค้นหา LOT อัตโนมัติ | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `disable_edit_order` | ห้ามแก้ไขรายการอาหาร | erp_option | 3 | SMLPOSControl (2), SMLERPGlobal (1) |
| `print_pos_settle_bill_detail` | พิมพ์สรุปยอดใบส่งเงิน | erp_option | 3 | SMLPosClient (2), SMLERPGlobal (1) |
| `sum_point_all` | เข้าระบบสะสมแต้มทุกรายการ | erp_option | 3 | SMLERPGlobal (1), SMLProcess (1), SMLPosClient (1) |
| `internet` |  |  | 3 | SMLERPGlobal (1), SMLInventoryControl (1), SMLERPTemplate (1) |
| `join_money_credit_list` | ชื่อฐานข้อมูลวงเงิน | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `stock_reserved_control` | ห้ามขายสินค้าค้างจองทั้งระบบ | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `calc_point_from_pay` | คำนวณแต้มจากยอดชำระ | erp_option | 3 | SMLERPGlobal (1), SMLProcess (1), SMLPosClient (1) |
| `orders_speech` | พูดรายการอาหาร | erp_option | 3 | SMLERPGlobal (1), SMLPOS (1), SMLPOSControl (1) |
| `order_table_url` | Table URL | erp_option | 3 | SMLPOSControl (2), SMLERPGlobal (1) |
| `warning_product_expire` | เตือนสินค้าหมดอายุ | erp_option | 3 | SMLERPGlobal (1), SMLAccount (1), SMLPOS (1) |
| `sale_hub_approve` | ผู้อนุมัติ Sale Hub | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `hidden_price_formula` | ไม่แสดงตารางราคาตามสูตร | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `quotation_expire` | ใช้ระบบหมดอายุใบเสนอราคา | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `close_warning_backup` | ปิดเตือนสำรองข้อมูล | erp_option | 3 | SMLERPGlobal (1), SMLAccount (1), SMLPOS (1) |
| `ss_ref_po_only` | ใบสั่งขายอ้างอิงเสนอราคาเท่านั้น | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `use_sml_eorder` | ใช้ระบบ SML E-Order | erp_option | 3 | SMLERPTemplate (2), SMLERPGlobal (1) |
| `mobile_sale_url` | Mobile Sale Server URL | erp_option | 3 | SINGHAReport (2), SMLERPGlobal (1) |
| `check_delivery_date` | ใส่วัน รับ/ส่ง สินค้าทุกครั้ง | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `check_overdue` | ห้ามขายเมื่อเกินกำหนดชำระ | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `check_qty_over_doc_ref` | ห้ามใส่จำนวนเกินเอกสารอ้างอิง | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `wallet_book_code` | สมุดเงินฝาก wallet | erp_option | 3 | SMLPosClient (2), SMLERPGlobal (1) |
| `dohome_dealer_code` | Dohome Dealer Code | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `dohome_username` | Username | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `dohome_password` | Password | erp_option | 3 | SMLInventoryControl (2), SMLERPGlobal (1) |
| `tiger_app_id` | tiger app id | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `tiger_x_api_key` | tiger x api key | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `tiger_end_point` | tiger end point | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `pay_bill_over` | อนุญาติให้ชำระเกินยอดบิลได้ | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `ar_bill_inform` | ห้ามวางบิลขายซ้ำ | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `ap_bill_inform` | ห้ามรับวางบิลซ้ำ | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `ap_pay_from_bill_note` | จ่ายชำระหนี้อ้างอิงวางบิลทุกครั้ง | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `ar_pay_from_bill_note` | รับชำระหนี้อ้างอิงวางบิลทุกครั้ง | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `filter_pay_bill` | ไม่แสดงเอกสารที่วางบิลไปแล้ว | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `merchant_name` | Merchant Name | erp_qr_payment | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `company_terminal_id` | Terminal ID | erp_thai_qr_config | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `company_store_id` | Store ID | erp_thai_qr_config | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `wallet_lugent_domain` | DomainName | erp_option | 2 | SMLAPARControl (1), SMLERPGlobal (1) |
| `sale_real_price` | ดึงราคาขายแบบคำนวณส่วนลดทันที | erp_option | 2 | SMLERPGlobal (2) |
| `company_name_eng` |  |  | 2 | SMLERPGlobal (1), SMLPosClient (1) |
| `company_address_eng` |  |  | 2 | SMLERPGlobal (1), SMLPosClient (1) |
| `year_type` | ประเภทปี | erp_option | 2 | SMLERPGlobal (2) |
| `vat_type` | ประเภทภาษีมูลค่าเพิ่ม (ขาย) | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `vat_type_1` | ประเภทภาษีมูลค่าเพิ่ม (ซื้อ) | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_price_1` | เตือนเมื่อไม่พบราคาขาย | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_price_2` | เตือนราคาขายกับประเภทภาษี | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `pr_approve_lock` | ใบอนุมัติซื้ออ้างอิงได้ครั้งเดียว | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `count_stock_display_saleprice` | แสดงราคาขายในระบบตรวจนับ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_credit_money` | เตือนเกินวงเงินเครดิต | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `get_last_price_type` | ระบบเรียกราคาขายล่าสุด | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `auto_run_docno_sale` | กำหนดเลขที่เอกสารขายใหม่เมื่อเลขที่ซ้ำ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `disable_ic_cost_process` | ปิดระบบคำนวณต้นทุนสินค้า | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `save_logs` | ใช้ระบบเก็บประวัติการใชังาน | erp_option | 2 | SMLERPGlobal (2) |
| `use_reference_pr` | เปิดระบบอ้างอิงจากใบเสนอซื้อ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `get_purchase_price` | ใช้ระบบดึงราคาซื้อ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `password_ar_credit` | ใช้ระบบรหัสผ่านอนุมัติวงเงินเครดิต | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `manual_customer_code` | ใช้ระบบตั้งรหัสลูกค้า | erp_option | 2 | SMLERPGlobal (1), SMLERPControl (1) |
| `count_customer_table` | จัดเก็บจำนวนลูกค้า | erp_option | 2 | SMLERPGlobal (1), SMLPOSControl (1) |
| `auto_open_table` | เปิดโต๊ะอัตโนมัติหลังจากคิดเงิน | erp_option | 2 | SMLERPGlobal (1), SMLPosClient (1) |
| `check_input_vat` | ป้อนเลขที่ใบกำกับภาษีทุกครั้ง | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `order_after_open_table` | สั่งอาหารหลังเปิดโต๊ะทันที | erp_option | 2 | SMLERPGlobal (1), SMLPOSControl (1) |
| `join_money_credit` | เชื่อมวงเงินเครดิต | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `real_doc_date_doc_time` | กำหนดเวลาเอกสารอัตโนมัติ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_bill_overdue` | เตือนลูกหนี้เกินชำระ | erp_option | 2 | SMLERPGlobal (1), SMLAccount (1) |
| `disable_sync_time` | ปิดระบบตรวจสอบเวลาเครื่อง | erp_option | 2 | SMLERPGlobal (1), SMLERPTemplate (1) |
| `check_ar_duplicate_name` | ตรวจสอบชื่อลูกหนี้ซ้ำ | erp_option | 2 | SMLERPGlobal (1), SMLERPControl (1) |
| `tax_from_invoice` | ใบกำกับภาษีขายตรงกับเอกสารขาย | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `show_menu_by_permission` | ใช้ระบบแสดงเมนูตามสิทธิ์การใช้งาน | erp_option | 2 | SMLERPGlobal (1), SMLAccount (1) |
| `ref_pr_approve` | อ้างอิงเอกสารเสนอซื้อที่อนุมัติแล้วเท่านั้น | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_input_customer` | เตือนเลือกลูกค้าก่อนทำรายการ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `inv_disable_quotation` | จอขายปิดอ้างอิงใบเสนอราคา | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `check_refer_wh_shelf` | ห้ามแก้ไขคลังที่เก็บกรณีอ้างอิงเอกสาร | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `price_list_server` | URL Server | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `purchase_zero_vat_use_price1` | ใช้ราคาแยกภาษีกรณีซื้อสินค้าภาษีศูนย์ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `pr_wh_shelf` | เสนอซื้อสินค้าแสดงช่องคลัง/ที่เก็บ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `send_area_check` | ตรวจสอบการป้อนเขตขนส่งกรณีส่งให้ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `mobile_bypasskey` | Mobile Sale Key | erp_option | 2 | SMLERPGlobal (1), SINGHAReport (1) |
| `show_serial_car` | แสดงระบบ Serial รถยนต์ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `select_branch_first` | ใช้ระบบเลือกสาขาก่อนเข้าโปรแกรม | erp_option | 2 | SMLERPGlobal (1), SMLAccount (1) |
| `change_price_formula` | เปิดเลือกราคาขายตามสูตร | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `check_expiration_date` | ใส่วันหมดอายุทุกครั้ง | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `warning_overdue` | เตือนเมื่อเกินกำหนดชำระ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `check_overdue_order` | ตรวจสอบเกินกำหนดชำระ(สั่งจอง) | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `check_overdue_sell` | ตรวจสอบเกินกำหนดชำระ(สั่งขาย) | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `allow_sale_over_reserve` | ปิดการตรวจสอบขายเกินกว่าจอง | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `check_credit_sale_reserve_sale_order` | สั่งจอง สั่งขาย เงินเชื่อตรวจสอบวงเงินลูกค้า | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `stock_issue_show_cost` | เบิกสินค้าแสดงช่องต้นทุน | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `skip_cn_over_due` | ไม่ตรวจสอบวันครบกำหนด ใบลดหนี้ (ขาย) | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `display_lot_column` | แสดงคอลัมน์ Lot Number | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `sale_auto_input_qty` | ป้อนจำนวนขายเริ่มต้นอันโนมัติ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `fill_sale_deposit` | ดึงรายการมัดจำคงค้าง | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `doc_ref_salesorder_approve` | เปิดใช้ระบบอ้างอิงใบสั่งขายที่อนุมัติแล้วเท่านั้น | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `doc_ref_reservation_approve` | เปิดใช้ระบบอ้างอิงใบสั่งจองที่อนุมัติแล้วเท่านั้น | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `no_coppy` | ห้ามคัดลอกเอกสาร | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `lock_edit_product_name_in_detail` | ห้ามแก้ไขชื่อสินค้าในรายการ | erp_option | 2 | SMLERPGlobal (2) |
| `hide_price_item_set` | ไม่แสดงราคาสินค้าชุด | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `cn_pos_over_day` | ระยะเวลาในการรับคืนสินค้า(วัน) | erp_option | 2 | SMLERPGlobal (1), SMLPosClient (1) |
| `check_qty` | ใส่จำนวนสินค้าทุกครั้ง | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `disable_capture_screen` | ปิดการใช้งาน capture screen | erp_option | 2 | SMLERPGlobal (1), SMLERPTemplate (1) |
| `disable_ar_autorun` | ปิดระบบรันลูกหนี้อัตโนมัติ | erp_option | 2 | SMLERPGlobal (1), SMLERPControl (1) |
| `show_item_remark` | เปิดช่องหมายเหตุ | erp_option | 2 | SMLERPGlobal (1), SMLInventoryControl (1) |
| `coupon_full_amount` | ใช้คูปองเต็มมูลค่าเท่านั้น | erp_option | 1 | SMLAPARControl (1) |
| `promp_pay_telephone_number` | Promp-Pay Telephone Number | erp_thai_qr_config | 1 | SMLERPGlobal (1) |
| `use_log_book` | ใช้ระบบตรวจสอบการใช้งาน | erp_option | 1 | SMLERPGlobal (1) |
| `use_print_slip` | พิมพ์เอกสารหลังการบันทึกข้อมูล | erp_option | 1 | SMLERPGlobal (1) |
| `use_work_in_process` | ใช้ระบบแยกการผลิต | erp_option | 1 | SMLERPGlobal (1) |
| `purchase_credit_note_type` | ส่งคืน,ลดหนี้ใช้แบบอ้างอิงเอกสารใบเดียว | erp_option | 1 | SMLERPGlobal (1) |
| `sale_auto_packing` | เปลี่ยนหน่วยนับอัตโนมัติ (จอขาย) | erp_option | 1 | SMLERPGlobal (1) |
| `check_ar_status_credit` | ตรวจสอบสถานะเครดิตลูกหนี้ | erp_option | 1 | SMLERPGlobal (1) |
| `price_list_serial_process` | หมายเลขเครื่อง Process | erp_option | 1 | SMLERPGlobal (1) |
| `price_list_branch` | รหัสสาขา | erp_option | 1 | SMLERPGlobal (1) |
| `price_list_key` | รหัสเข้าสู่ระบบ | erp_option | 1 | SMLERPGlobal (1) |
| `cn_request_doc_ref` | ลดหนี้ต้องอ้างอิงเอกสารทุกครั้ง | erp_option | 1 | SMLERPGlobal (1) |
| `print_table_move` | พิมพ์รายการย้ายโต๊ะ | erp_option | 1 | SMLERPGlobal (1) |
| `show_stock_balance_wh` | แสดงยอดคงเหลือทุกคลังที่เก็บและเลือกที่เก็บตามสิทธ์ | erp_option | 1 | SMLERPGlobal (1) |
| `show_stock_available` | แสดงจำนวนสินค้าพร้อมขาย ใบสั่งขาย | erp_option | 1 | SMLERPGlobal (1) |
| `e_tax_company_id` |  |  | 1 | SMLETaxInvoice (1) |
