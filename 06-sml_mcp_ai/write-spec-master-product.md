---
tags: [sml, sml_mcp_ai, write-spec, master-data, product, unit, barcode]
status: verified-runtime รอบ 4 (สร้างสินค้าหลายหน่วย + บาร์โค้ดจากหน้าจอข้อมูลสินค้า) · หน้าจอบาร์โค้ดแยก verified-runtime รอบ 5.2 · แก้ไข/ลบสินค้า from-code
source: smlerp SMLERPIC/_icMain.cs (`_saveData`, `_dataList__deleteData`), SMLERPIC/_icBarcode.cs, SMLERPControl/_icmainScreenTopControl.cs, SMLERPGlobal/_utils.cs (`_updateInventoryMasterFunction`), MyLib/_myScreen.cs, SMLERPTemplate/smldatabase.xml + DB aoy/kbgtest/samai/wawacrm (2026-10-21, นับ/โครงสร้างเท่านั้น)
---
# สเปกข้อมูลหลัก: สินค้า / หน่วยนับ / บาร์โค้ด

กลับไป [[00-Index]] · ราคา [[pricing-vat-gl]] · สต็อก/ต้นทุน [[stock-cost]] · เมนู [[module-inventory]]

> หน้าจอ: ข้อมูลสินค้า › ข้อมูลสินค้า (`menu_ic_item_detail`, `SMLERPIC._icMain`), กำหนดบาร์โค้ดสินค้า (`menu_ic_item_barcode`, `SMLERPIC._icBarcode`), กำหนดหน่วยนับสินค้า (`menu_setup_ic_unit`, `MyLib._manageMasterCodeFull` → ตาราง `ic_unit`)
> ✅ รอบ 4 ยืนยันการสร้างสินค้า ZZTEST-0001 (§10) · ⚠️ หน้าจอบาร์โค้ดแยก, แก้ไข, ลบ ยังเป็นข้อมูลจากโค้ด

## 1. ตารางและความสัมพันธ์
| ตาราง | หน้าที่ | Unique (ตรวจ `pg_indexes` aoy) |
|---|---|---|
| `ic_unit` | รายชื่อหน่วยนับกลางของร้าน (`code, name_1, name_2, status, guid_code`) | `code` |
| `ic_inventory` | หัวสินค้า (รหัส, ชื่อ, ประเภท, หน่วย, วิธีต้นทุน, ยอดคงเหลือ/ต้นทุนที่ระบบคำนวณ) | `code` |
| `ic_inventory_detail` | ข้อมูลเสริม 106 คอลัมน์ (กลุ่มบัญชี, คลังเริ่มต้นซื้อ/ขาย, จุดสั่งซื้อ, ผู้ดูแล …) — **1 แถวต่อสินค้า** | `ic_code` |
| `ic_unit_use` | หน่วยนับที่สินค้านี้ใช้ + อัตราแปลง (`code, line_number, stand_value, divide_value, ratio, row_order, width_length_height, ic_code, remark, weight, status, unit_size`) | `(code, ic_code)` |
| `ic_opposite_unit` | หน่วยนับขนาน (เฉพาะ edition Account/AccountPro/**AccountPOSPro**/CM) | — |
| `ic_wh_shelf` | คลัง/ที่เก็บที่สินค้าอยู่ได้ (`wh_code, shelf_code, max_point, min_point, ic_code, remark, status, shelf_list`) | `(wh_code, shelf_code, ic_code)` |
| `ic_inventory_barcode` | บาร์โค้ด → สินค้า + หน่วย + ราคาตามบาร์โค้ด (`ic_code, barcode, description, wh_code, shelf_code, unit_code, price, price_2..4, price_member..4, status, line_number, no_point, is_clearance, from_date, to_date, hidden_text, guid_code`) | **`barcode` อย่างเดียว** (ห้ามซ้ำทั้งร้าน ไม่ผูกกับสินค้า) |
| `ic_standard_cost` | ต้นทุนมาตรฐาน (cost_type 4) | `(ic_code, date_start)` |
| `ic_inventory_price`, `ic_inventory_price_formula` | ราคาขาย ([[pricing-vat-gl]]) — หน้าจอแยก | `roworder` (index `unique_ic_inventory_price_formul_idx` **ไม่ใช่ unique** จริง) |
| `master_logs` (database ร้าน ไม่ใช่ `_logs`) | log การแก้ข้อมูลหลัก — คอลัมน์จริงใน aoy: `function_code, data1, data2, user_code, date_time, screen_code, guid, function_type, computer_name, menu_name, code, name_1` | |

**การแปลงหน่วย:** จำนวนในหน่วยมาตรฐาน = `qty × stand_value / divide_value` ของแถว `ic_unit_use` (สูตรเดียวกับ `ic_trans_detail` ใน [[stock-cost]]) — ตัวอย่าง aoy AH-0026: แท่ง = 1/1, แพ็ค = 12/1 ⇒ 1 แพ็ค = 12 แท่ง; บาร์โค้ดแยกต่อหน่วย (แท่ง 60 บาท, แพ็ค 290 บาท)

## 2. ค่ารหัส (ป้ายจาก `smldatabase.xml`, ลำดับจาก `_icmainScreenTopControl.cs` ~81–128)
| คอลัมน์ | ค่า |
|---|---|
| `item_type` | 0 สินค้าทั่วไป · 1 สินค้าบริการ (ไม่ทำสต๊อก) · 2 สินค้าให้เช่า · 3 สินค้าชุด (ไม่ทำสต๊อก) · 4 สินค้าฝากขาย · 5 สูตรการผลิต · 6 สีผสม — สูตรยอดคงเหลือนับเฉพาะ `item_type in (0,4,6)` ([[stock-cost]]) |
| `unit_type` | 0 หน่วยนับเดี่ยว · 1 หลายหน่วยนับ · 2 หน่วยนับขนาน · 3 หลายหน่วยนับ+หน่วยนับขนาน (2–3 แสดงเฉพาะ edition Account/AccountPro/IMS/AccountPOSPro/CM) |
| `cost_type` | 0 ถัวเฉลี่ย · 1 FIFO · 2 กำหนดเอง (lot) · 3 ตามวันหมดอายุ · 4 มาตรฐาน · 5 อื่น 1 ([[stock-cost]]) |
| `tax_type` | 0 `normal_vat` · 1 `exc_vat` |

การใช้จริง: aoy `item_type` 0/1/3/4 = 55/3/4/5, `unit_type` 0/1 = 61/6 · kbgtest `unit_type` 1 = 299 จาก 20,111 · samai `unit_type` 1 = 9,332 จาก 9,344

## 3. ก่อนบันทึก (`_icMain._saveData`)
- สิทธิ์: `MyLib._myGlobal._checkChangeMaster()` → `_allowChangeMaster` ซึ่งตั้งจาก `erp_user_group.is_change_masterdata == 1` (`SMLERPGlobal/_global.cs` ~3728) ไม่ผ่าน → "ไม่อนุญาติให้แก้ไขข้อมูล"
- ช่องห้ามว่าง (`isEmtry=false` ใน `_addTextBox`, `MyLib/_myScreen.cs` ~1965): **`code`, `name_1`, `unit_cost` (หน่วยต้นทุน), `unit_standard` (หน่วยมาตรฐาน)** — ช่องอื่น (`name_2`, `name_eng_*`, `sign_code`, `income_type`, `item_pattern`, `supplier_code` …) ว่างได้
- `unit_cost` **ต้องมีในตารางหน่วยนับของสินค้า** ("ไม่พบหน่วยต้นทุนในตารางหน่วยนับ") และ `unit_standard` ต้องมีเช่นกัน ("ไม่พบหน่วยมาตรฐานในตารางหน่วยนับ")
- ต้องมีคลัง/ที่เก็บอย่างน้อย 1 แถว ("ยังไม่บันทึกคลังที่เก็บ") — **ยกเว้น**ร้านเปิด `erp_option.enable_all_ic_wh_shelf` หรือโหมด sync
- ข้อมูลจริง: ทั้ง 4 ร้านรหัสสินค้าเป็นตัวพิมพ์ใหญ่ทั้งหมด (โค้ดเทียบด้วย `upper()` ทุกจุด) · aoy/kbgtest/wawacrm ไม่มีสินค้าที่ขาดแถว `ic_unit_use` ของหน่วยมาตรฐาน; **samai ขาด 90 รายการ** (ข้อมูลเก่า/นำเข้า — ระบบที่อ่านต้องรับมือ) · บาร์โค้ดซ้ำ = 0 ทุกร้าน (บังคับด้วย unique)

## 4. บันทึกสินค้าใหม่ (mode 1) — 1 batch (`_queryList`)
1. `delete from ic_inventory_detail where not exists (select code from ic_inventory where ic_inventory.code=ic_inventory_detail.ic_code)` (ล้างแถวกำพร้า)
2. `insert into ic_inventory (<ช่องบนหน้าจอหลัก + หน้าจอเพิ่มเติม>, create_code, create_datetime=now())`
3. `insert ic_unit_use` ทุกแถวในตารางหน่วยนับ (`_icmainGridUnit._createQueryForInsert`)
4. `insert ic_opposite_unit` (เฉพาะ edition ข้างต้น — รวม AccountPOSPro)
5. `insert ic_wh_shelf` (ถ้าไม่ใช่โหมด sync)
6. `insert into ic_inventory_detail (ic_code, have_point) values (…)`
7. `insert ic_inventory_barcode` (ถ้าไม่ใช่โหมด sync)
8. `insert ic_standard_cost`

**แก้ไข (mode 2):** `update ic_inventory set … , last_update_code, last_update_date_time=now() where <รหัสเดิม>` แล้ว **ลบแล้วใส่ใหม่ทั้งชุด** สำหรับ `ic_unit_use`, `ic_opposite_unit`, `ic_wh_shelf` (ไม่ใส่ใหม่ถ้า `enable_all_ic_wh_shelf`), `ic_inventory_barcode`, `ic_standard_cost` (`where upper(ic_code) in (<รหัสเดิม>, <รหัสใหม่>)`) + `update ic_inventory_detail set have_point=…`

## 5. หลังบันทึก
1. `insert into master_logs (function_code, computer_name, guid, menu_name, screen_code, function_type, user_code, date_time, code, name_1, data1, data2)` — **ยืนยันรอบ 4: ไม่มี `module_name`** (โค้ดที่มี `module_name` ใน `_createLog` ไม่ใช่เส้นทางที่รันจริงบน edition นี้)
2. `_utils._updateInventoryMasterFunction()` (1 batch):
   - `ic_inventory.unit_standard_name` = ชื่อจาก `ic_unit`
   - `unit_standard_stand_value`/`unit_standard_divide_value`: ตั้ง 1 ถ้าว่าง/0 หรือ `unit_type=0`; ถ้า `unit_type=1` ใช้ค่าจาก `ic_unit_use` ของหน่วยมาตรฐาน (ข้อมูลจริง: ค่าไม่ตรง = 0 ทุกร้าน)
   - `ic_inventory_barcode.description` = ชื่อสินค้า
   - `insert into ic_inventory_detail (ic_code) select UPPER(code) from ic_inventory where not exists (…)` (ถ้าไม่ใช่ `activeSync`) ⇒ ข้อมูลจริง: สินค้าที่ไม่มีแถว detail = 0 ทุกร้าน
3. `SMLProcess._docFlow._processAll(สินค้า_ปรับปรุงสต็อก, '<รหัส>', '')`
4. `_process_stock_balance('<รหัส>', "*")` — คำนวณยอดคงเหลือ/ค้างทุกแบบของสินค้านี้ใหม่ + คิว `process` 'IC'

## 6. บาร์โค้ด (หน้าจอแยก `_icBarcode`)
- บันทึก = `delete from ic_inventory_barcode where upper(ic_code) = '<รหัส>'` แล้ว insert ทุกแถวในตาราง (แทนที่ทั้งชุดของสินค้านั้น)
- unique ที่ `barcode` ⇒ บาร์โค้ดที่ซ้ำกับสินค้าอื่นจะทำให้ทั้ง batch ล้ม
- `unit_code` ของบาร์โค้ด**ไม่ถูกบังคับ**ให้อยู่ใน `ic_unit_use`: kbgtest มี 1,933 แถว, wawacrm 9, samai 1 ที่หน่วยของบาร์โค้ดไม่มีในหน่วยนับของสินค้า
- ราคาตามบาร์โค้ด (`price`, `price_2..4`, `price_member*`) เป็นแหล่งราคาลำดับ 6 ใน [[pricing-vat-gl]] และ POS ใช้


### 6.1 ยืนยันจากรอบ 5.2 (2026-10-26, เมนู 2.1.7 กำหนดบาร์โค้ดสินค้า, `ZZTEST-0001` เพิ่ม `8859999000035` หน่วยชิ้น ราคา 3.00)
- ผู้ใช้ทดสอบ 3 ครั้ง: **เพิ่ม** บาร์โค้ดใหม่แล้วบันทึก (10:27:18, 3 บรรทัด) → **ลบ** บรรทัดนั้นออกจากตารางแล้วบันทึก (10:29:09, 2 บรรทัด) → **เพิ่มใหม่** แล้วบันทึก (10:29:35, 3 บรรทัด) — ทั้งเพิ่มและลบใช้คำสั่งรูปแบบเดียวกัน
- ลำดับต่อการแก้ 1 ครั้ง:
  1. เปิดสินค้า: `select * from ic_inventory_barcode where upper(ic_code)=?` + **ล็อก** `update ic_inventory set guid_code=<GUID> where code=?`
  2. Transaction 1: `delete from ic_inventory_barcode where upper(ic_code) = ?` → `insert into ic_inventory_barcode (ic_code, barcode, unit_code, price, price_member, price_2, price_member_2, price_3, price_member_3, price_4, price_member_4, hidden_text, no_point, is_clearance, from_date, to_date)` ทุกบรรทัดในตาราง → `COMMIT`
  3. Transaction 2 (`_updateInventoryMasterFunction`): ซ่อม `ic_inventory.unit_standard_*` + `update ic_inventory_barcode set description = ic_inventory.name_1` + เติม `ic_inventory_detail` ที่ขาด → `COMMIT`
  4. ปลดล็อก `update ic_inventory set guid_code=null`
- **ยืนยัน "ลบทั้งชุดแล้วใส่ใหม่":** `roworder` ของบาร์โค้ดเดิม 152, 153 → หลังบันทึกเป็น 159, 160, 161 · **การลบบาร์โค้ดในหน้าจอนี้ไม่มีคำสั่ง delete แยก** — บรรทัดที่ไม่อยู่ในตารางตอนกดบันทึกจะหายไปเพราะลบทั้งชุดแล้วไม่ถูก insert กลับ (ครั้งที่ 2)
- ราคาที่พิมพ์ในหน้าจอนี้ (ราคากลุ่มที่ 1 ราคาทั่วไป) เก็บที่ `ic_inventory_barcode.price` ตารางเดียว — ไม่แตะ `ic_inventory_price` · บาร์โค้ดเดิมที่โหลดมาถูกเขียนกลับด้วยทศนิยม 14 หลัก (`1.00000000000000`) ส่วนแถวใหม่ใช้ค่าตามที่พิมพ์ (`3.00`)
- ไม่มีงานสต็อก/คิว `process`/doc flow
- **สำหรับ sml_mcp_ai:** การเพิ่มบาร์โค้ด 1 ตัวต้องอ่านบาร์โค้ดทั้งหมดของสินค้าแล้วส่งกลับครบชุด (หรือ insert แถวเดียวโดยไม่ลบ ซึ่งต่างจากโปรแกรม — ต้องตัดสินใน ADR) และต้องล็อก/ปลดล็อก `guid_code` เหมือนโปรแกรม

## 7. ลบสินค้า (`_dataList__deleteData`)
- **ห้ามลบถ้ามีใน `ic_trans_detail`** (`select count(doc_no) … where item_code=…` > 0 → "สินค้ามีการใช้ไปแล้ว ห้ามลบ")
- ลบ: `ic_inventory`, `ic_unit_use`, `ic_opposite_unit`, `ic_wh_shelf`, `ic_inventory_detail`, `ic_name_billing`, `ic_name_merket`, `ic_color_use`, `ic_size_use`, `ic_name_short`, `ic_name_pos`, `ic_pattern_use`, `ic_inventory_set_detail`, `ic_inventory_barcode` + `master_logs`

## 8. สำหรับ sml_mcp_ai
- **อ่าน:** `search_product` ปัจจุบันอ่าน `ic_inventory`, `ic_unit_use`, `ic_inventory_barcode`, `ic_inventory_price(_formula)`, `ic_trans(_detail)` — ต้อง
  - แปลงหน่วยด้วย `stand_value/divide_value` ของ `ic_unit_use` (ไม่ใช่ `ic_unit`)
  - ค้นบาร์โค้ดผ่าน `ic_inventory_barcode.barcode` (unique) แล้วได้ทั้ง `ic_code` และ `unit_code`
  - รองรับสินค้าที่ไม่มีแถว `ic_unit_use` ของหน่วยมาตรฐาน (samai) และบาร์โค้ดที่หน่วยไม่อยู่ใน `ic_unit_use`
- **เขียน (ถ้าจะเปิด):** ทำตามข้อ 3–5 ใน transaction เดียว (รวม `_updateInventoryMasterFunction` ส่วนของสินค้านั้น และ `master_logs`) + เรียกงานสต็อกของสินค้านั้น; ตรวจบาร์โค้ดซ้ำทั้งร้านก่อน; **ห้าม** แก้ `unit_standard`/อัตราแปลงของสินค้าที่มีเอกสารแล้ว จนกว่าจะเข้าใจผลกระทบ (โค้ดมี `_changeUnitCodeRatio` ที่ไล่แก้ `stand_value/divide_value` ใน `ic_trans_detail` ย้อนหลัง — ยังไม่ได้ไล่ว่าเรียกจากไหน)
- แนะนำลำดับความเสี่ยงต่ำ → สูง: บาร์โค้ดเพิ่ม (ไม่แตะเอกสาร) → สินค้าใหม่ → แก้ชื่อ/ข้อมูลทั่วไป → แก้หน่วย/อัตราแปลง (สูงสุด)

## 9. ยังไม่ทราบ
- SQL จริงครบชุดของ `insert ic_inventory` (คอลัมน์ที่หน้าจอส่ง) — ต้องดักจับการสร้างสินค้า 1 รายการ
- `_changeUnitCodeRatio` (`_icMain.cs` ~529) ถูกเรียกเมื่อใด
- ผลของ `_docFlow._processAll(สินค้า_ปรับปรุงสต็อก, …)` หลังบันทึกสินค้า
- หน่วยนับขนาน (`ic_opposite_unit`) ใช้ในการคำนวณอย่างไร
- กฎของ `ic_inventory_price` / `ic_inventory_price_formula` ตอนบันทึก (หน้าจอราคาแยก)
- ~~`master_logs.module_name`~~ → ตอบแล้ว (ไม่ได้ใส่จริง)

## 10. ยืนยันจากรอบ 4: สร้างสินค้า ZZTEST-0001 (16:27:53)
**Transaction เดียว** ตรงกับลำดับในโค้ด §4:
1. `delete from ic_inventory_detail where not exists (…)`
2. `insert ic_inventory` (33 คอลัมน์): `code, ic_serial_no=0, tax_type=0, item_type=0, name_1, name_2, name_eng_1, name_eng_2, unit_type=1, unit_cost, unit_standard, cost_type=0, income_type, item_pattern, supplier_code, sign_code, account_code_1..4, update_detail=1, update_price=1, manufacturer_code, drink_type=0, use_expire=0, production_period=0, barcode_checker_print=0, print_order_per_unit=0, is_eordershow=0, is_speech=0, pos_no_sum=0, create_code, create_datetime=now()`
3. `insert ic_unit_use` ต่อหน่วย (11): `ic_code, line_number (0,1), code, stand_value, divide_value, ratio (= stand/divide: 1, 6), row_order (1, 2), width_length_height, weight, unit_size=0, status=1`
4. `insert ic_wh_shelf` ต่อแถว (7): `ic_code, wh_code, shelf_code, shelf_list=null, min_point=0, max_point=0, status=1`
5. `insert into ic_inventory_detail (ic_code, have_point) values (?, 0)`
6. `insert ic_inventory_barcode` ต่อบาร์โค้ด (16): `ic_code, barcode, unit_code, price, price_member, price_2, price_member_2, price_3, price_member_3, price_4, price_member_4, hidden_text, no_point=0, is_clearance=0, from_date, to_date`
7. `COMMIT` — **ไม่มี** `ic_opposite_unit` และ `ic_standard_cost` เพราะ grid ว่าง (grid ว่างไม่สร้างคำสั่ง)
- หลัง commit: `master_logs` (16:27:53.667) → ชุด `_updateInventoryMasterFunction` (`unit_standard_name`, `unit_standard_stand/divide_value`, `ic_inventory_barcode.description`, เติม `ic_inventory_detail`) → (16:27:55) `_process_stock_balance('<รหัส>', "*")`: `item_type`, `balance_qty` … คิว `process`
- ผลใน DB: `unit_standard_name='ชิ้น'`, `unit_standard_stand_value=1`, `unit_standard_divide_value=1`, `ic_inventory_detail` 1 แถว
- หน้าจอ "กำหนดบาร์โค้ดสินค้า" ไม่ได้ทดสอบในรอบนี้ (ผู้ใช้ใส่บาร์โค้ดในตารางของหน้าจอข้อมูลสินค้า)

## 11. ยืนยันจาก V.1: แก้ข้อมูลสินค้าเพิ่มเติม (ตั้งจุดสั่งซื้อ, 2026-10-27 15:06–15:07)
หน้าจอ: แท็บ "ข้อมูลสินค้าเพิ่มเติม" (จากภาพหน้าจอ — capture ไม่มีแถว `logs` เปิดเมนู จึงยืนยันชื่อเมนูไม่ได้) · ช่อง "จุดสั่งซื้อ" = `ic_inventory_detail.purchase_point`
- ก่อนเปิด: `insert into ic_inventory_detail (ic_code) select code from ic_inventory where item_type<>5 and not exists (…)` — สร้างแถว detail ที่ขาด
- บันทึก 1 สินค้า (ไม่เห็น BEGIN แยก): `update ic_inventory` (กลุ่ม/ยี่ห้อ/รุ่น… และ `remark`) → `update ic_inventory_detail` **6 ชุด** (dimension_1–20, คลังเริ่มต้นซื้อ/ขาย/จ่าย, กลุ่มผู้ใช้, `purchase_point, discount, minimum_qty, maximum_qty, have_point, balance_control, accrued_control, lock_cost, is_end, lock_price, lock_discount, is_hold_purchase, is_hold_sale, is_premium`) → `update ic_inventory set last_update_date_time=now()` → **ลบตารางลูก 11 ตาราง** (`ic_name_billing, ic_name_merket, ic_color_use, ic_size_use, ic_name_short, ic_name_pos, ic_pattern_use, ic_inventory_replacement, ic_inventory_bundle, ic_inventory_suggest, ic_manufacturer_list`) แล้วใส่ใหม่เฉพาะที่มีบนจอ → `master_logs` (`module_name='inventory'`, `function_code=2`) → ซ่อม serial
- **เขียนทุกช่องของหน้าจอทับ** (ค่าที่ไม่ได้แสดง = null) — รูปแบบเดียวกับบาร์โค้ด (§6.1) และลูกค้า ⇒ sml_mcp_ai ห้ามใช้วิธีนี้ถ้าจะแก้ช่องเดียว: ให้ `update ic_inventory_detail set purchase_point=? where ic_code=?` อย่างเดียว (ตัดสินใน ADR)
