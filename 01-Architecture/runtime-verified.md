---
tags: [sml, runtime, verified, phase2]
source: tcpdump capture aoy-run1 (2026-10-21 08:43–09:06, client 172.18.0.3 = SMLJavaWebService), parsed by scripts/parse_pg_pcap.py
status: verified-runtime
date: 2026-10-21
---
# สิ่งที่ยืนยันจากการรันจริง (เฟส 2)

กลับไป [[00-Index]] · วิธีทำ [[phase2-tcpdump]] · ค่าตั้งค่าร้าน [[aoy-settings]]

> ดักจับ SQL ระหว่าง web service กับ PostgreSQL ขณะทดสอบ 8 ขั้นบนร้าน AOY: ได้ 4,489 คำสั่งของ database `aoy` (+ `aoy_images` 8, `aoy_logs` 12) · SQL ดิบ/ไฟล์ .pcap เก็บนอก vault (`~/sml-sqllog/`) · ข้างล่างเป็นโครงสร้างเท่านั้น

## ทดสอบที่ทำ
| ขั้น | เวลา | เอกสาร |
|---|---|---|
| 1 Login | 08:48 | |
| 2 เปิดหน้าจอขายสินค้า/บริการ | 08:50 | |
| 3 บันทึกบิลขาย (2 รายการ, เงินสด) | 08:55 | INV26100001 |
| 4 ยกเลิกบิล | 08:57 | SIC00010001 |
| 5 ขาย POS เงินสด | 08:59 | 001-261021-0001 |
| 6 ซื้อสินค้า | 09:02 | PU26100001 |
| 7 รายงานการขายสินค้าและบริการ | 09:04 | |
| 8 ปิดโปรแกรม | 09:05 | |

## ข้อค้นพบหลัก

### 1. ต้นทุน/สต็อกหลังบันทึก **ทำผ่านคิวในตาราง `process`** (แก้ความเข้าใจเดิม)
ลำดับจริงหลังบันทึกเอกสาร (ทั้งขาย ยกเลิก POS ซื้อ):
1. โปรแกรมอัปเดตสถานะสายเอกสาร (doc flow) — `update ic_trans_detail/ap_ar_trans_detail/cb_trans/cb_trans_detail set last_status/status …`, ทะเบียนเช็ค `delete cb_chq_list where not exists …`, serial `ic_serial`, หัก ณ ที่จ่าย `gl_wht_list_detail`, ยอดค้างรับ `update ic_inventory set accrued_in_qty …`
2. **ส่งงานเข้าคิว:** `delete from process where process_name=? and wherein in (…)` แล้ว `insert into process (process_name, wherein) select ?, code from ic_inventory where code in (…)` — 1 แถวต่อสินค้าที่ต้องคำนวณใหม่
3. **โปรแกรม Windows ที่เปิดอยู่หยิบคิวผ่าน web service** (`SMLProcess._sendProcess._procesNow`, 3 thread วนทุก 10 วินาที ดู [[stock-cost]]: `select roworder, process_name from process where last_guid=? or last_guid is null …`) → จองงาน `update process set last_guid=?, last_process_time=now() …` (งานค้างนานถูกยึดคืนด้วย `last_process_time < now() - interval ?`)
4. คำนวณ: `update/insert/delete ic_trans_detail_lot` (ล็อต), `update ic_trans_detail set sum_of_cost=?, sum_of_cost_1=?, average_cost=?, average_cost_1=?, profit_lost_cost_amount=?`, `update ic_inventory set average_cost=?` → `delete from process where roworder=?`
- ผล: ต้นทุนในเอกสารอัปเดต **หลังบันทึกไม่กี่วินาทีถึงหลายสิบวินาที** ไม่ใช่ในทันที → ดู [[stock-cost]], [[document-engine]]

### 2. บันทึกเอกสารจริง (ตรงกับ [[document-engine]])
- **บิลขาย (44):** `insert ic_trans` → `insert ic_trans_detail` ×รายการ → `insert cb_trans` (รับเงินสด) → `delete cb_trans_detail where trans_number is null …` → `insert gl_journal_vat_sale` → `insert ic_trans_shipment` → `insert logs` → `insert erp_logs` (DB `aoy_logs`) — ทั้งหมดภายใน ~0.4 วินาที (ชุดเดียว)
- **ยกเลิกบิล (45):** `insert ic_trans` (เอกสารยกเลิก, `doc_ref` = บิลเดิม) + `logs`/`erp_logs` → doc flow ตั้ง `last_status` ของบิลเดิมและตารางลูกทั้งหมด → เข้าคิวคำนวณสต็อก (**ไม่ลบบิลเดิม**)
- **ซื้อ (12):** `insert ic_trans` → `ic_trans_detail` → `delete cb_trans_detail …` → `insert gl_journal_vat_buy` → `logs`/`erp_logs` → doc flow → คิวต้นทุน
- **ไม่มี `insert gl_journal`** ในทุกขั้น — สอดคล้องกับร้าน AOY ตั้ง `gl_process_realtime = 0` (GL ทำเป็นชุดภายหลัง)

### 3. POS (ตรงกับ [[pos-client]])
- บันทึกบิล: `insert ic_trans` (คอลัมน์มี `cashier_code`, `tax_doc_no`, `vat_rate`) → `ic_trans_detail` (มี `calc_flag`, `doc_date_calc`) → `insert cb_trans (sale_shift_id, …, pay_type, cash_amount …)` → `insert gl_journal_vat_sale` → `update ic_trans set send_type, send_day, send_date` → คิวต้นทุน
- `insert pos_log` เกิดขึ้นตอนปิดหน้าจอ POS (~27 วินาทีหลังจบบิล) — สอดคล้องกับ command `*98`

### 4. Login และการตั้งค่าที่โหลด
- อ่าน `erp_user`, `erp_user_group`(+`_detail`, `_approve`), `erp_branch_list`, `erp_company_profile`, `erp_option`, `erp_thai_qr_config`, `erp_option_etax_inet`, `erp_option_mobillyst`, `pg_indexes` (ตรวจ index) และตัวเลขสรุปหลายตาราง
- เขียนตอน login: `update ap_ar_trans`, `update ic_trans` (ปลดล็อกเอกสาร), ล้าง `barcode_import_list(_detail)`
- **แก้ไข (2026-10-21):** login AOY ใช้ main database `smlerpmainnext` (provider NEXT) — เห็นครบเมื่อ parse capture ใหม่แบบไม่กรอง database (บันทึกเดิมว่า "ไม่พบ" ผิดเพราะ parse กรองแค่ `aoy`/`smlerpmainaoy`) ลำดับ SQL และ heartbeat ดู [[login-flow]]
- ทุกครั้งที่เปิดเมนู โปรแกรมโหลด `erp_account_period` ซ้ำ และสั่ง `update erp_account_period set period_year = … where period_year is null`

### 5. รายงานการขายสินค้าและบริการ (`menu_so_report_invoice`)
เงื่อนไขจริงของรายงาน (หัวเอกสาร):
```sql
from ic_trans
where trans_flag in (?)                -- 44
  and doc_date between ? and ?
  and last_status = ?                  -- 0 = ไม่ถูกยกเลิก
  and (coalesce(doc_ref, ?) = ? or is_pos = ?)   -- ไม่มีเอกสารอ้างอิง หรือเป็นบิล POS
  and is_doc_copy <> ?
```
แล้วดึงรายละเอียด `ic_trans_detail` ต่อ — **tool ที่สรุปยอดขาย (เช่น sml_mcp_ai) ควรใช้เงื่อนไขชุดนี้** จะได้ตัวเลขตรงกับรายงานของโปรแกรม

### 6. connection อื่นที่เห็น
- `172.18.0.3` = SMLJavaWebService (โปรแกรม SML ทั้งหมดผ่านตัวนี้)
- `172.18.0.5` = บริการอื่น (ไม่ใช่โปรแกรม SML): ส่ง `-- ping` เป็นระยะ และ query สรุปใบเสนอราคา (`WITH base_orders AS …`) — ยังไม่ทราบว่าเป็นระบบอะไร (ไม่ใช่ SMLJavaWebService เพราะเป็นคนละ IP)
- client ที่เห็นทั้ง 3 capture (นับจาก source IP ในเครือข่าย docker): `172.18.0.3` = SMLJavaWebService (`application_name='PostgreSQL JDBC Driver'`, ให้บริการทุก tenant: aoy, cus_ms, kbyt, samai, smlerpmain{next,kbyt,cusms,demo}); `172.18.0.2` → wawacrm; `172.18.0.5` → aoy, demo, ploy_test; `172.18.0.10` → demo, demo2 (+ `loyalty_hub` ซึ่งไม่ใช่ DB ของ SML); `172.18.0.15` → kbgtest; IP สาธารณะ 1 ตัว → kbyt — **ยังไม่ทราบว่า .2/.5/.10/.15 เป็น container อะไร** (ต้อง `docker network inspect` ซึ่งต้องใช้ sudo) และ capture มีงานของ tenant อื่นปนด้วย ต้องกรองตาม database ตอนวิเคราะห์
- web service ส่ง `SET extra_float_digits`, `SET application_name`, `set enable_seqscan=false` ทุกครั้งที่เปิด connection

## รอบที่ 2 (2026-10-21 09:43–10:16, ไฟล์ aoy-run2, 5,481 คำสั่ง)

| ขั้น | เวลา | เอกสาร | ผล |
|---|---|---|---|
| ใบสั่งขาย (36) | 09:45 | SO26100001 | ✅ บันทึกแล้ว |
| ขายเชื่อจากใบสั่งขาย (44) | 09:46 | INV26100002 | ✅ บันทึกแล้ว |
| รับชำระหนี้ (239) | 09:48 | RC26100003 | ⚠️ รอบนี้ไม่ได้บันทึก → ทดสอบใหม่ในรอบ 3 ✅ |
| ปรับปรุงสต็อก เพิ่ม (66) | 10:09–10:11 | IA26100001 | ✅ บันทึกแล้ว |
| โอนสินค้า (72) | 10:11 | TF26100001 | ⚠️ รอบนี้ไม่ได้บันทึก → ทดสอบใหม่ในรอบ 3 ✅ |
| ส่งเงิน POS | 10:12–10:14 | 001-261021-0001 | ✅ |
| ประมวลผล GL จากรายวัน | 10:14–10:15 | — | ✅ สร้าง GL 3 เอกสาร |

### 7. ใบสั่งขาย → บิลขาย (สายเอกสาร)
- **ใบสั่งขาย:** `insert ic_trans` → `ic_trans_detail` → `ic_trans_shipment` → `logs`/`erp_logs` แล้วปรับ **ยอดค้างจอง** `update ic_inventory set book_out_qty=? …` และเข้าคิวต้นทุน
- **บิลขายเชื่อที่ดึงจากใบสั่งขาย:** `insert ic_trans` (`doc_ref` = ใบสั่งขาย) → `ic_trans_detail` → **`insert ap_ar_trans_detail (calc_flag -1, bill_type, billing_no, ref_doc_no …)`** (ตั้งลูกหนี้ ไม่มี `cb_trans` เพราะไม่รับเงิน) → `gl_journal_vat_sale` → `ic_trans_shipment` → logs
- หลังบันทึก doc flow: **`update ic_trans set used_status=?, doc_success=? where roworder=?`** บนใบสั่งขาย — ตรวจใน DB แล้ว ใบสั่งขาย `used_status = 1`, `doc_success = 1` (ใช้ครบ) ✅ ตรงกับ [[doc-flow-rules]]

### 8. ปรับปรุงสต็อก (66)
- ลบรายการกำพร้าก่อน (`delete from ic_trans_detail where not exists หัวเอกสาร`), `insert ic_trans` (มี `wh_from`, `location_from`) → `ic_trans_detail` → logs → คำนวณล็อต/ต้นทุนทันที และ `update ic_trans_detail set …, sum_amount=?, price=? …` (เติมมูลค่าจากต้นทุน) → `update ic_trans set total_amount = $1 …` (server-side prepared statement) → คิว `process`

### 9. ส่งเงิน POS
- `insert POSCashierSettle (MACHINECODE, DocNo, DocDate, doc_time, CashierCode, CashAmount, CreditCardAmount, CoupongAmount, sum_amount, total_in, total_out, …)` + `insert pos_settle_bill_discount (…, period_guid)` ✅ ตรงกับ [[pos-client]]

### 10. ประมวลผล GL จากข้อมูลรายวัน (`menu_gl_process`)
1. โหลดรูปแบบเอกสารที่มีผังบัญชี (`erp_doc_format` ที่มี `erp_doc_format_gl` หรือ `gl_book`) และ `erp_doc_format_gl where condition_number > 0`
2. โหลดแหล่งเลขบัญชีทั้งหมด: `ic_inventory.account_code_1..4`, `ap_supplier_detail.account_code`, `ar_customer_detail.account_code`, `erp_pass_book.account_code_1/2`, `cb_petty_cash.chart_of_account`, `erp_expenses_list.gl_account_code`, `erp_income_list.gl_account_code`, `erp_bank.chq_income_account_code`, `erp_credit_type.account_code`, `as_asset.*account_code`, `erp_wallet_list.account_code`, `gl_chart_of_account`
3. ดึงเอกสารของช่วงวันที่ แล้ว**ต่อเอกสาร**: `BEGIN` → `delete gl_journal` + `delete gl_journal_detail` (ของเอกสารนั้น) → `insert gl_journal` → `insert gl_journal_detail` → `COMMIT` (ประมวลผลซ้ำได้ ไม่ซ้ำซ้อน)
4. อัปเดตสถานะผ่านรายการ (`WITH journal_pass AS …`) และล้าง `guid_code` ใน `gl_journal`/`ic_trans`
→ ยืนยัน [[pricing-vat-gl]] ส่วน GL และ [[aoy-settings]] (`gl_process_realtime = 0` → GL เกิดเมื่อสั่งประมวลผล)

## รอบที่ 3 (2026-10-21 10:39–10:44, ไฟล์ aoy-run3, 2,072 คำสั่ง)

### 11. รับชำระหนี้ / ออกใบเสร็จ (239) — RC26100003 ชำระ INV26100002 ด้วยเงินสด
1. **ลบของเดิมของเอกสารนี้ก่อน** (รูปแบบ delete-แล้ว-insert รองรับการแก้ไข): `delete cb_trans`, `cb_trans_detail`, `gl_wht_list(_detail)`, `gl_journal_vat_sale` ของเลขที่นี้
2. `insert ap_ar_trans` (หัว: trans_type, trans_flag, cust_code, doc_format_code, sale_code, total_net_value, creator_code, create_datetime)
3. `insert ap_ar_trans_detail` 1 แถวต่อบิลที่ชำระ (`billing_no` = เลขที่บิล, `billing_date`, `ref_doc_no`, `due_date`, `sum_debt_amount` ยอดหนี้, `balance_ref` ยอดคงค้าง, `sum_pay_money` ยอดชำระ …)
4. `insert cb_trans` (pay_type, cash_amount …) — การรับเงิน
5. ล้าง GL ของเอกสารนี้ (`delete gl_journal`, `gl_journal_detail`, `_side_list`, `_job_list`, `_project_list`, `_depart_list`, `_allocate_list`) รอประมวลผลใหม่
6. `update ic_trans set due_date = date(doc_date) + credit_day` บนบิลที่อ้างถึง, logs/erp_logs
7. doc flow: **`update ic_trans set used_status_2 = ? where roworder = ?`** บนบิลขาย → ตรวจ DB แล้ว INV26100002 `used_status_2 = 1` ✅ → **`used_status_2` = บิลถูกนำไปรับชำระแล้ว** (ใช้หาบิลค้างชำระได้)

### 12. โอนสินค้าระหว่างคลัง (72 → 70)
- บันทึกครั้งเดียวได้ **2 เอกสารเลขที่เดียวกัน** ใน `ic_trans`: **72 โอนออก** (`calc_flag −1` คลังต้นทาง) และ **70 โอนเข้า** (`calc_flag +1` คลังปลายทาง) หัวเอกสารมี `wh_from`, `location_from`, `wh_to`, `location_to` ✅ ตรวจใน DB แล้ว
- จากนั้นคำนวณล็อต/ต้นทุนทันที + คิว `process` เหมือนเอกสารสต็อกอื่น
- ข้อสังเกต: ในรอบนี้มี `update ic_inventory set average_cost = -…` (ค่าทุนเฉลี่ยติดลบ) กับสินค้าที่สต็อกติดลบ — ผลจากการคำนวณเมื่อสต็อกไม่พอ

## ยังไม่ได้ทดสอบ (รอบถัดไป)
ซื้อแบบมีใบสั่งซื้อ (6 → 12), ขายบัตรเครดิต/เช็ค, ใบวางบิล (235), จ่ายชำระเจ้าหนี้ (19)
