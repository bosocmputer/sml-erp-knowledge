---
tags: [sml, cash-bank, payment, cheque, wht]
status: from-code + ข้อมูลจริง + capture (เงินสด รอบ 1–4, โอนเงิน รอบ 4, บัตรเครดิต + ขึ้นเงินบัตร รอบ 5.3, เช็ครับ → นำฝาก → ผ่าน รอบ 5.4, เช็คจ่าย รอบ 7.7)
source: smlerp SMLAPARControl/_payControl.cs (`_queryInsert` ~594), _advanceControl.cs, SMLERPGlobal/_global.cs (`_payType` ~2151), SMLProcess/_docFlowThread.cs (~958–1100), SMLERPControl/_bank/_chqListControl.cs, _customer/_arStatusForm.cs + DB + capture aoy-run1..3
---
# เงินสด / ธนาคาร: การรับ-จ่ายเงิน, เช็ค, ภาษีหัก ณ ที่จ่าย

กลับไป [[00-Index]] · โมดูล [[module-cashbank]] · บิลขาย [[write-spec-sale-invoice]] · รับชำระ [[write-spec-receipt]] · จ่ายชำระ [[write-spec-ap-payment]]

## 1. โครงสร้าง
- **`cb_trans`** = หัวการรับ/จ่ายเงิน 1 แถวต่อเอกสาร (unique `(doc_no, trans_flag)`) ใช้ `doc_no`/`trans_flag` **ของเอกสารต้นทาง** (บิลขายสด 44, รับชำระ 239, จ่ายชำระ 19, ลดหนี้คืนเงิน 48 …) — ไม่มีเลขเอกสารการเงินแยก
- **`cb_trans_detail`** = รายละเอียดแต่ละช่องทาง (`doc_type`) — เงินสดล้วนไม่มีแถว detail (ยอดอยู่ที่ `cb_trans.cash_amount`)
- **`cb_chq_list`** = ทะเบียนเช็ค/บัตร (สถานะเปลี่ยนตามเอกสารเช็คต่อมา)
- **`gl_wht_list` / `gl_wht_list_detail`** = ภาษีหัก ณ ที่จ่าย
- เขียนโดย `SMLAPARControl._payControl._queryInsert(docNo, docDate, docTime, docFormatCode, remark)` ใน**ชุดเดียวกับเอกสารต้นทาง** (บิลขายสดเรียกเมื่อ `_payControl.Enabled`)

### `cb_trans.pay_type` (`_payType`, `SMLERPGlobal/_global.cs` ~2151)
- **1 = รับเงิน**: ขาย 44, เพิ่มหนี้ขาย, รับเงินล่วงหน้า/มัดจำ, รับคืนเงินล่วงหน้า/มัดจำฝั่งซื้อ, รับชำระหนี้ 239, ตั้งหนี้อื่นลูกหนี้, รายได้อื่น 250, ถอนเงิน, เช็ครับฝาก/ผ่าน/คืน/ยกเลิก/เข้าใหม่/เปลี่ยน, เช็คจ่ายผ่าน/ยกเลิก, บัตรเครดิตผ่าน/ยกเลิก, wallet ผ่าน, เบิกเงินสดย่อย, ขายสินทรัพย์ …
- **2 = จ่ายเงิน**: ซื้อ 12, ตั้งหนี้อื่นเจ้าหนี้, คืนเงินล่วงหน้า/มัดจำฝั่งขาย, **รับคืน/ลดหนี้ขาย 48**, เพิ่มหนี้ซื้อ …
- ยืนยันกับข้อมูล: บิลขายสด/รับชำระ `pay_type=1`; CN26090001 (คืนเงินสด) `pay_type=2` ([[write-spec-credit-note]])

### `cb_trans_detail.doc_type` (ลำดับ insert ใน `_queryInsert`)
| doc_type | ช่องทาง (grid) | คอลัมน์พิเศษที่ใส่ | kbgtest (แถว) |
|---|---|---|---|
| 1 | โอนเงิน (`_payTransferGrid`) | — | 152,615 |
| 2 | เช็ค (`_payChequeGrid`) | `trans_number_type` = ChqType, `ap_ar_type` (1 ลูกหนี้ / 2 เจ้าหนี้), `ap_ar_code` | 36,792 |
| 3 | บัตรเครดิต (`_payCreditCardGrid`) | `trans_number_type` = pay_type, `ap_ar_type`, `ap_ar_code` | 4,819 |
| 4 | เงินสดย่อย (`_payPettyCashGrid`) | — | 43,932 |
| 5 | Deposit (`_payDepositGrid`, ยอดรวมใน `cb_trans.deposit_amount`) | — | 18,504 |
| 6 | เงินล่วงหน้า/มัดจำที่นำมาตัด (`_advanceControl.cs` ~56) | `ap_ar_type`, `ap_ar_code` | 2 |
| 9 | คูปอง (`_payCouponGrid`) | — | — |
| 11 | ค่าใช้จ่ายอื่น (`_gridExpense`) | — | 55,993 |
| 12 | รายได้อื่น (`_gridIncome`) | — | 32,160 |
| 19 | สกุลเงินอื่น (`_payOtherCurrencyGrid`) | — | — |
| 21 | Wallet (`_payWalletGrid`) | `trans_number_type=1`, `ap_ar_type=1`, `ap_ar_code` | — |
- ทุกแถวมี `doc_no, doc_date, doc_time, trans_type, trans_flag` ของเอกสารต้นทาง
- **คำสั่งสุดท้ายของ `_queryInsert`: `delete from cb_trans_detail where trans_number is null or trans_number=''`** — ลบแถวว่างที่ grid สร้าง (เป็นที่มาของคำสั่งนี้ที่เห็นใน capture บิลขาย/ซื้อ/รับชำระ)
- ตอนเปิดเอกสาร โปรแกรมโหลด detail แยกตาม `doc_type` 1, 2, 3, 5, 9, 21 และ 6 (capture aoy-run1 09:00:39)
- แก้ไขเอกสาร (mode 2): `_payControl._queryDelete(oldDocNo)` ก่อน แล้ว insert ใหม่ (`_icTransControl.cs` ~15768)

## 2. เช็ค (`cb_chq_list`)
คอลัมน์: `chq_get_date, chq_type, chq_number, chq_due_date, chq_description, doc_ref, book_code, pass_book_code, bank_code, bank_branch, bank_description, amount, currency_code, owner_name, person_code, side_code, department_code, ap_ar_code, remark, status, guid_code, trans_type, trans_flag, no_approved, credit_card_type, charge, sum_amount, ap_ar_type, doc_line_number, external_chq`

- **`chq_type`**: 1 = เช็ครับ, 2 = เช็คจ่าย (คอมเมนต์ใน `_docFlowThread.cs` ~958); `_chqListControl.cs` ~132 จัด 1 กับ 3 เป็นฝั่งลูกหนี้ และ 2 เป็นฝั่งเจ้าหนี้ — kbgtest: type 3 มีคอลัมน์บัตร (`credit_card_type`) สถานะ 0/1 (ยังไม่ได้ยืนยันว่า 3 = บัตรเครดิต)
- แถวถูกสร้างตอนบันทึกเอกสารที่รับ/จ่ายด้วยเช็ค (`_payControl.cs` ~1653) และจากหน้าจอธนาคาร (`SMLERPControl/_bank/_bankControl.cs` ~1874–1946)
- **สถานะคำนวณใหม่ใน doc flow ทุกครั้ง** จากเอกสารเช็คล่าสุดใน `ic_trans_detail` ที่ `chq_number`, `doc_ref`, `ref_row = doc_line_number` ตรงกัน และ `last_status = 0` (เรียงวันที่/เวลาล่าสุด):

| status | ป้าย (`_arStatusForm.cs` ~112) | เช็ครับ (chq_type 1) จาก flag | เช็คจ่าย (chq_type 2) จาก flag |
|---|---|---|---|
| 0 | เช็คในมือ | ยังไม่มีเอกสารต่อ | ยังไม่มีเอกสารต่อ |
| 1 | เช็คนำฝาก | 410 เช็ครับ_ฝาก | — |
| 2 | เช็คผ่าน | 411 เช็ครับ_ผ่าน | 451 เช็คจ่าย_ผ่าน |
| 3 | เช็ครับคืน | 412 เช็ครับ_คืน | 453 เช็คจ่าย_คืน |
| 4 | เช็คยกเลิก | 413 เช็ครับ_ยกเลิก | 452 เช็คจ่าย_ยกเลิก |
| 5 | เช็คขายลด | (ไม่มีใน mapping ของ doc flow) | — |
| 6 | เช็คคืนนำเข้าใหม่ | 414 เช็ครับ_เข้าใหม่ | — |
| 7 | เช็คเปลี่ยน | 416 เช็ครับ_เปลี่ยนเช็ค | 456 เช็คจ่าย_เปลี่ยนเช็ค |
| 8 | (ตั้งหนี้ใหม่) | 418 เช็ครับ_ตั้งหนี้ใหม่ (จับคู่ด้วย `item_code` แทน `chq_number`) | — |
- เอกสารเช็ค (405/406 ยกมา, 410–418, 451–456) เก็บใน `ic_trans`/`ic_trans_detail` โดยบรรทัดมี `chq_number`, `doc_ref`, `ref_row`
- **เช็คในมือที่นับเพิ่มในหนี้ลูกค้า** (`_arStatusForm`): `chq_type = 1 and status not in (2, 7, 8)`; ตัวเลือก `ar_credit_chq_outstanding` เอายอดเช็คค้างไปบวกยอดหนี้ตอนตรวจวงเงิน ([[write-spec-sale-invoice]] §1.3)
- ข้อมูลจริง kbgtest: เช็ครับ status 2 = 32,106, 7 = 1,369, 0 = 242, 8 = 93 · เช็คจ่าย status 2 = 1,479, 0 = 23

### 2.1 บัตรเครดิต — ยืนยันจากรอบ 5.3 (2026-10-26: รับชำระ RC26100005 10:37:01, ขึ้นเงิน CRD26100001 10:39:49)
**รับชำระด้วยบัตร (239)** — transaction เดียวกับรับชำระเงินสด/โอน ([[write-spec-receipt]] §2) ต่างที่:
- `cb_trans`: `pay_type=1`, **`card_amount=48`**, `cash_amount=0`, `total_credit_charge=0`, `total_amount = total_net_amount = total_amount_pay = 48`
- `cb_trans_detail` 1 แถว: **`doc_type=3`**, `trans_number_type=1`, `ap_ar_type=1`, `ap_ar_code=<ลูกค้า>`, **`trans_number=<เลขบัตร>`**, `no_approved=<เลขอนุมัติ>`, **`credit_card_type=<รหัสใน erp_credit_type>`**, `amount`, `charge=0`, `sum_amount`, `remark`, `line_number=0`
- **`cb_chq_list` ไม่ได้ถูกเขียนใน transaction บันทึก** — เกิดหลัง commit ~3 วินาที ใน doc flow: ลบแถวที่ไม่มี `cb_trans_detail` คู่ → `insert into cb_chq_list (chq_number=<เลขบัตร>, doc_ref=<RC>, chq_get_date, chq_due_date, remark, ap_ar_code, pass_book_code=null, ap_ar_type=1, **chq_type=3**, bank_code=null, amount, sum_amount, charge, trans_type=2, trans_flag=239, no_approved, credit_card_type, doc_line_number=0, external_chq=0)` → ลบแถวซ้ำ
- doc flow บิลที่รับ: `used_status_2=1` (เหมือนเงินสด)

**ขึ้นเงินบัตรเครดิต (461, เมนู เงินสด/ธนาคาร › ธนาคาร › บัตรเครดิต › บันทึกขึ้นเงินบัตรเครดิต)** — ใบแรกของ AOY · transaction เดียว 2 คำสั่ง:
- `ic_trans`: `trans_type=2, trans_flag=461, doc_format_code='CRD', pass_book_code=<สมุดบัญชีที่ขึ้นเงิน>, total_amount=48, total_cost/before_vat/vat=0, is_manual_vat=1, is_pos=0`
- `ic_trans_detail` ต่อบัตร: **`item_code=<รหัสสมุดบัญชี>`** (ไม่ใช่สินค้า), `bank_name`, `bank_branch`, **`chq_number=<เลขบัตร>`, `doc_ref=<ใบรับชำระ>`, `ref_row=<doc_line_number>`**, `price = sum_amount = 48`, `calc_flag=1`
- ไม่มี `cb_trans`, ไม่มี GL (ร้านปิด realtime)
- หลัง commit: ใส่คิว `process` 'IC' ด้วย `wherein=<รหัสสมุดบัญชี>` (คิวว่างเพราะไม่มีสินค้ารหัสนั้น — เป็นผลข้างเคียงของการใช้ `item_code`) → **`update cb_chq_list set status = 1` (461) / 2 (462 ยกเลิก) / 0** จากเอกสาร 461/462 ล่าสุดที่ `chq_number`, `doc_ref`, `ref_row = doc_line_number` ตรงกัน ⇒ สถานะบัตร: 0 = ยังไม่ขึ้นเงิน, 1 = ขึ้นเงินแล้ว, 2 = ยกเลิก
- **ใบรับชำระไม่ได้ถูกนับว่า "ถูกใช้"**: กฎ doc flow ของ 239 นับ `ic_trans_detail.doc_ref = RC and trans_flag in (410,411,461)` เป็น `used_status=1` แต่ doc flow ของ 461 ไม่มี `__queryDocRefForNextProcess` (`_docFlowThread.cs` ~2663) จึงไม่ประมวลผลใบรับชำระต่อ ⇒ `RC26100005.used_status` ยังเป็น 0 · มีแค่ **410 นำฝากเช็ค** ที่ไล่ต่อไปใบรับชำระ (~2611) ดู §2.2 · ข้อมูลจริง: ใบรับชำระที่มีเอกสาร 410/411/461 อ้างถึง มี `used_status=1` แค่ kbgtest 112/27,133, samai 31/1,542 ⇒ **อย่าใช้ `used_status` ของใบรับชำระตัดสินว่าเช็ค/บัตรผ่านแล้ว** ให้ดู `cb_chq_list.status` หรือเอกสาร 410/411/461 โดยตรง

### 2.2 เช็ครับ — ยืนยันจากรอบ 5.4 (2026-10-26: รับชำระ RC26100006 12:06:29, นำฝาก CHD26100001 12:07:48, ผ่าน CHP26100001 12:08:49)
**รับชำระด้วยเช็ค (239)** — ลำดับเดียวกับเงินสด/บัตร ต่างที่:
- `cb_trans`: `pay_type=1`, **`chq_amount=255`**, `cash_amount=0`
- `cb_trans_detail`: **`doc_type=2`**, `trans_number_type=1`, `ap_ar_type=1`, `ap_ar_code`, **`chq_on_hand=0`**, `bank_code`, `bank_branch`, **`trans_number=<เลขเช็ค>`**, `sum_amount = amount`, **`chq_due_date`**, `remark`, `balance_amount=0`, `doc_ref=null`, `line_number`
- `cb_chq_list` เกิดหลัง commit ใน doc flow (เหมือนบัตร): `chq_type=1`, `status` เริ่ม 0, `bank_code`, `bank_branch`, `chq_due_date`, `pass_book_code=null`, `no_approved/credit_card_type=null` · เงื่อนไข `coalesce(chq_on_hand,0)=0` ⇒ เช็คที่ติ๊ก "เช็คในมือ" ไม่ถูกเก็บในทะเบียน
- doc flow บิล: `used_status_2=1`

**นำฝาก (410, CHD) และเช็คผ่าน (411, CHP)** — แต่ละใบ transaction เดียว 2 คำสั่ง รูปแบบเดียวกับ 461:
- `ic_trans`: `trans_flag=410/411`, `doc_format_code='CHD'/'CHP'`, `pass_book_code=<สมุดบัญชี>`, `total_amount` (411 ใส่ `total_value` ด้วย), `is_pos=0`
- `ic_trans_detail` ต่อเช็ค: **`item_code=<รหัสสมุดบัญชี>`**, `bank_name`, `bank_branch`, **`chq_number`, `doc_ref=<ใบรับชำระ>`, `ref_row=<doc_line_number>`**, `sum_amount` (411 มี `date_due`, `price` ด้วย), `calc_flag=1`
- หลัง commit: คิว `process` ด้วยรหัสสมุดบัญชี (ว่าง) → reset `last_status` → ซ่อม `cb_chq_list` → **อัปเดตสถานะเช็คด้วยคำสั่ง `with chq_last_flag as (...)`** จากเอกสารเช็คล่าสุด (418 จับคู่ด้วย `item_code`) ⇒ `status` 0 → 1 (หลัง 410) → **2 (หลัง 411)** ตรงกับตาราง §2
- **410 ไล่ doc flow ต่อไปใบรับชำระ** (`select doc_ref from ic_trans_detail where doc_no=<CHD>`) ⇒ **`RC26100006.used_status = 1` ตั้งแต่นำฝาก** · 411/461 ไม่ไล่ต่อ ⇒ ใบรับชำระที่ขึ้นเงินบัตร หรือเช็คที่บันทึกผ่านโดยไม่นำฝากก่อน จะยัง `used_status=0`
- ไม่มี GL (ร้านปิด realtime)

### 2.3 เช็คจ่าย — ยืนยันจากรอบ 7.7 (จ่ายชำระ PV26100004 จ่าย PU26100003 10 บาท ด้วยเช็ค 0000801, 15:45:32 วันที่ 2026-10-26)
- ลำดับเหมือนจ่ายชำระเงินสด ([[write-spec-ap-payment]] §6) ต่างที่:
  - `cb_trans`: `pay_type=2`, **`chq_amount=10`**, `cash_amount=0`
  - `cb_trans_detail`: `doc_type=2`, **`trans_number_type=2`, `ap_ar_type=2`** (เจ้าหนี้; ฝั่งรับเป็น 1/1), `ap_ar_code=<ผู้ขาย>`, `chq_on_hand=0`, **`pass_book_code=<สมุดบัญชีที่ออกเช็ค>`** (ฝั่งรับไม่มี), `bank_code`, `bank_branch`, `trans_number=<เลขเช็ค>`, `sum_amount = amount`, `chq_due_date`, `remark`, `balance_amount=0`
- `cb_chq_list` เกิดใน doc flow ~3 วินาทีหลัง commit (เหมือนเช็ครับ): **`chq_type=2`, `status=0`**, `ap_ar_type=2`, `pass_book_code='5843697'`, `trans_type=1`, `trans_flag=19`
- doc flow ใบซื้อ: `used_status_2=1`
- **เช็คจ่ายผ่าน 451 (รอบ 8.1, CPP26100001 10:17:32 วันที่ 2026-10-27, เมนู เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › บันทึกเช็คผ่าน)** — รูปแบบเดียวกับเช็ครับผ่าน 411 (§2.2):
  - `ic_trans`: **`trans_type=1`**, `trans_flag=451`, `doc_format_code='CPP'`, `pass_book_code`, `total_amount=10`
  - `ic_trans_detail`: `item_code=<สมุดบัญชี>`, `bank_name`, `bank_branch`, `chq_number`, `date_due`, `doc_ref=<ใบจ่ายชำระ>`, `ref_row=0`, `price = sum_amount = 10`, `calc_flag=1`
  - หลัง commit: คิว `process` ด้วยรหัสสมุดบัญชี (ว่าง) → ซ่อม `cb_chq_list` → **สถานะเช็ค 0 → 2** (ข้ามนำฝาก — เช็คจ่ายไม่มีขั้นนำฝาก)
  - ใบจ่ายชำระ `PV26100004` **`used_status` ยังเป็น 0** (เหมือนเช็ครับผ่าน 411 ที่ไม่ไล่ต่อไปใบรับชำระ)
- ขั้นต่อที่ยังไม่ได้ทดสอบ: 452 ยกเลิก, 453 คืน, 456 เปลี่ยนเช็ค

## 3. ภาษีหัก ณ ที่จ่าย (`gl_wht_list`)
- คอลัมน์: `doc_date, doc_no, amount, tax_value, status, trans_flag, due_date, line_number, cust_code, card_number, tax_number, cust_tax_type, cust_name, tax_doc_no, cust_address` + รายละเอียดใน `gl_wht_list_detail`
- เขียน/ลบพร้อมเอกสารต้นทาง: ใบรับชำระลบ `gl_wht_list`/`_detail` ตามเลขที่ก่อน insert ([[write-spec-receipt]] §2); แก้ไขเอกสาร `_withHoldingTax._queryDelete(oldDocNo, type)` (`_icTransControl.cs` ~15775)
- หลังบันทึกทุกเอกสาร `_updateDateTimeForCalc` ซ่อม `gl_wht_list_detail.due_date`/`cust_code` ให้ตรงหัว
- ข้อมูลจริง kbgtest: 6,899 ใบ (รายจ่ายอื่น 260 = 3,046, รับชำระ 239 = 1,683, จ่ายชำระ 19 = 1,597, รายได้อื่น 250 = 389, ขาย 44 = 184)

### 3.1 ยืนยันจากรอบ 5.8 (2026-10-26: จ่ายชำระ PV26100002 จ่าย PU26100002 120 บาท หัก ภ.ง.ด.53 3% = 3.36, 13:11:02)
- เลขที่หนังสือรับรอง: รูปแบบเอกสาร `screen_code='RWHT'` → `code='RWHT53'` · หาเลขล่าสุดด้วย `select tax_doc_no from gl_wht_list where tax_doc_no <= 'RWHT532610z' order by tax_doc_no desc limit 1` ⇒ ได้ `RWHT5326100001` (รูปแบบ RWHT53 + YYMM + ลำดับ)
- อยู่ใน**transaction เดียวกับใบจ่ายชำระ** ลำดับ: ลบของเลขว่าง (`cb_trans`, `cb_trans_detail`, `gl_wht_list`, `gl_wht_list_detail`, `gl_journal_vat_buy`) → `ap_ar_trans` → `ap_ar_trans_detail` → **`gl_wht_list`** → **`gl_wht_list_detail`** → `cb_trans` → cleanup → `COMMIT`
- `gl_wht_list` (13 คอลัมน์): `doc_no=<PV>, doc_date, tax_doc_no=<RWHT…>, due_date, amount=<ฐาน 112.15>, tax_value=3.36, cust_code, trans_flag=19, cust_name, cust_address` (คัดจากข้อมูลผู้ขาย), **`cust_tax_type=1`** (นิติบุคคล), `card_number=''`, `tax_number=''`
- `gl_wht_list_detail` ต่อบรรทัด: `line_number=1` (เริ่ม 1), `doc_no, tax_doc_no, trans_flag, income_type=<ข้อความช่องรายละเอียด>, amount=112.15, tax_rate=3.00, tax_value=3.36, due_date, cust_code`
- `cb_trans`: `pay_type=2` (จ่าย), `cash_amount=116.64`, **`total_tax_at_pay=3.36`**, `total_amount = total_net_amount = total_amount_pay = 120` ⇒ ยอดหักภาษีนับเป็นส่วนหนึ่งของยอดจ่าย · **ไม่มี `cb_trans_detail`** (จ่ายเงินสดอย่างเดียว)
- `ap_ar_trans_detail`: `bill_type=12, sum_debt_amount = balance_ref = sum_pay_money = 120` (เต็มยอดรวมภาษีหัก)
- doc flow: ใบซื้อ `used_status_2=1`
- หน้าจอ: ระหว่างกรอก ช่อง "เอกสารวันที่" แสดง `/2569` ผู้ใช้พิมพ์วันที่ใหม่ก่อนบันทึก — ค่าที่บันทึกจริง `2026-10-26` · ยังไม่รู้ว่าอาการนี้ทำให้ค่าผิดหรือแค่แสดงผิด

### 3.2 รอบ 7.8: รับชำระที่ลูกค้าหัก ณ ที่จ่าย แบบพิมพ์ยอดตรง (RC26100007 รับ INV26100003 247, 15:48:45 วันที่ 2026-10-26)
- `cb_trans`: `pay_type=1, cash_amount=244.69, **total_tax_at_pay=2.31**, total_amount = total_net_amount = total_amount_pay = 247` · `ap_ar_trans_detail sum_pay_money=247` · บิล `used_status_2=1`
- **ไม่มี `insert gl_wht_list` / `gl_wht_list_detail`** ใน transaction (มีแค่ลบของเลขว่าง) และไม่มีใน DB ⇒ ยอดภาษีถูกหักอยู่ใน `cb_trans.total_tax_at_pay` อย่างเดียว ไม่มีหนังสือรับรอง
- **ผู้ทดสอบพิมพ์ 2.31 ตรงในช่อง "ภาษีถูกหัก ณ ที่จ่าย" ของแท็บรายละเอียดการรับเงิน (ไม่ได้เพิ่มรายการในแท็บภาษีถูกหัก)** ⇒ **ช่องนี้แก้ได้เองและบันทึกแค่ `cb_trans.total_tax_at_pay`** ไม่สร้างหนังสือรับรอง/ทะเบียนภาษีถูกหัก — ต่างจากฝั่งจ่ายรอบ 5.8 ที่ช่องเดียวกันคำนวณจากแท็บ (ล็อกไว้)
- ข้อมูลจริง kbgtest: ใบรับชำระ 239 มี `gl_wht_list` 1,683 ใบ ⇒ เมื่อกรอกผ่านแท็บภาษีถูกหัก ฝั่งรับเขียน `gl_wht_list` (ยังไม่ได้ดักจับแบบนี้)
- ⇒ รายงานภาษีถูกหัก ณ ที่จ่ายที่อ่าน `gl_wht_list` จะไม่เห็นยอดที่พิมพ์ตรง

### 3.3 รอบ 7.8b: รับชำระแบบเพิ่มรายการในแท็บภาษีถูกหัก (RC26100008 รับ INV26100005 240, 16:17:24 วันที่ 2026-10-26)
- ลำดับใน transaction เดียวกับฝั่งจ่าย (§3.1): `ap_ar_trans` → `ap_ar_trans_detail` → **`gl_wht_list`** → **`gl_wht_list_detail`** → `cb_trans` → `COMMIT`
- `gl_wht_list`: `doc_no=<RC>, doc_date, **tax_doc_no=<ช่อง "เอกสารเลขที่" ที่ผู้ใช้พิมพ์>** (ฝั่งรับไม่ออกเลข `RWHT…` ให้ — เป็นเลขหนังสือรับรองของลูกค้า), due_date, amount=224.30, tax_value=2.24, cust_code, **trans_flag=239**, cust_name, cust_address (จากลูกค้า), cust_tax_type=1, card_number='', tax_number=''`
- `gl_wht_list_detail`: `line_number=1, doc_no, tax_doc_no, trans_flag=239, income_type=<รายละเอียด>, amount=224.30, tax_rate=1.00, tax_value=2.24, due_date, cust_code`
- `cb_trans`: `cash_amount=237.76, total_tax_at_pay=2.24, total_amount_pay=240` — **เหมือนแบบพิมพ์ยอดตรง (§3.2) ทุกค่า ต่างกันแค่มี/ไม่มีแถว `gl_wht_list`**
- บิล `used_status_2=1`
- **สำหรับ sml_mcp_ai:** รับชำระที่ลูกค้าหักภาษีต้องเขียน `gl_wht_list` + `_detail` (`trans_flag=239`) ด้วย ไม่ใช่แค่ `total_tax_at_pay`

## 3.5 เงินรับล่วงหน้า (40) — ยืนยันจากรอบ 8.3 (DPS26100001 100 บาท ลูกค้า ZZCUST-0001, 10:24:45 วันที่ 2026-10-27)
เมนู ขาย › รับเงินล่วงหน้า (4.11) · จอ `_po_so_deposit_control`
- **Transaction:** `insert into ic_trans(trans_type=2, trans_flag=40, doc_date, doc_time, doc_no, doc_format_code='DPS', cust_code, deposit_day=0, deposit_date, doc_ref, doc_ref_date, remark, total_value=100, total_amount=100, cashier_code, creator_code, create_datetime)` (17 คอลัมน์, **ไม่มี `vat_type`/ยอดภาษี → ค่าเริ่มต้น 0**) → `ap_ar_trans_detail (doc_no, doc_date, trans_type=2, trans_flag=40, sale_shift_id='', remark='เงินล่วงหน้า', sum_debt_amount=100, line_number=0)` + แถวว่าง line 1 (ถูกลบโดย cleanup ในรอบนี้) → **`cb_trans` (`doc_format_code='DPS', pay_type=1`, `cash_amount=100`, `total_amount_pay=100`)** → cleanup → `COMMIT`
- **ไม่มี `ic_trans_detail` และไม่มี `gl_journal_vat_sale`** ⇒ ร้านนี้รับเงินล่วงหน้าโดยไม่ออกใบกำกับภาษี
- สถานะหลังบันทึก: `used_status=0, used_status_2=0, doc_success=0`
- **ตัดในบิลขาย (รอบ 8.4, INV26100007 10:32:20 วันที่ 2026-10-27 — ขายสด 26.75 ตัดเงินล่วงหน้าเต็มยอดบิล):**
  - `cb_trans`: **`deposit_amount=26.75`**, `cash_amount=0`, `total_amount = total_net_amount = total_amount_pay = 26.75` · `ic_trans.advance_amount=0` (ไม่ได้ใช้คอลัมน์นี้)
  - **`cb_trans_detail`: `doc_type=5`, `trans_number='DPS26100001'`, `doc_date_ref`, `sum_amount=100` (ยอดใบล่วงหน้า), `balance_amount=100` (คงเหลือก่อนตัด), `amount=26.75` (ยอดที่ตัด)** + แถวว่าง line 1 (`trans_number=null`) ที่ถูกลบโดย cleanup `trans_number is null`
  - ภาษีขาย `gl_journal_vat_sale` ของบิลคิดจากยอดเต็ม (ฐาน 25 ภาษี 1.75) — ตอนรับเงินล่วงหน้าไม่ได้ออกภาษี
  - doc flow: **`DPS26100001` `used_status=1, used_status_2=1, doc_success=0`** (ตัดบางส่วน เหลือ 73.25) — ยอดคงเหลือคำนวณจาก Σ `cb_trans_detail.amount` ที่ `doc_type=5, trans_number=<DPS>`
- เลขบิล `INV26100007` เป็นเลขเดียวกับบิลที่ถูกลบในรอบ 7.3 ⇒ **เลขของเอกสารที่ถูกลบถูกนำกลับมาใช้**

## 3.6 ค่าใช้จ่ายอื่น (260) — ยืนยันจากรอบ 8.5 (EPI-26100001 ผู้ขาย ZZSUP-0001 50 บาท เงินสด, 10:36:57 วันที่ 2026-10-27)
เมนู เงินสด/ธนาคาร › ค่าใช้จ่ายอื่นๆ (8.5) · หน้าจอเอกสารกลาง (`_clone_icTrans`)
- **Transaction:** `ic_trans` → `ic_trans_detail` → `cb_trans` → cleanup → `gl_journal_vat_buy` → `COMMIT`
- `ic_trans`: **`trans_type=2`** (ตาม `_transType()` แม้เป็นรายจ่าย), `trans_flag=260`, `cust_code=<ผู้ขาย>`, `doc_format_code='EPI'`, `tax_doc_no = doc_no`, `inquiry_type=1`, `vat_type=1` (รวมใน), `credit_day=30` (จากผู้ขาย), `total_amount=50`, `total_before_vat=46.73`, `total_vat_value=3.27`
- `ic_trans_detail`: **`item_code=<รหัสค่าใช้จ่าย ใน erp_expenses_list>` (5001), `item_name`=ชื่อค่าใช้จ่าย**, `sum_amount=50`, `sum_amount_exclude_vat=46.73`, **ไม่มี qty/price/unit/คลัง**, `stand_value=0, divide_value=0`, `ref_row=-1`, `calc_flag=1` (260 ไม่อยู่ในสูตรสต็อก)
- `cb_trans`: `doc_format_code='EPI', pay_type=2, trans_type=2, trans_flag=260, cash_amount=50, total_amount_pay=50`
- **`gl_journal_vat_buy`: `trans_type=2`, `vat_calc=1`, ฐาน 46.73 ภาษี 3.27** ⇒ ค่าใช้จ่ายอื่นเข้ารายงานภาษีซื้อ

## 3.7 โอนเงินระหว่างธนาคาร (422 + 420) — ยืนยันจากรอบ 8.6 (TM26100001 100 บาท จาก 5843697 SCB ไป 68667871 KBANK, 10:51:24 วันที่ 2026-10-27) — ใบแรกของ AOY
เมนู เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › บันทึกโอนเงินระหว่างธนาคาร
- **เลขเดียว 2 เอกสาร ใน transaction เดียว:** `ic_trans` 422 (โอนออก) + `ic_trans` 420 (โอนเข้า) เลขที่ `TM26100001` ทั้งคู่ → `ic_trans_detail` ของแต่ละ flag → `COMMIT`
- `ic_trans` (16 คอลัมน์): **`trans_type=0`**, `trans_flag=422/420`, `doc_format_code='TM'`, `remark`, `total_amount=100`, `total_amount_2=0` — ไม่มี `pass_book_code` ที่หัว
- `ic_trans_detail`: **422: `item_code=<บัญชีต้นทาง>`, `bank_name/bank_branch`, `item_code_2=<บัญชีปลายทาง>`, `bank_name_2/bank_branch_2`** · 420: สลับต้นทาง/ปลายทาง · `transfer_amount=100, fee_amount=0, sum_amount=100` · **`calc_flag`: 422 = 1, 420 = -1** (ตรงกับ `_transStockCalcType`) · `ref_row=-1`
- **ไม่มี `cb_trans`/`cb_trans_detail`** และ**ไม่มีการอัปเดตยอดใน `erp_pass_book`** ⇒ ยอดคงเหลือในสมุดบัญชีต้องคำนวณจากเอกสาร (รายงาน)
- หลัง commit: `logs` + doc flow reset `last_status` ของทั้ง 420 และ 422
- ค่าธรรมเนียมโอน (`fee_amount`) ยังไม่ได้ทดสอบ

## 4. สำหรับ sml_mcp_ai
- ช่องทางที่ยืนยันด้วย SQL จริงแล้วมีแค่ **เงินสด** (`cb_trans` อย่างเดียว) — เปิดเขียนเฉพาะเงินสดก่อน
- **โอนเงินยืนยันแล้ว (รอบ 4)**: `cb_trans_detail` doc_type 1 = 13 คอลัมน์ `doc_no, doc_date, doc_time, trans_type, trans_flag, doc_type=1, chq_due_date, trans_number=<erp_pass_book.code ตัวพิมพ์ใหญ่>, bank_code, bank_branch, amount, remark, line_number` + `cb_trans.tranfer_amount` ([[write-spec-receipt]] §6)
- บัตร/เช็ค/อื่น ๆ: ยังต้อง capture 1 ครั้งต่อช่องทางก่อนเปิด
- รับเช็ค ⇒ ต้องสร้างแถว `cb_chq_list` (status 0) ด้วย ไม่เช่นนั้นเช็คจะไม่อยู่ในทะเบียนและหน้าจอฝาก/ผ่านเช็คหาไม่เจอ

## 5. ยังไม่ทราบ
- คอลัมน์ครบของ `cb_trans_detail` ต่อ `doc_type` (ต้องดูคอลัมน์ของแต่ละ grid หรือ capture)
- `chq_type = 3` และ status 5 (ขายลด) เกิดจากเอกสารไหน
- เอกสารฝาก/ผ่านเช็ค (410/411) เขียน `cb_trans` อย่างไร
- GL ของภาษีหัก ณ ที่จ่าย และหนังสือรับรองการหักภาษี
