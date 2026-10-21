---
tags: [sml, module, ar, generated]
menu_group: "ลูกหนี้"
trans_flags: [93, 95, 97, 99, 100, 101, 102, 103, 104, 235, 236, 239, 240, 810]
---
# โมดูล: ลูกหนี้

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายละเอียดเชิงลึก: [[write-spec-receipt]], ใบวางบิล [[write-spec-billing-note]]
- เอกสารลูกหนี้เก็บใน `ap_ar_trans` / `ap_ar_trans_detail` (ไม่ใช่ ic_trans): ตั้งหนี้ยกมา 93, ใบวางบิล 235, รับชำระ 239 (ยืนยันกับ AOY)
- หน้าจอกลาง `SMLAPARControl._ar_ap_trans`; หลังบันทึกเรียก `_process_ap_ar_flow` อัปเดตยอดค้างของบิลขาย
- ข้อมูลลูกค้า `ar_customer` / `ar_customer_detail`; วงเงินเครดิตตรวจตอนบันทึกเอกสารขาย

## ตัวเลข

- เมนูปลายทาง 55 รายการ, จับคู่คลาสได้ 53, เห็นใน SMLAccountPOSProfessional (edition 12) 49
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPReportTool._reportTrans` (9), `SMLInventoryControl._clone_icTrans` (6), `SMLERPReportTool._reportArApTrans` (5), `SMLFastReport._designer` (3), `SMLERPAR._ar` (1), `SMLERPAR._ar_detail` (1)
- control หลักที่ฝัง: `SMLERPAPARControl._ar_ap_trans` (8), `SMLInventoryControl._icTransControl` (6), `SMLInventoryControl._formSaleOrderPreview` (2), `SMLERPAPARControl._ar_point_balance` (1), `SMLERPAPARControl._ar_cut_point` (1), `SMLERPControl._documentPicture` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 93 | ลูกหนี้_ตั้งหนี้ยกมา | 2 |
| 95 | ลูกหนี้_เพิ่มหนี้ยกมา | 2 |
| 97 | ลูกหนี้_ลดหนี้ยกมา | 2 |
| 99 | ลูกหนี้_ตั้งหนี้อื่น | 2 |
| 100 | ลูกหนี้_ตั้งหนี้อื่น_ยกเลิก | 2 |
| 101 | ลูกหนี้_เพิ่มหนี้อื่น | 2 |
| 102 | ลูกหนี้_เพิ่มหนี้อื่น_ยกเลิก | 2 |
| 103 | ลูกหนี้_ลดหนี้อื่น | 2 |
| 104 | ลูกหนี้_ลดหนี้อื่น_ยกเลิก | 2 |
| 235 | ลูกหนี้_ใบวางบิล | 2 |
| 236 | ลูกหนี้_ใบวางบิล_ยกเลิก | 2 |
| 239 | ลูกหนี้_รับชำระหนี้ | 3 |
| 240 | ลูกหนี้_รับชำระหนี้_ยกเลิก | 2 |
| 810 | IMEX_Bill_Collector | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans`, `ic_trans_detail`, `cb_trans_detail`, `ap_ar_resource`, `resource_report`, `ap_ar_trans_detail`, `ap_ar_trans`, `ar_customer`, `sml_fastreport`, `ap_ar_transport_label`, `ar_customer_detail`, `ap_supplier_detail`, `ap_supplier`, `formdesign`, `ap_group`, `ar_group`, `ar_customer_connected`, `pos_resource`, `cb_trans`, `ic_inventory`, `cb_petty_cash`, `ic_resource`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ข้อมูลลูกหนี้ › กำหนดลูกหนี้ | `menu_ar_detail` | ✓ | `SMLERPAR._ar` |  |  |
| ข้อมูลลูกหนี้ › รายละเอียดลูกหนี้ | `menu_ar_detail_2` | ✓ | `SMLERPAR._ar_detail` |  |  |
| ข้อมูลลูกหนี้ › รายละเอียดสมาชิก | `menu_ar_dealer` | ✓ | `SMLERPAR._ar_dealer` |  |  |
| ข้อมูลลูกหนี้ › บันทึกเอกสารอ้างอิง | `menu_ar_reference` |  | tag:ar (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ข้อมูลลูกหนี้ › กำหนดแต้มคงเหลือยกมา | `menu_ar_point_balance` | ✓ | `SMLERPAR._ar_point_balance` |  |  |
| ข้อมูลลูกหนี้ › บันทึกตัดแต้ม | `menu_ar_cut_point` | ✓ | `SMLERPAR._ar_cut_point` |  |  |
| ข้อมูลลูกหนี้ › แต้มสะสม | `menu_ar_point` | ✓ | `SMLERPAR.ar_point` |  |  |
| ข้อมูลลูกหนี้ › คำณวนแต้มสะสม | `menu_ar_point_recal` | ✓ | `SMLERPAR.ar_point_recal` |  |  |
| ข้อมูลลูกหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label` | ✓ | `SMLTransportLabel._transport_label` |  | ap_ar_transport_label |
| ข้อมูลลูกหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ar_transport_label_print` | ✓ | `SMLTransportLabel._transport_label_print` |  | ap_ar_transport_label, ap_supplier_detail, ar_customer_detail, ap_supplier |
| ข้อมูลลูกหนี้ › นำเข้าที่อยู่จัดส่งลูกหนี้ | `menu_import_ar_transport_label` | ✓ | `SMLTransportLabel._importTransportLabel` |  |  |
| ข้อมูลลูกหนี้ › ข้อมูลคู่ค้า(ลูกหนี้) | `menu_ar_customer_connected` |  | `SMLERPAR.ar_customer_connected` |  | ar_customer_connected |
| ข้อมูลลูกหนี้ › รายงาน › รายงานรายละเอียดลูกค้า-ตามรหัสลูกค้า | `menu_ar_report_detail_ar` | ✓ | `SMLERPReport.ar._report_ar_detail` |  | ar_customer |
| ข้อมูลลูกหนี้ › รายงาน › รายงานแต้มคงเหลือลูกหนี้ | `menu_report_point_balance` | ✓ | `SMLERPARReport.report._ar_report` |  | pos_resource, ap_ar_resource, resource_report, ic_trans |
| ตั้งหนี้ยกมา (ลูกหนี้) | `menu_ar_debt_balance` | ✓ | `SMLERPAR._ar_debt_balance` | 93 |  |
| เพิ่มหนี้ยกมา (ลูกหนี้) | `menu_ar_increase_debt` | ✓ | `SMLERPAR._ar_increase_debt` | 95 |  |
| ลดหนี้ยกมา (ลูกหนี้) | `menu_ar_cn_balance` | ✓ | `SMLERPAR._ar_cn_balance` | 97 |  |
| รายงาน › รายงานตั้งหนี้ยกมา | `menu_ar_report_early_year_balance_setup` | ✓ | `SMLERPReportTool._reportTrans` | 93 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ar_report_early_year_balance_increase` | ✓ | `SMLERPReportTool._reportTrans` | 95 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน › รายงานลดหนี้ยกมา | `menu_ar_report_early_year_balance_decrease` | ✓ | `SMLERPReportTool._reportTrans` | 97 | ic_trans, ic_trans_detail, cb_trans_detail |
| ตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_debt_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 99 |  |
| เพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_increase_debt_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 101 |  |
| ลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cn_debt_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 103 |  |
| รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_debt_balance_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 100 |  |
| รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_cn_debt_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 104 |  |
| รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (ลูกหนี้) | `menu_ar_cancel_increase_debt_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 102 |  |
| รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_ar_documents_early_year_other` | ✓ | `SMLERPReportTool._reportTrans` | 99 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_report_ar_increase_debt_other` | ✓ | `SMLERPReportTool._reportTrans` | 101 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_ar_reduction_dept_other` | ✓ | `SMLERPReportTool._reportTrans` | 103 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_ar_cancel_documents_early_year_other` | ✓ | `SMLERPReportTool._reportTrans` | 100 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_ar_cancel_increase_debt_other` | ✓ | `SMLERPReportTool._reportTrans` | 102 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_ar_cancel_reduction_dept_other` | ✓ | `SMLERPReportTool._reportTrans` | 104 | ic_trans, ic_trans_detail, cb_trans_detail |
| ใบวางบิล (ลูกหนี้) | `menu_ar_pay_bill` | ✓ | `SMLERPAR._ar_pay_bill` | 235 |  |
| Bill Collector | `menu_imex_bill_collector` |  | `SMLERPAR._ar_bill_collector` | 810 | ar_customer, ap_ar_resource |
| รับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_debt_billing` | ✓ | `SMLERPAR._ar_debt_billing` | 239 |  |
| รายงาน/ยกเลิก › ยกเลิกใบวางบิล (ลูกหนี้) | `menu_ar_cancel_pay_bill` | ✓ | `SMLERPAR._ar_cancel_pay_bill` | 236 |  |
| รายงาน/ยกเลิก › ยกเลิกชำระหนี้/ยกเลิกใบเสร็จรับเงิน | `menu_ar_cancel_debt_billing` | ✓ | `SMLERPAR._ar_cancel_debt_billing` | 240 |  |
| รายงาน/ยกเลิก › รายงานยกเลิกใบวางบิล(ลูกหนี้) | `menu_ar_report_cancel_pay_billing` | ✓ | `SMLERPReportTool._reportArApTrans` | 236 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_cancel_invoice` | ✓ | `SMLERPReportTool._reportArApTrans` | 240 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานใบวางบิล (ลูกหนี้) | `menu_ar_report_billing` | ✓ | `SMLERPReportTool._reportArApTrans` | 235 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานการรับชำระหนี้ประจำวัน | `menu_ar_report_pay_debt_trans` | ✓ | `SMLERPReportTool._reportArApTrans` | 239 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_receipt` | ✓ | `SMLERPReportTool._reportArApTrans` | 239 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียดการรับเงินสด,เงินโอน) | `menu_report_ar_payment_pay_detail` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงายใบเสร็จรับเงินพร้อมรายการย่อย | `menu_ar_report_receipt_and_detail` |  | `SMLERPReport.ar._report_ar_receipt_and_detail` |  | ap_ar_trans, ap_ar_trans_detail |
| รายงาน/ยกเลิก › รายงานใบวางบิลตามพนักงานเก็บเงิน | `menu_report_billing_note_by_customer_cashier` |  | `IMEXControl.report.report_billing_note_by_customer_cashier` |  |  |
| รายงานสรุป › รายงานใบส่งของค้างชำระ-ตามวันที่ | `menu_ar_report_invoice_remain_pay` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานตรวจสอบยอดวงเงิน | `menu_ar_report_check_balance` | ✓ | `SMLERPReport.ar._report_ar_check_balance` |  | ar_customer, ap_ar_resource, ar_customer_detail, cb_petty_cash |
| รายงานสรุป › รายงานสรุป การบันทึก รับเงินจากการขาย/รับชำระหนี้ | `menu_report_receive_money_summary` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานเคลื่อนไหวลูกหนี้ | `menu_ar_report_movement` | ✓ | `SMLERPARAPReport.report._movement` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานอายุลูกหนี้ | `menu_ar_report_period_ar_debt_remain` | ✓ | `SMLERPARAPReport.report._ageing` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานอายุลูกหนี้-ตามเอกสาร | `menu_ar_report_period_ar_debt_remain_by_doc` | ✓ | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานสถานะลูกหนี้ | `menu_ar_report_status_ar` | ✓ | `SMLERPARAPReport.report._absolute_status` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงาน Statement ลูกหนี้ | `menu_report_imex_ar_statement` |  | `IMEXControl.report._reportARStatement` |  | ap_ar_resource, ic_resource |
| บันทึกรูปภาพเอกสาร | `menu_ar_doc_picture` | ✓ | `SMLERPAR._ar_doc_picture` |  |  |
| รายงานอื่น ๆ | `menu_fastreport_other_customer` | ✓ | tag:fastreportother |  |  |
