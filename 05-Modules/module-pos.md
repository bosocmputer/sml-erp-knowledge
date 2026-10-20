---
tags: [sml, module, pos, generated]
menu_group: "ขาย POS"
trans_flags: [44, 45, 144]
---
# โมดูล: ขาย POS

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- หน้าจอขายหน้าร้านจริงอยู่ในโปรเจกต์ `SMLPOSClient` (ยังไม่ได้ไล่ละเอียด) ส่วนเมนูนี้เป็นการตั้งค่า/ดูข้อมูล POS
- บิล POS บันทึกเป็น `ic_trans` flag 44 `is_pos=1` (ยืนยันกับ AOY)
- ตั้งค่า POS อยู่ในเมนูเริ่มต้น: ค่าเริ่มต้น POS, รหัสเครื่อง POS, เงื่อนไขสะสมแต้ม

## ตัวเลข

- เมนูปลายทาง 35 รายการ, จับคู่คลาสได้ 34
- คลาสหน้าจอที่ใช้บ่อย: `SMLFastReport._designer` (25), `StreamReader` (1), `SMLERPControl._coupon._couponList` (1), `SMLERPControl._coupon._couponGenerate` (1), `SMLPosClient._posSaveMoneyReceive` (1), `SMLPosClient._posSaveSendMoney` (1)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (3)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 44 | ขาย_ขายสินค้าและบริการ | 1 |
| 45 | ขาย_ขายสินค้าและบริการ_ยกเลิก | 1 |
| 144 | ขาย_ใบกำกับภาษีอย่างเต็มออกแทน | 2 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`sml_fastreport`, `coupon_list`, `cb_trans_detail`, `logs`, `POSCashierSettle`, `ar_customer`, `banknotes`, `POSCashierSettle_detail`, `ic_trans`, `ic_trans_detail`

## เมนูทั้งหมด

| เมนู | menu name | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|
| หน้าจอขาย POS | `menu_pos_screen` | `StreamReader` |  |  |
| รายละเอียดคูปอง | `menu_coupon_list` | `SMLERPControl._coupon._couponList` |  | coupon_list, cb_trans_detail, ar_customer |
| สร้างคูปองแบบเร็ว | `menu_coupon_generate` | `SMLERPControl._coupon._couponGenerate` |  | coupon_list |
| บันทึกรับเงิน (เงินทอน) | `menu_save_pos_receive_money` | `SMLPosClient._posSaveMoneyReceive` |  | logs, POSCashierSettle |
| บันทึกส่งเงิน POS | `menu_save_send_money_pos` | `SMLPosClient._posSaveSendMoney` |  | banknotes, POSCashierSettle, POSCashierSettle_detail, logs |
| รายการใบกำกับภาษีอย่างย่อ | `pos_invoice_list_pos` | `SMLERPSO._soInvoice` | 44 |  |
| รายการใบกำกับภาษีอย่างเต็มออกแทน | `pos_full_invoide_list_pos` | `SMLERPSO._soFullInvoice` | 144 |  |
| รายการใบกำกับภาษีอย่างย่อยกเลิก | `pos_invoice_cancel_pos` | `SMLERPSO._soInvoiceCancel` | 45 |  |
| รายงาน/ยกเลิก › รายงานการรับเงิน | `menu_fastreport_received_money` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานการนำส่งเงินประจำวัน | `report_send_money_pos` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างเต็มออกแทน | `menu_so_report_pos_full_invoice` | `SMLERPReportTool._reportTrans` | 144 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างย่อ | `menu_pos_sum_short_vat` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างย่อยกเลิก | `menu_fastreport_invoice_cancel` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานสรุปการขายหน้าร้าน | `menu_pos_sum_front` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานสรุปใบกำกับภาษีอย่างเต็ม | `menu_pos_sum_full_vat` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามวันที่ | `menu_pos_sale_detail_001` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามลูกค้า | `menu_pos_sale_detail_002` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแคชเชียร์ | `menu_pos_sale_detail_008` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามยี่ห้อสินค้า | `menu_pos_sale_detail_004` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามพนักงาน | `menu_pos_sale_detail_005` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแผนก | `menu_pos_sale_detail_006` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มสินค้า | `menu_pos_sale_detail_009` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามประเภทลูกค้า | `menu_pos_sale_detail_007` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มลูกค้า | `menu_pos_sale_detail_010` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามรหัส | `menu_pos_sale_detail_003` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง › รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรีบงตามรหัส (แสดง Serial) | `menu_report_pos_sale_sugest_by_item_and_serial` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามยี่ห้อสินค้า | `menu_pos_sumary_004` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มลูกค้า | `menu_pos_sumary_009` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามวันที่ | `menu_pos_sumary_002` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มสินค้า | `menu_pos_sumary_008` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-เรียงตามแคชเชียร์ | `menu_pos_sumary_001` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย | `menu_pos_sumary_005` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า | `menu_pos_sumary_003` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามประเภทลูกค้า | `
menu_pos_sumary_007` | `SMLFastReport._designer` |  | sml_fastreport |
| รายงานอื่น ๆ | `menu_fastreport_other_sale_pos` | tag:fastreportother |  |  |
