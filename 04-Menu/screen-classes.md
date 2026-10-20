---
tags: [sml, screen, generated]
---
# คลาสหน้าจอ จัดกลุ่มตาม base class (หน้าจอต้นแบบ)

> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` — base class บอกว่าหน้าจอใช้ต้นแบบอะไร (เช่นหน้าจอเอกสาร, รายงาน, master data) กลับไป [[menu-map]]

| base class | จำนวนคลาส | จำนวนเมนู |
|---|---|---|
| `UserControl` | 259 | 859 |
| `MyLib._ManageTransData` | 18 | 19 |
| `SMLReport._report._viewReport` | 17 | 18 |
| `Form` | 12 | 13 |
| `MyLib._myForm` | 7 | 7 |
| `MyLib._manageMasterCodeFull` | 3 | 3 |
| `_create_delivery_order` | 3 | 3 |
| `MyLib._dialogConfigForm` | 2 | 2 |
| `_report_lao_balance_sheet._report_lao_balance_sheet` | 2 | 2 |
| `_itemCodeUserControl` | 1 | 1 |
| `_stockAutoAdjustControl` | 1 | 1 |
| `(ไม่พบ base)` | 1 | 1 |
| `SMLInventoryControl._icTransControl` | 1 | 1 |
| `_IMyFrameWork` | 1 | 1 |
| `_report_profit_and_lost_sum_year` | 1 | 1 |

## UserControl

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLFastReport._designer` | `SMLFastReport/_designer.cs` | รายงานพนักงานเรียงตามกลุ่ม (`menu_report_employee_group`), ออกแบบรายงาน (`fast_report_designer`), รายงานการอนุมัติผู้จำหน่ายสินค้า (`report_imex_qc_approved_vendor`), สินค้าที่ไม่มีการขาย (`IC_INVENTORY_NO_SALE`), รายงานยอดคงเหลือสินค้า (แสดงทุกสินค้า)  แสดงมูลค่าปัจจุบัน (`menu_stock_balance_all_show_current_value`), รายงานการปรับปรุงสินค้า (`menu_report_inventory_adjust`) … +127 |
| `SMLInventoryControl._clone_icTrans` | `SMLInventoryControl/_clone_icTrans.cs` | สินค้า/วัตถุดิบ คงเหลือยกมา (`menu_ic_stk_balance`), รับสินค้าสำเร็จรูป (`menu_ic_finish_receive`), ขอเบิกสินค้า/วัตถุดิบ (`menu_ic_request_issue`), เบิกสินค้า/วัตถุดิบ (`menu_ic_issue`), รับคืนสินค้า/วัตถุดิบ จากการเบิก (`menu_ic_return_receive`), ขอโอนสินค้า/วัตถุดิบ (`menu_ic_request_transfer`) … +98 |
| `SMLERPReportTool._reportTrans` | `SMLERPReportTool/_reportTrans.cs` | รายงานยกเลิกรับสินค้าสำเร็จรูป (`menu_ic_report_cancel_goods_pack`), รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ (`menu_ic_report_cancel_raw_material`), รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก (`menu_ic_report_cancel_goods_raw_meterial`), รายงานสินค้าและวัตถุดิบ คงเหลือยกมา (`menu_ic_report_goods_balance`), รายงานการรับสินค้าสำเร็จรูป (`menu_import_item_ready_by_date`), รายงานการเบิกสินค้าและวัตถุดิบ (`menu_ic_report_item_withdraw`) … +91 |
| `MyLib._manageMasterCodeFull` | `MyLib/_manageMasterCodeFull.cs` | กำหนดรายละเอียดสาขา (`menu_setup_branch`), กำหนดรายละเอียดแผนก (`menu_setup_department_list`), กำหนดพนักงาน (`menu_setup_staff`), กำหนดกลุ่มพนักงาน (`menu_setup_user_group`), กำหนดผู้ใช้ระบบ MIS (`menu_setup_staff_mis`), กำหนดกลุ่มเอกสาร (`menu_setup_doc_group`) … +68 |
| `SINGHAReport._saleToolsWebControl` | `SINGHAReport/_saleToolsWebControl.cs` | Customer (`menu_saletools_customer`), Route Planning (`menu_saletools_route_planning`), AdHoc Jobs (`menu_saletools_adhoc_jobs`), Manage Route Plan (`menu_saletools_manage_route_plan`), Approve Invoice (`menu_saletools_approve_invoice`), Approve Invoice (`menu_saletools_approve_sales_invoice`) … +58 |
| `SMLERPReportTool._reportCashBankTrans` | `SMLERPReportTool/_reportCashBankTrans.cs` | รายงานรายได้อื่นๆ (`menu_cash_income_other_report`), รายงานลดหนี้รายได้อื่นๆ (`menu_cash_income_other_credit_report`), รายงานเพิ่มหนี้รายได้อื่นๆ (`menu_cash_income_other_debit_report`), รายงานยกเลิกรายได้อื่นๆ (`menu_cash_income_other_cancel_report`), รายงานยกเลิกลดหนี้รายได้อื่นๆ (`menu_cash_income_other_credit_cancel_report`), รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ (`menu_cash_income_other_debit_cancel_report`) … +32 |
| `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` | `SMLERPICReport/ic_analysis/_ic_report_info_stk_profit.cs` | รายงานกำไรขั้นต้น (สินค้า) (`menu_ic_report_info_stk_profit`), รายงานกำไรขั้นต้น (สินค้า-เอกสาร) (`menu_ic_report_info_stk_profit_ic_doc`), รายงานกำไรขั้นต้น (สินค้า-ลูกค้า) (`menu_ic_report_info_stk_profit_ic_cust`), รายงานกำไรขั้นต้น (สินค้า-ลูกค้า-เอกสาร) (`menu_ic_report_info_stk_profit_ic_cust_doc`), รายงานกำไรขั้นต้น (เอกสาร) (`menu_ic_report_info_stk_profit_doc`), รายงานกำไรขั้นต้น (เอกสาร-สินค้า) (`menu_ic_report_info_stk_profit_doc_ic`) … +5 |
| `SMLERPReportTool._reportArApTrans` | `SMLERPReportTool/_reportArApTrans.cs` | รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) (`menu_ap_report_cancel_pay_bill`), รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) (`menu_ap_report_cancel_debt_billing`), รายงานใบรับวางบิล (เจ้าหนี้) (`menu_ap_report_billing`), รายงานการจ่ายชำระหนี้ (เจ้าหนี้) (`menu_ap_report_payment`), รายงานยกเลิกใบวางบิล(ลูกหนี้) (`menu_ar_report_cancel_pay_billing`), รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน (`menu_ar_report_cancel_invoice`) … +3 |
| `SMLERPICReport._report_ic_summary` | `SMLERPICReport/_report_ic_summary.cs` | รายงานสินค้าแบบมี Serial (`menu_ic_by_license`), รายงานของแถมซื้อ (`menu_ic_report_item_giveaway`), รายงานผลต่างจากการตรวจนับ (`menu_diff_from_count`), รายงานสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ (`menu_stock_no_balance_from_count`), รายงานการตรวจสอบสินค้า Serial (`menu_report_serial_check`), รายงานสถานะสินค้า (`menu_item_status`) … +2 |
| `SMLERPGL._tax._vat` | `SMLERPGL/_report/_tax/_vat.cs` | รายงาน ภาษีขาย (`menu_report_vat_sale`), รายงาน ภาษีขาย (แสดงมูลค่าอัตราภาษีศูนย์) (`menu_report_except_vat_sale`), รายงานภาษีขาย (รูปแบบใหม่) (`menu_report_vat_sale_2557`), รายงานภาษีขาย (รูปแบบใหม่แสดงมูลค่าอัตราภาษีศูนย์) (`menu_report_except_vat_sale_with_tax`), รายงานสรุปภาษีขาย (`menu_report_sum_vat_sale`), รายงาน ภาษีซื้อ (`menu_report_vat_buy`) … +2 |
| `SINGHAReport.GL._glReport` | `SINGHAReport/GL/_glReport.cs` | สรุปการ์ดสินค้า (`menu_singha_report_stock_movement`), สรุปโหลดสินค้า รายคลัง (`menu_singha_report_load_product_warehouse`), รายงานยอดขายรายเดือนตามกลุ่มผลิตภัณฑ์/เทียบปี (`menu_report_sale_category_year_compare`), รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.3) (`menu_singha_report_product_wht_3`), รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.53) (`menu_singha_report_product_wht_53`), สมุดบัญชีแยกประเภทเงินสด (`menu_report_cash_gl_sheet`) … +2 |
| `SMLERPIC._cancelControl` | `SMLERPIC/_cancelControl.cs` | ยกเลิกรับสินค้าสำเร็จรูป (`menu_ic_finish_receive_cancel`), ยกเลิกขอเบิกสินค้า/วัตถุดิบ (`menu_ic_request_issue_cancel`), ยกเลิกใบเบิกสินค้า/วัตถุดิบ (`menu_ic_issue_cancel`), ยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก (`menu_ic_return_receive_cancel`), ยกเลิกโอนสินค้า/วัตถุดิบ (`menu_ic_transfer_wh_out_cancel`), ยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) (`menu_ic_stk_adjust_over_cancel`) … +1 |
| `SINGHAReport._singhareportGenerate` | `SINGHAReport/_singhareportGenerate.cs` | การ์ดเจ้าหนี้ (`menu_singha_report_supplier_card`), รายงานสรุปการขายสินค้าตามพนักงานขาย (`menu_singha_report_sale_summary_by_saleman`), ยอดลูกหนี้คงเหลือ (`menu_singha_report_customer_credit_balance`), ลูกหนี้คงค้าง (`menu_singha_report_ar_outstanding`), ยอดลูกหนี้คงเหลือ ตามระยะเวลาเครดิต (`menu_singha_report_customer_credit_balance_by_creditdate`), รายงานการตัดเช็ค (`report_singha_chq_receive_movement`) … +1 |
| `SMLERPICInfo._stkProfit` | `SMLERPICInfo/_stkProfit.cs` | กำไรขั้นต้นตามสินค้า (`menu_ic_info_stk_profit`), กำไรขั้นต้นตามสินค้า (รวมต้นทุนแฝง) (`menu_ic_info_stk_profit_hidden`), กำไรขั้นต้นตามเอกสารขาย (`menu_ic_info_stk_profit_by_doc`), กำไรขั้นต้นตามลูกค้า (`menu_ic_info_stk_profit_by_ar`) |
| `SMLERPGL._report._singhaReportProfitAndLost._report` | `SMLERPGL/_report/_singhaReportProfitAndLost/_report.cs` | งบดุล (`menu_singha_report_balancesheet_asset`), งบกำไรขาดทุน (`menu_singha_report_profit_and_lost`), งบกำไรขาดทุน (`menu_singha_report_profit_and_lost`), งบดุล (`menu_singha_report_balancesheet_asset`) |
| `SMLERPIC._icMain` | `SMLERPIC/_icMain.cs` | ข้อมูลสินค้า (`menu_ic_item_detail`), ข้อมูลสินค้า (แสดงตามบาร์โค๊ด) (`menu_ic_item_detail_barcode`), กำหนดสินค้า (`menu_ic_item_for_sync`) |
| `SMLERPICInfo._stkMovement` | `SMLERPICInfo/_stkMovement.cs` | เคลื่อนไหวสินค้า (`menu_ic_info_stk_move`), บัญชีคุมพิเศษ (`menu_ic_info_stk_movement`), บัญชีคุมพิเศษ (รวมต้นทุนแฝง) (`menu_ic_info_stk_movement_hidden`) |
| `SMLERPCASHBANKReport._report_chq._chqCreditCardList` | `SMLERPCASHBANKReport/_report_chq/_chqCreditCardList.cs` | รายงานทะเบียนเช็ครับ (`menu_cb_report_chq_in_receive`), รายงานทะเบียนเช็คจ่าย (`menu_cb_report_chq_out_payment`), รายงานรายการรับบัตรเครดิต (`menu_cb_report_credit_card_receive`) |
| `SMLERPGL._report._tax._wht` | `SMLERPGL/_report/_tax/_wht.cs` | รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.53) (`menu_gl_wht_report_in_53`), รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.3) (`menu_gl_wht_report_in_3`), รายงานภาษีถูกหัก ณ. ที่จ่าย (`menu_gl_wht_report_sum`) |
| `SINGHAReport._singhaDataSyncControl` | `SINGHAReport/_singhaDataSyncControl.cs` | Data ARM (`menu_sync_data_arm`), Data Saleout (`menu_sync_data_saleout`), Data Stock (`menu_sync_data_stock`) |
| `_g._changeCode._changeApArCodeUserControl` | `SMLERPGlobal/_changeCode/_changeApArCodeUserControl.cs` | เปลี่ยนรหัสเจ้าหนี้ (`menu_change_code_supplier`), เปลี่ยนรหัสลูกหนี้ (`menu_change_code_customer`) |
| `SMLFastReport._importFastReport` | `SMLFastReport/_importFastReport.cs` | นำเข้ารายงาน (`menu_import_report`), นำเข้ารายงานสาขา (`menu_import_report_branch`) |
| `SMLERPIC._icMainDetail` | `SMLERPIC/_icMainDetail.cs` | ข้อมูลสินค้าเพิ่มเติม (`menu_ic_item_detail_2`), ข้อมูลสินค้าเพิ่มเติม (แสดงตามบาร์โค๊ด) (`menu_ic_item_detail_2_barcode`) |
| `SMLInventoryControl._icPrice._icPriceList` | `SMLInventoryControl/_icPrice/_icPriceList.cs` | กำหนดราคาขายมาตรฐาน (`menu_ic_item_saleprice`), กำหนดราคาขายทั่วไป (`menu_ic_item_saleprice_2`) |
| `SMLERPICReport._report_ic_sale_price` | `SMLERPICReport/_report_ic_sale_price.cs` | รายงานราคาขายสินค้ามาตรฐาน (`menu_ic_report_item_sale_price`), รายงานราคาขายสินค้าทั่วไป (`menu_ic_report_item_sale_price_normal`) |
| `SMLERPSO._soSaleorder` | `SMLERPSO/_soSaleorder.cs` | ใบสั่งผลิต (`menu_imex_sale_order`), บันทึกใบสั่งขาย (`menu_so_sale_order`) |
| `SMLERPICInfo._stkMovementSum` | `SMLERPICInfo/_stkMovementSum.cs` | สรุปการเคลื่อนไหวตามปริมาณ (`menu_ic_info_stk_movement_sum`), สรุปการเคลื่อนไหวตามมูลค่า (`menu_ic_info_stk_movement_sum_by_amount`) |
| `SMLInventoryControl._transHistory` | `SMLInventoryControl/_transHistory.cs` | ประวัติการซื้อสินค้า (`menu_ic_info_purchase_history`), ประวัติการขายสินค้า (`menu_ic_info_sale_history`) |
| `SMLERPICReport._report_ic_stk_movement` | `SMLERPICReport/_report_ic_stk_movement.cs` | รายงานบัญชีคุมพิเศษสินค้า (`menu_account_special_item`), รายงานเคลื่อนไหวสินค้า (`menu_item_transfer`) |
| `SMLERPICReport._report_ic_balance` | `SMLERPICReport/_report_ic_balance.cs` | รายงานยอดคงเหลือสินค้า (`menu_item_balance`), รายงานยอดคงเหลือสินค้าตาม LOT (`menu_item_balance_lot`) |
| `SMLERPSOReport._report._report_sale_service_by_item` | `SMLERPSOReport/_report/_report_sale_service_by_item.cs` | รายงานซื้อสินค้าแยกตามสินค้า (`menu_po_recive_by_item`), รายงานการขายและบริการเรียงตามสินค้า (`menu_so_sale_service_by_item`) |
| `SMLERPSO._soInvoice` | `SMLERPSO/_soInvoice.cs` | ขายสินค้า/บริการ (`menu_so_invoice`), รายการใบกำกับภาษีอย่างย่อ (`pos_invoice_list_pos`) |
| `SMLERPSO._soInvoiceCancel` | `SMLERPSO/_soInvoiceCancel.cs` | ยกเลิกขายสินค้า/บริการ (`menu_so_invoice_cancel`), รายการใบกำกับภาษีอย่างย่อยกเลิก (`pos_invoice_cancel_pos`) |
| `SMLERPSOReport._report_drug_sale_8` | `SMLERPSOReport/_report_drug_sale_8.cs` | รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.8) (`menu_so_report_sale_drug_by_lot`), บัญชีการผลิตยาและขายยาที่ผลิต (แบบ ผ.ย. ๕) (`menu_so_report_sale_drug_by_lot_5`) |
| `SMLTransportLabel._transport_label` | `SMLTransportLabel/_transport_label.cs` | ที่อยู่จัดส่งสินค้า (`menu_ap_transport_label`), ที่อยู่จัดส่งสินค้า (`menu_ar_transport_label`) |
| `SMLTransportLabel._transport_label_print` | `SMLTransportLabel/_transport_label_print.cs` | พิมพ์ที่อยู่จัดส่งสินค้า (`menu_ap_transport_label_print`), พิมพ์ที่อยู่จัดส่งสินค้า (`menu_ar_transport_label_print`) |
| `SMLERPARAPReport.report._movement` | `SMLERPARReport/report/_movement.cs` | รายงานเคลื่อนไหวเจ้าหนี้ (`menu_ap_report_payable_movement`), รายงานเคลื่อนไหวลูกหนี้ (`menu_ar_report_movement`) |
| `SMLERPARAPReport.report._ageing` | `SMLERPARReport/report/_ageing.cs` | รายงานอายุเจ้าหนี้ (`menu_ap_report_payable_aging`), รายงานอายุลูกหนี้ (`menu_ar_report_period_ar_debt_remain`) |
| `SMLERPARAPReport.report._ageingByCodeAndDoc` | `SMLERPARReport/report/_ageingByCodeAndDoc.cs` | รายงานอายุเจ้าหนี้-ตามเอกสาร (`menu_ap_report_payable_aging_by_doc`), รายงานอายุลูกหนี้-ตามเอกสาร (`menu_ar_report_period_ar_debt_remain_by_doc`) |
| `SMLERPARAPReport.report._absolute_status` | `SMLERPARReport/report/_absolute_status.cs` | รายงานสถานะเจ้าหนี้ (`menu_ap_report_payable_status`), รายงานสถานะลูกหนี้ (`menu_ar_report_status_ar`) |
| `SMLERPCASHBANKReport._report_petty_cash` | `SMLERPCASHBANKReport/_report_petty_cash.cs` | รายงานเคลื่อนไหวเงินสดย่อย (`menu_sub_cash_movements`), รายงานสถานะเงินสดย่อย (`menu_peety_cash_status`) |
| `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` | `SMLERPGL/_report/_trialBalanceDepart/_reportTrialBalanceDepart.cs` | รายงานงบทดลอง (แยกแผนก) (`menu_gl_report_trial_balance_depart`), รายงานงบทดลอง (แยกแผนก) (`menu_gl_report_trial_balance_depart`) |
| `SMLERPGL._report._trialBalanceBranch._report` | `SMLERPGL/_report/_trialBalanceBranch/_report.cs` | รายงานงบทดลอง (แยกสาขา) (`menu_gl_report_trial_balance_branch`), รายงานงบทดลอง (แยกสาขา) (`menu_gl_report_trial_balance_branch`) |
| `SMLERPGL._report._workSheet._report` | `SMLERPGL/_report/_workSheet/_report.cs` | รายงานกระดาษทำการ (`menu_gl_report_balance_sheet`), รายงานกระดาษทำการ (`menu_gl_report_balance_sheet`) |
| `SMLERPGL._report._profitAndLostBranch._report` | `SMLERPGL/_report/_profitAndLostBranch/_report.cs` | งบกำไรขาดทุน (แยกสาขา) (`menu_gl_report_profit_and_lost_branch_1`), งบกำไรขาดทุน (แยกสาขา) (`menu_gl_report_profit_and_lost_branch_1`) |
| `SMLERPGL._report._trialBalanceBranchDepart._report` | `SMLERPGL/_report/_trialBalanceBranchDepart/_report.cs` | งบกำไรขาดทุน (แยกสาขา-แผนก) (`menu_gl_report_trial_balance_branch_depart`), งบกำไรขาดทุน (แยกสาขา-แผนก) (`menu_gl_report_trial_balance_branch_depart`) |
| `SMLERPGL._report._other_1._report` | `SMLERPGL/_report/_other_1/_report.cs` | งบกระแสเงินสด (`menu_gl_report_other_1`), งบกระแสเงินสด (`menu_gl_report_other_1`) |
| `SMLERPGL._glTransControl` | `SMLERPGL/_glTransControl.cs` | ประมวลผลสิ้นงวด (`menu_gl_end_of_period`), ประมวลผลสิ้นปี (`menu_gl_end_of_year`) |
| `SINGHAReport.GL._glReportGenerate` | `SINGHAReport/GL/_glReportGenerate.cs` | รายงานภาษีซื้อ (`menu_singha_report_vat_buy`), รายงานภาษีขาย (`menu_singha_report_vat_sale`) |
| `_g._userGroupWarehouseShelf` | `SMLERPGlobal/_userGroupWarehouseShelf.cs` | กำหนดการใช้คลังและที่เก็บ (`menu_setup_user_group_warehouse_shelf`) |
| `SMLERPControl.erp_user._erp_userDetailpicture` | `SMLERPControl/erp_user/_erp_userDetailpicture.cs` | กำหนดรูปภาพพนักงาน (`menu_setup_staff_pic`) |
| `SMLERPConfig._provinceLoadFromWebControl` | `SMLERPConfig/_provinceLoadFromWebControl.cs` | ดึงรายชื่อจังหวัดอัตโนมัติ (`menu_setup_province_auto`) |
| `SMLPOSControl._posMachine` | `SMLPOSControl/_posMachine.cs` | กำหนดรหัสเครื่อง POS (`menu_config_pos_machine`) |
| `SMLPOSControl._designer._clientDesign` | `SMLPOSControl/_designer/_clientDesign.cs` | ออกแบบหน้าจอขาย POS (`client_design`) |
| `SMLERPConfig._salePlanManage` | `SMLERPConfig/_salePlanManage.cs` | กำหนดแผนการขาย (`menu_sale_plan`) |
| `SMLERPCASHBANK._cb_petty_cash` | `SMLERPCASHBANK/_cb_petty_cash.cs` | กำหนดวงเงินสดย่อย (`menu_petty_cash`) |
| `SMLERPGL.StatementDesign._statementDesigner` | `SMLERPGL/StatementDesign/_statementDesigner.cs` | ออกแบบงบการเงิน (`menu_gl_report_design`) |
| `SMLReport._formReport._formDesigner` | `SMLReport/_formReport/_formDesigner.cs` | สร้าง/แก้ไขแบบฟอร์ม (`menu_form_edit`) |
| `_g._viewManageCustom` | `SMLERPGlobal/_viewManageCustom.cs` | กำหนดรูปแบบการค้นหาข้อมูล (`menu_view_manager_custom`) |
| `MyLib._databaseManage._databaseStruct` | `MyLib/_databaseManage/_databaseStruct.cs` | แสดงโครงสร้างฐานข้อมูลทั้งหมด (`menu_database_struct`) |
| `SMLERPICInfo._icTransectionCheck` | `SMLERPICInfo/_icTransectionCheck.cs` | ตรวจสอบและปรับปรุงข้อมูล (`menu_checking_ic_trans`) |
| `SMLERPControl._systemFlow` | `SMLERPControl/_systemFlow.cs` | ผังการทำงานระบบ (`menu_system_flow`) |
| `MyLib._databaseManage._queryDataView` | `MyLib/_databaseManage/_queryDataView.cs` | ใช้คำสั่ง Query (`menu_query`) |
| `_g._changeCode._itemCodeUserControl` | `SMLERPGlobal/_changeCode/_itemCodeUserControl.cs` | เปลี่ยนรหัสสินค้า (`menu_change_code_item`) |
| `_viewCapture._viewScreen` | `SMLERPGlobal/_viewScreen.cs` | แสดงหน้าจอการใช้งาน (`menu_view_capture_screen_realtime`) |
| `SMLReport._ImportFormDesign` | `SMLReport/_ImportFormDesign.cs` | นำเข้าแบบฟอร์ม (`menu_import_formdesign`) |
| `_viewCapture._viewCaptureScreen` | `SMLERPGlobal/_viewCaptureScreen.cs` | แสดงหน้าจอการใช้งาน (ย้อนหลัง) (`menu_view_capture_screen`) |
| `SMLERPAudit._loginLog` | `SMLERPAudit/_loginLog.cs` | เข้าใช้ฐานข้อมูล (`menu_audit_login`) |
| `SMLERPAudit._menuLog` | `SMLERPAudit/_menuLog.cs` | เข้าออกระบบ (`menu_audit_menu`) |
| `SMLERPAudit._transLog` | `SMLERPAudit/_transLog.cs` | ข้อมูลรายวัน (`menu_audit_trans`) |
| `SMLERPAudit._masterLog` | `SMLERPAudit/_masterLog.cs` | ข้อมูลหลัก (`menu_audit_master`) |
| `SMLERPAudit._fullLogs` | `SMLERPAudit/_fullLogs.cs` | ประวัติการแก้ไขรายวัน (`menu_trans_full_logs`) |
| `MyLib._databaseManage._importDataControl` | `MyLib/_databaseManage/_importDataControl.cs` | นำเข้าข้อมูลหลัก (`menu_import_data_master`) |
| `MyLib._databaseManage._genQueryControl` | `MyLib/_databaseManage/_genQueryControl.cs` | สร้างคำสั่ง Query (`menu_gen_qeury`) |
| `SMLAccount._mainShortcut` | `SMLAccount/_mainShortcut.cs` | หน้าจอเริ่มต้น (`menu_welcome_page`) |
| `SMLERPIC._icImportPicture` | `SMLERPIC/_icImportPicture.cs` | นำเข้ารูปภาพสินค้า (`menu_import_ic_picture`) |
| `SMLERPControl._imageTransfer` | `SMLERPControl/_imageTransfer.cs` | ย้ายรูปภาพสินค้า (`menu_tools_image_transfer`) |
| `_g._resource_viewer` | `SMLERPGlobal/_resource_viewer.cs` | แสดง Resource Language (`menu_resource_view`) |
| `SMLERPIC._icDescription` | `SMLERPIC/_icDescription.cs` | รายละเอียดสินค้า (`menu_ic_description`) |
| `SMLERPIC._icEditDetailFast` | `SMLERPIC/_icEditDetailFast.cs` | แก้ไขรายละเอียด(เร็ว) (`menu_ic_description_fast`) |
| `SMLERPIC._icBarcode` | `SMLERPIC/_icBarcode.cs` | กำหนดบาร์โค้ดสินค้า (`menu_ic_item_barcode`) |
| `SMLERPIC._icBarcodeDiscount` | `SMLERPIC/_icBarcodeDiscount.cs` | กำหนดส่วนลดตามบาร์โค๊ด (`menu_ic_item_barcode_discount`) |
| `SMLERPIC._icMultiBarcodeDiscount` | `SMLERPIC/_icMultiBarcodeDiscount.cs` | กำหนดส่วนลดตามบาร์โค๊ด (เร็ว) (`menu_ic_item_multibarcode_discount`) |
| `SMLERPIC._icSearchLevel` | `SMLERPIC/_icSearchLevel.cs` | กำหนดลำดับการค้นหา (`menu_ic_item_level`) |
| `SMLERPIC._icSearchLevelMultiItem` | `SMLERPIC/_icSearchLevelMultiItem.cs` | กำหนดลำดับการค้นหา (เร็ว) (`menu_ic_multi_item_level`) |
| `SMLERPIC._icMainDetailPicture` | `SMLERPIC/_icMainDetailPicture.cs` | กำหนดรูปภาพ (`menu_ic_item_picture`) |
| `SMLERPIC._icBarcodePicture` | `SMLERPIC/_icBarcodePicture.cs` | กำหนดรูปภาพตามบาร์โค้ด (`menu_ic_item_barcode_picture`) |
| `SMLERPIC._icPromotion._formula` | `SMLERPIC/_icPromotion/_formula.cs` | กำหนดสูตรโปรโมชั่น (`pos_promotion_formula`) |
| `SMLERPIC._icSerialNumber` | `SMLERPIC/_icSerialNumber.cs` | ทะเบียน Serial Number (`menu_ic_item_serial`) |
| `SMLERPIC._icMainProductSet` | `SMLERPIC/_icMainProductSet.cs` | สินค้าชุด (`menu_ic_item_set`) |
| `SMLERPIC._icAddBarcodeFastControl` | `SMLERPIC/_icAddBarcodeFastControl.cs` | เพิ่มบาร์โค๊ดสินค้าแบบเร็ว (`menu_ic_item_add_barcode_fast`) |
| `SMLERPIC._icUnitCheckerControl` | `SMLERPIC/_icUnitCheckerControl.cs` | ตรวจสอบสินค้าหลายหน่วยนับ (`menu_ic_unit_checker`) |
| `SMLERPIC._barcodeCheckerControl` | `SMLERPIC/_barcodeCheckerControl.cs` | ตรวจสอบบาร์โค๊ดจาก Text File (`menu_ic_item_barcode_checker`) |
| `SMLBarcodeManage._itemBarcodeCheckerEan13` | `SMLBarcodeManage/_itemBarcodeCheckerEan13.cs` | ตรวจสอบบาร์โค๊ดตามมาตรฐาน EAN13 (`menu_ic_item_barcode_checker_ean13`) |
| `SMLPOSControl._checkPriceUserControl` | `SMLPOSControl/_checkPriceUserControl.cs` | ตรวจสอบราคาสินค้า (`check_price`) |
| `SMLBarcodeManage._itemBarcodePrint` | `SMLBarcodeManage/_itemBarcodePrint.cs` | พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป (`menu_ic_item_barcode_laser_print`) |
| `SMLERPIC._icSpecificSearch` | `SMLERPIC/_icSpecificSearch.cs` | กำหนดการค้นหาแบบเฉพาะเจาะจง (`menu_ic_specific_search`) |
| `SMLERPIC._icWarehouseLocation` | `SMLERPIC/_icWarehouseLocation.cs` | คลังที่เก็บสินค้า (`menu_ic_warehouse_locaton`) |
| `SMLERPIC._whLocationGroup` | `SMLERPIC/_whLocationGroup.cs` | กำหนดกลุ่มที่เก็บ (`ic_warehouse_and_location_group`) |
| `SMLERPICReport._report_ic_master` | `SMLERPICReport/_report_ic_master.cs` | รายงานรายละเอียดสินค้า (`menu_ic_detail`) |
| `SMLERPICReport._report_item_set_formula` | `SMLERPICReport/_report_item_set_formula.cs` | รายงานสินค้าชุด (`menu_ic_report_item_set_formula`) |
| `SMLERPICReport._report_ic_barcode` | `SMLERPICReport/_report_ic_barcode.cs` | รายงานบาร์โค้ดสินค้า (`menu_ic_report_item_barcode`) |
| `SMLERPIC._icModifyPrice` | `SMLERPIC/_icModifyPrice.cs` | ปรับราคาสินค้า (`menu_ic_modify_price`) |
| `SMLInventoryControl._icPurchasePrice._icPriceList` | `SMLInventoryControl/_icPurchasePrice/_icPriceList.cs` | กำหนดราคาซื้อ (`menu_ic_purchase_price`) |
| `SMLERPIC._icPurchasePermium` | `SMLERPIC/_icPurchasePermium.cs` | ของแถมซื้อ (`menu_ic_purchase_premium`) |
| `SMLInventoryControl._icPrice._icDiscount` | `SMLInventoryControl/_icPrice/_icDiscount.cs` | กำหนดส่วนลดสินค้า (`menu_ic_discount`) |
| `SMLInventoryControl._icPrice._icPriceFormulaTemplate` | `SMLInventoryControl/_icPrice/_icPriceFormulaTemplate.cs` | กำหนดรูปแบบสูตรราคาขาย (`menu_ic_item_formula_template`) |
| `SMLInventoryControl._icPrice._icPriceFormula` | `SMLInventoryControl/_icPrice/_icPriceFormula.cs` | กำหนดสูตรราคาขาย (`menu_ic_item_saleprice_formula`) |
| `SMLInventoryControl._icPrice._icAllPrice` | `SMLInventoryControl/_icPrice/_icAllPrice.cs` | ราคาขายสินค้า (`menu_ic_all_price`) |
| `SMLERPICReport._report_ic_purchase_price` | `SMLERPICReport/_report_ic_purchase_price.cs` | รายงานราคาซื้อสินค้า (`menu_ic_report_item_purchase_price`) |
| `IMEXControl.QualityControl.ICQCProductReceive` | `IMEXControl/QualityControl/ICQCProductReceive.cs` | บันทึกรับสินค้า (`menu_ic_qc_receive`) |
| `IMEXControl.QualityControl.ICQCLabList` | `IMEXControl/QualityControl/ICQCLabList.cs` | ทะเบียนการตรวจสอบคุณภาพ (`menu_ic_qc_lab_list`) |
| `SMLInventoryControl._icTransLabelPrintControl` | `SMLInventoryControl/_icTransLabelPrint/_icTransLabelPrintControl.cs` | พิมพ์แท็กสินค้า (`menu_print_tag_label`) |
| `IMEXControl.QualityControl.QCLatInformation.LabInformation` | `IMEXControl/QualityControl/QCLatInformation/LabInformation.cs` | Lab Information (`menu_imex_qc_lab_information`) |
| `SMLERPIC._icSerialStockCheck` | `SMLERPIC/_icSerialStockCheck.cs` | ตรวจสอบสินค้า Serial Number (`menu_ic_serialnumber_checker`) |
| `SMLInventoryControl._stockAutoAdjustControl` | `SMLInventoryControl/_stockAutoAdjustControl.cs` | ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ (`menu_ic_stk_adjust_auto`) |
| `SMLInventoryControl.StockLotAdjustmentForm` | `SMLInventoryControl/StockLotAdjustmentForm.cs` | ปรับปรุงมูลค่าสินค้า Lot คงค้าง (`menu_ic_adjust_stock_lot_amount`) |
| `SMLERPICInfo._stkBalance` | `SMLERPICInfo/_stkBalance.cs` | ยอดคงเหลือสินค้า (`menu_ic_info_stk_balance`) |
| `SMLERPICInfo._stkBalanceWareHouse` | `SMLERPICInfo/_stkBalanceWareHouse.cs` | ยอดคงเหลือสินค้าตามคลัง (`menu_ic_info_stk_balance_warehouse`) |
| `SMLERPICInfo._stkBalanceLocation` | `SMLERPICInfo/_stkBalanceLocation.cs` | ยอดคงเหลือสินค้าตามที่เก็บ (`menu_ic_info_stk_balance_shelf`) |
| `SMLERPICInfo._stkBalanceByLot` | `SMLERPICInfo/_stkBalanceByLot.cs` | ยอดคงเหลือสินค้าตาม LOT (`menu_ic_info_stk_balance_lot`) |
| `SMLInventoryControl._stkReorder` | `SMLInventoryControl/_stkReorder.cs` | สินค้าถึงจุดสั่งซื้อ (`menu_ic_info_stk_reorder`) |
| `SMLERPICInfo._stkNoMovement` | `SMLERPICInfo/_stkNoMovement.cs` | สินค้าที่ไม่มีการเคลื่อนไหว (`menu_ic_info_product_no_movement`) |
| `SMLERPICInfo._icSerialAnalyze` | `SMLERPICInfo/_icSerialAnalyze.cs` | ตรวจสอบ Serial มีปัญหา (`menu_ic_serial_analyze`) |
| `SMLERPICReport.ic_analysis._report_ic_stk_reorder` | `SMLERPICReport/ic_analysis/_report_ic_stk_reorder.cs` | รายงานสินค้าที่ถึงจุดสั่งซื้อ (`menu_ic_report_info_stk_reorder`) |
| `SMLERPICReport._report_ic_none_movement` | `SMLERPICReport/_report_ic_none_movement.cs` | รายงานสินค้าที่ไม่มีการเคลื่อนไหว (`menu_item_non_transfer`) |
| `SMLERPICReport._report_ic_info_stk_movement_sum` | `SMLERPICReport/_report_ic_info_stk_movement_sum.cs` | รายงานสรุปเคลื่อนไหวปริมาณสินค้า (`menu_result_transfer_item`) |
| `SMLERPICReport.ic_analysis._report_info_stk_profit_by_doc_and_discount` | `SMLERPICReport/ic_analysis/_report_info_stk_profit_by_doc_and_discount.cs` | รายงานกำไรขั้นต้นตามเอกสาร (แสดงส่วนลด) (`menu_ic_report_info_stk_profit_by_doc_and_discount`) |
| `SMLERPIC._icRecalc` | `SMLERPIC/_icRecalc.cs` | คำนวณยอดสต๊อกใหม่ (`menu_ic_recalc`) |
| `SMLERPIC._icDocPicture` | `SMLERPIC/_icDocPicture.cs` | บันทึกรูปภาพเอกสาร (`menu_ic_document_picture`) |
| `SMLERPIC._icLotManage` | `SMLERPIC/_icLotManage.cs` | จัดการ LOT สินค้า (`menu_ic_lot_manage`) |
| `SMLERPPO._po_advance_money_balance` | `SMLERPPO/_po_advance_money_balance.cs` | จ่ายเงินล่วงหน้ายกมา (`menu_po_advance_payment_balance`) |
| `SMLERPPO._po_advance_money` | `SMLERPPO/_po_advance_money.cs` | จ่ายเงินล่วงหน้า (`menu_po_deposit_payment_1`) |
| `SMLERPPO._po_advance_money_return` | `SMLERPPO/_po_advance_money_return.cs` | รับคืนจ่ายเงินล่วงหน้า (`menu_po_deposit_return_1`) |
| `SMLERPPO._po_deposit_money_balance` | `SMLERPPO/_po_deposit_money_balance.cs` | จ่ายเงินมัดจำยกมา (`menu_po_deposit_money_balance`) |
| `SMLERPPO._po_deposit_money` | `SMLERPPO/_po_deposit_money.cs` | จ่ายเงินมัดจำ (`menu_po_deposit_payment_2`) |
| `SMLERPPO._po_deposit_money_return` | `SMLERPPO/_po_deposit_money_return.cs` | รับคืนจ่ายเงินมัดจำ (`menu_po_deposit_return_2`) |
| `SMLERPPO._po_docPicture` | `SMLERPPO/_po_docPicture.cs` | บันทึกรูปภาพเอกสาร (`menu_po_doc_picture`) |
| `SMLERPSO._soQuotation` | `SMLERPSO/_soQuotation.cs` | ใบเสนอราคา (`menu_so_quotation_order`) |
| `SMLERPSO._soQuotationApproval` | `SMLERPSO/_soQuotationApproval.cs` | อนุมัติใบเสนอราคา (`menu_so_quotation_approve`) |
| `SMLERPSO._soQuotationCancel` | `SMLERPSO/_soQuotationCancel.cs` | ยกเลิกใบเสนอราคา (`menu_so_quotation_cancel`) |
| `SMLERPSO._soReserved` | `SMLERPSO/_soReserved.cs` | ใบสั่งซื้อ/สั่งจอง (`menu_so_inquiry_order`) |
| `SMLERPSO._soReservedApproval` | `SMLERPSO/_soReservedApproval.cs` | อนุมัติใบสั่งซื้อ/สั่งจอง (`menu_so_inquiry_order_approve`) |
| `SMLERPSO._soReservedCancel` | `SMLERPSO/_soReservedCancel.cs` | ยกเลิกใบสั่งซื้อ/สั่งจอง (`menu_so_inquiry_order_cancel`) |
| `SMLERPSO._soSaleorderApproval` | `SMLERPSO/_soSaleorderApproval.cs` | อนุมัติใบสั่งขาย (`menu_so_sale_order_approve`) |
| `SMLERPSO._soSaleorderCancel` | `SMLERPSO/_soSaleorderCancel.cs` | ยกเลิกใบสั่งขาย (`menu_so_sale_order_cancel`) |
| `SMLERPSO._so_advance_money_balance` | `SMLERPSO/_so_advance_money_balance.cs` | รับเงินล่วงหน้ายกมา (`menu_so_advance_money_balance`) |
| `SMLERPSO._so_advance_money` | `SMLERPSO/_so_advance_money.cs` | รับเงินล่วงหน้า (`menu_so_deposit_receive_1`) |
| `SMLERPSO._so_advance_money_return` | `SMLERPSO/_so_advance_money_return.cs` | คืนเงินรับล่วงหน้า (`menu_so_deposit_return_1`) |
| `SMLERPSO._so_advance_money_cancel` | `SMLERPSO/_so_advance_money_cancel.cs` | ยกเลิกรับเงินล่วงหน้า (`menu_so_deposit_receive_1_cancel`) |
| `SMLERPSO._so_advance_money_return_cancel` | `SMLERPSO/_so_advance_money_return_cancel.cs` | ยกเลิกคืนเงินรับล่วงหน้า (`menu_so_deposit_return_1_cancel`) |
| `SMLERPSO._so_deposit_money_balance` | `SMLERPSO/_so_deposit_money_balance.cs` | รับเงินมัดจำยกมา (`menu_so_deposit_money_balance`) |
| `SMLERPSO._so_deposit_money` | `SMLERPSO/_so_deposit_money.cs` | รับเงินมัดจำ (`menu_so_deposit_receive_2`) |
| `SMLERPSO._so_deposit_money_return` | `SMLERPSO/_so_deposit_money_return.cs` | คืนเงินมัดจำ (`menu_so_deposit_return_2`) |
| `SMLERPSO._so_deposit_money_cancel` | `SMLERPSO/_so_deposit_money_cancel.cs` | ยกเลิกรับเงินมัดจำ (`menu_so_deposit_receive_2_cancel`) |
| `SMLERPSO._so_deposit_money_return_cancel` | `SMLERPSO/_so_deposit_money_return_cancel.cs` | ยกเลิกคืนเงินมัดจำ (`menu_so_deposit_return_2_cancel`) |
| `SMLERPSO._creditNote` | `SMLERPSO/_creditNote.cs` | รับคืนสินค้า/ลดหนี้ (`menu_so_credit_note`) |
| `SMLERPSO._soInvoiceAdd` | `SMLERPSO/_soInvoiceAdd.cs` | เพิ่มหนี้ (`menu_so_invoice_add`) |
| `SMLETaxInvoice._sendETaxControl` | `SMLETaxInvoice/_sendETaxControl.cs` | ส่งข้อมูล e-Tax (`menu_so_send_etax`) |
| `SMLERPSO._creditNoteCancel` | `SMLERPSO/_creditNoteCancel.cs` | ยกเลิกรับคืนสินค้า/ลดหนี้ (`menu_so_credit_note_cancel`) |
| `SMLERPSO._soInvoiceAddCancel` | `SMLERPSO/_soInvoiceAddCancel.cs` | ยกเลิกขายเพิ่มสินค้า/เพิ่มหนี้ (`menu_so_invoice_add_cancel`) |
| `SMLERPSOReport._report_summary._report_sell_by_sale` | `SMLERPSOReport/_report_summary/_report_sell_by_sale.cs` | รายงานสรุปการขายสินค้าตามพนักงานขาย (`menu_sell_by_sale`) |
| `SMLERPSOReport._report_sale_drug_13` | `SMLERPSOReport/_report_sale_drug_13.cs` | รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.13) (`menu_so_report_sale_drug_13`) |
| `SMLERPSOReport._report_sale_drug_recall` | `SMLERPSOReport/_report_sale_drug_recall.cs` | รายงานเรียกเก็บยาคืน (Recall) (`menu_so_report_sale_recall`) |
| `SMLERPSO._so_docPicture` | `SMLERPSO/_so_docPicture.cs` | บันทึกรูปภาพเอกสาร (`menu_so_doc_picture`) |
| `SMLERPControl._coupon._couponGenerate` | `SMLERPControl/_coupon/_couponGenerate.cs` | สร้างคูปองแบบเร็ว (`menu_coupon_generate`) |
| `SMLPosClient._posSaveMoneyReceive` | `SMLPosClient/_posSaveMoneyReceive.cs` | บันทึกรับเงิน (เงินทอน) (`menu_save_pos_receive_money`) |
| `SMLPosClient._posSaveSendMoney` | `SMLPosClient/_posSaveSendMoney.cs` | บันทึกส่งเงิน POS (`menu_save_send_money_pos`) |
| `SMLERPSO._soFullInvoice` | `SMLERPSO/_soFullInvoice.cs` | รายการใบกำกับภาษีอย่างเต็มออกแทน (`pos_full_invoide_list_pos`) |
| `SMLERPAP._ap` | `SMLERPAP/_ap.cs` | กำหนดเจ้าหนี้ (`menu_ap_detail`) |
| `SMLERPAP._ap_detail` | `SMLERPAP/_ap_detail.cs` | รายละเอียดเจ้าหนี้ (`menu_ap_detail_2`) |
| `SMLERPReportTool._reportCustMaster` | `SMLERPReportTool/_reportCustMaster.cs` | รายงานรายละเอียดเจ้าหนี้ (`menu_ap_report_detail_ap`) |
| `SMLERPAP._ap_debt_balance` | `SMLERPAP/_ap_debt_balance.cs` | ตั้งหนี้ยกมา (เจ้าหนี้) (`menu_ap_debt_balance`) |
| `SMLERPAP._ap_cn_balance` | `SMLERPAP/_ap_cn_balance.cs` | ลดหนี้ยกมา (เจ้าหนี้) (`menu_ap_cn_balance`) |
| `SMLERPAP._ap_increase_debt` | `SMLERPAP/_ap_increase_debt.cs` | เพิ่มหนี้ยกมา (เจ้าหนี้) (`menu_ap_increase_debt`) |
| `SMLERPAP._apPartnerBillImport` | `SMLERPAP/_apPartnerBillImport.cs` | นำเข้าข้อมูลจากคู่ค้า (`menu_ap_partner_import`) |
| `SMLERPAP._apPartnerBillImportReturnProduct` | `SMLERPAP/_apPartnerBillImportReturnProduct.cs` | นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) (`menu_ap_partner_import_return_product`) |
| `SMLERPAP._apPartnerBillImportAddDebt` | `SMLERPAP/_apPartnerBillImportAddDebt.cs` | นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้) (`menu_ap_partner_import_add_debt`) |
| `SMLERPAP._ap_pay_bill` | `SMLERPAP/_ap_pay_bill.cs` | ใบรับวางบิล (เจ้าหนี้) (`menu_ap_pay_bill`) |
| `SMLERPAP._ap_debt_billing` | `SMLERPAP/_ap_debt_billing.cs` | จ่ายชำระหนี้ (เจ้าหนี้) (`menu_ap_debt_billing`) |
| `SMLERPAP._ap_cancel_pay_bill` | `SMLERPAP/_ap_cancel_pay_bill.cs` | ยกเลิกใบรับวางบิล (เจ้าหนี้) (`menu_ap_cancel_pay_bill`) |
| `SMLERPAP._ap_cancel_debt_billing` | `SMLERPAP/_ap_cancel_debt_billing.cs` | ยกเลิกจ่ายชำระหนี้ (เจ้าหนี้) (`menu_ap_cancel_debt_billing`) |
| `SMLERPAP._ap_doc_picture` | `SMLERPAP/_ap_doc_picture.cs` | บันทึกรูปภาพเอกสาร (`menu_ap_doc_picture`) |
| `SMLERPAR._ar` | `SMLERPAR/_ar.cs` | กำหนดลูกหนี้ (`menu_ar_detail`) |
| `SMLERPAR._ar_detail` | `SMLERPAR/_ar_detail.cs` | รายละเอียดลูกหนี้ (`menu_ar_detail_2`) |
| `SMLERPAR._ar_dealer` | `SMLERPAR/_ar_dealer.cs` | รายละเอียดสมาชิก (`menu_ar_dealer`) |
| `SMLERPAR._ar_point_balance` | `SMLERPAR/_ar_point_balance.cs` | กำหนดแต้มคงเหลือยกมา (`menu_ar_point_balance`) |
| `SMLERPAR._ar_cut_point` | `SMLERPAR/_ar_cut_point.cs` | บันทึกตัดแต้ม (`menu_ar_cut_point`) |
| `SMLERPAR.ar_point` | `SMLERPAR/ar_point.cs` | แต้มสะสม (`menu_ar_point`) |
| `SMLERPAR.ar_point_recal` | `SMLERPAR/ar_point_recal.cs` | คำณวนแต้มสะสม (`menu_ar_point_recal`) |
| `SMLERPReport.ar._report_ar_detail` | `SMLERPReport/ar/_report_ar_detail.cs` | รายงานรายละเอียดลูกค้า-ตามรหัสลูกค้า (`menu_ar_report_detail_ar`) |
| `SMLERPARReport.report._ar_report` | `SMLERPARReport/report/_ar_report.cs` | รายงานแต้มคงเหลือลูกหนี้ (`menu_report_point_balance`) |
| `SMLERPAR._ar_debt_balance` | `SMLERPAR/_ar_debt_balance.cs` | ตั้งหนี้ยกมา (ลูกหนี้) (`menu_ar_debt_balance`) |
| `SMLERPAR._ar_increase_debt` | `SMLERPAR/_ar_increase_debt.cs` | เพิ่มหนี้ยกมา (ลูกหนี้) (`menu_ar_increase_debt`) |
| `SMLERPAR._ar_cn_balance` | `SMLERPAR/_ar_cn_balance.cs` | ลดหนี้ยกมา (ลูกหนี้) (`menu_ar_cn_balance`) |
| `SMLERPAR._ar_pay_bill` | `SMLERPAR/_ar_pay_bill.cs` | ใบวางบิล (ลูกหนี้) (`menu_ar_pay_bill`) |
| `SMLERPAR._ar_bill_collector` | `SMLERPAR/_ar_bill_collector.cs` | Bill Collector (`menu_imex_bill_collector`) |
| `SMLERPAR._ar_debt_billing` | `SMLERPAR/_ar_debt_billing.cs` | รับชำระหนี้/ออกใบเสร็จรับเงิน (`menu_ar_debt_billing`) |
| `SMLERPAR._ar_cancel_pay_bill` | `SMLERPAR/_ar_cancel_pay_bill.cs` | ยกเลิกใบวางบิล (ลูกหนี้) (`menu_ar_cancel_pay_bill`) |
| `SMLERPAR._ar_cancel_debt_billing` | `SMLERPAR/_ar_cancel_debt_billing.cs` | ยกเลิกชำระหนี้/ยกเลิกใบเสร็จรับเงิน (`menu_ar_cancel_debt_billing`) |
| `SMLERPReport.ar._report_ar_receipt_and_detail` | `SMLERPReport/ar/_report_ar_receipt_and_detail.cs` | รายงายใบเสร็จรับเงินพร้อมรายการย่อย (`menu_ar_report_receipt_and_detail`) |
| `SMLERPReport.ar._report_ar_check_balance` | `SMLERPReport/ar/_report_ar_check_balance.cs` | รายงานตรวจสอบยอดวงเงิน (`menu_ar_report_check_balance`) |
| `SMLERPAR._ar_doc_picture` | `SMLERPAR/_ar_doc_picture.cs` | บันทึกรูปภาพเอกสาร (`menu_ar_doc_picture`) |
| `SMLERPConfig._book` | `SMLERPConfig/_book.cs` | กำหนดสมุดเงินฝาก (`menu_book_bank`) |
| `SMLERPCASHBANK._cb_chq_in_receive_master` | `SMLERPCASHBANK/_cb_chq_in_receive_master.cs` | ทะเบียนเช็ครับ (`menu_cb_chq_in_receive_master`) |
| `SMLERPReport.Cheque_Card._report_chq_card_Disposit_Cheque_Detail` | `SMLERPReport/Cheque_Card/_report_chq_card_Disposit_Cheque_Detail.cs` | รายงานใบนำฝากเช็ครับพร้อมรายการย่อย (`menu_report_chq_card_disposit_cheque_detail`) |
| `SMLERPCASHBANK._cb_chq_out_payment_master` | `SMLERPCASHBANK/_cb_chq_out_payment_master.cs` | ทะเบียนเช็คจ่าย (`menu_cb_chq_out_payment_master`) |
| `SMLERPCASHBANK._cb_credit_master` | `SMLERPCASHBANK/_cb_credit_master.cs` | ทะเบียนบัตรเครดิต (`menu_cb_credit_card_receive`) |
| `SMLERPCASHBANKReport._cashbank_report` | `SMLERPCASHBANKReport/_cashbank_report.cs` | รายงานเคลื่อนไหวเงินสด (`_menu_cash_movements`) |
| `SMLERPReport.cash_bank.Received_Cash_sub_item` | `SMLERPReport/cash_bank/Received_Cash_sub_item.cs` | รายงานการรับเงินอื่นๆพร้อมรายการย่อย (`_menu_received_cash_sub_item`) |
| `SMLERPReport.cash_bank._bankStatment` | `SMLERPReport/cash_bank/_bankStatment.cs` | รายงาน Bank Statement (`_menu_bank_statement`) |
| `SMLERPCASHBANK._cb_doc_picture` | `SMLERPCASHBANK/_cb_doc_picture.cs` | บันทึกรูปภาพเอกสาร (`menu_cb_doc_picture`) |
| `SMLERPASSET._as_list` | `SMLERPASSET/_as_list.cs` | ข้อมูลสินทรัพย์ (`menu_asset_lists`) |
| `SMLERPASSET._as_list_pic` | `SMLERPASSET/_as_list_pic.cs` | กำหนดรูปภาพ (`menu_asset_picture`) |
| `SMLERPASSET._as_maintain` | `SMLERPASSET/_as_maintain.cs` | บันทึกการซ่อมบำรุงสินทรัพย์ (`menu_asset_maintenance`) |
| `SMLERPASSET._display._depreciateByDay` | `SMLERPASSET/_display/_depreciateByDay.cs` | แสดงค่าเสื่อมราคาสินทรัพย์รายวัน (`menu_show_asset_byday`) |
| `SMLERPASSET._display._depreciateByMonth` | `SMLERPASSET/_display/_depreciateByMonth.cs` | แสดงค่าเสื่อมราคาสินทรัพย์รายเดือน (`menu_show_asset_bymonth`) |
| `SMLERPASSET._display._depreciateByYear` | `SMLERPASSET/_display/_depreciateByYear.cs` | แสดงค่าเสื่อมราคาสินทรัพย์รายปี (`menu_show_asset_byyear`) |
| `SMLERPASSET._as_transfer` | `SMLERPASSET/_as_transfer.cs` | โอนข้อมูลเข้าระบบบัญชี (`menu_asset_transfers`) |
| `SMLERPASSET._report._asset._report` | `SMLERPASSET/_report/_asset/_report.cs` | รายงานรายละเอียดสินทรัพย์ (`menu_asset_report_list`) |
| `SMLERPASSET._report._depreciate._report` | `SMLERPASSET/_report/_depreciate/_report.cs` | รายงานค่าเสื่อมราคาสินทรัพย์ (`menu_asset_report_depreciate`) |
| `SMLERPASSET._report._maintain._report` | `SMLERPASSET/_report/_maintain/_report.cs` | รายงานการซ่อมบำรุงสินทรัพย์ (`menu_asset_report_maintain`) |
| `SMLERPGL._chart._chartOfAccount` | `SMLERPGL/_chart/_chartOfAccount.cs` | รายละเอียดผังบัญชี (`menu_chart_of_account`) |
| `SMLERPGL._chart._chatOfAccountFlow` | `SMLERPGL/_chart/_chatOfAccountFlow.cs` | ตรวจสอบโครงสร้างผังบัญชี (`menu_chart_of_account_flow`) |
| `SMLERPGL._report._chartOfAccount._report` | `SMLERPGL/_report/_chartOfAccount/_report.cs` | รายงานรายละเอียดผังบัญชี (`menu_report_chart_of_account`) |
| `SMLERPGL._journalEntryAccount` | `SMLERPGL/_journalEntryAccount.cs` | ข้อมูลรายวัน (`menu_gl_journal`) |
| `SMLERPGL._journalEntryFast` | `SMLERPGL/_journalEntryFast.cs` | บันทึกข้อมูลรายวันแบบเร็ว (`menu_gl_journal_fast`) |
| `SMLERPGL._journalEntryAccount_pic` | `SMLERPGL/_journalEntryAccount_pic.cs` | บันทึกรูปภาพ (`menu_gl_picture`) |
| `SMLERPGL._transProcessUserControl` | `SMLERPGL/_transProcessUserControl.cs` | ประมวลผลจากข้อมูลรายวัน (`menu_gl_process`) |
| `SMLERPGL._checkData` | `SMLERPGL/_checkData.cs` | ตรวจสอบความถูกต้อง (`menu_gl_check_data`) |
| `SMLERPGL._journalPass` | `SMLERPGL/_journalPass.cs` | ผ่านรายการ (`menu_gl_journal_pass`) |
| `SMLERPGL._journalPassUndo` | `SMLERPGL/_journalPassUndo.cs` | ยกเลิกผ่านรายการ (`menu_gl_journal_pass_cancel`) |
| `SMLERPGL._display._glList` | `SMLERPGL/_display/_glList.cs` | แสดงบัญชีแยกประเภท (`menu_gl_show_sheet`) |
| `SMLERPGL._display._glListSum` | `SMLERPGL/_display/_glListSum.cs` | แสดงบัญชีแยกประเภท (แบบสรุป) (`menu_gl_show_sheet_sum`) |
| `SMLERPGL._report._journalSum._report` | `SMLERPGL/_report/_journalSum/_report.cs` | รายงานข้อมูลรายวันแบบสรุป (`menu_gl_report_journal_sum`) |
| `SMLERPGL._report._sheet._report` | `SMLERPGL/_report/_sheet/_report.cs` | รายงานบัญชีแยกประเภท (`menu_gl_report_sheet`) |
| `SMLERPGL._report._sheetSum._report` | `SMLERPGL/_report/_sheetSum/_report.cs` | รายงานบัญชีแยกประเภท (แบบสรุป) (`menu_gl_report_sheet_sum`) |
| `SMLERPGL._tax._vatSale` | `SMLERPGL/_report/_tax/_vatSale.cs` | รายงานภาษีขายรูปแบบใหม่อัตราภาษีศูนย์ (เพิ่มรายละเอียด) (`menu_report_except_vat_sale_with_tax_add_detail`) |
| `SMLERPGL._tax._vatBuyNewType1` | `SMLERPGL/_report/_tax/_vatBuyNewType1.cs` | รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 1) (`menu_report_except_vat_buy_type1`) |
| `SMLERPGL._tax._vatBuyNewType2` | `SMLERPGL/_report/_tax/_vatBuyNewType2.cs` | รายงานภาษีชื้อ(รุบแบบใหม่-แบบที่ 2) (`menu_report_except_vat_buy_type2`) |
| `SMLERPGL._tax._whtExport` | `SMLERPGL/_report/_tax/_whtExport.cs` | ส่งออกข้อมูลภาษีหัก ณ ทีจ่าย (`menu_export_wht`) |
| `SMLERPGL._display._glTrialBalance` | `SMLERPGL/_display/_glTrialBalance.cs` | แสดงงบทดลอง (`menu_gl_show_trial_balance`) |
| `SMLERPGL._analysis._trialBalance` | `SMLERPGL/_analysis/_trialBalance.cs` | แสดงงบทดลอง (มิติ) (`menu_gl_analysis_trial_balance`) |
| `SMLERPGL._display._glWorkSheet` | `SMLERPGL/_display/_glWorkSheet.cs` | แสดงกระดาษทำการ (`menu_gl_show_work_sheet`) |
| `SMLERPGL.LostAndProfit._display_lost_and_profit_compare_dimension` | `SMLERPGL/LostAndProfit/_display_lost_and_profit_compare_dimension.cs` | งบกำไรขาดทุน เปรียบเทียบ (`menu_display_lost_and_profit_compare_dimension`) |
| `SMLERPGL.AccountCloseWizard.JournalCloseAccountControl` | `SMLERPGL/AccountCloseWizard/JournalCloseAccountControl.cs` | ประมวลผลกำไร/ขาดทุน และต้นทุนขาย (`menu_close_account_process`) |
| `SMLMIS.calendar_trans` | `SMLMIS/calendar_trans.cs` | จำนวนรายการรายวัน (`menu_mis_calendar_trans`) |
| `SMLERPSO._saleInformation` | `SMLERPSO/_saleInformation.cs` | Sale  Information (`menu_sale_information`) |
| `SMLERPICInfo._ic_inventory_information` | `SMLERPICInfo/_ic_inventory_information.cs` | Inventory Information (`menu_ic_information`) |
| `SMLERPICInfo._ic_inventory_information_2` | `SMLERPICInfo/_ic_inventory_information_2.cs` | หน้าจอสำหรับผู้บริหาร (`menu_ic_information_manager`) |
| `SMLERPPO._buyInformation` | `SMLERPPO/_buyInformation.cs` | Buy Information (`menu_buy_information`) |
| `SMLEDIControl._ediExternal` | `SMLEDIControl/_ediExternal.cs` | รายละเอียดลูกค้า EDI (`menu_edi_external`) |
| `SMLEDIControl._ediExport` | `SMLEDIControl/_ediExport.cs` | ส่งออกข้อมูล EDI (`menu_edi_export`) |
| `SMLERPICReport._icReportSort` | `SMLERPICReport/_icReportSort.cs` | กำหนดการเรียงข้อมูลรายงาน (`menu_ic_report_sort`) |
| `SMLPPShipment._shipment` | `SMLPPShipment/_shipment.cs` | บันทึกการส่งสินค้า (`menu_shipment_load`) |
| `SMLERPTransferControl._saleImportFromStockCountDiff` | `SMLERPTransferControl/_saleImportFromStockCountDiff.cs` | สร้างการขายจากผลต่างจากการตรวจนับ (`menu_import_sale_from_stock_count_diff`) |
| `SMLERPTransferControl._saleImportFromPOSSaleReport` | `SMLERPTransferControl/_saleImportFromPOSSaleReport.cs` | สร้างรายการขายจากสรุปการขาย POS (`menu_imort_sale_from_pos_sale_report`) |
| `SMLERPTransferControl._salesItemsFromPurchaseBill` | `SMLERPTransferControl/_salesItemsFromPurchaseBill.cs` | สร้างรายการขายจาก บิลซื้อ (`menu_imort_sale_from_purchase_bill`) |
| `SMLERPSO.mobillyst_tms._create_delivery_order` | `SMLERPSO/mobillyst_tms/_create_delivery_order.cs` | สร้างคำสั่งส่งสินค้า (`menu_mobillyst_create_delivery_order`) |

## MyLib._ManageTransData

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPControl._coupon._couponList` | `SMLERPControl/_coupon/_couponList.cs` | รายละเอียดคูปอง (`menu_coupon_list`), รายละเอียดคูปอง (`menu_coupon_list`) |
| `SMLERPConfig.qrpayment._config_qr_payment_control` | `SMLERPConfig/qrpayment/_config_qr_payment_control.cs` | กำหนดค่า QR Code Payment (`menu_setup_qr_payment`) |
| `SMLERPControl.pos_slip_campaign.pos_slip_campaign` | `SMLERPControl/pos_slip_campaign/pos_slip_campaign.cs` | กำหนดแคมเปญท้ายใบเสร็จ (`menu_setup_pos_slip_campaign`) |
| `IMEXControl.QualityControl.ICQCPurchaesPackingSizeSplit` | `IMEXControl/QualityControl/PackingSize/ICQCPurchaesPackingSizeSplit.cs` | กำหนดจำนวนภาชนะ(Container) (`menu_imex_qc_purchase_packing_size_container_assign`) |
| `IMEXControl.QualityControl.ICQCPassControl` | `IMEXControl/QualityControl/ICQCPassControl.cs` | บันทึกการตรวจสอบคุณภาพ - Pass (`menu_ic_qc_control_pass`) |
| `IMEXControl.QualityControl.ICQCRejectControl` | `IMEXControl/QualityControl/ICQCRejectControl.cs` | บันทึกการตรวจสอบคุณภาพ - Reject (`menu_ic_qc_control_reject`) |
| `IMEXControl.QualityControl.ICQCRetestControl` | `IMEXControl/QualityControl/ICQCRetestControl.cs` | บันทึกการตรวจสอบคุณภาพซ้ำ (ReTest) (`menu_ic_qc_retest`) |
| `IMEXControl.QualityControl.LabBeginningBalance.QCLabBalance` | `IMEXControl/QualityControl/LabBeginningBalance/QCLabBalance.cs` | บันทึก Lab Container ยกมา (`menu_qc_lab_beginning_balance`) |
| `IMEXControl.QualityControl.ProductContainerIssue._productContainerIssueControl` | `IMEXControl/QualityControl/ProductContainerIssue/_productContainerIssueControl.cs` | บันทึกเบิก Container (`menu_imex_qc_container_issue`) |
| `IMEXControl.QualityControl.ProductContainerAdjustment._productContainerAdjustmentControl` | `IMEXControl/QualityControl/ProductContainerAdjustment/_productContainerAdjustmentControl.cs` | บันทึกปรับปรุง Container (`menu_imex_qc_container_adjustment`) |
| `IMEXControl.QualityControl.QCLabCut._qcLabCutControl` | `IMEXControl/QualityControl/QCLabCut/_qcLabCutControl.cs` | บันทึกการตัดจากระบบ weighing System (`menu_qc_lab_cut`) |
| `IMEXControl.QualityControl._approvedVendorControl` | `IMEXControl/QualityControl/_approvedVendorControl.cs` | อนุมัติผู้จำหน่ายและสินค้า (`menu_qc_approved_vendor`) |
| `SMLERPIC._icHiddenCost._icHiddenCostProcess` | `SMLERPIC/_icHiddenCost/_icHiddenCostProcess.cs` | ประมวลผลเฉลี่ยต้นทุนแฝง (`menu_ic_hidden_cost_process`) |
| `SMLERPCASHBANK._cb_cash_balance` | `SMLERPCASHBANK/_cb_cash_balance.cs` | ยกมาเงินสด (`menu_cb_cash_balance`) |
| `SMLERPCASHBANK._cb_bank_balance` | `SMLERPCASHBANK/_cb_bank_balance.cs` | เงินฝากธนาคารยกมา (`menu_cb_bank_balance`) |
| `SMLERPGL.JournalProductSaleCost._journalProductSaleCostControl` | `SMLERPGL/JournalProductSaleCost/_journalProductSaleCostControl.cs` | สรุปบัญชีสินค้าและต้นทุนขาย (`menu_product_sale_cost_close`) |
| `SMLERPGL.JournalSummary.JournalSummaryControl` | `SMLERPGL/JournalSummary/JournalSummaryControl.cs` | สรุปยอดบัญชี (`menu_journal_summary`) |
| `SMLERPSO.mobillyst_tms._delivery_order_list` | `SMLERPSO/mobillyst_tms/_delivery_order_list.cs` | รายการสั่งส่งสินค้า (`menu_mobillyst_delivery_order_list`) |

## SMLReport._report._viewReport

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` | `SMLERPGL/_report/_report_lao_balance_sheet/_report_lao_balance_sheet.cs` | รายงานงบทดลอง (มาตรฐาน) (`menu_gl_report_trial_balance`), รายงานงบทดลอง (มาตรฐาน) (`menu_gl_report_trial_balance`) |
| `SMLERPICReport._report_ic_product_and_material` | `SMLERPICReport/_report_ic_product_and_material.cs` | รายงานสินค้าและวัตถุดิบ (`menu_report_ic_product_and_material`) |
| `SMLERPICReport._report_ic_info_stk_movement_sum_show_amount` | `SMLERPICReport/_report_ic_info_stk_movement_sum_show_amount.cs` | รายงานสรุปเคลื่อนไหวปริมาณสินค้า-แสดงมูลค่า (`menu_report_ic_info_stk_movement_sum_show_amount`) |
| `IMEXControl.report.report_product_sale_monthly` | `IMEXControl/report/report_product_sale_monthly.cs` | รายงานสินค้า ขายประจำเดือน (`menu_report_product_sale_monthly`) |
| `IMEXControl.report.report_billing_note_by_customer_cashier` | `IMEXControl/report/report_billing_note_by_customer_cashier.cs` | รายงานใบวางบิลตามพนักงานเก็บเงิน (`menu_report_billing_note_by_customer_cashier`) |
| `IMEXControl.report._reportARStatement` | `IMEXControl/report/_reportARStatement.cs` | รายงาน Statement ลูกหนี้ (`menu_report_imex_ar_statement`) |
| `IMEXControl.report._report_chq_receive_by_status` | `IMEXControl/report/_report_chq_receive_by_status.cs` | รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม (`imex_report_cheque_received_by_date_by_status`) |
| `IMEXControl.report._report_chq_receive_status_by_date` | `IMEXControl/report/_report_chq_receive_status_by_date.cs` | รายงานรายละเอียดเช็ครับ - ตามวันที่ - ตามสถานะเช็ค แสดงยอดรวม (`menu_imex_report_chqreceive_status_by_date`) |
| `IMEXControl.report._report_chq_receive_status_by_date_2` | `IMEXControl/report/_report_chq_receive_status_by_date_2.cs` | รายงานรายละเอียดเช็ครับ - ตามสถานะเช็ค แสดงยอดรวม(ไม่รวมเช็คคืน,เช็คคืนตั้งหนี้ใหม่) (`menu_imex_report_chqreceive_status_by_date_only_hand`) |
| `IMEXControl.report._report_chq_receive_last_status_by_date` | `IMEXControl/report/_report_chq_receive_last_status_by_date.cs` | รายงานรายละเอียดเช็ครับ - ณ วันที่ (`menu_imex_report_chq_receive_at_date`) |
| `IMEXControl.report.report_chq_pay_by_status` | `IMEXControl/report/report_chq_pay_by_status.cs` | รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม (`imex_report_cheque_pay_by_date_by_status`) |
| `IMEXControl.report._report_chq_pay_status_by_date` | `IMEXControl/report/_report_chq_pay_status_by_date.cs` | รายงานรายละเอียดเช็คจ่าย - ตามวันที่ - ตามสถานะเช็ค (`imex_report_cheque_pay_status_by_date`) |
| `IMEXControl.report._report_chq_pay_last_status_by_date` | `IMEXControl/report/_report_chq_pay_last_status_by_date.cs` | รายงานรายละเอียดเช็คจ่าย ณ วันที่ (`menu_imex_report_chq_pay_at_date`) |
| `SMLERPGL._report._report_journal_daily_lao._report_daily_journal_lao` | `SMLERPGL/_report/_report_journal_daily_lao/_report_daily_journal_lao.cs` | รายงานข้อมูลรายวัน (`menu_gl_report_journal`) |
| `SMLERPGL._report._tax._reportVatSale` | `SMLERPGL/_report/_tax/_reportVatSale.cs` | รายงานภาษีขาย (มาตรฐาน) (`menu_report_vat_sale_standard`) |
| `SMLERPGL._report._tax._reportVatBuy` | `SMLERPGL/_report/_tax/_reportVatBuy.cs` | รายงานภาษีซื้อ (มาตรฐาน) (`menu_report_vat_buy_standard`) |
| `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year` | `SMLERPGL/_report/_profit_and_lost_sum_year/_report_profit_and_lost_sum_year.cs` | งบกำไรขาดทุน (13 ช่อง) (`menu_report_profit_and_lost_sum_year`) |

## Form

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLTransportLabel._importTransportLabel` | `SMLTransportLabel/_importTransportLabel.cs` | นำเข้าที่อยู่จัดส่งเจ้าหนี้ (`menu_import_ap_transport_label`), นำเข้าที่อยู่จัดส่งลูกหนี้ (`menu_import_ar_transport_label`) |
| `SMLPOSControl._posPointPeriodForm` | `SMLPOSControl/_posPointPeriodForm.cs` | กำหนดเงื่อนไขสะสมแต้ม (`menu_pos_point_rate`) |
| `SMLPosClient._configPOSScreen` | `SMLPosClient/_configPOSScreen.cs` | กำหนดคุณสมบัติของเครื่อง POS (`menu_config_pos_screen`) |
| `_g._ic_add_warehouse_shelf_form` | `SMLERPGlobal/_ic_add_warehouse_shelf_form.cs` | เพิ่มคลังและพื้นที่เก็บอัตโนมัติ (`ic_auto_add_warehouse_and_location`) |
| `SMLPOSControl._posDownloadSound` | `SMLPOSControl/_posDownloadSound.cs` | Download ระบบเสียงพูด (`menu_pos_sound_download_install`) |
| `MyLib._databaseManage._dataBackupForm` | `MyLib/_databaseManage/_dataBackupForm.cs` | สำรองข้อมูล (`data_backup`) |
| `MyLib._databaseManage._dataRestoreForm` | `MyLib/_databaseManage/_dataRestoreForm.cs` | นำข้อมูลสำรองกลับมาใช้ (`data_restore`) |
| `MyLib._databaseManage._smlChangePassword` | `MyLib/_databaseManage/_smlChangePassword.cs` | เปลี่ยนรหัสผ่าน (`menu_change_password`) |
| `SMLERPControl._importFromImageForm` | `SMLERPControl/_importFromImageForm.cs` | นำเข้าข้อมูลจากรูปภาพ (`menu_import_from_image`) |
| `IMEXControl.QualityControl._qcConfigScreen` | `IMEXControl/QualityControl/_qcConfigScreen.cs` | กำหนดค่าระบบตรวจสอบคุณภาพ (`menu_imex_qc_config`) |
| `SMLFastReport._loadForm` | `SMLFastReport/_loadForm.cs` | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `SMLERPAPARControl._importDebtBilling` | `SMLAPARControl/_importDebtBilling.cs` | Import File Cash Received Account Receivable (`menu_debt_import`) |

## MyLib._myForm

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPConfig._companyProfile` | `SMLERPConfig/_companyProfile.cs` | กำหนดรายละเอียดบริษัท (`menu_company_profile`) |
| `SMLERPConfig._option` | `SMLERPConfig/_option.cs` | กำหนดข้อเลือกพิเศษต่างๆ (`menu_option`) |
| `SMLPOSControl._posConfig` | `SMLPOSControl/_posConfig.cs` | กำหนดค่าเริ่มต้น POS (`menu_config_pos_startup`) |
| `SMLERPControl.ARCreditPayBillForm` | `SMLERPControl/ARCreditPayBillForm.cs` | กำหนดวันครบกำหนดชำระเงิน (`menu_ar_credit_pay_bill`) |
| `SMLERPConfig._accountPeriod._accountPeriod` | `SMLERPConfig/_accountPeriod/_accountPeriodMain.cs` | กำหนดงวดบัญชี (`menu_account_period`) |
| `MyLib._databaseManage._verifyDatabase` | `MyLib/_databaseManage/_verifyDatabase.cs` | ตรวจสอบโครงสร้างฐานข้อมูล (`menu_verify_database`) |
| `MyLib._databaseManage._shrinkDatabase` | `MyLib/_databaseManage/_shrinkDatabase.cs` | ลดขนาดข้อมูล (`menu_shink_database`) |

## MyLib._manageMasterCodeFull

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `_g._docFormat` | `SMLERPGlobal/_docFormat.cs` | กำหนดรูปแบบเลขที่เอกสาร (`menu_setup_doc_format`) |
| `SMLERPAP.ap_supplier_connected` | `SMLERPAP/ap_supplier_connected.cs` | ข้อมูลคู่ค้า (`menu_ap_partner_detail`) |
| `SMLERPAR.ar_customer_connected` | `SMLERPAR/ar_customer_connected.cs` | ข้อมูลคู่ค้า(ลูกหนี้) (`menu_ar_customer_connected`) |

## _create_delivery_order

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPSO.mobillyst_tms._create_cn_delivery_order` | `SMLERPSO/mobillyst_tms/_create_cn_delivery_order.cs` | สร้างคำสั่งส่ง-จากการรับคืนสินค้า (`menu_mobillyst_create_cn_delivery_order`) |
| `SMLERPSO.mobillyst_tms._create_transfer_delivery_order` | `SMLERPSO/mobillyst_tms/_create_transfer_delivery_order.cs` | สร้างคำสั่งส่ง-จากการโอนสินค้า (`menu_mobillyst_create_tr_delivery_order`) |
| `SMLERPSO.mobillyst_tms._create_po_delivery_order` | `SMLERPSO/mobillyst_tms/_create_po_delivery_order.cs` | สร้างคำสั่งส่ง-จากการสั่งซื้อสินค้า (`menu_mobillyst_create_po_delivery_order`) |

## MyLib._dialogConfigForm

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPConfig._edcConfigForm` | `SMLERPConfig/_edcConfigForm.cs` | กำหนดค่าเครื่องรูดบัตรเครดิต (`menu_edc_config`) |
| `SMLERPConfig._usbQRDisplayConfigForm` | `SMLERPConfig/_usbQRDisplayConfigForm.cs` | กำหนดค่าจอแสดงผล QR Code (`menu_usb_qr_display_config`) |

## _report_lao_balance_sheet._report_lao_balance_sheet

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPGL._report._report_balancesheet_asset_lao._report_balancesheet_asset_lao` | `SMLERPGL/_report/_report_balancesheet_asset_lao/_report_balancesheet_asset_lao.cs` | งบดุลหลังปรับปรุง (`menu_gl_report_balancesheet_asset_lao`) |
| `SMLERPGL._report._report_balancesheet_profit_and_lost_lao._report_balancesheet_profit_and_lost_lao` | `SMLERPGL/_report/_report_balancesheet_profit_and_lost_lao/_report_balancesheet_profit_and_lost_lao.cs` | งบรายรับรายจ่าย (`menu_gl_report_profit_and_lost_lao`) |

## _itemCodeUserControl

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `_g._changeCode.changeChartOfAccountUserControl` | `SMLERPGlobal/_changeCode/changeChartOfAccountUserControl.cs` | เปลี่ยนรหัสผังบัญชี (`menu_change_gl_account_code`) |

## _stockAutoAdjustControl

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLInventoryControl._stockAutoAdjustLotControl` | `SMLInventoryControl/_stockAutoAdjustLotControl.cs` | ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ (สินค้า Lot) (`menu_ic_stk_adjust_lot_auto`) |

## (ไม่พบ base)

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `StreamReader` | `` | หน้าจอขาย POS (`menu_pos_screen`) |

## SMLInventoryControl._icTransControl

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPSO._saleAssets` | `SMLERPSO/_saleAssets.cs` | บันทึกการขายสินทรัพย์ (`menu_asset_sale`) |

## _IMyFrameWork

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `MyLib._myFrameWork` | `MyLib/_myFrameWork.cs` | ปรับปรุงผังบัญชีแบบเร็ว (`menu_chart_of_account_fast`) |

## _report_profit_and_lost_sum_year

| คลาส | ไฟล์ | เมนู |
|---|---|---|
| `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year_by_department` | `SMLERPGL/_report/_profit_and_lost_sum_year/_report_profit_and_lost_sum_year_by_department.cs` | งบกำไรขาดทุน (13 ช่อง) ตามแผนก (`menu_report_profit_and_lost_sum_year_by_department`) |
