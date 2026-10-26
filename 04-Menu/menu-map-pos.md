---
tags: [sml, menu, generated]
---
# แผนที่เมนู → หน้าจอ (SMLPOS / Lite / TomYumGoong / TomYumGoongPro / Coffee)

> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` (static analysis) — อย่าแก้ด้วยมือ ข้อมูลดิบสำหรับ agent อยู่ที่ `04-Menu/menu-map-pos.json`

เมนูปลายทาง 654 รายการ จับคู่คลาสได้ 605 รายการ (92%) · เห็นตามรุ่น: POS (&6&) 569 · Lite (&7&) 244 · TYG (&8&) 249 · TYGPro (&11&) 523 · Coffee (&16&) 511

**เลข edition ใน tag ของเมนู** (`SMLERPTemplate/_templateMainForm.cs` `_menuRemoveByVersion`): 2 = SMLAccount, 3 = SMLAccountProfessional, 6 = SMLPOS/IMSPOS, 7 = POSLite, 8 = TomYumGoong, 9 = POSMED, 10 = POSStarter, 11 = TomYumGoongPro, 12 = SMLAccountPOS, **13 = SMLAccountPOSProfessional / SMLCM**, 15 = Merchant, 16 = POSCoffee · ตัวเปิดที่ยังพัฒนาอยู่ `SMLAccountPOSPro/Program.cs` ตั้ง `SMLAccountPOSProfessional` (13) (โปรเจกต์เก่า `SMLAccountPOSProfessional/` แก้ล่าสุด 2015 ตั้ง `SMLAccountPOS` = 12) — เมนูแสดงเมื่อ tag ว่าง, มีเลขของ edition, หรือเป็น `&hide&` ตรงๆ (หรือ tag OEM `&imex&`/`&singha&`, หรือเปิดใน enableMenuFeatures) แล้วจึงกรองตามสิทธิ์ผู้ใช้

**เลขเมนู** = เลข X.Y.Z ที่โปรแกรมใส่หน้าชื่อเมนู (`mainMenuChangeResource`) หลังตัดเมนูตามรุ่น — นับรวมเมนูที่ซ่อน (`&hide&`) ด้วย จึงอาจมีเลขข้าม · เลขที่ต่างกันตามรุ่นแสดงแยก เช่น `5.1 Acc/Pro · 6.1 AccPOS/AccPOSPro` · ไม่มีเลข = รุ่นเหล่านั้นไม่เห็นเมนูนี้ · ไม่รวมผลของสิทธิ์ผู้ใช้ (ตัวเลือก `show_menu_by_permission` ซ่อนเมนูแต่ไม่เปลี่ยนเลข), OEM และเมนูที่เปิดจาก service

การ route: `SMLPOS/_mainForm.cs` `_activeMenu` ตรวจสิทธิ์ → ดู tag ของเมนูตามลำดับการเช็คในโค้ด (ตัวแรกที่ตรงชนะ) → `_selectMenuXxx` → `<Module>._selectMenu._getObject(menuName)` (switch) → `new ScreenClass(...)` เปิดเป็นแท็บ · ลำดับการเช็ค tag ต่างจาก SMLAccount (เช่น `&pos&` ถูกเช็คหลัง `&so&`/`&ar&`/`&ic&`) · ตระกูล SMLAccount ดู [[menu-map]]

คอลัมน์ trans_flag แปลงจาก `_transControlTypeEnum` ที่ส่งเข้า constructor (ถ้ามี) ดู [[trans_flag]]

## เริ่มต้น (102)

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
| 1.1.9 | รายละเอียดข้อมูลทั่วไป › กำหนดผู้ใช้ระบบ MIS | `menu_setup_staff_mis` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.10 | รายละเอียดข้อมูลทั่วไป › กำหนดกลุ่มเอกสาร | `menu_setup_doc_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.11 | รายละเอียดข้อมูลทั่วไป › กำหนดรูปแบบเลขที่เอกสาร | `menu_setup_doc_format` | `_g._docFormat` |  |  |
| 1.1.12 | รายละเอียดข้อมูลทั่วไป › กำหนดประเภทการขนส่ง | `menu_setup_transport` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.13 | รายละเอียดข้อมูลทั่วไป › กำหนดเขตการขนส่ง | `menu_setup_ar_logistic_area` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.14 | รายละเอียดข้อมูลทั่วไป › กำหนดค่าจอแสดงผล QR Code | `menu_usb_qr_display_config` | `SMLERPConfig._usbQRDisplayConfigForm` |  |  |
| 1.1.15 | รายละเอียดข้อมูลทั่วไป › กำหนดค่า QR Code Payment | `menu_setup_qr_payment` | `SMLERPConfig.qrpayment._config_qr_payment_control` |  |  |
| 1.1.16 | รายละเอียดข้อมูลทั่วไป › ดึงรายชื่อจังหวัดอัตโนมัติ | `menu_setup_province_auto` | `SMLERPConfig._provinceLoadFromWebControl` |  |  |
| 1.1.17 | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสจังหวัด | `menu_setup_province` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.18 | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสอำเภอ | `menu_setup_ampher` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.19 | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสตำบล | `menu_setup_tambon` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.1.20 | รายละเอียดข้อมูลทั่วไป › กำหนดค่าเริ่มต้น POS | `menu_config_pos_startup` | `SMLPOSControl._posConfig` | _searchDataFull |  |
| 1.1.21 | รายละเอียดข้อมูลทั่วไป › กำหนดรหัสเครื่อง POS | `menu_config_pos_machine` | `SMLPOSControl._posMachine` | _myManageData, _searchDataFull |  |
| 1.1.22 | รายละเอียดข้อมูลทั่วไป › กำหนดเงื่อนไขสะสมแต้ม | `menu_pos_point_rate` | `SMLPOSControl._posPointPeriodForm` |  |  |
| 1.1.23 | รายละเอียดข้อมูลทั่วไป › กำหนดคุณสมบัติของเครื่อง POS | `menu_config_pos_screen` | `SMLPosClient._configPOSScreen` | _searchDataFull, _posScreenConfig, _screenConfig |  |
| — | รายละเอียดข้อมูลทั่วไป › กำหนดค่าฉลากยา | `menu_config_print_label_healthy` | `SMLPosClient._counSellingConfigForm` |  |  |
| 1.2.1 | ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าหลัก | `menu_setup_ic_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.2 | ระบบสินค้าคงคลัง › กำหนดกลุ่มสินค้าย่อย | `menu_setup_ic_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.3 | ระบบสินค้าคงคลัง › กำหนดยี่ห้อสินค้า | `menu_setup_ic_brand` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.4 | ระบบสินค้าคงคลัง › กำหนดรุ่นสินค้า | `menu_setup_ic_model` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.5 | ระบบสินค้าคงคลัง › กำหนดสีสินค้า | `menu_setup_ic_color` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.6 | ระบบสินค้าคงคลัง › กำหนดขนาดสินค้า | `menu_setup_ic_size` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.7 | ระบบสินค้าคงคลัง › กำหนดรูปแบบสินค้า | `menu_setup_ic_pattern` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.8 | ระบบสินค้าคงคลัง › กำหนดเกรดสินค้า | `menu_setup_ic_grade` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.9 | ระบบสินค้าคงคลัง › กำหนดหมวดสินค้า | `menu_setup_ic_category` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.10 | ระบบสินค้าคงคลัง › กำหนดรูปทรงสินค้า | `menu_setup_ic_design` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.11 | ระบบสินค้าคงคลัง › กำหนดชื่อมิติสินค้า | `menu_setup_ic_dimension_name` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.12 | ระบบสินค้าคงคลัง › กำหนดมิติสินค้า | `menu_setup_ic_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.13 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › ประเภทรายได้ | `menu_income_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.14 POS/TYG/TYGPro/Coffee · 1.2.13 Lite | ระบบสินค้าคงคลัง › กำหนดระดับสินค้า | `menu_setup_ic_class` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.15 POS/TYG/TYGPro/Coffee · 1.2.14 Lite | ระบบสินค้าคงคลัง › กำหนดหน่วยนับสินค้า | `menu_setup_ic_unit` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.16 POS/TYG/TYGPro/Coffee · 1.2.15 Lite | ระบบสินค้าคงคลัง › กำหนดคลังสินค้า | `menu_setup_ic_wh` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.17 POS/TYG/TYGPro/Coffee · 1.2.16 Lite | ระบบสินค้าคงคลัง › กำหนดพื้นที่เก็บสินค้า | `menu_setup_ic_shelf` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.18 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › กำหนดกลุ่มบัญชีสินค้า | `menu_setup_ic_account_group` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.2.19 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › กำหนดพิกัดศุลกากร | `menu_setup_ic_import_duty_point` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.20 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › กำหนดประเภทการเบิก | `menu_setup_ic_issue_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.21 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › กำหนดสาเหตุการปรับปรุง | `menu_setup_stk_adjust` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.22 POS/TYG/TYGPro/Coffee | ระบบสินค้าคงคลัง › กำหนดเหตุผลการปิดสินค้า | `menu_setup_ic_close_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.2.23 POS/TYG/TYGPro/Coffee · 1.2.17 Lite | ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ | `ic_auto_add_warehouse_and_location` | `_g._ic_add_warehouse_shelf_form` |  |  |
| 1.3.1 POS/TYGPro/Coffee | ระบบขาย › กำหนดรายได้อื่นๆ | `menu_setup_other_income` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.3.2 POS/TYGPro/Coffee | ระบบขาย › กำหนดเขตการขาย | `menu_setup_ar_sale_area` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.3.3 POS/TYGPro/Coffee | ระบบขาย › ออกแบบหน้าจอขาย POS | `client_design` | `SMLPOSControl._designer._clientDesign` | _searchDataFull |  |
| 1.3.4 POS/TYGPro/Coffee · 1.3.1 Lite/TYG | ระบบขาย › Download ระบบเสียงพูด | `menu_pos_sound_download_install` | `SMLPOSControl._posDownloadSound` |  |  |
| 1.3.2 Lite/TYG · 1.3.5 TYGPro/Coffee | ระบบขาย › ประเภทบัตรเครดิต | `menu_setup_credit_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.4.1 POS/TYGPro/Coffee | ระบบซื้อ › กำหนดรายจ่ายอื่นๆ | `menu_expenses_list` | `SMLERPConfig._expenses_list` | _myManageData, _searchDataFull |  |
| 1.5.1 POS/TYGPro/Coffee · 1.4.1 Lite/TYG | ระบบเจ้าหนี้ › กำหนดประเภทเจ้าหนี้ | `menu_setup_ap_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.2 POS/TYGPro/Coffee | ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้หลัก | `menu_setup_ap_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.3 POS/TYGPro/Coffee | ระบบเจ้าหนี้ › กำหนดกลุ่มเจ้าหนี้ย่อย | `menu_setup_ap_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.5.4 POS/TYGPro/Coffee | ระบบเจ้าหนี้ › กำหนดมิติเจ้าหนี้ | `menu_setup_ap_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.1 POS/TYGPro/Coffee · 1.5.1 Lite/TYG | ระบบลูกหนี้ › กำหนดประเภทลูกหนี้ | `menu_setup_ar_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.2 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้หลัก | `menu_setup_ar_group_main` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.3 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดกลุ่มลูกหนี้ย่อย | `menu_setup_ar_group_sub` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.4 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดมิติลูกหนี้ | `menu_setup_ar_dimension` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.5 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดเหตุผลอนุมัติวงเงิน | `menu_setup_ar_credit_approve` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.6 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดเงื่อนไขการวางบิล | `menu_setup_ar_pay_bill_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.7 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดเงื่อนไขการรับเช็ค | `menu_setup_ar_keep_chq_reason` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.8 POS/TYGPro/Coffee | ระบบลูกหนี้ › กำหนดเงือนไขการชำระเงิน | `menu_setup_ar_keep_money` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.6.9 POS/TYGPro/Coffee · 1.5.2 TYG | ระบบลูกหนี้ › สัญชาติ | `menu_setup_healthy_m_nationality` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.1 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › กำหนดธนาคาร | `menu_setup_bank` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.2 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › กำหนดสาขาธนาคาร | `menu_setup_bank_branch` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.3 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › ประเภทสมุดเงินฝาก | `menu_book_bank_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.4 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › ตัวย่อในสมุดเงินฝาก | `menu_book_bank_trans_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.5 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › กำหนดประเภทรายได้ | `menu_income_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.6 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › กำหนดประเภทค่าใช้จ่าย | `menu_expenses_list` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.7 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › ประเภทบัตรเครดิต | `menu_setup_credit_type` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 1.7.8 POS/TYGPro/Coffee | ระบบเงินสด-ธนาคาร › กำหนดเงินวงสดย่อย | `menu_petty_cash` | `SMLERPCASHBANK._cb_petty_cash` |  |  |
| 1.8 POS/TYGPro/Coffee | สร้าง/แก้ไขแบบฟอร์ม | `menu_form_edit` | `SMLReport._formReport._formDesigner` |  |  |
| 1.9 POS/TYGPro/Coffee | ออกแบบรายงาน | `fast_report_designer` | `SMLFastReport._designer` |  |  |
| 1.10.1.1 POS/TYGPro/Coffee · 1.6.1.1 Lite/TYG | เครื่องมือ › ระบบข้อมูล › กำหนดรูปแบบการค้นหาข้อมูล | `menu_view_manager_custom` | `_g._viewManageCustom` | _myManageData |  |
| 1.10.1.2 POS/TYGPro/Coffee · 1.6.1.2 Lite/TYG | เครื่องมือ › ระบบข้อมูล › ตรวจสอบโครงสร้างฐานข้อมูล | `menu_verify_database` | `MyLib._databaseManage._verifyDatabase` |  |  |
| 1.10.1.3 POS/TYGPro/Coffee · 1.6.1.3 Lite/TYG | เครื่องมือ › ระบบข้อมูล › ลดขนาดข้อมูล | `menu_shink_database` | `MyLib._databaseManage._shrinkDatabase` |  |  |
| 1.10.1.4 POS/TYGPro/Coffee · 1.6.1.4 Lite/TYG | เครื่องมือ › ระบบข้อมูล › สำรองข้อมูล | `data_backup` | `MyLib._databaseManage._dataBackupForm` |  |  |
| 1.10.1.5 POS/TYGPro/Coffee · 1.6.1.5 Lite/TYG | เครื่องมือ › ระบบข้อมูล › นำข้อมูลสำรองกลับมาใช้ | `data_restore` | `MyLib._databaseManage._dataRestoreForm` |  |  |
| 1.10.1.6 POS/TYGPro/Coffee · 1.6.1.6 Lite/TYG | เครื่องมือ › ระบบข้อมูล › เปลี่ยนรหัสผ่าน | `menu_change_password` | `MyLib._databaseManage._smlChangePassword` |  |  |
| ซ่อน | เครื่องมือ › ระบบข้อมูล › กำหนดผู้มีสิทธิเข้าใช้ข้อมูล | `Node9` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ซ่อน | เครื่องมือ › ระบบข้อมูล › กำหนดสิทธิการใช้งาน | `Node10` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 1.10.1.9 POS/TYGPro/Coffee · 1.6.1.9 Lite/TYG | เครื่องมือ › ระบบข้อมูล › แสดงโครงสร้างฐานข้อมูลทั้งหมด | `menu_database_struct` | `MyLib._databaseManage._databaseStruct` |  |  |
| 1.10.1.10 POS/TYGPro/Coffee · 1.6.1.10 Lite/TYG | เครื่องมือ › ระบบข้อมูล › ตรวจสอบและปรับปรุงข้อมูล | `menu_checking_ic_trans` | `SMLERPICInfo._icTransectionCheck` |  |  |
| 1.10.1.11 POS/TYGPro/Coffee · 1.6.1.11 Lite/TYG | เครื่องมือ › ระบบข้อมูล › ใช้คำสั่ง Query | `menu_query` | `MyLib._databaseManage._queryDataView` |  |  |
| 1.10.2.1 POS/TYGPro/Coffee · 1.6.2.1 Lite/TYG | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสสินค้า | `menu_change_code_item` | `_g._changeCode._itemCodeUserControl` | _searchDataFull |  |
| 1.10.2.2 POS/TYGPro/Coffee · 1.6.2.2 Lite/TYG | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสเจ้าหนี้ | `menu_change_code_supplier` | `_g._changeCode._changeApArCodeUserControl` | _searchDataFull |  |
| 1.10.2.3 POS/TYGPro/Coffee · 1.6.2.3 Lite/TYG | เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสลูกหนี้/ลูกค้า | `menu_change_code_customer` | `_g._changeCode._changeApArCodeUserControl` | _searchDataFull |  |
| 1.10.3 POS/TYGPro/Coffee · 1.6.3 Lite/TYG | เครื่องมือ › แสดงหน้าจอการใช้งาน | `menu_view_capture_screen_realtime` | `_viewCapture._viewScreen` |  |  |
| 1.10.4 POS/TYGPro/Coffee · 1.6.4 Lite/TYG | เครื่องมือ › นำเข้าแบบฟอร์ม | `menu_import_formdesign` | `SMLReport._ImportFormDesign` |  |  |
| 1.10.5.1 POS/TYGPro/Coffee · 1.6.5.1 Lite/TYG | เครื่องมือ › ประวัติการใช้งาน › แสดงหน้าจอการใช้งาน (ย้อนหลัง) | `menu_view_capture_screen` | `_viewCapture._viewCaptureScreen` |  |  |
| 1.10.5.2 POS/TYGPro/Coffee · 1.6.5.2 Lite/TYG | เครื่องมือ › ประวัติการใช้งาน › เข้าใช้ฐานข้อมูล | `menu_audit_login` | `SMLERPAudit._loginLog` |  |  |
| 1.10.5.3 POS/TYGPro/Coffee · 1.6.5.3 Lite/TYG | เครื่องมือ › ประวัติการใช้งาน › เข้าออกระบบ | `menu_audit_menu` | `SMLERPAudit._menuLog` |  |  |
| 1.10.5.4 POS/TYGPro/Coffee · 1.6.5.4 Lite/TYG | เครื่องมือ › ประวัติการใช้งาน › ข้อมูลรายวัน | `menu_audit_trans` | `SMLERPAudit._transLog` |  |  |
| 1.10.6 POS/TYGPro/Coffee · 1.6.6 Lite/TYG | เครื่องมือ › นำเข้าข้อมูลหลัก | `menu_import_data_master` | `MyLib._databaseManage._importDataControl` |  |  |
| 1.10.7 POS/TYGPro/Coffee · 1.6.7 Lite/TYG | เครื่องมือ › นำเข้ารายงาน | `menu_import_report` | `SMLFastReport._importFastReport` |  |  |
| 1.10.8 POS/TYGPro/Coffee · 1.6.8 Lite/TYG | เครื่องมือ › นำเข้ารายงานสาขา | `menu_import_report_branch` | `SMLFastReport._importFastReport` |  |  |
| 1.10.9 POS/TYGPro/Coffee · 1.6.9 TYG | เครื่องมือ › นำเข้ารูปภาพสินค้า | `menu_import_ic_picture` | `SMLERPIC._icImportPicture` |  |  |
| 1.10.10 POS/TYGPro/Coffee · 1.6.9 Lite · 1.6.10 TYG | เครื่องมือ › หน้าจอเริ่มต้น | `menu_welcome_page` | `SMLAccount._mainShortcut` |  |  |
| 1.10.11 POS/TYGPro/Coffee · 1.6.10 Lite · 1.6.11 TYG | เครื่องมือ › ย้ายรูปภาพสินค้า | `menu_tools_image_transfer` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |

## สินค้า (131)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | ข้อมูลสินค้า | `menu_ic_item_detail` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| — | ข้อมูลสินค้า (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_barcode` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| — | กำหนดบาร์โค้ดสินค้า | `menu_ic_item_barcode` | `SMLERPIC._icBarcode` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| — | ตรวจสอบราคาสินค้า | `check_price` | `SMLPOSControl._checkPriceUserControl` |  |  |
| 2.1.1 | ข้อมูลสินค้า › ข้อมูลสินค้า | `menu_ic_item_detail` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.2 | ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_barcode` | `SMLERPIC._icMain` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.3 | ข้อมูลสินค้า › ข้อมูลสินค้า (เพิ่มเติม) | `menu_ic_item_detail_2` | `SMLERPIC._icMainDetail` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.4 | ข้อมูลสินค้า › ข้อมูลสินค้าเพิ่มเติม (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_2_barcode` | `SMLERPIC._icMainDetail` | _myManageData, _barcodeSearchForm, _icPictureForm |  |
| 2.1.5 | ข้อมูลสินค้า › รายละเอียดสินค้า | `menu_ic_description` | `SMLERPIC._icDescription` | _myManageData, _icmainScreenTopControl |  |
| 2.1.6 | ข้อมูลสินค้า › แก้ไขรายละเอียด(เร็ว) | `menu_ic_description_fast` | `SMLERPIC._icEditDetailFast` | _myManageData, _icmainScreenDescripControl, _icmainScreenDimesionControl |  |
| 2.1.7 | ข้อมูลสินค้า › กำหนดบาร์โค้ดสินค้า | `menu_ic_item_barcode` | `SMLERPIC._icBarcode` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.1.8 | ข้อมูลสินค้า › กำหนดรูปภาพ | `menu_ic_item_picture` | `SMLERPIC._icMainDetailPicture` | _myManageData, _barcodeSearchForm, _getPicture |  |
| 2.1.9 | ข้อมูลสินค้า › กำหนดรูปภาพตามบาร์โค้ด | `menu_ic_item_barcode_picture` | `SMLERPIC._icBarcodePicture` | _myManageData, _getPicture, _icmainScreenTopControl |  |
| 2.1.10 | ข้อมูลสินค้า › กำหนดสูตรโปรโมชั่น | `pos_promotion_formula` | `SMLERPIC._icPromotion._formula` | _myManageData |  |
| 2.1.11 | ข้อมูลสินค้า › กำหนดแคมเปญท้ายใบเสร็จ | `menu_setup_pos_slip_campaign` | `SMLERPControl.pos_slip_campaign.pos_slip_campaign` |  |  |
| 2.1.12 | ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด | `menu_ic_item_barcode_discount` | `SMLERPIC._icBarcodeDiscount` | _myManageData |  |
| 2.1.13 | ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด (เร็ว) | `menu_ic_item_multibarcode_discount` | `SMLERPIC._icMultiBarcodeDiscount` | _myManageData |  |
| 2.1.14 | ข้อมูลสินค้า › กำหนดลำดับการค้นหา | `menu_ic_item_level` | `SMLERPIC._icSearchLevel` | _myManageData, _barcodeSearchForm, _itemSearchLevelControl |  |
| 2.1.15 | ข้อมูลสินค้า › กำหนดลำดับการค้นหา (เร็ว) | `menu_ic_multi_item_level` | `SMLERPIC._icSearchLevelMultiItem` | _myManageData, _itemSearchLevelControl |  |
| 2.1.16 | ข้อมูลสินค้า › จัดเรียงลำดับการค้นหา | `menu_ic_search_level_sort` | `SMLERPIC._icSearchLevelSort` |  |  |
| 2.1.17 | ข้อมูลสินค้า › กำหนดกลุ่มส่วนลด | `menu_ic_discount_group` | `SMLERPIC.ic_discount_group` |  |  |
| 2.1.18 | ข้อมูลสินค้า › ตรวจสอบราคาสินค้า | `check_price` | `SMLPOSControl._checkPriceUserControl` |  |  |
| 2.1.19 POS | ข้อมูลสินค้า › ทะเบียน Serial Number | `menu_ic_item_serial` | `SMLERPIC._icSerialNumber` | _myManageData, _icSerialNumerScreen |  |
| 2.1.20 POS · 2.1.19 TYGPro/Coffee | ข้อมูลสินค้า › สินค้าชุด | `menu_ic_item_set` | `SMLERPIC._icMainProductSet` | _myManageData, _icmainScreenTopControl, _icTransItemGridControl |  |
| 2.1.21 POS · 2.1.19 Lite/TYG · 2.1.20 TYGPro/Coffee | ข้อมูลสินค้า › เพิ่มบาร์โค๊ดสินค้าแบบเร็ว | `menu_ic_item_add_barcode_fast` | `SMLERPIC._icAddBarcodeFastControl` | _searchDataFull, _selectWarehouseAndLocationForm, GetItemCodeEventHandler |  |
| 2.1.22 POS · 2.1.20 Lite/TYG · 2.1.21 TYGPro/Coffee | ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดจาก Text File | `menu_ic_item_barcode_checker` | `SMLERPIC._barcodeCheckerControl` |  |  |
| 2.1.23 POS · 2.1.21 Lite/TYG · 2.1.22 TYGPro/Coffee | ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดตามมาตรฐาน EAN13 | `menu_ic_item_barcode_checker_ean13` | `SMLBarcodeManage._itemBarcodeCheckerEan13` |  |  |
| 2.1.24 POS · 2.1.22 Lite/TYG · 2.1.23 TYGPro/Coffee | ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป | `menu_ic_item_barcode_laser_print` | `SMLBarcodeManage._itemBarcodePrint` | _getImageData | 501 |
| 2.1.25 POS | ข้อมูลสินค้า › กำหนดสูตร | `menu_ic_item_color_set` | `SMLERPIC._icMainColorSet` | _myManageData, _icmainScreenTopControl, _icTransItemGridControl |  |
| — | ข้อมูลสินค้า › รายละเอียดยาและอาหารสุขภาพ | `menu_healthy_m_information` | `SMLHealthyControl._healthyControl.M_information` | _myManageData |  |
| 2.1.26.1 POS | ข้อมูลสินค้า › รายงาน › รายงานรายละเอียดสินค้า | `menu_ic_detail` | `SMLERPICReport._report_ic_master` |  |  |
| 2.1.26.2 POS | ข้อมูลสินค้า › รายงาน › รายงานสินค้าชุด | `menu_ic_report_item_set_formula` | `SMLERPICReport._report_item_set_formula` |  |  |
| 2.1.26.3 POS | ข้อมูลสินค้า › รายงาน › รายงานบาร์โค้ดสินค้า | `menu_ic_report_item_barcode` | `SMLERPICReport._report_ic_barcode` |  |  |
| 2.1.26.4 POS | ข้อมูลสินค้า › รายงาน › รายงานสินค้าแบบมี Serial | `menu_ic_by_license` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_by_serial |
| 2.1.27 POS · 2.1.23 TYG · 2.1.24 TYGPro/Coffee | ข้อมูลสินค้า › ปรับราคาสินค้า | `menu_ic_modify_price` | `SMLERPIC._icModifyPrice` |  |  |
| 2.1.28 POS · 2.1.23 Lite · 2.1.24 TYG · 2.1.25 TYGPro/Coffee | ข้อมูลสินค้า › สูตรการผลิต | `menu_ic_production_formula` | `SMLERPIC._ic_production_formula` | _myManageData, _searchItemForm |  |
| 2.2 POS | กำหนดราคาซื้อ | `menu_ic_purchase_price` | `SMLInventoryControl._icPurchasePrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.3 POS | ของแถมซื้อ | `menu_ic_purchase_premium` | `SMLERPIC._icPurchasePermium` | _myManageData, _icTransItemGridControl |  |
| 2.4 POS | กำหนดราคาขายมาตรฐาน | `menu_ic_item_saleprice` | `SMLInventoryControl._icPrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.5 POS | กำหนดราคาขายทั่วไป | `menu_ic_item_saleprice_2` | `SMLInventoryControl._icPrice._icPriceList` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.6 POS · 2.2 TYGPro/Coffee | กำหนดรูปแบบสูตรราคาขาย | `menu_ic_item_formula_template` | `SMLInventoryControl._icPrice._icPriceFormulaTemplate` |  |  |
| 2.7 POS · 2.3 TYGPro/Coffee | กำหนดสูตรราคาขาย | `menu_ic_item_saleprice_formula` | `SMLInventoryControl._icPrice._icPriceFormula` | _myManageData, _barcodeSearchForm, _icmainScreenTopControl |  |
| 2.8 POS · 2.4 TYGPro/Coffee | ปรับปรุงราคาสินค้า | `menu_ic_price_adjust` | `SMLInventoryControl._icPriceManage._icPriceManageList` |  |  |
| 2.2.1 Lite/TYG · 2.5.1 TYGPro/Coffee | รายงาน › รายงานรายละเอียดสินค้า | `menu_ic_detail` | `SMLERPICReport._report_ic_master` |  |  |
| 2.2.2 Lite/TYG · 2.5.2 TYGPro/Coffee | รายงาน › รายงานบาร์โค้ดสินค้า | `menu_ic_report_item_barcode` | `SMLERPICReport._report_ic_barcode` |  |  |
| 2.9.1 POS | รายงาน › รายงานราคาซื้อสินค้า | `menu_ic_report_item_purchase_price` | `SMLERPICReport._report_ic_purchase_price` |  |  |
| — | รายงาน › รายงานของแถมซื้อ | `menu_ic_report_item_giveaway` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_Giveaway |
| 2.9.2 POS | รายงาน › รายงานราคาขายสินค้ามาตรฐาน | `menu_ic_report_item_sale_price` | `SMLERPICReport._report_ic_sale_price` |  |  |
| 2.9.3 POS | รายงาน › รายงานราคาขายสินค้าทั่วไป | `menu_ic_report_item_sale_price_normal` | `SMLERPICReport._report_ic_sale_price` |  |  |
| 2.10 POS · 2.3 Lite/TYG · 2.6 TYGPro/Coffee | สินค้า/วัตถุดิบ คงเหลือยกมา | `menu_ic_stk_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 54 |
| 2.11 POS · 2.4 Lite/TYG · 2.7 TYGPro/Coffee | รับสินค้าสำเร็จรูป | `menu_ic_finish_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 60 |
| 2.12 POS · 2.5 Lite/TYG · 2.8 TYGPro/Coffee | เบิกสินค้า/วัตถุดิบ | `menu_ic_issue` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 56 |
| 2.13 POS · 2.6 Lite/TYG · 2.9 TYGPro/Coffee | รับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 58 |
| 2.14.1 POS · 2.7.1 Lite/TYG · 2.10.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_finish_receive_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 61 |
| 2.14.2 POS · 2.7.2 Lite/TYG · 2.10.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_issue_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 57 |
| 2.14.3 POS · 2.7.3 Lite/TYG · 2.10.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 59 |
| 2.14.4 POS · 2.7.4 Lite/TYG · 2.10.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_report_cancel_goods_pack` | `SMLERPReportTool._reportTrans` |  | 61 |
| 2.14.5 POS · 2.7.5 Lite/TYG · 2.10.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_report_cancel_raw_material` | `SMLERPReportTool._reportTrans` |  | 57 |
| 2.14.6 POS · 2.7.6 Lite/TYG · 2.10.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_report_cancel_goods_raw_meterial` | `SMLERPReportTool._reportTrans` |  | 59 |
| 2.14.7 POS · 2.7.7 Lite/TYG · 2.10.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานสินค้าและวัตถุดิบ คงเหลือยกมา | `menu_ic_report_goods_balance` | `SMLERPReportTool._reportTrans` |  | 54 |
| 2.14.8 POS · 2.7.8 Lite/TYG · 2.10.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับสินค้าสำเร็จรูป | `menu_import_item_ready_by_date` | `SMLERPReportTool._reportTrans` |  | 60 |
| 2.14.9 POS · 2.7.9 Lite/TYG · 2.10.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการเบิกสินค้าและวัตถุดิบ | `menu_ic_report_item_withdraw` | `SMLERPReportTool._reportTrans` |  | 56 |
| 2.14.10 POS · 2.7.10 Lite/TYG · 2.10.10 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานรับคืนสินค้าและวัตถุดิบ จากการเบิก | `menu_ic_report_item_return` | `SMLERPReportTool._reportTrans` |  | 58 |
| 2.15 POS · 2.8 Lite/TYG · 2.11 TYGPro/Coffee | โอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 72 |
| 2.16 POS · 2.9 Lite/TYG · 2.12 TYGPro/Coffee | ตรวจนับสินค้า | `menu_ic_stk_count` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 76 |
| 2.17 POS | ตรวจสอบสินค้า Serial Number | `menu_ic_serialnumber_checker` | `SMLERPIC._icSerialStockCheck` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.18 POS · 2.10 Lite/TYG · 2.13 TYGPro/Coffee | ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ | `menu_ic_stk_adjust_auto` | `SMLInventoryControl._stockAutoAdjustControl` |  |  |
| 2.19 POS · 2.11 Lite/TYG · 2.14 TYGPro/Coffee | ปรับปรุงสต็อกสินค้า/วัตถุดิบ | `menu_ic_stk_adjust` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 66 |
| 2.20.1 POS · 2.12.1 Lite/TYG · 2.15.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 73 |
| 2.20.2 POS · 2.12.2 Lite/TYG · 2.15.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_stk_adjust_over_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 67 |
| 2.20.3 POS · 2.12.3 Lite/TYG · 2.15.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_stk_adjust_lost_cancel` | `SMLERPIC._cancelControl` | _icTransControl | 69 |
| 2.20.4 POS · 2.12.4 Lite/TYG · 2.15.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_report_stk_cancel` | `SMLERPReportTool._reportTrans` |  | 73 |
| 2.20.5 POS · 2.12.5 Lite/TYG · 2.15.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_report_stk_cancel_over` | `SMLERPReportTool._reportTrans` |  | 67 |
| 2.20.6 POS · 2.12.6 Lite/TYG · 2.15.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_report_stk_cancel_lost` | `SMLERPReportTool._reportTrans` |  | 69 |
| 2.20.7 POS · 2.12.7 Lite/TYG · 2.15.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการโอนสินค้าและวัตถุดิบ | `menu_ic_report_item_transfer` | `SMLERPReportTool._reportTrans` |  | 72 |
| 2.20.8 POS | รายงาน/ยกเลิก › รายงานตรวจนับสินค้า | `menu_ic_report_item_count` | `SMLERPReportTool._reportTrans` |  | 76 |
| 2.20.9 POS · 2.12.8 Lite/TYG · 2.15.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการปรับปรุงสต็อกสินค้าและวัตถุดิบ (เกิน) | `menu_ic_report_item_adjust_increase` | `SMLERPReportTool._reportTrans` |  | 66 |
| 2.20.10 POS · 2.12.9 Lite/TYG · 2.15.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) | `menu_ic_report_item_adjust_decrease` | `SMLERPReportTool._reportTrans` |  | 68 |
| 2.21.1 POS · 2.13.1 Lite/TYG · 2.16.1 TYGPro/Coffee | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้า | `menu_ic_info_stk_balance` | `SMLERPICInfo._stkBalance` | _icBalanceForm, _icInfoProcess, _selectWarehouseAndLocationForm |  |
| 2.21.2 POS · 2.13.2 Lite/TYG · 2.16.2 TYGPro/Coffee | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามคลัง | `menu_ic_info_stk_balance_warehouse` | `SMLERPICInfo._stkBalanceWareHouse` | _selectWarehouseAndLocationForm |  |
| 2.21.3 POS · 2.13.3 Lite/TYG · 2.16.3 TYGPro/Coffee | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามที่เก็บ | `menu_ic_info_stk_balance_shelf` | `SMLERPICInfo._stkBalanceLocation` | _selectWarehouseAndLocationForm |  |
| 2.21.4 POS | วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตาม LOT | `menu_ic_info_stk_balance_lot` | `SMLERPICInfo._stkBalanceByLot` | _icInfoProcess |  |
| 2.21.5 POS · 2.13.4 Lite/TYG · 2.16.4 TYGPro/Coffee | วิเคราะห์ข้อมูล › เคลื่อนไหวสินค้า | `menu_ic_info_stk_move` | `SMLERPICInfo._stkMovement` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.21.6 POS · 2.13.5 Lite/TYG · 2.16.5 TYGPro/Coffee | วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ (เคลื่อนไหว) | `menu_ic_info_stk_movement` | `SMLERPICInfo._stkMovement` | _searchDataFull, _selectWarehouseAndLocationForm |  |
| 2.21.7 POS · 2.13.6 Lite/TYG · 2.16.6 TYGPro/Coffee | วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามปริมาณ | `menu_ic_info_stk_movement_sum` | `SMLERPICInfo._stkMovementSum` | _icInfoProcess |  |
| 2.21.8 POS · 2.13.7 Lite/TYG · 2.16.7 TYGPro/Coffee | วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามมูลค่า | `menu_ic_info_stk_movement_sum_by_amount` | `SMLERPICInfo._stkMovementSum` | _icInfoProcess |  |
| 2.21.9 POS · 2.13.8 Lite/TYG · 2.16.8 TYGPro/Coffee | วิเคราะห์ข้อมูล › สินค้าถึงจุดสั่งซื้อ | `menu_ic_info_stk_reorder` | `SMLInventoryControl._stkReorder` | _searchDataFull, _stkReorderConditionScreen |  |
| 2.21.10 POS | วิเคราะห์ข้อมูล › ประวัติการซื้อสินค้า | `menu_ic_info_purchase_history` | `SMLInventoryControl._transHistory` | _searchDataFull, _saleHistoryConditionScreen |  |
| 2.21.11 POS · 2.13.9 Lite/TYG · 2.16.9 TYGPro/Coffee | วิเคราะห์ข้อมูล › ประวัติการขายสินค้า | `menu_ic_info_sale_history` | `SMLInventoryControl._transHistory` | _searchDataFull, _saleHistoryConditionScreen |  |
| 2.21.12 POS · 2.13.10 Lite/TYG · 2.16.10 TYGPro/Coffee | วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการเคลื่อนไหว | `menu_ic_info_product_no_movement` | `SMLERPICInfo._stkNoMovement` | _icInfoProcess |  |
| 2.21.13 POS · 2.13.11 Lite/TYG · 2.16.11 TYGPro/Coffee | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามสินค้า | `menu_ic_info_stk_profit` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.21.14 POS · 2.13.12 Lite/TYG · 2.16.12 TYGPro/Coffee | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามเอกสารขาย | `menu_ic_info_stk_profit_by_doc` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.21.15 POS · 2.13.13 Lite/TYG · 2.16.13 TYGPro/Coffee | วิเคราะห์ข้อมูล › กำไรขั้นต้นตามลูกค้า | `menu_ic_info_stk_profit_by_ar` | `SMLERPICInfo._stkProfit` | _icTransControl |  |
| 2.21.16 POS · 2.13.14 Lite/TYG · 2.16.14 TYGPro/Coffee | วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการขาย | `IC_INVENTORY_NO_SALE` | `SMLFastReport._designer` |  |  |
| 2.21.17 POS · 2.13.15 Lite/TYG · 2.16.15 TYGPro/Coffee | วิเคราะห์ข้อมูล › ตรวจสอบ Serial มีปัญหา | `menu_ic_serial_analyze` | `SMLERPICInfo._icSerialAnalyze` |  |  |
| 2.22.1 POS · 2.14.1 Lite/TYG · 2.17.1 TYGPro/Coffee | รายงานสรุป › รายงานสถานะสินค้า | `menu_item_status` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_status |
| 2.22.2 POS · 2.14.2 Lite/TYG · 2.17.2 TYGPro/Coffee | รายงานสรุป › รายงานบัญชีคุมพิเศษสินค้า | `menu_account_special_item` | `SMLERPICReport._report_ic_stk_movement` | _icInfoProcess | สินค้า_รายงานบัญชีคุมพิเศษ |
| 2.22.3 POS · 2.14.3 Lite/TYG · 2.17.3 TYGPro/Coffee | รายงานสรุป › รายงานผลต่างจากการตรวจนับ | `menu_diff_from_count` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | รายงานผลต่างจากการตรวจนับ |
| 2.22.4 POS · 2.14.4 Lite/TYG · 2.17.4 TYGPro/Coffee | รายงานสรุป › รายงานสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ | `menu_stock_no_balance_from_count` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Stock_no_count_no_balance |
| 2.22.5 POS · 2.14.5 Lite/TYG · 2.17.5 TYGPro/Coffee | รายงานสรุป › รายงานการปรับปรุงสินค้า | `menu_report_inventory_adjust` | `SMLFastReport._designer` |  |  |
| 2.22.6 POS · 2.14.6 Lite/TYG · 2.17.6 TYGPro/Coffee | รายงานสรุป › รายงาน Lot สินค้า | `menu_report_lot_inventory` | `SMLFastReport._designer` |  |  |
| 2.22.7 POS · 2.14.7 Lite/TYG · 2.17.7 TYGPro/Coffee | รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_report_ic_product_and_material` | `SMLERPICReport._report_ic_product_and_material` | _icInfoProcess |  |
| 2.23.1 POS | รายงานวิเคราะห์ › รายงานเคลื่อนไหว Serial Number | `menu_ic_serial_number` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Serial_number |
| 2.23.2 POS | รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างส่ง | `menu_result_item_export` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.23.3 POS | รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างรับ | `menu_result_item_import` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.23.4 POS · 2.15.1 Lite/TYG · 2.18.1 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า | `menu_item_balance` | `SMLERPICReport._report_ic_balance` | _icInfoProcess | สินค้า_รายงานยอดคงเหลือสินค้า |
| 2.23.5 POS · 2.15.2 Lite/TYG · 2.18.2 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าที่ถึงจุดสั่งซื้อ | `menu_ic_report_info_stk_reorder` | `SMLERPICReport.ic_analysis._report_ic_stk_reorder` | _icInfoProcess | สินค้า_ถึงจุดสั่งซื้อ_ตามสินค้า |
| 2.23.6 POS · 2.15.3 Lite/TYG · 2.18.3 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_max` | `SMLFastReport._designer` |  |  |
| 2.23.7 POS · 2.15.4 Lite/TYG · 2.18.4 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_min` | `SMLFastReport._designer` |  |  |
| 2.23.8 POS · 2.15.5 Lite/TYG · 2.18.5 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_max` | `SMLFastReport._designer` |  |  |
| 2.23.9 POS · 2.15.6 Lite/TYG · 2.18.6 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_min` | `SMLFastReport._designer` |  |  |
| 2.23.10 POS | รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า ณ ปัจจุบัน(เฉพาะสินค้ามี Serial) | `menu_item_balance_now_only_serial` | `SMLERPICReport._report_ic_summary` | _icInfoProcess | Item_Balance_now_Only_Serial |
| 2.23.11 POS · 2.15.7 Lite/TYG · 2.18.7 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าที่ไม่มีการเคลื่อนไหว | `menu_item_non_transfer` | `SMLERPICReport._report_ic_none_movement` | _icInfoProcess |  |
| 2.23.12 POS · 2.15.8 Lite/TYG · 2.18.8 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้า | `menu_item_transfer` | `SMLERPICReport._report_ic_stk_movement` | _icInfoProcess | สินค้า_รายงานเคลื่อนไหว |
| 2.23.13 POS · 2.15.9 Lite/TYG · 2.18.9 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า | `menu_result_transfer_item` | `SMLERPICReport._report_ic_info_stk_movement_sum` | _icInfoProcess |  |
| 2.23.14 POS | รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้าต้นทุนมาตรฐาน | `menu_item_transfer_standard` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 2.24.1 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้นตามเอกสาร (แสดงส่วนลด) | `menu_ic_report_info_stk_profit_by_doc_and_discount` | `SMLERPICReport.ic_analysis._report_info_stk_profit_by_doc_and_discount` |  | สินค้า_รายงานกำไรขั้นต้นตามเอกสารแบบมีส่วนลด |
| 2.24.2 POS · 2.16.1 Lite/TYG · 2.19.1 TYGPro/Coffee | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า) | `menu_ic_report_info_stk_profit` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.3 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.4 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า) | `menu_ic_report_info_stk_profit_ic_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.5 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.6 POS · 2.16.2 Lite/TYG · 2.19.2 TYGPro/Coffee | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร) | `menu_ic_report_info_stk_profit_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.7 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.8 POS · 2.16.3 Lite/TYG · 2.19.3 TYGPro/Coffee | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า) | `menu_ic_report_info_stk_profit_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.9 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า) | `menu_ic_report_info_stk_profit_cust_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.10 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.11 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.24.12 POS | รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_cust_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |  |
| 2.25 POS · 2.17 Lite/TYG · 2.20 TYGPro/Coffee | คำนวณยอดสต๊อกใหม่ | `menu_ic_recalc` | `SMLERPIC._icRecalc` |  |  |
| 2.26 POS · 2.18 Lite/TYG · 2.21 TYGPro/Coffee | บันทึกรูปภาพเอกสาร | `menu_ic_document_picture` | `SMLERPIC._icDocPicture` | _documentPicture |  |
| 2.27 POS · 2.19 Lite/TYG · 2.22 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_ic` | tag:fastreportother |  |  |

## ซื้อ (48)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | ใบสั่งซื้อ | `menu_po_purchase_order` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 6 |
| 3.1 POS/TYGPro/Coffee | จ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1` | `SMLERPPO._po_advance_money` | _formSaleOrderPreview |  |
| 3.2 POS/TYGPro/Coffee | รับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1` | `SMLERPPO._po_advance_money_return` | _formSaleOrderPreview |  |
| 3.3.1 POS/TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกจ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 150 |
| 3.3.2 POS/TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 161 |
| 3.3.3 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานบันทึกการจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.3.4 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานบันทึกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return` | `SMLERPReportTool._reportTrans` |  | 20 |
| 3.3.5 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 150 |
| 3.3.6 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 161 |
| 3.3.7 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยอดคงเหลือจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.3.8 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการตัดจ่ายเงินล่วงหน้า | `menu_po_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 10 |
| 3.4 POS/TYGPro/Coffee | จ่ายเงินมัดจำ | `menu_po_deposit_payment_2` | `SMLERPPO._po_deposit_money` |  |  |
| 3.5 POS/TYGPro/Coffee | รับคืนเงินมัดจำ | `menu_po_deposit_return_2` | `SMLERPPO._po_deposit_money_return` |  |  |
| 3.6.1 POS/TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกจ่ายเงินมัดจำ | `menu_po_deposit_payment_2_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 151 |
| 3.6.2 POS/TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับคืนเงินมัดจำ | `menu_po_deposit_return_2_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 152 |
| 3.6.3 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานจ่ายเงินมัดจำ | `menu_po_report_advance_payment` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.6.4 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานรับคืนเงินมัดจำ | `menu_po_report_advance_payment_return` | `SMLERPReportTool._reportTrans` |  | 25 |
| 3.6.5 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินมัดจำ | `menu_po_report_advance_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 151 |
| 3.6.6 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_po_report_advance_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 152 |
| 3.6.7 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_po_report_deposit_payment_2_remain` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.6.8 POS/TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการตัดใบจ่ายเงินมัดจำ | `menu_po_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` |  | 11 |
| 3.7 POS/TYGPro/Coffee · 3.1 Lite/TYG | ซื้อสินค้า | `menu_po_purchase_billing` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 12 |
| 3.8 POS/TYGPro/Coffee | ส่งคืนสินค้า/ราคาผิด | `menu_po_credit_note` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 16 |
| 3.9 POS/TYGPro/Coffee | เพิ่มหนี้/ราคาผิด | `menu_po_addition_debt` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 14 |
| 3.10.1 POS/TYGPro/Coffee · 3.2.1 Lite/TYG | รายงาน/ยกเลิก › ยกเลิกซื้อสินค้า | `menu_po_purchase_billing_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 13 |
| 3.10.2 POS | รายงาน/ยกเลิก › ยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 17 |
| 3.10.3 POS | รายงาน/ยกเลิก › ยกเลิกซื้อเพิ่มสินค้า/เพิ่มหนี้ | `menu_po_addition_debt_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 15 |
| 3.10.4 POS · 3.2.2 TYG · 3.10.2 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับสินค้า/ตั้งหนี้ | `menu_po_report_purchase` | `SMLERPReportTool._reportTrans` |  | 12 |
| 3.2.2 Lite | รายงาน/ยกเลิก › รายงานการซื้อสินค้า | `menu_po_report_purchase_pos` | `SMLERPReportTool._reportTrans` |  | 12 |
| 3.10.5 POS | รายงาน/ยกเลิก › รายงานการส่งคืนสินค้า/ลดหนี้ | `menu_po_report_credit_note` | `SMLERPReportTool._reportTrans` |  | 16 |
| 3.10.6 POS | รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods` | `SMLERPReportTool._reportTrans` |  | 14 |
| 3.10.7 POS · 3.2.3 TYG · 3.10.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้า/ตั้งหนี้ | `menu_po_report_purchase_cancel` | `SMLERPReportTool._reportTrans` |  | 13 |
| 3.2.3 Lite | รายงาน/ยกเลิก › รายงานยกเลิกซื้อสินค้า | `menu_po_report_purchase_cancel_pos` | `SMLERPReportTool._reportTrans` |  | 13 |
| 3.10.8 POS | รายงาน/ยกเลิก › รายงานยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel_report` | `SMLERPReportTool._reportTrans` |  | 17 |
| 3.10.9 POS | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` |  | 15 |
| 3.11.1 POS/TYGPro/Coffee · 3.3.1 Lite/TYG | รายงานสรุป › รายงานซื้อสินค้าแยกตามสินค้า | `menu_po_recive_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` |  | ซื้อ_รายงานซื้อสินค้าแยกตามสินค้า |
| 3.11.2 POS/TYGPro/Coffee · 3.3.2 Lite/TYG | รายงานสรุป › รายงานการซื้อสินค้าแบบสรุป-ตามวันที่ | `menu_fast_report_purchase_summary_by_date` | `SMLFastReport._designer` |  |  |
| 3.11.3 POS/TYGPro/Coffee · 3.3.3 Lite/TYG | รายงานสรุป › รายงานการซื้อสินค้าสรุปตามประเภทภาษี | `menu_report_sum_purchase_by_vat` | `SMLFastReport._designer` |  |  |
| 3.11.4 POS | รายงานสรุป › รายงานใบตั้งหนี้จากการซื้อแบบสรุป-ตามวันที่ | `menu_po_report_debt_from_purchase` | `SMLERPPOReport._report_summary._report_debt_from_purchase` |  |  |
| 3.11.5 POS | รายงานสรุป › รายงานการสั่งซื้อสินค้าแบบสรุป-ตามวันที่ | `menu_po_report_purchase_order_sum` | `SMLERPPOReport._report_summary._report_purchase_order_sum` |  |  |
| 3.11.6 POS | รายงานสรุป › รายงานใบเพิ่มสินค้า(เจ้าหนี้)แบบสรุป-ตามสินค้า | `menu_fast_report_additional_product_purchase_summary_by_item` | `SMLFastReport._designer` |  |  |
| 3.11.7 POS | รายงานสรุป › รายงานการส่งคืนสินค้า/ลดหนี้แบบสรุป-ตามสินค้า | `menu_fast_report_summary_credit_note_by_item` | `SMLFastReport._designer` |  |  |
| 3.11.8 POS | รายงานสรุป › รายงานใบซื้อสินค้าที่ถึงกำหนดจ่ายเงิน | `menu_fast_report_purchase_due_date` | `SMLFastReport._designer` |  |  |
| 3.12.1 POS/TYGPro/Coffee · 3.4.1 Lite/TYG | รายงานวิเคราะห์ › รายงานการจัดอันดับยอดซื้อ(ตามสินค้า-กลุ่มสินค้า) | `menu_po_report_rank_purchase_total` | `SMLERPPOReport._report_analyze._report_rank_purchase_total` |  |  |
| 3.12.2 POS/TYGPro/Coffee · 3.4.2 Lite/TYG | รายงานวิเคราะห์ › รายงานวิเคราะห์การซื้อสุทธิ-ตามสินค้า | `menu_po_report_purchase_analyze` | `SMLERPPOReport._report_analyze._report_purchase_analyze` |  |  |
| 3.12.3 POS/TYGPro/Coffee · 3.4.3 Lite/TYG | รายงานวิเคราะห์ › รายงานสรุปยอดซื้อ 12 เดือน ตามเจ้าหนี้ | `menu_fast_report_compare_purchase_monthly` | `SMLFastReport._designer` |  |  |
| 3.13 POS/TYGPro/Coffee · 3.5 Lite/TYG | บันทึกรูปภาพเอกสาร | `menu_po_doc_picture` | `SMLERPPO._po_docPicture` | _documentPicture |  |
| 3.14 POS/TYGPro/Coffee · 3.6 Lite/TYG | รายงานอื่น ๆ | `menu_fastreport_other_purchase` | tag:fastreportother |  |  |

## ขาย (58)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 4.1 POS | ใบเสนอราคา | `menu_so_quotation_order` | `SMLERPSO._soQuotation` | _icTransControl | 30 |
| 4.2 POS | อนุมัติใบเสนอราคา | `menu_so_quotation_approve` | `SMLERPSO._soQuotationApproval` | _icTransControl | 32 |
| 4.3.1 POS | รายงาน/ยกเลิก › ยกเลิกใบเสนอราคา | `menu_so_quotation_cancel` | `SMLERPSO._soQuotationCancel` | _icTransControl | 31 |
| 4.3.2 POS | รายงาน/ยกเลิก › รายงานบันทึกใบเสนอราคา | `menu_so_report_quotation` | `SMLERPReportTool._reportTrans` |  | 30 |
| 4.3.3 POS | รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอราคา | `menu_so_report_quotation_approve` | `SMLERPReportTool._reportTrans` |  | 32 |
| 4.3.4 POS | รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอราคา | `menu_so_report_quotation_cancel` | `SMLERPReportTool._reportTrans` |  | 31 |
| 4.3.5 POS | รายงาน/ยกเลิก › รายงานสถานะใบเสนอราคา | `menu_so_report_quotation_stat` | `SMLERPReportTool._reportTrans` |  | 30 |
| — | ขายสินค้า/บริการ | `menu_pos_screen` | `StreamReader` |  |  |
| — | ใบเสนอราคา | `menu_so_quotation_order` | `SMLERPSO._soQuotation` | _icTransControl | 30 |
| 4.4 POS · 4.1 TYGPro/Coffee | รับเงินล่วงหน้า | `menu_so_deposit_receive_1` | `SMLERPSO._so_advance_money` | _formSaleOrderPreview |  |
| 4.5 POS · 4.2 TYGPro/Coffee | คืนเงินรับล่วงหน้า | `menu_so_deposit_return_1` | `SMLERPSO._so_advance_money_return` | _formSaleOrderPreview |  |
| 4.6.1 POS · 4.3.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับเงินล่วงหน้า | `menu_so_deposit_receive_1_cancel` | `SMLERPSO._so_advance_money_cancel` | _icTransControl | 41 |
| 4.6.2 POS · 4.3.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกคืนเงินรับล่วงหน้า | `menu_so_deposit_return_1_cancel` | `SMLERPSO._so_advance_money_return_cancel` | _icTransControl | 43 |
| 4.6.3 POS · 4.3.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานรับเงินล่วงหน้า | `menu_so_report_deposit_receive` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.6.4 POS · 4.3.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานคืนเงินรับล่วงหน้า | `menu_so_report_deposit_return` | `SMLERPReportTool._reportTrans` |  | 42 |
| 4.6.5 POS · 4.3.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับเงินล่วงหน้า | `menu_so_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` |  | 41 |
| 4.6.6 POS · 4.3.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินรับล่วงหน้า | `menu_so_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` |  | 43 |
| 4.6.7 POS · 4.3.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินรับล่วงหน้า | `menu_so_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.6.8 POS · 4.3.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการตัดเงินรับล่วงหน้า | `menu_so_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` |  | 40 |
| 4.7 POS · 4.4 TYGPro/Coffee | รับเงินมัดจำ | `menu_so_deposit_receive_2` | `SMLERPSO._so_deposit_money` |  |  |
| 4.8 POS · 4.5 TYGPro/Coffee | คืนเงินมัดจำ | `menu_so_deposit_return_2` | `SMLERPSO._so_deposit_money_return` |  |  |
| 4.9.1 POS · 4.6.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับเงินมัดจำ | `menu_so_deposit_receive_2_cancel` | `SMLERPSO._so_deposit_money_cancel` | _icTransControl | 111 |
| 4.9.2 POS · 4.6.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกคืนเงินมัดจำ | `menu_so_deposit_return_2_cancel` | `SMLERPSO._so_deposit_money_return_cancel` | _icTransControl | 113 |
| 4.9.3 POS · 4.6.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานรับเงินมัดจำ | `menu_so_report_deposit_receive_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.9.4 POS · 4.6.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานคืนเงินมัดจำ | `menu_so_report_deposit_return_2` | `SMLERPReportTool._reportTrans` |  | 112 |
| 4.9.5 POS · 4.6.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับเงินมัดจำ | `menu_so_report_deposit_payment_cancel_2` | `SMLERPReportTool._reportTrans` |  | 111 |
| 4.9.6 POS · 4.6.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_so_report_deposit_payment_return_cancel_2` | `SMLERPReportTool._reportTrans` |  | 113 |
| 4.9.7 POS · 4.6.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_so_report_deposit_payment_remain_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.9.8 POS · 4.6.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการตัดเงินมัดจำ | `menu_so_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.10 POS · 4.7 TYGPro/Coffee | ขายสินค้า/บริการ | `menu_so_invoice` | `SMLERPSO._soInvoice` | _icTransControl | 44 |
| 4.11 POS · 4.8 TYGPro/Coffee | รับคืนสินค้า/ลดหนี้ | `menu_so_credit_note` | `SMLERPSO._creditNote` | _icTransControl | 48 |
| 4.12 POS · 4.9 TYGPro/Coffee | เพิ่มหนี้ | `menu_so_invoice_add` | `SMLERPSO._soInvoiceAdd` | _icTransControl | 46 |
| 4.13 POS · 4.10 TYGPro/Coffee | ส่งข้อมูล e-Tax | `menu_so_send_etax` | `SMLETaxInvoice._sendETaxControl` |  |  |
| 4.14.1 POS · 4.11.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกขายสินค้า/บริการ | `menu_so_invoice_cancel` | `SMLERPSO._soInvoiceCancel` | _icTransControl | 45 |
| 4.14.2 POS · 4.11.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_credit_note_cancel` | `SMLERPSO._creditNoteCancel` | _icTransControl | 49 |
| 4.14.3 POS · 4.11.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกขายเพิ่มสินค้า/เพิ่มหนี้ | `menu_so_invoice_add_cancel` | `SMLERPSO._soInvoiceAddCancel` | _icTransControl | 47 |
| 4.14.4 POS · 4.11.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ | `menu_so_report_invoice` | `SMLERPReportTool._reportTrans` |  | 44 |
| 4.14.5 POS · 4.11.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการขายและบริการเรียงตามสินค้า | `menu_so_sale_service_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` |  | ขาย_รายงานขายสินค้าแยกตามสินค้า |
| 4.14.6 POS · 4.11.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note` | `SMLERPReportTool._reportTrans` |  | 48 |
| 4.14.7 POS · 4.11.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods` | `SMLERPReportTool._reportTrans` |  | 46 |
| 4.14.8 POS · 4.11.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ/เพิ่มหนี้/ลดหนี้ | `menu_so_report_invoice_credit_note_add_goods` | `SMLERPReportTool._reportTrans` |  | 44 |
| 4.14.9 POS · 4.11.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกขายสินค้าและบริการ | `menu_so_report_invoice_cancel` | `SMLERPReportTool._reportTrans` |  | 45 |
| 4.14.10 POS · 4.11.10 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note_cancel` | `SMLERPReportTool._reportTrans` |  | 49 |
| 4.14.11 POS · 4.11.11 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` |  | 47 |
| 4.15.1 POS · 4.12.1 TYGPro/Coffee | รายงานสรุป › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_sell_by_sale` | `SMLERPSOReport._report_summary._report_sell_by_sale` |  | สินค้า_sell_by_sale |
| 4.15.2 POS · 4.12.2 TYGPro/Coffee | รายงานสรุป › รายงานสรุปยอดขายสินค้า-สรุปตามวันที่ | `menu_shipments_by_date` | `SMLFastReport._designer` |  |  |
| 4.15.3 POS · 4.12.3 TYGPro/Coffee | รายงานสรุป › รายงานประวัติการขายสินค้า | `menu_fast_report_sale_history_product` | `SMLFastReport._designer` |  |  |
| 4.15.4 POS | รายงานสรุป › รายงานยอดขาย-ตามพนักงานขาย | `menu_fast_report_sale_by_employee` | `SMLFastReport._designer` |  |  |
| 4.16.1 POS · 4.13.1 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบแจกแจง-ตามสินค้า | `menu_fast_report_analysis_sell_ex_by_product` | `SMLFastReport._designer` |  |  |
| 4.16.2 POS · 4.13.2 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบสรุป-ตามเอกสาร | `menu_fast_report_analysis_sell_sum_by_docno` | `SMLFastReport._designer` |  |  |
| 4.16.3 POS · 4.13.3 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานกำไรขั้นต้นแสดงหักรับคืน | `menu_fast_report_margin_reacceptance` | `SMLFastReport._designer` |  |  |
| 4.16.4 POS · 4.13.4 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานจัดอันดับยอด-สินค้า | `menu_fast_report_product_rank` | `SMLFastReport._designer` |  |  |
| 4.16.5 POS · 4.13.5 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานเปรียบเที่ยบยอดสินค้า12เดือน | `menu_fast_report_shipments_compare_month` | `SMLFastReport._designer` |  |  |
| 4.16.6 POS · 4.13.6 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานการเทียบการขายกับราคาขาย | `menu_compare_sale_with_price` | `SMLFastReport._designer` |  |  |
| 4.16.7 POS · 4.13.7 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสินค้าขายต่ำกว่าทุน | `menu_product_sale_loss` | `SMLFastReport._designer` |  |  |
| 4.16.8 POS | รายงานวิเคราะห์ › รายงานจัดอันดับยอดขาย-ตามพนักงาน | `menu_fast_report_product_rank_by_sale` | `SMLFastReport._designer` |  |  |
| 4.17 POS · 4.14 TYGPro/Coffee | บันทึกรูปภาพเอกสาร | `menu_so_doc_picture` | `SMLERPSO._so_docPicture` | _documentPicture |  |
| 4.18 POS · 4.15 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_sale` | tag:fastreportother |  |  |

## ร้านกาแฟ (1)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 5.1 Coffee | กำหนดจุดพิมพ์ | `menu_print_station_coffee` | `SMLPOSControl._food._kitchenManage` | _myManageData |  |

## เงินมัดจำ (10)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 4.1 Lite | รับเงินมัดจำ | `menu_so_deposit_receive_2` | `SMLERPSO._so_deposit_money` |  |  |
| 4.2 Lite | คืนเงินมัดจำ | `menu_so_deposit_return_2` | `SMLERPSO._so_deposit_money_return` |  |  |
| 4.3.1 Lite | รายงาน/ยกเลิก › ยกเลิกรับเงินมัดจำ | `menu_so_deposit_receive_2_cancel` | `SMLERPSO._so_deposit_money_cancel` | _icTransControl | 111 |
| 4.3.2 Lite | รายงาน/ยกเลิก › ยกเลิกคืนเงินมัดจำ | `menu_so_deposit_return_2_cancel` | `SMLERPSO._so_deposit_money_return_cancel` | _icTransControl | 113 |
| 4.3.3 Lite | รายงาน/ยกเลิก › รายงานรับเงินมัดจำ | `menu_so_report_deposit_receive_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.3.4 Lite | รายงาน/ยกเลิก › รายงานคืนเงินมัดจำ | `menu_so_report_deposit_return_2` | `SMLERPReportTool._reportTrans` |  | 112 |
| 4.3.5 Lite | รายงาน/ยกเลิก › รายงานยกเลิกรับเงินมัดจำ | `menu_so_report_deposit_payment_cancel_2` | `SMLERPReportTool._reportTrans` |  | 111 |
| 4.3.6 Lite | รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_so_report_deposit_payment_return_cancel_2` | `SMLERPReportTool._reportTrans` |  | 113 |
| 4.3.7 Lite | รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_so_report_deposit_payment_remain_2` | `SMLERPReportTool._reportTrans` |  | 110 |
| 4.3.8 Lite | รายงาน/ยกเลิก › รายงานการตัดเงินมัดจำ | `menu_so_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` |  | 110 |

## ร้านอาหาร (13)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 4.1.1 TYG · 5.1.1 TYGPro | ค่าเริ่มต้น › กำหนดโต๊ะ | `menu_food_master_table` | `SMLPOSControl._table` | _myManageData |  |
| 4.1.2 TYG · 5.1.2 TYGPro | ค่าเริ่มต้น › กำหนดรหัสเครื่องสั่งอาหาร | `menu_order_device_id` | `SMLPOSControl._orderDevice` | _myManageData, _orderDeviceScreenTop |  |
| 4.1.3 TYG · 5.1.3 TYGPro | ค่าเริ่มต้น › กำหนดุณสมบัติเครื่องสั่งอาหาร | `menu_food_config_order_device` | `SMLPOSControl._orderdeviceConfig` | _searchDataFull, _orderDeviceConfigScreen, _orderFontSlipScreen |  |
| 4.1.4 TYG · 5.1.4 TYGPro | ค่าเริ่มต้น › กำหนดห้องครัว/บาร์น้ำ | `menu_food_kitchen` | `SMLPOSControl._food._kitchenManage` | _myManageData |  |
| 4.1.5 TYG · 5.1.5 TYGPro | ค่าเริ่มต้น › ตรวจสอบการพิมพ์ครัว/บาร์น้ำ | `menu_food_kitchen_fast` | `SMLPOSControl._food._kitchenFast` |  |  |
| 5.1.6 TYGPro | ค่าเริ่มต้น › กำหนดเครื่อง Checker | `menu_food_config_checker_device` | `SMLPOSControl._checkerDeviceConfig` |  |  |
| 5.1.7 TYGPro | ค่าเริ่มต้น › กำหนดผู้ปรุงอาหาร | `menu_chefmaster_list` | `SMLPOSControl._food._chefListControl` | _myManageData |  |
| 4.1.6 TYG · 5.1.8 TYGPro | ค่าเริ่มต้น › หมายเหตุสินค้าทั้งหมด | `menu_food_master_remark` | `SMLPOSControl._masterRemark` |  |  |
| 5.1.9 TYGPro | ค่าเริ่มต้น › กำหนดการพิมพ์ใบสรุปการสั่งอาหาร | `menu_printer_order_check` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| 4.2 TYG · 5.2 TYGPro | สั่งอาหาร | `menu_food_order` | `MyLib._erpUserLoginForm` |  |  |
| 4.3 TYG · 5.3 TYGPro | สั่งอาหาร (ด้วยรหัส) | `menu_food_order_fast` | `SMLPOSControl._food._orderControl` |  |  |
| 4.4 TYG · 5.4 TYGPro | สั่งจัดอาหาร | `menu_fast_order` | `SMLPOSControl._food._orderControl` |  |  |
| 5.5 TYGPro | หน้าจอ Checker | `menu_food_checker` | `SMLPOSControl._checkerKitchen` |  |  |

## ขาย POS (40)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 5.1 POS/Lite/TYG · 6.1 TYGPro/Coffee | หน้าจอขาย POS | `menu_pos_screen` | `StreamReader` |  |  |
| 5.2 Lite | รับคืนสินค้า | `menu_so_credit_note_pos` | `SMLERPSO._creditNote` | _icTransControl | 48 |
| 5.2 POS/TYG · 5.3 Lite · 6.2 TYGPro/Coffee | รายละเอียดคูปอง | `menu_coupon_list` | `SMLERPControl._coupon._couponList` |  |  |
| 5.3 POS | สร้างคูปองแบบเร็ว | `menu_coupon_generate` | `SMLERPControl._coupon._couponGenerate` | _myManageData |  |
| 5.4 POS/Lite · 5.3 TYG · 6.3 TYGPro/Coffee | บันทึกรับเงิน (เงินทอน) | `menu_save_pos_receive_money` | `SMLPosClient._posSaveMoneyReceive` | _myManageData |  |
| 5.5 POS/Lite · 5.4 TYG · 6.4 TYGPro/Coffee | บันทึกส่งเงิน POS | `menu_save_send_money_pos` | `SMLPosClient._posSaveSendMoney` | _myManageData |  |
| 5.6 POS/Lite · 5.5 TYG · 6.5 TYGPro/Coffee | รายการใบกำกับภาษีอย่างย่อ | `pos_invoice_list_pos` | `SMLERPSO._soInvoice` | _icTransControl | 44 |
| 5.7 POS/Lite · 5.6 TYG · 6.6 TYGPro/Coffee | รายการใบกำกับภาษีอย่างเต็มออกแทน | `pos_full_invoide_list_pos` | `SMLERPSO._soFullInvoice` | _icTransControl | 144 |
| 5.8 POS/Lite · 5.7 TYG · 6.7 TYGPro/Coffee | รายการใบกำกับภาษีอย่างย่อยกเลิก | `pos_invoice_cancel_pos` | `SMLERPSO._soInvoiceCancel` | _icTransControl | 45 |
| 5.9.1 Lite | รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า | `menu_so_credit_note_cancel_pos` | `SMLERPSO._creditNoteCancel` | _icTransControl | 49 |
| 5.9.2 Lite | รายงาน/ยกเลิก › รายงานการรับคืนสินค้า | `menu_so_report_credit_note_pos` | `SMLERPReportTool._reportTrans` |  | 48 |
| 5.9.3 Lite | รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า | `menu_so_report_credit_note_cancel_pos` | `SMLERPReportTool._reportTrans` |  | 49 |
| 5.9.1 POS · 5.9.4 Lite · 5.8.1 TYG · 6.8.1 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับเงิน | `menu_fastreport_received_money` | `SMLFastReport._designer` |  |  |
| 5.9.2 POS · 5.9.5 Lite · 5.8.2 TYG · 6.8.2 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ | `menu_so_report_invoice` | `SMLERPReportTool._reportTrans` |  | 44 |
| 5.9.3 POS · 5.9.6 Lite · 5.8.3 TYG · 6.8.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการนำส่งเงินประจำวัน | `report_send_money_pos` | `SMLFastReport._designer` |  |  |
| 5.9.4 POS · 5.9.7 Lite · 5.8.4 TYG · 6.8.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างเต็มออกแทน | `menu_so_report_pos_full_invoice` | `SMLERPReportTool._reportTrans` |  | 144 |
| 5.9.5 POS · 5.9.8 Lite · 5.8.5 TYG · 6.8.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างย่อ | `menu_pos_sum_short_vat` | `SMLFastReport._designer` |  |  |
| 5.9.6 POS · 5.9.9 Lite · 5.8.6 TYG · 6.8.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างย่อยกเลิก | `menu_fastreport_invoice_cancel` | `SMLFastReport._designer` |  |  |
| 5.9.7 POS · 5.9.10 Lite · 5.8.7 TYG · 6.8.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานสรุปการขายหน้าร้าน | `menu_pos_sum_front` | `SMLFastReport._designer` |  |  |
| 5.9.8 POS · 5.9.11 Lite · 5.8.8 TYG · 6.8.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างเต็ม | `menu_pos_sum_full_vat` | `SMLFastReport._designer` |  |  |
| 5.9.9.1 POS · 5.9.12.1 Lite · 5.8.9.1 TYG · 6.8.9.1 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามวันที่ | `menu_pos_sale_detail_001` | `SMLFastReport._designer` |  |  |
| 5.9.9.2 POS · 5.9.12.2 Lite · 5.8.9.2 TYG · 6.8.9.2 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามลูกค้า | `menu_pos_sale_detail_002` | `SMLFastReport._designer` |  |  |
| 5.9.9.3 POS · 5.9.12.3 Lite · 5.8.9.3 TYG · 6.8.9.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแคชเชียร์ | `menu_pos_sale_detail_008` | `SMLFastReport._designer` |  |  |
| 5.9.9.4 POS · 5.9.12.4 Lite · 5.8.9.4 TYG · 6.8.9.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามยี่ห้อสินค้า | `menu_pos_sale_detail_004` | `SMLFastReport._designer` |  |  |
| 5.9.9.5 POS · 5.9.12.5 Lite · 5.8.9.5 TYG · 6.8.9.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามพนักงาน | `menu_pos_sale_detail_005` | `SMLFastReport._designer` |  |  |
| 5.9.9.6 POS · 5.9.12.6 Lite · 5.8.9.6 TYG · 6.8.9.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแผนก | `menu_pos_sale_detail_006` | `SMLFastReport._designer` |  |  |
| 5.9.9.7 POS · 5.9.12.7 Lite · 5.8.9.7 TYG · 6.8.9.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มสินค้า | `menu_pos_sale_detail_009` | `SMLFastReport._designer` |  |  |
| 5.9.9.8 POS · 5.9.12.8 Lite · 5.8.9.8 TYG · 6.8.9.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามประเภทลูกค้า | `menu_pos_sale_detail_007` | `SMLFastReport._designer` |  |  |
| 5.9.9.9 POS · 5.9.12.9 Lite · 5.8.9.9 TYG · 6.8.9.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มลูกค้า | `menu_pos_sale_detail_010` | `SMLFastReport._designer` |  |  |
| 5.9.9.10 POS · 5.9.12.10 Lite · 5.8.9.10 TYG · 6.8.9.10 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามรหัส | `menu_pos_sale_detail_003` | `SMLFastReport._designer` |  |  |
| 5.9.9.11 POS · 5.8.9.11 TYG · 6.8.9.11 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรีบงตามรหัส (แสดง Serial) | `menu_report_pos_sale_sugest_by_item_and_serial` | `SMLERPReportTool._reportPosAnalyze` |  | 44 |
| 5.9.10.1 POS · 5.9.13.1 Lite · 5.8.10.1 TYG · 6.8.10.1 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามยี่ห้อสินค้า | `menu_pos_sumary_004` | `SMLFastReport._designer` |  |  |
| 5.9.10.2 POS · 5.9.13.2 Lite · 5.8.10.2 TYG · 6.8.10.2 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มลูกค้า | `menu_pos_sumary_009` | `SMLFastReport._designer` |  |  |
| 5.9.10.3 POS · 5.9.13.3 Lite · 5.8.10.3 TYG · 6.8.10.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามวันที่ | `menu_pos_sumary_002` | `SMLFastReport._designer` |  |  |
| 5.9.10.4 POS · 5.9.13.4 Lite · 5.8.10.4 TYG · 6.8.10.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มสินค้า | `menu_pos_sumary_008` | `SMLFastReport._designer` |  |  |
| 5.9.10.5 POS · 5.9.13.5 Lite · 5.8.10.5 TYG · 6.8.10.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-เรียงตามแคชเชียร์ | `menu_pos_sumary_001` | `SMLFastReport._designer` |  |  |
| 5.9.10.6 POS · 5.9.13.6 Lite · 5.8.10.6 TYG · 6.8.10.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย | `menu_pos_sumary_005` | `SMLFastReport._designer` |  |  |
| 5.9.10.7 POS · 5.9.13.7 Lite · 5.8.10.7 TYG · 6.8.10.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า | `menu_pos_sumary_003` | `SMLFastReport._designer` |  |  |
| 5.9.10.8 POS · 5.9.13.8 Lite · 5.8.10.8 TYG · 6.8.10.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามประเภทลูกค้า | `menu_pos_sumary_007` | `SMLFastReport._designer` |  |  |
| 5.10 POS/Lite · 5.9 TYG · 6.9 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_sale_pos` | tag:fastreportother |  |  |

## เจ้าหนี้ (59)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 6.1 Lite/TYG | กำหนดเจ้าหนี้ | `menu_ap_detail` | `SMLERPAP._ap` |  |  |
| 6.2 Lite/TYG | รายละเอียดเจ้าหนี้ | `menu_ap_detail_2` | `SMLERPAP._ap_detail` |  |  |
| 6.3 Lite/TYG | ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 6.4 Lite/TYG | พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 6.5 Lite/TYG | นำเข้าที่อยู่จัดส่งเจ้าหนี้ | `menu_import_ap_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 6.6 Lite/TYG | รายงานรายละเอียดเจ้าหนี้ | `menu_ap_report_detail_ap` | `SMLERPReportTool._reportCustMaster` |  | เจ้าหนี้_รายละเอียด |
| 6.1.1 POS · 7.1.1 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › กำหนดเจ้าหนี้ | `menu_ap_detail` | `SMLERPAP._ap` |  |  |
| 6.1.2 POS · 7.1.2 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › รายละเอียดเจ้าหนี้ | `menu_ap_detail_2` | `SMLERPAP._ap_detail` |  |  |
| 6.1.3 POS · 7.1.3 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › กำหนดรูปภาพ | `menu_ap_picture` | tag:ap (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 6.1.4 POS · 7.1.4 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 6.1.5 POS · 7.1.5 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 6.1.6 POS · 7.1.6 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › นำเข้าที่อยู่จัดส่งเจ้าหนี้ | `menu_import_ap_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 6.1.7 POS · 7.1.7 TYGPro/Coffee | ข้อมูลเจ้าหนี้ › รายงานรายละเอียดเจ้าหนี้ | `menu_ap_report_detail_ap` | `SMLERPReportTool._reportCustMaster` |  | เจ้าหนี้_รายละเอียด |
| 6.2 POS · 7.2 TYGPro/Coffee | ตั้งหนี้ยกมา (เจ้าหนี้) | `menu_ap_debt_balance` | `SMLERPAP._ap_debt_balance` | _ar_ap_trans | 81 |
| 6.3 POS · 7.3 TYGPro/Coffee | ลดหนี้ยกมา (เจ้าหนี้) | `menu_ap_cn_balance` | `SMLERPAP._ap_cn_balance` | _ar_ap_trans | 85 |
| 6.4 POS · 7.4 TYGPro/Coffee | เพิ่มหนี้ยกมา (เจ้าหนี้) | `menu_ap_increase_debt` | `SMLERPAP._ap_increase_debt` | _ar_ap_trans | 83 |
| 6.5.1 POS · 7.5.1 TYGPro/Coffee | รายงาน › รายงานตั้งหนี้ยกมา | `menu_ap_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` |  | 81 |
| 6.5.2 POS · 7.5.2 TYGPro/Coffee | รายงาน › รายงานลดหนี้ยกมา | `menu_ap_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` |  | 85 |
| 6.5.3 POS · 7.5.3 TYGPro/Coffee | รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ap_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` |  | 83 |
| 6.6 POS · 7.6 TYGPro/Coffee | ตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 87 |
| 6.7 POS · 7.7 TYGPro/Coffee | ลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 91 |
| 6.8 POS · 7.8 TYGPro/Coffee | เพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 89 |
| 6.9.1 POS · 7.9.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_debt_balance_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 88 |
| 6.9.2 POS · 7.9.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 92 |
| 6.9.3 POS · 7.9.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 90 |
| 6.9.4 POS · 7.9.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 87 |
| 6.9.5 POS · 7.9.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 89 |
| 6.9.6 POS · 7.9.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 91 |
| 6.9.7 POS · 7.9.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_cancel_documents_early_year_other` | `SMLERPReportTool._reportTrans` |  | 88 |
| 6.9.8 POS · 7.9.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_cancel_increase_debt_other` | `SMLERPReportTool._reportTrans` |  | 90 |
| 6.9.9 POS · 7.9.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_cancel_reduction_dept_other` | `SMLERPReportTool._reportTrans` |  | 92 |
| 6.10 POS · 7.10 TYGPro/Coffee | ใบรับวางบิล (เจ้าหนี้) | `menu_ap_pay_bill` | `SMLERPAP._ap_pay_bill` | _ar_ap_trans, _formSaleOrderPreview | 213 |
| 6.11 POS · 7.11 TYGPro/Coffee | จ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_debt_billing` | `SMLERPAP._ap_debt_billing` | _ar_ap_trans, _formSaleOrderPreview | 19 |
| 6.12.1 POS · 7.12.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกใบรับวางบิล (เจ้าหนี้) | `menu_ap_cancel_pay_bill` | `SMLERPAP._ap_cancel_pay_bill` | _ar_ap_trans | 214 |
| 6.12.2 POS · 7.12.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_cancel_debt_billing` | `SMLERPAP._ap_cancel_debt_billing` | _ar_ap_trans | 23 |
| 6.12.3 POS · 7.12.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) | `menu_ap_report_cancel_pay_bill` | `SMLERPReportTool._reportArApTrans` |  | 214 |
| 6.12.4 POS · 7.12.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) | `menu_ap_report_cancel_debt_billing` | `SMLERPReportTool._reportArApTrans` |  | 23 |
| 6.12.5 POS · 7.12.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบรับวางบิล (เจ้าหนี้) | `menu_ap_report_billing` | `SMLERPReportTool._reportArApTrans` |  | 213 |
| 6.12.6 POS · 7.12.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้า-ตามใบส่งของ | `menu_billing_value_by_invoice` | `SMLERPReport.ap.Billing_Value_by_Invoice` |  |  |
| 6.12.7 POS · 7.12.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้าที่คงค้าง | `menu_billing_outstanding` | `SMLERPReport.ap.Billing_Outstanding` |  |  |
| 6.12.8 POS · 7.12.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_report_payment` | `SMLERPReportTool._reportArApTrans` |  | 19 |
| 6.12.9 POS · 7.12.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานจ่ายชำระค่าสินค้าพร้อมรายการย่อย | `menu_payment_detail` | `SMLERPReport.ap.Payment_Detail` |  |  |
| 6.12.10 POS · 7.12.10 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.3) | `menu_gl_wht_report_in_3` | `SMLERPGL._report._tax._wht` |  |  |
| 6.12.11 POS · 7.12.11 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.53) | `menu_gl_wht_report_in_53` | `SMLERPGL._report._tax._wht` |  |  |
| 6.13.1 POS · 7.13.1 TYGPro/Coffee | รายงานสรุป › รายงานใบส่งของค้างจ่ายชำระ-ตามวันที่ | `menu_invoice_arrears_by_date` | `SMLFastReport._designer` |  |  |
| 6.13.2 POS · 7.13.2 TYGPro/Coffee | รายงานสรุป › รายงานใบส่งของถึงกำหนดชำระ-ตามวันที่ | `menu_invoice_due_by_date` | `SMLFastReport._designer` |  |  |
| 6.13.3 POS · 7.13.3 TYGPro/Coffee | รายงานสรุป › รายงานใบส่งของค้างชำระแสดงวันที่ถึงกำหนด | `menu_invoice_arrears_due` | `SMLFastReport._designer` |  |  |
| 6.13.4 POS · 7.13.4 TYGPro/Coffee | รายงานสรุป › รายงานใบส่งของเกินกำหนดชำระ-ตามวันที่ | `menu_invoice_overdue_by_date` | `SMLFastReport._designer` |  |  |
| 6.13.5 POS · 7.13.5 TYGPro/Coffee | รายงานสรุป › รายงานจ่ายชำระค่าสินค้า-ตามใบส่งของ | `menu_payment_by_invoice` | `SMLFastReport._designer` |  |  |
| 6.13.6 POS · 7.13.6 TYGPro/Coffee | รายงานสรุป › รายงานการจ่ายชำระประจำวัน-ตามวันที่ | `menu_payment_by_date` | `SMLFastReport._designer` |  |  |
| 6.13.7 POS · 7.13.7 TYGPro/Coffee | รายงานสรุป › รายงานการจ่ายเงินประจำวัน-ตามแผนก | `menu_payment_by_department` | `SMLFastReport._designer` |  |  |
| 6.14.1 POS · 7.14.1 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานเคลื่อนไหวเจ้าหนี้ | `menu_ap_report_payable_movement` | `SMLERPARAPReport.report._movement` |  |  |
| 6.14.2 POS · 7.14.2 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้ | `menu_ap_report_payable_aging` | `SMLERPARAPReport.report._ageing` |  |  |
| 6.14.3 POS · 7.14.3 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้-ตามเอกสาร | `menu_ap_report_payable_aging_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |  |
| 6.14.4 POS · 7.14.4 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสถานะเจ้าหนี้ | `menu_ap_report_payable_status` | `SMLERPARAPReport.report._absolute_status` |  |  |
| 6.14.5 POS · 7.14.5 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานเจ้าหนี้ที่ไม่มีการเคลื่อนไหว | `menu_ap_report_payable_not_movement` | tag:apreport (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 6.14.6 POS · 7.14.6 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานใบตั้งหนี้จากการซื้อแบบแจกแจงตามเจ้าหนี้ | `menu_ap_detail_debt_by_ap` | `SMLFastReport._designer` |  |  |
| 6.15 POS · 7.15 TYGPro/Coffee | บันทึกรูปภาพเอกสาร | `menu_ap_doc_picture` | `SMLERPAP._ap_doc_picture` | _documentPicture |  |
| 6.16 POS · 6.7 Lite/TYG · 7.16 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_supplier` | tag:fastreportother |  |  |

## ลูกหนี้ (63)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 7.1 Lite/TYG | กำหนดลูกหนี้ | `menu_ar_detail` | `SMLERPAR._ar` |  |  |
| 7.2 Lite/TYG | รายละเอียดลูกหนี้ | `menu_ar_detail_2` | `SMLERPAR._ar_detail` |  |  |
| 7.3 Lite/TYG | รายละเอียดสมาชิก | `menu_ar_detail_healthy` | `SMLERPAR.ar_dealerHealthy` |  |  |
| 7.4 Lite/TYG | กำหนดแต้มคงเหลือยกมา | `menu_ar_point_balance` | `SMLERPAR._ar_point_balance` | _ar_point_balance |  |
| 7.5 Lite/TYG | บันทึกตัดแต้ม | `menu_ar_cut_point` | `SMLERPAR._ar_cut_point` | _ar_cut_point |  |
| 7.6 Lite/TYG | กำหนดรูปภาพ | `menu_ar_picture` | tag:ar (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.7 Lite/TYG | แต้มสะสม | `menu_ar_point` | `SMLERPAR.ar_point` |  |  |
| 7.8 Lite/TYG | คำณวนแต้มสะสม | `menu_ar_point_recal` | `SMLERPAR.ar_point_recal` |  |  |
| 7.9 Lite/TYG | ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 7.10 Lite/TYG | พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 7.11 Lite/TYG | นำเข้าที่อยู่จัดส่งลูกหนี้ | `menu_import_ar_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 7.12.1 Lite/TYG | รายงาน › รายงานแต้มคงเหลือลูกหนี้ | `menu_report_point_balance` | `SMLERPARReport.report._ar_report` |  | ลูกหนี้_แต้มคงเหลือ |
| 7.1.1 POS · 8.1.1 TYGPro/Coffee | ข้อมูลลูกหนี้ › กำหนดลูกหนี้ | `menu_ar_detail` | `SMLERPAR._ar` |  |  |
| 7.1.2 POS · 8.1.2 TYGPro/Coffee | ข้อมูลลูกหนี้ › รายละเอียดลูกหนี้ | `menu_ar_detail_2` | `SMLERPAR._ar_detail` |  |  |
| 7.1.3 POS · 8.1.3 TYGPro/Coffee | ข้อมูลลูกหนี้ › รายละเอียดสมาชิก | `menu_ar_detail_healthy` | `SMLERPAR.ar_dealerHealthy` |  |  |
| 7.1.4 POS · 8.1.4 TYGPro/Coffee | ข้อมูลลูกหนี้ › กำหนดแต้มคงเหลือยกมา | `menu_ar_point_balance` | `SMLERPAR._ar_point_balance` | _ar_point_balance |  |
| 7.1.5 POS · 8.1.5 TYGPro/Coffee | ข้อมูลลูกหนี้ › บันทึกตัดแต้ม | `menu_ar_cut_point` | `SMLERPAR._ar_cut_point` | _ar_cut_point |  |
| 8.1.6 TYGPro/Coffee | ข้อมูลลูกหนี้ › กำหนดรูปภาพ | `menu_ar_picture` | tag:ar (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.1.6 POS · 8.1.7 TYGPro/Coffee | ข้อมูลลูกหนี้ › แต้มสะสม | `menu_ar_point` | `SMLERPAR.ar_point` |  |  |
| 7.1.7 POS · 8.1.8 TYGPro/Coffee | ข้อมูลลูกหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label` | `SMLTransportLabel._transport_label` | _myManageData |  |
| 7.1.8 POS · 8.1.9 TYGPro/Coffee | ข้อมูลลูกหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label_print` | `SMLTransportLabel._transport_label_print` | _myManageData |  |
| 7.1.9 POS · 8.1.10 TYGPro/Coffee | ข้อมูลลูกหนี้ › นำเข้าที่อยู่จัดส่งลูกหนี้ | `menu_import_ar_transport_label` | `SMLTransportLabel._importTransportLabel` |  |  |
| 7.1.10 POS · 8.1.11 TYGPro/Coffee | ข้อมูลลูกหนี้ › คำณวนแต้มสะสม | `menu_ar_point_recal` | `SMLERPAR.ar_point_recal` |  |  |
| 7.1.11.1 POS · 8.1.12.1 TYGPro/Coffee | ข้อมูลลูกหนี้ › รายงาน › รายงานรายละเอียดลูกค้า-ตามรหัสลูกค้า | `menu_ar_report_detail_ar` | `SMLERPReport.ar._report_ar_detail` |  |  |
| 7.1.11.2 POS · 8.1.12.2 TYGPro/Coffee | ข้อมูลลูกหนี้ › รายงาน › รายงานแต้มคงเหลือลูกหนี้ | `menu_report_point_balance` | `SMLERPARReport.report._ar_report` |  | ลูกหนี้_แต้มคงเหลือ |
| 7.2 POS · 8.2 TYGPro/Coffee | ตั้งหนี้ยกมา (ลูกหนี้) | `menu_ar_debt_balance` | `SMLERPAR._ar_debt_balance` | _ar_ap_trans | 93 |
| 7.3 POS · 8.3 TYGPro/Coffee | เพิ่มหนี้ยกมา (ลูกหนี้) | `menu_ar_increase_debt` | `SMLERPAR._ar_increase_debt` | _ar_ap_trans | 95 |
| 7.4 POS · 8.4 TYGPro/Coffee | ลดหนี้ยกมา (ลูกหนี้) | `menu_ar_cn_balance` | `SMLERPAR._ar_cn_balance` | _ar_ap_trans | 97 |
| 7.5.1 POS · 8.5.1 TYGPro/Coffee | รายงาน › รายงานตั้งหนี้ยกมา | `menu_ar_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` |  | 93 |
| 7.5.2 POS · 8.5.2 TYGPro/Coffee | รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ar_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` |  | 95 |
| 7.5.3 POS · 8.5.3 TYGPro/Coffee | รายงาน › รายงานลดหนี้ยกมา | `menu_ar_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` |  | 97 |
| 7.6 POS · 8.6 TYGPro/Coffee | ตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 99 |
| 7.7 POS · 8.7 TYGPro/Coffee | เพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 101 |
| 7.8 POS · 8.8 TYGPro/Coffee | ลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 103 |
| 7.9.1 POS · 8.9.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_debt_balance_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 100 |
| 7.9.2 POS · 8.9.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_cn_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 104 |
| 7.9.3 POS · 8.9.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_increase_debt_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 102 |
| 7.9.4 POS · 8.9.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_ar_documents_early_year_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.5 POS · 8.9.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_report_ar_increase_debt_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.6 POS · 8.9.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_ar_reduction_dept_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.7 POS · 8.9.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_ar_cancel_documents_early_year_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.8 POS · 8.9.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_ar_cancel_increase_debt_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.9.9 POS · 8.9.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_ar_cancel_reduction_dept_other` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 7.10 POS · 8.10 TYGPro/Coffee | ใบวางบิล (ลูกหนี้) | `menu_ar_pay_bill` | `SMLERPAR._ar_pay_bill` | _ar_ap_trans, _formSaleOrderPreview | 235 |
| 7.11 POS · 8.11 TYGPro/Coffee | รับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_debt_billing` | `SMLERPAR._ar_debt_billing` | _ar_ap_trans, _formSaleOrderPreview | 239 |
| 7.12.1 POS · 8.12.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกใบวางบิล (ลูกหนี้) | `menu_ar_cancel_pay_bill` | `SMLERPAR._ar_cancel_pay_bill` | _ar_ap_trans | 236 |
| 7.12.2 POS · 8.12.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกชำระหนี้/ยกเลิกใบเสร็จรับเงิน | `menu_ar_cancel_debt_billing` | `SMLERPAR._ar_cancel_debt_billing` | _ar_ap_trans | 240 |
| 7.12.3 POS · 8.12.3 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกใบวางบิล(ลูกหนี้) | `menu_ar_report_cancel_pay_billing` | `SMLERPReportTool._reportArApTrans` |  | 236 |
| 7.12.4 POS · 8.12.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_cancel_invoice` | `SMLERPReportTool._reportArApTrans` |  | 240 |
| 7.12.5 POS · 8.12.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานใบวางบิล (ลูกหนี้) | `menu_ar_report_billing` | `SMLERPReportTool._reportArApTrans` |  | 235 |
| — | รายงาน/ยกเลิก › รายงานใบวางบิลพร้อมรายการย่อย | `menu_ar_report_billing_and_detail` | `SMLERPReport.ar._report_ar_billing_and_detail` |  |  |
| 7.12.6 POS · 8.12.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับชำระหนี้ประจำวัน | `menu_ar_report_pay_debt_trans` | `SMLERPReportTool._reportArApTrans` |  | 239 |
| 7.12.7 POS · 8.12.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_receipt` | `SMLERPReportTool._reportArApTrans` |  | 239 |
| 7.12.8 POS · 8.12.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงายใบเสร็จรับเงินพร้อมรายการย่อย | `menu_ar_report_receipt_and_detail` | `SMLERPReport.ar._report_ar_receipt_and_detail` |  |  |
| 7.12.9 POS · 8.12.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานภาษีถูกหัก ณ. ที่จ่าย | `menu_gl_wht_report_sum` | `SMLERPGL._report._tax._wht` |  |  |
| 7.13.1 POS · 8.13.1 TYGPro/Coffee | รายงานสรุป › รายงานใบส่งของค้างชำระ-ตามวันที่ | `menu_ar_report_invoice_remain_pay` | `SMLFastReport._designer` |  |  |
| 7.13.2 POS · 8.13.2 TYGPro/Coffee | รายงานสรุป › รายงานตรวจสอบยอดวงเงิน | `menu_ar_report_check_balance` | `SMLERPReport.ar._report_ar_check_balance` |  |  |
| 7.14.1 POS · 8.14.1 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานเคลื่อนไหวลูกหนี้ | `menu_ar_report_movement` | `SMLERPARAPReport.report._movement` |  |  |
| 7.14.2 POS · 8.14.2 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานอายุลูกหนี้ | `menu_ar_report_period_ar_debt_remain` | `SMLERPARAPReport.report._ageing` |  |  |
| 7.14.3 POS · 8.14.3 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานอายุลูกหนี้-ตามเอกสาร | `menu_ar_report_period_ar_debt_remain_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |  |
| 7.14.4 POS · 8.14.4 TYGPro/Coffee | รายงานวิเคราะห์ › รายงานสถานะลูกหนี้ | `menu_ar_report_status_ar` | `SMLERPARAPReport.report._absolute_status` |  |  |
| 7.15 POS · 8.15 TYGPro/Coffee | บันทึกรูปภาพเอกสาร | `menu_ar_doc_picture` | `SMLERPAR._ar_doc_picture` | _documentPicture |  |
| 7.16 POS · 7.13 Lite/TYG · 8.16 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_customer` | tag:fastreportother |  |  |

## เงินสด/ธนาคาร (110)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 8.1 POS · 9.1 TYGPro/Coffee | รายได้อื่นๆ | `menu_cash_income_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 250 |
| 8.2 POS · 9.2 TYGPro/Coffee | ลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 252 |
| 8.3 POS · 9.3 TYGPro/Coffee | เพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 254 |
| 8.4.1 POS · 9.4.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 251 |
| 8.4.2 POS · 9.4.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 253 |
| 8.4.3 POS · 9.4.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 255 |
| 8.4.4 POS · 9.4.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานรายได้อื่นๆ | `menu_cash_income_other_report` | `SMLERPReportTool._reportCashBankTrans` |  | 250 |
| 8.4.5 POS · 9.4.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_report` | tag:cashbank (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.4.6 POS · 9.4.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_report` | tag:cashbank (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.4.7 POS · 9.4.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel_report` | tag:cashbank (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.4.8 POS · 9.4.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_cancel_report` | tag:cashbank (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.4.9 POS · 9.4.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_cancel_report` | tag:cashbank (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.5 POS · 9.5 TYGPro/Coffee | ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 260 |
| 8.6 POS · 9.6 TYGPro/Coffee | ลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 262 |
| 8.7 POS · 9.7 TYGPro/Coffee | เพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 264 |
| 8.8.1 POS · 9.8.1 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 261 |
| 8.8.2 POS · 9.8.2 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 263 |
| 8.8.3 POS · 9.8.3 TYGPro/Coffee | รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 265 |
| 8.8.4 POS · 9.8.4 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_report` | `SMLERPReportTool._reportCashBankTrans` |  | 260 |
| 8.8.5 POS · 9.8.5 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 262 |
| 8.8.6 POS · 9.8.6 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_report` | `SMLERPReportTool._reportCashBankTrans` |  | 264 |
| 8.8.7 POS · 9.8.7 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 261 |
| 8.8.8 POS · 9.8.8 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 263 |
| 8.8.9 POS · 9.8.9 TYGPro/Coffee | รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` |  | 265 |
| 8.9.1 POS · 9.9.1 TYGPro/Coffee | เงินสดย่อย › เบิกเงินสดย่อย | `menu_cb_petty_cash_receive` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 300 |
| 8.9.2 POS · 9.9.2 TYGPro/Coffee | เงินสดย่อย › รับคืนเงินสดย่อย | `menu_cb_petty_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 2 |
| 8.9.3.1 POS · 9.9.3.1 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกเบิกเงินสดย่อย | `menu_cb_petty_cash_receive_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 302 |
| 8.9.3.2 POS · 9.9.3.2 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกรับคืนเงินสดย่อย | `menu_cb_petty_return_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 303 |
| 8.9.3.3 POS · 9.9.3.3 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › รายงานเบิกเงินสดย่อย | `menu_report_cb_petty_cash_request` | `SMLFastReport._designer` |  |  |
| 8.9.3.4 POS · 9.9.3.4 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › รายงานรับคืนเงินสดย่อย | `menu_report_cb_petty_cash_return` | `SMLFastReport._designer` |  |  |
| 8.9.3.5 POS · 9.9.3.5 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกเบิกเงินสดย่อย | `menu_report_cb_cancel_pettycash_request` | `SMLERPReportTool._reportTrans` |  | 302 |
| 8.9.3.6 POS · 9.9.3.6 TYGPro/Coffee | เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกรับคืนเงินสดย่อย | `menu_report_cb_cancel_pettycash_return` | `SMLERPReportTool._reportTrans` |  | 303 |
| 8.9.4.1 POS · 9.9.4.1 TYGPro/Coffee | เงินสดย่อย › รายงานสรุป › รายงานเคลื่อนไหวเงินสดย่อย | `menu_sub_cash_movements` | `SMLERPCASHBANKReport._report_petty_cash` |  | เงินสดย่อย_เคลื่อนไหว |
| 8.9.4.2 POS · 9.9.4.2 TYGPro/Coffee | เงินสดย่อย › รายงานสรุป › รายการตั้งเบิกเงินสดย่อย | `menu_report_cb_pettycash_request_budget` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.9.4.3 POS · 9.9.4.3 TYGPro/Coffee | เงินสดย่อย › รายงานสรุป › รายงานบันทึกขอเบิกเงินทดลองจ่าย - เรียงตามวันที่เอกสาร | `menu_report_cb_request_testpay` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.9.4.4 POS · 9.9.4.4 TYGPro/Coffee | เงินสดย่อย › รายงานสรุป › รายงานสถานะเงินสดย่อย | `menu_peety_cash_status` | `SMLERPCASHBANKReport._report_petty_cash` |  | เงินสดย่อย_สถานะ |
| 8.10.1.1 POS | ธนาคาร › ฝาก/ถอน › กำหนดสมุดเงินฝาก | `menu_book_bank` | `SMLERPConfig._book` | _myManageData, _searchDataFull |  |
| 8.10.1.2 POS | ธนาคาร › ฝาก/ถอน › บันทึกฝากเงิน | `menu_cb_cash_payin` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 401 |
| 8.10.1.3 POS | ธนาคาร › ฝาก/ถอน › บันทึกถอนเงิน | `menu_cb_cash_withdraw` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 402 |
| 8.10.1.4.1 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกฝากเงิน | `menu_cb_cash_payin_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 403 |
| 8.10.1.4.2 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกถอนเงิน | `menu_cb_cash_withdraw_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 404 |
| 8.10.1.4.3 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกฝากเงิน | `menu_report_cancel_withdraw` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.1.4.4 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกถอนเงิน | `menu_report_cancel_payin` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.1.4.5 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการฝากเงิน | `menu_report_cash_payin` | `SMLFastReport._designer` |  |  |
| 8.10.1.4.6 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการถอนเงิน | `menu_report_cash_withdraw` | `SMLFastReport._designer` |  |  |
| — | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการโอนเงินระหว่างธนาคาร | `menu_cb_report_transfer_bank` | `SMLERPReportTool._reportCashBankTrans` |  | 422 |
| 8.10.1.4.7 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานรายได้จากธนาคาร | `menu_cb_report_bank_income` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.1.4.8 POS | ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานค่าใช้จ่ายจากธนาคาร | `menu_cb_report_bank_expanse` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.1 POS · 9.10.1.1 TYGPro/Coffee | ธนาคาร › เช็ครับ › เช็ครับยกมา | `menu_cb_chq_in_receive_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 405 |
| 8.10.2.2 POS · 9.10.1.2 TYGPro/Coffee | ธนาคาร › เช็ครับ › ทะเบียนเช็ครับ | `menu_cb_chq_in_receive_master` | `SMLERPCASHBANK._cb_chq_in_receive_master` |  |  |
| 8.10.2.3 POS · 9.10.1.3 TYGPro/Coffee | ธนาคาร › เช็ครับ › บันทึกนำฝาก (เช็ครับ) | `menu_cb_chq_in_payin` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 410 |
| 8.10.2.4 POS · 9.10.1.4 TYGPro/Coffee | ธนาคาร › เช็ครับ › บันทึกเช็คผ่าน (เช็ครับ) | `menu_cb_chq_in_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 411 |
| 8.10.2.5 POS · 9.10.1.5 TYGPro/Coffee | ธนาคาร › เช็ครับ › บันทึกเช็คคืน (เช็ครับ) | `menu_cb_chq_in_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 412 |
| 8.10.2.6 POS · 9.10.1.6 TYGPro/Coffee | ธนาคาร › เช็ครับ › บันทึกเช็คขาดสิทธิ์ (เช็ครับ) | `menu_cb_chq_in_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 413 |
| 8.10.2.7 POS · 9.10.1.7 TYGPro/Coffee | ธนาคาร › เช็ครับ › บันทึกการเปลี่ยนเช็ค (เช็ครับ) | `menu_cb_chq_renew` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 416 |
| 8.10.2.8.1 POS · 9.10.1.8.1 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกนำฝากเช็ค | `menu_cb_chq_in_payin_cancle` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 430 |
| 8.10.2.8.2 POS · 9.10.1.8.2 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คผ่าน | `menu_cb_chq_in_honor_cancle` | `SMLERPCASHBANK._cb_chq_in_honor_cancle` |  |  |
| 8.10.2.8.3 POS · 9.10.1.8.3 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็ครับคืน | `menu_cb_chq_in_return_cancle` | `SMLERPCASHBANK._cb_chq_in_return_cancle` |  |  |
| 8.10.2.8.4 POS · 9.10.1.8.4 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็ค | `menu_cb_chq_cancel` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.5 POS · 9.10.1.8.5 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็ค | `menu_cb_chq_in_change_cancle` | `SMLERPCASHBANK._cb_chq_in_change_cancle` |  |  |
| 8.10.2.8.6 POS · 9.10.1.8.6 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกนำฝากเช็ค | `menu_report_cb_chq_in_payin_cancel` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.7 POS · 9.10.1.8.7 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็คผ่าน | `menu_report_cb_chq_in_honor_cancle` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.8 POS · 9.10.1.8.8 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็ครับคืน | `menu_report_cb_chq_in_return_cancle` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.9 POS · 9.10.1.8.9 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็ค | `menu_report_cb_chq_cancel` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.10 POS · 9.10.1.8.10 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็ค | `menu_report_cb_chq_in_change_cancle` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.2.8.11 POS · 9.10.1.8.11 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานทะเบียนเช็ครับ | `menu_cb_report_chq_in_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | เช็ค_รายงานเช็ครับ_ตามวันที่รับเช็ค |
| 8.10.2.8.12 POS · 9.10.1.8.12 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ | `menu_report_chq_card_detail_cheque_by_date_import` | `SMLERPReport.Cheque_Card._report_chq_card_Detail_Cheque_by_Date_Import` |  |  |
| 8.10.2.8.13 POS · 9.10.1.8.13 TYGPro/Coffee | ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานใบนำฝากเช็ครับพร้อมรายการย่อย | `menu_report_chq_card_disposit_cheque_detail` | `SMLERPReport.Cheque_Card._report_chq_card_Disposit_Cheque_Detail` |  |  |
| 8.10.3.1 POS · 9.10.2.1 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › เช็คจ่ายยกมา | `menu_cb_chq_out_payment_balance` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 406 |
| 8.10.3.2 POS · 9.10.2.2 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › ทะเบียนเช็คจ่าย | `menu_cb_chq_out_payment_master` | `SMLERPCASHBANK._cb_chq_out_payment_master` |  |  |
| 8.10.3.3 POS · 9.10.2.3 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › บันทึกเช็คผ่าน (เช็คจ่าย) | `menu_cb_chq_out_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 451 |
| 8.10.3.4 POS · 9.10.2.4 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › บันทึกเช็คคืน (เช็คจ่าย) | `menu_cb_chq_out_return` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 453 |
| 8.10.3.5 POS · 9.10.2.5 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › บันทึกเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_cb_chq_out_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 452 |
| 8.10.3.6 POS · 9.10.2.6 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › บันทึกการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_cb_chq_out_renew` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 456 |
| 8.10.3.7.1 POS · 9.10.2.7.1 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คจ่ายผ่าน | `menu_cb_chq_out_honor_cancle` | `SMLERPCASHBANK._cb_chq_out_honor_cancle` |  |  |
| 8.10.3.7.2 POS · 9.10.2.7.2 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิก ยกเลิกเช็ค | `menu_cb_chq_out_cancel_hornor_cancel` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.3.7.3 POS · 9.10.2.7.3 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็คจ่าย | `menu_cb_chq_out_change_cancle` | `SMLERPCASHBANK._cb_chq_out_change_cancle` |  |  |
| 8.10.3.7.4 POS · 9.10.2.7.4 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คจ่ายผ่าน | `menu_report_cb_chq_out_honor_cancel` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.3.7.5 POS · 9.10.2.7.5 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็คจ่าย | `menu_report_cb_chq_out_cancel_hornor_cancel` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.3.7.6 POS · 9.10.2.7.6 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็คจ่าย | `menu_report_cb_chq_out_change_cancle` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.3.7.7 POS · 9.10.2.7.7 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานทะเบียนเช็คจ่าย | `menu_cb_report_chq_out_payment` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | เช็ค_รายงานเช็คจ่าย_ตามวันที่จ่ายเช็ค |
| 8.10.3.7.8 POS · 9.10.2.7.8 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - วันครบกำหนด | `menu_report_chq_card_enddate_pay_cheque` | `SMLERPReport.Cheque_Card._report_chq_card_EndDate_Pay_Cheque` |  |  |
| 8.10.3.7.9 POS · 9.10.2.7.9 TYGPro/Coffee | ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานการยกเลิกเช็คจ่ายพร้อมรายการย่อย | `menu_report_chq_card_cancel_cheque_detail` | `SMLERPReport.Cheque_Card._report_chq_card_Cancel_Cheque_Detail` |  |  |
| 8.10.4.1 POS · 9.10.3.1 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › ทะเบียนบัตรเครดิต | `menu_cb_credit_card_receive` | `SMLERPCASHBANK._cb_credit_master` |  |  |
| 8.10.4.2 POS · 9.10.3.2 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › บันทึกขึ้นเงินบัตรเครดิต | `menu_cb_credit_card_pass` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 461 |
| 8.10.4.3 POS · 9.10.3.3 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › บันทึกยกเลิกบัตรเครดิต | `menu_cb_credit_card_cancel` | `SMLInventoryControl._clone_icTrans` | _icTransControl | 462 |
| 8.10.4.4 POS · 9.10.3.4 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › รายงานขึ้นเงินบัตรเครดิต | `menu_cb_report_credit_card_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | บัตรเครดิต_รายงานบัตรเครดิต_ตามวันที่รับ |
| 8.10.4.5 POS · 9.10.3.5 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › รายงานยกเลิกบัตรเครดิต | `menu_report_cb_credit_card_cancel` | `SMLERPReportTool._reportCashBankTrans` |  | 462 |
| 8.10.4.6 POS · 9.10.3.6 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › รายงานรายรายวันขึ้นเงินพร้อมรายการย่อย | `menu_report_cb_credit_card_receive` | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.4.7 POS · 9.10.3.7 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › รายงานรายละเอียดบัตรเครดิต - ครบกำหนด | `menu_report_chq_card_enddate_card` | `SMLERPReport.Cheque_Card._report_chq_card_EndDate_Card` |  |  |
| 8.10.4.8 POS · 9.10.3.8 TYGPro/Coffee | ธนาคาร › บัตรเครดิต › รายงานการยกเลิกบัตรพร้อมรายการย่อย | `menu_report_chq_card_cancel_card_detail` | `SMLERPReport.Cheque_Card._report_chq_card_Cancel_Card_Detail` |  |  |
| 8.10.5.1 POS · 9.10.4.1 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงานเคลื่อนไหวเงินสด | `_menu_cash_movements` | `SMLERPReport.cash_bank.Pay_Cash_by_DocDate` |  |  |
| 8.10.5.2 POS · 9.10.4.2 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงานการฝากเงินสด | `_menu_cash_deposit` | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.10.5.3 POS · 9.10.4.3 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงานการรับเงินอื่นๆพร้อมรายการย่อย | `_menu_received_cash_sub_item` | `SMLERPReport.cash_bank.Received_Cash_sub_item` |  |  |
| 8.10.5.4 POS · 9.10.4.4 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงานสรุปการจ่ายเงิน | `_menu_summary_payment` | `SMLERPReport.cash_bank.Summary_Payment` |  |  |
| 8.10.5.5 POS · 9.10.4.5 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงานยอดเงินคงเหลือสมุดฝากธนาคาร | `_menu_book_bank_balance` | `SMLERPReport.cash_bank.Book_Bank_Balance` |  |  |
| 8.10.5.6 POS · 9.10.4.6 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงาน Bank Statement | `_menu_bank_statement` | `SMLERPReport.cash_bank._bankStatment` |  |  |
| 8.10.5.7 POS · 9.10.4.7 TYGPro/Coffee | ธนาคาร › รายงานสรุป › รายงาน Statement ล่วงหน้า | `_menu_statement_advance` | `SMLERPReport.cash_bank.Statement_Advance` |  |  |
| 8.11.1 POS · 9.11.1 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย | `menu_report_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.11.2 POS · 9.11.2 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.11.3 POS · 9.11.3 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (รูปแบบใหม่) | `menu_report_vat_sale_2557` | `SMLERPGL._tax._vat` |  |  |
| 8.11.4 POS · 9.11.4 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษีขาย | `menu_report_sum_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.11.5 POS · 9.11.5 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ | `menu_report_vat_buy` | `SMLERPGL._tax._vat` |  |  |
| 8.11.6 POS · 9.11.6 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ (รูปแบบใหม่) | `menu_report_vat_buy_2557` | `SMLERPGL._tax._vat` |  |  |
| 8.11.7 POS · 9.11.7 TYGPro/Coffee | ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษี | `menu_gl_vat_report_sum` | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| 8.12.1 POS · 9.12.1 TYGPro/Coffee | หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.53) | `menu_gl_wht_report_in_53` | `SMLERPGL._report._tax._wht` |  |  |
| 8.12.2 POS · 9.12.2 TYGPro/Coffee | หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย (ภงด.3) | `menu_gl_wht_report_in_3` | `SMLERPGL._report._tax._wht` |  |  |
| 8.12.3 POS · 9.12.3 TYGPro/Coffee | หัก ณ. ที่จ่าย › รายงานภาษีถูกหัก ณ. ที่จ่าย | `menu_gl_wht_report_sum` | `SMLERPGL._report._tax._wht` |  |  |
| 8.13 POS · 9.13 TYGPro/Coffee | บันทึกรูปภาพเอกสาร | `menu_cb_doc_picture` | `SMLERPCASHBANK._cb_doc_picture` | _documentPicture |  |
| 8.14 POS · 9.14 TYGPro/Coffee | รายงานอื่น ๆ | `menu_fastreport_other_cashbank` | tag:fastreportother |  |  |

## เภสัช (11)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| — | บันทึกการจ่ายยา | `pm_counseling` | `SMLPosClient._posLoginForm` |  |  |
| — | กำหนดค่ามาตรฐานสุขภาพ | `menu_healthy_m_healty_standard` | `SMLHealthyConfig._m_information` |  |  |
| — | สินค้ายาและอาหารสุขภาพ › กลุ่มยาตาม MIM | `menu_setup_ic_healthy_m_mim_group` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ช่วงเวลาการใช้ยา | `menu_setup_ic_healthy_m_times` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ข้อกำหนดเวลาใช้ยา | `menu_setup_ic_healthy_m_frequency` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ขนาดและวิธีใช้ยา | `menu_setup_ic_healthy_m_dozen` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › คำเตือนการใช้ยา | `menu_setup_ic_healthy_m_warning` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › สรรพคุณยา | `menu_setup_ic_healthy_m_properties` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ชนิดโรค | `menu_setup_ic_healthy_m_disease` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ตารางความเสี่ยงกระดูกพรุน | `menu_setup_ic_healthy_m_kkos` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |
| — | สินค้ายาและอาหารสุขภาพ › ดัชนีมวลกาย | `menu_setup_ic_healthy_m_bodymassindex` | `MyLib._manageMasterCodeFull` | _managerMasterScreenClass, _myManageData |  |

## ภาษีมูลค่าเพิ่ม (8)

| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |
|---|---|---|---|---|---|
| 8.1 Lite/TYG | รายงาน ภาษีขาย | `menu_report_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.2 Lite/TYG | รายงาน ภาษีขาย (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.3 Lite/TYG | รายงานภาษีขาย (รูปแบบใหม่) | `menu_report_vat_sale_2557` | `SMLERPGL._tax._vat` |  |  |
| 8.4 Lite/TYG | รายงานภาษีขาย (รูปแบบใหม่แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale_with_tax` | `SMLERPGL._tax._vat` |  |  |
| 8.5 Lite/TYG | รายงานสรุปภาษีขาย | `menu_report_sum_vat_sale` | `SMLERPGL._tax._vat` |  |  |
| 8.6 Lite/TYG | รายงาน ภาษีซื้อ | `menu_report_vat_buy` | `SMLERPGL._tax._vat` |  |  |
| 8.7 Lite/TYG | รายงาน ภาษีซือ (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_buy` | `SMLERPGL._tax._vat` |  |  |
| 8.8 Lite/TYG | รายงาน ภาษีซื้อ (รูปแบบใหม่) | `menu_report_vat_buy_2557` | `SMLERPGL._tax._vat` |  |  |
