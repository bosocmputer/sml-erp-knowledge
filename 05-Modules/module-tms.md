---
tags: [sml, module, tms, generated]
menu_group: "Mobillyst TMS"
trans_flags: []
---
# โมดูล: Mobillyst TMS

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 5 รายการ, จับคู่คลาสได้ 5, เห็นใน SMLAccountPOSProfessional (edition 12) 5
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPSO.mobillyst_tms._create_delivery_order` (1), `SMLERPSO.mobillyst_tms._create_cn_delivery_order` (1), `SMLERPSO.mobillyst_tms._create_transfer_delivery_order` (1), `SMLERPSO.mobillyst_tms._create_po_delivery_order` (1), `SMLERPSO.mobillyst_tms._delivery_order_list` (1)
- control หลักที่ฝัง: -

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`erp_delivery_order_item`, `ic_trans`, `erp_delivery_order`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| สร้างคำสั่งส่งสินค้า | `menu_mobillyst_create_delivery_order` | ✓ | `SMLERPSO.mobillyst_tms._create_delivery_order` |  | ic_trans, erp_delivery_order_item |
| สร้างคำสั่งส่ง-จากการรับคืนสินค้า | `menu_mobillyst_create_cn_delivery_order` | ✓ | `SMLERPSO.mobillyst_tms._create_cn_delivery_order` |  |  |
| สร้างคำสั่งส่ง-จากการโอนสินค้า | `menu_mobillyst_create_tr_delivery_order` | ✓ | `SMLERPSO.mobillyst_tms._create_transfer_delivery_order` |  |  |
| สร้างคำสั่งส่ง-จากการสั่งซื้อสินค้า | `menu_mobillyst_create_po_delivery_order` | ✓ | `SMLERPSO.mobillyst_tms._create_po_delivery_order` |  |  |
| รายการสั่งส่งสินค้า | `menu_mobillyst_delivery_order_list` | ✓ | `SMLERPSO.mobillyst_tms._delivery_order_list` |  | erp_delivery_order, erp_delivery_order_item |
