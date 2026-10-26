---
tags: [sml, module, ap, generated]
menu_group: "เจ้าหนี้"
trans_flags: [19, 23, 81, 83, 85, 87, 88, 89, 90, 91, 92, 213, 214]
---
# โมดูล: เจ้าหนี้

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายละเอียดเชิงลึก: [[write-spec-ap-payment]]
- เอกสารเจ้าหนี้เก็บใน `ap_ar_trans`: ตั้งหนี้ยกมา 81, รับวางบิล 213, จ่ายชำระ 19 (ยืนยันกับ AOY)
- หน้าจอกลาง `SMLAPARControl._ar_ap_trans` (เดียวกับลูกหนี้)

## ตัวเลข

- เมนูปลายทาง 54 รายการ, จับคู่คลาสได้ 51, เห็นใน SMLAccountPOSProfessional (edition 13) 50
- คลาสหน้าจอที่ใช้บ่อย: `SMLFastReport._designer` (10), `SMLERPReportTool._reportTrans` (9), `SMLInventoryControl._clone_icTrans` (6), `SMLERPReportTool._reportArApTrans` (4), `SMLERPAP._ap` (1), `SMLERPAP._ap_detail` (1)
- control หลักที่ฝัง: `SMLERPAPARControl._ar_ap_trans` (7), `SMLInventoryControl._icTransControl` (6), `SMLInventoryControl._icTransScreenTopControl` (3), `SMLInventoryControl._formSaleOrderPreview` (2), `SMLERPControl._documentPicture` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 19 | เจ้าหนี้_จ่ายชำระหนี้ | 2 |
| 23 | เจ้าหนี้_จ่ายชำระหนี้_ยกเลิก | 2 |
| 81 | เจ้าหนี้_ตั้งหนี้ยกมา | 2 |
| 83 | เจ้าหนี้_เพิ่มหนี้ยกมา | 2 |
| 85 | เจ้าหนี้_ลดหนี้ยกมา | 2 |
| 87 | เจ้าหนี้_ตั้งหนี้อื่น | 2 |
| 88 | เจ้าหนี้_ตั้งหนี้อื่น_ยกเลิก | 2 |
| 89 | เจ้าหนี้_เพิ่มหนี้อื่น | 2 |
| 90 | เจ้าหนี้_เพิ่มหนี้อื่น_ยกเลิก | 2 |
| 91 | เจ้าหนี้_ลดหนี้อื่น | 2 |
| 92 | เจ้าหนี้_ลดหนี้อื่น_ยกเลิก | 2 |
| 213 | เจ้าหนี้_ใบรับวางบิล | 2 |
| 214 | เจ้าหนี้_ใบรับวางบิล_ยกเลิก | 2 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans`, `sml_fastreport`, `ic_trans_detail`, `cb_trans_detail`, `ap_supplier_connected`, `ap_ar_trans_detail`, `ap_ar_trans`, `resource_report`, `ap_ar_resource`, `ap_supplier`, `erp_doc_format`, `ic_warehouse`, `ic_shelf`, `ap_ar_transport_label`, `ap_supplier_detail`, `ar_customer`, `ar_customer_detail`, `formdesign`, `ap_group`, `ar_group`, `erp_company_profile`, `ic_trans_serial_number`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ข้อมูลเจ้าหนี้ › กำหนดเจ้าหนี้ | `menu_ap_detail` | 6.1.1 | `SMLERPAP._ap` |  |  |
| ข้อมูลเจ้าหนี้ › รายละเอียดเจ้าหนี้ | `menu_ap_detail_2` | 6.1.2 | `SMLERPAP._ap_detail` |  |  |
| ข้อมูลเจ้าหนี้ › บันทึกเอกสารอ้างอิง | `menu_ap_reference` |  | tag:ap (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ข้อมูลเจ้าหนี้ › ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label` | 6.1.3 | `SMLTransportLabel._transport_label` |  | ap_ar_transport_label |
| ข้อมูลเจ้าหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า | `menu_ap_transport_label_print` | 6.1.4 | `SMLTransportLabel._transport_label_print` |  | ap_ar_transport_label, ap_supplier_detail, ar_customer_detail, ap_supplier |
| ข้อมูลเจ้าหนี้ › นำเข้าที่อยู่จัดส่งเจ้าหนี้ | `menu_import_ap_transport_label` | 6.1.5 | `SMLTransportLabel._importTransportLabel` |  |  |
| ข้อมูลเจ้าหนี้ › รายงานรายละเอียดเจ้าหนี้ | `menu_ap_report_detail_ap` | 6.1.6 | `SMLERPReportTool._reportCustMaster` |  | ar_customer, ap_supplier, ic_trans |
| ตั้งหนี้ยกมา (เจ้าหนี้) | `menu_ap_debt_balance` | 6.2 | `SMLERPAP._ap_debt_balance` | 81 |  |
| ลดหนี้ยกมา (เจ้าหนี้) | `menu_ap_cn_balance` | 6.3 | `SMLERPAP._ap_cn_balance` | 85 |  |
| เพิ่มหนี้ยกมา (เจ้าหนี้) | `menu_ap_increase_debt` | 6.4 | `SMLERPAP._ap_increase_debt` | 83 |  |
| รายงาน › รายงานตั้งหนี้ยกมา | `menu_ap_report_early_year_balance_setup` | 6.5.1 | `SMLERPReportTool._reportTrans` | 81 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน › รายงานลดหนี้ยกมา | `menu_ap_report_early_year_balance_decrease` | 6.5.2 | `SMLERPReportTool._reportTrans` | 85 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ap_report_early_year_balance_increase` | 6.5.3 | `SMLERPReportTool._reportTrans` | 83 | ic_trans, ic_trans_detail, cb_trans_detail |
| คู่ค้า › ข้อมูลคู่ค้า | `menu_ap_partner_detail` | 6.6.1 | `SMLERPAP.ap_supplier_connected` |  | ap_supplier_detail, ap_supplier, ap_supplier_connected |
| คู่ค้า › นำเข้าข้อมูลจากคู่ค้า | `menu_ap_partner_import` |  | `SMLERPAP._apPartnerBillImport` |  | ic_trans, erp_company_profile, erp_doc_format, ic_trans_serial_number |
| คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) | `menu_ap_partner_import_return_product` |  | `SMLERPAP._apPartnerBillImportReturnProduct` |  | ic_trans, erp_doc_format, ic_warehouse, ic_shelf |
| คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้) | `menu_ap_partner_import_add_debt` |  | `SMLERPAP._apPartnerBillImportAddDebt` |  | ic_trans, erp_doc_format, ic_warehouse, ic_shelf |
| ตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_debt_other` | 6.7 | `SMLInventoryControl._clone_icTrans` | 87 |  |
| ลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cn_debt_other` | 6.8 | `SMLInventoryControl._clone_icTrans` | 91 |  |
| เพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_increase_debt_other` | 6.9 | `SMLInventoryControl._clone_icTrans` | 89 |  |
| รายงาน/ยกเลิก › ยกเลิกตั้งหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_debt_balance_other` | 6.10.1 | `SMLInventoryControl._clone_icTrans` | 88 |  |
| รายงาน/ยกเลิก › ยกเลิกลดหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_cn_debt_other` | 6.10.2 | `SMLInventoryControl._clone_icTrans` | 92 |  |
| รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้อื่นๆ (เจ้าหนี้) | `menu_ap_cancel_increase_debt_other` | 6.10.3 | `SMLInventoryControl._clone_icTrans` | 90 |  |
| รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_documents_early_year_other` | 6.10.4 | `SMLERPReportTool._reportTrans` | 87 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_increase_debt_other` | 6.10.5 | `SMLERPReportTool._reportTrans` | 89 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_reduction_dept_other` | 6.10.6 | `SMLERPReportTool._reportTrans` | 91 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_cancel_documents_early_year_other` | 6.10.7 | `SMLERPReportTool._reportTrans` | 88 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_cancel_increase_debt_other` | 6.10.8 | `SMLERPReportTool._reportTrans` | 90 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_cancel_reduction_dept_other` | 6.10.9 | `SMLERPReportTool._reportTrans` | 92 | ic_trans, ic_trans_detail, cb_trans_detail |
| ใบรับวางบิล (เจ้าหนี้) | `menu_ap_pay_bill` | 6.11 | `SMLERPAP._ap_pay_bill` | 213 |  |
| จ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_debt_billing` | 6.12 | `SMLERPAP._ap_debt_billing` | 19 |  |
| รายงาน/ยกเลิก › ยกเลิกใบรับวางบิล (เจ้าหนี้) | `menu_ap_cancel_pay_bill` | 6.13.1 | `SMLERPAP._ap_cancel_pay_bill` | 214 |  |
| รายงาน/ยกเลิก › ยกเลิกจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_cancel_debt_billing` | 6.13.2 | `SMLERPAP._ap_cancel_debt_billing` | 23 |  |
| รายงาน/ยกเลิก › รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) | `menu_ap_report_cancel_pay_bill` | 6.13.3 | `SMLERPReportTool._reportArApTrans` | 214 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) | `menu_ap_report_cancel_debt_billing` | 6.13.4 | `SMLERPReportTool._reportArApTrans` | 23 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานใบรับวางบิล (เจ้าหนี้) | `menu_ap_report_billing` | 6.13.5 | `SMLERPReportTool._reportArApTrans` | 213 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้า-ตามใบส่งของ | `menu_billing_value_by_invoice` | 6.13.6 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานใบรับวางบิลค่าสินค้าที่คงค้าง | `menu_billing_outstanding` | 6.13.7 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานการจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_report_payment` | 6.13.8 | `SMLERPReportTool._reportArApTrans` | 19 | ap_ar_trans_detail, ap_ar_trans, resource_report, ic_trans |
| รายงานสรุป › รายงานใบส่งของค้างจ่ายชำระ-ตามวันที่ | `menu_invoice_arrears_by_date` | 6.14.1 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบส่งของถึงกำหนดชำระ-ตามวันที่ | `menu_invoice_due_by_date` | 6.14.2 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบส่งของค้างชำระแสดงวันที่ถึงกำหนด | `menu_invoice_arrears_due` | 6.14.3 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานใบส่งของเกินกำหนดชำระ-ตามวันที่ | `menu_invoice_overdue_by_date` | 6.14.4 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานจ่ายชำระค่าสินค้า-ตามใบส่งของ | `menu_payment_by_invoice` | 6.14.5 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการจ่ายชำระประจำวัน-ตามวันที่ | `menu_payment_by_date` | 6.14.6 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานสรุป › รายงานการจ่ายเงินประจำวัน-ตามแผนก | `menu_payment_by_department` | 6.14.7 | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานวิเคราะห์ › รายงานเคลื่อนไหวเจ้าหนี้ | `menu_ap_report_payable_movement` | 6.15.1 | `SMLERPARAPReport.report._movement` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้ | `menu_ap_report_payable_aging` | 6.15.2 | `SMLERPARAPReport.report._ageing` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้-ตามเอกสาร | `menu_ap_report_payable_aging_by_doc` | 6.15.3 | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานสถานะเจ้าหนี้ | `menu_ap_report_payable_status` | 6.15.4 | `SMLERPARAPReport.report._absolute_status` |  | ap_ar_resource |
| รายงานวิเคราะห์ › รายงานเจ้าหนี้ที่ไม่มีการเคลื่อนไหว | `menu_ap_report_payable_not_movement` | 6.15.5 | tag:apreport (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงานวิเคราะห์ › รายงานใบตั้งหนี้จากการซื้อแบบแจกแจงตามเจ้าหนี้ | `menu_ap_detail_debt_by_ap` | 6.15.6 | `SMLFastReport._designer` |  | sml_fastreport |
| บันทึกรูปภาพเอกสาร | `menu_ap_doc_picture` | 6.16 | `SMLERPAP._ap_doc_picture` |  |  |
| รายงานอื่น ๆ | `menu_fastreport_other_supplier` | 6.17 | tag:fastreportother |  |  |
