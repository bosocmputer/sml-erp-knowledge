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
- `172.18.0.5` = บริการอื่น (ไม่ใช่โปรแกรม SML): ส่ง `-- ping` เป็นระยะ และ query สรุปใบเสนอราคา (`WITH base_orders AS …`) — **= `nexflow-sml-api-bybos`** (ยืนยันจาก `docker network inspect` 2026-10-21)
- client ที่เห็นทั้ง 3 capture (นับจาก source IP ในเครือข่าย docker): `172.18.0.3` = SMLJavaWebService (`application_name='PostgreSQL JDBC Driver'`, ให้บริการทุก tenant: aoy, cus_ms, kbyt, samai, smlerpmain{next,kbyt,cusms,demo}); `172.18.0.2` → wawacrm; `172.18.0.5` → aoy, demo, ploy_test; `172.18.0.10` → demo, demo2 (+ `loyalty_hub` ซึ่งไม่ใช่ DB ของ SML); `172.18.0.15` → kbgtest; IP สาธารณะ 1 ตัว → kbyt — **ชื่อ container (ยืนยันด้วย `docker network inspect` 2026-10-21):** .2 = `pricelabelservice`, .5 = `nexflow-sml-api-bybos`, .10 = `nextloyalty-api` (เขียน `ar_customer.website` ตรง), .15 = `kbwshop-nextstep-api-1` ดูรายละเอียด [[server-layout]] และ capture มีงานของ tenant อื่นปนด้วย ต้องกรองตาม database ตอนวิเคราะห์
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
- **บิลขายเชื่อที่ดึงจากใบสั่งขาย:** `insert ic_trans` (`doc_ref` = null — การอ้างอิงอยู่ที่บรรทัด `doc_ref_type=3`, `ref_doc_no`, `ref_row`) → `ic_trans_detail` → **`insert ap_ar_trans_detail (calc_flag -1, bill_type=3, billing_no=<เลขใบสั่งขาย>, …)`** = แถวในตาราง**เอกสารอ้างอิง**ของบิล (grid `_icTransRef`) ไม่ใช่การตั้งลูกหนี้ — **แก้ไข 2026-10-21:** บันทึกเดิมว่า "ตั้งลูกหนี้" ผิด; ยอดลูกหนี้คำนวณสดจากเอกสาร ดู [[write-spec-sale-invoice]] (ไม่มี `cb_trans` เพราะไม่รับเงิน) → `gl_journal_vat_sale` → `ic_trans_shipment` → logs
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

## รอบ 4 (2026-10-21 16:03–16:29) — capture aoy-run4
| เวลา | ขั้น | เอกสาร | สเปก |
|---|---|---|---|
| 16:03 | login (NEXT → AOY) | | [[login-flow]] |
| 16:06:50 | ใบสั่งขายจากใบเสนอราคา QT26090001 | SO26100002 | [[write-spec-sale-order]] §6.1 |
| 16:07:56 | แก้ไขใบสั่งขาย (ลบ-ใส่ใหม่, ล็อก `guid_code`) | SO26100002 | §6.2, [[document-engine]] |
| 16:10:01 | ยกเลิกใบสั่งขายทั้งหมด | SSC26100001 | [[write-spec-cancel]] B.0 |
| 16:13:19 | ใบวางบิล | BL26100001 | [[write-spec-billing-note]] §0 |
| 16:15:06 | รับชำระตามใบวางบิล + โอนเงิน | RC26100004 | [[write-spec-receipt]] §6 |
| 16:17:27 | รับคืนจากขายเชื่อ | CN26100002 | [[write-spec-credit-note]] §0 |
| 16:19:53 | รับคืนจากขายเชื่อ (ใบที่ 2 — แผนเดิมเป็นลดหนี้ไม่กระทบสต็อก) | CN26100003 | §0 |
| 16:22:03 | จ่ายชำระเงินสด | PV26100001 | [[write-spec-ap-payment]] §6 |
| 16:27:53 | สร้างสินค้าหลายหน่วย + บาร์โค้ด | ZZTEST-0001 | [[write-spec-master-product]] §10 |
| 16:29 | logout (ปลดล็อกทุกแถวเพราะไม่มี session เหลือ) | | [[document-engine]] |
- ไม่ได้ทำ: ลดหนี้ไม่กระทบสต็อก (inquiry 2), หน้าจอกำหนดบาร์โค้ดแยก
- tcpdump หยุดโดย Claude (kill -INT process ของ ubuntu) หลังผู้ใช้ปิดโปรแกรม; ไฟล์ 432 MB copy มาที่ `~/sml-sqllog/` แล้วลบบน server

## รอบที่ 5.1 (2026-10-26 10:12–10:21, ไฟล์ aoy-run5-1, 19,213 คำสั่งทุก database / aoy 2,844)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 10:19:25 | ลดหนี้จากขายเงินเชื่อ ไม่กระทบสต๊อก อ้าง BF-INV26100036 ลด 10 บาท | CN26100004 | [[write-spec-credit-note]] §0.1 — `inquiry_type=2`, บรรทัด `calc_flag=1` แต่สูตรสต็อกตัดออก, `balance_qty` ไม่เปลี่ยน |
- รอบนี้แยกเป็นรอบย่อยทีละเรื่อง (แผนใน [[phase2-tcpdump]] รอบ 5) · ไม่ได้ตัด connection เพราะไม่มีของ AOY ค้าง (0 แถว) — parse ได้ครบโดยไม่ต้อง `--include-unknown`
- ผู้ใช้หยุด tcpdump เอง; ไฟล์ 113 MB copy มาที่ `~/sml-sqllog/` แล้วลบบน server

## รอบที่ 5.2 (2026-10-26 10:26–10:30, ไฟล์ aoy-run5-2, 8,348 คำสั่งทุก database)
| เวลา | ขั้น | ผล |
|---|---|---|
| 10:27:18, 10:29:09, 10:29:35 | กำหนดบาร์โค้ดสินค้า `ZZTEST-0001` เพิ่ม `8859999000035` (บันทึก 3 ครั้ง) | [[write-spec-master-product]] §6.1 — ลบทั้งชุดแล้ว insert ใหม่ทุกครั้ง (`roworder` 152/153 → 159/160/161), ราคาเก็บที่ `ic_inventory_barcode.price` |

## รอบที่ 5.3 (2026-10-26 10:35–10:40, ไฟล์ aoy-run5-3 (บน server ชื่อ aoy-run5-2), 8,093 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 10:37:01 | รับชำระ BF-INV26100034 (48) ด้วยบัตรเครดิต | RC26100005 | [[cash-bank]] §2.1 — `cb_trans_detail.doc_type=3`, `cb_chq_list` chq_type 3 สร้างใน doc flow หลัง commit |
| 10:39:49 | ขึ้นเงินบัตรเข้าสมุดบัญชี 5843697 | CRD26100001 | 461: `ic_trans_detail.item_code` = รหัสสมุดบัญชี, สถานะบัตร 0→1, ใบรับชำระ `used_status` ยังเป็น 0 |

## รอบที่ 5.4 (2026-10-26 12:05–12:09, ไฟล์ aoy-run5-4, 8,160 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 12:06:29 | รับชำระ BF-INV26100031 (255) ด้วยเช็ค 0000501 SCB | RC26100006 | [[cash-bank]] §2.2 — `doc_type=2`, ทะเบียนเช็คเกิดใน doc flow, status 0 |
| 12:07:48 | นำฝากเช็คเข้าสมุดบัญชี 5843697 | CHD26100001 | 410: status 0→1, **ใบรับชำระ `used_status=1`** |
| 12:08:49 | เช็คผ่าน | CHP26100001 | 411: status 1→2 |

## รอบที่ 5.5 (2026-10-26 12:15–12:18, ไฟล์ aoy-run5-5, 6,777 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 12:16:19 | ใบสั่งซื้อ 2 บรรทัด | PO26100001 | [[write-spec-purchase]] §5 — `ic_trans` + `ic_trans_detail` (`ref_row=-1`), คิวต้นทุนทำงานด้วย |
| 12:17:43 | ซื้อเงินเชื่ออ้าง PO ครบทุกบรรทัด | PU26100002 | `ref_doc_no/ref_row` + แถว `ap_ar_trans_detail` อ้าง PO, PO `doc_success=1`, สต็อก/ต้นทุนเปลี่ยน |

## รอบที่ 5.6 (2026-10-26 12:21–12:23, ไฟล์ aoy-run5-6, 3,031 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 12:22:26 | ยกเลิกบิลขายเชื่อ BF-INV26100039 | SIC26100001 | [[write-spec-cancel]] A.5 — หัวอย่างเดียว, บิล `last_status=1`, สต็อก AH-0001 122 → 123 |

## รอบที่ 5.7 (2026-10-26 12:26–12:30, ไฟล์ aoy-run5-7, 7,781 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 12:27:21 | ใบสั่งขาย 2 บรรทัด ไม่อ้างเอกสาร | SO26100003 | [[write-spec-sale-order]] §6.4 — `price_mode -1` เมื่อไม่มีสูตรราคา |
| 12:29:19 | ยกเลิกใบสั่งขายรายสินค้า (บรรทัด 2) | SSC26100002 | [[write-spec-cancel]] B.1 — `cancel_type=2` มีบรรทัด + แถวอ้างอิง, SO `used_status=1` ไม่ใช่ `last_status` |

## รอบที่ 5.8 (2026-10-26 13:08–13:12, ไฟล์ aoy-run5-8, 6,957 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 13:11:02 | จ่ายชำระ PU26100002 (120) เงินสด 116.64 + หัก ภ.ง.ด.53 3% 3.36 | PV26100002 / RWHT5326100001 | [[cash-bank]] §3.1 — `gl_wht_list` + `_detail` ใน transaction เดียวกัน, ใบซื้อ `used_status_2=1` |

## รอบที่ 5.9 (2026-10-26 13:17–13:20, ไฟล์ aoy-run5-9, 4,560 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 13:18:18 | ใบรับวางบิลเจ้าหนี้ PU26090001 | PB26100001 | [[write-spec-ap-payment]] §8 — ใบซื้อ `used_status_2=1` ตั้งแต่รับวางบิล |
| 13:19:23 | จ่ายชำระตามใบรับวางบิล เงินสด 111,600 | PV26100003 | `doc_ref=PB` + แถว `trans_flag=99`, PB `used_status=1, doc_success=1` (ยืนยันกฎ flag 99) |

## รอบที่ 5.10 (2026-10-26 13:23–13:25, ไฟล์ aoy-run5-10, 2,790 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 13:24:23 | ยกเลิกใบรับชำระ RC26100004 (ตามใบวางบิล, เงินโอน) | EEC26100001 (จอแสดง EEC26100002) | [[write-spec-receipt]] §8 — หัวอย่างเดียว, RC `last_status=1`, `cb_trans.status=1`, ใบวางบิล `used_status=0` |

## รอบที่ 5 — ภาพหน้าจอ (2026-10-26, ไม่ต้องดักจับ)
- เมนู 1.เริ่มต้น › 1.3.ระบบขาย แสดง `1.3.2 กำหนดเขตการขาย`, `1.3.3 ออกแบบหน้าจอขาย POS`, `1.3.4 Download ระบบเสียงพูด`, `1.3.5 กำหนดกลุ่มอนุมัติวงเงิน` ⇒ เลขเมนูนับรวมเมนูซ่อน ([[menu-map]])
- แถบเมนูบนสุดมี `11.คลังสินค้า 12.Data` ⇒ เครื่องร้านรัน edition 13 (AccountPOSPro)

## รอบที่ 6.1 (2026-10-26 13:42–13:45, ไฟล์ aoy-run6-1, 4,694 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 13:43:56 | ขายเชื่อไม่อ้างเอกสาร 2 บรรทัด ส่วนลดท้ายบิล 5% | INV26100003 | [[write-spec-sale-invoice]] §6 — ส่วนลดเก็บที่หัว (`discount_word='5%'`, `total_discount=13`), ไม่กระจายลงบรรทัด, ภาษีหลังลด |

## รอบที่ 6.2 (2026-10-26 13:46–13:49, ไฟล์ aoy-run6-2, 6,977 คำสั่งทุก database)
| เวลา | ขั้น | ผล |
|---|---|---|
| 13:47:45 | สร้างลูกค้า `ZZCUST-0001` | [[write-spec-master-customer]] §1 — `ar_customer` + `ar_customer_detail` 5 คอลัมน์ + `master_logs` |
| 13:48:09–13:48:37 | แก้ไข 3 ครั้ง (ใส่วันเครดิต 30 ที่แท็บรายละเอียดเพิ่มเติม) | §2 — ล็อก `guid_code`, ลบตารางลูก 4 ตาราง → update หัว → insert detail 43 คอลัมน์ |

## รอบที่ 6.3 (2026-10-26 14:03–14:12, ไฟล์ aoy-run6-3, 10,492 คำสั่งทุก database)
| เวลา | ขั้น | ผล |
|---|---|---|
| 14:04:15 | ตั้งราคาขายทั่วไป `ZZTEST-0001` ชิ้น ราคาแยกภาษี 25 | [[pricing-vat-gl]] §1.1 — `ic_inventory_price` แถวที่ `from/to_date=null`, `from/to_qty=0` |
| 14:06–14:11 | เปิดบิลขาย (เงินสด/ภาษีรวมใน แล้วเชื่อ/แยกนอก) ใส่ ZZTEST-0001 | "ไม่พบราคาสินค้า" เพราะเงื่อนไขช่วงวันที่/จำนวน · ข้อความ "ห้ามขายเกินยอดคงเหลือลบด้วยค้างส่ง" (คงเหลือ 1 − ค้างส่ง 1 จาก SO26100003; ร้านตั้ง `stock_accured_level=0, ic_stock_control=0`) · **ไม่ได้บันทึกบิล** |
- หน้าจอบิลแสดงช่องเอกสารวันที่ไม่ครบอีกครั้ง (เหมือนรอบ 5.8)

## รอบที่ 6.3b (2026-10-26 14:15–14:18, ไฟล์ aoy-run6-3b, 2,427 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 14:16:50 | แก้แถวราคา ZZTEST-0001 ใส่ช่วงจำนวน 0–999 และวันที่ | — | [[pricing-vat-gl]] §1.1 |
| 14:17:20 | ขายเชื่อ ภาษีแยกนอก ZZCUST-0001 ZZTEST-0001 1 ชิ้น (ราคาขึ้นเอง 25) | INV26100004 | ราคา 25 + VAT 1.75 = 26.75 · คำเตือนค้างส่งไม่บล็อกการบันทึก |

## รอบที่ 6.4 (2026-10-26 14:33–14:38, ไฟล์ aoy-run6-4, 7,589 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 14:34:45 | ใบเสนอราคา AH-0001 1 × 240 | QT26100001 | [[write-spec-sale-invoice]] §7 |
| 14:35:52 | ใบสั่งจองอ้าง QT | BS26100001 | `ref_doc_no=QT, ref_row=-1` + แถวอ้างอิง · QT ปิด (`doc_success=1`) |
| 14:37:05 | ขายเชื่ออ้าง BS | INV26100005 | `doc_ref_type=2`, `bill_type=2` + แถวว่าง 2 แถวค้าง · BS ปิด · สต็อก 122 → 121 |

## รอบที่ 6.5 (2026-10-26 14:42–14:51, ไฟล์ aoy-run6-5, 19,909 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 14:43:32 | ซื้อเงินสด ZZTEST-0001 3 × 10 | PU00010002 | [[write-spec-purchase]] §6.1 — `cb_trans` ฝั่งจ่าย · ⚠️ เลขออกตอนวันที่ว่าง → ไม่มี `tax_doc_no` และ `gl_journal_vat_buy` |
| 14:45:05 | ใบสั่งซื้อ 2 ชิ้น | PO26100002 | §6.2 |
| 14:49:59 | ซื้อเชื่ออ้าง PO รับ 1 ชิ้น | PU26100003 | §6.3 — PO `doc_success=0`, ค้างรับ 1, สต็อก 4 |

## รอบที่ 6.6 (2026-10-26 14:54–14:56, ไฟล์ aoy-run6-6, 6,498 คำสั่งทุก database)
| เวลา | ขั้น | เลขที่ | ผล |
|---|---|---|---|
| 14:54:55 | ใบเสนอราคา AH-0001 1 × 240 | QT26100002 | เหมือนรอบ 6.4 |
| 14:55:37 | ลบใบเสนอราคา | QT26100002 | [[document-engine]] ลบเอกสาร — hard delete ใน transaction เดียว + `logs` function_code 3 |
