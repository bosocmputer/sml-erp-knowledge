---
tags: [sml, module, setup, generated]
menu_group: "เริ่มต้น"
trans_flags: []
---
# โมดูล: เริ่มต้น

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายละเอียดเชิงลึก: สิทธิ์ผู้ใช้ [[permissions]], งวดบัญชี/ล็อกวันที่ [[tax-period]]
- ตั้งค่าบริษัท สาขา แผนก พนักงาน กลุ่มเอกสาร รูปแบบเลขที่เอกสาร และข้อมูลหลักต่าง ๆ
- หน้าจอข้อมูลหลักส่วนใหญ่ใช้ `MyLib._manageMasterCodeFull` ผูก 1 เมนู = 1 ตาราง (ดูคอลัมน์ตารางด้านล่าง)

## ตัวเลข

- เมนูปลายทาง 135 รายการ, จับคู่คลาสได้ 129, เห็นใน SMLAccountPOSProfessional (edition 12) 125
- คลาสหน้าจอที่ใช้บ่อย: `MyLib._manageMasterCodeFull` (73), `SMLFastReport._designer` (2), `_g._changeCode._changeApArCodeUserControl` (2), `SMLFastReport._importFastReport` (2), `SMLERPConfig._companyProfile` (1), `SMLERPConfig._option` (1)
- control หลักที่ฝัง: `SMLERPControl._getPicture` (1), `SMLPOSControl._posScreenConfig` (1), `SMLPOSControl._screenConfig` (1)

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_shelf`, `ic_warehouse`, `ic_inventory`, `erp_user`, `sml_fastreport`, `erp_province`, `ar_customer`, `logs`, `ar_sale_area`, `erp_doc_format`, `erp_amper`, `erp_tambon`, `ic_group`, `ic_group_sub`, `erp_income_list`, `cb_trans_detail`, `ic_inventory_price`, `ic_trans`, `ar_customer_detail`, `ap_supplier_detail`, `erp_option`, `erp_branch_list`, `erp_department_list`, `ar_paybill_area`, `erp_user_group`, `gl_journal_book`, `erp_currency`, `erp_bank_branch`, `POSConfig`, `POS_ID`, `sml_posdesign`, `ic_group_sub2`, `ic_dimension_name`, `ic_dimension`, `ap_group`, `ap_group_sub`, `ar_group`, `ar_group_sub`, `erp_bank`, `erp_expenses_list`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดบริษัท | `menu_company_profile` | ✓ | `SMLERPConfig._companyProfile` |  | erp_company_profile |
| รายละเอียดข้อมูลทั่วไป › กำหนดข้อเลือกพิเศษต่างๆ | `menu_option` | ✓ | `SMLERPConfig._option` |  | erp_thai_qr_config, erp_option_etax_inet, erp_option_mobillyst, erp_option |
| รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดสาขา | `menu_setup_branch` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_branch_list |
| รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดแผนก | `menu_setup_department_list` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_department_list |
| รายละเอียดข้อมูลทั่วไป › กำหนดพนักงาน | `menu_setup_staff` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_paybill_area, ar_sale_area, erp_branch_list, erp_user |
| รายละเอียดข้อมูลทั่วไป › กำหนดกลุ่มพนักงาน | `menu_setup_user_group` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_user_group |
| รายละเอียดข้อมูลทั่วไป › กำหนดการใช้คลังและที่เก็บ | `menu_setup_user_group_warehouse_shelf` |  | `_g._userGroupWarehouseShelf` |  | erp_user_group_wh_shelf, ic_shelf, ic_warehouse, erp_user_group |
| รายละเอียดข้อมูลทั่วไป › กำหนดรูปภาพพนักงาน | `menu_setup_staff_pic` | ✓ | `SMLERPControl.erp_user._erp_userDetailpicture` |  | erp_user, images_erp_user |
| รายละเอียดข้อมูลทั่วไป › รายงานพนักงานเรียงตามกลุ่ม | `menu_report_employee_group` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายละเอียดข้อมูลทั่วไป › กำหนดผู้ใช้ระบบ MIS | `menu_setup_staff_mis` | ✓ | `MyLib._manageMasterCodeFull` |  | mis_user |
| รายละเอียดข้อมูลทั่วไป › กำหนดกลุ่มเอกสาร | `menu_setup_doc_group` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_doc_group |
| รายละเอียดข้อมูลทั่วไป › กำหนดรูปแบบเลขที่เอกสาร | `menu_setup_doc_format` | ✓ | `_g._docFormat` |  | erp_doc_format_etax, erp_doc_format, erp_doc_format_gl, gl_journal_book |
| รายละเอียดข้อมูลทั่วไป › กำหนดประเภทการขนส่ง | `menu_setup_transport` | ✓ | `MyLib._manageMasterCodeFull` |  | transport_type |
| รายละเอียดข้อมูลทั่วไป › กำหนดเขตการขนส่ง | `menu_setup_ar_logistic_area` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_logistic_area |
| รายละเอียดข้อมูลทั่วไป › กำหนดสกุลเงิน | `menu_setup_currency` |  | `MyLib._manageMasterCodeFull` |  | erp_currency |
| รายละเอียดข้อมูลทั่วไป › กำหนดค่าเครื่องรูดบัตรเครดิต | `menu_edc_config` | ✓ | `SMLERPConfig._edcConfigForm` |  |  |
| รายละเอียดข้อมูลทั่วไป › กำหนดค่าจอแสดงผล QR Code | `menu_usb_qr_display_config` | ✓ | `SMLERPConfig._usbQRDisplayConfigForm` |  | erp_option |
| รายละเอียดข้อมูลทั่วไป › กำหนดค่า QR Code Payment | `menu_setup_qr_payment` | ✓ | `SMLERPConfig.qrpayment._config_qr_payment_control` |  | erp_amper, erp_bank_branch, erp_tambon |
| รายละเอียดข้อมูลทั่วไป › ดึงรายชื่อจังหวัดอัตโนมัติ | `menu_setup_province_auto` | ✓ | `SMLERPConfig._provinceLoadFromWebControl` |  | erp_province, erp_amper, erp_tambon |
| รายละเอียดข้อมูลทั่วไป › กำหนดรหัสจังหวัด | `menu_setup_province` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_province |
| รายละเอียดข้อมูลทั่วไป › กำหนดรหัสอำเภอ | `menu_setup_ampher` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_amper, erp_province |
| รายละเอียดข้อมูลทั่วไป › กำหนดรหัสตำบล | `menu_setup_tambon` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_province, erp_tambon |
| รายละเอียดข้อมูลทั่วไป › กำหนดค่าเริ่มต้น POS | `menu_config_pos_startup` | ✓ | `SMLPOSControl._posConfig` |  | POSConfig, erp_currency, ar_customer |
| รายละเอียดข้อมูลทั่วไป › กำหนดรหัสเครื่อง POS | `menu_config_pos_machine` | ✓ | `SMLPOSControl._posMachine` |  | erp_department_list, ic_warehouse, ic_shelf, erp_doc_format |
| รายละเอียดข้อมูลทั่วไป › กำหนดเงื่อนไขสะสมแต้ม | `menu_pos_point_rate` | ✓ | `SMLPOSControl._posPointPeriodForm` |  | pos_point_period, pos_point_condition, pos_point_special_day |
| รายละเอียดข้อมูลทั่วไป › กำหนดคุณสมบัติของเครื่อง POS | `menu_config_pos_screen` | ✓ | `SMLPosClient._configPOSScreen` |  | POSConfig, POS_ID, sml_posdesign |
| ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าหลัก | `menu_setup_ic_group_main` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_group |
| ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าย่อย | `menu_setup_ic_group_sub` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_group, ic_group_sub |
| ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าย่อย2 | `menu_setup_ic_group_sub2` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_group, ic_group_sub, ic_group_sub2 |
| ระบบสินค้าคงคลัง › กำหนดยี่ห้อสินค้า | `menu_setup_ic_brand` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_brand |
| ระบบสินค้าคงคลัง › กำหนดรุ่นสินค้า | `menu_setup_ic_model` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_model |
| ระบบสินค้าคงคลัง › กำหนดสีสินค้า | `menu_setup_ic_color` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_color |
| ระบบสินค้าคงคลัง › กำหนดขนาดสินค้า | `menu_setup_ic_size` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_size |
| ระบบสินค้าคงคลัง › กำหนดรูปแบบสินค้า | `menu_setup_ic_pattern` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_pattern |
| ระบบสินค้าคงคลัง › กำหนดเกรดสินค้า | `menu_setup_ic_grade` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_grade |
| ระบบสินค้าคงคลัง › กำหนดหมวดสินค้า | `menu_setup_ic_category` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_category |
| ระบบสินค้าคงคลัง › กำหนดรูปทรงสินค้า | `menu_setup_ic_design` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_design |
| ระบบสินค้าคงคลัง › กำหนดชื่อมิติสินค้า | `menu_setup_ic_dimension_name` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_dimension_name |
| ระบบสินค้าคงคลัง › กำหนดมิติสินค้า | `menu_setup_ic_dimension` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_dimension, ic_dimension_name |
| ระบบสินค้าคงคลัง › ประเภทรายได้ | `menu_income_list` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_income_list |
| ระบบสินค้าคงคลัง › กำหนดระดับสินค้า | `menu_setup_ic_class` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_class |
| ระบบสินค้าคงคลัง › กำหนดหน่วยนับสินค้า | `menu_setup_ic_unit` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_unit |
| ระบบสินค้าคงคลัง › กำหนดคลังสินค้า | `menu_setup_ic_wh` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_warehouse |
| ระบบสินค้าคงคลัง › กำหนดพื้นที่เก็บสินค้า | `menu_setup_ic_shelf` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_shelf, ic_warehouse |
| ระบบสินค้าคงคลัง › กำหนดกลุ่มบัญชีสินค้า | `menu_setup_ic_account_group` | ✓ | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ระบบสินค้าคงคลัง › กำหนดพิกัดศุลกากร | `menu_setup_ic_import_duty_point` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_import_duty |
| ระบบสินค้าคงคลัง › กำหนดประเภทการเบิก | `menu_setup_ic_issue_type` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_issue_type |
| ระบบสินค้าคงคลัง › กำหนดสาเหตุการปรับปรุง | `menu_setup_stk_adjust` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_stk_adjust_reason |
| ระบบสินค้าคงคลัง › กำหนดเหตุผลการปิดสินค้า | `menu_setup_ic_close_reason` | ✓ | `MyLib._manageMasterCodeFull` |  | ic_close_reason |
| ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ | `ic_auto_add_warehouse_and_location` | ✓ | `_g._ic_add_warehouse_shelf_form` |  | ic_inventory, ic_wh_shelf, ic_shelf |
| ระบบสินค้าคงคลัง › กำหนดผู้ผลิต | `menu_manufacturer_list` | ✓ | `MyLib._manageMasterCodeFull` |  | manufacturer_list |
| ระบบขาย › กำหนดรายได้อื่นๆ | `menu_setup_other_income` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ระบบขาย › กำหนดเขตการขาย | `menu_setup_ar_sale_area` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_sale_area |
| ระบบขาย › ออกแบบหน้าจอขาย POS | `client_design` | ✓ | `SMLPOSControl._designer._clientDesign` |  | sml_posdesign |
| ระบบขาย › Download ระบบเสียงพูด | `menu_pos_sound_download_install` | ✓ | `SMLPOSControl._posDownloadSound` |  |  |
| ระบบขาย › กำหนดแผนการขาย | `menu_sale_plan` |  | `SMLERPConfig._salePlanManage` |  | erp_sale_plan_detail, erp_sale_plan, ar_sale_area, erp_user |
| ระบบขาย › กำหนดเขตเก็บเงิน | `menu_ar_setup_paybill_area` |  | `MyLib._manageMasterCodeFull` |  | ar_paybill_area |
| ระบบขาย › กำหนดกลุ่มอนุมัติวงเงิน | `menu_approve_credit_level` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_credit_approve_level |
| ระบบเจ้าหนี้ › กำหนดประเภทเจ้าหนี้ | `menu_setup_ap_type` | ✓ | `MyLib._manageMasterCodeFull` |  | ap_type |
| ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้หลัก | `menu_setup_ap_group_main` | ✓ | `MyLib._manageMasterCodeFull` |  | ap_group |
| ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้ย่อย | `menu_setup_ap_group_sub` | ✓ | `MyLib._manageMasterCodeFull` |  | ap_group, ap_group_sub |
| ระบบเจ้าหนี้ › กำหนดมิติเจ้าหนี้ | `menu_setup_ap_dimension` | ✓ | `MyLib._manageMasterCodeFull` |  | ap_dimension |
| ระบบลูกหนี้ › กำหนดประเภทลูกหนี้ | `menu_setup_ar_type` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_type |
| ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้หลัก | `menu_setup_ar_group_main` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_group |
| ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้ย่อย | `menu_setup_ar_group_sub` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_group, ar_group_sub |
| ระบบลูกหนี้ › กำหนดมิติลูกหนี้ | `menu_setup_ar_dimension` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_dimension |
| ระบบลูกหนี้ › กำหนดเหตุผลอนุมัติวงเงิน | `menu_setup_ar_credit_approve` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_credit_approve |
| ระบบลูกหนี้ › กำหนดเงื่อนไขการวางบิล | `menu_setup_ar_pay_bill_reason` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_pay_bill_condition |
| ระบบลูกหนี้ › กำหนดเงื่อนไขการรับเช็ค | `menu_setup_ar_keep_chq_reason` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_keep_chq_condition |
| ระบบลูกหนี้ › กำหนดเงือนไขการชำระเงิน | `menu_setup_ar_keep_money` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_keep_money_condition |
| ระบบลูกหนี้ › กำหนดวันครบกำหนดชำระเงิน | `menu_ar_credit_pay_bill` | ✓ | `SMLERPControl.ARCreditPayBillForm` |  | ar_credit_pay_bill |
| ระบบลูกหนี้ › กำหนดกลุ่มผู้ติดต่อ | `menu_ar_contact_group` | ✓ | `MyLib._manageMasterCodeFull` |  | ar_contact_group |
| ระบบเงินสด-ธนาคาร › กำหนดธนาคาร | `menu_setup_bank` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_bank |
| ระบบเงินสด-ธนาคาร › กำหนดสาขาธนาคาร | `menu_setup_bank_branch` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_bank, erp_bank_branch |
| ระบบเงินสด-ธนาคาร › ประเภทสมุดเงินฝาก | `menu_book_bank_type` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_pass_book_type |
| ระบบเงินสด-ธนาคาร › ตัวย่อในสมุดเงินฝาก | `menu_book_bank_trans_type` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_book_bank_trans_type |
| ระบบเงินสด-ธนาคาร › กำหนดประเภทรายได้ | `menu_income_list` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_income_list |
| ระบบเงินสด-ธนาคาร › กำหนดประเภทค่าใช้จ่าย | `menu_expenses_list` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_expenses_list |
| ระบบเงินสด-ธนาคาร › ประเภทบัตรเครดิต | `menu_setup_credit_type` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_credit_type |
| ระบบเงินสด-ธนาคาร › กำหนดวงเงินสดย่อย | `menu_petty_cash` | ✓ | `SMLERPCASHBANK._cb_petty_cash` |  |  |
| ระบบเงินสด-ธนาคาร › รายละเอียดคูปอง | `menu_coupon_list` | ✓ | `SMLERPControl._coupon._couponList` |  | coupon_list, cb_trans_detail, ar_customer |
| ระบบเงินสด-ธนาคาร › กำหนดธนบัตร | `menu_setup_banknotes` | ✓ | `MyLib._manageMasterCodeFull` |  | banknotes |
| ระบบสินทรัพย์ › กำหนดประเภทสินทรัพย์ | `menu_asset_setup_type` | ✓ | `MyLib._manageMasterCodeFull` |  | as_asset_type |
| ระบบสินทรัพย์ › กำหนดตำแหน่งที่ตั้งสินทรัพย์ | `menu_asset_setup_location` | ✓ | `MyLib._manageMasterCodeFull` |  | as_asset_location |
| ระบบสินทรัพย์ › กำหนดการบำรุงรักษาสินทรัพย์ | `menu_asset_setup_maintain` | ✓ | `MyLib._manageMasterCodeFull` |  | as_asset_maintain |
| ระบบสินทรัพย์ › กำหนดหน่วยการบำรุงรักษาสินทรัพย์ | `menu_asset_setup_maintain_unit` | ✓ | `MyLib._manageMasterCodeFull` |  | as_asset_maintain_unit |
| ระบบสินทรัพย์ › กำหนดประเภทการตัดจำหน่าย | `menu_asset_setup_retire` | ✓ | `MyLib._manageMasterCodeFull` |  | as_asset_retire |
| ระบบบัญชี › กำหนดงวดบัญชี | `menu_account_period` | ✓ | `SMLERPConfig._accountPeriod._accountPeriod` |  | erp_account_period |
| ระบบบัญชี › กำหนดสมุดบัญชี | `menu_setup_gl_journal_book` | ✓ | `MyLib._manageMasterCodeFull` |  | gl_journal_book |
| ระบบบัญชี › กำหนดประเภทบัญชี | `menu_setup_gl_account_type` | ✓ | `MyLib._manageMasterCodeFull` |  | gl_account_type |
| ระบบบัญชี › กำหนดกลุ่มบัญชี | `menu_setup_gl_account_group` | ✓ | `MyLib._manageMasterCodeFull` |  | gl_account_group |
| ระบบบัญชี › กำหนดกลุ่มบัญชีกระแสเงินสด | `menu_setup_gl_group_for_cash_flow` | ✓ | `MyLib._manageMasterCodeFull` |  | gl_cash_flow_group |
| ระบบบัญชี › กำหนดกลุ่มภาษี | `menu_tax_group` | ✓ | `MyLib._manageMasterCodeFull` |  | gl_tax_group |
| ระบบบัญชี › กำหนดประเภทภาษี | `menu_tax_type` | ✓ | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ระบบบัญชี › กำหนดหน่วยงาน | `menu_setup_side` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_side_list |
| ระบบบัญชี › กำหนดการจัดสรร | `menu_setup_allocate` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_allocate_list |
| ระบบบัญชี › กำหนดโครงการ | `menu_setup_project` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_project_list |
| ระบบบัญชี › กำหนดงาน | `menu_setup_job` | ✓ | `MyLib._manageMasterCodeFull` |  | erp_job_list |
| ระบบบัญชี › ออกแบบงบการเงิน | `menu_gl_report_design` | ✓ | `SMLERPGL.StatementDesign._statementDesigner` |  | gl_design_report |
| สร้าง/แก้ไขแบบฟอร์ม | `menu_form_edit` | ✓ | `SMLReport._formReport._formDesigner` |  | formdesign |
| ออกแบบรายงาน | `fast_report_designer` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| เครื่องมือ › ระบบข้อมูล › กำหนดรูปแบบการค้นหาข้อมูล | `menu_view_manager_custom` | ✓ | `_g._viewManageCustom` |  | erp_view_table_custom, erp_view_column_custom, erp_view_table, erp_view_column |
| เครื่องมือ › ระบบข้อมูล › ตรวจสอบโครงสร้างฐานข้อมูล | `menu_verify_database` | ✓ | `MyLib._databaseManage._verifyDatabase` |  |  |
| เครื่องมือ › ระบบข้อมูล › ลดขนาดข้อมูล | `menu_shink_database` | ✓ | `MyLib._databaseManage._shrinkDatabase` |  |  |
| เครื่องมือ › ระบบข้อมูล › สำรองข้อมูล | `data_backup` | ✓ | `MyLib._databaseManage._dataBackupForm` |  |  |
| เครื่องมือ › ระบบข้อมูล › นำข้อมูลสำรองกลับมาใช้ | `data_restore` | ✓ | `MyLib._databaseManage._dataRestoreForm` |  |  |
| เครื่องมือ › ระบบข้อมูล › เปลี่ยนรหัสผ่าน | `menu_change_password` | ✓ | `MyLib._databaseManage._smlChangePassword` |  |  |
| เครื่องมือ › ระบบข้อมูล › กำหนดผู้มีสิทธิเข้าใช้ข้อมูล | `Node9` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| เครื่องมือ › ระบบข้อมูล › กำหนดสิทธิการใช้งาน | `Node10` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| เครื่องมือ › ระบบข้อมูล › แสดงโครงสร้างฐานข้อมูลทั้งหมด | `menu_database_struct` | ✓ | `MyLib._databaseManage._databaseStruct` |  |  |
| เครื่องมือ › ระบบข้อมูล › ตรวจสอบและปรับปรุงข้อมูล | `menu_checking_ic_trans` | ✓ | `SMLERPICInfo._icTransectionCheck` |  |  |
| เครื่องมือ › ระบบข้อมูล › ผังการทำงานระบบ | `menu_system_flow` |  | `SMLERPControl._systemFlow` |  |  |
| เครื่องมือ › ระบบข้อมูล › ใช้คำสั่ง Query | `menu_query` | ✓ | `MyLib._databaseManage._queryDataView` |  |  |
| เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสสินค้า | `menu_change_code_item` | ✓ | `_g._changeCode._itemCodeUserControl` |  | ic_inventory, ic_extra_detail, ic_color_use, ic_inventory_append |
| เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสเจ้าหนี้ | `menu_change_code_supplier` | ✓ | `_g._changeCode._changeApArCodeUserControl` |  | ar_customer, ap_supplier, ic_trans, ic_trans_detail |
| เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสลูกหนี้ | `menu_change_code_customer` | ✓ | `_g._changeCode._changeApArCodeUserControl` |  | ar_customer, ap_supplier, ic_trans, ic_trans_detail |
| เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสผังบัญชี | `menu_change_gl_account_code` | ✓ | `_g._changeCode.changeChartOfAccountUserControl` |  | gl_chart_of_account, ic_inventory, gl_journal_detail, gl_journal_allocate_list |
| เครื่องมือ › แสดงหน้าจอการใช้งาน | `menu_view_capture_screen_realtime` | ✓ | `_viewCapture._viewScreen` |  |  |
| เครื่องมือ › นำเข้าแบบฟอร์ม | `menu_import_formdesign` | ✓ | `SMLReport._ImportFormDesign` |  | formdesign |
| เครื่องมือ › ประวัติการใช้งาน › แสดงหน้าจอการใช้งาน (ย้อนหลัง) | `menu_view_capture_screen` | ✓ | `_viewCapture._viewCaptureScreen` |  |  |
| เครื่องมือ › ประวัติการใช้งาน › เข้าใช้ฐานข้อมูล | `menu_audit_login` | ✓ | `SMLERPAudit._loginLog` |  | logs |
| เครื่องมือ › ประวัติการใช้งาน › เข้าออกระบบ | `menu_audit_menu` | ✓ | `SMLERPAudit._menuLog` |  | logs |
| เครื่องมือ › ประวัติการใช้งาน › ข้อมูลรายวัน | `menu_audit_trans` | ✓ | `SMLERPAudit._transLog` |  | logs |
| เครื่องมือ › ประวัติการใช้งาน › ข้อมูลหลัก | `menu_audit_master` | ✓ | `SMLERPAudit._masterLog` |  | master_logs |
| เครื่องมือ › ประวัติการใช้งาน › ประวัติการแก้ไขรายวัน | `menu_trans_full_logs` | ✓ | `SMLERPAudit._fullLogs` |  | master_logs, logs |
| เครื่องมือ › นำเข้าข้อมูลหลัก | `menu_import_data_master` | ✓ | `MyLib._databaseManage._importDataControl` |  |  |
| เครื่องมือ › นำเข้ารายงาน | `menu_import_report` | ✓ | `SMLFastReport._importFastReport` |  | sml_fastreport |
| เครื่องมือ › นำเข้ารายงานสาขา | `menu_import_report_branch` | ✓ | `SMLFastReport._importFastReport` |  | sml_fastreport |
| เครื่องมือ › นำเข้ารูปภาพสินค้า | `menu_import_ic_picture` | ✓ | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| เครื่องมือ › สร้างคำสั่ง Query | `menu_gen_qeury` | ✓ | `MyLib._databaseManage._genQueryControl` |  |  |
| เครื่องมือ › หน้าจอเริ่มต้น | `menu_welcome_page` | ✓ | `SMLAccount._mainShortcut` |  |  |
| เครื่องมือ › นำเข้าข้อมูลจากรูปภาพ | `menu_import_from_image` | ✓ | `SMLERPControl._importFromImageForm` |  | erp_doc_format, sml_doc_images, ic_trans |
| เครื่องมือ › นำเข้ารูปภาพสินค้า | `menu_import_ic_picture` |  | `SMLERPIC._icImportPicture` |  | images, ic_inventory |
| เครื่องมือ › ย้ายรูปภาพสินค้า | `menu_tools_image_transfer` |  | `SMLERPControl._imageTransfer` |  |  |
| เครื่องมือ › แสดง Resource Language | `menu_resource_view` | ✓ | `_g._resource_viewer` |  | ap_group_sub, ar_group_sub, erp_expenses_list, erp_income_list |
