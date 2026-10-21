---
tags: [sml, sml_mcp_ai, write-spec, master-data, product, unit, barcode]
status: from-code + ข้อมูลจริงหลายร้าน (ยังไม่มี capture SQL ของการบันทึกสินค้า)
source: smlerp SMLERPIC/_icMain.cs (`_saveData`, `_dataList__deleteData`), SMLERPIC/_icBarcode.cs, SMLERPControl/_icmainScreenTopControl.cs, SMLERPGlobal/_utils.cs (`_updateInventoryMasterFunction`), MyLib/_myScreen.cs, SMLERPTemplate/smldatabase.xml + DB aoy/kbgtest/samai/wawacrm (2026-10-21, นับ/โครงสร้างเท่านั้น)
---
# สเปกข้อมูลหลัก: สินค้า / หน่วยนับ / บาร์โค้ด

กลับไป [[00-Index]] · ราคา [[pricing-vat-gl]] · สต็อก/ต้นทุน [[stock-cost]] · เมนู [[module-inventory]]

> หน้าจอ: ข้อมูลสินค้า › ข้อมูลสินค้า (`menu_ic_item_detail`, `SMLERPIC._icMain`), กำหนดบาร์โค้ดสินค้า (`menu_ic_item_barcode`, `SMLERPIC._icBarcode`), กำหนดหน่วยนับสินค้า (`menu_setup_ic_unit`, `MyLib._manageMasterCodeFull` → ตาราง `ic_unit`)
> ⚠️ **ยังไม่มี SQL จริงของการบันทึกสินค้า** (การทดสอบรอบ 1–3 ไม่ได้สร้าง/แก้สินค้า) — ลำดับคำสั่งด้านล่างมาจากโค้ด และกฎความสัมพันธ์ตรวจกับข้อมูลที่โปรแกรมบันทึกไว้แล้ว

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
1. `insert into master_logs (…)` (`_createLog`, `_icMain.cs` ~134) — ⚠️ โค้ดใส่คอลัมน์ `module_name` แต่ตารางจริงใน aoy **ไม่มีคอลัมน์นี้** (ยังไม่ทราบว่าคำสั่งนี้ล้มเงียบ ๆ หรือ web service ปรับโครงสร้างให้ — ต้องดูจาก capture)
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
- `master_logs.module_name` ที่โค้ดใส่แต่ไม่มีในตาราง
