---
tags: [sml, module, purchase, generated]
menu_group: "ซื้อ"
trans_flags: [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 20, 25, 150, 151, 152, 161, 310, 311, 315, 316, 317, 330, 331, 335, 337]
---
# โมดูล: ซื้อ

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายละเอียดเชิงลึก: [[write-spec-purchase]]
- สายเอกสาร: เสนอซื้อ (2) → อนุมัติ (4) → ใบสั่งซื้อ (6) → อนุมัติ (8) → ซื้อ/รับสินค้า (12) → ส่งคืน/ลดหนี้ (16); มีแบบรับบางส่วน (partial, 310+)
- ใช้ `_icTransControl` เหมือนฝั่งขาย ดู [[document-engine]]
- เอกสารที่เหมาะให้ AI สร้างเป็นร่าง: ใบเสนอซื้อ (2) เพราะยังต้องอนุมัติและไม่กระทบสต็อก

## ตัวเลข

- เมนูปลายทาง 77 รายการ, จับคู่คลาสได้ 75, เห็นใน SMLAccountPOSProfessional (edition 13) 77
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPReportTool._reportTrans` (31), `SMLInventoryControl._clone_icTrans` (26), `SMLFastReport._designer` (10), `SMLERPPO._po_advance_money_balance` (1), `SMLERPPO._po_advance_money` (1), `SMLERPPO._po_advance_money_return` (1)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (26), `SMLInventoryControl._formSaleOrderPreview` (2), `SMLERPControl._documentPicture` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 1 | PoInvestigate | 1 |
| 2 | ซื้อ_เสนอซื้อ | 3 |
| 3 | ซื้อ_เสนอซื้อ_ยกเลิก | 1 |
| 4 | ซื้อ_เสนอซื้อ_อนุมัติ | 2 |
| 6 | ซื้อ_ใบสั่งซื้อ | 4 |
| 7 | ซื้อ_ใบสั่งซื้อ_ยกเลิก | 2 |
| 8 | ซื้อ_ใบสั่งซื้อ_อนุมัติ | 2 |
| 10 | ซื้อ_จ่ายเงินล่วงหน้า | 3 |
| 11 | ซื้อ_จ่ายเงินมัดจำ | 3 |
| 12 | ซื้อ_ซื้อสินค้าและค่าบริการ | 2 |
| 13 | ซื้อ_ซื้อสินค้าและบริการ_ยกเลิก | 2 |
| 14 | ซื้อ_ซื้อสินค้าเพิ่มหนี้หรือราคาผิด | 2 |
| 15 | ซื้อ_ซื้อสินค้าเพิ่มหนี้หรือราคาผิด_ยกเลิก | 2 |
| 16 | ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด | 2 |
| 17 | ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด_ยกเลิก | 2 |
| 20 | ซื้อ_จ่ายเงินล่วงหน้า_รับคืน | 1 |
| 25 | ซื้อ_จ่ายเงินมัดจำ_รับคืน | 1 |
| 150 | ซื้อ_จ่ายเงินล่วงหน้า_ยกเลิก | 2 |
| 151 | ซื้อ_จ่ายเงินมัดจำ_ยกเลิก | 2 |
| 152 | ซื้อ_จ่ายเงินมัดจำ_รับคืน_ยกเลิก | 2 |
| 161 | ซื้อ_จ่ายเงินล่วงหน้า_รับคืน_ยกเลิก | 2 |
| 310 | ซื้อ_พาเชียล_รับสินค้า | 2 |
| 311 | ซื้อ_พาเชียล_ส่งคืนสินค้าหรือราคาผิด | 2 |
| 315 | ซื้อ_พาเชียล_ตั้งหนี้ | 2 |
| 316 | ซื้อ_พาเชียล_เพิ่มหนี้ | 2 |
| 317 | ซื้อ_พาเชียล_ลดหนี้ | 2 |
| 330 | ซื้อ_พาเชียล_รับสินค้า_ยกเลิก | 1 |
| 331 | ซื้อ_พาเชียล_ส่งคืนสินค้าหรือราคาผิด_ยกเลิก | 1 |
| 335 | ซื้อ_พาเชียล_ตั้งหนี้_ยกเลิก | 1 |
| 337 | ซื้อ_พาเชียล_ลดหนี้_ยกเลิก | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans_detail`, `ic_trans`, `cb_trans_detail`, `sml_fastreport`, `ar_customer`, `ap_supplier`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ใบเสนอซื้อ | `menu_purchase_requisition` | 3.1 | `SMLInventoryControl._clone_icTrans` | 2 |  |
| อนุมัติใบเสนอซื้อ | `menu_purchase_requisition_approval` | 3.2 | `SMLInventoryControl._clone_icTrans` | 4 |  |
| รายงาน/ยกเลิก › ยกเลิกใบเสนอซื้อ | `menu_cancel_purchase_requisition` | 3.3.1 | `SMLInventoryControl._clone_icTrans` | 3 |  |
| รายงาน/ยกเลิก › รายงานใบเสนอซื้อ | `menu_po_report_record_requisition_purchase` | 3.3.2 | `SMLERPReportTool._reportTrans` | 2 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอซื้อ | `menu_po_report_requisition_purchase1` | 3.3.3 | `SMLERPReportTool._reportTrans` | 4 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอซื้อ | `menu_po_report_requisition_cancel` | 3.3.4 | tag:poreport (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน/ยกเลิก › รายงานสถานะใบเสนอซื้อ | `menu_po_report_requisition_purchase` | 3.3.5 | `SMLERPReportTool._reportTrans` | 2 | ic_trans, ic_trans_detail, cb_trans_detail |
| ใบสั่งซื้อ | `menu_po_purchase_order` | 3.4 | `SMLInventoryControl._clone_icTrans` | 6 |  |
| อนุมัติใบสั่งซื้อ | `menu_po_purchase_order_approve` | 3.5 | `SMLInventoryControl._clone_icTrans` | 8 |  |
| รายงาน/ยกเลิก › ยกเลิกใบสั่งซื้อ | `menu_po_purchase_order_cancel` | 3.6.1 | `SMLInventoryControl._clone_icTrans` | 7 |  |
| รายงาน/ยกเลิก › รายงานบันทึกใบสั่งซื้อ | `menu_po_report_purchase_order` | 3.6.2 | `SMLERPReportTool._reportTrans` | 6 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ | `menu_po_report_purchase_order_approve` | 3.6.3 | `SMLERPReportTool._reportTrans` | 8 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ | `menu_po_report_purchase_order_cancel` | 3.6.4 | `SMLERPReportTool._reportTrans` | 7 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ | `menu_po_report_purchase_order_status` | 3.6.5 | `SMLERPReportTool._reportTrans` | 6 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานค้างรับสินค้าตามใบสั่งซื้อ | `menu_po_hold_receive_by_doc` | 3.6.6 | `SMLERPReportTool._reportTrans` | 6 | ic_trans, ic_trans_detail, cb_trans_detail |
| จ่ายเงินล่วงหน้ายกมา | `menu_po_advance_payment_balance` | 3.7 | `SMLERPPO._po_advance_money_balance` |  |  |
| จ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1` | 3.8 | `SMLERPPO._po_advance_money` |  |  |
| รับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1` | 3.9 | `SMLERPPO._po_advance_money_return` |  |  |
| รายงาน/ยกเลิก › ยกเลิกจ่ายเงินล่วงหน้า | `menu_po_deposit_payment_1_cancel` | 3.10.1 | `SMLInventoryControl._clone_icTrans` | 150 |  |
| รายงาน/ยกเลิก › ยกเลิกรับคืนจ่ายเงินล่วงหน้า | `menu_po_deposit_return_1_cancel` | 3.10.2 | `SMLInventoryControl._clone_icTrans` | 161 |  |
| รายงาน/ยกเลิก › รายงานบันทึกการจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment` | 3.10.3 | `SMLERPReportTool._reportTrans` | 10 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานบันทึกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return` | 3.10.4 | `SMLERPReportTool._reportTrans` | 20 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_cancel` | 3.10.5 | `SMLERPReportTool._reportTrans` | 150 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return_cancel` | 3.10.6 | `SMLERPReportTool._reportTrans` | 161 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยอดคงเหลือจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_remain` | 3.10.7 | `SMLERPReportTool._reportTrans` | 10 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการตัดจ่ายเงินล่วงหน้า | `menu_po_report_cut_deposit_payment` | 3.10.8 | `SMLERPReportTool._reportTrans` | 10 | ic_trans, ic_trans_detail, cb_trans_detail |
| จ่ายเงินมัดจำยกมา | `menu_po_deposit_money_balance` | 3.11 | `SMLERPPO._po_deposit_money_balance` |  |  |
| จ่ายเงินมัดจำ | `menu_po_deposit_payment_2` | 3.12 | `SMLERPPO._po_deposit_money` |  |  |
| รับคืนจ่ายเงินมัดจำ | `menu_po_deposit_return_2` | 3.13 | `SMLERPPO._po_deposit_money_return` |  |  |
| รายงาน/ยกเลิก › ยกเลิกจ่ายเงินมัดจำ | `menu_po_deposit_payment_2_cancel` | 3.14.1 | `SMLInventoryControl._clone_icTrans` | 151 |  |
| รายงาน/ยกเลิก › ยกเลิกรับคืนจ่ายเงินมัดจำ | `menu_po_deposit_return_2_cancel` | 3.14.2 | `SMLInventoryControl._clone_icTrans` | 152 |  |
| รายงาน/ยกเลิก › รายงานจ่ายเงินมัดจำ | `menu_po_report_advance_payment` | 3.14.3 | `SMLERPReportTool._reportTrans` | 11 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานรับคืนเงินมัดจำ | `menu_po_report_advance_payment_return` | 3.14.4 | `SMLERPReportTool._reportTrans` | 25 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินมัดจำ | `menu_po_report_advance_payment_cancel` | 3.14.5 | `SMLERPReportTool._reportTrans` | 151 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_po_report_advance_payment_return_cancel` | 3.14.6 | `SMLERPReportTool._reportTrans` | 152 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_po_report_deposit_payment_2_remain` | 3.14.7 | `SMLERPReportTool._reportTrans` | 11 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการตัดใบจ่ายเงินมัดจำ | `menu_po_report_cut_deposit_payment_2` | 3.14.8 | `SMLERPReportTool._reportTrans` | 11 | ic_trans, ic_trans_detail, cb_trans_detail |
| ซื้อสินค้า/ตั้งหนี้ | `menu_po_purchase_billing` | 3.15 | `SMLInventoryControl._clone_icTrans` | 12 |  |
| เพิ่มหนี้/ราคาผิด | `menu_po_addition_debt` | 3.16 | `SMLInventoryControl._clone_icTrans` | 14 |  |
| ส่งคืนสินค้า/ราคาผิด | `menu_po_credit_note` | 3.17 | `SMLInventoryControl._clone_icTrans` | 16 |  |
| ซื้อสินค้าแบบทะยอยรับ › รับสินค้า | `menu_po_purchase_partial_item` | 3.18.1 | `SMLInventoryControl._clone_icTrans` | 310 |  |
| ซื้อสินค้าแบบทะยอยรับ › ส่งคืนสินค้า/ราคาผิด | `menu_po_purchase_partial_item_debit` | 3.18.2 | `SMLInventoryControl._clone_icTrans` | 311 |  |
| ซื้อสินค้าแบบทะยอยรับ › ตั้งหนี้จากการรับสินค้า | `menu_po_purchase_partial_1` | 3.18.3 | `SMLInventoryControl._clone_icTrans` | 315 |  |
| ซื้อสินค้าแบบทะยอยรับ › เพิ่มหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_3` | 3.18.4 | `SMLInventoryControl._clone_icTrans` | 316 |  |
| ซื้อสินค้าแบบทะยอยรับ › ลดหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_2` | 3.18.5 | `SMLInventoryControl._clone_icTrans` | 317 |  |
| ซื้อสินค้าแบบทะยอยรับ › ยกเลิกรับสินค้า | `menu_po_purchase_partial_item_cancel` | 3.18.6 | `SMLInventoryControl._clone_icTrans` | 330 |  |
| ซื้อสินค้าแบบทะยอยรับ › ยกเลิกส่งคืนสินค้า/ราคาผิด | `menu_po_purchase_partial_item_debit_cancel` | 3.18.7 | `SMLInventoryControl._clone_icTrans` | 331 |  |
| ซื้อสินค้าแบบทะยอยรับ › ยกเลิกตั้งหนี้จากการรับสินค้า | `menu_po_purchase_partial_1_cancel` | 3.18.8 | `SMLInventoryControl._clone_icTrans` | 335 |  |
| ซื้อสินค้าแบบทะยอยรับ › ยกเลิกลดหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_2_cancel` | 3.18.9 | `SMLInventoryControl._clone_icTrans` | 337 |  |
| ซื้อสินค้าแบบทะยอยรับ › ยกเลิกเพิ่มหนี้จากใบตั้งหนี้ | `menu_po_purchase_partial_3_cancel` | 3.18.10 | `SMLInventoryControl._clone_icTrans` | 1 |  |
| ซื้อสินค้าแบบทะยอยรับ › รายงานรับสินค้า | `menu_po_report_purchase_partial` | 3.18.11 | `SMLERPReportTool._reportTrans` | 310 | ic_trans, ic_trans_detail, cb_trans_detail |
| ซื้อสินค้าแบบทะยอยรับ › รายงานส่งคืนสินค้า/ราคาผิด | `menu_po_report_purchase_partial_debit` | 3.18.12 | `SMLERPReportTool._reportTrans` | 311 | ic_trans, ic_trans_detail, cb_trans_detail |
| ซื้อสินค้าแบบทะยอยรับ › รายงานตั้งหนี้จากการรับสินค้า | `menu_po_report_purchase_partial_1` | 3.18.13 | `SMLERPReportTool._reportTrans` | 315 | ic_trans, ic_trans_detail, cb_trans_detail |
| ซื้อสินค้าแบบทะยอยรับ › รายงานเพิ่มหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_2` | 3.18.14 | `SMLERPReportTool._reportTrans` | 316 | ic_trans, ic_trans_detail, cb_trans_detail |
| ซื้อสินค้าแบบทะยอยรับ › รายงานลดหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_3` | 3.18.15 | `SMLERPReportTool._reportTrans` | 317 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › ยกเลิกซื้อสินค้า | `menu_po_purchase_billing_cancel` | 3.19.1 | `SMLInventoryControl._clone_icTrans` | 13 |  |
| รายงาน/ยกเลิก › ยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel` | 3.19.2 | `SMLInventoryControl._clone_icTrans` | 17 |  |
| รายงาน/ยกเลิก › ยกเลิกซื้อเพิ่มสินค้า/เพิ่มหนี้ | `menu_po_addition_debt_cancel` | 3.19.3 | `SMLInventoryControl._clone_icTrans` | 15 |  |
| รายงาน/ยกเลิก › รายงานการซื้อสินค้า/ตั้งหนี้ | `menu_po_report_purchase` | 3.19.4 | `SMLERPReportTool._reportTrans` | 12 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการส่งคืนสินค้า/ลดหนี้ | `menu_po_report_credit_note` | 3.19.5 | `SMLERPReportTool._reportTrans` | 16 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods` | 3.19.6 | `SMLERPReportTool._reportTrans` | 14 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้า/ตั้งหนี้ | `menu_po_report_purchase_cancel` | 3.19.7 | `SMLERPReportTool._reportTrans` | 13 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel_report` | 3.19.8 | `SMLERPReportTool._reportTrans` | 17 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods_cancel` | 3.19.9 | `SMLERPReportTool._reportTrans` | 15 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงานสรุป › รายงานซื้อสินค้าแยกตามสินค้า | `menu_po_recive_by_item` | 3.20.1 | `SMLERPSOReport._report._report_sale_service_by_item` |  | ic_trans_detail, ar_customer, ap_supplier |
| รายงานสรุป › รายงานยอดซื้อ(ตามวันที่) | `menu_report_purchase_by_date` | 3.20.2 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการซื้อสินค้าสรุปตามประเภทภาษี | `menu_report_sum_purchase_by_vat` | 3.20.3 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบตั้งหนี้จากการซื้อแบบสรุป-ตามวันที่ | `menu_report_purchase_credit_by_date` | 3.20.4 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการสั่งซื้อสินค้าแบบสรุป-ตามวันที่ | `menu_report_purchase_order_by_date` | 3.20.5 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบเพิ่มสินค้า(เจ้าหนี้)แบบสรุป-ตามสินค้า | `menu_report_purchase_add_by_date` | 3.20.6 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการส่งคืนสินค้า/ลดหนี้แบบสรุป-ตามสินค้า | `menu_report_purchase_credit_note_by_item` | 3.20.7 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบซื้อสินค้าที่ถึงกำหนดจ่ายเงิน | `menu_report_purchse_on_due` | 3.20.8 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานการจัดอันดับยอดซื้อ(ตามสินค้า-กลุ่มสินค้า) | `menu_report_purchase_rank_item_group` | 3.21.1 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานวิเคราะห์การซื้อสุทธิ-ตามสินค้า | `menu_po_report_purchase_analyze` | 3.21.2 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานเปรียบเทียบยอดซื้อสินค้า12เดือน(ตามสินค้า-ราคา/ปริมาณ) | `menu_po_report_compare_purchase_monthly` | 3.21.3 | `SMLFastReport._designer` |  | sml_fastreport |
| บันทึกรูปภาพเอกสาร | `menu_po_doc_picture` | 3.22 | `SMLERPPO._po_docPicture` |  |  |
| รายงานอื่น ๆ | `menu_fastreport_other_purchase` | 3.23 | tag:fastreportother |  |  |
