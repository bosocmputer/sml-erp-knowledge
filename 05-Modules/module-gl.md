---
tags: [sml, module, gl, generated]
menu_group: "บัญชี"
trans_flags: [1998, 1999]
---
# โมดูล: บัญชี

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- สมุดรายวัน `gl_journal` / `gl_journal_detail`, ผังบัญชี `gl_chart_of_account`, ภาษี `gl_journal_vat_buy` / `_sale`
- GL ส่วนใหญ่สร้างอัตโนมัติจากเอกสาร (`_processGLByTrans`) เมื่อเปิด `gl_process_realtime`; หน้าจอบันทึกมือ `SMLERPGLControl._journalScreen`
- AOY: 176 จาก 188 รายการ GL ผูก doc_no กับ ic_trans

## ตัวเลข

- เมนูปลายทาง 66 รายการ, จับคู่คลาสได้ 57, เห็นใน SMLAccountPOSProfessional (edition 12) 60
- คลาสหน้าจอที่ใช้บ่อย: `SMLERPGL._tax._vat` (8), `SMLERPGL._report._tax._wht` (3), `SMLERPGL._report._singhaReportProfitAndLost._report` (2), `SMLERPGL._glTransControl` (2), `SMLERPGL._chart._chartOfAccount` (1), `MyLib._myFrameWork` (1)
- control หลักที่ฝัง: `SMLERPGLControl._glDetail` (5), `SMLERPGLControl._journalScreen` (5), `SMLERPGLControl._recurring` (2), `SMLERPControl._selectCode` (1), `SMLERPGLControl._vatBuy` (1), `SMLERPGLControl._vatSale` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 1998 | บัญชี_ประมวลผลสิ้นงวด | 1 |
| 1999 | บัญชี_ประมวลผลสิ้นปี | 1 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`resource_report_vat`, `erp_branch_list`, `gl_list_view`, `gl_chart_of_account`, `gl_journal_vat_buy`, `gl_journal_vat_sale`, `ar_customer_detail`, `ar_customer`, `gl_journal`, `ap_supplier_detail`, `ap_supplier`, `gl_journal_detail`, `gl_tax_group`, `ic_trans`, `gl_account_group`, `erp_doc_format`, `gl_wht_list_detail`, `gl_wht_list`, `gl_resource`, `ap_ar_trans`, `gl_journal_book`, `gl_journal_summary`, `gl_summary_close_account_detaiil`, `gl_journal_summary_detail`, `gl_trans`, `gl_trans_detail`, `gl_chart_of_account_side_list`, `gl_chart_of_account_depart_list`, `gl_chart_of_account_allocate_list`, `gl_chart_of_account_project_list`, `gl_chart_of_account_job_list`, `erp_side_list`, `erp_department_list`, `erp_allocate_list`, `erp_job_list`, `erp_project_list`, `gl_cash_flow_group`, `logs`, `erp_doc_format_gl`, `as_trans_detail`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| ผังบัญชี › รายละเอียดผังบัญชี | `menu_chart_of_account` | ✓ | `SMLERPGL._chart._chartOfAccount` |  | gl_chart_of_account_side_list, gl_chart_of_account_depart_list, gl_chart_of_account_allocate_list, gl_chart_of_account_project_list |
| ผังบัญชี › ปรับปรุงผังบัญชีแบบเร็ว | `menu_chart_of_account_fast` | ✓ | `MyLib._myFrameWork` |  | gl_chart_of_account |
| ผังบัญชี › ตรวจสอบโครงสร้างผังบัญชี | `menu_chart_of_account_flow` | ✓ | `SMLERPGL._chart._chatOfAccountFlow` |  |  |
| ผังบัญชี › รายงานรายละเอียดผังบัญชี | `menu_report_chart_of_account` | ✓ | `SMLERPGL._report._chartOfAccount._report` |  | gl_chart_of_account |
| บัญชีแยกประเภท › ข้อมูลรายวัน | `menu_gl_journal` | ✓ | `SMLERPGL._journalEntryAccount` |  | gl_journal, gl_journal_detail, gl_journal_vat_buy, gl_journal_vat_sale |
| บัญชีแยกประเภท › บันทึกข้อมูลรายวันแบบเร็ว | `menu_gl_journal_fast` | ✓ | `SMLERPGL._journalEntryFast` |  | gl_journal, gl_chart_of_account, gl_journal_detail |
| บัญชีแยกประเภท › บันทึกรูปภาพ | `menu_gl_picture` | ✓ | `SMLERPGL._journalEntryAccount_pic` |  | gl_journal |
| บัญชีแยกประเภท › ประมวลผลจากข้อมูลรายวัน | `menu_gl_process` | ✓ | `SMLERPGL._transProcessUserControl` |  | gl_journal, erp_doc_format_gl, erp_doc_format, gl_journal_detail |
| บัญชีแยกประเภท › ตรวจสอบความถูกต้อง | `menu_gl_check_data` | ✓ | `SMLERPGL._checkData` |  | gl_journal_detail, gl_journal, ic_trans, gl_chart_of_account |
| บัญชีแยกประเภท › ผ่านรายการ | `menu_gl_journal_pass` | ✓ | `SMLERPGL._journalPass` |  | gl_journal, gl_journal_detail, gl_chart_of_account |
| บัญชีแยกประเภท › ยกเลิกผ่านรายการ | `menu_gl_journal_pass_cancel` | ✓ | `SMLERPGL._journalPassUndo` |  | gl_journal |
| บัญชีแยกประเภท › สรุปบัญชีสินค้าและต้นทุนขาย | `menu_product_sale_cost_close` | ✓ | `SMLERPGL.JournalProductSaleCost._journalProductSaleCostControl` |  | gl_account_close_detail, gl_account_close, gl_journal, gl_journal_detail |
| บัญชีแยกประเภท › สรุปยอดบัญชี | `menu_journal_summary` | ✓ | `SMLERPGL.JournalSummary.JournalSummaryControl` |  | gl_journal_summary, gl_summary_close_account_detaiil, gl_journal_summary_detail, gl_journal |
| บัญชีแยกประเภท › แสดงบัญชีแยกประเภท | `menu_gl_show_sheet` | ✓ | `SMLERPGL._display._glList` |  | gl_list_view |
| บัญชีแยกประเภท › แสดงบัญชีแยกประเภท (แบบสรุป) | `menu_gl_show_sheet_sum` | ✓ | `SMLERPGL._display._glListSum` |  | gl_list_view |
| บัญชีแยกประเภท › รายงานข้อมูลรายวัน | `menu_gl_report_journal` | ✓ | `SMLERPGL._report._report_journal_daily_lao._report_daily_journal_lao` |  |  |
| บัญชีแยกประเภท › รายงานข้อมูลรายวันแบบสรุป | `menu_gl_report_journal_sum` | ✓ | `SMLERPGL._report._journalSum._report` |  | gl_journal, gl_journal_book |
| บัญชีแยกประเภท › รายงานบัญชีแยกประเภท | `menu_gl_report_sheet` | ✓ | `SMLERPGL._report._sheet._report` |  | gl_list_view, gl_chart_of_account |
| บัญชีแยกประเภท › รายงานบัญชีแยกประเภท (แบบสรุป) | `menu_gl_report_sheet_sum` | ✓ | `SMLERPGL._report._sheetSum._report` |  | gl_list_view |
| ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย | `menu_report_vat_sale` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงาน ภาษีขาย (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (รูปแบบใหม่) | `menu_report_vat_sale_2557` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (มาตรฐาน) | `menu_report_vat_sale_standard` | ✓ | `SMLERPGL._report._tax._reportVatSale` |  | gl_journal_vat_sale, resource_report_vat, erp_branch_list |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (รูปแบบใหม่แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_sale_with_tax` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษีขาย | `menu_report_sum_vat_sale` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ | `menu_report_vat_buy` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ (แสดงมูลค่าอัตราภาษีศูนย์) | `menu_report_except_vat_buy` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงาน ภาษีซื้อ (รูปแบบใหม่) | `menu_report_vat_buy_2557` | ✓ | `SMLERPGL._tax._vat` |  | gl_journal_vat_sale, gl_journal_vat_buy, ar_customer_detail, ap_supplier_detail |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีซื้อ (มาตรฐาน) | `menu_report_vat_buy_standard` | ✓ | `SMLERPGL._report._tax._reportVatBuy` |  | gl_journal_vat_sale, erp_branch_list, gl_journal_vat_buy, resource_report_vat |
| ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษี | `menu_gl_vat_report_sum` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีขายต่างประเทศ | `menu_gl_vat_report_sale_inter` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีซื้อต่างประเทศ | `menu_gl_vat_report_buy_inter` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ภาษีมูลค่าเพิ่ม › รายงานสรุปภาษีต่างประเทศ | `menu_gl_vat_report_inter_sum` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีขายรูปแบบใหม่อัตราภาษีศูนย์ (เพิ่มรายละเอียด) | `menu_report_except_vat_sale_with_tax_add_detail` |  | `SMLERPGL._tax._vatSale` |  | gl_journal_vat_sale, ar_customer_detail, ic_trans, resource_report_vat |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 1) | `menu_report_except_vat_buy_type1` |  | `SMLERPGL._tax._vatBuyNewType1` |  | ic_trans, resource_report_vat, erp_branch_list, gl_journal_vat_buy |
| ภาษีมูลค่าเพิ่ม › รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 2) | `menu_report_except_vat_buy_type2` |  | `SMLERPGL._tax._vatBuyNewType2` |  | ic_trans, gl_journal_vat_sale, resource_report_vat, erp_branch_list |
| หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.53) | `menu_gl_wht_report_in_53` | ✓ | `SMLERPGL._report._tax._wht` |  | resource_report_vat, gl_wht_list_detail, gl_wht_list, ap_supplier |
| หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.3) | `menu_gl_wht_report_in_3` | ✓ | `SMLERPGL._report._tax._wht` |  | resource_report_vat, gl_wht_list_detail, gl_wht_list, ap_supplier |
| หัก ณ. ที่จ่าย › รายงานภาษีถูกหัก ณ. ที่จ่าย | `menu_gl_wht_report_sum` | ✓ | `SMLERPGL._report._tax._wht` |  | resource_report_vat, gl_wht_list_detail, gl_wht_list, ap_supplier |
| หัก ณ. ที่จ่าย › ส่งออกข้อมูลภาษีหัก ณ ทีจ่าย | `menu_export_wht` | ✓ | `SMLERPGL._tax._whtExport` |  |  |
| การจัดสรรค์ › ข้อมูลรายวันเชิงวิเคราะห์ | `menu_gl_allocate_all` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| รายงาน › ใบปะหน้าเอกสาร | `menu_gl_report_slip` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| งบการเงิน › แสดงงบทดลอง | `menu_gl_show_trial_balance` | ✓ | `SMLERPGL._display._glTrialBalance` |  | gl_list_view |
| งบการเงิน › แสดงงบทดลอง (มิติ) | `menu_gl_analysis_trial_balance` | ✓ | `SMLERPGL._analysis._trialBalance` |  | gl_list_view |
| งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (มาตรฐาน) | `menu_gl_report_trial_balance` | ✓ | `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` |  |  |
| งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (แยกแผนก) | `menu_gl_report_trial_balance_depart` | ✓ | `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` |  | gl_list_view |
| งบการเงิน › รายงานงบทดลอง › รายงานงบทดลอง (แยกสาขา) | `menu_gl_report_trial_balance_branch` | ✓ | `SMLERPGL._report._trialBalanceBranch._report` |  | gl_list_view |
| งบการเงิน › รายงานงบทดลอง › งบดุลหลังปรับปรุง | `menu_gl_report_balancesheet_asset_lao` |  | `SMLERPGL._report._report_balancesheet_asset_lao._report_balancesheet_asset_lao` |  |  |
| งบการเงิน › รายงานงบทดลอง › งบรายรับรายจ่าย | `menu_gl_report_profit_and_lost_lao` |  | `SMLERPGL._report._report_balancesheet_profit_and_lost_lao._report_balancesheet_profit_and_lost_lao` |  |  |
| งบการเงิน › แสดงรายการงบดุล | `menu_display_balance_sheet` |  | fallback:_g._selectMenu (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| งบการเงิน › รายงานงบดุล | `menu_gl_report_balance` | ✓ | tag:gl (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| งบการเงิน › งบดุล | `menu_singha_report_balancesheet_asset` | ✓ | `SMLERPGL._report._singhaReportProfitAndLost._report` |  | gl_chart_of_account, gl_journal_detail, gl_list_view, gl_account_group |
| งบการเงิน › แสดงกระดาษทำการ | `menu_gl_show_work_sheet` | ✓ | `SMLERPGL._display._glWorkSheet` |  | gl_list_view |
| งบการเงิน › รายงานกระดาษทำการ | `menu_gl_report_balance_sheet` | ✓ | `SMLERPGL._report._workSheet._report` |  | gl_list_view |
| งบการเงิน › งบกำไรขาดทุน เปรียบเทียบ | `menu_display_lost_and_profit_compare_dimension` | ✓ | `SMLERPGL.LostAndProfit._display_lost_and_profit_compare_dimension` |  | gl_resource |
| งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (แยกสาขา) | `menu_gl_report_profit_and_lost_branch_1` | ✓ | `SMLERPGL._report._profitAndLostBranch._report` |  | gl_list_view |
| งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (แยกสาขา-แผนก) | `menu_gl_report_trial_balance_branch_depart` | ✓ | `SMLERPGL._report._trialBalanceBranchDepart._report` |  | gl_list_view |
| งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน | `menu_singha_report_profit_and_lost` | ✓ | `SMLERPGL._report._singhaReportProfitAndLost._report` |  | gl_chart_of_account, gl_journal_detail, gl_list_view, gl_account_group |
| งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) | `menu_report_profit_and_lost_sum_year` | ✓ | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year` |  |  |
| งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) ตามแผนก | `menu_report_profit_and_lost_sum_year_by_department` | ✓ | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year_by_department` |  |  |
| งบการเงิน › งบกระแสเงินสด | `menu_gl_report_other_1` | ✓ | `SMLERPGL._report._other_1._report` |  | gl_list_view |
| รายงานงบการเงิน | `menu_financial_report` | ✓ | tag:gl |  |  |
| ประมวลผลสิ้นงวด | `menu_gl_end_of_period` | ✓ | `SMLERPGL._glTransControl` | 1998 | gl_journal_detail, gl_trans, gl_trans_detail, gl_chart_of_account |
| ประมวลผลสิ้นปี | `menu_gl_end_of_year` | ✓ | `SMLERPGL._glTransControl` | 1999 | gl_journal_detail, gl_trans, gl_trans_detail, gl_chart_of_account |
| ประมวลผลกำไร/ขาดทุน และต้นทุนขาย | `menu_close_account_process` | ✓ | `SMLERPGL.AccountCloseWizard.JournalCloseAccountControl` |  | gl_journal_summary, gl_journal_summary_detail, gl_summary_close_account_detaiil |
| รายงานอื่น ๆ | `menu_fastreport_other_gl` | ✓ | `SMLFastReport._loadForm` |  | sml_fastreport |
