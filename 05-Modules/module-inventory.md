---
tags: [sml, module, inventory, generated]
menu_group: "สินค้า"
trans_flags: [36, 54, 56, 57, 58, 59, 60, 61, 66, 67, 68, 69, 72, 73, 76, 122, 123, 124, 276, 501]
---
# โมดูล: สินค้า

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- ข้อมูลหลักสินค้า `ic_inventory` (+ barcode, หน่วย, ราคา) และเอกสารสต็อก: ยกมา 54, เบิก 56, รับคืนจากเบิก 58, รับสำเร็จรูป 60, ปรับปรุง 66/68, โอน 70/72, ตรวจนับ
- เอกสารสต็อกส่วนใหญ่เปิดด้วย `SMLInventoryControl._clone_icTrans(transType, menuName)`
- ต้นทุนคำนวณหลังบันทึกผ่าน web service (Average/FIFO/Lot) ดู [[document-engine]]

## ตัวเลข

- เมนูปลายทาง 160 รายการ, จับคู่คลาสได้ 156, เห็นใน SMLAccountPOSProfessional (edition 12) 138
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPReportTool._reportTrans` (14), `SMLFastReport._designer` (11), `SMLInventoryControl._clone_icTrans` (11), `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` (11), `SMLERPICReport._report_ic_summary` (8), `SMLERPIC._cancelControl` (7)
- control หลักที่ฝัง: `SMLERPControl._icInfoProcess` (25), `SMLInventoryControl._icTransControl` (23), `SMLERPControl._barcodeSearchForm` (12), `SMLERPControl._icmainScreenTopControl` (12), `SMLERPControl._selectWarehouseAndLocationForm` (8), `SMLERPControl._icPictureForm` (5)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 36 | ขาย_สั่งขาย | 1 |
| 54 | สินค้า_ยอดคงเหลือสินค้ายกมา | 2 |
| 56 | สินค้า_เบิกสินค้าวัตถุดิบ | 2 |
| 57 | สินค้า_เบิกสินค้าวัตถุดิบ_ยกเลิก | 2 |
| 58 | สินค้า_รับคืนสินค้าจากการเบิก | 2 |
| 59 | สินค้า_รับคืนสินค้าจากการเบิก_ยกเลิก | 2 |
| 60 | สินค้า_รับสินค้าสำเร็จรูป | 2 |
| 61 | สินค้า_รับสินค้าสำเร็จรูป_ยกเลิก | 2 |
| 66 | สินค้า_ปรับปรุงสต็อก | 2 |
| 67 | สินค้า_ปรับปรุงสต็อก_ยกเลิก | 2 |
| 68 | สินค้า_ปรับปรุงสต๊อก_ขาด | 2 |
| 69 | สินค้า_ปรับปรุงสต๊อก_ขาด_ยกเลิก | 2 |
| 72 | สินค้า_โอนออก | 2 |
| 73 | สินค้า_โอนออก_ยกเลิก | 2 |
| 76 | สินค้า_ตรวจนับสินค้า | 2 |
| 122 | สินค้า_ขอเบิกสินค้าวัตถุดิบ | 1 |
| 123 | สินค้า_ขอเบิกสินค้าวัตถุดิบ_ยกเลิก | 1 |
| 124 | สินค้า_ขอโอน | 1 |
| 276 | สินค้า_ขอตรวจนับสินค้า | 1 |
| 501 | คลัง_ยอดคงเหลือสินค้ายกมา | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_resource`, `ic_inventory`, `ic_trans_detail`, `ic_trans`, `ic_unit`, `ic_inventory_barcode`, `ar_customer`, `cb_trans_detail`, `ap_supplier`, `sml_fastreport`, `master_logs`, `ic_serial`, `ic_trans_serial_number`, `ic_unit_use`, `ic_purchase_permium`, `ic_purchase_permium_condition`, `ic_inventory_detail`, `ar_type`, `ap_ar_resource`, `resource_report`, `ic_inventory_price`, `ic_wh_shelf`, `ic_name_billing`, `ic_name_merket`, `ic_color_use`, `ic_size_use`, `ic_name_short`, `ic_name_pos`, `ic_pattern_use`, `ic_inventory_set_detail`, `erp_doc_format`, `images`, `ic_shelf`, `ic_warehouse`, `ic_inventory_price_formula`, `ar_group_sub`, `ar_group`, `ic_quality_control`, `ic_opposite_unit`, `ic_standard_cost`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ข้อมูลสินค้า › ข้อมูลสินค้า | `menu_ic_item_detail` | ✓ | `SMLERPIC._icMain` |  | ic_inventory, ic_unit_use, ic_inventory_barcode, ic_inventory_detail |
| ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_barcode` | ✓ | `SMLERPIC._icMain` |  | ic_inventory, ic_unit_use, ic_inventory_barcode, ic_inventory_detail |
| ข้อมูลสินค้า › ข้อมูลสินค้าเพิ่มเติม | `menu_ic_item_detail_2` | ✓ | `SMLERPIC._icMainDetail` |  | ic_inventory, ic_inventory_detail, ic_size, ic_size_use |
| ข้อมูลสินค้า › ข้อมูลสินค้าเพิ่มเติม (แสดงตามบาร์โค๊ด) | `menu_ic_item_detail_2_barcode` | ✓ | `SMLERPIC._icMainDetail` |  | ic_inventory, ic_inventory_detail, ic_size, ic_size_use |
| ข้อมูลสินค้า › รายละเอียดสินค้า | `menu_ic_description` | ✓ | `SMLERPIC._icDescription` |  | ic_inventory, ic_description |
| ข้อมูลสินค้า › แก้ไขรายละเอียด(เร็ว) | `menu_ic_description_fast` | ✓ | `SMLERPIC._icEditDetailFast` |  | ic_inventory, ic_resource |
| ข้อมูลสินค้า › กำหนดบาร์โค้ดสินค้า | `menu_ic_item_barcode` | ✓ | `SMLERPIC._icBarcode` |  | ic_inventory, ic_inventory_barcode |
| ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด | `menu_ic_item_barcode_discount` | ✓ | `SMLERPIC._icBarcodeDiscount` |  | ic_inventory_barcode_price, ic_inventory_barcode |
| ข้อมูลสินค้า › กำหนดส่วนลดตามบาร์โค๊ด (เร็ว) | `menu_ic_item_multibarcode_discount` | ✓ | `SMLERPIC._icMultiBarcodeDiscount` |  | ic_inventory_barcode_price, ic_inventory_barcode, ic_unit |
| ข้อมูลสินค้า › กำหนดลำดับการค้นหา | `menu_ic_item_level` | ✓ | `SMLERPIC._icSearchLevel` |  | ic_unit_use, ic_inventory_barcode, ic_inventory_barcode_condition, ic_inventory_level |
| ข้อมูลสินค้า › กำหนดลำดับการค้นหา (เร็ว) | `menu_ic_multi_item_level` | ✓ | `SMLERPIC._icSearchLevelMultiItem` |  | ic_inventory_level, ic_inventory_barcode, ic_unit, POS_ID |
| ข้อมูลสินค้า › กำหนดรูปภาพ | `menu_ic_item_picture` | ✓ | `SMLERPIC._icMainDetailPicture` |  | ic_inventory, images, ic_inventory_barcode |
| ข้อมูลสินค้า › กำหนดรูปภาพตามบาร์โค้ด | `menu_ic_item_barcode_picture` | ✓ | `SMLERPIC._icBarcodePicture` |  | ic_inventory_barcode, ic_inventory, images |
| ข้อมูลสินค้า › กำหนดสูตรโปรโมชั่น | `pos_promotion_formula` | ✓ | `SMLERPIC._icPromotion._formula` |  | ic_promotion_formula_action, ic_promotion_formula, ic_promotion_formula_condition, ic_promotion_formula_price_discount |
| ข้อมูลสินค้า › กำหนดแคมเปญท้ายใบเสร็จ | `menu_setup_pos_slip_campaign` | ✓ | `SMLERPControl.pos_slip_campaign.pos_slip_campaign` |  | pos_slip_campaign, pos_slip_campaign_items, pos_slip_campaign_group, pos_slip_campaign_brand |
| ข้อมูลสินค้า › ทะเบียน Serial Number | `menu_ic_item_serial` | ✓ | `SMLERPIC._icSerialNumber` |  | ic_serial |
| ข้อมูลสินค้า › สินค้าชุด | `menu_ic_item_set` | ✓ | `SMLERPIC._icMainProductSet` |  | ic_inventory_set_detail, ic_inventory, ic_unit |
| ข้อมูลสินค้า › เพิ่มบาร์โค๊ดสินค้าแบบเร็ว | `menu_ic_item_add_barcode_fast` | ✓ | `SMLERPIC._icAddBarcodeFastControl` |  | ic_wh_shelf, ic_inventory_barcode, ic_shelf, ic_inventory |
| ข้อมูลสินค้า › ตรวจสอบสินค้าหลายหน่วยนับ | `menu_ic_unit_checker` |  | `SMLERPIC._icUnitCheckerControl` |  | ic_inventory, ic_unit_use |
| ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดจาก Text File | `menu_ic_item_barcode_checker` | ✓ | `SMLERPIC._barcodeCheckerControl` |  | ic_inventory_barcode, ic_inventory |
| ข้อมูลสินค้า › ตรวจสอบบาร์โค๊ดตามมาตรฐาน EAN13 | `menu_ic_item_barcode_checker_ean13` | ✓ | `SMLBarcodeManage._itemBarcodeCheckerEan13` |  | ic_inventory_barcode |
| ข้อมูลสินค้า › ตรวจสอบราคาสินค้า | `check_price` | ✓ | `SMLPOSControl._checkPriceUserControl` |  | ic_inventory_barcode |
| ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป | `menu_ic_item_barcode_laser_print` | ✓ | `SMLBarcodeManage._itemBarcodePrint` | 501 | ic_inventory_barcode, ic_inventory_price_formula, sml_barcode_print_format, ic_unit |
| ข้อมูลสินค้า › กำหนดการค้นหาแบบเฉพาะเจาะจง | `menu_ic_specific_search` |  | `SMLERPIC._icSpecificSearch` |  | ic_specific_search_word, ic_specific_search |
| ข้อมูลสินค้า › คลังที่เก็บสินค้า | `menu_ic_warehouse_locaton` | ✓ | `SMLERPIC._icWarehouseLocation` |  | ic_inventory, ic_unit_use, ic_inventory_detail, ic_warehouse |
| ข้อมูลสินค้า › กำหนดกลุ่มที่เก็บ | `ic_warehouse_and_location_group` | ✓ | `SMLERPIC._whLocationGroup` |  | ic_warehouse_location_group_detail, ic_warehouse_location_group |
| ข้อมูลสินค้า › รายงาน › รายงานรายละเอียดสินค้า | `menu_ic_detail` | ✓ | `SMLERPICReport._report_ic_master` |  | ic_inventory, ic_unit |
| ข้อมูลสินค้า › รายงาน › รายงานสินค้าชุด | `menu_ic_report_item_set_formula` | ✓ | `SMLERPICReport._report_item_set_formula` |  | ic_inventory_set_detail, ic_unit |
| ข้อมูลสินค้า › รายงาน › รายงานบาร์โค้ดสินค้า | `menu_ic_report_item_barcode` | ✓ | `SMLERPICReport._report_ic_barcode` |  | ic_inventory_barcode, ic_unit |
| ข้อมูลสินค้า › รายงาน › รายงานสินค้าแบบมี Serial | `menu_ic_by_license` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| ข้อมูลสินค้า › กำหนดสินค้า | `menu_ic_item_for_sync` | ✓ | `SMLERPIC._icMain` |  | ic_inventory, ic_unit_use, ic_inventory_barcode, ic_inventory_detail |
| ข้อมูลสินค้า › ปรับราคาสินค้า | `menu_ic_modify_price` | ✓ | `SMLERPIC._icModifyPrice` |  | ic_inventory_price, ic_inventory_price_formula, ic_resource, ic_inventory_barcode |
| กำหนดราคาซื้อ | `menu_ic_purchase_price` | ✓ | `SMLInventoryControl._icPurchasePrice._icPriceList` |  | ic_inventory_purchase_price, ic_inventory, ic_unit, ar_customer |
| ของแถมซื้อ | `menu_ic_purchase_premium` | ✓ | `SMLERPIC._icPurchasePermium` |  | ic_purchase_permium, ic_purchase_permium_condition, ic_purchase_permium_list, ic_inventory |
| กำหนดราคาขายมาตรฐาน | `menu_ic_item_saleprice` | ✓ | `SMLInventoryControl._icPrice._icPriceList` |  | ic_inventory_price, ic_inventory, ar_group_sub, ic_unit |
| กำหนดราคาขายทั่วไป | `menu_ic_item_saleprice_2` | ✓ | `SMLInventoryControl._icPrice._icPriceList` |  | ic_inventory_price, ic_inventory, ar_group_sub, ic_unit |
| กำหนดส่วนลดสินค้า | `menu_ic_discount` | ✓ | `SMLInventoryControl._icPrice._icDiscount` |  | ic_inventory_discount, ar_group_sub, ic_unit, ar_group |
| กำหนดรูปแบบสูตรราคาขาย | `menu_ic_item_formula_template` | ✓ | `SMLInventoryControl._icPrice._icPriceFormulaTemplate` |  | ic_price_formula_template |
| กำหนดสูตรราคาขาย | `menu_ic_item_saleprice_formula` | ✓ | `SMLInventoryControl._icPrice._icPriceFormula` |  | ic_inventory, ic_inventory_price_formula, ic_inventory_barcode, master_logs |
| ราคาขายสินค้า | `menu_ic_all_price` | ✓ | `SMLInventoryControl._icPrice._icAllPrice` |  | ic_inventory_price, ic_unit_use, ic_inventory, ic_inventory_barcode |
| รายงาน › รายงานราคาซื้อสินค้า | `menu_ic_report_item_purchase_price` | ✓ | `SMLERPICReport._report_ic_purchase_price` |  | ic_inventory_purchase_price, ic_resource, ic_unit |
| รายงาน › รายงานของแถมซื้อ | `menu_ic_report_item_giveaway` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| รายงาน › รายงานราคาขายสินค้ามาตรฐาน | `menu_ic_report_item_sale_price` | ✓ | `SMLERPICReport._report_ic_sale_price` |  | ic_inventory_price, ic_resource, ic_unit |
| รายงาน › รายงานราคาขายสินค้าทั่วไป | `menu_ic_report_item_sale_price_normal` | ✓ | `SMLERPICReport._report_ic_sale_price` |  | ic_inventory_price, ic_resource, ic_unit |
| ตรวจสอบคุณภาพสินค้า › กำหนดจำนวนภาชนะ(Container) | `menu_imex_qc_purchase_packing_size_container_assign` |  | `IMEXControl.QualityControl.ICQCPurchaesPackingSizeSplit` |  | ic_qc_purchase_packing_size, ic_qc_purchase_packing_size_item, ic_qc_purchase_packing_size_container |
| ตรวจสอบคุณภาพสินค้า › บันทึกรับสินค้า | `menu_ic_qc_receive` |  | `IMEXControl.QualityControl.ICQCProductReceive` |  | ic_qc_lab, erp_doc_format, ic_trans, ic_qc_purchase_packing_size_container |
| ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพ - Pass | `menu_ic_qc_control_pass` |  | `IMEXControl.QualityControl.ICQCPassControl` |  | ic_quality_control, ic_quality_control_detail, ic_trans, ic_trans_detail |
| ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพ - Reject | `menu_ic_qc_control_reject` |  | `IMEXControl.QualityControl.ICQCRejectControl` |  | ic_quality_control, ic_quality_control_detail, ic_trans, ic_trans_detail |
| ตรวจสอบคุณภาพสินค้า › บันทึกการตรวจสอบคุณภาพซ้ำ (ReTest) | `menu_ic_qc_retest` |  | `IMEXControl.QualityControl.ICQCRetestControl` |  | ic_quality_control, ic_quality_control_detail, ic_qc_container_adjust, ic_qc_container_transaction |
| ตรวจสอบคุณภาพสินค้า › ทะเบียนการตรวจสอบคุณภาพ | `menu_ic_qc_lab_list` |  | `IMEXControl.QualityControl.ICQCLabList` |  | ic_qc_lab, ic_quality_control, ic_qc_lab_container |
| ตรวจสอบคุณภาพสินค้า › กำหนดค่าระบบตรวจสอบคุณภาพ | `menu_imex_qc_config` |  | `IMEXControl.QualityControl._qcConfigScreen` |  | ic_qc_config |
| ตรวจสอบคุณภาพสินค้า › กำหนด Identify | `menu_qc_indentify` |  | `MyLib._manageMasterCodeFull` |  | ic_qc_indentify |
| ตรวจสอบคุณภาพสินค้า › พิมพ์แท็กสินค้า | `menu_print_tag_label` |  | `SMLInventoryControl._icTransLabelPrintControl` |  | erp_doc_format, formdesign, ic_trans, ic_trans_detail |
| ตรวจสอบคุณภาพสินค้า › บันทึก Lab Container ยกมา | `menu_qc_lab_beginning_balance` |  | `IMEXControl.QualityControl.LabBeginningBalance.QCLabBalance` |  | ic_qc_lab_beginning_balance, ic_qc_lab_beginning_balance_detail, ic_qc_lab_beginning_balance_lab, ic_qc_lab_beginning_balance_lab_container |
| ตรวจสอบคุณภาพสินค้า › บันทึกเบิก Container | `menu_imex_qc_container_issue` |  | `IMEXControl.QualityControl.ProductContainerIssue._productContainerIssueControl` |  | ic_qc_lab_container_issue, ic_qc_container_transaction |
| ตรวจสอบคุณภาพสินค้า › บันทึกปรับปรุง Container | `menu_imex_qc_container_adjustment` |  | `IMEXControl.QualityControl.ProductContainerAdjustment._productContainerAdjustmentControl` |  | ic_qc_container_adjust, ic_qc_container_transaction, ic_qc_container_adjustment_detail |
| ตรวจสอบคุณภาพสินค้า › บันทึกการตัดจากระบบ weighing System | `menu_qc_lab_cut` |  | `IMEXControl.QualityControl.QCLabCut._qcLabCutControl` |  | ic_qc_lab_cut, ic_qc_lab_cut_detail, ic_trans, ic_trans_detail |
| ตรวจสอบคุณภาพสินค้า › อนุมัติผู้จำหน่ายและสินค้า | `menu_qc_approved_vendor` |  | `IMEXControl.QualityControl._approvedVendorControl` |  | qc_approved_vendor_list |
| ตรวจสอบคุณภาพสินค้า › รายงานการอนุมัติผู้จำหน่ายสินค้า | `report_imex_qc_approved_vendor` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ตรวจสอบคุณภาพสินค้า › Lab Information | `menu_imex_qc_lab_information` |  | `IMEXControl.QualityControl.QCLatInformation.LabInformation` |  |  |
| สินค้า/วัตถุดิบ คงเหลือยกมา | `menu_ic_stk_balance` | ✓ | `SMLInventoryControl._clone_icTrans` | 54 |  |
| ใบสั่งผลิต | `menu_imex_sale_order` |  | `SMLERPSO._soSaleorder` | 36 |  |
| รับสินค้าสำเร็จรูป | `menu_ic_finish_receive` | ✓ | `SMLInventoryControl._clone_icTrans` | 60 |  |
| ขอเบิกสินค้า/วัตถุดิบ | `menu_ic_request_issue` | ✓ | `SMLInventoryControl._clone_icTrans` | 122 |  |
| เบิกสินค้า/วัตถุดิบ | `menu_ic_issue` | ✓ | `SMLInventoryControl._clone_icTrans` | 56 |  |
| รับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive` | ✓ | `SMLInventoryControl._clone_icTrans` | 58 |  |
| รายงาน/ยกเลิก › ยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_finish_receive_cancel` | ✓ | `SMLERPIC._cancelControl` | 61 |  |
| รายงาน/ยกเลิก › ยกเลิกขอเบิกสินค้า/วัตถุดิบ | `menu_ic_request_issue_cancel` | ✓ | `SMLERPIC._cancelControl` | 123 |  |
| รายงาน/ยกเลิก › ยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_issue_cancel` | ✓ | `SMLERPIC._cancelControl` | 57 |  |
| รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_return_receive_cancel` | ✓ | `SMLERPIC._cancelControl` | 59 |  |
| รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_report_cancel_goods_pack` | ✓ | `SMLERPReportTool._reportTrans` | 61 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_report_cancel_raw_material` | ✓ | `SMLERPReportTool._reportTrans` | 57 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_report_cancel_goods_raw_meterial` | ✓ | `SMLERPReportTool._reportTrans` | 59 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสินค้าและวัตถุดิบ คงเหลือยกมา | `menu_ic_report_goods_balance` | ✓ | `SMLERPReportTool._reportTrans` | 54 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการรับสินค้าสำเร็จรูป | `menu_import_item_ready_by_date` | ✓ | `SMLERPReportTool._reportTrans` | 60 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการเบิกสินค้าและวัตถุดิบ | `menu_ic_report_item_withdraw` | ✓ | `SMLERPReportTool._reportTrans` | 56 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานรับคืนสินค้าและวัตถุดิบ จากการเบิก | `menu_ic_report_item_return` | ✓ | `SMLERPReportTool._reportTrans` | 58 | ic_trans, ic_trans_detail, cb_trans_detail |
| ขอโอนสินค้า/วัตถุดิบ | `menu_ic_request_transfer` | ✓ | `SMLInventoryControl._clone_icTrans` | 124 |  |
| โอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out` | ✓ | `SMLInventoryControl._clone_icTrans` | 72 |  |
| ระบบตรวจนับสินค้า › ขอตรวจนับสินค้า | `menu_ic_request_stk_count` | ✓ | `SMLInventoryControl._clone_icTrans` | 276 |  |
| ระบบตรวจนับสินค้า › ตรวจนับสินค้า | `menu_ic_stk_count` | ✓ | `SMLInventoryControl._clone_icTrans` | 76 |  |
| ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number | `menu_ic_serialnumber_checker` | ✓ | `SMLERPIC._icSerialStockCheck` |  | ic_inventory, ic_trans_serial_number, ic_trans, ic_serial |
| ระบบตรวจนับสินค้า › รายงานผลต่างจากการตรวจนับ | `menu_diff_from_count` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| ระบบตรวจนับสินค้า › รายงานสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ | `menu_stock_no_balance_from_count` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| ระบบตรวจนับสินค้า › รายงานการตรวจสอบสินค้า Serial | `menu_report_serial_check` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ | `menu_ic_stk_adjust_auto` | ✓ | `SMLInventoryControl._stockAutoAdjustControl` |  | ic_trans_detail, erp_doc_format, ic_trans, ic_inventory |
| ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ (สินค้า Lot) | `menu_ic_stk_adjust_lot_auto` | ✓ | `SMLInventoryControl._stockAutoAdjustLotControl` |  | ic_trans, ic_trans_detail, ap_ar_trans_detail, ic_inventory |
| ระบบตรวจนับสินค้า › ปรับปรุงมูลค่าสินค้า Lot คงค้าง | `menu_ic_adjust_stock_lot_amount` | ✓ | `SMLInventoryControl.StockLotAdjustmentForm` |  | ic_trans, ic_trans_detail, ic_resource, logs |
| ปรับปรุงสต็อกสินค้า/วัตถุดิบ (เพิ่ม) | `menu_ic_stk_adjust` | ✓ | `SMLInventoryControl._clone_icTrans` | 66 |  |
| ปรับปรุงสต็อกสินค้า/วัตถุดิบ (ลด) | `menu_ic_stk_adjust_subtract` | ✓ | `SMLInventoryControl._clone_icTrans` | 68 |  |
| ประมวลผลเฉลี่ยต้นทุนแฝง | `menu_ic_hidden_cost_process` | ✓ | `SMLERPIC._icHiddenCost._icHiddenCostProcess` |  | ic_hidden_cost_process_ref, ic_hidden_cost_process, ic_hidden_cost_process_item, ic_trans |
| รายงาน/ยกเลิก › ยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_transfer_wh_out_cancel` | ✓ | `SMLERPIC._cancelControl` | 73 |  |
| รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_stk_adjust_over_cancel` | ✓ | `SMLERPIC._cancelControl` | 67 |  |
| รายงาน/ยกเลิก › ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_stk_adjust_lost_cancel` | ✓ | `SMLERPIC._cancelControl` | 69 |  |
| รายงาน/ยกเลิก › รายงานยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_report_stk_cancel` | ✓ | `SMLERPReportTool._reportTrans` | 73 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_report_stk_cancel_over` | ✓ | `SMLERPReportTool._reportTrans` | 67 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_report_stk_cancel_lost` | ✓ | `SMLERPReportTool._reportTrans` | 69 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการโอนสินค้าและวัตถุดิบ | `menu_ic_report_item_transfer` | ✓ | `SMLERPReportTool._reportTrans` | 72 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานตรวจนับสินค้า | `menu_ic_report_item_count` | ✓ | `SMLERPReportTool._reportTrans` | 76 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการปรับปรุงสต็อกสินค้าและวัตถุดิบ (เกิน) | `menu_ic_report_item_adjust_increase` | ✓ | `SMLERPReportTool._reportTrans` | 66 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) | `menu_ic_report_item_adjust_decrease` | ✓ | `SMLERPReportTool._reportTrans` | 68 | ic_trans, ic_trans_detail, cb_trans_detail |
| วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้า | `menu_ic_info_stk_balance` | ✓ | `SMLERPICInfo._stkBalance` |  | ic_resource |
| วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามคลัง | `menu_ic_info_stk_balance_warehouse` | ✓ | `SMLERPICInfo._stkBalanceWareHouse` |  |  |
| วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตามที่เก็บ | `menu_ic_info_stk_balance_shelf` | ✓ | `SMLERPICInfo._stkBalanceLocation` |  |  |
| วิเคราะห์ข้อมูล › ยอดคงเหลือสินค้าตาม LOT | `menu_ic_info_stk_balance_lot` | ✓ | `SMLERPICInfo._stkBalanceByLot` |  | ic_resource, ic_trans_detail_lot |
| วิเคราะห์ข้อมูล › เคลื่อนไหวสินค้า | `menu_ic_info_stk_move` | ✓ | `SMLERPICInfo._stkMovement` |  | ic_resource, ic_inventory |
| วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ | `menu_ic_info_stk_movement` | ✓ | `SMLERPICInfo._stkMovement` |  | ic_resource, ic_inventory |
| วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ (รวมต้นทุนแฝง) | `menu_ic_info_stk_movement_hidden` | ✓ | `SMLERPICInfo._stkMovement` |  | ic_resource, ic_inventory |
| วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามปริมาณ | `menu_ic_info_stk_movement_sum` | ✓ | `SMLERPICInfo._stkMovementSum` |  | ic_resource, ic_inventory |
| วิเคราะห์ข้อมูล › สรุปการเคลื่อนไหวตามมูลค่า | `menu_ic_info_stk_movement_sum_by_amount` | ✓ | `SMLERPICInfo._stkMovementSum` |  | ic_resource, ic_inventory |
| วิเคราะห์ข้อมูล › สินค้าถึงจุดสั่งซื้อ | `menu_ic_info_stk_reorder` | ✓ | `SMLInventoryControl._stkReorder` |  | ic_trans_detail, ic_inventory, ic_resource, ap_supplier |
| วิเคราะห์ข้อมูล › ประวัติการซื้อสินค้า | `menu_ic_info_purchase_history` | ✓ | `SMLInventoryControl._transHistory` |  | ic_trans_detail, ap_supplier, ar_customer, ic_inventory |
| วิเคราะห์ข้อมูล › ประวัติการขายสินค้า | `menu_ic_info_sale_history` | ✓ | `SMLInventoryControl._transHistory` |  | ic_trans_detail, ap_supplier, ar_customer, ic_inventory |
| วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการเคลื่อนไหว | `menu_ic_info_product_no_movement` | ✓ | `SMLERPICInfo._stkNoMovement` |  | ic_resource |
| วิเคราะห์ข้อมูล › กำไรขั้นต้นตามสินค้า | `menu_ic_info_stk_profit` | ✓ | `SMLERPICInfo._stkProfit` |  |  |
| วิเคราะห์ข้อมูล › กำไรขั้นต้นตามสินค้า (รวมต้นทุนแฝง) | `menu_ic_info_stk_profit_hidden` | ✓ | `SMLERPICInfo._stkProfit` |  |  |
| วิเคราะห์ข้อมูล › กำไรขั้นต้นตามเอกสารขาย | `menu_ic_info_stk_profit_by_doc` | ✓ | `SMLERPICInfo._stkProfit` |  |  |
| วิเคราะห์ข้อมูล › กำไรขั้นต้นตามลูกค้า | `menu_ic_info_stk_profit_by_ar` | ✓ | `SMLERPICInfo._stkProfit` |  |  |
| วิเคราะห์ข้อมูล › สินค้าที่ไม่มีการขาย | `IC_INVENTORY_NO_SALE` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| วิเคราะห์ข้อมูล › ตรวจสอบ Serial มีปัญหา | `menu_ic_serial_analyze` | ✓ | `SMLERPICInfo._icSerialAnalyze` |  | ic_trans_serial_number |
| วิเคราะห์ข้อมูล › รายงานยอดคงเหลือสินค้า (แสดงทุกสินค้า)  แสดงมูลค่าปัจจุบัน | `menu_stock_balance_all_show_current_value` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานสถานะสินค้า | `menu_item_status` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| รายงานสรุป › รายงานบัญชีคุมพิเศษสินค้า | `menu_account_special_item` | ✓ | `SMLERPICReport._report_ic_stk_movement` |  | ic_resource, ic_trans, ic_trans_detail, ic_unit |
| รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_report_ic_product_and_material` | ✓ | `SMLERPICReport._report_ic_product_and_material` |  | ic_resource, ic_trans, ic_trans_detail |
| รายงานสรุป › รายงานการปรับปรุงสินค้า | `menu_report_inventory_adjust` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานประเมินการรับสินค้า | `menu_span_import_item` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงานสรุป › รายงาน Lot สินค้า | `menu_report_lot_inventory` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_item_and_staple` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงานวิเคราะห์ › รายงานเคลื่อนไหว Serial Number | `menu_ic_serial_number` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างส่ง | `menu_ic_report_sale_remain` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสรุปยอดสินค้าค้างรับ | `menu_report_accrued_in_qty` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า | `menu_item_balance` | ✓ | `SMLERPICReport._report_ic_balance` |  | ic_resource, resource_report_ic_column, ic_warehouse, ic_unit |
| รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้าตาม LOT | `menu_item_balance_lot` | ✓ | `SMLERPICReport._report_ic_balance` |  | ic_resource, resource_report_ic_column, ic_warehouse, ic_unit |
| รายงานวิเคราะห์ › รายงานสินค้าที่ถึงจุดสั่งซื้อ | `menu_ic_report_info_stk_reorder` | ✓ | `SMLERPICReport.ic_analysis._report_ic_stk_reorder` |  | ic_resource, ic_trans_detail, ic_trans |
| รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_max` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง | `menu_report_ic_stock_balance_warehouse_min` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_max` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง-จุดเก็บ | `menu_report_ic_stock_balance_location_min` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า ณ ปัจจุบัน(เฉพาะสินค้ามี Serial) | `menu_item_balance_now_only_serial` | ✓ | `SMLERPICReport._report_ic_summary` |  | ic_trans_detail, ic_resource, ic_serial, ic_trans_serial_number |
| รายงานวิเคราะห์ › รายงานสินค้าที่ไม่มีการเคลื่อนไหว | `menu_item_non_transfer` | ✓ | `SMLERPICReport._report_ic_none_movement` |  | ic_resource, ic_trans_detail, ic_trans |
| รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้า | `menu_item_transfer` | ✓ | `SMLERPICReport._report_ic_stk_movement` |  | ic_resource, ic_trans, ic_trans_detail, ic_unit |
| รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า | `menu_result_transfer_item` | ✓ | `SMLERPICReport._report_ic_info_stk_movement_sum` |  | ic_resource, ic_trans_detail, ic_inventory, ic_trans |
| รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า-แสดงมูลค่า | `menu_report_ic_info_stk_movement_sum_show_amount` | ✓ | `SMLERPICReport._report_ic_info_stk_movement_sum_show_amount` |  | ic_resource, ic_trans, ic_trans_detail, ic_inventory |
| รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้าต้นทุนมาตรฐาน | `menu_item_transfer_standard` | ✓ | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้นตามเอกสาร (แสดงส่วนลด) | `menu_ic_report_info_stk_profit_by_doc_and_discount` | ✓ | `SMLERPICReport.ic_analysis._report_info_stk_profit_by_doc_and_discount` |  | ic_resource |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า) | `menu_ic_report_info_stk_profit` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_doc` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า) | `menu_ic_report_info_stk_profit_ic_cust` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_cust_doc` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร) | `menu_ic_report_info_stk_profit_doc` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_doc_ic` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า) | `menu_ic_report_info_stk_profit_cust` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า) | `menu_ic_report_info_stk_profit_cust_ic` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_ic_doc` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_doc` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_cust_doc_ic` | ✓ | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  | ic_resource, ap_supplier |
| คำนวณยอดสต๊อกใหม่ | `menu_ic_recalc` | ✓ | `SMLERPIC._icRecalc` |  | ic_trans_detail, ic_trans, ic_inventory |
| บันทึกรูปภาพเอกสาร | `menu_ic_document_picture` | ✓ | `SMLERPIC._icDocPicture` |  |  |
| จัดการ LOT สินค้า | `menu_ic_lot_manage` |  | `SMLERPIC._icLotManage` |  | ic_lot_manage, ic_resource, ic_inventory |
| รายงานอื่น ๆ | `menu_fastreport_other_ic` | ✓ | tag:fastreportother |  |  |
