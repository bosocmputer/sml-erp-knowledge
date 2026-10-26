---
tags: [sml, module, asset, generated]
menu_group: "ค่าเสื่อม"
trans_flags: [2]
---
# โมดูล: ค่าเสื่อม

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 12 รายการ, จับคู่คลาสได้ 11, เห็นใน SMLAccountPOSProfessional (edition 13) 12
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPASSET._as_list` (1), `SMLERPASSET._as_list_pic` (1), `SMLERPASSET._as_maintain` (1), `SMLERPSO._saleAssets` (1), `SMLERPASSET._display._depreciateByDay` (1), `SMLERPASSET._display._depreciateByMonth` (1)
- control หลักที่ฝัง: `SMLERPControl._getPicture` (1), `SMLERPGLControl._glDetail` (1), `SMLERPGLControl._journalScreen` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 2 | ซื้อ_เสนอซื้อ | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`as_asset`, `as_asset_detail`, `erp_department_list`, `as_asset_maintenance_detail`, `as_asset_type`, `as_asset_location`, `erp_doc_format`, `as_trans_detail`, `ic_unit`, `erp_side_list`, `erp_branch_list`, `as_resource`, `gl_chart_of_account`, `as_asset_sale_detail`, `as_asset_result`, `erp_user`, `erp_province`, `as_asset_maintenance`, `as_trans`, `gl_journal`, `gl_journal_detail`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| รายละเอียดสินทรัพย์ › ข้อมูลสินทรัพย์ | `menu_asset_lists` | 9.1.1 | `SMLERPASSET._as_list` |  | as_asset, as_asset_detail, gl_chart_of_account, as_asset_sale_detail |
| รายละเอียดสินทรัพย์ › กำหนดรูปภาพ | `menu_asset_picture` | 9.1.2 | `SMLERPASSET._as_list_pic` |  | as_asset |
| บันทึกการซ่อมบำรุงสินทรัพย์ | `menu_asset_maintenance` | 9.2 | `SMLERPASSET._as_maintain` |  | as_asset_maintenance_detail, as_asset_maintenance, erp_branch_list, erp_side_list |
| บันทึกการขายสินทรัพย์ | `menu_asset_sale` | 9.3 | `SMLERPSO._saleAssets` | 2 |  |
| แสดงค่าเสื่อมราคาสินทรัพย์รายวัน | `menu_show_asset_byday` | 9.4 | `SMLERPASSET._display._depreciateByDay` |  | as_resource, as_asset_detail |
| แสดงค่าเสื่อมราคาสินทรัพย์รายเดือน | `menu_show_asset_bymonth` | 9.5 | `SMLERPASSET._display._depreciateByMonth` |  | as_asset_detail |
| แสดงค่าเสื่อมราคาสินทรัพย์รายปี | `menu_show_asset_byyear` | 9.6 | `SMLERPASSET._display._depreciateByYear` |  | as_asset_detail |
| โอนข้อมูลเข้าระบบบัญชี | `menu_asset_transfers` | 9.7 | `SMLERPASSET._as_transfer` |  | as_trans, as_asset, as_trans_detail, gl_journal |
| รายงาน › รายงานรายละเอียดสินทรัพย์ | `menu_asset_report_list` | 9.8.1 | `SMLERPASSET._report._asset._report` |  | as_asset_detail, as_asset, erp_department_list, as_asset_type |
| รายงาน › รายงานค่าเสื่อมราคาสินทรัพย์ | `menu_asset_report_depreciate` | 9.8.2 | `SMLERPASSET._report._depreciate._report` |  | as_asset, as_resource, erp_department_list, as_asset_type |
| รายงาน › รายงานการซ่อมบำรุงสินทรัพย์ | `menu_asset_report_maintain` | 9.8.3 | `SMLERPASSET._report._maintain._report` |  | as_asset_maintenance_detail, as_asset |
| รายงานอื่น ๆ | `menu_fastreport_other_asset` | 9.9 | tag:fastreportother |  |  |
