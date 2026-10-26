---
tags: [sml, module, data, generated]
menu_group: "Data"
trans_flags: []
---
# โมดูล: Data

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 7 รายการ, จับคู่คลาสได้ 7, เห็นใน SMLAccountPOSProfessional (edition 13) 0
- คลาสหน้าจอที่ใช้บ่อย: `SINGHAReport._singhaDataSyncControl` (3), `SMLERPTransferControl._saleImportFromStockCountDiff` (1), `SMLERPTransferControl._saleImportFromPOSSaleReport` (1), `SMLERPTransferControl._salesItemsFromPurchaseBill` (1), `SMLERPAPARControl._importDebtBilling` (1)
- control หลักที่ฝัง: `SMLERPAPARControl._ar_ap_trans_screen_top` (1), `SMLERPAPARControl._importDebtGridControl` (1)

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`resource_report`, `ic_trans_detail`, `ic_trans`, `ic_inventory`, `ic_unit`, `ap_ar_trans_detail`, `erp_doc_format`, `ic_trans_resource`, `erp_income_list`, `erp_expenses_list`, `ap_ar_trans`

## เมนูทั้งหมด

| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| Data ARM | `menu_sync_data_arm` |  | `SINGHAReport._singhaDataSyncControl` |  | resource_report |
| Data Saleout | `menu_sync_data_saleout` |  | `SINGHAReport._singhaDataSyncControl` |  | resource_report |
| Data Stock | `menu_sync_data_stock` |  | `SINGHAReport._singhaDataSyncControl` |  | resource_report |
| สร้างการขายจากผลต่างจากการตรวจนับ | `menu_import_sale_from_stock_count_diff` |  | `SMLERPTransferControl._saleImportFromStockCountDiff` |  |  |
| สร้างรายการขายจากสรุปการขาย POS | `menu_imort_sale_from_pos_sale_report` |  | `SMLERPTransferControl._saleImportFromPOSSaleReport` |  | ic_trans_detail |
| สร้างรายการขายจาก บิลซื้อ | `menu_imort_sale_from_purchase_bill` |  | `SMLERPTransferControl._salesItemsFromPurchaseBill` |  | ic_trans_detail, ic_inventory, ic_unit, ic_trans |
| Import File Cash Received Account Receivable | `menu_debt_import` |  | `SMLERPAPARControl._importDebtBilling` |  | ap_ar_trans_detail, ic_trans, ic_trans_detail, erp_doc_format |
