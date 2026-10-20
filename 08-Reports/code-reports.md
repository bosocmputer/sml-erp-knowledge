---
tags: [sml, reports, generated]
status: from-code
---
# รายงานที่เขียนในโค้ด (SMLERPReportTool)

> สร้างอัตโนมัติด้วย `scripts/gen_code_reports.py` — เครื่องมือ `_reportTrans` / `_reportCashBankTrans` / `_reportArApTrans` รับ `reportEnum` + ประเภทเอกสาร แล้วสร้าง query ตามกรณี
> ตาราง = ตารางที่อ้างในโค้ดกรณีนั้น (static) · กลับไป [[reports]] · [[00-Index]]

ทั้งหมด 151 reportEnum

| reportEnum | เมนู | trans_flag | ตาราง | ไฟล์ |
|---|---|---|---|---|
| ขาย_ขายสินค้าและบริการ | รายงานการขายสินค้าและบริการ (`menu_so_report_invoice`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_ขายสินค้าและบริการ_ยกเลิก | รายงานยกเลิกขายสินค้าและบริการ (`menu_so_report_invoice_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_ขายสินค้าและบริการ_รายงานการออกใบกำกับภาษีอย่างเต็ม | รายงานใบกำกับภาษีอย่างเต็มออกแทน (`menu_so_report_pos_full_invoice`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_ขายสินค้าและบริการ_ลดหนี้_เพิ่มหนี้ |  | 48 | ic_trans, ic_trans_detail | _reportTrans.cs |
| ขาย_รับคืนสินค้า | รายงานการรับคืนสินค้า/ลดหนี้ (`menu_so_report_credit_note`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับคืนสินค้า_ยกเลิก | รายงานยกเลิกรับคืนสินค้า/ลดหนี้ (`menu_so_report_credit_note_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ | รายงานรับเงินมัดจำ (`menu_so_report_deposit_receive_2`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ_คืน | รายงานคืนเงินมัดจำ (`menu_so_report_deposit_return_2`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ_คืน_ยกเลิก | รายงานยกเลิกคืนเงินมัดจำ (`menu_so_report_deposit_payment_return_cancel_2`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ_ยกเลิก | รายงานยกเลิกรับเงินมัดจำ (`menu_so_report_deposit_payment_cancel_2`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ_รายงานตัดเงิน | รายงานการตัดเงินมัดจำ (`menu_so_report_cut_deposit_payment_2`) | 42, 112 | cb_trans_detail, ic_trans, ic_trans_detail | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินมัดจำ_รายงานยอดคงเหลือ | รายงานยอดคงเหลือเงินมัดจำ (`menu_so_report_deposit_payment_remain_2`) | 42, 112 | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า | รายงานรับเงินล่วงหน้า (`menu_so_report_deposit_receive`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า_คืน | รายงานคืนเงินรับล่วงหน้า (`menu_so_report_deposit_return`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า_คืน_ยกเลิก | รายงานยกเลิกคืนเงินรับล่วงหน้า (`menu_so_report_deposit_payment_return_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า_ยกเลิก | รายงานยกเลิกรับเงินล่วงหน้า (`menu_so_report_deposit_payment_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า_รายงานตัดเงิน | รายงานการตัดเงินรับล่วงหน้า (`menu_so_report_cut_deposit_payment`) | 42, 112 | cb_trans_detail, ic_trans, ic_trans_detail | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_รับเงินล่วงหน้า_รายงานยอดคงเหลือ | รายงานยอดคงเหลือเงินรับล่วงหน้า (`menu_so_report_deposit_payment_remain`) | 42, 112 | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งขาย | รายงานใบสั่งขาย (`menu_so_report_sale_order`) | 52 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งขาย_ยกเลิก | รายงานยกเลิกใบสั่งขาย (`menu_so_report_sale_order_cancel`) | 52 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งขาย_สถานะ | รายงานสถานะใบสั่งขาย (`menu_so_report_sale_order_stat`) | 52 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งขาย_อนุมัติ | รายงานอนุมัติใบสั่งขาย (`menu_so_report_sale_order_approve`) | 52 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งจองและสั่งซื้อสินค้า | รายงานใบสั่งซื้อ/สั่งจอง (`menu_so_report_inquiry`) | 38 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งจองและสั่งซื้อสินค้า_ยกเลิก | รายงานยกเลิกใบสั่งซื้อ/สั่งจอง (`menu_so_report_inquiry_cancel`) | 38 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งจองและสั่งซื้อสินค้า_สถานะ | รายงานสถานะใบสั่งซื้อ/สั่งจอง (`menu_so_report_inquiry_stat`) | 38 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_สั่งจองและสั่งซื้อสินค้า_อนุมัติ | รายงานอนุมัติใบสั่งซื้อ/สั่งจอง (`menu_so_report_inquiry_approve`) | 38 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เพิ่มหนี้สินค้าราคาผิด | รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า (`menu_so_report_add_goods`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เพิ่มหนี้สินค้าราคาผิด_ยกเลิก | รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า (`menu_so_report_add_goods_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เสนอราคา | รายงานบันทึกใบเสนอราคา (`menu_so_report_quotation`) | 32 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เสนอราคา_ยกเลิก | รายงานยกเลิกใบเสนอราคา (`menu_so_report_quotation_cancel`) | 32 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เสนอราคา_สถานะ | รายงานสถานะใบเสนอราคา (`menu_so_report_quotation_stat`) | 32 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ขาย_เสนอราคา_อนุมัติ | รายงานอนุมัติใบเสนอราคา (`menu_so_report_quotation_approve`) | 32 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินมัดจำ | รายงานจ่ายเงินมัดจำ (`menu_po_report_advance_payment`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินมัดจำ_ยกเลิก | รายงานยกเลิกจ่ายเงินมัดจำ (`menu_po_report_advance_payment_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินมัดจำ_รับคืน | รายงานรับคืนเงินมัดจำ (`menu_po_report_advance_payment_return`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินมัดจำ_รับคืน_ยกเลิก | รายงานยกเลิกคืนเงินมัดจำ (`menu_po_report_advance_payment_return_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินล่วงหน้า | รายงานบันทึกการจ่ายเงินล่วงหน้า (`menu_po_report_deposit_payment`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินล่วงหน้า_ยกเลิก | รายงานยกเลิกจ่ายเงินล่วงหน้า (`menu_po_report_deposit_payment_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินล่วงหน้า_รับคืน | รายงานบันทึกรับคืนเงินล่วงหน้า (`menu_po_report_deposit_payment_return`) |  | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_จ่ายเงินล่วงหน้า_รับคืน_ยกเลิก | รายงานยกเลิกรับคืนเงินล่วงหน้า (`menu_po_report_deposit_payment_return_cancel`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ซื้อสินค้าและบริการ | รายงานการซื้อสินค้า/ตั้งหนี้ (`menu_po_report_purchase`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ซื้อสินค้าและบริการ_ยกเลิก | รายงานยกเลิกรับสินค้า/ตั้งหนี้ (`menu_po_report_purchase_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_พาเชียล_ตั้งหนี้ | รายงานตั้งหนี้จากการรับสินค้า (`menu_po_report_purchase_partial_1`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| ซื้อ_พาเชียล_รับสินค้า | รายงานรับสินค้า (`menu_po_report_purchase_partial`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| ซื้อ_พาเชียล_ลดหนี้ | รายงานลดหนี้จากใบตั้งหนี้ (`menu_po_report_purchase_partial_3`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| ซื้อ_พาเชียล_ส่งคืนสินค้าหรือราคาผิด | รายงานส่งคืนสินค้า/ราคาผิด (`menu_po_report_purchase_partial_debit`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| ซื้อ_พาเชียล_เพิ่มหนี้ | รายงานเพิ่มหนี้จากใบตั้งหนี้ (`menu_po_report_purchase_partial_2`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| ซื้อ_รายงานค้างรับตามใบสั่งซื้อ | รายงานค้างรับสินค้าตามใบสั่งซื้อ (`menu_po_hold_receive_by_doc`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานตัดเงินจ่ายล่วงหน้า | รายงานการตัดจ่ายเงินล่วงหน้า (`menu_po_report_cut_deposit_payment`) | 20, 25 | cb_trans_detail, ic_trans, ic_trans_detail | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานตัดเงินมัดจำจ่าย | รายงานการตัดใบจ่ายเงินมัดจำ (`menu_po_report_cut_deposit_payment_2`) | 20, 25 | cb_trans_detail, ic_trans, ic_trans_detail | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานยกเลิกใบสั่งซื้อ | รายงานยกเลิกใบสั่งซื้อ (`menu_po_report_purchase_order_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานยอดคงเหลือเงินจ่ายล่วงหน้า | รายงานยอดคงเหลือจ่ายเงินล่วงหน้า (`menu_po_report_deposit_payment_remain`) | 20, 25 | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานยอดคงเหลือเงินมัดจำจ่าย | รายงานยอดคงเหลือเงินมัดจำ (`menu_po_report_deposit_payment_2_remain`) | 20, 25 | ic_trans, ic_trans_detail | _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานสถานะใบสั่งซื้อ | รายงานสถานะใบสั่งซื้อ (`menu_po_report_purchase_order_status`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานอนุมัติใบสั่งซื้อ | รายงานอนุมัติใบสั่งซื้อ (`menu_po_report_purchase_order_approve`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_รายงานใบสั่งซื้อ | รายงานบันทึกใบสั่งซื้อ (`menu_po_report_purchase_order`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด | รายงานการส่งคืนสินค้า/ลดหนี้ (`menu_po_report_credit_note`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด_ยกเลิก | รายงานยกเลิกส่งคืนสินค้า/ลดหนี้ (`menu_po_credit_note_cancel_report`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_เพิ่มหนี้ราคาผิด | รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า (`menu_po_report_add_goods`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_เพิ่มหนี้ราคาผิด_ยกเลิก | รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า (`menu_po_report_add_goods_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ใบเสนอซื้อ | รายงานใบเสนอซื้อ (`menu_po_report_record_requisition_purchase`) | 4 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ใบเสนอซื้อ_ยกเลิก |  | 4 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ใบเสนอซื้อ_สถานะ | รายงานสถานะใบเสนอซื้อ (`menu_po_report_requisition_purchase`) | 4 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ซื้อ_ใบเสนอซื้อ_อนุมัติ | รายงานอนุมัติใบเสนอซื้อ (`menu_po_report_requisition_purchase1`) | 4 | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| ธนาคาร_ถอนเงิน_ยกเลิก | รายงานยกเลิกถอนเงิน (`menu_report_cancel_payin`) |  | ic_trans | _reportCashBankTrans.cs |
| ธนาคาร_ฝากเงิน_ยกเลิก | รายงานยกเลิกฝากเงิน (`menu_report_cancel_withdraw`) |  | ic_trans | _reportCashBankTrans.cs |
| ธนาคาร_โอนเงิน | รายงานการโอนเงินระหว่างธนาคาร (`menu_cb_report_transfer_bank`) |  | erp_pass_book, ic_trans_detail, erp_bank_branch, ic_trans, erp_bank | _reportCashBankTrans.cs |
| ธนาคาร_โอนเงิน_ยกเลิก | รายงานยกเลิกการโอนเงินระหว่างธนาคาร (`menu_report_transfer_bank_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| บัตรเครดิต_ขึ้นเงิน | รายงานขึ้นเงินบัตรเครดิต (`menu_cb_report_credit_card_pass`) |  | ic_trans_detail, erp_pass_book, ic_trans, erp_bank_branch, erp_bank | _reportCashBankTrans.cs |
| บัตรเครดิต_ยกเลิก | รายงานยกเลิกบัตรเครดิต (`menu_report_cb_credit_card_cancel`) |  | ic_trans_detail, erp_pass_book, ic_trans, erp_bank_branch, erp_bank | _reportCashBankTrans.cs |
| ลูกหนี้_ตั้งหนี้ยกมา | รายงานตั้งหนี้ยกมา (`menu_ar_report_early_year_balance_setup`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ลูกหนี้_ตั้งหนี้อื่น | รายงานตั้งหนี้อื่นๆ (`menu_ar_documents_early_year_other`) |  | ic_trans | _reportTrans.cs |
| ลูกหนี้_ตั้งหนี้อื่น_ยกเลิก | รายงานยกเลิกตั้งหนี้อื่นๆ (`menu_ar_cancel_documents_early_year_other`) |  | ic_trans | _reportTrans.cs |
| ลูกหนี้_รับชำระหนี้ | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (`menu_ar_report_receipt`) |  | ap_ar_trans_detail, ap_ar_trans | _reportArApTrans.cs |
| ลูกหนี้_รับชำระหนี้_ยกเลิก | รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน (`menu_ar_report_cancel_invoice`) |  | ap_ar_trans | _reportArApTrans.cs |
| ลูกหนี้_รับวางบิล | รายงานใบวางบิล (ลูกหนี้) (`menu_ar_report_billing`) |  | ap_ar_trans_detail, ap_ar_trans | _reportArApTrans.cs |
| ลูกหนี้_รับวางบิล_ยกเลิก | รายงานยกเลิกใบวางบิล(ลูกหนี้) (`menu_ar_report_cancel_pay_billing`) |  | ap_ar_trans | _reportArApTrans.cs |
| ลูกหนี้_รายงานการรับชำระหนี้ประจำวัน | รายงานการรับชำระหนี้ประจำวัน (`menu_ar_report_pay_debt_trans`) |  | ap_ar_trans_detail, resource_report, ap_ar_trans, ic_trans | _reportArApTrans.cs |
| ลูกหนี้_รายละเอียด |  |  | ar_customer | _reportCustMaster.cs |
| ลูกหนี้_ลดหนี้ยกมา | รายงานลดหนี้ยกมา (`menu_ar_report_early_year_balance_decrease`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ลูกหนี้_ลดหนี้อื่น | รายงานลดหนี้อื่นๆ (`menu_ar_reduction_dept_other`) |  | ic_trans | _reportTrans.cs |
| ลูกหนี้_ลดหนี้อื่น_ยกเลิก | รายงานยกเลิกลดหนี้อื่นๆ (`menu_ar_cancel_reduction_dept_other`) |  | ic_trans | _reportTrans.cs |
| ลูกหนี้_เพิ่มหนี้ยกมา | รายงานเพิ่มหนี้ยกมา (`menu_ar_report_early_year_balance_increase`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| ลูกหนี้_เพิ่มหนี้อื่น | รายงานเพิ่มหนี้อื่นๆ (`menu_report_ar_increase_debt_other`) |  | ic_trans | _reportTrans.cs |
| ลูกหนี้_เพิ่มหนี้อื่น_ยกเลิก | รายงานยกเลิกเพิ่มหนี้อื่นๆ (`menu_ar_cancel_increase_debt_other`) |  | ic_trans | _reportTrans.cs |
| สินค้า_pos_sale_sugest_by_item_and_serial |  |  | ic_trans_detail, ic_trans_serial_number | _reportPosAnalyze.cs |
| สินค้า_sell_by_sale | รายงานสรุปการขายสินค้าตามพนักงานขาย (`menu_sell_by_sale`) |  |  | _reportTrans.cs |
| สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_ขาด | รายงานการปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) (`menu_ic_report_item_adjust_decrease`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_ขาด_ยกเลิก |  |  | ic_trans | _reportTrans.cs |
| สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_เกิน | รายงานการปรับปรุงสต็อกสินค้าและวัตถุดิบ (เกิน) (`menu_ic_report_item_adjust_increase`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_เกิน_ยกเลิก |  |  | ic_trans | _reportTrans.cs |
| สินค้า_รายงานรับคืนเบิกสินค้าวัตถุดิบ | รายงานรับคืนสินค้าและวัตถุดิบ จากการเบิก (`menu_ic_report_item_return`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานรับคืนเบิกสินค้าวัตถุดิบ_ยกเลิก | รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก (`menu_ic_report_cancel_goods_raw_meterial`) |  | ic_trans | _reportTrans.cs |
| สินค้า_รายงานรับสินค้าสำเร็จรูป | รายงานการรับสินค้าสำเร็จรูป (`menu_import_item_ready_by_date`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานรับสินค้าสำเร็จรูป_ยกเลิก | รายงานยกเลิกรับสินค้าสำเร็จรูป (`menu_ic_report_cancel_goods_pack`); รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) (`menu_ic_report_stk_cancel_over`); รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) (`menu_ic_report_stk_cancel_lost`) |  | ic_trans | _reportTrans.cs |
| สินค้า_รายงานสินค้าตรวจนับ | รายงานตรวจนับสินค้า (`menu_ic_report_item_count`); รายงานตรวจนับสินค้า (คลัง) (`menu_wh_report_item_count`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานสินค้าและวัตถุดิบคงเหลือยกมา | รายงานสินค้าและวัตถุดิบ คงเหลือยกมา (`menu_ic_report_goods_balance`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานเบิกสินค้าวัตถุดิบ | รายงานการเบิกสินค้าและวัตถุดิบ (`menu_ic_report_item_withdraw`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานเบิกสินค้าวัตถุดิบ_ยกเลิก | รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ (`menu_ic_report_cancel_raw_material`) |  | ic_trans | _reportTrans.cs |
| สินค้า_รายงานโอนสินค้าและวัตถุดิบ | รายงานการโอนสินค้าและวัตถุดิบ (`menu_ic_report_item_transfer`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs, _reportPosAnalyze.cs, _reportTrans.cs |
| สินค้า_รายงานโอนสินค้าและวัตถุดิบ_ยกเลิก | รายงานยกเลิกโอนสินค้า/วัตถุดิบ (`menu_ic_report_stk_cancel`) |  | ic_trans | _reportTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น | รายงานค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น_ยกเลิก | รายงานยกเลิกค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้ | รายงานลดหนี้ค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_credit_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้_ยกเลิก | รายงานยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_credit_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้ | รายงานเพิ่มหนี้ค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_debit_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้_ยกเลิก | รายงานยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ (`menu_cash_expense_other_debit_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น | รายงานรายได้อื่นๆ (`menu_cash_income_other_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น_ยกเลิก | รายงานยกเลิกรายได้อื่นๆ (`menu_cash_income_other_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น_ลดหนี้ | รายงานลดหนี้รายได้อื่นๆ (`menu_cash_income_other_credit_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น_ลดหนี้_ยกเลิก | รายงานยกเลิกลดหนี้รายได้อื่นๆ (`menu_cash_income_other_credit_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้ | รายงานเพิ่มหนี้รายได้อื่นๆ (`menu_cash_income_other_debit_report`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้_ยกเลิก | รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ (`menu_cash_income_other_debit_cancel_report`) |  | ic_trans | _reportCashBankTrans.cs |
| เงินสดย่อย_รับคืน |  |  | ic_trans_detail, ic_trans, cb_petty_cash | _reportCashBankTrans.cs |
| เงินสดย่อย_รับคืน_ยกเลิก | รายงานยกเลิกรับเงินสดย่อย (`menu_report_cb_cancel_pettycash_return`) |  | ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| เงินสดย่อย_เบิก |  |  | ic_trans_detail, ic_trans, cb_petty_cash | _reportCashBankTrans.cs |
| เงินสดย่อย_เบิก_ยกเลิก | รายงานยกเลิกเบิกเงินสดย่อย (`menu_report_cb_cancel_pettycash_request`) |  | ic_trans | _reportCashBankTrans.cs, _reportTrans.cs |
| เจ้าหนี้_จ่ายชำระหนี้ | รายงานการจ่ายชำระหนี้ (เจ้าหนี้) (`menu_ap_report_payment`) |  | ap_ar_trans_detail, ap_ar_trans | _reportArApTrans.cs |
| เจ้าหนี้_จ่ายชำระหนี้_ยกเลิก | รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) (`menu_ap_report_cancel_debt_billing`) |  | ap_ar_trans | _reportArApTrans.cs |
| เจ้าหนี้_ตั้งหนี้ยกมา | รายงานตั้งหนี้ยกมา (`menu_ap_report_early_year_balance_setup`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_ตั้งหนี้อื่น | รายงานตั้งหนี้อื่นๆ (`menu_documents_early_year_other`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_ตั้งหนี้อื่น_ยกเลิก | รายงานยกเลิกตั้งหนี้อื่นๆ (`menu_cancel_documents_early_year_other`) |  | ic_trans | _reportTrans.cs |
| เจ้าหนี้_รับวางบิล | รายงานใบรับวางบิล (เจ้าหนี้) (`menu_ap_report_billing`) |  | ap_ar_trans_detail, ap_ar_trans | _reportArApTrans.cs |
| เจ้าหนี้_รับวางบิล_ยกเลิก | รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) (`menu_ap_report_cancel_pay_bill`) |  | ap_ar_trans | _reportArApTrans.cs |
| เจ้าหนี้_รายละเอียด | รายงานรายละเอียดเจ้าหนี้ (`menu_ap_report_detail_ap`) |  | ap_supplier | _reportCustMaster.cs |
| เจ้าหนี้_ลดหนี้ยกมา | รายงานลดหนี้ยกมา (`menu_ap_report_early_year_balance_decrease`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_ลดหนี้อื่น | รายงานลดหนี้อื่นๆ (`menu_reduction_dept_other`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_ลดหนี้อื่น_ยกเลิก | รายงานยกเลิกลดหนี้อื่นๆ (`menu_cancel_reduction_dept_other`) |  | ic_trans | _reportTrans.cs |
| เจ้าหนี้_เพิ่มหนี้ยกมา | รายงานเพิ่มหนี้ยกมา (`menu_ap_report_early_year_balance_increase`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_เพิ่มหนี้อื่น | รายงานเพิ่มหนี้อื่นๆ (`menu_increase_debt_other`) |  | ic_trans | _reportPosAnalyze.cs, _reportTrans.cs |
| เจ้าหนี้_เพิ่มหนี้อื่น_ยกเลิก | รายงานยกเลิกเพิ่มหนี้อื่นๆ (`menu_cancel_increase_debt_other`) |  | ic_trans | _reportTrans.cs |
| เช็คจ่าย_ขาดสิทธิ์ | รายงานเช็คขาดสิทธิ์ (เช็คจ่าย) (`menu_bank_report_chq_out_pass_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_ขาดสิทธิ์_ยกเลิก | รายงานยกเลิก ยกเลิกเช็คจ่าย (`menu_report_cb_chq_out_cancel_hornor_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_คืน | รายงานเช็คคืน (เช็คจ่าย) (`menu_bank_report_chq_out_return`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_คืน_ยกเลิก | รายงานยกเลิกเช็คคืน (`menu_report_chq_out_return_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_ผ่าน | รายงานเช็คผ่าน (เช็คจ่าย) (`menu_bank_report_chq_out_pass`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_ผ่าน_ยกเลิก | รายงานยกเลิกเช็คจ่ายผ่าน (`menu_report_cb_chq_out_honor_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_ยกมา | รายงานเช็คจ่ายยกมา (`menu_cb_report_chq_out_payment_balance`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_เปลี่ยน_ยกเลิก | รายงานยกเลิกเปลี่ยนเช็คจ่าย (`menu_report_cb_chq_out_change_cancle`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็คจ่าย_เปลี่ยนเช็ค | รายงานการเปลี่ยนเช็ค (เช็คจ่าย) (`menu_bank_report_chq_out_change`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ขาดสิทธิ์ | รายงานเช็คขาดสิทธิ์ (เช็ครับ) (`menu_bank_report_chq_in_pass_cancel`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ขาดสิทธิ์_ยกเลิก | รายงานยกเลิก ยกเลิกเช็ค (`menu_report_cb_chq_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ผ่าน | รายงานเช็คผ่าน (เช็ครับ) (`menu_bank_report_chq_in_pass`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ผ่าน_ยกเลิก | รายงานยกเลิกเช็คผ่าน (`menu_report_cb_chq_in_honor_cancle`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ฝาก | รายงานนำฝาก (เช็ครับ) (`menu_bank_report_chq_in_deposit`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ฝาก_ยกเลิก | รายงานยกเลิกนำฝากเช็ค (`menu_report_cb_chq_in_payin_cancel`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_ยกมา | รายงานเช็ครับยกมา (`menu_cb_report_chq_in_receive_balance`) |  | ic_trans, ic_trans_detail | _reportCashBankTrans.cs |
| เช็ครับ_รับคืน | รายงานรับคืน (เช็ครับ) (`menu_bank_report_chq_in_return`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_รับคืน_ยกเลิก | รายงานยกเลิกเช็ครับคืน (`menu_report_cb_chq_in_return_cancle`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_เปลี่ยน_ยกเลิก | รายงานยกเลิกเปลี่ยนเช็ค (`menu_report_cb_chq_in_change_cancle`) |  | ic_trans | _reportCashBankTrans.cs |
| เช็ครับ_เปลี่ยนเช็ค | รายงานการเปลี่ยนเช็ค (เช็ครับ) (`menu_bank_report_chq_in_change`) |  | ic_trans_detail, ic_trans | _reportCashBankTrans.cs |
