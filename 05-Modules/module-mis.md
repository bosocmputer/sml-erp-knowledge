---
tags: [sml, module, mis, generated]
menu_group: "MIS"
trans_flags: []
---
# โมดูล: MIS

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 9 รายการ, จับคู่คลาสได้ 5
- คลาสหน้าจอที่ใช้บ่อย: `SMLMIS.calendar_trans` (1), `SMLERPSO._saleInformation` (1), `SMLERPICInfo._ic_inventory_information` (1), `SMLERPICInfo._ic_inventory_information_2` (1), `SMLERPPO._buyInformation` (1)
- control หลักที่ฝัง: `SMLERPAPARControl._ap_ar_billForm` (1), `SMLERPControl._icInfoProcess` (1), `SMLERPControl._icmainScreenTopControl` (1), `SMLERPControl._getPicture` (1), `SMLInventoryControl._icPriceFormulaGrid` (1)

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_resource`, `resource_report`, `ic_trans_detail`, `ic_unit_use`, `ic_inventory`, `ic_unit`, `ic_inventory_price_formula`, `ar_customer`, `ic_serial`, `ic_inventory_barcode`, `ic_cost_date`, `ic_dimension`, `ic_specific_search_word`, `ic_specific_search`, `ic_dimension_name`, `erp_doc_format`, `ic_inventory_detail`, `ic_wh_shelf`, `ap_supplier`

## เมนูทั้งหมด

| เมนู | menu name | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|
| จำนวนรายการรายวัน | `menu_mis_calendar_trans` | `SMLMIS.calendar_trans` |  |  |
| Sale  Information | `menu_sale_information` | `SMLERPSO._saleInformation` |  | resource_report, ar_customer, ic_trans_detail, ic_resource |
| Inventory Information | `menu_ic_information` | `SMLERPICInfo._ic_inventory_information` |  | ic_resource, ic_unit_use, ic_inventory, ic_serial |
| หน้าจอสำหรับผู้บริหาร | `menu_ic_information_manager` | `SMLERPICInfo._ic_inventory_information_2` |  | ic_inventory, ic_cost_date, ic_inventory_price_formula, ic_unit_use |
| Buy Information | `menu_buy_information` | `SMLERPPO._buyInformation` |  | resource_report, ap_supplier, ic_trans_detail, ic_resource |
| บันทึกค่าส่งเสริมการขาย | `menu_sales_commission` | fallback:_g._selectMenu (no case found) |  |  |
| รายละเอียดการจัดส่ง | `menu_ic_sale_shipment` | fallback:_g._selectMenu (no case found) |  |  |
| บันทึกจัดสินค้า | `menu_packing` | fallback:_g._selectMenu (no case found) |  |  |
| บันทึกการส่งสินค้า | `menu_shipment_confirm` | fallback:_g._selectMenu (no case found) |  |  |
