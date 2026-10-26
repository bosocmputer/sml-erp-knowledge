---
tags: [sml, menu, generated]
---
# แผนที่เมนู → หน้าจอ (SMLAccount / Pro / AccountPOS / AccountPOSPro)

> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` (static analysis) — อย่าแก้ด้วยมือ ข้อมูลดิบสำหรับ agent อยู่ที่ `04-Menu/menu-map.json`

เมนูปลายทาง 990 รายการ จับคู่คลาสได้ 932 รายการ (94%) · เห็นตามรุ่น: Acc (&2&) 686 · Pro (&3&) 690 · AccPOS (&12&) 738 · AccPOSPro (&13&) 742

**เลข edition ใน tag ของเมนู** (`SMLERPTemplate/_templateMainForm.cs` `_menuRemoveByVersion`): 2 = SMLAccount, 3 = SMLAccountProfessional, 6 = SMLPOS/IMSPOS, 7 = POSLite, 8 = TomYumGoong, 9 = POSMED, 10 = POSStarter, 11 = TomYumGoongPro, 12 = SMLAccountPOS, **13 = SMLAccountPOSProfessional / SMLCM**, 15 = Merchant, 16 = POSCoffee · ตัวเปิดที่ยังพัฒนาอยู่ `SMLAccountPOSPro/Program.cs` ตั้ง `SMLAccountPOSProfessional` (13) — ✅ ยืนยันจากเครื่องร้าน AOY (แถบเมนูมี 11.คลังสินค้า 12.Data ซึ่งมีเฉพาะ edition 3/13) (โปรเจกต์เก่า `SMLAccountPOSProfessional/` แก้ล่าสุด 2015 ตั้ง `SMLAccountPOS` = 12) — เมนูแสดงเมื่อ tag ว่าง, มีเลขของ edition, หรือเป็น `&hide&` ตรงๆ (หรือ tag OEM `&imex&`/`&singha&`, หรือเปิดใน enableMenuFeatures) แล้วจึงกรองตามสิทธิ์ผู้ใช้

**เลขเมนู** = เลข X.Y.Z ที่โปรแกรมใส่หน้าชื่อเมนู (`mainMenuChangeResource`) หลังตัดเมนูตามรุ่น — นับรวมเมนูที่ซ่อน (`&hide&`) ด้วย จึงอาจมีเลขข้าม (✅ ยืนยันจากภาพหน้าจอ AOY 2026-10-26: เมนู ระบบขาย เริ่มที่ 1.3.2 เพราะ 1.3.1 ถูกซ่อน) · เลขที่ต่างกันตามรุ่นแสดงแยก เช่น `5.1 Acc/Pro · 6.1 AccPOS/AccPOSPro` · ไม่มีเลข = รุ่นเหล่านั้นไม่เห็นเมนูนี้ · ไม่รวมผลของสิทธิ์ผู้ใช้ (ตัวเลือก `show_menu_by_permission` ซ่อนเมนูแต่ไม่เปลี่ยนเลข), OEM และเมนูที่เปิดจาก service

การ route: `SMLAccount/_mainForm.cs` `_activeMenu` ตรวจสิทธิ์ → ดู tag ของเมนูตามลำดับการเช็คในโค้ด (ตัวแรกที่ตรงชนะ) → `_selectMenuXxx` → `<Module>._selectMenu._getObject(menuName)` (switch) → `new ScreenClass(...)` เปิดเป็นแท็บ ดู [[login-flow]], [[screen-classes]] · ตระกูล SMLPOS ดู [[menu-map-pos]]

คอลัมน์ trans_flag แปลงจาก `_transControlTypeEnum` ที่ส่งเข้า constructor (ถ้ามี) ดู [[trans_flag]]

## เริ่มต้น (135)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 1.1.1 | รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดบริษัท | `menu_company_profile` | `SMLERPConfig._companyProfile` |  |  |
| 1.1.2 | รายละเอียดข้อมูลทั่วไป › กำหนดข้อเลือกพิเศษต่างๆ | `menu_option` | `SMLERPConfig._option` |  |  |
| 1.1.3 | รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดสาขา | `menu_setup_branch` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.4 | รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดแผนก | `menu_setup_department_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.5 | รายละเอียดข้อมูลทั่วไป › กำหนดพนักงาน | `menu_setup_staff` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.6 | รายละเอียดข้อมูลทั่วไป › กำหนดกลุ่มพนักงาน | `menu_setup_user_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.7 | รายละเอียดข้อมูลทั่วไป › กำหนดการใช้คลังและที่เก็บ | `menu_setup_user_group_warehouse_shelf` | `_g._userGroupWarehouseShelf` | _myManageData |  |
| 1.1.8 | รายละเอียดข้อมูลทั่วไป › กำหนดรูปภาพพนักงาน | `menu_setup_staff_pic` | `SMLERPControl.erp_user._erp_userDetailpicture` | _myManageData, _getPicture |  |
| 1.1.9 | รายละเอียดข้อมูลทั่วไป › รายงานพนักงานเรียงตามกลุ่ม | `menu_report_employee_group` | `SMLFastReport._designer` |  |  |
| 1.1.10 | รายละเอียดข้อมูลทั่วไป › กำหนดผู้ใช้ระบบ MIS | `menu_setup_staff_mis` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.11 | รายละเอียดข้อมูลทั่วไป › กำหนดกลุ่มเอกสาร | `menu_setup_doc_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.12 | รายละเอียดข้อมูลทั่วไป › กำหนดรูปแบบเลขที่เอกสาร | `menu_setup_doc_format` | `_g._docFormat` |  |  |
| 1.1.13 | รายละเอียดข้อมูลทั่วไป › กำหนดประเภทการขนส่ง | `menu_setup_transport` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.14 | รายละเอียดข้อมูลทั่วไป › กำหนดเขตการขนส่ง | `menu_setup_ar_logistic_area` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.15 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดสกุลเงิน | `menu_setup_currency` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.15 Acc/AccPOS · 1.1.16 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดค่าเครื่องรูดบัตรเครดิต | `menu_edc_config` | `SMLERPConfig._edcConfigForm` |  |  |
| 1.1.16 Acc/AccPOS · 1.1.17 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดค่าจอแสดงผล QR Code | `menu_usb_qr_display_config` | `SMLERPConfig._usbQRDisplayConfigForm` |  |  |
| 1.1.17 Acc/AccPOS · 1.1.18 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดค่า QR Code Payment | `menu_setup_qr_payment` | `SMLERPConfig.qrpayment._config_qr_payment_control` |  |  |
| 1.1.18 Acc/AccPOS · 1.1.19 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › ดึงรายชื่อจังหวัดอัตโนมัติ | `menu_setup_province_auto` | `SMLERPConfig._provinceLoadFromWebControl` |  |  |
| 1.1.19 Acc/AccPOS · 1.1.20 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสจังหวัด | `menu_setup_province` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.20 Acc/AccPOS · 1.1.21 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสอำเภอ | `menu_setup_ampher` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.21 Acc/AccPOS · 1.1.22 Pro/AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสตำบล | `menu_setup_tambon` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.22 AccPOS · 1.1.23 AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดค่าเริ่มต้น POS | `menu_config_pos_startup` | `SMLPOSControl._posConfig` | _searchDataFull |  |
| 1.1.23 AccPOS · 1.1.24 AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสเครื่อง POS | `menu_config_pos_machine` | `SMLPOSControl._posMachine` | _myManageData, _searchDataFull |  |
| 1.1.24 AccPOS · 1.1.25 AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดเงื่อนไขสะสมแต้ม | `menu_pos_point_rate` | `SMLPOSControl._posPointPeriodForm` |  |  |
| 1.1.25 AccPOS · 1.1.26 AccPOSPro | รายละเอียดข้อมูลทั่วไป › กำหนดคุณสมบัติของเครื่อง POS | `menu_config_pos_screen` | `SMLPosClient._configPOSScreen` | _searchDataFull, _posScreenConfig, _screenConfig |  |
| 1.2.1 | ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าหลัก | `menu_setup_ic_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.2 | ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าย่อย | `menu_setup_ic_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.3 | ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าย่อย2 | `menu_setup_ic_group_sub2` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.4 | ระบบสินค้าคงคลัง › กำหนดยี่ห้อสินค้า | `menu_setup_ic_brand` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.5 | ระบบสินค้าคงคลัง › กำหนดรุ่นสินค้า | `menu_setup_ic_model` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.6 | ระบบสินค้าคงคลัง › กำหนดสีสินค้า | `menu_setup_ic_color` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.7 | ระบบสินค้าคงคลัง › กำหนดขนาดสินค้า | `menu_setup_ic_size` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.8 | ระบบสินค้าคงคลัง › กำหนดรูปแบบสินค้า | `menu_setup_ic_pattern` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.9 | ระบบสินค้าคงคลัง › กำหนดเกรดสินค้า | `menu_setup_ic_grade` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.10 | ระบบสินค้าคงคลัง › กำหนดหมวดสินค้า | `menu_setup_ic_category` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.11 | ระบบสินค้าคงคลัง › กำหนดรูปทรงสินค้า | `menu_setup_ic_design` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.12 | ระบบสินค้าคงคลัง › กำหนดชื่อมิติสินค้า | `menu_setup_ic_dimension_name` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.13 | ระบบสินค้าคงคลัง › กำหนดมิติสินค้า | `menu_setup_ic_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.14 | ระบบสินค้าคงคลัง › ประเภทรายได้ | `menu_income_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.15 | ระบบสินค้าคงคลัง › กำหนดระดับสินค้า | `menu_setup_ic_class` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.16 | ระบบสินค้าคงคลัง › กำหนดหน่วยนับสินค้า | `menu_setup_ic_unit` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.17 | ระบบสินค้าคงคลัง › กำหนดคลังสินค้า | `menu_setup_ic_wh` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.18 | ระบบสินค้าคงคลัง › กำหนดพื้นที่เก็บสินค้า | `menu_setup_ic_shelf` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.19 | ระบบสินค้าคงคลัง › กำหนดกลุ่มบัญชีสินค้า | `menu_setup_ic_account_group` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.2.20 | ระบบสินค้าคงคลัง › กำหนดพิกัดศุลกากร | `menu_setup_ic_import_duty_point` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.21 | ระบบสินค้าคงคลัง › กำหนดประเภทการเบิก | `menu_setup_ic_issue_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.22 | ระบบสินค้าคงคลัง › กำหนดสาเหตุการปรับปรุง | `menu_setup_stk_adjust` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.23 | ระบบสินค้าคงคลัง › กำหนดเหตุผลการปิดสินค้า | `menu_setup_ic_close_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.24 | ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ | `ic_auto_add_warehouse_and_location` | `_g._ic_add_warehouse_shelf_form` |  |  |
| 1.2.25 | ระบบสินค้าคงคลัง › กำหนดผู้ผลิต | `menu_manufacturer_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| ซ่อน | ระบบขาย › กำหนดรายได้อื่นๆ | `menu_setup_other_income` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.3.2 | ระบบขาย › กำหนดเขตการขาย | `menu_setup_ar_sale_area` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.3.3 AccPOS/AccPOSPro | ระบบขาย › ออกแบบหน้าจอขาย POS | `client_design` | `SMLPOSControl._designer._clientDesign` | _searchDataFull |  |
| 1.3.4 AccPOS/AccPOSPro | ระบบขาย › Download ระบบเสียงพูด | `menu_pos_sound_download_install` | `SMLPOSControl._posDownloadSound` |  |  |
| — | ระบบขาย › กำหนดแผนการขาย | `menu_sale_plan` | `SMLERPConfig._salePlanManage` | _myManageData |  |
| — | ระบบขาย › กำหนดเขตเก็บเงิน | `menu_ar_setup_paybill_area` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.3.3 Acc/Pro · 1.3.5 AccPOS/AccPOSPro | ระบบขาย › กำหนดกลุ่มอนุมัติวงเงิน | `menu_approve_credit_level` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.4.1 | ระบบเจ้าหนี้ › กำหนดประเภทเจ้าหนี้ | `menu_setup_ap_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.4.2 | ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้หลัก | `menu_setup_ap_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.4.3 | ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้ย่อย | `menu_setup_ap_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.4.4 | ระบบเจ้าหนี้ › กำหนดมิติเจ้าหนี้ | `menu_setup_ap_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.1 | ระบบลูกหนี้ › กำหนดประเภทลูกหนี้ | `menu_setup_ar_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.2 | ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้หลัก | `menu_setup_ar_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.3 | ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้ย่อย | `menu_setup_ar_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.4 | ระบบลูกหนี้ › กำหนดมิติลูกหนี้ | `menu_setup_ar_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.5 | ระบบลูกหนี้ › กำหนดเหตุผลอนุมัติวงเงิน | `menu_setup_ar_credit_approve` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.6 | ระบบลูกหนี้ › กำหนดเงื่อนไขการวางบิล | `menu_setup_ar_pay_bill_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.7 | ระบบลูกหนี้ › กำหนดเงื่อนไขการรับเช็ค | `menu_setup_ar_keep_chq_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.8 | ระบบลูกหนี้ › กำหนดเงือนไขการชำระเงิน | `menu_setup_ar_keep_money` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.9 | ระบบลูกหนี้ › กำหนดวันครบกำหนดชำระเงิน | `menu_ar_credit_pay_bill` | `SMLERPControl.ARCreditPayBillForm` |  |  |
| 1.5.10 | ระบบลูกหนี้ › กำหนดกลุ่มผู้ติดต่อ | `menu_ar_contact_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.1 | ระบบเงินสด-ธนาคาร › กำหนดธนาคาร | `menu_setup_bank` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.2 | ระบบเงินสด-ธนาคาร › กำหนดสาขาธนาคาร | `menu_setup_bank_branch` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.3 | ระบบเงินสด-ธนาคาร › ประเภทสมุดเงินฝาก | `menu_book_bank_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.4 | ระบบเงินสด-ธนาคาร › ตัวย่อในสมุดเงินฝาก | `menu_book_bank_trans_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.5 | ระบบเงินสด-ธนาคาร › กำหนดประเภทรายได้ | `menu_income_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.6 | ระบบเงินสด-ธนาคาร › กำหนดประเภทค่าใช้จ่าย | `menu_expenses_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.7 | ระบบเงินสด-ธนาคาร › ประเภทบัตรเครดิต | `menu_setup_credit_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.8 | ระบบเงินสด-ธนาคาร › กำหนดวงเงินสดย่อย | `menu_petty_cash` | `SMLERPCASHBANK._cb_petty_cash` |  |  |
| 1.6.9 | ระบบเงินสด-ธนาคาร › รายละเอียดคูปอง | `menu_coupon_list` | `SMLERPControl._coupon._couponList` |  |  |
| 1.6.10 | ระบบเงินสด-ธนาคาร › กำหนดธนบัตร | `menu_setup_banknotes` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.1 | ระบบสินทรัพย์ › กำหนดประเภทสินทรัพย์ | `menu_asset_setup_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.2 | ระบบสินทรัพย์ › กำหนดตำแหน่งที่ตั้งสินทรัพย์ | `menu_asset_setup_location` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.3 | ระบบสินทรัพย์ › กำหนดการบำรุงรักษาสินทรัพย์ | `menu_asset_setup_maintain` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.4 | ระบบสินทรัพย์ › กำหนดหน่วยการบำรุงรักษาสินทรัพย์ | `menu_asset_setup_maintain_unit` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.5 | ระบบสินทรัพย์ › กำหนดประเภทการตัดจำหน่าย | `menu_asset_setup_retire` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.1 | ระบบบัญชี › กำหนดงวดบัญชี | `menu_account_period` | `SMLERPConfig._accountPeriod._accountPeriod` |  |  |
| 1.8.2 | ระบบบัญชี › กำหนดสมุดบัญชี | `menu_setup_gl_journal_book` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.3 | ระบบบัญชี › กำหนดประเภทบัญชี | `menu_setup_gl_account_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.4 | ระบบบัญชี › กำหนดกลุ่มบัญชี | `menu_setup_gl_account_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.5 | ระบบบัญชี › กำหนดกลุ่มบัญชีกระแสเงินสด | `menu_setup_gl_group_for_cash_flow` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.6 | ระบบบัญชี › กำหนดกลุ่มภาษี | `menu_tax_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.7 | ระบบบัญชี › กำหนดประเภทภาษี | `menu_tax_type` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.8.8 | ระบบบัญชี › กำหนดหน่วยงาน | `menu_setup_side` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.9 | ระบบบัญชี › กำหนดการจัดสรร | `menu_setup_allocate` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.10 | ระบบบัญชี › กำหนดโครงการ | `menu_setup_project` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.11 | ระบบบัญชี › กำหนดงาน | `menu_setup_job` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.8.12 | ระบบบัญชี › ออกแบบงบการเงิน | `menu_gl_report_design` | `SMLERPGL.StatementDesign._statementDesigner` | _searchDataFull |  |
| 1.9 | สร้าง/แก้ไขแบบฟอร์ม | `menu_form_edit` | `SMLReport._formReport._formDesigner` |  |  |
| 1.10 | ออกแบบรายงาน | `fast_report_designer` | `SMLFastReport._designer` |  |  |
| 1.11.1.1 | เครื่องมือ › ระบบข้อมูล › กำหนดรูปแบบการค้นหาข้อมูล | `menu_view_manager_custom` | `_g._viewManageCustom` | _myManageData |  |
| 1.11.1.2 | เครื่องมือ › ระบบข้อมูล › ตรวจสอบโครงสร้างฐานข้อมูล | `menu_verify_database` | `MyLib._databaseManage._verifyDatabase` |  |  |
| 1.11.1.3 | เครื่องมือ › ระบบข้อมูล › ลดขนาดข้อมูล | `menu_shink_database` | `MyLib._databaseManage._shrinkDatabase` |  |  |
| 1.11.1.4 | เครื่องมือ › ระบบข้อมูล › สำรองข้อมูล | `data_backup` | `MyLib._databaseManage._dataBackupForm` |  |  |
| 1.11.1.5 | เครื่องมือ › ระบบข้อมูล › นำข้อมูลสำรองกลับมาใช้ | `data_restore` | `MyLib._databaseManage._dataRestoreForm` |  |  |
| 1.11.1.6 | เครื่องมือ › ระบบข้อมูล › เปลี่ยนรหัสผ่าน | `menu_change_password` | `MyLib._databaseManage._smlChangePassword` |  |  |
| ซ่อน | เครื่องมือ › ระบบข้อมูล › กำหนดผู้มีสิทธิเข้าใช้ข้อมูล | `Node9` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ซ่อน | เครื่องมือ › ระบบข้อมูล › กำหนดสิทธิการใช้งาน | `Node10` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.11.1.9 | เครื่องมือ › ระบบข้อมูล › แสดงโครงสร้างฐานข้อมูลทั้งหมด | `menu_database_struct` | `MyLib._databaseManage._databaseStruct` |  |  |
| 1.11.1.10 | เครื่องมือ › ระบบข้อมูล › ตรวจสอบและปรับปรุงข้อมูล | `menu_checking_ic_trans` | `SMLERPICInfo._icTransectionCheck` |  |  |
| 1.11.1.11 | เครื่องมือ › ระบบข้อมูล › ผังการทำงานระบบ | `menu_system_flow` | `SMLERPControl._systemFlow` |  |  |
| 1.11.1.12 | เครื่องมือ › ระบบข้อมูล › ใช้คำสั่ง Query | `menu_query` | `MyLib._databaseManage._queryDataView` |  |  |
| 1.11.2.1 | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสสินค้า | `menu_change_code_item` | `_g._changeCode._itemCodeUserControl` | _searchDataFull |  |
| 1.11.2.2 | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสเจ้าหนี้ | `menu_change_code_supplier` | `_g._changeCode._changeApArCodeUserControl` | _searchDataFull |  |
| 1.11.2.3 | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสลูกหนี้ | `menu_change_code_customer` | `_g._changeCode._changeApArCodeUserControl` | _searchDataFull |  |
| 1.11.2.4 | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสผังบัญชี | `menu_change_gl_account_code` | `_g._changeCode.changeChartOfAccountUserControl` |  |  |
| 1.11.3 | เครื่องมือ › แสดงหน้าจอการใช้งาน | `menu_view_capture_screen_realtime` | `_viewCapture._viewScreen` |  |  |
| 1.11.4 | เครื่องมือ › นำเข้าแบบฟอร์ม | `menu_import_formdesign` | `SMLReport._ImportFormDesign` |  |  |
| 1.11.5.1 | เครื่องมือ › ประวัติการใช้งาน › แสดงหน้าจอการใช้งาน (ย้อนหลัง) | `menu_view_capture_screen` | `_viewCapture._viewCaptureScreen` |  |  |
| 1.11.5.2 | เครื่องมือ › ประวัติการใช้งาน › เข้าใช้ฐานข้อมูล | `menu_audit_login` | `SMLERPAudit._loginLog` |  |  |
| 1.11.5.3 | เครื่องมือ › ประวัติการใช้งาน › เข้าออกระบบ | `menu_audit_menu` | `SMLERPAudit._menuLog` |  |  |
| 1.11.5.4 | เครื่องมือ › ประวัติการใช้งาน › ข้อมูลรายวัน | `menu_audit_trans` | `SMLERPAudit._transLog` |  |  |
| 1.11.5.5 | เครื่องมือ › ประวัติการใช้งาน › ข้อมูลหลัก | `menu_audit_master` | `SMLERPAudit._masterLog` |  |  |
| 1.11.5.6 | เครื่องมือ › ประวัติการใช้งาน › ประวัติการแก้ไขรายวัน | `menu_trans_full_logs` | `SMLERPAudit._fullLogs` |  |  |
| 1.11.6 | เครื่องมือ › นำเข้าข้อมูลหลัก | `menu_import_data_master` | `MyLib._databaseManage._importDataControl` |  |  |
| 1.11.7 | เครื่องมือ › นำเข้ารายงาน | `menu_import_report` | `SMLFastReport._importFastReport` |  |  |
| 1.11.8 | เครื่องมือ › นำเข้ารายงานสาขา | `menu_import_report_branch` | `SMLFastReport._importFastReport` |  |  |
| 1.11.9 | เครื่องมือ › นำเข้ารูปภาพสินค้า | `menu_import_ic_picture` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.11.10 | เครื่องมือ › สร้างคำสั่ง Query | `menu_gen_qeury` | `MyLib._databaseManage._genQueryControl` |  |  |
| 1.11.11 AccPOS/AccPOSPro | เครื่องมือ › หน้าจอเริ่มต้น | `menu_welcome_page` | `SMLAccount._mainShortcut` |  |  |
| 1.11.11 Acc/Pro · 1.11.12 AccPOS/AccPOSPro | เครื่องมือ › นำเข้าข้อมูลจากรูปภาพ | `menu_import_from_image` | `SMLERPControl._importFromImageForm` |  |  |
| 1.11.12 Acc/Pro | เครื่องมือ › นำเข้ารูปภาพสินค้า | `menu_import_ic_picture` | `SMLERPIC._icImportPicture` |  |  |
| 1.11.13 | เครื่องมือ › ย้ายรูปภาพสินค้า | `menu_tools_image_transfer` | `SMLERPControl._imageTransfer` |  |  |
| 1.11.14 | เครื่องมือ › แสดง Resource Language | `menu_resource_view` | `_g._resource_viewer` |  |  |

## สินค้า (160)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 2.1.1 | ข้อมูลสินค้า › ข้อมูลสินค้า | `menu_ic_item_detail` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.2 | ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_barcode` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.3 | ข้อมูลสินค้า › ข้อมูลสินค้าเพิ่มเติม | `menu_ic_item_detail_2` | `SMLERPIC._icMainDetail` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.4 | ข้อมูลสินค้า › ข้อมูลสินค้าเพิ่มเติม (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_2_barcode` | `SMLERPIC._icMainDetail` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.5 | ข้อมูลสินค้า › รายละเอียดสินค้า | `menu_ic_description` | `SMLERPIC._icDescription` | _myManageData, _icmainScreenTopControl |  |
| 2.1.6 | ข้อมูลสินค้า › แก้ไขรายละเอียด(เร็ว) | `menu_ic_description_fast` | `SMLERPIC._icEditDetailFast` | _myManageData, _icmainScreenDescripControl, _icmainScreenDimesionControl |  |
| 2.1.7 | ข้อมูลสินค้า › กำหนดบาร์โค้ดสินค้า | `menu_ic_item_barcode` | `SMLERPIC._icBarcode` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.1.8 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด | `menu_ic_item_barcode_discount` | `SMLERPIC._icBarcodeDiscount` | _myManageData |  |
| 2.1.9 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด (เร็ว) | `menu_ic_item_multibarcode_discount` | `SMLERPIC._icMultiBarcodeDiscount` | _myManageData |  |
| 2.1.8 Acc/Pro · 2.1.10 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดลำดับการค้นหา | `menu_ic_item_level` | `SMLERPIC._icSearchLevel` | _myManageData, _barcodeSearchForm, _itemSearchLevelControl |  |
| 2.1.9 Acc/Pro · 2.1.11 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดลำดับการค้นหา (เร็ว) | `menu_ic_multi_item_level` | `SMLERPIC._icSearchLevelMultiItem` | _myManageData, _itemSearchLevelControl |  |
| 2.1.10 Acc/Pro · 2.1.12 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดรูปภาพ | `menu_ic_item_picture` | `SMLERPIC._icMainDetailPicture` | _myManageData, _barcodeSearchForm, _getPicture |  |
| 2.1.11 Acc/Pro · 2.1.13 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดรูปภาพตามบาร์โค้ด | `menu_ic_item_barcode_picture` | `SMLERPIC._icBarcodePicture` | _myManageData, _getPicture, _icmainScreenTopControl |  |
| 2.1.14 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดสูตรโปรโมชั่น | `pos_promotion_formula` | `SMLERPIC._icPromotion._formula` | _myManageData |  |
| 2.1.15 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดแคมเปญท้ายใบเสร็จ | `menu_setup_pos_slip_campaign` | `SMLERPControl.pos_slip_campaign.pos_slip_campaign` |  |  |
| 2.1.12 Acc/Pro · 2.1.16 AccPOS/AccPOSPro | ข้อมูลสินค้า › ทะเบียน Serial Number | `menu_ic_item_serial` | `SMLERPIC._icSerialNumber` | _myManageData, _icSerialNumerScreen |  |
| 2.1.13 Acc/Pro · 2.1.17 AccPOS/AccPOSPro | ข้อมูลสินค้า › สินค้าชุด | `menu_ic_item_set` | `SMLERPIC._icMainProductSet` | _myManageData, _icmainScreenTopControl, _icTransItemGridControl |  |
| 2.1.14 Acc/Pro · 2.1.18 AccPOS/AccPOSPro | ข้อมูลสินค้า › เพิ่มบาร์โค๊ดสินค้าแบบเร็ว | `menu_ic_item_add_barcode_fast` | `SMLERPIC._icAddBarcodeFastControl` | _searchDataFull, _selectWarehouseAndLocationForm, GetItemCodeEventHandler |  |
| — | ข้อมูลสินค้า › ตรวจสอบสินค้าหลายหน่วยนับ | `menu_ic_unit_checker` | `SMLERPIC._icUnitCheckerControl` |  |  |
| 2.1.15 Acc/Pro · 2.1.19 AccPOS/AccPOSPro | ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดจาก Text File | `menu_ic_item_barcode_checker` | `SMLERPIC._barcodeCheckerControl` |  |  |
| 2.1.16 Acc/Pro · 2.1.20 AccPOS/AccPOSPro | ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดตามมาตรฐาน EAN13 | `menu_ic_item_barcode_checker_ean13` | `SMLBarcodeManage._itemBarcodeCheckerEan13` |  |  |
| 2.1.21 AccPOS/AccPOSPro | ข้อมูลสินค้า › ตรวจสอบราคาสินค้า | `check_price` | `SMLPOSControl._checkPriceUserControl` |  |  |
| 2.1.17 Acc/Pro · 2.1.22 AccPOS/AccPOSPro | ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป | `menu_ic_item_barcode_laser_print` | `SMLBarcodeManage._itemBarcodePrint` | _getImageData | 501 |
| — | ข้อมูลสินค้า › กำหนดการค้นหาแบบเฉพาะเจาะจง | `menu_ic_specific_search` | `SMLERPIC._icSpecificSearch` | _myManageData |  |
| 2.1.18 Acc/Pro · 2.1.23 AccPOS/AccPOSPro | ข้อมูลสินค้า › คลังที่เก็บสินค้า | `menu_ic_warehouse_locaton` | `SMLERPIC._icWarehouseLocation` | _myManageData, _icmainScreenTopControl, _icmainGridWarehouseLocationControl |  |
| 2.1.19 Acc/Pro · 2.1.24 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดกลุ่มที่เก็บ | `ic_warehouse_and_location_group` | `SMLERPIC._whLocationGroup` | _myManageData |  |
| 2.1.20.1 Acc/Pro · 2.1.25.1 AccPOS/AccPOSPro | ข้อมูลสินค้า › รายงาน › รายงานรายละเอียดสินค้า | `menu_ic_detail` | `SMLERPICReport._report_ic_master` |  |  |
| 2.1.20.2 Acc/Pro · 2.1.25.2 AccPOS/AccPOSPro | ข้อมูลสินค้า › รายงาน › รายงานสินค้าชุด | `menu_ic_report_item_set_formula` | `SMLERPICReport._report_item_set_formula` |  |  |
| 2.1.20.3 Acc/Pro · 2.1.25.3 AccPOS/AccPOSPro | ข้อมูลสินค้า › รายงาน › รายงานบาร์โค้ดสินค้า | `menu_ic_report_item_barcode` | `SMLERPICReport._report_ic_barcode` |  |  |
| 2.1.20.4 Acc/Pro · 2.1.25.4 AccPOS/AccPOSPro | ข้อมูลสินค้า › รายงาน › รายงานสินค้าแบบมี Serial | `menu_ic_by_license` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_by_serial |
| 2.1.21 Acc/Pro · 2.1.26 AccPOS/AccPOSPro | ข้อมูลสินค้า › กำหนดสินค้า | `menu_ic_item_for_sync` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.22 Acc/Pro · 2.1.27 AccPOS/AccPOSPro | ข้อมูลสินค้า › ปรับราคาสินค้า | `menu_ic_modify_price` | `SMLERPIC._icModifyPrice` |  |  |
| 2.2 | กำหนดราคาซื้อ | `menu_ic_purchase_price` | `SMLInventoryControl._icPurchasePrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.3 | ของแถมซื้อ | `menu_ic_purchase_premium` | `SMLERPIC._icPurchasePermium` | _myManageData, _icTransItemGridControl |  |
| 2.4 | กำหนดราคาขายมาตรฐาน | `menu_ic_item_saleprice` | `SMLInventoryControl._icPrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.5 | กำหนดราคาขายทั่วไป | `menu_ic_item_saleprice_2` | `SMLInventoryControl._icPrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.6 | กำหนดส่วนลดสินค้า | `menu_ic_discount` | `SMLInventoryControl._icPrice._icDiscount` | _myManageData |  |
| 2.7 | กำหนดรูปแบบสูตรราคาขาย | `menu_ic_item_formula_template` | `SMLInventoryControl._icPrice._icPriceFormulaTemplate` |  |  |
| 2.8 | กำหนดสูตรราคาขาย | `menu_ic_item_saleprice_formula` | `SMLInventoryControl._icPrice._icPriceFormula` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.9 | ราคาขายสินค้า | `menu_ic_all_price` | `SMLInventoryControl._icPrice._icAllPrice` | _myManageData |  |
| 2.10.1 | รายงาน › รายงานราคาซื้อสินค้า | `menu_ic_report_item_purchase_price` | `SMLERPICReport._report_ic_purchase_price` |  |  |
| 2.10.2 | รายงาน › รายงานของแถมซื้อ | `menu_ic_report_item_giveaway` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_Giveaway |
| 2.10.3 | รายงาน › รายงานราคาขายสินค้ามาตรฐาน | `menu_ic_report_item_sale_price` | `SMLERPICReport._report_ic_sale_price` |  |  |
| 2.10.4 | รายงาน › รายงานราคาขายสินค้าทั่วไป | `menu_ic_report_item_sale_price_normal` | `SMLERPICReport._report_ic_sale_price` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › กำหนดจำนวนภาชนะ(Container) | `menu_imex_qc_purchase_packing_size_container_assign` | `IMEXControl.QualityControl.ICQCPurchaesPackingSizeSplit` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกรับสินค้า | `menu_ic_qc_receive` | `IMEXControl.QualityControl.ICQCProductReceive` | _searchDataFull |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพ - Pass | `menu_ic_qc_control_pass` | `IMEXControl.QualityControl.ICQCPassControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพ - Reject | `menu_ic_qc_control_reject` | `IMEXControl.QualityControl.ICQCRejectControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพซ้ำ (ReTest) | `menu_ic_qc_retest` | `IMEXControl.QualityControl.ICQCRetestControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › ทะเบียนการตรวจสอบคุณภาพ | `menu_ic_qc_lab_list` | `IMEXControl.QualityControl.ICQCLabList` | _myManageData |  |
| — | ตรวจสอบคุณภาพสินค้า › กำหนดค่าระบบตรวจสอบคุณภาพ | `menu_imex_qc_config` | `IMEXControl.QualityControl._qcConfigScreen` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › กำหนด Identify | `menu_qc_indentify` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | ตรวจสอบคุณภาพสินค้า › พิมพ์แท็กสินค้า | `menu_print_tag_label` | `SMLInventoryControl._icTransLabelPrintControl` | _myManageData, _icTransLabelPrintGrid, _icTransLabelPrintScreen |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึก Lab Container ยกมา | `menu_qc_lab_beginning_balance` | `IMEXControl.QualityControl.LabBeginningBalance.QCLabBalance` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกเบิก Container | `menu_imex_qc_container_issue` | `IMEXControl.QualityControl.ProductContainerIssue._productContainerIssueControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกปรับปรุง Container | `menu_imex_qc_container_adjustment` | `IMEXControl.QualityControl.ProductContainerAdjustment._productContainerAdjustmentControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › บันทึกการตัดจากระบบ weighing System | `menu_qc_lab_cut` | `IMEXControl.QualityControl.QCLabCut._qcLabCutControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › อนุมัติผู้จำหน่ายและสินค้า | `menu_qc_approved_vendor` | `IMEXControl.QualityControl._approvedVendorControl` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › รายงานการอนุมัติผู้จำหน่ายสินค้า | `report_imex_qc_approved_vendor` | `SMLFastReport._designer` |  |  |
| — | ตรวจสอบคุณภาพสินค้า › Lab Information | `menu_imex_qc_lab_information` | `IMEXControl.QualityControl.QCLatInformation.LabInformation` |  |  |
| 2.11 | สินค้า/วัตถุดิบ คงเหลือยกมา | `menu_ic_stk_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 54 |
| — | ใบสั่งผลิต | `menu_imex_sale_order` | `SMLERPSO._soSaleorder` | _icTransControl | 36 |
| 2.12 | รับสินค้าสำเร็จรูป | `menu_ic_finish_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 60 |
| 2.13 | ขอเบิกสินค้า/วัตถุดิบ | `menu_ic_request_issue` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 122 |
| 2.14 | เบิกสินค้า/วัตถุดิบ | `menu_ic_issue` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 56 |
| 2.15 | รับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 58 |
| 2.16.1 | รายงาน/ยกเลิก › ยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_finish_receive_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 61 |
| 2.16.2 | รายงาน/ยกเลิก › ยกเลิกขอเบิกสินค้า/วัตถุดิบ | `menu_ic_request_issue_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 123 |
| 2.16.3 | รายงาน/ยกเลิก › ยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_issue_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 57 |
| 2.16.4 | รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 59 |
| 2.16.5 | รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_report_cancel_goods_pack` | `SMLERPReportTool._reportTrans` |  | 61 |
| 2.16.6 | รายงาน/ยกเลิก › รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_report_cancel_raw_material` | `SMLERPReportTool._reportTrans` |  | 57 |
| 2.16.7 | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_report_cancel_goods_raw_meterial` | `SMLERPReportTool._reportTrans` |  | 59 |
| 2.16.8 | รายงาน/ยกเลิก › รายงานสินค้าและวัตถุดิบ คงเหลือยกมา | `menu_ic_report_goods_balance` | `SMLERPReportTool._reportTrans` |  | 54 |
| 2.16.9 | รายงาน/ยกเลิก › รายงานการรับสินค้าสำเร็จรูป | `menu_import_item_ready_by_date` | `SMLERPReportTool._reportTrans` |  | 60 |
| 2.16.10 | รายงาน/ยกเลิก › รายงานการเบิกสินค้าและวัตถุดิบ | `menu_ic_report_item_withdraw` | `SMLERPReportTool._reportTrans` |  | 56 |
| 2.16.11 | รายงาน/ยกเลิก › รายงานรับคืนสินค้าและวัตถุดิบ จากการเบิก | `menu_ic_report_item_return` | `SMLERPReportTool._reportTrans` |  | 58 |
| 2.17 | ขอโอนสินค้า/วัตถุดิบ | `menu_ic_request_transfer` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 124 |
| 2.18 | โอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 72 |
| 2.19.1 | ระบบตรวจนับสินค้า › ขอตรวจนับสินค้า | `menu_ic_request_stk_count` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 276 |
| 2.19.2 | ระบบตรวจนับสินค้า › ตรวจนับสินค้า | `menu_ic_stk_count` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 76 |
| 2.19.3 | ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number | `menu_ic_serialnumber_checker` | `SMLERPIC._icSerialStockCheck` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.19.4 | ระบบตรวจนับสินค้า › รายงานผลต่างจากการตรวจนับ | `menu_diff_from_count` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | รายงานผลต่างจากการตรวจนับ |
| 2.19.5 | ระบบตรวจนับสินค้า › รายงานสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ | `menu_stock_no_balance_from_count` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Stock_no_count_no_balance |
| 2.19.6 | ระบบตรวจนับสินค้า › รายงานการตรวจสอบสินค้า Serial | `menu_report_serial_check` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | สินค้า_รายงานการตรวจสอบสินค้า_serial |
| 2.19.7 | ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ | `menu_ic_stk_adjust_auto` | `SMLInventoryControl._stockAutoAdjustControl` |  |  |
| 2.19.8 | ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ (สินค้า Lot) | `menu_ic_stk_adjust_lot_auto` | `SMLInventoryControl._stockAutoAdjustLotControl` | _icInfoProcess |  |
| 2.19.9 | ระบบตรวจนับสินค้า › ปรับปรุงมูลค่าสินค้า Lot คงค้าง | `menu_ic_adjust_stock_lot_amount` | `SMLInventoryControl.StockLotAdjustmentForm` | _icInfoProcess, StockLotAdjustConditionControl, StockLotBalanceAdjustGrid |  |
| 2.20 | ปรับปรุงสต็อกสินค้า/วัตถุดิบ (เพิ่ม) | `menu_ic_stk_adjust` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 66 |
| 2.21 | ปรับปรุงสต็อกสินค้า/วัตถุดิบ (ลด) | `menu_ic_stk_adjust_subtract` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 68 |
| 2.22 | ประมวลผลเฉลี่ยต้นทุนแฝง | `menu_ic_hidden_cost_process` | `SMLERPIC._icHiddenCost._icHiddenCostProcess` |  |  |
| 2.23.1 | รายงาน/ยกเลิก › ยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 73 |
| 2.23.2 | รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_stk_adjust_over_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 67 |
| 2.23.3 | รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_stk_adjust_lost_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 69 |
| 2.23.4 | รายงาน/ยกเลิก › รายงานยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_report_stk_cancel` | `SMLERPReportTool._reportTrans` |  | 73 |
| 2.23.5 | รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_report_stk_cancel_over` | `SMLERPReportTool._reportTrans` |  | 67 |
| 2.23.6 | รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_report_stk_cancel_lost` | `SMLERPReportTool._reportTrans` |  | 69 |
| 2.23.7 | รายงาน/ยกเลิก › รายงานการโอนสินค้าและวัตถุดิบ | `menu_ic_report_item_transfer` | `SMLERPReportTool._reportTrans` |  | 72 |
| 2.23.8 | รายงาน/ยกเลิก › รายงานตรวจนับสินค้า | `menu_ic_report_item_count` | `SMLERPReportTool._reportTrans` |  | 76 |
| 2.23.9 | รายงาน/ยกเลิก › รายงานการปรับปรุงสต็อกสินค้าและวัตถุดิบ (เกิน) | `menu_ic_report_item_adjust_increase` | `SMLERPReportTool._reportTrans` |  | 66 |
| 2.23.10 | รายงาน/ยกเลิก › รายงานการปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) | `menu_ic_report_item_adjust_decrease` | `SMLERPReportTool._reportTrans` |  | 68 |
| 2.24.1 | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้า | `menu_ic_info_stk_balance` | `SMLERPICInfo._stkBalance` | _icBalanceForm, _icInfoProcess, _selectWarehouseAndLocationForm |  |
| 2.24.2 | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามคลัง | `menu_ic_info_stk_balance_warehouse` | `SMLERPICInfo._stkBalanceWareHouse` | _selectWarehouseAndLocationForm |  |
| 2.24.3 | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามที่เก็บ | `menu_ic_info_stk_balance_shelf` | `SMLERPICInfo._stkBalanceLocation` | _selectWarehouseAndLocationForm |  |
| 2.24.4 | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตาม LOT | `menu_ic_info_stk_balance_lot` | `SMLERPICInfo._stkBalanceByLot` | _icInfoProcess |  |
| 2.24.5 | วิเคราะห์ข้อมูล › เคลื่อนไหวสินค้า | `menu_ic_info_stk_move` | `SMLERPICInfo._stkMovement` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.24.6 | วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ | `menu_ic_info_stk_movement` | `SMLERPICInfo._stkMovement` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.24.7 | วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ (รวมต้นทุนแฝง) | `menu_ic_info_stk_movement_hidden` | `SMLERPICInfo._stkMovement` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.24.8 | วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามปริมาณ | `menu_ic_info_stk_movement_sum` | `SMLERPICInfo._stkMovementSum` | _icInfoProcess |  |
| 2.24.9 | วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามมูลค่า | `menu_ic_info_stk_movement_sum_by_amount` | `SMLERPICInfo._stkMovementSum` | _icInfoProcess |  |
| 2.24.10 | วิเคราะห์ข้อมูล › สินค้าถึงจุดสั่งซื้อ | `menu_ic_info_stk_reorder` | `SMLInventoryControl._stkReorder` | _searchDataFull, _stkReorderConditionScreen |  |
| 2.24.11 | วิเคราะห์ข้อมูล › ประวัติการซื้อสินค้า | `menu_ic_info_purchase_history` | `SMLInventoryControl._transHistory` | _searchDataFull, _saleHistoryConditionScreen |  |
| 2.24.12 | วิเคราะห์ข้อมูล › ประวัติการขายสินค้า | `menu_ic_info_sale_history` | `SMLInventoryControl._transHistory` | _searchDataFull, _saleHistoryConditionScreen |  |
| 2.24.13 | วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการเคลื่อนไหว | `menu_ic_info_product_no_movement` | `SMLERPICInfo._stkNoMovement` | _icInfoProcess |  |
| 2.24.14 | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามสินค้า | `menu_ic_info_stk_profit` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.24.15 | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามสินค้า (รวมต้นทุนแฝง) | `menu_ic_info_stk_profit_hidden` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.24.16 | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามเอกสารขาย | `menu_ic_info_stk_profit_by_doc` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.24.17 | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามลูกค้า | `menu_ic_info_stk_profit_by_ar` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.24.18 | วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการขาย | `IC_INVENTORY_NO_SALE` | `SMLFastReport._designer` |  |  |
| 2.24.19 | วิเคราะห์ข้อมูล › ตรวจสอบ Serial มีปัญหา | `menu_ic_serial_analyze` | `SMLERPICInfo._icSerialAnalyze` |  |  |
| 2.24.20 | วิเคราะห์ข้อมูล › รายงานยอดคงเหลือสินค้า (แสดงทุกสินค้า) แสดงมูลค่าปัจจุบัน | `menu_stock_balance_all_show_current_value` | `SMLFastReport._designer` |  |  |
| 2.25.1 | รายงานสรุป › รายงานสถานะสินค้า | `menu_item_status` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_status |
| 2.25.2 | รายงานสรุป › รายงานบัญชีคุมพิเศษสินค้า | `menu_account_special_item` | `SMLERPICReport._report_ic_stk_movement` | _icInfoProcess | สินค้า_รายงานบัญชีคุมพิเศษ |
| 2.25.3 | รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_report_ic_product_and_material` | `SMLERPICReport._report_ic_product_and_material` | _icInfoProcess |  |
| 2.25.4 | รายงานสรุป › รายงานการปรับปรุงสินค้า | `menu_report_inventory_adjust` | `SMLFastReport._designer` |  |  |
| — | รายงานสรุป › รายงานประเมินการรับสินค้า | `menu_span_import_item` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.25.5 | รายงานสรุป › รายงาน Lot สินค้า | `menu_report_lot_inventory` | `SMLFastReport._designer` |  |  |
| — | รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_item_and_staple` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.26.1 | รายงานวิเคราะห์ › รายงานเคลื่อนไหว Serial Number | `menu_ic_serial_number` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Serial_number |
| 2.26.2 | รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างส่ง | `menu_ic_report_sale_remain` | `SMLFastReport._designer` |  |  |
| 2.26.3 | รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างรับ | `menu_report_accrued_in_qty` | `SMLFastReport._designer` |  |  |
| 2.26.4 | รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า | `menu_item_balance` | `SMLERPICReport._report_ic_balance` | _icInfoProcess | สินค้า_รายงานยอดคงเหลือสินค้า |
| 2.26.5 | รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้าตาม LOT | `menu_item_balance_lot` | `SMLERPICReport._report_ic_balance` | _icInfoProcess | สินค้า_รายงานยอดคงเหลือสินค้า_Lot |
| 2.26.6 | รายงานวิเคราะห์ › รายงานสินค้าที่ถึงจุดสั่งซื้อ | `menu_ic_report_info_stk_reorder` | `SMLERPICReport.ic_analysis._report_ic_stk_reorder` | _icInfoProcess | สินค้า_ถึงจุดสั่งซื้อ_ตามสินค้า |
| 2.26.7 | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_max` | `SMLFastReport._designer` |  |  |
| 2.26.8 | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_min` | `SMLFastReport._designer` |  |  |
| 2.26.9 | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_max` | `SMLFastReport._designer` |  |  |
| 2.26.10 | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_min` | `SMLFastReport._designer` |  |  |
| 2.26.11 | รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า ณ ปัจจุบัน(เฉพาะสินค้ามี Serial) | `menu_item_balance_now_only_serial` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_Balance_now_Only_Serial |
| 2.26.12 | รายงานวิเคราะห์ › รายงานสินค้าที่ไม่มีการเคลื่อนไหว | `menu_item_non_transfer` | `SMLERPICReport._report_ic_none_movement` | _icInfoProcess |  |
| 2.26.13 | รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้า | `menu_item_transfer` | `SMLERPICReport._report_ic_stk_movement` | _icInfoProcess | สินค้า_รายงานเคลื่อนไหว |
| 2.26.14 | รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า | `menu_result_transfer_item` | `SMLERPICReport._report_ic_info_stk_movement_sum` | _icInfoProcess |  |
| 2.26.15 | รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า-แสดงมูลค่า | `menu_report_ic_info_stk_movement_sum_show_amount` | `SMLERPICReport._report_ic_info_stk_movement_sum_show_amount` | _icInfoProcess |  |
| 2.26.16 | รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้าต้นทุนมาตรฐาน | `menu_item_transfer_standard` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.27.1 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้นตามเอกสาร (แสดงส่วนลด) | `menu_ic_report_info_stk_profit_by_doc_and_discount` | `SMLERPICReport.ic_analysis._report_info_stk_profit_by_doc_and_discount` |  | สินค้า_รายงานกำไรขั้นต้นตามเอกสารแบบมีส่วนลด |
| 2.27.2 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า) | `menu_ic_report_info_stk_profit` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.3 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.4 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า) | `menu_ic_report_info_stk_profit_ic_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.5 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.6 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร) | `menu_ic_report_info_stk_profit_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.7 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.8 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า) | `menu_ic_report_info_stk_profit_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.9 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า) | `menu_ic_report_info_stk_profit_cust_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.10 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.11 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.27.12 | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_cust_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.28 | คำนวณยอดสต๊อกใหม่ | `menu_ic_recalc` | `SMLERPIC._icRecalc` |  |  |
| 2.29 | บันทึกรูปภาพเอกสาร | `menu_ic_document_picture` | `SMLERPIC._icDocPicture` | _documentPicture |  |
| — | จัดการ LOT สินค้า | `menu_ic_lot_manage` | `SMLERPIC._icLotManage` | _myManageData, _icInfoProcess |  |
| 2.30 | รายงานอื่น ๆ | `menu_fastreport_other_ic` | tag:fastreportother |  |  |

## คลัง (19)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | ยอดคงเหลือยกมา (คลัง) | `menu_wh_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 501 |
| — | รับสินค้าเข้า (คลัง) | `menu_wh_in_purchase` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 503 |
| — | ส่งคืนสินค้า (คลัง) | `menu_wh_in_ret` | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | จ่ายสินค้าออก (คลัง) | `menu_wh_out` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 505 |
| — | รับคืนสินค้า (คลัง) | `menu_wh_out_ret` | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | โอนย้ายสินค้าออก (คลัง) | `menu_wh_trans_out` | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | โอนย้ายสินค้าเข้า (คลัง) | `menu_wh_trans_in` | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ตรวจนับสินค้า (คลัง) | `menu_wh_stk_count` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 502 |
| — | ปรับปรุงเพิ่มลดสินค้า (คลัง) | `menu_wh_adj` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 509 |
| — | รายงาน (คลัง) › ยอดคงเหลือยกมา (คลัง) | `menu_wh_report_balance` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › รับสินค้าเข้า (คลัง) | `menu_wh_report_in` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › ส่งคืนสืนค้า (คลัง) | `menu_wh_report_in_ret` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › จ่ายสินค้าออก (คลัง) | `menu_wh_report_out` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › รับคืนสินค้า (คลัง) | `menu_wh_report_out_ret` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › โอนย้ายสินค้าออก (คลัง) | `menu_wh_report_trans_out` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › โอนย้ายสินค้าเข้า (คลัง) | `menu_wh_report_trans_in` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | รายงาน (คลัง) › รายงานตรวจนับสินค้า (คลัง) | `menu_wh_report_item_count` | `SMLERPReportTool._reportTrans` |  | 502 |
| — | รายงาน (คลัง) › ปรับปรุงเพิ่มลดสินค้า (คลัง) | `menu_wh_report_adj` | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | บันทึกการส่งสินค้า | `menu_ic_shipping` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 701 |

## ซื้อ (77)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 3.1 | ใบเสนอซื้อ | `menu_purchase_requisition` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 2 |
| 3.2 | อนุมัติใบเสนอซื้อ | `menu_purchase_requisition_approval` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 4 |
| 3.3.1 | รายงาน/ยกเลิก › ยกเลิกใบเสนอซื้อ | `menu_cancel_purchase_requisition` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 3 |
| 3.3.2 | รายงาน/ยกเลิก › รายงานใบเสนอซื้อ | `menu_po_report_record_requisition_purchase` | `SMLERPReportTool._reportTrans` |  | 2 |
| 3.3.3 | รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอซื้อ | `menu_po_report_requisition_purchase1` | `SMLERPReportTool._reportTrans` |  | 4 |
| 3.3.4 | รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอซื้อ | `menu_po_report_requisition_cancel` | tag:poreport (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 3.3.5 | รายงาน/ยกเลิก › รายงานสถานะใบเสนอซื้อ | `menu_po_report_requisition_purchase` | `SMLERPReportTool._reportTrans` |  | 2 |
| 3.4 | ใบสั่งซื้อ | `menu_po_purchase_order` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 6 |
| 3.5 | อนุมัติใบสั่งซื้อ | `menu_po_purchase_order_approve` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 8 |
| 3.6.1 | รายงาน/ยกเลิก › ยกเลิกใบสั่งซื้อ | `menu_po_purchase_order_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 7 |
| 3.6.2 | รายงาน/ยกเลิก › รายงานบันทึกใบสั่งซื้อ | `menu_po_report_purchase_order` | `SMLERPReportTool._reportTrans` |  | 6 |
| 3.6.3 | รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ | `menu_po_report_purchase_order_approve` | `SMLERPReportTool._reportTrans` |  | 8 |
| 3.6.4 | รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ | `menu_po_report_purchase_order_cancel` | `SMLERPReportTool._reportTrans` |  | 7 |
| 3.6.5 | รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ | `menu_po_report_purchase_order_status` | `SMLERPReportTool._reportTrans` |  | 6 |
| 3.6.6 | รายงาน/ยกเลิก › รายงานค้างรับสินค้าตามใบสั่งซื้อ | `menu_po_hold_receive_by_doc` | `SMLERPReportTool._reportTrans` |  | 6 |
| 3.7 | จ่ายเงินล่วงหน้ายกมา | `menu_po_advance_payment_balance` | `SMLERPPO._po_advance_money_balance` |  |  |
| 3.8 | จ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1` | `SMLERPPO._po_advance_money` | _formSaleOrderPreview |  |
| 3.9 | รับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1` | `SMLERPPO._po_advance_money_return` | _formSaleOrderPreview |  |
| 3.10.1 | รายงาน/ยกเลิก › ยกเลิกจ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 150 |
| 3.10.2 | รายงาน/ยกเลิก › ยกเลิกรับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 161 |
| 3.10.3 | รายงาน/ยกเลิก › รายงานบันทึกการจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.10.4 | รายงาน/ยกเลิก › รายงานบันทึกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return` | `SMLERPReportTool._reportTrans` |  | 20 |
| 3.10.5 | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 150 |
| 3.10.6 | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 161 |
| 3.10.7 | รายงาน/ยกเลิก › รายงานยอดคงเหลือจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.10.8 | รายงาน/ยกเลิก › รายงานการตัดจ่ายเงินล่วงหน้า | `menu_po_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.11 | จ่ายเงินมัดจำยกมา | `menu_po_deposit_money_balance` | `SMLERPPO._po_deposit_money_balance` |  |  |
| 3.12 | จ่ายเงินมัดจำ | `menu_po_deposit_payment_2` | `SMLERPPO._po_deposit_money` |  |  |
| 3.13 | รับคืนจ่ายเงินมัดจำ | `menu_po_deposit_return_2` | `SMLERPPO._po_deposit_money_return` |  |  |
| 3.14.1 | รายงาน/ยกเลิก › ยกเลิกจ่ายเงินมัดจำ | `menu_po_deposit_payment_2_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 151 |
| 3.14.2 | รายงาน/ยกเลิก › ยกเลิกรับคืนจ่ายเงินมัดจำ | `menu_po_deposit_return_2_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 152 |
| 3.14.3 | รายงาน/ยกเลิก › รายงานจ่ายเงินมัดจำ | `menu_po_report_advance_payment` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.14.4 | รายงาน/ยกเลิก › รายงานรับคืนเงินมัดจำ | `menu_po_report_advance_payment_return` | `SMLERPReportTool._reportTrans` |  | 25 |
| 3.14.5 | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินมัดจำ | `menu_po_report_advance_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 151 |
| 3.14.6 | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_po_report_advance_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 152 |
| 3.14.7 | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_po_report_deposit_payment_2_remain` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.14.8 | รายงาน/ยกเลิก › รายงานการตัดใบจ่ายเงินมัดจำ | `menu_po_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.15 | ซื้อสินค้า/ตั้งหนี้ | `menu_po_purchase_billing` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 12 |
| 3.16 | เพิ่มหนี้/ราคาผิด | `menu_po_addition_debt` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 14 |
| 3.17 | ส่งคืนสินค้า/ราคาผิด | `menu_po_credit_note` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 16 |
| 3.18.1 | ซื้อสินค้าแบบทะยอยรับ › รับสินค้า | `menu_po_purchase_partial_item` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 310 |
| 3.18.2 | ซื้อสินค้าแบบทะยอยรับ › ส่งคืนสินค้า/ราคาผิด | `menu_po_purchase_partial_item_debit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 311 |
| 3.18.3 | ซื้อสินค้าแบบทะยอยรับ › ตั้งหนี้จากการรับสินค้า | `menu_po_purchase_partial_1` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 315 |
| 3.18.4 | ซื้อสินค้าแบบทะยอยรับ › เพิ่มหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_3` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 316 |
| 3.18.5 | ซื้อสินค้าแบบทะยอยรับ › ลดหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_2` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 317 |
| 3.18.6 | ซื้อสินค้าแบบทะยอยรับ › ยกเลิกรับสินค้า | `menu_po_purchase_partial_item_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 330 |
| 3.18.7 | ซื้อสินค้าแบบทะยอยรับ › ยกเลิกส่งคืนสินค้า/ราคาผิด | `menu_po_purchase_partial_item_debit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 331 |
| 3.18.8 | ซื้อสินค้าแบบทะยอยรับ › ยกเลิกตั้งหนี้จากการรับสินค้า | `menu_po_purchase_partial_1_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 335 |
| 3.18.9 | ซื้อสินค้าแบบทะยอยรับ › ยกเลิกลดหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_2_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 337 |
| 3.18.10 | ซื้อสินค้าแบบทะยอยรับ › ยกเลิกเพิ่มหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_3_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 1 |
| 3.18.11 | ซื้อสินค้าแบบทะยอยรับ › รายงานรับสินค้า | `menu_po_report_purchase_partial` | `SMLERPReportTool._reportTrans` |  | 310 |
| 3.18.12 | ซื้อสินค้าแบบทะยอยรับ › รายงานส่งคืนสินค้า/ราคาผิด | `menu_po_report_purchase_partial_debit` | `SMLERPReportTool._reportTrans` |  | 311 |
| 3.18.13 | ซื้อสินค้าแบบทะยอยรับ › รายงานตั้งหนี้จากการรับสินค้า | `menu_po_report_purchase_partial_1` | `SMLERPReportTool._reportTrans` |  | 315 |
| 3.18.14 | ซื้อสินค้าแบบทะยอยรับ › รายงานเพิ่มหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_2` | `SMLERPReportTool._reportTrans` |  | 316 |
| 3.18.15 | ซื้อสินค้าแบบทะยอยรับ › รายงานลดหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_3` | `SMLERPReportTool._reportTrans` |  | 317 |
| 3.19.1 | รายงาน/ยกเลิก › ยกเลิกซื้อสินค้า | `menu_po_purchase_billing_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 13 |
| 3.19.2 | รายงาน/ยกเลิก › ยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 17 |
| 3.19.3 | รายงาน/ยกเลิก › ยกเลิกซื้อเพิ่มสินค้า/เพิ่มหนี้ | `menu_po_addition_debt_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 15 |
| 3.19.4 | รายงาน/ยกเลิก › รายงานการซื้อสินค้า/ตั้งหนี้ | `menu_po_report_purchase` | `SMLERPReportTool._reportTrans` |  | 12 |
| 3.19.5 | รายงาน/ยกเลิก › รายงานการส่งคืนสินค้า/ลดหนี้ | `menu_po_report_credit_note` | `SMLERPReportTool._reportTrans` |  | 16 |
| 3.19.6 | รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods` | `SMLERPReportTool._reportTrans` |  | 14 |
| 3.19.7 | รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้า/ตั้งหนี้ | `menu_po_report_purchase_cancel` | `SMLERPReportTool._reportTrans` |  | 13 |
| 3.19.8 | รายงาน/ยกเลิก › รายงานยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel_report` | `SMLERPReportTool._reportTrans` |  | 17 |
| 3.19.9 | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` |  | 15 |
| 3.20.1 | รายงานสรุป › รายงานซื้อสินค้าแยกตามสินค้า | `menu_po_recive_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` |  | ซื้อ_รายงานซื้อสินค้าแยกตามสินค้า |
| 3.20.2 | รายงานสรุป › รายงานยอดซื้อ(ตามวันที่) | `menu_report_purchase_by_date` | `SMLFastReport._designer` |  |  |
| 3.20.3 | รายงานสรุป › รายงานการซื้อสินค้าสรุปตามประเภทภาษี | `menu_report_sum_purchase_by_vat` | `SMLFastReport._designer` |  |  |
| 3.20.4 | รายงานสรุป › รายงานใบตั้งหนี้จากการซื้อแบบสรุป-ตามวันที่ | `menu_report_purchase_credit_by_date` | `SMLFastReport._designer` |  |  |
| 3.20.5 | รายงานสรุป › รายงานการสั่งซื้อสินค้าแบบสรุป-ตามวันที่ | `menu_report_purchase_order_by_date` | `SMLFastReport._designer` |  |  |
| 3.20.6 | รายงานสรุป › รายงานใบเพิ่มสินค้า(เจ้าหนี้)แบบสรุป-ตามสินค้า | `menu_report_purchase_add_by_date` | `SMLFastReport._designer` |  |  |
| 3.20.7 | รายงานสรุป › รายงานการส่งคืนสินค้า/ลดหนี้แบบสรุป-ตามสินค้า | `menu_report_purchase_credit_note_by_item` | `SMLFastReport._designer` |  |  |
| 3.20.8 | รายงานสรุป › รายงานใบซื้อสินค้าที่ถึงกำหนดจ่ายเงิน | `menu_report_purchse_on_due` | `SMLFastReport._designer` |  |  |
| 3.21.1 | รายงานวิเคราะห์ › รายงานการจัดอันดับยอดซื้อ(ตามสินค้า-กลุ่มสินค้า) | `menu_report_purchase_rank_item_group` | `SMLFastReport._designer` |  |  |
| 3.21.2 | รายงานวิเคราะห์ › รายงานวิเคราะห์การซื้อสุทธิ-ตามสินค้า | `menu_po_report_purchase_analyze` | `SMLFastReport._designer` |  |  |
| 3.21.3 | รายงานวิเคราะห์ › รายงานเปรียบเทียบยอดซื้อสินค้า12เดือน(ตามสินค้า-ราคา/ปริมาณ) | `menu_po_report_compare_purchase_monthly` | `SMLFastReport._designer` |  |  |
| 3.22 | บันทึกรูปภาพเอกสาร | `menu_po_doc_picture` | `SMLERPPO._po_docPicture` | _documentPicture |  |
| 3.23 | รายงานอื่น ๆ | `menu_fastreport_other_purchase` | tag:fastreportother |  |  |

## ขาย (75)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 4.1 | ใบเสนอราคา | `menu_so_quotation_order` | `SMLERPSO._soQuotation` | _icTransControl | 30 |
| 4.2 | อนุมัติใบเสนอราคา | `menu_so_quotation_approve` | `SMLERPSO._soQuotationApproval` | _icTransControl | 32 |
| 4.3.1 | รายงาน/ยกเลิก › ยกเลิกใบเสนอราคา | `menu_so_quotation_cancel` | `SMLERPSO._soQuotationCancel` | _icTransControl | 31 |
| 4.3.2 | รายงาน/ยกเลิก › รายงานบันทึกใบเสนอราคา | `menu_so_report_quotation` | `SMLERPReportTool._reportTrans` |  | 30 |
| 4.3.3 | รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอราคา | `menu_so_report_quotation_approve` | `SMLERPReportTool._reportTrans` |  | 32 |
| 4.3.4 | รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอราคา | `menu_so_report_quotation_cancel` | `SMLERPReportTool._reportTrans` |  | 31 |
| 4.3.5 | รายงาน/ยกเลิก › รายงานสถานะใบเสนอราคา | `menu_so_report_quotation_stat` | `SMLERPReportTool._reportTrans` |  | 30 |
| 4.4 | ใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order` | `SMLERPSO._soReserved` | _icTransControl | 34 |
| 4.5 | อนุมัติใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order_approve` | `SMLERPSO._soReservedApproval` | _icTransControl | 38 |
| 4.6.1 | รายงาน/ยกเลิก › ยกเลิกใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order_cancel` | `SMLERPSO._soReservedCancel` | _icTransControl | 39 |
| 4.6.2 | รายงาน/ยกเลิก › รายงานใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry` | `SMLERPReportTool._reportTrans` |  | 34 |
| 4.6.3 | รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_approve` | `SMLERPReportTool._reportTrans` |  | 38 |
| 4.6.4 | รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_cancel` | `SMLERPReportTool._reportTrans` |  | 39 |
| 4.6.5 | รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_stat` | `SMLERPReportTool._reportTrans` |  | 34 |
| 4.7 | บันทึกใบสั่งขาย | `menu_so_sale_order` | `SMLERPSO._soSaleorder` | _icTransControl | 36 |
| 4.8 | อนุมัติใบสั่งขาย | `menu_so_sale_order_approve` | `SMLERPSO._soSaleorderApproval` | _icTransControl | 52 |
| 4.9.1 | รายงาน/ยกเลิก › ยกเลิกใบสั่งขาย | `menu_so_sale_order_cancel` | `SMLERPSO._soSaleorderCancel` | _icTransControl | 37 |
| 4.9.2 | รายงาน/ยกเลิก › รายงานใบสั่งขาย | `menu_so_report_sale_order` | `SMLERPReportTool._reportTrans` |  | 36 |
| 4.9.3 | รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งขาย | `menu_so_report_sale_order_approve` | `SMLERPReportTool._reportTrans` |  | 52 |
| 4.9.4 | รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งขาย | `menu_so_report_sale_order_cancel` | `SMLERPReportTool._reportTrans` |  | 37 |
| 4.9.5 | รายงาน/ยกเลิก › รายงานสถานะใบสั่งขาย | `menu_so_report_sale_order_stat` | `SMLERPReportTool._reportTrans` |  | 36 |
| 4.10 | รับเงินล่วงหน้ายกมา | `menu_so_advance_money_balance` | `SMLERPSO._so_advance_money_balance` |  |  |
| 4.11 | รับเงินล่วงหน้า | `menu_so_deposit_receive_1` | `SMLERPSO._so_advance_money` | _formSaleOrderPreview |  |
| 4.12 | คืนเงินรับล่วงหน้า | `menu_so_deposit_return_1` | `SMLERPSO._so_advance_money_return` | _formSaleOrderPreview |  |
| 4.13.1 | รายงาน/ยกเลิก › ยกเลิกรับเงินล่วงหน้า | `menu_so_deposit_receive_1_cancel` | `SMLERPSO._so_advance_money_cancel` | _icTransControl | 41 |
| 4.13.2 | รายงาน/ยกเลิก › ยกเลิกคืนเงินรับล่วงหน้า | `menu_so_deposit_return_1_cancel` | `SMLERPSO._so_advance_money_return_cancel` | _icTransControl | 43 |
| 4.13.3 | รายงาน/ยกเลิก › รายงานรับเงินล่วงหน้า | `menu_so_report_deposit_receive` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.13.4 | รายงาน/ยกเลิก › รายงานคืนเงินรับล่วงหน้า | `menu_so_report_deposit_return` | `SMLERPReportTool._reportTrans` |  | 42 |
| 4.13.5 | รายงาน/ยกเลิก › รายงานยกเลิกรับเงินล่วงหน้า | `menu_so_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 41 |
| 4.13.6 | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินรับล่วงหน้า | `menu_so_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 43 |
| 4.13.7 | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินรับล่วงหน้า | `menu_so_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.13.8 | รายงาน/ยกเลิก › รายงานการตัดเงินรับล่วงหน้า | `menu_so_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.14 | รับเงินมัดจำยกมา | `menu_so_deposit_money_balance` | `SMLERPSO._so_deposit_money_balance` |  |  |
| 4.15 | รับเงินมัดจำ | `menu_so_deposit_receive_2` | `SMLERPSO._so_deposit_money` |  |  |
| 4.16 | คืนเงินมัดจำ | `menu_so_deposit_return_2` | `SMLERPSO._so_deposit_money_return` |  |  |
| 4.17.1 | รายงาน/ยกเลิก › ยกเลิกรับเงินมัดจำ | `menu_so_deposit_receive_2_cancel` | `SMLERPSO._so_deposit_money_cancel` | _icTransControl | 111 |
| 4.17.2 | รายงาน/ยกเลิก › ยกเลิกคืนเงินมัดจำ | `menu_so_deposit_return_2_cancel` | `SMLERPSO._so_deposit_money_return_cancel` | _icTransControl | 113 |
| 4.17.3 | รายงาน/ยกเลิก › รายงานรับเงินมัดจำ | `menu_so_report_deposit_receive_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.17.4 | รายงาน/ยกเลิก › รายงานคืนเงินมัดจำ | `menu_so_report_deposit_return_2` | `SMLERPReportTool._reportTrans` |  | 112 |
| 4.17.5 | รายงาน/ยกเลิก › รายงานยกเลิกรับเงินมัดจำ | `menu_so_report_deposit_payment_cancel_2` | `SMLERPReportTool._reportTrans` |  | 111 |
| 4.17.6 | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_so_report_deposit_payment_return_cancel_2` | `SMLERPReportTool._reportTrans` |  | 113 |
| 4.17.7 | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_so_report_deposit_payment_remain_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.17.8 | รายงาน/ยกเลิก › รายงานการตัดเงินมัดจำ | `menu_so_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.18 | ขายสินค้า/บริการ | `menu_so_invoice` | `SMLERPSO._soInvoice` | _icTransControl | 44 |
| 4.19 | รับคืนสินค้า/ลดหนี้ | `menu_so_credit_note` | `SMLERPSO._creditNote` | _icTransControl | 48 |
| 4.20 | เพิ่มหนี้ | `menu_so_invoice_add` | `SMLERPSO._soInvoiceAdd` | _icTransControl | 46 |
| 4.21 | ส่งข้อมูล e-Tax | `menu_so_send_etax` | `SMLETaxInvoice._sendETaxControl` |  |  |
| 4.22.1 | รายงาน/ยกเลิก › ยกเลิกขายสินค้า/บริการ | `menu_so_invoice_cancel` | `SMLERPSO._soInvoiceCancel` | _icTransControl | 45 |
| 4.22.2 | รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_credit_note_cancel` | `SMLERPSO._creditNoteCancel` | _icTransControl | 49 |
| 4.22.3 | รายงาน/ยกเลิก › ยกเลิกขายเพิ่มสินค้า/เพิ่มหนี้ | `menu_so_invoice_add_cancel` | `SMLERPSO._soInvoiceAddCancel` | _icTransControl | 47 |
| 4.22.4 | รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ | `menu_so_report_invoice` | `SMLERPReportTool._reportTrans` |  | 44 |
| 4.22.5 | รายงาน/ยกเลิก › รายงานการขายและบริการเรียงตามสินค้า | `menu_so_sale_service_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` |  | ขาย_รายงานขายสินค้าแยกตามสินค้า |
| 4.22.6 | รายงาน/ยกเลิก › รายงานการรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note` | `SMLERPReportTool._reportTrans` |  | 48 |
| 4.22.7 | รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods` | `SMLERPReportTool._reportTrans` |  | 46 |
| 4.22.8 | รายงาน/ยกเลิก › รายงานยกเลิกขายสินค้าและบริการ | `menu_so_report_invoice_cancel` | `SMLERPReportTool._reportTrans` |  | 45 |
| 4.22.9 | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note_cancel` | `SMLERPReportTool._reportTrans` |  | 49 |
| 4.22.10 | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` |  | 47 |
| 4.23.1 | รายงานสรุป › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_sell_by_sale` | `SMLERPSOReport._report_summary._report_sell_by_sale` |  | สินค้า_sell_by_sale |
| 4.23.2 | รายงานสรุป › รายงานสรุปยอดขายสินค้าสุทธิตามพนักงานขาย | `menu_fast_report_summary_sell_by_sale` | `SMLFastReport._designer` |  |  |
| 4.23.3 | รายงานสรุป › รายงานสรุปยอดขายสินค้า-สรุปตามวันที่ | `menu_shipments_by_date` | `SMLFastReport._designer` |  |  |
| 4.23.4 | รายงานสรุป › รายงานประวัติการขายสินค้า | `menu_sale_history_product` | `SMLFastReport._designer` |  |  |
| 4.23.5 | รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.8) | `menu_so_report_sale_drug_by_lot` | `SMLERPSOReport._report_drug_sale_8` | _searchDataFull, _icInfoProcess |  |
| 4.23.6 | รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.13) | `menu_so_report_sale_drug_13` | `SMLERPSOReport._report_sale_drug_13` | _searchDataFull, _icInfoProcess |  |
| 4.23.7 | รายงานสรุป › บัญชีการผลิตยาและขายยาที่ผลิต (แบบ ผ.ย. ๕) | `menu_so_report_sale_drug_by_lot_5` | `SMLERPSOReport._report_drug_sale_8` | _searchDataFull, _icInfoProcess |  |
| 4.23.8 | รายงานสรุป › รายงานเรียกเก็บยาคืน (Recall) | `menu_so_report_sale_recall` | `SMLERPSOReport._report_sale_drug_recall` | _searchDataFull, _icInfoProcess |  |
| 4.24.1 | รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบแจกแจง-ตามสินค้า | `menu_fast_report_analysis_sell_ex_by_product` | `SMLFastReport._designer` |  |  |
| 4.24.2 | รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบสรุป-ตามเอกสาร | `menu_fast_report_analysis_sell_sum_by_docno` | `SMLFastReport._designer` |  |  |
| 4.24.3 | รายงานวิเคราะห์ › รายงานกำไรขั้นต้นแสดงหักรับคืน | `menu_fast_report_margin_reacceptance` | `SMLFastReport._designer` |  |  |
| 4.24.4 | รายงานวิเคราะห์ › รายงานจัดอันดับยอดขาย-ตามสินค้า | `menu_fast_report_product_rank` | `SMLFastReport._designer` |  |  |
| 4.24.5 | รายงานวิเคราะห์ › รายงานเปรียบเที่ยบยอดสินค้า12 เดือน | `menu_fast_report_shipments_compare_month` | `SMLFastReport._designer` |  |  |
| 4.24.6 | รายงานวิเคราะห์ › รายงานการเทียบการขายกับราคาขาย | `menu_compare_sale_with_price` | `SMLFastReport._designer` |  |  |
| 4.24.7 | รายงานวิเคราะห์ › รายงานสินค้าขายต่ำกว่าทุน | `menu_product_sale_loss` | `SMLFastReport._designer` |  |  |
| — | รายงานวิเคราะห์ › รายงานสินค้า ขายประจำเดือน | `menu_report_product_sale_monthly` | `IMEXControl.report.report_product_sale_monthly` |  |  |
| 4.25 | บันทึกรูปภาพเอกสาร | `menu_so_doc_picture` | `SMLERPSO._so_docPicture` | _documentPicture |  |
| 4.26 | รายงานอื่น ๆ | `menu_fastreport_other_sale` | tag:fastreportother |  |  |

## ขาย POS (35)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 5.1 AccPOS/AccPOSPro | หน้าจอขาย POS | `menu_pos_screen` | `StreamReader` |  |  |
| 5.2 AccPOS/AccPOSPro | รายละเอียดคูปอง | `menu_coupon_list` | `SMLERPControl._coupon._couponList` |  |  |
| 5.3 AccPOS/AccPOSPro | สร้างคูปองแบบเร็ว | `menu_coupon_generate` | `SMLERPControl._coupon._couponGenerate` | _myManageData |  |
| 5.4 AccPOS/AccPOSPro | บันทึกรับเงิน (เงินทอน) | `menu_save_pos_receive_money` | `SMLPosClient._posSaveMoneyReceive` | _myManageData |  |
| 5.5 AccPOS/AccPOSPro | บันทึกส่งเงิน POS | `menu_save_send_money_pos` | `SMLPosClient._posSaveSendMoney` | _myManageData |  |
| 5.6 AccPOS/AccPOSPro | รายการใบกำกับภาษีอย่างย่อ | `pos_invoice_list_pos` | `SMLERPSO._soInvoice` | _icTransControl | 44 |
| 5.7 AccPOS/AccPOSPro | รายการใบกำกับภาษีอย่างเต็มออกแทน | `pos_full_invoide_list_pos` | `SMLERPSO._soFullInvoice` | _icTransControl | 144 |
| 5.8 AccPOS/AccPOSPro | รายการใบกำกับภาษีอย่างย่อยกเลิก | `pos_invoice_cancel_pos` | `SMLERPSO._soInvoiceCancel` | _icTransControl | 45 |
| 5.9.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการรับเงิน | `menu_fastreport_received_money` | `SMLFastReport._designer` |  |  |
| 5.9.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการนำส่งเงินประจำวัน | `report_send_money_pos` | `SMLFastReport._designer` |  |  |
| 5.9.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างเต็มออกแทน | `menu_so_report_pos_full_invoice` | `SMLERPReportTool._reportTrans` |  | 144 |
| 5.9.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างย่อ | `menu_pos_sum_short_vat` | `SMLFastReport._designer` |  |  |
| 5.9.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างย่อยกเลิก | `menu_fastreport_invoice_cancel` | `SMLFastReport._designer` |  |  |
| 5.9.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานสรุปการขายหน้าร้าน | `menu_pos_sum_front` | `SMLFastReport._designer` |  |  |
| 5.9.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างเต็ม | `menu_pos_sum_full_vat` | `SMLFastReport._designer` |  |  |
| 5.9.8.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามวันที่ | `menu_pos_sale_detail_001` | `SMLFastReport._designer` |  |  |
| 5.9.8.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามลูกค้า | `menu_pos_sale_detail_002` | `SMLFastReport._designer` |  |  |
| 5.9.8.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแคชเชียร์ | `menu_pos_sale_detail_008` | `SMLFastReport._designer` |  |  |
| 5.9.8.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามยี่ห้อสินค้า | `menu_pos_sale_detail_004` | `SMLFastReport._designer` |  |  |
| 5.9.8.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามพนักงาน | `menu_pos_sale_detail_005` | `SMLFastReport._designer` |  |  |
| 5.9.8.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแผนก | `menu_pos_sale_detail_006` | `SMLFastReport._designer` |  |  |
| 5.9.8.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มสินค้า | `menu_pos_sale_detail_009` | `SMLFastReport._designer` |  |  |
| 5.9.8.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามประเภทลูกค้า | `menu_pos_sale_detail_007` | `SMLFastReport._designer` |  |  |
| 5.9.8.9 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มลูกค้า | `menu_pos_sale_detail_010` | `SMLFastReport._designer` |  |  |
| 5.9.8.10 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามรหัส | `menu_pos_sale_detail_003` | `SMLFastReport._designer` |  |  |
| 5.9.8.11 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรีบงตามรหัส (แสดง Serial) | `menu_report_pos_sale_sugest_by_item_and_serial` | `SMLFastReport._designer` |  |  |
| 5.9.9.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามยี่ห้อสินค้า | `menu_pos_sumary_004` | `SMLFastReport._designer` |  |  |
| 5.9.9.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มลูกค้า | `menu_pos_sumary_009` | `SMLFastReport._designer` |  |  |
| 5.9.9.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามวันที่ | `menu_pos_sumary_002` | `SMLFastReport._designer` |  |  |
| 5.9.9.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มสินค้า | `menu_pos_sumary_008` | `SMLFastReport._designer` |  |  |
| 5.9.9.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-เรียงตามแคชเชียร์ | `menu_pos_sumary_001` | `SMLFastReport._designer` |  |  |
| 5.9.9.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย | `menu_pos_sumary_005` | `SMLFastReport._designer` |  |  |
| 5.9.9.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า | `menu_pos_sumary_003` | `SMLFastReport._designer` |  |  |
| 5.9.9.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามประเภทลูกค้า | `menu_pos_sumary_007` | `SMLFastReport._designer` |  |  |
| 5.10 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_sale_pos` | tag:fastreportother |  |  |

## เจ้าหนี้ (54)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 5.1.1 Acc/Pro · 6.1.1 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › กำหนดเจ้าหนี้ | `menu_ap_detail` | `SMLERPAP._ap` |  |  |
| 5.1.2 Acc/Pro · 6.1.2 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › รายละเอียดเจ้าหนี้ | `menu_ap_detail_2` | `SMLERPAP._ap_detail` |  |  |
| — | ข้อมูลเจ้าหนี้ › บันทึกเอกสารอ้างอิง | `menu_ap_reference` | tag:ap (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 5.1.3 Acc/Pro · 6.1.3 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 5.1.4 Acc/Pro · 6.1.4 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 5.1.5 Acc/Pro · 6.1.5 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › นำเข้าที่อยู่จัดส่งเจ้าหนี้ | `menu_import_ap_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 5.1.6 Acc/Pro · 6.1.6 AccPOS/AccPOSPro | ข้อมูลเจ้าหนี้ › รายงานรายละเอียดเจ้าหนี้ | `menu_ap_report_detail_ap` | `SMLERPReportTool._reportCustMaster` |  | เจ้าหนี้_รายละเอียด |
| 5.2 Acc/Pro · 6.2 AccPOS/AccPOSPro | ตั้งหนี้ยกมา (เจ้าหนี้) | `menu_ap_debt_balance` | `SMLERPAP._ap_debt_balance` | _ar_ap_trans | 81 |
| 5.3 Acc/Pro · 6.3 AccPOS/AccPOSPro | ลดหนี้ยกมา (เจ้าหนี้) | `menu_ap_cn_balance` | `SMLERPAP._ap_cn_balance` | _ar_ap_trans | 85 |
| 5.4 Acc/Pro · 6.4 AccPOS/AccPOSPro | เพิ่มหนี้ยกมา (เจ้าหนี้) | `menu_ap_increase_debt` | `SMLERPAP._ap_increase_debt` | _ar_ap_trans | 83 |
| 5.5.1 Acc/Pro · 6.5.1 AccPOS/AccPOSPro | รายงาน › รายงานตั้งหนี้ยกมา | `menu_ap_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` |  | 81 |
| 5.5.2 Acc/Pro · 6.5.2 AccPOS/AccPOSPro | รายงาน › รายงานลดหนี้ยกมา | `menu_ap_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` |  | 85 |
| 5.5.3 Acc/Pro · 6.5.3 AccPOS/AccPOSPro | รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ap_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` |  | 83 |
| 5.6.1 Acc/Pro · 6.6.1 AccPOS/AccPOSPro | คู่ค้า › ข้อมูลคู่ค้า | `menu_ap_partner_detail` | `SMLERPAP.ap_supplier_connected` |  |  |
| — | คู่ค้า › นำเข้าข้อมูลจากคู่ค้า | `menu_ap_partner_import` | `SMLERPAP._apPartnerBillImport` | _searchDataFull, _icTransScreenTopControl |  |
| — | คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) | `menu_ap_partner_import_return_product` | `SMLERPAP._apPartnerBillImportReturnProduct` | _searchDataFull, _icTransScreenTopControl |  |
| — | คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้) | `menu_ap_partner_import_add_debt` | `SMLERPAP._apPartnerBillImportAddDebt` | _searchDataFull, _icTransScreenTopControl |  |
| 5.7 Acc/Pro · 6.7 AccPOS/AccPOSPro | ตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 87 |
| 5.8 Acc/Pro · 6.8 AccPOS/AccPOSPro | ลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 91 |
| 5.9 Acc/Pro · 6.9 AccPOS/AccPOSPro | เพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 89 |
| 5.10.1 Acc/Pro · 6.10.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_debt_balance_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 88 |
| 5.10.2 Acc/Pro · 6.10.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 92 |
| 5.10.3 Acc/Pro · 6.10.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 90 |
| 5.10.4 Acc/Pro · 6.10.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 87 |
| 5.10.5 Acc/Pro · 6.10.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 89 |
| 5.10.6 Acc/Pro · 6.10.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 91 |
| 5.10.7 Acc/Pro · 6.10.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_cancel_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 88 |
| 5.10.8 Acc/Pro · 6.10.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_cancel_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 90 |
| 5.10.9 Acc/Pro · 6.10.9 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_cancel_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 92 |
| 5.11 Acc/Pro · 6.11 AccPOS/AccPOSPro | ใบรับวางบิล (เจ้าหนี้) | `menu_ap_pay_bill` | `SMLERPAP._ap_pay_bill` | _ar_ap_trans, _formSaleOrderPreview | 213 |
| 5.12 Acc/Pro · 6.12 AccPOS/AccPOSPro | จ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_debt_billing` | `SMLERPAP._ap_debt_billing` | _ar_ap_trans, _formSaleOrderPreview | 19 |
| 5.13.1 Acc/Pro · 6.13.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกใบรับวางบิล (เจ้าหนี้) | `menu_ap_cancel_pay_bill` | `SMLERPAP._ap_cancel_pay_bill` | _ar_ap_trans | 214 |
| 5.13.2 Acc/Pro · 6.13.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_cancel_debt_billing` | `SMLERPAP._ap_cancel_debt_billing` | _ar_ap_trans | 23 |
| 5.13.3 Acc/Pro · 6.13.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) | `menu_ap_report_cancel_pay_bill` | `SMLERPReportTool._reportArApTrans` |  | 214 |
| 5.13.4 Acc/Pro · 6.13.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) | `menu_ap_report_cancel_debt_billing` | `SMLERPReportTool._reportArApTrans` |  | 23 |
| 5.13.5 Acc/Pro · 6.13.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบรับวางบิล (เจ้าหนี้) | `menu_ap_report_billing` | `SMLERPReportTool._reportArApTrans` |  | 213 |
| 5.13.6 Acc/Pro · 6.13.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้า-ตามใบส่งของ | `menu_billing_value_by_invoice` | `SMLFastReport._designer` |  |  |
| 5.13.7 Acc/Pro · 6.13.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้าที่คงค้าง | `menu_billing_outstanding` | `SMLFastReport._designer` |  |  |
| 5.13.8 Acc/Pro · 6.13.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_report_payment` | `SMLERPReportTool._reportArApTrans` |  | 19 |
| 5.14.1 Acc/Pro · 6.14.1 AccPOS/AccPOSPro | รายงานสรุป › รายงานใบส่งของค้างจ่ายชำระ-ตามวันที่ | `menu_invoice_arrears_by_date` | `SMLFastReport._designer` |  |  |
| 5.14.2 Acc/Pro · 6.14.2 AccPOS/AccPOSPro | รายงานสรุป › รายงานใบส่งของถึงกำหนดชำระ-ตามวันที่ | `menu_invoice_due_by_date` | `SMLFastReport._designer` |  |  |
| 5.14.3 Acc/Pro · 6.14.3 AccPOS/AccPOSPro | รายงานสรุป › รายงานใบส่งของค้างชำระแสดงวันที่ถึงกำหนด | `menu_invoice_arrears_due` | `SMLFastReport._designer` |  |  |
| 5.14.4 Acc/Pro · 6.14.4 AccPOS/AccPOSPro | รายงานสรุป › รายงานใบส่งของเกินกำหนดชำระ-ตามวันที่ | `menu_invoice_overdue_by_date` | `SMLFastReport._designer` |  |  |
| 5.14.5 Acc/Pro · 6.14.5 AccPOS/AccPOSPro | รายงานสรุป › รายงานจ่ายชำระค่าสินค้า-ตามใบส่งของ | `menu_payment_by_invoice` | `SMLFastReport._designer` |  |  |
| 5.14.6 Acc/Pro · 6.14.6 AccPOS/AccPOSPro | รายงานสรุป › รายงานการจ่ายชำระประจำวัน-ตามวันที่ | `menu_payment_by_date` | `SMLFastReport._designer` |  |  |
| 5.14.7 Acc/Pro · 6.14.7 AccPOS/AccPOSPro | รายงานสรุป › รายงานการจ่ายเงินประจำวัน-ตามแผนก | `menu_payment_by_department` | `SMLFastReport._designer` |  |  |
| 5.15.1 Acc/Pro · 6.15.1 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานเคลื่อนไหวเจ้าหนี้ | `menu_ap_report_payable_movement` | `SMLERPARAPReport.report._movement` |  |  |
| 5.15.2 Acc/Pro · 6.15.2 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้ | `menu_ap_report_payable_aging` | `SMLERPARAPReport.report._ageing` |  |  |
| 5.15.3 Acc/Pro · 6.15.3 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้-ตามเอกสาร | `menu_ap_report_payable_aging_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |  |
| 5.15.4 Acc/Pro · 6.15.4 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานสถานะเจ้าหนี้ | `menu_ap_report_payable_status` | `SMLERPARAPReport.report._absolute_status` |  |  |
| 5.15.5 Acc/Pro · 6.15.5 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานเจ้าหนี้ที่ไม่มีการเคลื่อนไหว | `menu_ap_report_payable_not_movement` | tag:apreport (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 5.15.6 Acc/Pro · 6.15.6 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานใบตั้งหนี้จากการซื้อแบบแจกแจงตามเจ้าหนี้ | `menu_ap_detail_debt_by_ap` | `SMLFastReport._designer` |  |  |
| 5.16 Acc/Pro · 6.16 AccPOS/AccPOSPro | บันทึกรูปภาพเอกสาร | `menu_ap_doc_picture` | `SMLERPAP._ap_doc_picture` | _documentPicture |  |
| 5.17 Acc/Pro · 6.17 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_supplier` | tag:fastreportother |  |  |

## ลูกหนี้ (55)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 6.1.1 Acc/Pro · 7.1.1 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › กำหนดลูกหนี้ | `menu_ar_detail` | `SMLERPAR._ar` |  |  |
| 6.1.2 Acc/Pro · 7.1.2 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › รายละเอียดลูกหนี้ | `menu_ar_detail_2` | `SMLERPAR._ar_detail` |  |  |
| 6.1.3 Acc/Pro · 7.1.3 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › รายละเอียดสมาชิก | `menu_ar_dealer` | `SMLERPAR._ar_dealer` |  |  |
| — | ข้อมูลลูกหนี้ › บันทึกเอกสารอ้างอิง | `menu_ar_reference` | tag:ar (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.1.4 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › กำหนดแต้มคงเหลือยกมา | `menu_ar_point_balance` | `SMLERPAR._ar_point_balance` | _ar_point_balance |  |
| 7.1.5 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › บันทึกตัดแต้ม | `menu_ar_cut_point` | `SMLERPAR._ar_cut_point` | _ar_cut_point |  |
| 7.1.6 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › แต้มสะสม | `menu_ar_point` | `SMLERPAR.ar_point` |  |  |
| 7.1.7 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › คำณวนแต้มสะสม | `menu_ar_point_recal` | `SMLERPAR.ar_point_recal` |  |  |
| 6.1.4 Acc/Pro · 7.1.8 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 6.1.5 Acc/Pro · 7.1.9 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 6.1.6 Acc/Pro · 7.1.10 AccPOS/AccPOSPro | ข้อมูลลูกหนี้ › นำเข้าที่อยู่จัดส่งลูกหนี้ | `menu_import_ar_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 7.1.11 AccPOSPro | ข้อมูลลูกหนี้ › ข้อมูลคู่ค้า(ลูกหนี้) | `menu_ar_customer_connected` | `SMLERPAR.ar_customer_connected` | _searchDataFull |  |
| 6.1.7.1 Acc/Pro · 7.1.11.1 AccPOS · 7.1.12.1 AccPOSPro | ข้อมูลลูกหนี้ › รายงาน › รายงานรายละเอียดลูกค้า-ตามรหัสลูกค้า | `menu_ar_report_detail_ar` | `SMLERPReport.ar._report_ar_detail` |  |  |
| 7.1.11.2 AccPOS · 7.1.12.2 AccPOSPro | ข้อมูลลูกหนี้ › รายงาน › รายงานแต้มคงเหลือลูกหนี้ | `menu_report_point_balance` | `SMLERPARReport.report._ar_report` |  | ลูกหนี้_แต้มคงเหลือ |
| 6.2 Acc/Pro · 7.2 AccPOS/AccPOSPro | ตั้งหนี้ยกมา (ลูกหนี้) | `menu_ar_debt_balance` | `SMLERPAR._ar_debt_balance` | _ar_ap_trans | 93 |
| 6.3 Acc/Pro · 7.3 AccPOS/AccPOSPro | เพิ่มหนี้ยกมา (ลูกหนี้) | `menu_ar_increase_debt` | `SMLERPAR._ar_increase_debt` | _ar_ap_trans | 95 |
| 6.4 Acc/Pro · 7.4 AccPOS/AccPOSPro | ลดหนี้ยกมา (ลูกหนี้) | `menu_ar_cn_balance` | `SMLERPAR._ar_cn_balance` | _ar_ap_trans | 97 |
| 6.5.1 Acc/Pro · 7.5.1 AccPOS/AccPOSPro | รายงาน › รายงานตั้งหนี้ยกมา | `menu_ar_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` |  | 93 |
| 6.5.2 Acc/Pro · 7.5.2 AccPOS/AccPOSPro | รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ar_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` |  | 95 |
| 6.5.3 Acc/Pro · 7.5.3 AccPOS/AccPOSPro | รายงาน › รายงานลดหนี้ยกมา | `menu_ar_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` |  | 97 |
| 6.6 Acc/Pro · 7.6 AccPOS/AccPOSPro | ตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 99 |
| 6.7 Acc/Pro · 7.7 AccPOS/AccPOSPro | เพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 101 |
| 6.8 Acc/Pro · 7.8 AccPOS/AccPOSPro | ลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 103 |
| 6.9.1 Acc/Pro · 7.9.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_debt_balance_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 100 |
| 6.9.2 Acc/Pro · 7.9.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 104 |
| 6.9.3 Acc/Pro · 7.9.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 102 |
| 6.9.4 Acc/Pro · 7.9.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_ar_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 99 |
| 6.9.5 Acc/Pro · 7.9.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_report_ar_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 101 |
| 6.9.6 Acc/Pro · 7.9.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_ar_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 103 |
| 6.9.7 Acc/Pro · 7.9.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_ar_cancel_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 100 |
| 6.9.8 Acc/Pro · 7.9.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_ar_cancel_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 102 |
| 6.9.9 Acc/Pro · 7.9.9 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_ar_cancel_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 104 |
| 6.10 Acc/Pro · 7.10 AccPOS/AccPOSPro | ใบวางบิล (ลูกหนี้) | `menu_ar_pay_bill` | `SMLERPAR._ar_pay_bill` | _ar_ap_trans, _formSaleOrderPreview | 235 |
| — | Bill Collector | `menu_imex_bill_collector` | `SMLERPAR._ar_bill_collector` | _ar_ap_trans | 810 |
| 6.11 Acc/Pro · 7.11 AccPOS/AccPOSPro | รับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_debt_billing` | `SMLERPAR._ar_debt_billing` | _ar_ap_trans, _formSaleOrderPreview | 239 |
| 6.12.1 Acc/Pro · 7.12.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกใบวางบิล (ลูกหนี้) | `menu_ar_cancel_pay_bill` | `SMLERPAR._ar_cancel_pay_bill` | _ar_ap_trans | 236 |
| 6.12.2 Acc/Pro · 7.12.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกชำระหนี้/ยกเลิกใบเสร็จรับเงิน | `menu_ar_cancel_debt_billing` | `SMLERPAR._ar_cancel_debt_billing` | _ar_ap_trans | 240 |
| 6.12.3 Acc/Pro · 7.12.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกใบวางบิล(ลูกหนี้) | `menu_ar_report_cancel_pay_billing` | `SMLERPReportTool._reportArApTrans` |  | 236 |
| 6.12.4 Acc/Pro · 7.12.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_cancel_invoice` | `SMLERPReportTool._reportArApTrans` |  | 240 |
| 6.12.5 Acc/Pro · 7.12.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานใบวางบิล (ลูกหนี้) | `menu_ar_report_billing` | `SMLERPReportTool._reportArApTrans` |  | 235 |
| 6.12.6 Acc/Pro · 7.12.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการรับชำระหนี้ประจำวัน | `menu_ar_report_pay_debt_trans` | `SMLERPReportTool._reportArApTrans` |  | 239 |
| 6.12.7 Acc/Pro · 7.12.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_receipt` | `SMLERPReportTool._reportArApTrans` |  | 239 |
| 6.12.8 Acc/Pro · 7.12.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียดการรับเงินสด,เงินโอน) | `menu_report_ar_payment_pay_detail` | `SMLFastReport._designer` |  |  |
| — | รายงาน/ยกเลิก › รายงายใบเสร็จรับเงินพร้อมรายการย่อย | `menu_ar_report_receipt_and_detail` | `SMLERPReport.ar._report_ar_receipt_and_detail` |  |  |
| — | รายงาน/ยกเลิก › รายงานใบวางบิลตามพนักงานเก็บเงิน | `menu_report_billing_note_by_customer_cashier` | `IMEXControl.report.report_billing_note_by_customer_cashier` |  |  |
| 6.13.1 Acc/Pro · 7.13.1 AccPOS/AccPOSPro | รายงานสรุป › รายงานใบส่งของค้างชำระ-ตามวันที่ | `menu_ar_report_invoice_remain_pay` | `SMLFastReport._designer` |  |  |
| 6.13.2 Acc/Pro · 7.13.2 AccPOS/AccPOSPro | รายงานสรุป › รายงานตรวจสอบยอดวงเงิน | `menu_ar_report_check_balance` | `SMLERPReport.ar._report_ar_check_balance` |  |  |
| 6.13.3 Acc/Pro · 7.13.3 AccPOS/AccPOSPro | รายงานสรุป › รายงานสรุป การบันทึก รับเงินจากการขาย/รับชำระหนี้ | `menu_report_receive_money_summary` | `SMLFastReport._designer` |  |  |
| 6.14.1 Acc/Pro · 7.14.1 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานเคลื่อนไหวลูกหนี้ | `menu_ar_report_movement` | `SMLERPARAPReport.report._movement` |  |  |
| 6.14.2 Acc/Pro · 7.14.2 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานอายุลูกหนี้ | `menu_ar_report_period_ar_debt_remain` | `SMLERPARAPReport.report._ageing` |  |  |
| 6.14.3 Acc/Pro · 7.14.3 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานอายุลูกหนี้-ตามเอกสาร | `menu_ar_report_period_ar_debt_remain_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |  |
| 6.14.4 Acc/Pro · 7.14.4 AccPOS/AccPOSPro | รายงานวิเคราะห์ › รายงานสถานะลูกหนี้ | `menu_ar_report_status_ar` | `SMLERPARAPReport.report._absolute_status` |  |  |
| — | รายงานวิเคราะห์ › รายงาน Statement ลูกหนี้ | `menu_report_imex_ar_statement` | `IMEXControl.report._reportARStatement` |  |  |
| 6.15 Acc/Pro · 7.15 AccPOS/AccPOSPro | บันทึกรูปภาพเอกสาร | `menu_ar_doc_picture` | `SMLERPAR._ar_doc_picture` | _documentPicture |  |
| 6.16 Acc/Pro · 7.16 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_customer` | tag:fastreportother |  |  |

## เงินสด/ธนาคาร (128)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 7.1 Acc/Pro · 8.1 AccPOS/AccPOSPro | รายได้อื่นๆ | `menu_cash_income_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 250 |
| 7.2 Acc/Pro · 8.2 AccPOS/AccPOSPro | ลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 252 |
| 7.3 Acc/Pro · 8.3 AccPOS/AccPOSPro | เพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 254 |
| 7.4.1 Acc/Pro · 8.4.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 251 |
| 7.4.2 Acc/Pro · 8.4.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 253 |
| 7.4.3 Acc/Pro · 8.4.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 255 |
| 7.4.4 Acc/Pro · 8.4.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานรายได้อื่นๆ | `menu_cash_income_other_report` | `SMLERPReportTool._reportCashBankTrans` |  | 250 |
| 7.4.5 Acc/Pro · 8.4.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 252 |
| 7.4.6 Acc/Pro · 8.4.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 254 |
| 7.4.7 Acc/Pro · 8.4.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 251 |
| 7.4.8 Acc/Pro · 8.4.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 253 |
| 7.4.9 Acc/Pro · 8.4.9 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 255 |
| 7.5 Acc/Pro · 8.5 AccPOS/AccPOSPro | ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 260 |
| 7.6 Acc/Pro · 8.6 AccPOS/AccPOSPro | ลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 262 |
| 7.7 Acc/Pro · 8.7 AccPOS/AccPOSPro | เพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 264 |
| 7.8.1 Acc/Pro · 8.8.1 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 261 |
| 7.8.2 Acc/Pro · 8.8.2 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 263 |
| 7.8.3 Acc/Pro · 8.8.3 AccPOS/AccPOSPro | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 265 |
| 7.8.4 Acc/Pro · 8.8.4 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_report` | `SMLERPReportTool._reportCashBankTrans` |  | 260 |
| 7.8.5 Acc/Pro · 8.8.5 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 262 |
| 7.8.6 Acc/Pro · 8.8.6 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 264 |
| 7.8.7 Acc/Pro · 8.8.7 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 261 |
| 7.8.8 Acc/Pro · 8.8.8 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 263 |
| 7.8.9 Acc/Pro · 8.8.9 AccPOS/AccPOSPro | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 265 |
| 7.9.1 Acc/Pro · 8.9.1 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › ยกมาเงินสด | `menu_cb_cash_balance` | `SMLERPCASHBANK._cb_cash_balance` | CashBalanceScreenTop |  |
| 7.9.2 Acc/Pro · 8.9.2 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › คืน/ลด วงเงินสดย่อย | `menu_cb_petty_cash_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 300 |
| 7.9.3 Acc/Pro · 8.9.3 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รับ/เพิ่ม วงเงินสดย่อย | `menu_cb_petty_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 2 |
| 7.9.4.1 Acc/Pro · 8.9.4.1 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกคืน/ลด วงเงินสดย่อย | `menu_cb_petty_cash_receive_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 302 |
| 7.9.4.2 Acc/Pro · 8.9.4.2 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกรับ/เพิ่ม วงเงินสดย่อย | `menu_cb_petty_return_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 303 |
| 7.9.4.3 Acc/Pro · 8.9.4.3 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานจ่ายเงินสดย่อย | `menu_report_cb_petty_cash_request` | `SMLFastReport._designer` |  |  |
| 7.9.4.4 Acc/Pro · 8.9.4.4 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานรับเงินสดย่อย | `menu_report_cb_petty_cash_return` | `SMLFastReport._designer` |  |  |
| 7.9.4.5 Acc/Pro · 8.9.4.5 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกเบิกเงินสดย่อย | `menu_report_cb_cancel_pettycash_request` | `SMLERPReportTool._reportTrans` |  | 302 |
| 7.9.4.6 Acc/Pro · 8.9.4.6 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกรับเงินสดย่อย | `menu_report_cb_cancel_pettycash_return` | `SMLERPReportTool._reportTrans` |  | 303 |
| 7.9.5.1 Acc/Pro · 8.9.5.1 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงานสรุป › รายงานเคลื่อนไหวเงินสดย่อย | `menu_sub_cash_movements` | `SMLERPCASHBANKReport._report_petty_cash` |  | เงินสดย่อย_เคลื่อนไหว |
| — | เงินสด/เงินสดย่อย › รายงานสรุป › รายการตั้งเบิกเงินสดย่อย | `menu_report_cb_pettycash_request_budget` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | เงินสด/เงินสดย่อย › รายงานสรุป › รายงานบันทึกขอเบิกเงินทดลองจ่าย - เรียงตามวันที่เอกสาร | `menu_report_cb_request_testpay` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.5.2 Acc/Pro · 8.9.5.2 AccPOS/AccPOSPro | เงินสด/เงินสดย่อย › รายงานสรุป › รายงานสถานะเงินสดย่อย | `menu_peety_cash_status` | `SMLERPCASHBANKReport._report_petty_cash` |  | เงินสดย่อย_สถานะ |
| 7.10.1.1 Acc/Pro · 8.10.1.1 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › กำหนดสมุดเงินฝาก | `menu_book_bank` | `SMLERPConfig._book` | _myManageData, _searchDataFull |  |
| 7.10.1.2 Acc/Pro · 8.10.1.2 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › เงินฝากธนาคารยกมา | `menu_cb_bank_balance` | `SMLERPCASHBANK._cb_bank_balance` | BankBalanceScreenTop |  |
| 7.10.1.3 Acc/Pro · 8.10.1.3 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › บันทึกฝากเงิน | `menu_cb_cash_payin` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 401 |
| 7.10.1.4 Acc/Pro · 8.10.1.4 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › บันทึกถอนเงิน | `menu_cb_cash_withdraw` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 402 |
| 7.10.1.5 Acc/Pro · 8.10.1.5 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › บันทึกโอนเงินระหว่างธนาคาร | `menu_cash_transfer` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 422 |
| 7.10.1.6 Acc/Pro · 8.10.1.6 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › บันทึกขึ้นเงินwallet | `menu_cb_wallet_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 1 |
| 7.10.1.7.1 Acc/Pro · 8.10.1.7.1 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกฝากเงิน | `menu_cb_cash_payin_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 403 |
| 7.10.1.7.2 Acc/Pro · 8.10.1.7.2 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกถอนเงิน | `menu_cb_cash_withdraw_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 404 |
| 7.10.1.7.3 Acc/Pro · 8.10.1.7.3 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกโอนเงินระหว่างธนาคาร | `menu_cash_transfer_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 423 |
| 7.10.1.7.4 Acc/Pro · 8.10.1.7.4 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการฝากเงิน | `menu_report_cash_payin` | `SMLFastReport._designer` |  |  |
| 7.10.1.7.5 Acc/Pro · 8.10.1.7.5 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการถอนเงิน | `menu_report_cash_withdraw` | `SMLFastReport._designer` |  |  |
| 7.10.1.7.6 Acc/Pro · 8.10.1.7.6 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการโอนเงินระหว่างธนาคาร | `menu_cb_report_transfer_bank` | `SMLERPReportTool._reportCashBankTrans` |  | 422 |
| 7.10.1.7.7 Acc/Pro · 8.10.1.7.7 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกฝากเงิน | `menu_report_cancel_withdraw` | `SMLERPReportTool._reportCashBankTrans` |  | 403 |
| 7.10.1.7.8 Acc/Pro · 8.10.1.7.8 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกถอนเงิน | `menu_report_cancel_payin` | `SMLERPReportTool._reportCashBankTrans` |  | 404 |
| 7.10.1.7.9 Acc/Pro · 8.10.1.7.9 AccPOS/AccPOSPro | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกการโอนเงินระหว่างธนาคาร | `menu_report_transfer_bank_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 423 |
| — | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานรายได้จากธนาคาร | `menu_cb_report_bank_income` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานค่าใช้จ่ายจากธนาคาร | `menu_cb_report_bank_expanse` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.10.2.1 Acc/Pro · 8.10.2.1 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › เช็ครับยกมา | `menu_cb_chq_in_receive_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 405 |
| 7.10.2.2 Acc/Pro · 8.10.2.2 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › ทะเบียนเช็ครับ | `menu_cb_chq_in_receive_master` | `SMLERPCASHBANK._cb_chq_in_receive_master` |  |  |
| 7.10.2.3 Acc/Pro · 8.10.2.3 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกนำฝาก (เช็ครับ) | `menu_cb_chq_in_payin` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 410 |
| 7.10.2.4 Acc/Pro · 8.10.2.4 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกเช็คผ่าน (เช็ครับ) | `menu_cb_chq_in_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 411 |
| 7.10.2.5 Acc/Pro · 8.10.2.5 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกเช็คคืน (เช็ครับ) | `menu_cb_chq_in_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 412 |
| 7.10.2.6 Acc/Pro · 8.10.2.6 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกเช็คขาดสิทธิ์ (เช็ครับ) | `menu_cb_chq_in_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 413 |
| 7.10.2.7 Acc/Pro · 8.10.2.7 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกการเปลี่ยนเช็ค (เช็ครับ) | `menu_cb_chq_renew` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 416 |
| 7.10.2.8 Acc/Pro · 8.10.2.8 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › บันทึกคืนเช็ค/ตั้งหนี้ใหม่ | `menu_cb_return_chq_new_debt` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 418 |
| 7.10.2.9.1 Acc/Pro · 8.10.2.9.1 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกนำฝากเช็ค | `menu_cb_chq_in_payin_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 430 |
| 7.10.2.9.2 Acc/Pro · 8.10.2.9.2 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คผ่าน | `menu_cb_chq_in_pass_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 431 |
| 7.10.2.9.3 Acc/Pro · 8.10.2.9.3 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็ครับคืน | `menu_cb_chq_in_return_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 432 |
| 7.10.2.9.4 Acc/Pro · 8.10.2.9.4 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คขาดสิทธิ์ | `menu_cb_chq_in_cancel_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 433 |
| 7.10.2.9.5 Acc/Pro · 8.10.2.9.5 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็ค | `menu_cb_chq_renew_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 436 |
| 7.10.2.9.6 Acc/Pro · 8.10.2.9.6 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็ครับยกมา | `menu_cb_report_chq_in_receive_balance` | `SMLERPReportTool._reportCashBankTrans` |  | 405 |
| 7.10.2.9.7 Acc/Pro · 8.10.2.9.7 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานนำฝาก (เช็ครับ) | `menu_bank_report_chq_in_deposit` | `SMLERPReportTool._reportCashBankTrans` |  | 410 |
| 7.10.2.9.8 Acc/Pro · 8.10.2.9.8 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็ครับ) | `menu_bank_report_chq_in_pass` | `SMLERPReportTool._reportCashBankTrans` |  | 411 |
| 7.10.2.9.9 Acc/Pro · 8.10.2.9.9 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรับคืน (เช็ครับ) | `menu_bank_report_chq_in_return` | `SMLERPReportTool._reportCashBankTrans` |  | 412 |
| 7.10.2.9.10 Acc/Pro · 8.10.2.9.10 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็ครับ) | `menu_bank_report_chq_in_pass_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 413 |
| 7.10.2.9.11 Acc/Pro · 8.10.2.9.11 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็ครับ) | `menu_bank_report_chq_in_change` | `SMLERPReportTool._reportCashBankTrans` |  | 416 |
| 7.10.2.9.12 Acc/Pro · 8.10.2.9.12 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกนำฝากเช็ค | `menu_report_cb_chq_in_payin_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 430 |
| 7.10.2.9.13 Acc/Pro · 8.10.2.9.13 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็คผ่าน | `menu_report_cb_chq_in_honor_cancle` | `SMLERPReportTool._reportCashBankTrans` |  | 431 |
| 7.10.2.9.14 Acc/Pro · 8.10.2.9.14 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็ครับคืน | `menu_report_cb_chq_in_return_cancle` | `SMLERPReportTool._reportCashBankTrans` |  | 432 |
| 7.10.2.9.15 Acc/Pro · 8.10.2.9.15 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็ค | `menu_report_cb_chq_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 433 |
| 7.10.2.9.16 Acc/Pro · 8.10.2.9.16 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็ค | `menu_report_cb_chq_in_change_cancle` | `SMLERPReportTool._reportCashBankTrans` |  | 436 |
| 7.10.2.9.17 Acc/Pro · 8.10.2.9.17 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานทะเบียนเช็ครับ | `menu_cb_report_chq_in_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | เช็ค_รายงานเช็ครับ_ตามวันที่รับเช็ค |
| 7.10.2.9.18 Acc/Pro · 8.10.2.9.18 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค | `menu_cb_report_chq_in_receive_by_date` | `SMLFastReport._designer` |  |  |
| 7.10.2.9.19 Acc/Pro · 8.10.2.9.19 AccPOS/AccPOSPro | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่ครบกำหนด | `menu_report_chq_receive_due_date` | `SMLFastReport._designer` |  |  |
| — | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานใบนำฝากเช็ครับพร้อมรายการย่อย | `menu_report_chq_card_disposit_cheque_detail` | `SMLERPReport.Cheque_Card._report_chq_card_Disposit_Cheque_Detail` |  |  |
| — | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_received_by_date_by_status` | `IMEXControl.report._report_chq_receive_by_status` |  |  |
| — | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่ - ตามสถานะเช็ค แสดงยอดรวม | `menu_imex_report_chqreceive_status_by_date` | `IMEXControl.report._report_chq_receive_status_by_date` |  |  |
| — | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามสถานะเช็ค แสดงยอดรวม(ไม่รวมเช็คคืน,เช็คคืนตั้งหนี้ใหม่) | `menu_imex_report_chqreceive_status_by_date_only_hand` | `IMEXControl.report._report_chq_receive_status_by_date_2` |  |  |
| — | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ณ วันที่ | `menu_imex_report_chq_receive_at_date` | `IMEXControl.report._report_chq_receive_last_status_by_date` |  |  |
| 7.10.3.1 Acc/Pro · 8.10.3.1 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › เช็คจ่ายยกมา | `menu_cb_chq_out_payment_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 406 |
| 7.10.3.2 Acc/Pro · 8.10.3.2 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › ทะเบียนเช็คจ่าย | `menu_cb_chq_out_payment_master` | `SMLERPCASHBANK._cb_chq_out_payment_master` |  |  |
| 7.10.3.3 Acc/Pro · 8.10.3.3 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › บันทึกเช็คผ่าน (เช็คจ่าย) | `menu_cb_chq_out_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 451 |
| 7.10.3.4 Acc/Pro · 8.10.3.4 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › บันทึกเช็คคืน (เช็คจ่าย) | `menu_cb_chq_out_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 453 |
| 7.10.3.5 Acc/Pro · 8.10.3.5 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › บันทึกเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_cb_chq_out_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 452 |
| 7.10.3.6 Acc/Pro · 8.10.3.6 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › บันทึกการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_cb_chq_out_renew` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 456 |
| 7.10.3.7.1 Acc/Pro · 8.10.3.7.1 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คจ่ายผ่าน | `menu_cb_chq_out_pass_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 471 |
| 7.10.3.7.2 Acc/Pro · 8.10.3.7.2 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คขาดสิทธิ์ | `menu_cb_chq_out_cancel_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 472 |
| 7.10.3.7.3 Acc/Pro · 8.10.3.7.3 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คคืน | `menu_cb_chq_out_return_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 473 |
| 7.10.3.7.4 Acc/Pro · 8.10.3.7.4 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็คจ่าย | `menu_cb_chq_out_renew_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 476 |
| 7.10.3.7.5 Acc/Pro · 8.10.3.7.5 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คจ่ายยกมา | `menu_cb_report_chq_out_payment_balance` | `SMLERPReportTool._reportCashBankTrans` |  | 406 |
| 7.10.3.7.6 Acc/Pro · 8.10.3.7.6 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็คจ่าย) | `menu_bank_report_chq_out_pass` | `SMLERPReportTool._reportCashBankTrans` |  | 451 |
| 7.10.3.7.7 Acc/Pro · 8.10.3.7.7 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คคืน (เช็คจ่าย) | `menu_bank_report_chq_out_return` | `SMLERPReportTool._reportCashBankTrans` |  | 453 |
| 7.10.3.7.8 Acc/Pro · 8.10.3.7.8 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_bank_report_chq_out_pass_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 452 |
| 7.10.3.7.9 Acc/Pro · 8.10.3.7.9 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_bank_report_chq_out_change` | `SMLERPReportTool._reportCashBankTrans` |  | 456 |
| 7.10.3.7.10 Acc/Pro · 8.10.3.7.10 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คจ่ายผ่าน | `menu_report_cb_chq_out_honor_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 471 |
| 7.10.3.7.11 Acc/Pro · 8.10.3.7.11 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็คจ่าย | `menu_report_cb_chq_out_cancel_hornor_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 472 |
| 7.10.3.7.12 Acc/Pro · 8.10.3.7.12 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คคืน | `menu_report_chq_out_return_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 473 |
| 7.10.3.7.13 Acc/Pro · 8.10.3.7.13 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็คจ่าย | `menu_report_cb_chq_out_change_cancle` | `SMLERPReportTool._reportCashBankTrans` |  | 476 |
| 7.10.3.7.14 Acc/Pro · 8.10.3.7.14 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานทะเบียนเช็คจ่าย | `menu_cb_report_chq_out_payment` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | เช็ค_รายงานเช็คจ่าย_ตามวันที่จ่ายเช็ค |
| 7.10.3.7.15 Acc/Pro · 8.10.3.7.15 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค | `menu_cb_report_chq_out_payment_by_date` | `SMLFastReport._designer` |  |  |
| 7.10.3.7.16 Acc/Pro · 8.10.3.7.16 AccPOS/AccPOSPro | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - วันครบกำหนด | `menu_report_chq_pay_due_date` | `SMLFastReport._designer` |  |  |
| — | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_pay_by_date_by_status` | `IMEXControl.report.report_chq_pay_by_status` |  |  |
| — | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่ - ตามสถานะเช็ค | `imex_report_cheque_pay_status_by_date` | `IMEXControl.report._report_chq_pay_status_by_date` |  |  |
| — | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย ณ วันที่ | `menu_imex_report_chq_pay_at_date` | `IMEXControl.report._report_chq_pay_last_status_by_date` |  |  |
| 7.10.4.1 Acc/Pro · 8.10.4.1 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › ทะเบียนบัตรเครดิต | `menu_cb_credit_card_receive` | `SMLERPCASHBANK._cb_credit_master` |  |  |
| 7.10.4.2 Acc/Pro · 8.10.4.2 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › บันทึกขึ้นเงินบัตรเครดิต | `menu_cb_credit_card_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 461 |
| 7.10.4.3 Acc/Pro · 8.10.4.3 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › บันทึกยกเลิกบัตรเครดิต | `menu_cb_credit_card_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 462 |
| 7.10.4.4 Acc/Pro · 8.10.4.4 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › รายงานขึ้นเงินบัตรเครดิต | `menu_cb_report_credit_card_pass` | `SMLERPReportTool._reportCashBankTrans` |  | 461 |
| 7.10.4.5 Acc/Pro · 8.10.4.5 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › รายงานยกเลิกบัตรเครดิต | `menu_report_cb_credit_card_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 462 |
| 7.10.4.6 Acc/Pro · 8.10.4.6 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › รายงานรายการรับบัตรเครดิต | `menu_cb_report_credit_card_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | บัตรเครดิต_รายงานบัตรเครดิต_ตามวันที่รับ |
| 7.10.4.7 Acc/Pro · 8.10.4.7 AccPOS/AccPOSPro | ธนาคาร › บัตรเครดิต › รายงานรายละเอียดบัตรเครดิต - ตามวันที่รับ | `menu_report_chq_card_enddate_card` | `SMLFastReport._designer` |  |  |
| 7.10.5.1 Acc/Pro · 8.10.5.1 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงานเคลื่อนไหวเงินสด | `_menu_cash_movements` | `SMLERPCASHBANKReport._cashbank_report` |  | เคลื่อนไหวเงินสด |
| — | ธนาคาร › รายงาน › รายงานการฝากเงินสด | `_menu_cash_deposit` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ธนาคาร › รายงาน › รายงานการรับเงินอื่นๆพร้อมรายการย่อย | `_menu_received_cash_sub_item` | `SMLERPReport.cash_bank.Received_Cash_sub_item` |  |  |
| 7.10.5.2 Acc/Pro · 8.10.5.2 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงานสรุปการรับเงิน | `menu_summary_received` | `SMLFastReport._designer` |  |  |
| 7.10.5.3 Acc/Pro · 8.10.5.3 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงานสรุปการจ่ายเงิน | `menu_summary_payment` | `SMLFastReport._designer` |  |  |
| 7.10.5.4 Acc/Pro · 8.10.5.4 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงานยอดเงินคงเหลือสมุดฝากธนาคาร | `menu_book_bank_balance` | `SMLFastReport._designer` |  |  |
| 7.10.5.5 Acc/Pro · 8.10.5.5 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงาน Bank Statement | `_menu_bank_statement` | `SMLERPReport.cash_bank._bankStatment` |  |  |
| 7.10.5.6 Acc/Pro · 8.10.5.6 AccPOS/AccPOSPro | ธนาคาร › รายงาน › รายงาน Statement ล่วงหน้า | `menu_statement_advance` | `SMLFastReport._designer` |  |  |
| 7.11 Acc/Pro · 8.11 AccPOS/AccPOSPro | บันทึกรูปภาพเอกสาร | `menu_cb_doc_picture` | `SMLERPCASHBANK._cb_doc_picture` | _documentPicture |  |
| 7.12 Acc/Pro · 8.12 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_cashbank` | tag:fastreportother |  |  |

## ค่าเสื่อม (12)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 8.1.1 Acc/Pro · 9.1.1 AccPOS/AccPOSPro | รายละเอียดสินทรัพย์ › ข้อมูลสินทรัพย์ | `menu_asset_lists` | `SMLERPASSET._as_list` | _myManageData, _searchDataFull |  |
| 8.1.2 Acc/Pro · 9.1.2 AccPOS/AccPOSPro | รายละเอียดสินทรัพย์ › กำหนดรูปภาพ | `menu_asset_picture` | `SMLERPASSET._as_list_pic` | _myManageData, _getPicture |  |
| 8.2 Acc/Pro · 9.2 AccPOS/AccPOSPro | บันทึกการซ่อมบำรุงสินทรัพย์ | `menu_asset_maintenance` | `SMLERPASSET._as_maintain` | _myManageData, _searchDataFull |  |
| 8.3 Acc/Pro · 9.3 AccPOS/AccPOSPro | บันทึกการขายสินทรัพย์ | `menu_asset_sale` | `SMLERPSO._saleAssets` |  | 2 |
| 8.4 Acc/Pro · 9.4 AccPOS/AccPOSPro | แสดงค่าเสื่อมราคาสินทรัพย์รายวัน | `menu_show_asset_byday` | `SMLERPASSET._display._depreciateByDay` |  |  |
| 8.5 Acc/Pro · 9.5 AccPOS/AccPOSPro | แสดงค่าเสื่อมราคาสินทรัพย์รายเดือน | `menu_show_asset_bymonth` | `SMLERPASSET._display._depreciateByMonth` |  |  |
| 8.6 Acc/Pro · 9.6 AccPOS/AccPOSPro | แสดงค่าเสื่อมราคาสินทรัพย์รายปี | `menu_show_asset_byyear` | `SMLERPASSET._display._depreciateByYear` |  |  |
| 8.7 Acc/Pro · 9.7 AccPOS/AccPOSPro | โอนข้อมูลเข้าระบบบัญชี | `menu_asset_transfers` | `SMLERPASSET._as_transfer` | _myManageData, _glDetail, _journalScreen |  |
| 8.8.1 Acc/Pro · 9.8.1 AccPOS/AccPOSPro | รายงาน › รายงานรายละเอียดสินทรัพย์ | `menu_asset_report_list` | `SMLERPASSET._report._asset._report` |  |  |
| 8.8.2 Acc/Pro · 9.8.2 AccPOS/AccPOSPro | รายงาน › รายงานค่าเสื่อมราคาสินทรัพย์ | `menu_asset_report_depreciate` | `SMLERPASSET._report._depreciate._report` |  |  |
| 8.8.3 Acc/Pro · 9.8.3 AccPOS/AccPOSPro | รายงาน › รายงานการซ่อมบำรุงสินทรัพย์ | `menu_asset_report_maintain` | `SMLERPASSET._report._maintain._report` |  |  |
| 8.9 Acc/Pro · 9.9 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_asset` | tag:fastreportother |  |  |

## บัญชี (66)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 9.1.1 Acc/Pro · 10.1.1 AccPOS/AccPOSPro | ผังบัญชี › รายละเอียดผังบัญชี | `menu_chart_of_account` | `SMLERPGL._chart._chartOfAccount` | _myManageData, _searchDataFull, _selectCode |  |
| 9.1.2 Acc/Pro · 10.1.2 AccPOS/AccPOSPro | ผังบัญชี › ปรับปรุงผังบัญชีแบบเร็ว | `menu_chart_of_account_fast` | `MyLib._myFrameWork` |  |  |
| 9.1.3 Acc/Pro · 10.1.3 AccPOS/AccPOSPro | ผังบัญชี › ตรวจสอบโครงสร้างผังบัญชี | `menu_chart_of_account_flow` | `SMLERPGL._chart._chatOfAccountFlow` |  |  |
| 9.1.4 Acc/Pro · 10.1.4 AccPOS/AccPOSPro | ผังบัญชี › รายงานรายละเอียดผังบัญชี | `menu_report_chart_of_account` | `SMLERPGL._report._chartOfAccount._report` |  |  |
| 9.2.1 Acc/Pro · 10.2.1 AccPOS/AccPOSPro | บัญชีแยกประเภท › ข้อมูลรายวัน | `menu_gl_journal` | `SMLERPGL._journalEntryAccount` | _myManageData, _glDetail, _journalScreen |  |
| 9.2.2 Acc/Pro · 10.2.2 AccPOS/AccPOSPro | บัญชีแยกประเภท › บันทึกข้อมูลรายวันแบบเร็ว | `menu_gl_journal_fast` | `SMLERPGL._journalEntryFast` | _glDetail, _journalScreen, _recurring |  |
| 9.2.3 Acc/Pro · 10.2.3 AccPOS/AccPOSPro | บัญชีแยกประเภท › บันทึกรูปภาพ | `menu_gl_picture` | `SMLERPGL._journalEntryAccount_pic` | _myManageData, _getPicture, _journalScreen_pic |  |
| 9.2.4 Acc/Pro · 10.2.4 AccPOS/AccPOSPro | บัญชีแยกประเภท › ประมวลผลจากข้อมูลรายวัน | `menu_gl_process` | `SMLERPGL._transProcessUserControl` |  |  |
| 9.2.5 Acc/Pro · 10.2.5 AccPOS/AccPOSPro | บัญชีแยกประเภท › ตรวจสอบความถูกต้อง | `menu_gl_check_data` | `SMLERPGL._checkData` |  |  |
| 9.2.6 Acc/Pro · 10.2.6 AccPOS/AccPOSPro | บัญชีแยกประเภท › ผ่านรายการ | `menu_gl_journal_pass` | `SMLERPGL._journalPass` |  |  |
| 9.2.7 Acc/Pro · 10.2.7 AccPOS/AccPOSPro | บัญชีแยกประเภท › ยกเลิกผ่านรายการ | `menu_gl_journal_pass_cancel` | `SMLERPGL._journalPassUndo` |  |  |
| 9.2.8 Acc/Pro · 10.2.8 AccPOS/AccPOSPro | บัญชีแยกประเภท › สรุปบัญชีสินค้าและต้นทุนขาย | `menu_product_sale_cost_close` | `SMLERPGL.JournalProductSaleCost._journalProductSaleCostControl` | _glDetail, _journalScreen |  |
| 9.2.9 Acc/Pro · 10.2.9 AccPOS/AccPOSPro | บัญชีแยกประเภท › สรุปยอดบัญชี | `menu_journal_summary` | `SMLERPGL.JournalSummary.JournalSummaryControl` |  |  |
| 9.2.10 Acc/Pro · 10.2.10 AccPOS/AccPOSPro | บัญชีแยกประเภท › แสดงบัญชีแยกประเภท | `menu_gl_show_sheet` | `SMLERPGL._display._glList` |  |  |
| 9.2.11 Acc/Pro · 10.2.11 AccPOS/AccPOSPro | บัญชีแยกประเภท › แสดงบัญชีแยกประเภท (แบบสรุป) | `menu_gl_show_sheet_sum` | `SMLERPGL._display._glListSum` |  |  |
| 9.2.12 Acc/Pro · 10.2.12 AccPOS/AccPOSPro | บัญชีแยกประเภท › รายงานข้อมูลรายวัน | `menu_gl_report_journal` | `SMLERPGL._report._report_journal_daily_lao._report_daily_journal_lao` |  |  |
| 9.2.13 Acc/Pro · 10.2.13 AccPOS/AccPOSPro | บัญชีแยกประเภท › รายงานข้อมูลรายวันแบบสรุป | `menu_gl_report_journal_sum` | `SMLERPGL._report._journalSum._report` |  |  |
| 9.2.14 Acc/Pro · 10.2.14 AccPOS/AccPOSPro | บัญชีแยกประเภท › รายงานบัญชีแยกประเภท | `menu_gl_report_sheet` | `SMLERPGL._report._sheet._report` |  |  |
| 9.2.15 Acc/Pro · 10.2.15 AccPOS/AccPOSPro | บัญชีแยกประเภท › รายงานบัญชีแยกประเภท (แบบสรุป) | `menu_gl_report_sheet_sum` | `SMLERPGL._report._sheetSum._report` |  |  |
| 9.3.1 Acc/Pro · 10.3.1 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย | `menu_report_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 9.3.2 Acc/Pro · 10.3.2 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 9.3.3 Acc/Pro · 10.3.3 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (รูปแบบใหม่) | `menu_report_vat_sale_2557` | `SMLERPGL._tax._vat` |  |  |
| 9.3.4 Acc/Pro · 10.3.4 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (มาตรฐาน) | `menu_report_vat_sale_standard` | `SMLERPGL._report._tax._reportVatSale` |  |  |
| 9.3.5 Acc/Pro · 10.3.5 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (รูปแบบใหม่แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale_with_tax` | `SMLERPGL._tax._vat` |  |  |
| 10.3.6 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษีขาย | `menu_report_sum_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 9.3.6 Acc/Pro · 10.3.7 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ | `menu_report_vat_buy` | `SMLERPGL._tax._vat` |  |  |
| 9.3.7 Acc/Pro · 10.3.8 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_buy` | `SMLERPGL._tax._vat` |  |  |
| 9.3.8 Acc/Pro · 10.3.9 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ (รูปแบบใหม่) | `menu_report_vat_buy_2557` | `SMLERPGL._tax._vat` |  |  |
| 9.3.9 Acc/Pro · 10.3.10 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีซื้อ (มาตรฐาน) | `menu_report_vat_buy_standard` | `SMLERPGL._report._tax._reportVatBuy` |  |  |
| 9.3.10 Acc/Pro · 10.3.11 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษี | `menu_gl_vat_report_sum` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.3.11 Acc/Pro · 10.3.12 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีขายต่างประเทศ | `menu_gl_vat_report_sale_inter` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.3.12 Acc/Pro · 10.3.13 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานภาษีซื้อต่างประเทศ | `menu_gl_vat_report_buy_inter` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.3.13 Acc/Pro · 10.3.14 AccPOS/AccPOSPro | ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษีต่างประเทศ | `menu_gl_vat_report_inter_sum` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ภาษีมูลค่าเพิ่ม › รายงานภาษีขายรูปแบบใหม่อัตราภาษีศูนย์ (เพิ่มรายละเอียด) | `menu_report_except_vat_sale_with_tax_add_detail` | `SMLERPGL._tax._vatSale` |  |  |
| — | ภาษีมูลค่าเพิ่ม › รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 1) | `menu_report_except_vat_buy_type1` | `SMLERPGL._tax._vatBuyNewType1` |  |  |
| — | ภาษีมูลค่าเพิ่ม › รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 2) | `menu_report_except_vat_buy_type2` | `SMLERPGL._tax._vatBuyNewType2` |  |  |
| 9.4.1 Acc/Pro · 10.4.1 AccPOS/AccPOSPro | หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.53) | `menu_gl_wht_report_in_53` | `SMLERPGL._report._tax._wht` |  |  |
| 9.4.2 Acc/Pro · 10.4.2 AccPOS/AccPOSPro | หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.3) | `menu_gl_wht_report_in_3` | `SMLERPGL._report._tax._wht` |  |  |
| 9.4.3 Acc/Pro · 10.4.3 AccPOS/AccPOSPro | หัก ณ. ที่จ่าย › รายงานภาษีถูกหัก ณ. ที่จ่าย | `menu_gl_wht_report_sum` | `SMLERPGL._report._tax._wht` |  |  |
| 9.4.4 Acc/Pro · 10.4.4 AccPOS/AccPOSPro | หัก ณ. ที่จ่าย › ส่งออกข้อมูลภาษีหัก ณ ทีจ่าย | `menu_export_wht` | `SMLERPGL._tax._whtExport` |  |  |
| 9.5.1 Acc/Pro · 10.5.1 AccPOS/AccPOSPro | การจัดสรรค์ › ข้อมูลรายวันเชิงวิเคราะห์ | `menu_gl_allocate_all` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.6.1 Acc/Pro · 10.6.1 AccPOS/AccPOSPro | รายงาน › ใบปะหน้าเอกสาร | `menu_gl_report_slip` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.7.1 Acc/Pro · 10.7.1 AccPOS/AccPOSPro | งบการเงิน › แสดงงบทดลอง | `menu_gl_show_trial_balance` | `SMLERPGL._display._glTrialBalance` |  |  |
| 9.7.2 Acc/Pro · 10.7.2 AccPOS/AccPOSPro | งบการเงิน › แสดงงบทดลอง (มิติ) | `menu_gl_analysis_trial_balance` | `SMLERPGL._analysis._trialBalance` |  |  |
| 9.7.3.1 Acc/Pro · 10.7.3.1 AccPOS/AccPOSPro | งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (มาตรฐาน) | `menu_gl_report_trial_balance` | `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` |  |  |
| 9.7.3.2 Acc/Pro · 10.7.3.2 AccPOS/AccPOSPro | งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (แยกแผนก) | `menu_gl_report_trial_balance_depart` | `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` |  |  |
| 9.7.3.3 Acc/Pro · 10.7.3.3 AccPOS/AccPOSPro | งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (แยกสาขา) | `menu_gl_report_trial_balance_branch` | `SMLERPGL._report._trialBalanceBranch._report` |  |  |
| — | งบการเงิน › รายงานงบทดลอง › งบดุลหลังปรับปรุง | `menu_gl_report_balancesheet_asset_lao` | `SMLERPGL._report._report_balancesheet_asset_lao._report_balancesheet_asset_lao` |  |  |
| — | งบการเงิน › รายงานงบทดลอง › งบรายรับรายจ่าย | `menu_gl_report_profit_and_lost_lao` | `SMLERPGL._report._report_balancesheet_profit_and_lost_lao._report_balancesheet_profit_and_lost_lao` |  |  |
| 9.7.4 Acc/Pro · 10.7.4 AccPOS/AccPOSPro | งบการเงิน › แสดงรายการงบดุล | `menu_display_balance_sheet` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.7.5 Acc/Pro · 10.7.5 AccPOS/AccPOSPro | งบการเงิน › รายงานงบดุล | `menu_gl_report_balance` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 9.7.6 Acc/Pro · 10.7.6 AccPOS/AccPOSPro | งบการเงิน › งบดุล | `menu_singha_report_balancesheet_asset` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |  |
| 9.7.7 Acc/Pro · 10.7.7 AccPOS/AccPOSPro | งบการเงิน › แสดงกระดาษทำการ | `menu_gl_show_work_sheet` | `SMLERPGL._display._glWorkSheet` |  |  |
| 9.7.8 Acc/Pro · 10.7.8 AccPOS/AccPOSPro | งบการเงิน › รายงานกระดาษทำการ | `menu_gl_report_balance_sheet` | `SMLERPGL._report._workSheet._report` |  |  |
| 9.7.9 Acc/Pro · 10.7.9 AccPOS/AccPOSPro | งบการเงิน › งบกำไรขาดทุน เปรียบเทียบ | `menu_display_lost_and_profit_compare_dimension` | `SMLERPGL.LostAndProfit._display_lost_and_profit_compare_dimension` |  |  |
| 9.7.10.1 Acc/Pro · 10.7.10.1 AccPOS/AccPOSPro | งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (แยกสาขา) | `menu_gl_report_profit_and_lost_branch_1` | `SMLERPGL._report._profitAndLostBranch._report` |  |  |
| 9.7.10.2 Acc/Pro · 10.7.10.2 AccPOS/AccPOSPro | งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (แยกสาขา-แผนก) | `menu_gl_report_trial_balance_branch_depart` | `SMLERPGL._report._trialBalanceBranchDepart._report` |  |  |
| 9.7.10.3 Acc/Pro · 10.7.10.3 AccPOS/AccPOSPro | งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน | `menu_singha_report_profit_and_lost` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |  |
| 9.7.10.4 Acc/Pro · 10.7.10.4 AccPOS/AccPOSPro | งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) | `menu_report_profit_and_lost_sum_year` | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year` |  |  |
| 9.7.10.5 Acc/Pro · 10.7.10.5 AccPOS/AccPOSPro | งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) ตามแผนก | `menu_report_profit_and_lost_sum_year_by_department` | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year_by_department` |  |  |
| 9.7.11 Acc/Pro · 10.7.11 AccPOS/AccPOSPro | งบการเงิน › งบกระแสเงินสด | `menu_gl_report_other_1` | `SMLERPGL._report._other_1._report` |  |  |
| 9.8 Acc/Pro · 10.8 AccPOS/AccPOSPro | รายงานงบการเงิน | `menu_financial_report` | tag:gl |  |  |
| 9.9 Acc/Pro · 10.9 AccPOS/AccPOSPro | ประมวลผลสิ้นงวด | `menu_gl_end_of_period` | `SMLERPGL._glTransControl` | _myManageData, _glDetail, _journalScreen | 1998 |
| 9.10 Acc/Pro · 10.10 AccPOS/AccPOSPro | ประมวลผลสิ้นปี | `menu_gl_end_of_year` | `SMLERPGL._glTransControl` | _myManageData, _glDetail, _journalScreen | 1999 |
| 9.11 Acc/Pro · 10.11 AccPOS/AccPOSPro | ประมวลผลกำไร/ขาดทุน และต้นทุนขาย | `menu_close_account_process` | `SMLERPGL.AccountCloseWizard.JournalCloseAccountControl` | _glControl |  |
| 9.12 Acc/Pro · 10.12 AccPOS/AccPOSPro | รายงานอื่น ๆ | `menu_fastreport_other_gl` | `SMLFastReport._loadForm` |  |  |

## MIS (9)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 10.1 Pro | จำนวนรายการรายวัน | `menu_mis_calendar_trans` | `SMLMIS.calendar_trans` |  |  |
| — | Sale Information | `menu_sale_information` | `SMLERPSO._saleInformation` | _ap_ar_billForm |  |
| — | Inventory Information | `menu_ic_information` | `SMLERPICInfo._ic_inventory_information` | _icInfoProcess, _icmainScreenTopControl |  |
| — | หน้าจอสำหรับผู้บริหาร | `menu_ic_information_manager` | `SMLERPICInfo._ic_inventory_information_2` | _searchDataFull, _getPicture, _icPriceFormulaGrid |  |
| — | Buy Information | `menu_buy_information` | `SMLERPPO._buyInformation` |  |  |
| ซ่อน | บันทึกค่าส่งเสริมการขาย | `menu_sales_commission` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ซ่อน | รายละเอียดการจัดส่ง | `menu_ic_sale_shipment` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ซ่อน | บันทึกจัดสินค้า | `menu_packing` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ซ่อน | บันทึกการส่งสินค้า | `menu_shipment_confirm` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |

## EDI (2)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | รายละเอียดลูกค้า EDI | `menu_edi_external` | `SMLEDIControl._ediExternal` | _myManageData |  |
| — | ส่งออกข้อมูล EDI | `menu_edi_export` | `SMLEDIControl._ediExport` | _searchDataFull |  |

## รายงาน (71)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | ข้อมูลทั่วไป › กำหนดการเรียงข้อมูลรายงาน | `menu_ic_report_sort` | `SMLERPICReport._icReportSort` | _searchDataFull |  |
| — | ข้อมูลทั่วไป › รายงานการตรวจสอบการแก้ไขข้อมูลย้อนหลัง | `menu_report_singha_logs_trans` | `SMLFastReport._designer` |  |  |
| — | ข้อมูลทั่วไป › รายงานการยกเลิกเอกสาร | `menu_singha_report_cancel_doc` | `SMLFastReport._designer` |  |  |
| — | ข้อมูลทั่วไป › รายงานตรวจสอบรายการรายวัน ไม่พบรายละเอียดสาขา | `menu_gl_check_no_bracnch` | `SMLFastReport._designer` |  |  |
| — | สินค้า › รายการรับสินค้ากรณีอื่นๆ โดยละเอียด | `menu_singha_report_product_receive` | `SMLFastReport._designer` |  |  |
| — | สินค้า › รับโอนสินค้าสรุปตามคลัง | `menu_singha_report_product_sum_transfer` | `SMLFastReport._designer` |  |  |
| — | สินค้า › จ่ายโอนสินค้าสรุปตามคลัง | `menu_singha_report_product_sum_transferout` | `SMLFastReport._designer` |  |  |
| — | สินค้า › รายการจ่ายสินค้ากรณีอื่นๆ โดยละเอียด | `menu_singha_report_product_out_other` | `SMLFastReport._designer` |  |  |
| — | สินค้า › สรุปยอดจ่ายสินค้าออกจากคลัง | `menu_singha_report_product_sum_out_by_day` | `SMLFastReport._designer` |  |  |
| — | สินค้า › รายการการโอนสินค้าและวัตถุดิบ | `menu_singha_report_product_transfer` | `SMLFastReport._designer` |  |  |
| — | สินค้า › รายงานสโตร์ | `menu_singha_report_product_movement_store` | `SMLFastReport._designer` |  |  |
| — | สินค้า › สรุปการ์ดสินค้า | `menu_singha_report_stock_movement` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | สินค้า › สรุปโหลดสินค้า รายคลัง | `menu_singha_report_load_product_warehouse` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | ซื้อ › สรุปยอดซื้อสินค้า วิเคราะห์ตามผู้ขาย | `menu_singha_report_ap_purchase_summary_product` | `SMLFastReport._designer` |  |  |
| — | ซื้อ › รายละเอียดเจ้าหนี้ | `menu_singha_report_supplier_detail` | `SMLFastReport._designer` |  |  |
| — | ซื้อ › การ์ดเจ้าหนี้ | `menu_singha_report_supplier_card` | `SINGHAReport._singhareportGenerate` |  |  |
| — | ซื้อ › สรุปยอดเงินจ่าย | `menu_singha_report_sum_pay_money` | `SMLFastReport._designer` |  |  |
| — | ซื้อ › รายงานรับสินค้า แยกสาขา | `menu_singha_report_product_receive_by_branch` | `SMLFastReport._designer` |  |  |
| — | ซื้อ › รายงานสรุปยอดซื้อจากผู้ขาย วิเคราะห์ตามสินค้า | `menu_singha_report_pu_by_product` | `SMLFastReport._designer` |  |  |
| — | ซื้อ › ราคาซื้อสินค้าล่าสุด | `menu_singha_report_price_last_buy` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล | `menu_singha_report_sale_invoice` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปยอดขายสินค้า(QTY)ตามช่วงเวลา | `menu_singha_report_sum_sale_qty` | `SMLFastReport._designer` |  |  |
| — | ขาย › การ์ดลูกค้า | `menu_singha_report_ar_sale_card` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปยอดเงินรับ | `menu_singha_report_sum_receive_money` | `SMLFastReport._designer` |  |  |
| — | ขาย › ยอดขายสินค้า วิเคราะห์ตามลูกค้า (ไม่หักรับคืน) | `menu_singha_report_analyst_sale_customer` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (หักรับคืน) | `menu_singha_report_sale_summary_byproduct` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานขายสินค้าต่ำกว่าทุน | `menu_sing_report_sale_lessthan_cost` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานสรุปยอดขายสินค้าเรียงตามสาขา | `menu_singha_report_sale_by_branch` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานประวัติการขายสินค้า แยกสาขา | `menu_singha_report_sale_history_branch` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_singha_report_sale_summary_by_saleman` | `SINGHAReport._singhareportGenerate` |  |  |
| — | ขาย › ยอดขายสินค้า วิเคราะห์ตามลูกค้า หักรับคืน | `menu_singha_report_analyst_sale_customer_cut_return` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปยอดการส่งสินค้าตามประเภทการขนส่ง | `menu_singha_report_sum_transport_type` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานสรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า(หักรับคืน) แบบแถวเดียว | `menu_singha_report_sale_summary_byproduct_oneline` | `SMLFastReport._designer` |  |  |
| — | ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล แสดงหมายเหตุ | `menu_singha_report_sale_invoice_showremark` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานสรุปขาย/แถมรายวัน | `menu_singha_report_sale_premium_by_date` | `SMLFastReport._designer` |  |  |
| — | ขาย › ยอดขายสินค้า ตามพื้นที่ | `menu_singha_report_analyst_sale_area` | `SMLFastReport._designer` |  |  |
| — | ขาย › รายงานยอดขายรายเดือนตามกลุ่มผลิตภัณฑ์/เทียบปี | `menu_report_sale_category_year_compare` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล ตามระยะเวลาเครดิต | `menu_singha_report_sale_invoice_by_credit_day` | `SMLFastReport._designer` |  |  |
| — | ลูกหนี้ › ยอดลูกหนี้คงเหลือ | `menu_singha_report_customer_credit_balance` | `SINGHAReport._singhareportGenerate` |  |  |
| — | ลูกหนี้ › รายงานตรวจสอบยอดวงเงิน | `menu_singha_report_credit_money_check` | `SMLFastReport._designer` |  |  |
| — | ลูกหนี้ › ลูกหนี้คงค้าง | `menu_singha_report_ar_outstanding` | `SINGHAReport._singhareportGenerate` |  |  |
| — | ลูกหนี้ › รายงานที่อยู่จัดส่งลูกค้า | `menu_singha_report_transport_address` | `SMLFastReport._designer` |  |  |
| — | ลูกหนี้ › ยอดลูกหนี้คงเหลือ ตามระยะเวลาเครดิต | `menu_singha_report_customer_credit_balance_by_creditdate` | `SINGHAReport._singhareportGenerate` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › ทะเบียนรับเช็ค | `menu_singha_report_chequein_list` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › สรุปยอดรับเช็คคงเหลือ | `menu_singha_report_chequein_balance` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › สรุปยอดรับเช็ค ส่งเข้าธนาคาร | `menu_singha_report_chequein_deposit` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › สรุปเช็ครับล่วงหน้า (ผ่าน) | `menu_singha_report_chequein_pass` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › รายงานการตัดเช็ค | `report_singha_chq_receive_movement` | `SINGHAReport._singhareportGenerate` |  |  |
| — | เงินสด/ธนาคาร › เช็ครับ › รายงานรับคืน (เช็ครับ) | `menu_singha_report_chq_in_return` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › รายงาน Bank Statement | `menu_singha_report_bank_statement` | `SINGHAReport._singhareportGenerate` |  |  |
| — | เงินสด/ธนาคาร › รายงาน Bank Statement แสดงช่องทางการจ่ายเงิน | `menu_singha_report_bank_statement_show_payment_detail` | `SMLFastReport._designer` |  |  |
| — | เงินสด/ธนาคาร › รายงานค่าใช้จ่ายอื่น ๆ | `menu_singha_report_other_expenses` | `SMLFastReport._designer` |  |  |
| — | บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.3) | `menu_singha_report_product_wht_3` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.53) | `menu_singha_report_product_wht_53` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | บัญชี › รายงานภาษีซื้อ | `menu_singha_report_vat_buy` | `SINGHAReport.GL._glReportGenerate` |  |  |
| — | บัญชี › รายงานภาษีขาย | `menu_singha_report_vat_sale` | `SINGHAReport.GL._glReportGenerate` |  |  |
| — | บัญชี › สมุดบัญชีแยกประเภทเงินสด | `menu_report_cash_gl_sheet` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | บัญชี › สมุดบัญชีแยกประเงินโอน | `menu_report_transfer_gl_sheet` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | บัญชี › รายงานข้อมูลรายวัน | `menu_singha_report_journal` | `SINGHAReport.GL._glReport` | _icInfoProcess |  |
| — | บัญชี › รายงานภาษีขายสินค้าฟรี(ใบควบคุม) | `menu_singha_report_vat_free_by_issue` | `SMLFastReport._designer` |  |  |
| — | บัญชี › งบกำไรขาดทุน | `menu_singha_report_profit_and_lost` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |  |
| — | บัญชี › งบดุล | `menu_singha_report_balancesheet_asset` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |  |
| — | บัญชี › งบดุลเปรียบเทียบ | `menu_singha_report_balancesheet_compare` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | บัญชี › งบกำไร(ขาดทุน)เปรียบเทียบ | `menu_singha_report_lost_profit_compare` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (มาตรฐาน) | `menu_gl_report_trial_balance` | `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` |  |  |
| — | บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกแผนก) | `menu_gl_report_trial_balance_depart` | `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` |  |  |
| — | บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกสาขา) | `menu_gl_report_trial_balance_branch` | `SMLERPGL._report._trialBalanceBranch._report` |  |  |
| — | บัญชี › รายงานกระดาษทำการ | `menu_gl_report_balance_sheet` | `SMLERPGL._report._workSheet._report` |  |  |
| — | บัญชี › รายงานอื่น ๆ › งบกระแสเงินสด | `menu_gl_report_other_1` | `SMLERPGL._report._other_1._report` |  |  |
| — | บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา) | `menu_gl_report_profit_and_lost_branch_1` | `SMLERPGL._report._profitAndLostBranch._report` |  |  |
| — | บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา-แผนก) | `menu_gl_report_trial_balance_branch_depart` | `SMLERPGL._report._trialBalanceBranchDepart._report` |  |  |

## คลังสินค้า (16)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | ฝาก / เบิก / รับคืน สินค้า › ฝาก | `menu_wh_deposits` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 521 |
| — | ฝาก / เบิก / รับคืน สินค้า › เบิก | `menu_wh_issue` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 522 |
| — | ฝาก / เบิก / รับคืน สินค้า › รับคืน | `menu_wh_issue_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 523 |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปฝากรายลูกค้า | `menu_singha_report_wh_deposits_customer` | `SMLFastReport._designer` |  |  |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปสินค้า ค้างส่ง | `menu_singha_report_wh_accrued_out` | `SMLFastReport._designer` |  |  |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปฝาก | `menu_singha_report_summary_warehouse_deposit` | `SMLFastReport._designer` |  |  |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › เบิกฝาก | `menu_singha_report_summary_warehouse_deposit_depart` | `SMLFastReport._designer` |  |  |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปรับคืนฝาก | `menu_singha_report_summary_warehouse_depart_return` | `SMLFastReport._designer` |  |  |
| — | ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปการ์ดสินค้า VS สินค้าฝาก | `menu_singha_report_stock_balance_compare_deposit` | `SMLFastReport._designer` |  |  |
| — | ยืม / คืน ภาชนะ › ยอดยกมา ยืม ภาชนะ | `menu_wh_rent_balance` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ยืม / คืน ภาชนะ › เงินมัดจำภาชนะ | `menu_wh_rent_deposits` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ยืม / คืน ภาชนะ › คืนภาชนะ | `menu_wh_rent_return` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ยืม / คืน ภาชนะ › คืนเงินมัดจำภาชนะ | `menu_wh_rent_return_deposit` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| — | ยืม / คืน ภาชนะ › รายงาน | `menu_wh_rent_report` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 11.1.1 Pro/AccPOSPro | การส่งสินค้า › บันทึกการส่งสินค้า | `menu_shipment_load` | `SMLPPShipment._shipment` |  |  |
| 11.1.2 Pro/AccPOSPro | การส่งสินค้า › รายงานบันทึกการจัดส่ง | `menu_singha_report_shipment` | `SMLFastReport._designer` |  |  |

## Mobile Sales (64)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | Customer | `menu_saletools_customer` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Route › Route Planning | `menu_saletools_route_planning` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Route › AdHoc Jobs | `menu_saletools_adhoc_jobs` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Route › Manage Route Plan | `menu_saletools_manage_route_plan` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › VAN › Approve Invoice | `menu_saletools_approve_invoice` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Pre-Order › Approve Invoice | `menu_saletools_approve_sales_invoice` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Bill Collection › Approve Bill Collection | `menu_saletools_approve_bill_collection` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › Approve Goods Transfer | `menu_saletools_approve_goods_transfer_request` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › Approve ods Transfer | `menu_saletools_approve_ods_transfer` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › Approve ods Recieved Customer (คืน/จ่ายมัดจำ) | `menu_saletools_approve_ods_recieved_customer` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › Approve ods Issued Customer (ยืม/รับมัดจำ) | `menu_saletools_approve_ods_issued_customer` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › ods Exchange (เปลี่ยนของเสีย) | `menu_saletools_ods_exchange` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Manage Stock › Approve Goods Return | `menu_saletools_approve_goods_return` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Generate Code › Approve Code | `menu_saletools_approve_code` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Generate Code › Document Running NO | `menu_saletools_document_running_no` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Transaction › Interface SML › ods Transfer | `menu_saletools_ods_transfer` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Photo › Photo Group | `menu_saletools_photo_group` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Photo › Photos | `menu_saletools_photos` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › Heat Map | `menu_saletools_hea_map` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › View Map | `menu_saletools_view_map` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › Fleet | `menu_saletools_fleet` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › Real Time | `menu_saletools_real_time` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › Customer GPS by salesman | `menu_saletools_customer_gps_by_salesman` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Map › Map Analysis | `menu_saletools_aap_analysis` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Promotion › Promotions | `menu_saletools_promotions` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Promotion › Import Promotion | `menu_saletools_import_promotion` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Promotion › Promotion Group | `menu_saletools_promotion_group` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Promotion › Advance Price | `menu_saletools_advance_price` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Users › Web Users | `menu_saletools_web_users` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Users › Change Password | `menu_saletools_change_password` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Users › Mobile Users | `menu_saletools_mobile_users` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Users › Sync Log | `menu_saletools_sync_log` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Users › User Roles | `menu_saletools_user_roles` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Administrator › Import/Export data | `menu_saletools_import_export_data` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Administrator › Update Mobile | `menu_saletools_update_mobile` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Administrator › Import Master SML | `menu_saletools_import_master_sml` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Product | `menu_saletools_product` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Store | `menu_saletools_store` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Region | `menu_saletools_region` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › State | `menu_saletools_state` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › City | `menu_saletools_city` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Town | `menu_saletools_town` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Customer Type | `menu_saletools_customer_type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Credit Days | `menu_saletools_credit_days` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Price Level | `menu_saletools_price_level` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Adjust Money | `menu_saletools_adjust_money` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › News Type | `menu_saletools_news_type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Payment Type | `menu_saletools_payment_type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Survey Type | `menu_saletools_survey_type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Delivery Days | `menu_saletools_delivery_days` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Material Type | `menu_saletools_material_Type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Common › Display Type | `menu_saletools_display_type` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Distributor | `menu_saletools_distributor` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Company | `menu_saletools_company` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Warehouse | `menu_saletools_warehouse` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › DC State | `menu_saletools_dc_state` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › DC Section | `menu_saletools_dcsection` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Sales Area | `menu_saletools_sales_area` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Delivery Route | `menu_saletools_delivery_route` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Bank | `menu_saletools_bank` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Agent/DC › Bank Account | `menu_saletools_bank_account` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Operation › News And Documents | `menu_saletools_news_and_documents` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | Master Data › Operation › Mustlist Product | `menu_saletools_mustlist_product` | `SINGHAReport._saleToolsWebControl` |  |  |
| — | กำหนดค่าตัวแปร Mobile | `menu_saletools_14_9` | `SINGHAReport._saleToolsWebControl` |  |  |

## Data (7)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | Data ARM | `menu_sync_data_arm` | `SINGHAReport._singhaDataSyncControl` |  |  |
| — | Data Saleout | `menu_sync_data_saleout` | `SINGHAReport._singhaDataSyncControl` |  |  |
| — | Data Stock | `menu_sync_data_stock` | `SINGHAReport._singhaDataSyncControl` |  |  |
| — | สร้างการขายจากผลต่างจากการตรวจนับ | `menu_import_sale_from_stock_count_diff` | `SMLERPTransferControl._saleImportFromStockCountDiff` |  |  |
| — | สร้างรายการขายจากสรุปการขาย POS | `menu_imort_sale_from_pos_sale_report` | `SMLERPTransferControl._saleImportFromPOSSaleReport` |  |  |
| — | สร้างรายการขายจาก บิลซื้อ | `menu_imort_sale_from_purchase_bill` | `SMLERPTransferControl._salesItemsFromPurchaseBill` |  |  |
| — | Import File Cash Received Account Receivable | `menu_debt_import` | `SMLERPAPARControl._importDebtBilling` | _searchDataFull, _ar_ap_trans_screen_top, _importDebtGridControl |  |

## Mobillyst TMS (5)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | สร้างคำสั่งส่งสินค้า | `menu_mobillyst_create_delivery_order` | `SMLERPSO.mobillyst_tms._create_delivery_order` |  |  |
| — | สร้างคำสั่งส่ง-จากการรับคืนสินค้า | `menu_mobillyst_create_cn_delivery_order` | `SMLERPSO.mobillyst_tms._create_cn_delivery_order` |  |  |
| — | สร้างคำสั่งส่ง-จากการโอนสินค้า | `menu_mobillyst_create_tr_delivery_order` | `SMLERPSO.mobillyst_tms._create_transfer_delivery_order` |  |  |
| — | สร้างคำสั่งส่ง-จากการสั่งซื้อสินค้า | `menu_mobillyst_create_po_delivery_order` | `SMLERPSO.mobillyst_tms._create_po_delivery_order` |  |  |
| — | รายการสั่งส่งสินค้า | `menu_mobillyst_delivery_order_list` | `SMLERPSO.mobillyst_tms._delivery_order_list` |  |  |
