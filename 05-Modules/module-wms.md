---
tags: [sml, module, wms, generated]
menu_group: "คลังสินค้า"
trans_flags: [521, 522, 523]
---
# โมดูล: คลังสินค้า

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 16 รายการ, จับคู่คลาสได้ 11, เห็นใน SMLAccountPOSProfessional (edition 13) 2
- คลาสหน้าจอที่ใช้บ่อย: `SMLFastReport._designer` (7), `SMLInventoryControl._clone_icTrans` (3), `SMLPPShipment._shipment` (1)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (3)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 521 | คลัง_รับฝาก_ฝาก | 1 |
| 522 | คลัง_รับฝาก_เบิก | 1 |
| 523 | คลัง_รับฝาก_รับคืนจากเบิก | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`sml_fastreport`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ฝาก / เบิก / รับคืน สินค้า › ฝาก | `menu_wh_deposits` |  | `SMLInventoryControl._clone_icTrans` | 521 |  |
| ฝาก / เบิก / รับคืน สินค้า › เบิก | `menu_wh_issue` |  | `SMLInventoryControl._clone_icTrans` | 522 |  |
| ฝาก / เบิก / รับคืน สินค้า › รับคืน | `menu_wh_issue_return` |  | `SMLInventoryControl._clone_icTrans` | 523 |  |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปฝากรายลูกค้า | `menu_singha_report_wh_deposits_customer` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปสินค้า ค้างส่ง | `menu_singha_report_wh_accrued_out` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปฝาก | `menu_singha_report_summary_warehouse_deposit` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › เบิกฝาก | `menu_singha_report_summary_warehouse_deposit_depart` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปรับคืนฝาก | `menu_singha_report_summary_warehouse_depart_return` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ฝาก / เบิก / รับคืน สินค้า › รายงาน › สรุปการ์ดสินค้า VS สินค้าฝาก | `menu_singha_report_stock_balance_compare_deposit` |  | `SMLFastReport._designer` |  | sml_fastreport |
| ยืม / คืน ภาชนะ › ยอดยกมา ยืม ภาชนะ | `menu_wh_rent_balance` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ยืม / คืน ภาชนะ › เงินมัดจำภาชนะ | `menu_wh_rent_deposits` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ยืม / คืน ภาชนะ › คืนภาชนะ | `menu_wh_rent_return` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ยืม / คืน ภาชนะ › คืนเงินมัดจำภาชนะ | `menu_wh_rent_return_deposit` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ยืม / คืน ภาชนะ › รายงาน | `menu_wh_rent_report` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| การส่งสินค้า › บันทึกการส่งสินค้า | `menu_shipment_load` | 11.1.1 | `SMLPPShipment._shipment` |  |  |
| การส่งสินค้า › รายงานบันทึกการจัดส่ง | `menu_singha_report_shipment` | 11.1.2 | `SMLFastReport._designer` |  | sml_fastreport |
