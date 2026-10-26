---
tags: [sml, sml_mcp_ai, write-spec, receipt, verified-runtime]
status: verified-runtime (เงินสด 1 บิล รอบ 3; ตามใบวางบิล + โอนเงิน รอบ 4) / from-code (ส่วนที่ระบุ)
source: capture aoy-run3 (RC26100003 รับชำระ INV26100002, 10:39–10:42) + DB aoy + smlerp SMLProcess/_docFlowThread.cs
---
# สเปกการบันทึก: รับชำระหนี้ (trans_flag 239)

กลับไป [[00-Index]] · บิลขาย [[write-spec-sale-invoice]] · สายเอกสาร [[doc-flow-rules]]

> **ขอบเขต:** รับชำระ**เงินสด**เต็มจำนวนสำหรับบิลขายเชื่อ 1 ใบ (INV26100002, 600.00)
> **ยังไม่ครอบคลุม:** จ่ายบางส่วน, หลายบิล, รับด้วยบัตร/เช็ค/โอน, ส่วนลด/ภาษีหัก ณ ที่จ่าย, กำไรขาดทุนจากอัตราแลกเปลี่ยน, รับชำระจากใบวางบิล (235), แก้ไข/ยกเลิก (240)
> รอบ 2 (09:48) ผู้ใช้ทำแต่**ไม่ได้บันทึกสำเร็จ** ไม่มี `insert ap_ar_trans` — ใช้รอบ 3 (10:41) เท่านั้น

## 0. ลำดับเหตุการณ์จริง (รอบ 3)
| เวลา | ขั้น | transaction |
|---|---|---|
| 10:39:52–53 | `erp_doc_format code='RC'` → `select doc_no from ap_ar_trans where (doc_date >= '<ต้นปี>') and doc_no like ? AND trans_flag = 239 order by doc_no desc limit 1` (หาเลขที่จาก **`ap_ar_trans`** ไม่ใช่ `ic_trans`) | อ่าน |
| 10:39:56–10:40:00 | เลือกลูกค้า → `select credit_day from ar_customer_detail where ar_code=?` | อ่าน |
| 10:40:33.461 | **ดึงบิลค้างชำระของลูกค้า** (ข้อ 1) | อ่าน |
| 10:41:00.8–01.2 | อ่าน `erp_company_profile`, `erp_option`, สิทธิ์ผู้ใช้ | อ่าน |
| 10:41:01.251–.364 | **`BEGIN` → ข้อ 2 → `COMMIT`** | **1 transaction** |
| 10:41:01.708 / .852 | `logs` / `erp_logs` | แยก |
| 10:41:45–49 | doc flow (ข้อ 3) — ห่าง 44 วินาที (ตรงกับรูปแบบ "พิมพ์ก่อนแล้วค่อยทำงานหลังบันทึก" ของหน้าจออื่น แต่ยังไม่ได้ไล่โค้ดของหน้าจอรับชำระ) | หลาย transaction |

## 1. ยอดค้างรายบิล (SQL จริง 10:40:33.461)
บิลที่แสดงให้เลือก = แถวที่ `ar_balance <> 0` จาก union ของ (ทุกตัว `coalesce(last_status,0)=0`, `doc_date <= วันที่รับ`, ลูกค้าในช่วงที่เลือก):

| ส่วน | เอกสาร | `amount` | `ar_balance` |
|---|---|---|---|
| ขายเชื่อ | `ic_trans` 44 ที่ `inquiry_type in (0,2)` | `total_amount` | `total_amount − Σ(sum_pay_money + lost_profit_exchange_amount)` |
| เพิ่มหนี้/อื่น | `ic_trans` 46, 93, 95, 99, 101, 418, (250, 254 ที่ `inquiry_type in (0,2)`) | `total_amount` | `total_amount − Σ sum_pay_money` |
| ลดหนี้ | `ic_trans` 48 (`inquiry_type in (0,2,4)`), 97, 103, (252 ที่ `inquiry_type in (0,2)`) | `−total_amount` | `−(total_amount + Σ sum_pay_money)` |
| ขายสินทรัพย์ | `as_trans` 1802 ที่ `inquiry_type in (0,2)` | `total_amount` | เหมือนขายเชื่อ |

- Σ มาจาก `ap_ar_trans_detail` ที่ `trans_flag in (239)`, `coalesce(last_status,0)=0`, **`billing_no = doc_no` และ `bill_type = trans_flag ของเอกสาร`** ← ต้องใส่ `bill_type` ให้ถูก ไม่เช่นนั้นยอดจะไม่ถูกหัก
- `due_date` = `credit_date` (93/95/97 ใช้ `due_date`, 418 ใช้ `doc_date`); `due_day` = วันที่รับ − due_date (ถ้าบวก)
- เรียงตาม `due_date, doc_date, doc_no`

## 2. Transaction หลัก (10:41:01.251–.364)
ลำดับจริง:
1. **ลบของเดิมตามเลขที่ก่อนเสมอ** (แม้เป็นใบใหม่): `delete from cb_trans where doc_no=? and trans_flag=239 and trans_type=2` → `delete from cb_trans_detail … and doc_type<>6` → `delete from gl_wht_list …` → `delete from gl_wht_list_detail …` → `delete from gl_journal_vat_sale where doc_no=? and trans_flag=239`
2. `insert ap_ar_trans` (12 คอลัมน์): `trans_type=2, trans_flag=239, doc_date, doc_time, doc_no, cust_code, doc_format_code='RC', sale_code, remark, total_net_value (600.00), creator_code, create_datetime`
3. `insert ap_ar_trans_detail` (15 คอลัมน์ ต่อบิลที่รับ): `trans_type=2, trans_flag=239, doc_date, doc_no, billing_no='INV26100002', billing_date, ref_doc_no=null, ref_doc_date=null, due_date, doc_ref=null, sum_debt_amount (600 = ยอดบิล), balance_ref (600 = ยอดค้างก่อนรับ), sum_pay_money (600 = ยอดที่รับ), bill_type=44 (= trans_flag ของบิล), line_number=0`
   - ⚠️ ความหมายของ `bill_type` ต่างกันตามเอกสาร: ในใบรับชำระ = trans_flag ของบิล (44); ในบิลขายที่อ้างใบสั่งขาย = ประเภทการอ้างอิง (3) ดู [[write-spec-sale-invoice]] §2.4
4. `insert cb_trans` (25 คอลัมน์): `doc_format_code='RC', doc_no, doc_date, doc_time, ap_ar_code, pay_type=1, trans_type=2, trans_flag=239, remark, total_amount, cash_amount, total_credit_charge, total_income_amount, total_expense_other, petty_cash_amount, deposit_amount, total_tax_at_pay, chq_amount, tranfer_amount, card_amount, coupon_amount, discount_amount, total_income_other, total_net_amount, total_amount_pay` (เงินสด 600 ช่องอื่น 0) — ต่างจาก `cb_trans` ของบิลขายสด (31 คอลัมน์) ที่มี `pay_cash_amount, money_change, point_*, wallet_amount` เพิ่ม
5. `delete from cb_trans_detail where trans_number is null or trans_number=''`
6. ลบ GL ของเลขที่นี้: `gl_journal`, `gl_journal_detail`, `gl_journal_side_list`, `gl_journal_job_list`, `gl_journal_project_list`, `gl_journal_depart_list`, `gl_journal_allocate_list` (`where doc_no=?`)
7. `delete from ap_ar_trans_detail where sum_debt_amount=0 and coalesce(remark,'')='' and (billing_no='' or billing_no is null)` — ลบบรรทัดว่าง
8. `update ic_trans set due_date=date(doc_date)+credit_day where due_date<>date(doc_date)+credit_day and doc_no='RC26100003'` (ใช้เลขใบรับชำระ ซึ่งไม่มีใน `ic_trans` → ไม่มีผลกับใบนี้)

## 3. หลัง commit
1. `logs` (16 คอลัมน์ — ไม่มี `doc_qty`) / `erp_logs`
2. **doc flow**:
   - บิลที่ถูกรับ: `update ic_trans set used_status_2=1 where roworder=<บิล>` + reset `last_status`/`status` ของ 44 (detail, `ap_ar_trans_detail`, `cb_trans`, `cb_trans_detail`) — ยืนยัน DB: INV26100002 `used_status_2=1`
   - ตัวใบรับเอง: reset `last_status` ของ `ap_ar_trans_detail`/`cb_trans`/`cb_trans_detail` ที่ trans_flag 239
   - ต้นทางของบิล (ใบสั่งขาย 36): reset `last_status`
   - **กฎ `used_status_2` จากโค้ด** (`_docFlowThread.cs` ~147): `= 1` เมื่อมีแถว `ap_ar_trans_detail` ของ 235 (ใบวางบิล) หรือ 239 ที่ `last_status=0` อ้าง `billing_no` = บิล — **ไม่ดูว่าจ่ายครบหรือไม่** ⇒ บิลที่จ่ายบางส่วนก็ `used_status_2=1` และยกเลิกบิลไม่ได้ ([[write-spec-cancel]] A.1)
3. ล้าง `cb_chq_list`, serial
4. **ไม่มี** งานสต็อก/คิว `process` (ไม่มีสินค้า), ไม่มี GL (AOY ไม่เปิด realtime; batch จะลงทีหลัง)

## 4. สำหรับ sml_mcp_ai
- `preview_receipt`: ดึงบิลค้างด้วยสูตรข้อ 1 (ห้ามคิดยอดค้างเอง), ตรวจยอดรับต่อบิล ≤ `ar_balance`, ตรวจเลขที่จาก `ap_ar_trans`
- `commit_receipt` (transaction เดียว): ข้อ 2 ตามลำดับ (`ap_ar_trans` → `ap_ar_trans_detail` ต่อบิล โดย `bill_type` = trans_flag ของบิล, `balance_ref` = ยอดค้างก่อนรับ → `cb_trans`) + doc flow ข้อ 3.2 (`used_status_2=1` ให้บิล) → `logs`; หลัง commit `erp_logs`
- unique key (ตรวจ `pg_indexes` aoy 2026-10-21): **`ap_ar_trans` unique ที่ `doc_no` อย่างเดียว** (เลขที่ห้ามซ้ำข้ามทุก trans_flag ของตารางนี้), `cb_trans` unique `(doc_no, trans_flag)` → เลขชนจะ rollback ทั้งชุด แล้วลองเลขถัดไป

## 5. ยังไม่ทราบ
- การรับด้วยช่องทางอื่น (`cb_trans_detail`, `cb_chq_list`), ส่วนลด, ภาษีหัก ณ ที่จ่าย (`gl_wht_list`), `lost_profit_exchange_amount`
- ขั้นตอนหลังบันทึกของหน้าจอรับชำระ (ห่าง 44 วินาที) เกิดจากพิมพ์หรือไม่ — ยังไม่ได้ไล่โค้ด `SMLAPARControl/_ar_ap_trans.cs`
- การยกเลิกใบรับชำระ (240) และผลต่อ `used_status_2`

## 6. ยืนยันจากรอบ 4: รับชำระตามใบวางบิล + โอนเงิน (RC26100004, 16:15:06)
ลำดับเดียวกับ §2 และเพิ่ม:
- บรรทัดบิล (`ap_ar_trans_detail` trans_flag 239, 15 คอลัมน์) มี **`doc_ref='BL26100001'`** และ `ref_doc_no`/`ref_doc_date` = `ic_trans.doc_ref` ของบิล
- `cb_trans`: `cash_amount=0`, **`tranfer_amount=90.00`**, `total_amount`/`total_net_amount`/`total_amount_pay=90`
- **`insert cb_trans_detail` (13 คอลัมน์):** `doc_no, doc_date, doc_time, trans_type=2, trans_flag=239, doc_type=1 (โอน), chq_due_date=<วันที่>, trans_number=<รหัสสมุดบัญชี erp_pass_book.code ตัวพิมพ์ใหญ่>, bank_code, bank_branch, amount=90.00, remark, line_number=0` (ดู [[cash-bank]])
- **แถวเอกสารอ้างอิงของใบรับชำระ:** หลัง `delete cb_trans_detail …ว่าง` มี `insert ap_ar_trans_detail` (8 คอลัมน์) **`trans_type=2, trans_flag=99, doc_date, doc_no='RC26100004', billing_no='BL26100001', billing_date, remark, line_number=0`** + แถวว่าง line 1 (ถูกลบโดยคำสั่ง cleanup ท้าย transaction) — `trans_flag=99` ในที่นี้ใช้กับแถวอ้างอิงใบวางบิล (ชื่อ flag 99 ใน [[trans_flag]] คือ ลูกหนี้_ตั้งหนี้อื่น) · kbgtest มีแถวแบบนี้ 20,158 แถวที่ผูกกับใบรับชำระ
- doc flow 16:15:45: ใบวางบิล `used_status=1, doc_success=1` ([[write-spec-billing-note]])

## 7. ยืนยันจากรอบ 5.3: รับชำระด้วยบัตรเครดิต (RC26100005, 10:37:01 วันที่ 2026-10-26)
- ลำดับคำสั่งเหมือน §2 ทุกขั้น (ลบ `cb_trans`/`cb_trans_detail`/`gl_wht_list*`/`gl_journal_vat_sale` ของเลขว่าง → `ap_ar_trans` → `ap_ar_trans_detail` `bill_type=44` → `cb_trans` → `cb_trans_detail` → cleanup → `COMMIT`)
- ต่างจากเงินสดเฉพาะ `cb_trans.card_amount` และแถว `cb_trans_detail` `doc_type=3` (เลขบัตร, เลขอนุมัติ, `credit_card_type`) — รายละเอียดคอลัมน์ [[cash-bank]] §2.1
- ทะเบียนบัตร `cb_chq_list` (chq_type 3) เกิดใน doc flow หลัง commit ไม่ใช่ใน transaction ⇒ sml_mcp_ai ต้องรอ/ตรวจแถวทะเบียนหลังบันทึก หรือเรียกงานหลังบันทึกเหมือนโปรแกรม
- `ap_ar_trans_detail.ref_doc_no` ของบิลนี้เป็นเลขอ้างอิงยาวจากระบบภายนอก (คัดจาก `ic_trans` ของบิล) — โปรแกรมคัดลอกตามเดิม ไม่ได้ตรวจรูปแบบ
