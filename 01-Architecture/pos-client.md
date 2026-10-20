---
tags: [sml, pos, core]
source: smlerp/SMLPosClient/_posClientForm.cs (+ AOY aggregate checks)
status: from-code, partly verified-on-aoy
date: 2026-10-20
---
# POS หน้าร้าน: `SMLPosClient._posClientForm`

กลับไป [[00-Index]] · โมดูล [[module-pos]] · ที่เก็บข้อมูล [[data-model]]

## เปิดหน้าจออย่างไร
- เมนู `menu_pos_screen` (tag `posclient`) → `SMLPosClient._selectMenu` → อ่าน config หน้าจอ POS (`SMLPOSControl._posScreenConfig`, XML) → ฟอร์ม login POS `_posLoginForm` (ตรวจ `erp_user` ด้วยรหัส/รหัสผ่าน) → `new _posClientForm(userCode, password)`
- โหมดเภสัชกร (ร้านยา) `pm_counseling` เปิดฟอร์มเดียวกันด้วยพารามิเตอร์ต่างกัน
- เมนูข้างเคียง: บันทึกส่งเงิน `_posSaveSendMoney`, รับเงิน `_posSaveMoneyReceive`, สรุปยอด `_summaryUserControl` / `_summaryDayUserControl`, ตั้งค่าหน้าจอ `_configPOSScreen`

## บันทึกบิล (`__pay__saveData`, ~บรรทัด 7901)
หลังกดชำระเงินในฟอร์ม `_posPayForm` จะสร้างชุดคำสั่งแล้วส่งด้วย `_queryList` (transaction เดียวที่ web service เหมือน [[document-engine]]):
- `ic_trans` (flag 44, `is_pos = 1`), `ic_trans_detail`, `ic_trans_detail_promotion`, `ic_trans_discount_group`, `ic_trans_serial_number`, `ic_trans_shipment`
- ภาษีขาย `gl_journal_vat_sale` (ใบกำกับภาษีอย่างย่อ)
- การรับเงิน `cb_trans` (+ ฟังก์ชันย่อย `_processChqCreditCard`, `_processDepositMoney` สำหรับบัตร/เช็ค/เงินมัดจำ)
- แต้ม/SMS `point_center_sms`
- หลังบันทึก: พิมพ์สลิป (`_printSlip` ใบกำกับภาษีอย่างย่อ), เก็บภาพสลิป e-Journal (`_save_eJournal`), เปิดลิ้นชัก, คำนวณสต็อก (`_processStockThread` → `_process_stock_balance`)

**ยืนยันกับ AOY:** บิล POS 132 ใบ มี `cb_trans` ครบทั้ง 132 ใบ และมี `gl_journal_vat_sale` 140 รายการที่ผูกกับเอกสาร POS

## ร้านอาหาร / โต๊ะ
ฟอร์มเดียวกันจัดการโต๊ะ: `table_master`, `table_order`, `table_order_doc`, `table_order_log`, `table_trans`, `order_checker` (`_processRoundTable`)

## Log การกระทำของแคชเชียร์ `pos_log`
`_saveCommandLog(user, command, message, approveCode, amount, commandType)` → `pos_log (datetime, user_code, command, message, approve_code, amount, command_type)`
- ใช้กับการกระทำที่ต้องอนุมัติ/ควรตรวจสอบ เช่น `*1*` แก้ราคา, `*2*` ยกเลิกส่วนลด, `*6*` (ลบ/แก้รายการ), `*61*` เปลี่ยนคลังเริ่มต้น
- AOY มี command_type: `***` 16, `*98` 11, `*71` 4, `*2*` 4, `*72` 3 — ความหมายของ `***`, `*98`, `*71`, `*72` ยังไม่ได้ไล่
- **โอกาสทำ product:** `pos_log` + บิลยกเลิก (flag 45) + ส่วนลด เป็นแหล่งข้อมูลตรวจจับความผิดปกติของแคชเชียร์ ดู [[product-ideas]]

## พักบิล
- `_holdBill` เป็น `List<_holdBillClass>` **ในหน่วยความจำของเครื่อง** — ไม่ได้บันทึกลง database (ปิดโปรแกรม = หาย) จากโค้ด ยังไม่ได้ยืนยันว่ามีที่เก็บสำรองอื่น

## ยังไม่ได้ไล่
- ปิดกะ / ส่งเงิน / ลิ้นชัก ละเอียด (`_posSaveSendMoney`, `temp_cash_movement`)
- โปรโมชั่นและแต้มสะสม (`SMLPOSControl`)
- ความหมาย command_type ที่เหลือใน `pos_log`
