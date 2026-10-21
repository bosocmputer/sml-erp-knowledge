---
tags: [sml, sml_mcp_ai, write-spec, sale-order, verified-runtime]
status: verified-runtime (สร้างใบใหม่, ดึงจากใบเสนอราคา, แก้ไข, ยกเลิก — รอบ 4) / from-code (ส่วนที่ระบุ)
source: capture aoy-run2 (SO26100001, 2026-10-21 09:44–09:46) + แถวจริงใน aoy + smlerp SMLInventoryControl/_icTransControl.cs, _processThread.cs, SMLProcess, SMLERPGlobal/_global.cs + smljavaws2 SMLICProcess.java
---
# สเปกการบันทึก: ใบสั่งขาย (trans_flag 36)

กลับไป [[00-Index]] · การตัดสินใจภาพรวม [[adr-001-write-path]] · สายเอกสาร [[doc-flow-rules]] · สต็อก [[stock-cost]]

> **ขอบเขต:** สร้างใบสั่งขาย**ใบใหม่** (`_myManageTrans._mode == 1`) ผ่านหน้าจอ `menu_so_sale_order` (screen code `SS`)
> **ยังไม่ครอบคลุม:** ลบ (mode 3), อนุมัติใบสั่งขาย (52), ยกเลิกรายสินค้า (37 type 2), ดึงจากใบจอง — (ดึงจากใบเสนอราคา / แก้ไข / ยกเลิกทั้งหมด ยืนยันแล้วใน §6)
> ค่าตัวอย่างทั้งหมดมาจาก SO26100001 (ข้อมูล demo) · ช่องที่เป็นชื่อ/ที่อยู่/หมายเหตุ ไม่คัดลอกค่าลง vault

## 0. ลำดับเหตุการณ์จริง (ผลรวมจาก capture + โค้ด)

| # | เวลา (capture) | ขั้น | transaction | แหล่ง |
|---|---|---|---|---|
| 1 | 09:44:42 | เปิดหน้าจอ → อ่าน `erp_doc_format` (code `SO`) → หาเลขที่ล่าสุด → แสดง SO26100001 | อ่านอย่างเดียว | capture |
| 2 | 09:45:55–56 | ก่อนบันทึก: อ่าน `erp_company_profile`, `erp_option`, สิทธิ์ผู้ใช้ (`erp_user_group*`, `erp_user`), `erp_thai_qr_config`, `erp_option_etax_inet`, `erp_option_mobillyst` | อ่านอย่างเดียว | capture |
| 3 | 09:45:56.361–.457 | **`BEGIN` → `ic_trans` → `ic_trans_detail` × จำนวนรายการ → `ic_trans_shipment` → `COMMIT`** | **1 transaction** (`_queryList`) | capture + `_icTransControl` |
| 4 | 09:45:56.578 | `insert into logs` (database ร้าน) | แยก (autocommit) | capture + `_createLog` |
| 5 | 09:45:56.757 | `insert into erp_logs` (database `<db>_logs`) | แยก, คนละ database | capture + `_writeFullLogs` |
| 6 | 09:45:59 | พิมพ์ฟอร์ม (`erp_doc_format.form_code` → `formdesign`) — **หน้าต่างพิมพ์ block จนกว่าจะปิด** | อ่านอย่างเดียว | capture + `_printFormData` |
| 7 | 09:46:09–10 | thread เบื้องหลัง `_processThread._run`: doc flow → `_updateDateTimeForCalc` → `_process_stock_balance(items, "36")` | หลาย transaction แยกกัน | capture + `_processThread.cs` |
| 8 | 09:46:11–12 | โปรแกรมที่เปิดอยู่หยิบคิว `process` 'IC' ไปคำนวณต้นทุน/ล็อต | แยก | capture + [[stock-cost]] § ใครเป็นคนหยิบคิว |

ช่วงห่าง 14 วินาทีระหว่างขั้น 3 กับ 7 เกิดจาก**โค้ดเรียกพิมพ์ก่อนแล้วค่อยเริ่ม thread** (`_icTransControl.cs` ~บรรทัด 17297 `_printFormData` → ~17356 `new _processThread(...)`) — ถ้าผู้ใช้ไม่ปิดหน้าพิมพ์ งานหลังบันทึกจะยังไม่เริ่ม

## 1. ก่อนเขียน: ค่าที่ต้องอ่าน/ตรวจ

| เรื่อง | อ่านจาก | ผลต่อการบันทึก | แหล่ง |
|---|---|---|---|
| รูปแบบเลขที่ | `erp_doc_format where code='SO'` → AOY: `format='@YYMM####'`, `screen_code='SS'`, `vat_type=0`, `form_code='SS0003'` | `@` = รหัส format, `YY` = ปี ค.ศ. 2 หลัก, `MM` = เดือน, `####` = running → SO26100001 (doc_date 2026-10-21) | capture + DB |
| เลขที่ถัดไป | `select doc_no from ic_trans where (doc_date >= '<ต้นปี>') and doc_no like 'SO2610%' AND trans_flag = 36 and trans_type = 2 order by doc_no desc limit 1` → +1 | **ไม่มีการล็อก** — คำนวณตอนเปิดหน้าจอ; ป้องกันซ้ำด้วย unique index `(doc_no, trans_flag)` บน `ic_trans` (มีครบทั้ง 13 tenant) → เลขชนกันจะทำให้ transaction ข้อ 3 ล้มทั้งชุด | capture + `pg_indexes` |
| ตรวจวงเงินลูกค้า | `erp_option.sr_ss_credit_check` | ถ้า = 1 และ `inquiry_type` เป็นเชื่อ (0 หรือ 2): เรียก `_creditMoneyCheck` → เกินวงเงิน: ถ้า `check_credit_sale_reserve_sale_order` = 1 **ห้ามบันทึก**, ไม่เช่นนั้นถามผู้ใช้แล้วบันทึกแบบ **`ic_trans.is_hold = 1` + `insert into erp_credit_request (...)`** ในชุดเดียวกัน; ไม่เกิน: `ic_trans.auto_approved = 1`; ถ้าเป็นเงินสด (1 หรือ 3) → `auto_approved = 1` | **from-code** (`_icTransControl.cs` ~14221–14280, ~14953, ~14988, ~16497) — ทั้ง 13 tenant `sr_ss_credit_check = 0` จึงยังไม่เคยเห็นจริง; `wawacrm` มี `check_credit_sale_reserve_sale_order = 1` |
| VAT / ทศนิยม | `erp_option.vat_rate`, `item_*_decimal` | ห้าม hard-code 7% และ 2 ตำแหน่ง ([[tenants-overview]] §4) | DB |
| หน่วยนับ | `ic_unit_use` ของสินค้า | `stand_value`, `divide_value` ต่อบรรทัด (SO26100001 = 1/1) | capture |

## 2. Transaction หลัก (ข้อ 3) — คอลัมน์ที่โปรแกรมใส่จริง

ใส่ตามลำดับนี้ใน transaction เดียว คอลัมน์ที่ไม่ได้ใส่จะได้ค่า default ของตาราง (ยังไม่ได้ทำรายการ default ทุกคอลัมน์)

### 2.1 `ic_trans` (39 คอลัมน์)
| คอลัมน์ | ค่าใน SO26100001 | ความหมาย / ที่มา |
|---|---|---|
| `trans_type` | 2 | ฝั่งขาย |
| `trans_flag` | 36 | ใบสั่งขาย ([[trans_flag]]) |
| `status` | 0 | |
| `doc_date`, `doc_time` | 2026-10-21, `09:44` | `doc_time` = เวลาตอนเปิดเอกสาร ไม่ใช่เวลาบันทึก (บันทึก 09:45:56) |
| `doc_no`, `doc_format_code` | SO26100001, SO | ดูข้อ 1 |
| `cust_code`, `contactor` | รหัสลูกค้า, ชื่อผู้ติดต่อ | |
| `doc_ref`, `doc_ref_date` | null | ไม่ได้อ้างเอกสารต้นทาง |
| `inquiry_type` | 0 | **0 = ขายเชื่อ, 1 = ขายสด, 2 = เชื่อ (สินค้าบริการ), 3 = สด (สินค้าบริการ)** — ลำดับจาก `_g.g._saleType` + ป้ายใน `SMLERPTemplate/smldatabase.xml` (ชื่อ field `cash_sale_service`/`credit_sale_service` สลับกับป้าย แต่ลำดับที่แสดงตรงกับโค้ดตรวจวงเงินที่ถือว่า 0/2 = เชื่อ) |
| `vat_type` | 1 | 0 แยกนอก, 1 รวมใน, 2 ยกเว้น ([[pricing-vat-gl]]) |
| `vat_rate` | 7.00 | จาก `erp_option.vat_rate` |
| `sale_code`, `sale_group` | null | |
| `expire_day`/`expire_date`, `credit_day`/`credit_date`, `send_day`/`send_date` | 0 / doc_date | วันหมดอายุ, เครดิต, วันส่ง = doc_date + จำนวนวัน |
| `total_value` | 600.00 | ผลรวมรายการ |
| `total_discount`, `discount_word` | 0, null | |
| `total_before_vat` | 560.75 | **คิดจากยอดรวม**: 600 / 1.07 = 560.75 (ผลรวมรายบรรทัด = 560.74) |
| `total_vat_value` | 39.25 | 600 − 560.75 (ผลรวมรายบรรทัด = 39.26) |
| `total_after_vat`, `total_amount` | 600.00 | |
| `total_except_vat` | 0 | ยอดสินค้ายกเว้นภาษี |
| `send_type` | 0 | |
| `remark` … `remark_5` | ข้อความ | |
| `is_pos` | 0 | |
| `creator_code`, `create_datetime` | ผู้ใช้, เวลาบันทึก | |

### 2.2 `ic_trans_detail` (60 คอลัมน์ ต่อบรรทัด)
| คอลัมน์ | ค่า | ความหมาย / ที่มา |
|---|---|---|
| `cust_code`, `trans_type`, `trans_flag`, `doc_no`, `doc_date`, `doc_time`, `is_pos`, `inquiry_type`, `vat_type` | ซ้ำกับหัว | |
| `doc_date_calc`, `doc_time_calc` | = doc_date, doc_time | ใช้เรียงลำดับคำนวณต้นทุน — โค้ดตั้งตอน insert (คอมเมนต์ใน `_updateDateTimeForCalc`) |
| `sale_code`, `sale_group` | `''` | (หัวเป็น null, บรรทัดเป็นค่าว่าง) |
| `status` | 0 | |
| `calc_flag` | 1 | ใช้ในสูตรค้างส่ง ([[stock-cost]]) |
| `last_status` | 0 | ยังไม่ถูกยกเลิก |
| `auto_create` | 0 | |
| `branch_code` | `000` | ยังไม่ได้ไล่ว่ามาจาก field ไหน |
| `doc_ref_type`, `ref_doc_no`, `ref_row` | 0, null, −1 | ไม่ได้ดึงจากเอกสารอื่น |
| `item_code`, `item_name`, `barcode` | | |
| `wh_code`, `shelf_code` | `AB-1`, `001` | คลัง / ที่เก็บ |
| `unit_code`, `stand_value`, `divide_value` | กล่อง, 1, 1 | |
| `qty`, `price`, `sum_amount` | 1, 300, 300 | |
| `discount`, `discount_amount` | null, 0 | |
| `price_exclude_vat`, `sum_amount_exclude_vat`, `total_vat_value` | 280.37, 280.37, 19.63 | ต่อบรรทัด (300 / 1.07) |
| `set_ref_line`, `set_ref_qty`, `set_ref_price` | null, 0, 300 | สินค้าชุด |
| `item_type` | 0 | ถูกแก้ให้ตรง `ic_inventory.item_type` ภายหลังในขั้น 7 |
| `item_code_main`, `ref_guid`, `price_guid`, `user_approve` | null | |
| `is_permium` (สะกดตาม schema), `is_get_price` | 0, 1 | |
| `price_mode`, `price_type` | `'6'`, `'6'` | `_findPriceClass` ตั้ง `_type = 6` ในกิ่ง "ราคาตามสูตร" (`ic_inventory_price_formula`) — ยังไม่ได้ไล่ว่า field รับค่าจาก `_type` ตรง ๆ |
| `is_serial_number`, `tax_type`, `lot_number_1`, `mfd_date`, `mfn_name`, `price_set_ratio` | 0/null | |
| `hidden_cost_1_exclude_vat`, `is_lock_cost`, `sum_of_cost_fix` | 0 | |
| `remark` | ข้อความ | |
| `line_number` | 0, 1, … | **เริ่มที่ 0** |

### 2.3 `ic_trans_shipment` (19 คอลัมน์, 1 แถวต่อเอกสาร)
`doc_no, doc_date, trans_flag, cust_code, transport_name, transport_address, transport_province, transport_amper, transport_tambon, transport_country, zipcode, transport_telephone, transport_fax, transport_code, destination, ship_code, logistic_area, latitude, longitude` — unique `(doc_no, trans_flag)`

### 2.4 (เฉพาะเมื่อเปิดตรวจวงเงิน) `erp_credit_request`
`insert into erp_credit_request (doc_no, trans_flag, credit_money, credit_money_max, chq_amount, advance_amount, ar_balance_amount, sr_amount, ss_amount, bill_amount, over_amount, over_percent, credit_status)` — `doc_no` ใส่ทีหลังด้วย `string.Format(query, docNo)` (~บรรทัด 16501) · **from-code เท่านั้น** (`_creditMoneyCheck` ~บรรทัด 11732/11766) ยังไม่ได้เห็นจริง (`aoy.erp_credit_request` = 0 แถว)

## 3. หลัง commit
1. **`logs`** (database ร้าน, `_createLog(mode)`): `function_type=2`, `screen_code` = trans_flag (36), `function_code` = mode (1 เพิ่ม / 2 แก้ / 3 ลบ), `menu_name='menu_so_sale_order'`, `doc_amount` = total_amount, `doc_qty` = ผลรวมจำนวน, `data1` = ค่าบนหน้าจอแบบ XML-escape, `guid` = GUID ใหม่ (`ToString("N")`), `computer_name`, `user_code`, `date_time`
2. **`erp_logs`** (database `<db>_logs`, `_writeFullLogs`): `doc_no, computer_name, menu_name, function_code, user_code, date_time, doc_date, old_doc_date ('1900-1-1' เมื่อเป็นใบใหม่), old_doc_no, trans_flag, trans_type, old_doc_amount, doc_amount, old_cust_code, cust_code, data_new` (JSON จาก `_getLogsJsonStr`)
3. **doc flow** (`SMLProcess._docFlow._processAll`): สำหรับใบนี้เอง เห็นแค่ `update ic_trans_detail set last_status = 0 where doc_no = ? and trans_flag in (36) and last_status <> 0` และเหมือนกันกับ `ap_ar_trans_detail` — **ไม่แตะ `used_status`/`doc_success` ของใบสั่งขาย** (จะเปลี่ยนเมื่อมีบิลมาอ้างอิง ดูข้อ 5)
4. **`_updateDateTimeForCalc`**: แก้ `gl_wht_list_detail.due_date`/`cust_code` ให้ตรงหัว (ไม่เกี่ยวกับใบสั่งขายโดยตรง ทำทุกครั้ง)
5. **`_process_stock_balance(items, "36")`** (`SMLICProcess.java`):
   - ปรับ `ic_trans_detail.item_type` ให้ตรง `ic_inventory` (`WITH inventory … UPDATE ic_trans_detail …`)
   - flag 36 อยู่ใน `_stockAccruedOut = "[36],[37],[34],[39]"` แต่**ไม่อยู่ใน** `_stockBalanceFlag` → คำนวณ **ค้างจอง (`book_out_qty`) และค้างส่ง (`accrued_out_qty`)** ด้วย CTE `bookout`/`accout` แล้วตั้ง 0 ให้สินค้าที่ไม่มีเอกสารค้าง; **ไม่เปลี่ยน `balance_qty`**
   - คิวต้นทุน: `delete from process where process_name='IC' and wherein in (…)` → `insert into process (process_name, wherein) (select 'IC', code from ic_inventory where code in (…))`

**สิ่งที่ไม่เกิดกับใบสั่งขาย** (ยืนยันจาก capture): ไม่มี `ap_ar_trans`/`ap_ar_trans_detail`, ไม่มี `cb_trans`, ไม่มี GL (`gl_journal*`), ไม่มี `gl_journal_vat_sale`, ไม่เปลี่ยนยอดคงเหลือ

**ต่อสายเอกสาร:** เมื่อบิลขาย 44 ดึงใบนี้ บรรทัดของบิลจะมี `doc_ref_type = 3`, `ref_doc_no = 'SO26100001'`, `ref_row` = line_number ต้นทาง และหลัง doc flow ของบิล ใบสั่งขายได้ `used_status = 1`, `doc_success = 1` (ยืนยันใน DB 2026-10-21) ดู [[runtime-verified]] §7

## 4. สำหรับ sml_mcp_ai (ตาม [[adr-001-write-path]])
- `preview_sale_order`: ตรวจลูกค้า/สินค้า/หน่วย/คลัง/ที่เก็บมีจริง, อ่าน `erp_option` (vat_rate, ทศนิยม, `sr_ss_credit_check`, `check_credit_sale_reserve_sale_order`) และ `erp_doc_format`, คำนวณยอดแบบเดียวกับข้อ 2 (VAT หัวคิดจากยอดรวม), คืนเลขที่ที่**คาดว่า**จะได้ + `confirmation_token`
- `commit_sale_order`: ใน transaction เดียว — หาเลขที่ใหม่อีกครั้ง → insert ข้อ 2.1–2.3 (+ 2.4/`is_hold`/`auto_approved` ถ้าร้านเปิดตรวจวงเงิน) → ส่วนที่ 1 ของงานสต็อก (ข้อ 3.5: item_type, ค้างจอง/ค้างส่ง) → คิว `process` 'IC' → `logs`; เลขชน unique → rollback แล้วลองเลขถัดไป (จำกัดจำนวนครั้ง)
- หลัง commit: `erp_logs` แบบมี reconcile
- ไม่ต้องทำ doc flow ของใบนี้เอง (มีแค่ reset `last_status` ซึ่งเป็น 0 อยู่แล้วตอนสร้าง)
- idempotency: เก็บ key + hash ของ payload ใน DB ของ sml_mcp_ai เอง (ไม่มีคอลัมน์สำหรับเรื่องนี้ใน `ic_trans`)

## 5. ยังไม่ทราบ (ต้องตรวจก่อนเขียนโค้ด)
- ค่า default ของคอลัมน์ที่โปรแกรมไม่ได้ใส่ (`used_status`, `doc_success`, `approve_status`, `is_cancel` … — SO26100001 ตอนนี้เป็น 0 ยกเว้นที่บิลมาอัปเดต)
- `branch_code = '000'` มาจากผู้ใช้หรือจากบริษัท
- `ic_trans.vat_type = 1` แต่ `erp_doc_format.vat_type` ของ SO = 0 — ยังไม่ได้ไล่ว่าค่า vat_type ของเอกสารมาจากไหน (ผู้ใช้เลือก / ลูกค้า / ตัวเลือกร้าน)
- `price_mode`/`price_type` ได้ค่าจาก `_findPriceClass._type` ตรง ๆ หรือไม่ และค่าอื่นแปลว่าอะไร
- `<ต้นปี>` ในการหาเลขที่ (`doc_date >= '2026-01-01'`) มาจากปีปฏิทินหรือรอบบัญชี (`erp_account_period`)
- พฤติกรรมเมื่อเปิด `sr_ss_credit_check` (ยังไม่เคยเห็นจริงบน tenant ใด)
- ใบสั่งขายที่ดึงจากใบเสนอราคา (30) / ใบจอง (34), ส่วนลดท้ายบิล, หลายคลัง, สินค้าชุด, serial/lot — ต้องดักจับเพิ่ม

## 6. ยืนยันจากรอบ 4 (capture aoy-run4, 2026-10-21 16:04–16:10): ดึงจากใบเสนอราคา / แก้ไข / ยกเลิก
### 6.1 สร้างใบสั่งขายจากใบเสนอราคา (SO26100002 จาก QT26090001, 16:06:50)
- Transaction เดียว: `ic_trans` (39 คอลัมน์) → `ic_trans_detail` × 2 → **`ap_ar_trans_detail` (10 คอลัมน์: `calc_flag=1, trans_type=2, trans_flag=36, doc_date, doc_no, bill_type=1, billing_no='QT26090001', billing_date=<วันที่ใบเสนอราคา>, remark, line_number=0`)** → `ic_trans_shipment` → `COMMIT`
- หัว `doc_ref` = null (การอ้างอยู่ที่บรรทัด) · บรรทัด **`doc_ref_type=1`, `ref_doc_no='QT26090001'`, `ref_row=-1`** (ไม่ใช่ line_number ของต้นทาง ต่างจากบิลที่ดึงจาก SO)
- ⇒ `doc_ref_type`/`bill_type` = **ประเภทเอกสารต้นทางตามมุมมองของเอกสารปลายทาง**: ใบสั่งขาย 1 = ใบเสนอราคา · บิลขาย 3 = ใบสั่งขาย, 2 = ใบจอง · ใบลดหนี้ 1 = บิลขาย ([[write-spec-credit-note]])
- doc flow 16:06:58: `update ic_trans set used_status=1, doc_success=1 where roworder=<QT>` (ดึงครบทุกจำนวน)
- ใบสั่งขายนี้ `inquiry_type=1` (ผู้ใช้เลือกขายสด)

### 6.2 แก้ไขใบสั่งขาย (mode 2, 16:07:40–16:07:56)
- **ล็อกเอกสารตอนเปิดแก้:** `select guid_code from ic_trans where doc_no=? and trans_flag=36 and guid_code is not null` (มีคนแก้อยู่หรือไม่) → `update ic_trans set guid_code=<GUID session> where doc_no=? and trans_flag=36`; ปิดหน้าจอ/เปลี่ยนเอกสาร → `update ic_trans set guid_code=null where … and guid_code is not null` ดู [[document-engine]] § การล็อกเอกสาร
- **บันทึกแก้ไข = ลบแล้วใส่ใหม่ทั้งหมดใน transaction เดียว:**
  `delete from ic_trans where doc_no=? and trans_flag=36` → `insert ic_trans` (**41 คอลัมน์** = 39 + `last_editor_code`, `lastedit_datetime`; `creator_code`/`create_datetime` ส่งค่าเดิมกลับไป) → `delete from ic_trans_detail …` → `delete from ic_trans_serial_number …` → `delete from ap_ar_trans_detail where doc_no=? and trans_flag=36` → insert บรรทัดใหม่ → insert `ap_ar_trans_detail` ใหม่ → `delete from ic_trans_shipment …` → insert ใหม่ → `COMMIT`
- ⚠️ **`roworder` ของหัวเอกสารเปลี่ยน** (SO26100002 ได้ roworder ใหม่ 1153) และ `guid_code` หายไปเพราะแถวใหม่ไม่ได้ใส่ — การล็อกจึงปลดไปพร้อมการบันทึก
- doc flow 16:08:16: ใบเสนอราคา `doc_success=0` (จำนวนที่ดึงเหลือ 6 จาก 10)

### 6.3 ยกเลิกใบสั่งขาย (SSC26100001, 37 type 1, 16:10:01) — ดู [[write-spec-cancel]] B
