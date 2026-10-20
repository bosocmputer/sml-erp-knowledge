---
tags: [sml, module, reports, generated]
menu_group: "รายงาน"
trans_flags: []
---
# โมดูล: รายงาน

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายงานใช้เครื่องมือ 3 แบบ: `SMLFastReport._designer` (รายงานที่โหลดตามชื่อเมนู), `SMLERPReportTool._reportTrans` (รายงานเอกสารตาม trans_flag), `SMLReport._report._viewReport`
- ดูรายการรายงานทั้งหมดที่ [[reports]]

## ตัวเลข

- เมนูปลายทาง 71 รายการ, จับคู่คลาสได้ 69
- คลาสหน้าจอที่ใช้บ่อย: `SMLFastReport._designer` (42), `SINGHAReport.GL._glReport` (8), `SINGHAReport._singhareportGenerate` (7), `SINGHAReport.GL._glReportGenerate` (2), `SMLERPGL._report._singhaReportProfitAndLost._report` (2), `SMLERPICReport._icReportSort` (1)
- control หลักที่ฝัง: `SMLERPControl._icInfoProcess` (8)

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`sml_fastreport`, `gl_list_view`, `ic_resource`, `ap_ar_resource`, `resource_report_vat`, `gl_journal_detail`, `ap_supplier`, `gl_chart_of_account`, `ap_supplier_detail`, `ar_customer`, `ar_customer_detail`, `gl_wht_list_detail`, `gl_journal`, `gl_wht_list`, `gl_journal_book`, `erp_branch_list`, `ic_shelf`, `ic_trans`, `ic_trans_detail`, `cb_chq_list`, `cb_trans_detail`, `cb_trans`, `erp_user`, `cb_resource`, `ap_ar_trans`, `gl_journal_vat_sale`, `gl_journal_vat_buy`, `gl_account_group`, `ic_report_sort_item`, `ic_inventory`

## เมนูทั้งหมด

| เมนู | menu name | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|
| ข้อมูลทั่วไป › กำหนดการเรียงข้อมูลรายงาน | `menu_ic_report_sort` | `SMLERPICReport._icReportSort` |  | ic_report_sort_item, ic_inventory |
| ข้อมูลทั่วไป › รายงานการตรวจสอบการแก้ไขข้อมูลย้อนหลัง | `menu_report_singha_logs_trans` | `SMLFastReport._designer` |  | sml_fastreport |
| ข้อมูลทั่วไป › รายงานการยกเลิกเอกสาร | `menu_singha_report_cancel_doc` | `SMLFastReport._designer` |  | sml_fastreport |
| ข้อมูลทั่วไป › รายงานตรวจสอบรายการรายวัน ไม่พบรายละเอียดสาขา | `menu_gl_check_no_bracnch` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › รายการรับสินค้ากรณีอื่นๆ โดยละเอียด | `menu_singha_report_product_receive` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › รับโอนสินค้าสรุปตามคลัง | `menu_singha_report_product_sum_transfer` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › จ่ายโอนสินค้าสรุปตามคลัง | `menu_singha_report_product_sum_transferout` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › รายการจ่ายสินค้ากรณีอื่นๆ โดยละเอียด | `menu_singha_report_product_out_other` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › สรุปยอดจ่ายสินค้าออกจากคลัง | `menu_singha_report_product_sum_out_by_day` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › รายการการโอนสินค้าและวัตถุดิบ | `menu_singha_report_product_transfer` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › รายงานสโตร์ | `menu_singha_report_product_movement_store` | `SMLFastReport._designer` |  | sml_fastreport |
| สินค้า › สรุปการ์ดสินค้า | `menu_singha_report_stock_movement` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| สินค้า › สรุปโหลดสินค้า รายคลัง | `menu_singha_report_load_product_warehouse` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| ซื้อ › สรุปยอดซื้อสินค้า วิเคราะห์ตามผู้ขาย | `menu_singha_report_ap_purchase_summary_product` | `SMLFastReport._designer` |  | sml_fastreport |
| ซื้อ › รายละเอียดเจ้าหนี้ | `menu_singha_report_supplier_detail` | `SMLFastReport._designer` |  | sml_fastreport |
| ซื้อ › การ์ดเจ้าหนี้ | `menu_singha_report_supplier_card` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| ซื้อ › สรุปยอดเงินจ่าย | `menu_singha_report_sum_pay_money` | `SMLFastReport._designer` |  | sml_fastreport |
| ซื้อ › รายงานรับสินค้า แยกสาขา | `menu_singha_report_product_receive_by_branch` | `SMLFastReport._designer` |  | sml_fastreport |
| ซื้อ › รายงานสรุปยอดซื้อจากผู้ขาย วิเคราะห์ตามสินค้า | `menu_singha_report_pu_by_product` | `SMLFastReport._designer` |  | sml_fastreport |
| ซื้อ › ราคาซื้อสินค้าล่าสุด | `menu_singha_report_price_last_buy` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล | `menu_singha_report_sale_invoice` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปยอดขายสินค้า(QTY)ตามช่วงเวลา | `menu_singha_report_sum_sale_qty` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › การ์ดลูกค้า | `menu_singha_report_ar_sale_card` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปยอดเงินรับ | `menu_singha_report_sum_receive_money` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › ยอดขายสินค้า วิเคราะห์ตามลูกค้า (ไม่หักรับคืน) | `menu_singha_report_analyst_sale_customer` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (หักรับคืน) | `menu_singha_report_sale_summary_byproduct` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานขายสินค้าต่ำกว่าทุน | `menu_sing_report_sale_lessthan_cost` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานสรุปยอดขายสินค้าเรียงตามสาขา | `menu_singha_report_sale_by_branch` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานประวัติการขายสินค้า แยกสาขา | `menu_singha_report_sale_history_branch` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_singha_report_sale_summary_by_saleman` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| ขาย › ยอดขายสินค้า วิเคราะห์ตามลูกค้า หักรับคืน | `menu_singha_report_analyst_sale_customer_cut_return` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปยอดการส่งสินค้าตามประเภทการขนส่ง | `menu_singha_report_sum_transport_type` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานสรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า(หักรับคืน) แบบแถวเดียว | `menu_singha_report_sale_summary_byproduct_oneline` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล แสดงหมายเหตุ | `menu_singha_report_sale_invoice_showremark` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานสรุปขาย/แถมรายวัน | `menu_singha_report_sale_premium_by_date` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › ยอดขายสินค้า ตามพื้นที่ | `menu_singha_report_analyst_sale_area` | `SMLFastReport._designer` |  | sml_fastreport |
| ขาย › รายงานยอดขายรายเดือนตามกลุ่มผลิตภัณฑ์/เทียบปี | `menu_report_sale_category_year_compare` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| ขาย › สรุปรายละเอียดการขาย/เก็บเงิน รายบิล ตามระยะเวลาเครดิต | `menu_singha_report_sale_invoice_by_credit_day` | `SMLFastReport._designer` |  | sml_fastreport |
| ลูกหนี้ › ยอดลูกหนี้คงเหลือ | `menu_singha_report_customer_credit_balance` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| ลูกหนี้ › รายงานตรวจสอบยอดวงเงิน | `menu_singha_report_credit_money_check` | `SMLFastReport._designer` |  | sml_fastreport |
| ลูกหนี้ › ลูกหนี้คงค้าง | `menu_singha_report_ar_outstanding` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| ลูกหนี้ › รายงานที่อยู่จัดส่งลูกค้า | `menu_singha_report_transport_address` | `SMLFastReport._designer` |  | sml_fastreport |
| ลูกหนี้ › ยอดลูกหนี้คงเหลือ ตามระยะเวลาเครดิต | `menu_singha_report_customer_credit_balance_by_creditdate` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| เงินสด/ธนาคาร › เช็ครับ › ทะเบียนรับเช็ค | `menu_singha_report_chequein_list` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › เช็ครับ › สรุปยอดรับเช็คคงเหลือ | `menu_singha_report_chequein_balance` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › เช็ครับ › สรุปยอดรับเช็ค  ส่งเข้าธนาคาร | `menu_singha_report_chequein_deposit` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › เช็ครับ › สรุปเช็ครับล่วงหน้า (ผ่าน) | `menu_singha_report_chequein_pass` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › เช็ครับ › รายงานการตัดเช็ค | `report_singha_chq_receive_movement` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| เงินสด/ธนาคาร › เช็ครับ › รายงานรับคืน (เช็ครับ) | `menu_singha_report_chq_in_return` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › รายงาน Bank Statement | `menu_singha_report_bank_statement` | `SINGHAReport._singhareportGenerate` |  | ic_trans, ap_ar_resource, ic_trans_detail, cb_chq_list |
| เงินสด/ธนาคาร › รายงาน Bank Statement แสดงช่องทางการจ่ายเงิน | `menu_singha_report_bank_statement_show_payment_detail` | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/ธนาคาร › รายงานค่าใช้จ่ายอื่น ๆ | `menu_singha_report_other_expenses` | `SMLFastReport._designer` |  | sml_fastreport |
| บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.3) | `menu_singha_report_product_wht_3` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.53) | `menu_singha_report_product_wht_53` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| บัญชี › รายงานภาษีซื้อ | `menu_singha_report_vat_buy` | `SINGHAReport.GL._glReportGenerate` |  | gl_journal_vat_sale, gl_journal_vat_buy, ap_supplier_detail, ar_customer_detail |
| บัญชี › รายงานภาษีขาย | `menu_singha_report_vat_sale` | `SINGHAReport.GL._glReportGenerate` |  | gl_journal_vat_sale, gl_journal_vat_buy, ap_supplier_detail, ar_customer_detail |
| บัญชี › สมุดบัญชีแยกประเภทเงินสด | `menu_report_cash_gl_sheet` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| บัญชี › สมุดบัญชีแยกประเงินโอน | `menu_report_transfer_gl_sheet` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| บัญชี › รายงานข้อมูลรายวัน | `menu_singha_report_journal` | `SINGHAReport.GL._glReport` |  | resource_report_vat, ic_resource, gl_wht_list_detail, gl_list_view |
| บัญชี › รายงานภาษีขายสินค้าฟรี(ใบควบคุม) | `menu_singha_report_vat_free_by_issue` | `SMLFastReport._designer` |  | sml_fastreport |
| บัญชี › งบกำไรขาดทุน | `menu_singha_report_profit_and_lost` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  | gl_chart_of_account, gl_journal_detail, gl_list_view, gl_account_group |
| บัญชี › งบดุล | `menu_singha_report_balancesheet_asset` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  | gl_chart_of_account, gl_journal_detail, gl_list_view, gl_account_group |
| บัญชี › งบดุลเปรียบเทียบ | `menu_singha_report_balancesheet_compare` | fallback:_g._selectMenu (no case found) |  |  |
| บัญชี › งบกำไร(ขาดทุน)เปรียบเทียบ | `menu_singha_report_lost_profit_compare` | fallback:_g._selectMenu (no case found) |  |  |
| บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (มาตรฐาน) | `menu_gl_report_trial_balance` | `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` |  |  |
| บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกแผนก) | `menu_gl_report_trial_balance_depart` | `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` |  | gl_list_view |
| บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกสาขา) | `menu_gl_report_trial_balance_branch` | `SMLERPGL._report._trialBalanceBranch._report` |  | gl_list_view |
| บัญชี › รายงานกระดาษทำการ | `menu_gl_report_balance_sheet` | `SMLERPGL._report._workSheet._report` |  | gl_list_view |
| บัญชี › รายงานอื่น ๆ › งบกระแสเงินสด | `menu_gl_report_other_1` | `SMLERPGL._report._other_1._report` |  | gl_list_view |
| บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา) | `menu_gl_report_profit_and_lost_branch_1` | `SMLERPGL._report._profitAndLostBranch._report` |  | gl_list_view |
| บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา-แผนก) | `menu_gl_report_trial_balance_branch_depart` | `SMLERPGL._report._trialBalanceBranchDepart._report` |  | gl_list_view |
