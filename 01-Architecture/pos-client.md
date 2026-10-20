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
- `command_type` คือ **รหัสคำสั่งที่แคชเชียร์พิมพ์ในช่องสินค้า** (ถอดจากโค้ด `_posClientForm.cs`):

| command_type | ความหมาย | ระดับความเสี่ยง (ตรวจการทุจริต) |
|---|---|---|
| `***` | ลบรายการสินค้า (`***5` = ลบบรรทัดที่ 5) ต้องใส่รหัสผ่าน | สูง |
| `*91` | ล้างบิลทั้งใบ/เริ่มรายการใหม่ (เก็บรายการที่ถูกล้างไว้ใน message) | สูง |
| `*1*` | แก้ไขราคา (ราคาเดิม → ราคาใหม่) | สูง |
| `*2*` | ยกเลิก/แก้ไขส่วนลดรายการ | สูง |
| `*71` | พักบิล (เก็บรายการ `รหัส@จำนวน:ยอด`) | กลาง |
| `*72` | เรียกบิลพักคืน | กลาง |
| `*92`, `*96` | พิมพ์บิลซ้ำ (Reprint) | กลาง |
| `*6*` | เปลี่ยนคลังของรายการ | ต่ำ |
| `*61*` | เลือกคลัง/ที่เก็บเริ่มต้นของการขาย | ต่ำ |
| `*98` | ปิดหน้าจอ POS | ต่ำ |

- AOY (2026-10-20): `***` 16, `*98` 11, `*71` 4, `*2*` 4, `*72` 3 → มีการลบรายการ 16 ครั้ง
- **โอกาสทำ product:** `pos_log` + บิลยกเลิก (flag 45) + ส่วนลด เป็นแหล่งข้อมูลตรวจจับความผิดปกติของแคชเชียร์ ดู [[product-ideas]]

## พักบิล
- `_holdBill` เป็น `List<_holdBillClass>` **ในหน่วยความจำของเครื่อง** — ไม่ได้บันทึกลง database (ปิดโปรแกรม = หาย) จากโค้ด ยังไม่ได้ยืนยันว่ามีที่เก็บสำรองอื่น

## กะ ส่งเงิน และปิดยอด (จากโค้ด + พจนานุกรม)
- **กะ** `pos_period`: เครื่อง (`machine_code`), เปิดกะ (`begin_date/time`, `begin_user_code`), ปิดกะ (`end_*`), `period_status` 0 = เปิดใช้ / 1 = ปิดแล้ว, ผูกด้วย `period_guid`
- รหัสรอบการขายปัจจุบันเก็บที่ `erp_option.sale_shift_id` และประทับลง `ic_trans.sale_shift_id` / `ic_trans_detail.sale_shift_id` ตอนบันทึกบิล (ร้าน AOY ไม่ได้ใช้ → ว่าง)
- **รับเงินทอน / ส่งเงิน** (`_posSaveMoneyReceive`, `_posSaveSendMoney`): ตาราง `POSCashierSettle` (`trans_type` 1 = รับเงินทอน, 2 = ส่งเงิน; แยกยอดเงินสด/บัตร/คูปอง/เช็ค/เงินโอน; ยอดขาย ยอดยกเลิก ยอดสุทธิ ยอดปัดเศษ; ผู้จัดการอนุมัติ) + `POSCashierSettle_detail` นับธนบัตรตาม `banknotes`
  - ⚠️ ตารางนี้มีคอลัมน์ `manager_password` — ห้ามดึงมาแสดงหรือส่งให้ AI
- **สรุปปิดยอด** (`_summaryUserControl`): อ่านบิล 44/45 ตามกะ/เครื่อง แล้วบันทึกบิลยกเลิกที่ส่ง `pos_settle_bill_cancel` และบิลส่วนลด `pos_settle_bill_discount` (ผูก `period_guid`)
- **ใช้ทำ product:** ส่วนต่างเงินที่ส่งจริงกับยอดขายต่อกะ (`POSCashierSettle.total_diff`, ยอดเงินสดเทียบ `cb_trans`), บิลยกเลิก/ส่วนลดต่อกะ, `pos_log` → ตรวจจับความผิดปกติของแคชเชียร์

## โปรโมชั่นและแต้ม
- ตารางกลุ่ม POS ทั้งหมด (47 ตาราง) ดู [[dict-pos]] — โปรโมชั่นที่ใช้ในบิลบันทึกที่ `ic_trans_detail_promotion`, แต้ม/SMS `point_center_sms`, ตั้งค่าแต้มจากเมนู "กำหนดเงื่อนไขสะสมแต้ม" (`SMLPOSControl._posPointPeriodForm`)

## ยังไม่ได้ไล่
- เงื่อนไขโปรโมชั่นละเอียด (SMLPOSControl)
