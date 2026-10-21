---
tags: [sml, module, cashbank, generated]
menu_group: "เงินสด/ธนาคาร"
trans_flags: [1, 2, 250, 251, 252, 253, 254, 255, 260, 261, 262, 263, 264, 265, 300, 302, 303, 401, 402, 403, 404, 405, 406, 410, 411, 412, 413, 416, 418, 422, 423, 430, 431, 432, 433, 436, 451, 452, 453, 456, 461, 462, 471, 472, 473, 476]
---
# โมดูล: เงินสด/ธนาคาร

กลับไป [[modules-index]] · [[00-Index]]

## สรุปการทำงาน

- รายละเอียดเชิงลึก: [[cash-bank]]
- การรับ/จ่ายเงินเก็บใน `cb_trans` / `cb_trans_detail` โดยใช้ trans_flag ของเอกสารต้นทาง; ทะเบียนเช็ค `cb_chq_list`
- รายได้อื่น 250 / รายจ่ายอื่น 260 มีหัวเอกสารใน `ic_trans` ด้วย (ยืนยันกับ AOY)
- วงจรเช็ค: รับ/จ่าย, ฝาก (410), ผ่าน (411/451), คืน, เปลี่ยนเช็ค — มีสถานะละเอียด เหมาะกับพยากรณ์กระแสเงินสด
- control ส่วนกลาง `SMLERPControl._bank._bankControl`

## ตัวเลข

- เมนูปลายทาง 128 รายการ, จับคู่คลาสได้ 122, เห็นใน SMLAccountPOSProfessional (edition 12) 114
- คลาสหน้าจอที่ใช้บ่อย: `SMLInventoryControl._clone_icTrans` (46), `SMLERPReportTool._reportCashBankTrans` (38), `SMLFastReport._designer` (13), `SMLERPCASHBANKReport._report_chq._chqCreditCardList` (3), `SMLERPReportTool._reportTrans` (2), `SMLERPCASHBANKReport._report_petty_cash` (2)
- control หลักที่ฝัง: `SMLInventoryControl._icTransControl` (46), `SMLERPCASHBANK.CashBalanceScreenTop` (1), `SMLERPCASHBANK.BankBalanceScreenTop` (1), `SMLERPControl._documentPicture` (1)

## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้

| trans_flag | ชื่อ | จำนวนเมนู |
|---|---|---|
| 1 | PoInvestigate | 1 |
| 2 | ซื้อ_เสนอซื้อ | 1 |
| 250 | เงินสดธนาคาร_รายได้อื่น | 2 |
| 251 | เงินสดธนาคาร_รายได้อื่น_ยกเลิก | 2 |
| 252 | เงินสดธนาคาร_รายได้อื่น_ลดหนี้ | 2 |
| 253 | เงินสดธนาคาร_รายได้อื่น_ลดหนี้_ยกเลิก | 2 |
| 254 | เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้ | 2 |
| 255 | เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้_ยกเลิก | 2 |
| 260 | เงินสดธนาคาร_รายจ่ายอื่น | 2 |
| 261 | เงินสดธนาคาร_รายจ่ายอื่น_ยกเลิก | 2 |
| 262 | เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้ | 2 |
| 263 | เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้_ยกเลิก | 2 |
| 264 | เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้ | 2 |
| 265 | เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้_ยกเลิก | 2 |
| 300 | เงินสดย่อย_เบิกเงินสดย่อย | 1 |
| 302 | เงินสดย่อย_เบิกเงินสดย่อย_ยกเลิก | 2 |
| 303 | เงินสดย่อย_รับคืนเงินสดย่อย_ยกเลิก | 2 |
| 401 | เงินสดธนาคาร_ฝากเงิน | 1 |
| 402 | เงินสดธนาคาร_ถอนเงิน | 1 |
| 403 | เงินสดธนาคาร_ฝากเงิน_ยกเลิก | 2 |
| 404 | เงินสดธนาคาร_ถอนเงิน_ยกเลิก | 2 |
| 405 | เงินสดธนาคาร_เช็ครับ_ยกมา | 2 |
| 406 | เงินสดธนาคาร_เช็คจ่าย_ยกมา | 2 |
| 410 | เงินสดธนาคาร_เช็ครับ_ฝาก | 2 |
| 411 | เงินสดธนาคาร_เช็ครับ_ผ่าน | 2 |
| 412 | เงินสดธนาคาร_เช็ครับ_คืน | 2 |
| 413 | เงินสดธนาคาร_เช็ครับ_ยกเลิก | 2 |
| 416 | เงินสดธนาคาร_เช็ครับ_เปลี่ยนเช็ค | 2 |
| 418 | เงินสดธนาคาร_เช็ครับ_ตั้งหนี้ใหม่ | 1 |
| 422 | เงินสดธนาคาร_โอนเงินออกธนาคาร | 2 |
| 423 | เงินสดธนาคาร_โอนเงินออกธนาคาร_ยกเลิก | 2 |
| 430 | เงินสดธนาคาร_เช็ครับ_ฝาก_ยกเลิก | 2 |
| 431 | เงินสดธนาคาร_เช็ครับ_ผ่าน_ยกเลิก | 2 |
| 432 | เงินสดธนาคาร_เช็ครับ_คืน_ยกเลิก | 2 |
| 433 | เงินสดธนาคาร_เช็ครับ_ยกเลิก_ยกเลิก | 2 |
| 436 | เงินสดธนาคาร_เช็ครับ_เปลี่ยนเช็ค_ยกเลิก | 2 |
| 451 | เงินสดธนาคาร_เช็คจ่าย_ผ่าน | 2 |
| 452 | เงินสดธนาคาร_เช็คจ่าย_ยกเลิก | 2 |
| 453 | เงินสดธนาคาร_เช็คจ่าย_คืน | 2 |
| 456 | เงินสดธนาคาร_เช็คจ่าย_เปลี่ยนเช็ค | 2 |
| 461 | เงินสดธนาคาร_บัตรเครดิต_ผ่าน | 2 |
| 462 | เงินสดธนาคาร_บัตรเครดิต_ยกเลิก | 2 |
| 471 | เงินสดธนาคาร_เช็คจ่าย_ผ่าน_ยกเลิก | 2 |
| 472 | เงินสดธนาคาร_เช็คจ่าย_ยกเลิก_ยกเลิก | 2 |
| 473 | เงินสดธนาคาร_เช็คจ่าย_คืน_ยกเลิก | 2 |
| 476 | เงินสดธนาคาร_เช็คจ่าย_เปลี่ยนเช็ค_ยกเลิก | 2 |

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`ic_trans`, `ic_trans_detail`, `cb_trans_detail`, `erp_pass_book`, `erp_bank_branch`, `erp_bank`, `cb_petty_cash`, `sml_fastreport`, `ic_inventory`, `ic_resource`, `resource_report`, `cb_chq_list`, `ic_trans_serial_number`, `ic_serial`, `ap_ar_resource`, `cb_resource`, `gl_chart_of_account`, `erp_pass_book_type`, `cb_trans`, `temp_cash_movement`

## เมนูทั้งหมด

| เมนู | menu name | POS Pro | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|---|
| รายได้อื่นๆ | `menu_cash_income_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 250 |  |
| ลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit` | ✓ | `SMLInventoryControl._clone_icTrans` | 252 |  |
| เพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit` | ✓ | `SMLInventoryControl._clone_icTrans` | 254 |  |
| รายงาน/ยกเลิก › ยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 251 |  |
| รายงาน/ยกเลิก › ยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 253 |  |
| รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 255 |  |
| รายงาน/ยกเลิก › รายงานรายได้อื่นๆ | `menu_cash_income_other_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 250 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 252 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 254 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 251 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 253 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 255 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other` | ✓ | `SMLInventoryControl._clone_icTrans` | 260 |  |
| ลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit` | ✓ | `SMLInventoryControl._clone_icTrans` | 262 |  |
| เพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit` | ✓ | `SMLInventoryControl._clone_icTrans` | 264 |  |
| รายงาน/ยกเลิก › ยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 261 |  |
| รายงาน/ยกเลิก › ยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 263 |  |
| รายงาน/ยกเลิก › ยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 265 |  |
| รายงาน/ยกเลิก › รายงานค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 260 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 262 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 264 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 261 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 263 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel_report` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 265 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| เงินสด/เงินสดย่อย › ยกมาเงินสด | `menu_cb_cash_balance` | ✓ | `SMLERPCASHBANK._cb_cash_balance` |  | ic_trans |
| เงินสด/เงินสดย่อย › คืน/ลด วงเงินสดย่อย | `menu_cb_petty_cash_receive` | ✓ | `SMLInventoryControl._clone_icTrans` | 300 |  |
| เงินสด/เงินสดย่อย › รับ/เพิ่ม วงเงินสดย่อย | `menu_cb_petty_return` | ✓ | `SMLInventoryControl._clone_icTrans` | 2 |  |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกคืน/ลด วงเงินสดย่อย | `menu_cb_petty_cash_receive_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 302 |  |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › ยกเลิกรับ/เพิ่ม วงเงินสดย่อย | `menu_cb_petty_return_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 303 |  |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานจ่ายเงินสดย่อย | `menu_report_cb_petty_cash_request` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานรับเงินสดย่อย | `menu_report_cb_petty_cash_return` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกเบิกเงินสดย่อย | `menu_report_cb_cancel_pettycash_request` | ✓ | `SMLERPReportTool._reportTrans` | 302 | ic_trans, ic_trans_detail, cb_trans_detail |
| เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกรับเงินสดย่อย | `menu_report_cb_cancel_pettycash_return` | ✓ | `SMLERPReportTool._reportTrans` | 303 | ic_trans, ic_trans_detail, cb_trans_detail |
| เงินสด/เงินสดย่อย › รายงานสรุป › รายงานเคลื่อนไหวเงินสดย่อย | `menu_sub_cash_movements` | ✓ | `SMLERPCASHBANKReport._report_petty_cash` |  | ic_trans_detail, ic_trans_serial_number, ic_serial, ic_resource |
| เงินสด/เงินสดย่อย › รายงานสรุป › รายการตั้งเบิกเงินสดย่อย | `menu_report_cb_pettycash_request_budget` |  | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| เงินสด/เงินสดย่อย › รายงานสรุป › รายงานบันทึกขอเบิกเงินทดลองจ่าย - เรียงตามวันที่เอกสาร | `menu_report_cb_request_testpay` |  | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| เงินสด/เงินสดย่อย › รายงานสรุป › รายงานสถานะเงินสดย่อย | `menu_peety_cash_status` | ✓ | `SMLERPCASHBANKReport._report_petty_cash` |  | ic_trans_detail, ic_trans_serial_number, ic_serial, ic_resource |
| ธนาคาร › ฝาก/ถอน › กำหนดสมุดเงินฝาก | `menu_book_bank` | ✓ | `SMLERPConfig._book` |  | erp_pass_book, gl_chart_of_account, erp_pass_book_type, erp_bank |
| ธนาคาร › ฝาก/ถอน › เงินฝากธนาคารยกมา | `menu_cb_bank_balance` | ✓ | `SMLERPCASHBANK._cb_bank_balance` |  | ic_trans |
| ธนาคาร › ฝาก/ถอน › บันทึกฝากเงิน | `menu_cb_cash_payin` | ✓ | `SMLInventoryControl._clone_icTrans` | 401 |  |
| ธนาคาร › ฝาก/ถอน › บันทึกถอนเงิน | `menu_cb_cash_withdraw` | ✓ | `SMLInventoryControl._clone_icTrans` | 402 |  |
| ธนาคาร › ฝาก/ถอน › บันทึกโอนเงินระหว่างธนาคาร | `menu_cash_transfer` | ✓ | `SMLInventoryControl._clone_icTrans` | 422 |  |
| ธนาคาร › ฝาก/ถอน › บันทึกขึ้นเงินwallet | `menu_cb_wallet_pass` | ✓ | `SMLInventoryControl._clone_icTrans` | 1 |  |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกฝากเงิน | `menu_cb_cash_payin_cancle` | ✓ | `SMLInventoryControl._clone_icTrans` | 403 |  |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกถอนเงิน | `menu_cb_cash_withdraw_cancle` | ✓ | `SMLInventoryControl._clone_icTrans` | 404 |  |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › บันทึกยกเลิกโอนเงินระหว่างธนาคาร | `menu_cash_transfer_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 423 |  |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการฝากเงิน | `menu_report_cash_payin` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการถอนเงิน | `menu_report_cash_withdraw` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการโอนเงินระหว่างธนาคาร | `menu_cb_report_transfer_bank` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 422 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกฝากเงิน | `menu_report_cancel_withdraw` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 403 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกถอนเงิน | `menu_report_cancel_payin` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 404 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกการโอนเงินระหว่างธนาคาร | `menu_report_transfer_bank_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 423 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานรายได้จากธนาคาร | `menu_cb_report_bank_income` |  | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานค่าใช้จ่ายจากธนาคาร | `menu_cb_report_bank_expanse` |  | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ธนาคาร › เช็ครับ › เช็ครับยกมา | `menu_cb_chq_in_receive_balance` | ✓ | `SMLInventoryControl._clone_icTrans` | 405 |  |
| ธนาคาร › เช็ครับ › ทะเบียนเช็ครับ | `menu_cb_chq_in_receive_master` | ✓ | `SMLERPCASHBANK._cb_chq_in_receive_master` |  |  |
| ธนาคาร › เช็ครับ › บันทึกนำฝาก (เช็ครับ) | `menu_cb_chq_in_payin` | ✓ | `SMLInventoryControl._clone_icTrans` | 410 |  |
| ธนาคาร › เช็ครับ › บันทึกเช็คผ่าน (เช็ครับ) | `menu_cb_chq_in_pass` | ✓ | `SMLInventoryControl._clone_icTrans` | 411 |  |
| ธนาคาร › เช็ครับ › บันทึกเช็คคืน (เช็ครับ) | `menu_cb_chq_in_return` | ✓ | `SMLInventoryControl._clone_icTrans` | 412 |  |
| ธนาคาร › เช็ครับ › บันทึกเช็คขาดสิทธิ์ (เช็ครับ) | `menu_cb_chq_in_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 413 |  |
| ธนาคาร › เช็ครับ › บันทึกการเปลี่ยนเช็ค (เช็ครับ) | `menu_cb_chq_renew` | ✓ | `SMLInventoryControl._clone_icTrans` | 416 |  |
| ธนาคาร › เช็ครับ › บันทึกคืนเช็ค/ตั้งหนี้ใหม่ | `menu_cb_return_chq_new_debt` | ✓ | `SMLInventoryControl._clone_icTrans` | 418 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกนำฝากเช็ค | `menu_cb_chq_in_payin_cancle` | ✓ | `SMLInventoryControl._clone_icTrans` | 430 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คผ่าน | `menu_cb_chq_in_pass_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 431 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็ครับคืน | `menu_cb_chq_in_return_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 432 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คขาดสิทธิ์ | `menu_cb_chq_in_cancel_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 433 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็ค | `menu_cb_chq_renew_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 436 |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็ครับยกมา | `menu_cb_report_chq_in_receive_balance` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 405 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานนำฝาก (เช็ครับ) | `menu_bank_report_chq_in_deposit` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 410 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็ครับ) | `menu_bank_report_chq_in_pass` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 411 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรับคืน (เช็ครับ) | `menu_bank_report_chq_in_return` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 412 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็ครับ) | `menu_bank_report_chq_in_pass_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 413 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็ครับ) | `menu_bank_report_chq_in_change` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 416 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกนำฝากเช็ค | `menu_report_cb_chq_in_payin_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 430 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็คผ่าน | `menu_report_cb_chq_in_honor_cancle` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 431 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็ครับคืน | `menu_report_cb_chq_in_return_cancle` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 432 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็ค | `menu_report_cb_chq_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 433 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็ค | `menu_report_cb_chq_in_change_cancle` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 436 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานทะเบียนเช็ครับ | `menu_cb_report_chq_in_receive` | ✓ | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | cb_chq_list, ic_inventory |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค | `menu_cb_report_chq_in_receive_by_date` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่ครบกำหนด | `menu_report_chq_receive_due_date` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานใบนำฝากเช็ครับพร้อมรายการย่อย | `menu_report_chq_card_disposit_cheque_detail` |  | `SMLERPReport.Cheque_Card._report_chq_card_Disposit_Cheque_Detail` |  |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_received_by_date_by_status` |  | `IMEXControl.report._report_chq_receive_by_status` |  |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่ - ตามสถานะเช็ค แสดงยอดรวม | `menu_imex_report_chqreceive_status_by_date` |  | `IMEXControl.report._report_chq_receive_status_by_date` |  |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามสถานะเช็ค แสดงยอดรวม(ไม่รวมเช็คคืน,เช็คคืนตั้งหนี้ใหม่) | `menu_imex_report_chqreceive_status_by_date_only_hand` |  | `IMEXControl.report._report_chq_receive_status_by_date_2` |  |  |
| ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ณ วันที่ | `menu_imex_report_chq_receive_at_date` |  | `IMEXControl.report._report_chq_receive_last_status_by_date` |  |  |
| ธนาคาร › เช็คจ่าย › เช็คจ่ายยกมา | `menu_cb_chq_out_payment_balance` | ✓ | `SMLInventoryControl._clone_icTrans` | 406 |  |
| ธนาคาร › เช็คจ่าย › ทะเบียนเช็คจ่าย | `menu_cb_chq_out_payment_master` | ✓ | `SMLERPCASHBANK._cb_chq_out_payment_master` |  |  |
| ธนาคาร › เช็คจ่าย › บันทึกเช็คผ่าน (เช็คจ่าย) | `menu_cb_chq_out_pass` | ✓ | `SMLInventoryControl._clone_icTrans` | 451 |  |
| ธนาคาร › เช็คจ่าย › บันทึกเช็คคืน (เช็คจ่าย) | `menu_cb_chq_out_return` | ✓ | `SMLInventoryControl._clone_icTrans` | 453 |  |
| ธนาคาร › เช็คจ่าย › บันทึกเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_cb_chq_out_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 452 |  |
| ธนาคาร › เช็คจ่าย › บันทึกการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_cb_chq_out_renew` | ✓ | `SMLInventoryControl._clone_icTrans` | 456 |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คจ่ายผ่าน | `menu_cb_chq_out_pass_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 471 |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คขาดสิทธิ์ | `menu_cb_chq_out_cancel_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 472 |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเช็คคืน | `menu_cb_chq_out_return_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 473 |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › บันทึกยกเลิกเปลี่ยนเช็คจ่าย | `menu_cb_chq_out_renew_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 476 |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คจ่ายยกมา | `menu_cb_report_chq_out_payment_balance` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 406 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็คจ่าย) | `menu_bank_report_chq_out_pass` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 451 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คคืน (เช็คจ่าย) | `menu_bank_report_chq_out_return` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 453 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_bank_report_chq_out_pass_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 452 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_bank_report_chq_out_change` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 456 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คจ่ายผ่าน | `menu_report_cb_chq_out_honor_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 471 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็คจ่าย | `menu_report_cb_chq_out_cancel_hornor_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 472 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คคืน | `menu_report_chq_out_return_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 473 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็คจ่าย | `menu_report_cb_chq_out_change_cancle` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 476 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานทะเบียนเช็คจ่าย | `menu_cb_report_chq_out_payment` | ✓ | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | cb_chq_list, ic_inventory |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค | `menu_cb_report_chq_out_payment_by_date` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - วันครบกำหนด | `menu_report_chq_pay_due_date` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_pay_by_date_by_status` |  | `IMEXControl.report.report_chq_pay_by_status` |  |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่ - ตามสถานะเช็ค | `imex_report_cheque_pay_status_by_date` |  | `IMEXControl.report._report_chq_pay_status_by_date` |  |  |
| ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย ณ วันที่ | `menu_imex_report_chq_pay_at_date` |  | `IMEXControl.report._report_chq_pay_last_status_by_date` |  |  |
| ธนาคาร › บัตรเครดิต › ทะเบียนบัตรเครดิต | `menu_cb_credit_card_receive` | ✓ | `SMLERPCASHBANK._cb_credit_master` |  |  |
| ธนาคาร › บัตรเครดิต › บันทึกขึ้นเงินบัตรเครดิต | `menu_cb_credit_card_pass` | ✓ | `SMLInventoryControl._clone_icTrans` | 461 |  |
| ธนาคาร › บัตรเครดิต › บันทึกยกเลิกบัตรเครดิต | `menu_cb_credit_card_cancel` | ✓ | `SMLInventoryControl._clone_icTrans` | 462 |  |
| ธนาคาร › บัตรเครดิต › รายงานขึ้นเงินบัตรเครดิต | `menu_cb_report_credit_card_pass` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 461 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › บัตรเครดิต › รายงานยกเลิกบัตรเครดิต | `menu_report_cb_credit_card_cancel` | ✓ | `SMLERPReportTool._reportCashBankTrans` | 462 | ic_trans_detail, ic_trans, erp_pass_book, erp_bank_branch |
| ธนาคาร › บัตรเครดิต › รายงานรายการรับบัตรเครดิต | `menu_cb_report_credit_card_receive` | ✓ | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` |  | cb_chq_list, ic_inventory |
| ธนาคาร › บัตรเครดิต › รายงานรายละเอียดบัตรเครดิต - ตามวันที่รับ | `menu_report_chq_card_enddate_card` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › รายงาน › รายงานเคลื่อนไหวเงินสด | `_menu_cash_movements` | ✓ | `SMLERPCASHBANKReport._cashbank_report` |  | resource_report, cb_resource, cb_petty_cash, ic_resource |
| ธนาคาร › รายงาน › รายงานการฝากเงินสด | `_menu_cash_deposit` |  | tag:report (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร) |  |  |
| ธนาคาร › รายงาน › รายงานการรับเงินอื่นๆพร้อมรายการย่อย | `_menu_received_cash_sub_item` |  | `SMLERPReport.cash_bank.Received_Cash_sub_item` |  |  |
| ธนาคาร › รายงาน › รายงานสรุปการรับเงิน | `menu_summary_received` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › รายงาน › รายงานสรุปการจ่ายเงิน | `menu_summary_payment` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › รายงาน › รายงานยอดเงินคงเหลือสมุดฝากธนาคาร | `menu_book_bank_balance` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| ธนาคาร › รายงาน › รายงาน Bank Statement | `_menu_bank_statement` | ✓ | `SMLERPReport.cash_bank._bankStatment` |  | cb_trans_detail, ic_trans_detail, cb_resource, erp_pass_book |
| ธนาคาร › รายงาน › รายงาน Statement ล่วงหน้า | `menu_statement_advance` | ✓ | `SMLFastReport._designer` |  | sml_fastreport |
| บันทึกรูปภาพเอกสาร | `menu_cb_doc_picture` | ✓ | `SMLERPCASHBANK._cb_doc_picture` |  |  |
| รายงานอื่น ๆ | `menu_fastreport_other_cashbank` | ✓ | tag:fastreportother |  |  |
