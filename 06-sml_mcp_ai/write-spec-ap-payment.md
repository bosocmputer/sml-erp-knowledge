---
tags: [sml, sml_mcp_ai, write-spec, ap, payment]
status: verified-runtime รอบ 4 (PV26100001 จ่ายเงินสด 1 บิล) · สูตรยอดเจ้าหนี้ค้าง from-code
source: smlerp SMLERPARInfo/_process.cs (`_createQuery` ~624–860, `_arBalanceDoc` ~1228), SMLAPARControl/_ar_ap_trans.cs, _ar_ap_trans_grid.cs (~818) + DB kbgtest (2026-10-21) + capture รับชำระ aoy-run3 (เทียบ)
---
# สเปกการบันทึก: จ่ายชำระหนี้ (trans_flag 19) และยอดเจ้าหนี้คงค้าง

กลับไป [[00-Index]] · ซื้อ [[write-spec-purchase]] · ฝั่งลูกหนี้ (verified) [[write-spec-receipt]] · เงินสด/ธนาคาร [[cash-bank]] · โมดูล [[module-ap]]

> ✅ การบันทึกใบจ่ายชำระยืนยันแล้วในรอบ 4 (§6) · สูตรยอดเจ้าหนี้ค้าง (§1) ยังมาจากโค้ด (ฟังก์ชันเดียวกับฝั่งลูกหนี้ที่ verified)

## 1. ไม่มีตาราง "ตั้งเจ้าหนี้" แยก — ยอดค้างคำนวณจากเอกสาร
`_createQuery(mode = เจ้าหนี้_ยอดคงเหลือตามเอกสาร)` สร้าง union ของ (ทุกส่วน `coalesce(last_status,0)=0`):

| ส่วน | เอกสาร (`ic_trans`) | ยอด | หักด้วย |
|---|---|---|---|
| 1 ซื้อเชื่อ | **12 ที่ `inquiry_type in (0,2)`** | `+total_amount` | Σ(`sum_pay_money` + `lost_profit_exchange_amount`) ของ `ap_ar_trans_detail` ที่ `trans_flag = 19`, `billing_no = doc_no`, `bill_type = trans_flag` |
| 4 เพิ่มหนี้/ตั้งหนี้ | **14** (เพิ่มหนี้/ราคาผิด), **315** ซื้อพาเชียล-ตั้งหนี้ (`inquiry_type in (0,2)`), **316** พาเชียล-เพิ่มหนี้, **81** ตั้งหนี้ยกมา, **87** ตั้งหนี้อื่น, **83** เพิ่มหนี้ยกมา, **89** เพิ่มหนี้อื่น, **260/264** รายจ่ายอื่น/เพิ่มหนี้ (`inquiry_type in (0,2)`); (+ **11** จ่ายมัดจำ `inquiry_type=1` เฉพาะ OEM `imex`) | `+total_amount` | Σ `sum_pay_money` ของใบจ่ายชำระ 19 |
| 2 ลดหนี้ | **16** ส่งคืน/ลดหนี้ (`inquiry_type in (0,1)`), **317** พาเชียล-ลดหนี้ (`inquiry_type in (0,1)`), **85** ลดหนี้ยกมา, **262** รายจ่ายอื่น-ลดหนี้ (`inquiry_type in (0,2)`), **91** ลดหนี้อื่น | `−total_amount` | Σ `sum_pay_money` ของใบจ่ายชำระ 19 (ตามโครงสร้างโค้ด ~183 เดียวกับส่วน 4) |
- `due_date`: 81/83/85 ใช้ `due_date` (อายุเจ้าหนี้), อื่น ๆ ใช้ `credit_date`
- `ref_doc_no` แสดงเฉพาะ 14, 81, 83, 85, 93, 95, 97, 315, 260
- ⚠️ เงื่อนไข `inquiry_type` ของลดหนี้ฝั่งซื้อ (16/317) คือ `(0,1)` — **ไม่เหมือน**ฝั่งขาย (48 ใช้ `(0,2,4)`)
- ข้อมูลจริง kbgtest: แถวใบจ่ายชำระ 19 อ้าง `bill_type` = 12 (41,657), 260 (25,311), 315 (5,235), 91 (4,658), 16 (3,189) — ตรงกับตารางข้างบน

## 2. โครงสร้างใบจ่ายชำระ (ข้อมูลจริง kbgtest 11,252 ใบ)
- `ap_ar_trans`: `trans_flag=19`, **`trans_type=1`** (ทุกใบ), `cust_code` = รหัสผู้ขาย, `total_net_value`
- `ap_ar_trans_detail` ต่อเอกสารที่จ่าย: `billing_no`, **`bill_type` = trans_flag ของเอกสาร**, `sum_debt_amount`, `balance_ref`, `sum_pay_money` (รูปแบบเดียวกับใบรับชำระ)
- `cb_trans`: **`pay_type=2`** (ทุกใบ) — ช่องทางจ่ายใน `cb_trans_detail` ตาม [[cash-bank]] (เช็คจ่าย → `cb_chq_list.chq_type=2`)
- ภาษีหัก ณ ที่จ่าย: หน้าจอสร้าง `_withHoldingTax(SMLERPGLControl._withHoldingTaxType.เจ้าหนี้_จ่ายชำระหนี้…)` (`_ar_ap_trans.cs` ~317) → `gl_wht_list` (kbgtest: 1,597 ใบของ 19)
- ภาษีซื้อในใบจ่ายชำระ: หน้าจอโหลด `_vatBuy` และซ่อนคอลัมน์อ้างอิง (`_checkHideGridVatRefColumn`, ~3696) — ภาษีซื้อที่เกิดตอนจ่าย (เช่น ค่าบริการ) ยังไม่ได้ไล่ว่าเขียน `gl_journal_vat_buy` อย่างไร
- เลขที่: ถ้าใช้ auto-run รายวัน `_g.g._getAutoRun(เจ้าหนี้_ลูกหนี้รายวัน, …)` (~958, ใช้ร่วมกับ 239, 213, 235)
- `doc_time` = เวลาปัจจุบันตอนเปิดเอกสาร (~3473 ทั้ง 19 และ 239)

## 3. ลำดับบันทึก
**ข้อเท็จจริงที่มี:**
- ใบจ่ายชำระ 19 ใช้หน้าจอและคลาสบันทึกเดียวกับใบรับชำระ 239 (`SMLAPARControl._ar_ap_trans`) — ลำดับที่เห็นจริงของ 239 อยู่ใน [[write-spec-receipt]] §2
- doc flow หลังบันทึก (`_docFlowThread.cs` ~165, ~184): `used_status_2=1` ให้ `ic_trans` trans_flag `12, 310, 14, 16, 317, 311, 316, 315` และ `260, 262, 264` ที่มีแถว `ap_ar_trans_detail` ของ **213 (รับวางบิล) หรือ 19** (`last_status=0`) อ้าง `billing_no` — ไม่ดูว่าจ่ายครบหรือไม่ (เหมือนฝั่งลูกหนี้)

**ตอบแล้วในรอบ 4:** ลำดับคำสั่งจริง, ตาราง VAT ที่ลบ (`gl_journal_vat_buy`) และคอลัมน์ครบ ดู §6 · ยังไม่ทราบ: การเขียน `gl_wht_list` ฝั่งเจ้าหนี้, ภาษีซื้อที่เกิดตอนจ่าย

## 4. สำหรับ sml_mcp_ai
- **อ่าน (เปิดได้):** ยอดเจ้าหนี้ค้างรายเอกสาร/รายผู้ขาย ด้วยสูตรข้อ 1 (อ่านอย่างเดียว ความเสี่ยงต่ำ; ทดสอบเทียบกับรายงานเจ้าหนี้คงค้างของ SML ก่อนใช้จริง)
- **เขียนใบจ่ายชำระ: ยังไม่เปิด** จนกว่าจะ capture ใบจ่ายชำระเงินสด 1 ใบ (ยืนยันข้อ 3) — งานจ่ายเงินมีความเสี่ยงสูง และโดยปกติไม่ควรให้ AI สร้างเองโดยไม่มีคนอนุมัติ

## 5. ยังไม่ทราบ
- SQL จริงของการบันทึก 19 (ลำดับ, ตาราง VAT ที่ลบ, WHT)
- ใบรับวางบิล (213) เขียนอะไร และทำไมทำให้ `used_status_2=1` เหมือนจ่ายแล้ว
- `lost_profit_exchange_amount` ฝั่งเจ้าหนี้ (หลายสกุลเงิน)
- ภาษีซื้อที่บันทึกตอนจ่ายชำระ

## 6. ยืนยันจากรอบ 4: จ่ายชำระเงินสด PV26100001 จ่าย PU26100001 (16:22:03)
**Transaction เดียว** (ลำดับเดียวกับใบรับชำระ [[write-spec-receipt]] §2):
1. ลบก่อน: `delete from cb_trans where doc_no=? and trans_flag=19 and trans_type=1` → `cb_trans_detail` (`doc_type<>6`) → `gl_wht_list` → `gl_wht_list_detail` → **`gl_journal_vat_buy`** (ใบรับชำระลบ `_vat_sale`)
2. `insert ap_ar_trans` (18 คอลัมน์): `trans_type=1, trans_flag=19, doc_date, doc_time, doc_no, cust_code=<ผู้ขาย>, doc_format_code='PV', project_code, allocate_code, job_code, side_code, department_code, doc_group, remark, is_manual_vat=0, total_net_value=260.00, creator_code, create_datetime`
3. `insert ap_ar_trans_detail` (15): `trans_type=1, trans_flag=19, billing_no='PU26100001', billing_date, ref_doc_no, ref_doc_date, due_date, doc_ref, sum_debt_amount=260, balance_ref=260, sum_pay_money=260, bill_type=12, line_number=0`
4. `insert cb_trans` (22 คอลัมน์): `doc_format_code='PV', doc_no, doc_date, doc_time, ap_ar_code, **pay_type=2**, trans_type=1, trans_flag=19, remark, total_amount, cash_amount=260, total_expense_other, total_income_amount, petty_cash_amount, deposit_amount, total_tax_at_pay, chq_amount, tranfer_amount, discount_amount, total_income_other, total_net_amount, total_amount_pay`
5. `delete cb_trans_detail …ว่าง` → ลบ GL 7 ตารางของเลขที่นี้ → ลบบรรทัดว่าง → `update ic_trans set due_date … where doc_no=<PV>` → `COMMIT`
- doc flow 16:22:09: **PU26100001 `used_status_2=1`**
- ⇒ ข้อ 3 "ยังไม่ทราบ" เดิมตอบแล้ว: ลำดับและตารางตามนี้ (WHT/VAT ซื้อในใบจ่ายชำระยังไม่ได้ทดสอบ)

## 7. ยืนยันจากรอบ 5.8: จ่ายชำระแบบหัก ณ ที่จ่าย (PV26100002 จ่าย PU26100002, 13:11:02 วันที่ 2026-10-26)
- ลำดับเหมือน §6 + `gl_wht_list`/`gl_wht_list_detail` แทรกหลัง `ap_ar_trans_detail` ก่อน `cb_trans` — รายละเอียด [[cash-bank]] §3.1
- ยอดหักภาษีอยู่ใน `cb_trans.total_tax_at_pay` และนับรวมในยอดจ่าย: `cash_amount 116.64 + total_tax_at_pay 3.36 = total_amount_pay 120` · ยอดตัดเจ้าหนี้ (`sum_pay_money`) = 120 เต็มจำนวน
- **สำหรับ sml_mcp_ai:** ต้องออกเลข `RWHT…` จาก `erp_doc_format` (screen_code RWHT) ใน transaction เดียวกัน และส่ง `cust_tax_type` (1 นิติบุคคล) ให้ตรงกับแบบ ภ.ง.ด.

## 8. ยืนยันจากรอบ 5.9: ใบรับวางบิลเจ้าหนี้ → จ่ายชำระตามใบรับวางบิล (PB26100001 13:18:18, PV26100003 13:19:23 วันที่ 2026-10-26)
**ใบรับวางบิล (213)** — transaction เดียว: `ap_ar_trans` → `ap_ar_trans_detail` ต่อใบซื้อ → cleanup → `COMMIT` (ไม่มี `cb_trans`)
- `ap_ar_trans`: `trans_type=1, trans_flag=213, doc_format_code='PB', cust_code, due_date = doc_date + credit_day (30 วัน), credit_day=30, doc_ref=null, remark, total_net_value=111600`
- `ap_ar_trans_detail`: `trans_flag=213, billing_no=<ใบซื้อ>, billing_date, due_date, sum_debt_amount = balance_ref = sum_pay_money = 111600, bill_type=12, doc_ref=null`
- doc flow: ใบซื้อ `PU26090001` **`used_status_2=1` ตั้งแต่รับวางบิล** (ก่อนจ่าย)

**จ่ายชำระตามใบรับวางบิล (19)** — เหมือน §6 ต่างที่:
- `ap_ar_trans_detail` ของใบซื้อ: **`doc_ref='PB26100001'`** (ใบจ่ายตรงไม่มีค่า)
- **แถวเอกสารอ้างอิง:** `insert ap_ar_trans_detail (trans_type=1, trans_flag=99, doc_date, doc_no=<PV>, billing_no=<PB>, billing_date, remark, line_number=0)` + แถวว่าง line 1 (ถูกลบโดย cleanup ใน transaction เดียวกัน) — รูปแบบเดียวกับฝั่งลูกหนี้ ([[write-spec-receipt]] §6)
- doc flow: **`PB26100001` `used_status=1, doc_success=1`** ⇒ กฎ `_docFlowThread.cs` ~2442 ที่นับ `ap_ar_trans_detail.trans_flag in (99)` **ถูกต้อง** — 99 ในตารางนี้คือแถวอ้างอิงของจอวางบิล/รับ-จ่ายชำระ ไม่ใช่ `ลูกหนี้_ตั้งหนี้อื่น` (ข้อสงสัยใน KB ทีม SML ดู [[team-review-2026-10-26-sml-team-kb]] ข้อ ข.)
- ข้อมูลเดิมใน AOY: ใบรับวางบิลที่จ่ายโดยไม่ผ่านใบรับวางบิล (ไม่มีแถว 99) `used_status=0` · มี 3 ใบ (PB26040010–12) ที่มีแถว 99 ของใบจ่ายที่ไม่ถูกยกเลิก แต่ `used_status=0, doc_success=1` ⇒ doc flow ของใบนั้นไม่ได้รันหลังจ่าย (ถ้าคำนวณใหม่ตามกฎจะได้ 1) — **อย่าใช้ `used_status` ของใบรับวางบิลเป็นตัวตัดสินอย่างเดียว** ให้ดูแถว 99 / `doc_ref` ของใบจ่ายด้วย
- **สำหรับ sml_mcp_ai:** จ่ายตามใบรับวางบิลต้องเขียนทั้ง `doc_ref=<PB>` ในบรรทัดใบซื้อ และแถว `trans_flag=99` ชี้ PB
