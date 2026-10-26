---
tags: [sml, module, warehouse, generated]
menu_group: "คลัง"
trans_flags: [501, 502, 503, 505, 509, 701]
---
# โมดูล: คลัง

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 19 รายการ, จับคู่คลาสได้ 7, เห็นใน SMLAccountPOSProfessional (edition 13) 0
- คลาสหน้าจอที่ใช้บ่อย: `SMLInventoryControl._clone_icTrans` (6), `SMLERPReportTool._reportTrans` (1)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (6)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 501 | คลัง_ยอดคงเหลือสินค้ายกมา | 1 |
| 502 | คลัง_ตรวจนับสินค้า | 2 |
| 503 | คลัง_รับสินค้าเข้า_จากการซื้อ | 1 |
| 505 | คลัง_จ่ายสินค้าออก_จากการขาย | 1 |
| 509 | คลัง_ปรับปรุงเพิ่มลดสินค้า | 1 |
| 701 | สินค้า_บันทึกการจัดส่ง | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans`, `ic_trans_detail`, `cb_trans_detail`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ยอดคงเหลือยกมา (คลัง) | `menu_wh_balance` |  | `SMLInventoryControl._clone_icTrans` | 501 |  |
| รับสินค้าเข้า (คลัง) | `menu_wh_in_purchase` |  | `SMLInventoryControl._clone_icTrans` | 503 |  |
| ส่งคืนสินค้า (คลัง) | `menu_wh_in_ret` |  | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| จ่ายสินค้าออก (คลัง) | `menu_wh_out` |  | `SMLInventoryControl._clone_icTrans` | 505 |  |
| รับคืนสินค้า (คลัง) | `menu_wh_out_ret` |  | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| โอนย้ายสินค้าออก (คลัง) | `menu_wh_trans_out` |  | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| โอนย้ายสินค้าเข้า (คลัง) | `menu_wh_trans_in` |  | tag:ic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ตรวจนับสินค้า (คลัง) | `menu_wh_stk_count` |  | `SMLInventoryControl._clone_icTrans` | 502 |  |
| ปรับปรุงเพิ่มลดสินค้า (คลัง) | `menu_wh_adj` |  | `SMLInventoryControl._clone_icTrans` | 509 |  |
| รายงาน (คลัง) › ยอดคงเหลือยกมา (คลัง) | `menu_wh_report_balance` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › รับสินค้าเข้า (คลัง) | `menu_wh_report_in` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › ส่งคืนสืนค้า (คลัง) | `menu_wh_report_in_ret` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › จ่ายสินค้าออก (คลัง) | `menu_wh_report_out` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › รับคืนสินค้า (คลัง) | `menu_wh_report_out_ret` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › โอนย้ายสินค้าออก (คลัง) | `menu_wh_report_trans_out` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › โอนย้ายสินค้าเข้า (คลัง) | `menu_wh_report_trans_in` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน (คลัง) › รายงานตรวจนับสินค้า (คลัง) | `menu_wh_report_item_count` |  | `SMLERPReportTool._reportTrans` | 502 | ic_trans, ic_trans_detail, cb_trans_detail |
| รายงาน (คลัง) › ปรับปรุงเพิ่มลดสินค้า (คลัง) | `menu_wh_report_adj` |  | tag:reportic (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| บันทึกการส่งสินค้า | `menu_ic_shipping` |  | `SMLInventoryControl._clone_icTrans` | 701 |  |
