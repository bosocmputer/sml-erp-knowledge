---
tags: [sml, runtime, verified, phase2]
source: tcpdump capture aoy-run1 (2026-10-21 08:43–09:06, client 172.18.0.3 = SMLJavaWebService), parsed by scripts/parse_pg_pcap.py
status: verified-runtime
date: 2026-10-21
---
# สิ่งที่ยืนยันจากการรันจริง (เฟส 2, รอบที่ 1)

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
3. **web service หยิบคิว** (poll ทุก ~10 วินาที: `select roworder, process_name from process where last_guid=? or last_guid is null …`) → จองงาน `update process set last_guid=?, last_process_time=now() …` (งานค้างนานถูกยึดคืนด้วย `last_process_time < now() - interval ?`)
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
- **ไม่พบคำสั่งไปที่ `smlerpmainaoy` เลย** ทั้งที่ login สำเร็จ → การตรวจ user/GUID (`sml_user_list`, `sml_guid`) ของ provider AOY น่าจะใช้ main database บน server อื่น (ดู [[login-flow]]) — ยังไม่ได้ยืนยันว่าอยู่ที่ไหน
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
- `172.18.0.5` = บริการอื่น (ไม่ใช่โปรแกรม SML): ส่ง `-- ping` เป็นระยะ และ query สรุปใบเสนอราคา (`WITH base_orders AS …`) — น่าจะเป็น dashboard/API ภายนอก
- web service ส่ง `SET extra_float_digits`, `SET application_name`, `set enable_seqscan=false` ทุกครั้งที่เปิด connection

## ยังไม่ได้ทดสอบ (รอบถัดไป)
ใบสั่งขาย→เปิดบิลจากใบสั่งขาย (สายเอกสาร), รับชำระหนี้ (239), ขายเชื่อ, ปรับปรุง/โอนสต็อก, ประมวลผล GL, ปิดกะ/ส่งเงิน POS
