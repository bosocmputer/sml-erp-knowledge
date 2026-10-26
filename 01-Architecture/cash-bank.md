---
tags: [sml, cash-bank, payment, cheque, wht]
status: from-code + ข้อมูลจริง + capture (เงินสด รอบ 1–4, โอนเงิน รอบ 4, บัตรเครดิต + ขึ้นเงินบัตร รอบ 5.3)
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
- **ใบรับชำระไม่ได้ถูกนับว่า "ถูกใช้"**: กฎ doc flow ของ 239 นับ `ic_trans_detail.doc_ref = RC and trans_flag in (410,411,461)` เป็น `used_status=1` แต่ doc flow ของ 461 ไม่ได้ประมวลผลใบรับชำระต่อ ⇒ `RC26100005.used_status` ยังเป็น 0 · ข้อมูลจริง: ใบรับชำระที่มีเอกสาร 410/411/461 อ้างถึง มี `used_status=1` แค่ kbgtest 112/27,133, samai 31/1,542 ⇒ **อย่าใช้ `used_status` ของใบรับชำระตัดสินว่าเช็ค/บัตรผ่านแล้ว** ให้ดู `cb_chq_list.status` หรือเอกสาร 410/411/461 โดยตรง

## 3. ภาษีหัก ณ ที่จ่าย (`gl_wht_list`)
- คอลัมน์: `doc_date, doc_no, amount, tax_value, status, trans_flag, due_date, line_number, cust_code, card_number, tax_number, cust_tax_type, cust_name, tax_doc_no, cust_address` + รายละเอียดใน `gl_wht_list_detail`
- เขียน/ลบพร้อมเอกสารต้นทาง: ใบรับชำระลบ `gl_wht_list`/`_detail` ตามเลขที่ก่อน insert ([[write-spec-receipt]] §2); แก้ไขเอกสาร `_withHoldingTax._queryDelete(oldDocNo, type)` (`_icTransControl.cs` ~15775)
- หลังบันทึกทุกเอกสาร `_updateDateTimeForCalc` ซ่อม `gl_wht_list_detail.due_date`/`cust_code` ให้ตรงหัว
- ข้อมูลจริง kbgtest: 6,899 ใบ (รายจ่ายอื่น 260 = 3,046, รับชำระ 239 = 1,683, จ่ายชำระ 19 = 1,597, รายได้อื่น 250 = 389, ขาย 44 = 184)

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
