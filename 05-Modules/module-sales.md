---
tags: [sml, module, sales, generated]
menu_group: "ขาย"
trans_flags: [30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 52, 110, 111, 112, 113]
---
# โมดูล: ขาย

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- เอกสารขายทุกประเภทเปิดด้วย `_icTransControl` ต่างกันที่ `_transControlType` ดู [[document-engine]]
- สายเอกสาร: เสนอราคา (30) → สั่งจอง (34) → สั่งขาย (36) → ขาย (44) → ลดหนี้ (48) / เพิ่มหนี้ (46); ยกเลิกเป็นเอกสารแยก (เช่น 45)
- ขายหน้าจอปกติ `is_pos=0`; บิล POS ดูได้จากเมนูเดียวกันแต่ `is_pos=1` แบบอ่านอย่างเดียว (ยืนยันกับ AOY: 132/649 ใบเป็น POS)
- ขายเงินสดสร้าง `cb_trans`, ขายเชื่อไปตั้งหนี้และรับชำระด้วยเอกสารลูกหนี้ 239 ดู [[data-model]]

## ตัวเลข

- เมนูปลายทาง 75 รายการ, จับคู่คลาสได้ 74, เห็นใน SMLAccountPOSProfessional (edition 13) 74
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPReportTool._reportTrans` (30), `SMLFastReport._designer` (10), `SMLERPSOReport._report_drug_sale_8` (2), `SMLERPSO._soQuotation` (1), `SMLERPSO._soQuotationApproval` (1), `SMLERPSO._soQuotationCancel` (1)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (19), `SMLERPControl._icInfoProcess` (4), `SMLInventoryControl._formSaleOrderPreview` (2), `SMLERPControl._documentPicture` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 30 | ขาย_เสนอราคา | 3 |
| 31 | ขาย_เสนอราคา_ยกเลิก | 2 |
| 32 | ขาย_เสนอราคา_อนุมัติ | 2 |
| 34 | ขาย_สั่งจองและสั่งซื้อสินค้า | 3 |
| 36 | ขาย_สั่งขาย | 3 |
| 37 | ขาย_สั่งขาย_ยกเลิก | 2 |
| 38 | ขาย_สั่งจองและสั่งซื้อสินค้า_อนุมัติ | 2 |
| 39 | ขาย_สั่งจองและสั่งซื้อสินค้า_ยกเลิก | 2 |
| 40 | ขาย_รับเงินล่วงหน้า | 3 |
| 41 | ขาย_รับเงินล่วงหน้า_ยกเลิก | 2 |
| 42 | ขาย_เงินล่วงหน้า_คืน | 1 |
| 43 | ขาย_เงินล่วงหน้า_คืน_ยกเลิก | 2 |
| 44 | ขาย_ขายสินค้าและบริการ | 2 |
| 45 | ขาย_ขายสินค้าและบริการ_ยกเลิก | 2 |
| 46 | ขาย_เพิ่มหนี้ | 2 |
| 47 | ขาย_เพิ่มหนี้_ยกเลิก | 2 |
| 48 | ขาย_รับคืนสินค้าจากการขายและลดหนี้ | 2 |
| 49 | ขาย_รับคืนสินค้าจากการขายและลดหนี้_ยกเลิก | 2 |
| 52 | ขาย_สั่งขาย_อนุมัติ | 2 |
| 110 | ขาย_รับเงินมัดจำ | 3 |
| 111 | ขาย_รับเงินมัดจำ_ยกเลิก | 2 |
| 112 | ขาย_เงินมัดจำ_คืน | 1 |
| 113 | ขาย_เงินมัดจำ_คืน_ยกเลิก | 2 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans`, `ic_trans_detail`, `cb_trans_detail`, `sml_fastreport`, `ic_resource`, `ic_inventory`, `ar_customer`, `ap_supplier`, `cb_trans`, `erp_user`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ใบเสนอราคา | `menu_so_quotation_order` | 4.1 | `SMLERPSO._soQuotation` | 30 |  |
| อนุมัติใบเสนอราคา | `menu_so_quotation_approve` | 4.2 | `SMLERPSO._soQuotationApproval` | 32 |  |
| รายงาน/ยกเลิก › ยกเลิกใบเสนอราคา | `menu_so_quotation_cancel` | 4.3.1 | `SMLERPSO._soQuotationCancel` | 31 |  |
| รายงาน/ยกเลิก › รายงานบันทึกใบเสนอราคา | `menu_so_report_quotation` | 4.3.2 | `SMLERPReportTool._reportTrans` | 30 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอราคา | `menu_so_report_quotation_approve` | 4.3.3 | `SMLERPReportTool._reportTrans` | 32 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอราคา | `menu_so_report_quotation_cancel` | 4.3.4 | `SMLERPReportTool._reportTrans` | 31 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสถานะใบเสนอราคา | `menu_so_report_quotation_stat` | 4.3.5 | `SMLERPReportTool._reportTrans` | 30 | ic_trans, ic_trans_detail, cb_trans_detail |
| ใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order` | 4.4 | `SMLERPSO._soReserved` | 34 |  |
| อนุมัติใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order_approve` | 4.5 | `SMLERPSO._soReservedApproval` | 38 |  |
| รายงาน/ยกเลิก › ยกเลิกใบสั่งซื้อ/สั่งจอง | `menu_so_inquiry_order_cancel` | 4.6.1 | `SMLERPSO._soReservedCancel` | 39 |  |
| รายงาน/ยกเลิก › รายงานใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry` | 4.6.2 | `SMLERPReportTool._reportTrans` | 34 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_approve` | 4.6.3 | `SMLERPReportTool._reportTrans` | 38 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_cancel` | 4.6.4 | `SMLERPReportTool._reportTrans` | 39 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_stat` | 4.6.5 | `SMLERPReportTool._reportTrans` | 34 | ic_trans, ic_trans_detail, cb_trans_detail |
| บันทึกใบสั่งขาย | `menu_so_sale_order` | 4.7 | `SMLERPSO._soSaleorder` | 36 |  |
| อนุมัติใบสั่งขาย | `menu_so_sale_order_approve` | 4.8 | `SMLERPSO._soSaleorderApproval` | 52 |  |
| รายงาน/ยกเลิก › ยกเลิกใบสั่งขาย | `menu_so_sale_order_cancel` | 4.9.1 | `SMLERPSO._soSaleorderCancel` | 37 |  |
| รายงาน/ยกเลิก › รายงานใบสั่งขาย | `menu_so_report_sale_order` | 4.9.2 | `SMLERPReportTool._reportTrans` | 36 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งขาย | `menu_so_report_sale_order_approve` | 4.9.3 | `SMLERPReportTool._reportTrans` | 52 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งขาย | `menu_so_report_sale_order_cancel` | 4.9.4 | `SMLERPReportTool._reportTrans` | 37 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสถานะใบสั่งขาย | `menu_so_report_sale_order_stat` | 4.9.5 | `SMLERPReportTool._reportTrans` | 36 | ic_trans, ic_trans_detail, cb_trans_detail |
| รับเงินล่วงหน้ายกมา | `menu_so_advance_money_balance` | 4.10 | `SMLERPSO._so_advance_money_balance` |  |  |
| รับเงินล่วงหน้า | `menu_so_deposit_receive_1` | 4.11 | `SMLERPSO._so_advance_money` |  |  |
| คืนเงินรับล่วงหน้า | `menu_so_deposit_return_1` | 4.12 | `SMLERPSO._so_advance_money_return` |  |  |
| รายงาน/ยกเลิก › ยกเลิกรับเงินล่วงหน้า | `menu_so_deposit_receive_1_cancel` | 4.13.1 | `SMLERPSO._so_advance_money_cancel` | 41 |  |
| รายงาน/ยกเลิก › ยกเลิกคืนเงินรับล่วงหน้า | `menu_so_deposit_return_1_cancel` | 4.13.2 | `SMLERPSO._so_advance_money_return_cancel` | 43 |  |
| รายงาน/ยกเลิก › รายงานรับเงินล่วงหน้า | `menu_so_report_deposit_receive` | 4.13.3 | `SMLERPReportTool._reportTrans` | 40 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานคืนเงินรับล่วงหน้า | `menu_so_report_deposit_return` | 4.13.4 | `SMLERPReportTool._reportTrans` | 42 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับเงินล่วงหน้า | `menu_so_report_deposit_payment_cancel` | 4.13.5 | `SMLERPReportTool._reportTrans` | 41 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินรับล่วงหน้า | `menu_so_report_deposit_payment_return_cancel` | 4.13.6 | `SMLERPReportTool._reportTrans` | 43 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินรับล่วงหน้า | `menu_so_report_deposit_payment_remain` | 4.13.7 | `SMLERPReportTool._reportTrans` | 40 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการตัดเงินรับล่วงหน้า | `menu_so_report_cut_deposit_payment` | 4.13.8 | `SMLERPReportTool._reportTrans` | 40 | ic_trans, ic_trans_detail, cb_trans_detail |
| รับเงินมัดจำยกมา | `menu_so_deposit_money_balance` | 4.14 | `SMLERPSO._so_deposit_money_balance` |  |  |
| รับเงินมัดจำ | `menu_so_deposit_receive_2` | 4.15 | `SMLERPSO._so_deposit_money` |  |  |
| คืนเงินมัดจำ | `menu_so_deposit_return_2` | 4.16 | `SMLERPSO._so_deposit_money_return` |  |  |
| รายงาน/ยกเลิก › ยกเลิกรับเงินมัดจำ | `menu_so_deposit_receive_2_cancel` | 4.17.1 | `SMLERPSO._so_deposit_money_cancel` | 111 |  |
| รายงาน/ยกเลิก › ยกเลิกคืนเงินมัดจำ | `menu_so_deposit_return_2_cancel` | 4.17.2 | `SMLERPSO._so_deposit_money_return_cancel` | 113 |  |
| รายงาน/ยกเลิก › รายงานรับเงินมัดจำ | `menu_so_report_deposit_receive_2` | 4.17.3 | `SMLERPReportTool._reportTrans` | 110 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานคืนเงินมัดจำ | `menu_so_report_deposit_return_2` | 4.17.4 | `SMLERPReportTool._reportTrans` | 112 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับเงินมัดจำ | `menu_so_report_deposit_payment_cancel_2` | 4.17.5 | `SMLERPReportTool._reportTrans` | 111 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_so_report_deposit_payment_return_cancel_2` | 4.17.6 | `SMLERPReportTool._reportTrans` | 113 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_so_report_deposit_payment_remain_2` | 4.17.7 | `SMLERPReportTool._reportTrans` | 110 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการตัดเงินมัดจำ | `menu_so_report_cut_deposit_payment_2` | 4.17.8 | `SMLERPReportTool._reportTrans` | 110 | ic_trans, ic_trans_detail, cb_trans_detail |
| ขายสินค้า/บริการ | `menu_so_invoice` | 4.18 | `SMLERPSO._soInvoice` | 44 |  |
| รับคืนสินค้า/ลดหนี้ | `menu_so_credit_note` | 4.19 | `SMLERPSO._creditNote` | 48 |  |
| เพิ่มหนี้ | `menu_so_invoice_add` | 4.20 | `SMLERPSO._soInvoiceAdd` | 46 |  |
| ส่งข้อมูล e-Tax | `menu_so_send_etax` | 4.21 | `SMLETaxInvoice._sendETaxControl` |  |  |
| รายงาน/ยกเลิก › ยกเลิกขายสินค้า/บริการ | `menu_so_invoice_cancel` | 4.22.1 | `SMLERPSO._soInvoiceCancel` | 45 |  |
| รายงาน/ยกเลิก › ยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_credit_note_cancel` | 4.22.2 | `SMLERPSO._creditNoteCancel` | 49 |  |
| รายงาน/ยกเลิก › ยกเลิกขายเพิ่มสินค้า/เพิ่มหนี้ | `menu_so_invoice_add_cancel` | 4.22.3 | `SMLERPSO._soInvoiceAddCancel` | 47 |  |
| รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ | `menu_so_report_invoice` | 4.22.4 | `SMLERPReportTool._reportTrans` | 44 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการขายและบริการเรียงตามสินค้า | `menu_so_sale_service_by_item` | 4.22.5 | `SMLERPSOReport._report._report_sale_service_by_item` |  | ic_trans_detail, ar_customer, ap_supplier |
| รายงาน/ยกเลิก › รายงานการรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note` | 4.22.6 | `SMLERPReportTool._reportTrans` | 48 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods` | 4.22.7 | `SMLERPReportTool._reportTrans` | 46 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกขายสินค้าและบริการ | `menu_so_report_invoice_cancel` | 4.22.8 | `SMLERPReportTool._reportTrans` | 45 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note_cancel` | 4.22.9 | `SMLERPReportTool._reportTrans` | 49 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods_cancel` | 4.22.10 | `SMLERPReportTool._reportTrans` | 47 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงานสรุป › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_sell_by_sale` | 4.23.1 | `SMLERPSOReport._report_summary._report_sell_by_sale` |  | ic_trans, ic_trans_detail, cb_trans, erp_user |
| รายงานสรุป › รายงานสรุปยอดขายสินค้าสุทธิตามพนักงานขาย | `menu_fast_report_summary_sell_by_sale` | 4.23.2 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานสรุปยอดขายสินค้า-สรุปตามวันที่ | `menu_shipments_by_date` | 4.23.3 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานประวัติการขายสินค้า | `menu_sale_history_product` | 4.23.4 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.8) | `menu_so_report_sale_drug_by_lot` | 4.23.5 | `SMLERPSOReport._report_drug_sale_8` |  | ic_resource, ic_inventory, ic_trans |
| รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.13) | `menu_so_report_sale_drug_13` | 4.23.6 | `SMLERPSOReport._report_sale_drug_13` |  | ic_inventory, ic_resource |
| รายงานสรุป › บัญชีการผลิตยาและขายยาที่ผลิต (แบบ ผ.ย. ๕) | `menu_so_report_sale_drug_by_lot_5` | 4.23.7 | `SMLERPSOReport._report_drug_sale_8` |  | ic_resource, ic_inventory, ic_trans |
| รายงานสรุป › รายงานเรียกเก็บยาคืน (Recall) | `menu_so_report_sale_recall` | 4.23.8 | `SMLERPSOReport._report_sale_drug_recall` |  | ic_resource, ic_inventory |
| รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบแจกแจง-ตามสินค้า | `menu_fast_report_analysis_sell_ex_by_product` | 4.24.1 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานวิเคราะห์การขายแบบสรุป-ตามเอกสาร | `menu_fast_report_analysis_sell_sum_by_docno` | 4.24.2 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานกำไรขั้นต้นแสดงหักรับคืน | `menu_fast_report_margin_reacceptance` | 4.24.3 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานจัดอันดับยอดขาย-ตามสินค้า | `menu_fast_report_product_rank` | 4.24.4 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานเปรียบเที่ยบยอดสินค้า12 เดือน | `menu_fast_report_shipments_compare_month` | 4.24.5 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานการเทียบการขายกับราคาขาย | `menu_compare_sale_with_price` | 4.24.6 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสินค้าขายต่ำกว่าทุน | `menu_product_sale_loss` | 4.24.7 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานสินค้า ขายประจำเดือน | `menu_report_product_sale_monthly` |  | `IMEXControl.report.report_product_sale_monthly` |  |  |
| บันทึกรูปภาพเอกสาร | `menu_so_doc_picture` | 4.25 | `SMLERPSO._so_docPicture` |  |  |
| รายงานอื่น ๆ | `menu_fastreport_other_sale` | 4.26 | tag:fastreportother |  |  |
