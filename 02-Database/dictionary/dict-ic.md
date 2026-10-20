---
tags: [sml, dictionary, ic, generated]
module: IC
---
# พจนานุกรม: IC — สินค้า

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ic_color_use]] | สีสินค้าที่ใช้ / Item Color Use | 6 |
| [[#ic_description]] | รายละเอียดสินค้า / IC Description | 2 |
| [[#ic_discount_group]] | กลุ่มส่วนลด / IC Discount Group | 8 |
| [[#ic_inventory]] | สินค้า / Inventory | 125 |
| [[#ic_inventory_append]] | สินค้าพ่วง / Inventory Append | 5 |
| [[#ic_inventory_append_detail]] | รายละเอียดสินค้าพ่วง / Inventory Append Detail | 6 |
| [[#ic_inventory_barcode]] | บาร์โค้ดสินค้า / Inventory Item Barcode | 30 |
| [[#ic_inventory_barcode_condition]] | ic_inventory_barcode_condition / ic_inventory_barcode_condition | 9 |
| [[#ic_inventory_barcode_price]] | กำหนดส่วนลดหรือโปรโมชั่นตามบาร์โค๊ด / Table 268 | 22 |
| [[#ic_inventory_bundle]] | สินค้าพ่วง / Table 340 | 8 |
| [[#ic_inventory_detail]] | รายละเอียดสินค้า / Inventory Detail | 107 |
| [[#ic_inventory_discount]] | กำหนดส่วนลดสินค้า / Inventory Discount | 40 |
| [[#ic_inventory_level]] | ลำดับการค้นหาสินค้า / Table 272 | 11 |
| [[#ic_inventory_lot]] | Lot สินค้า / Inventory Lot | 5 |
| [[#ic_inventory_permission]] | กำหนดสิทธิ์สินค้า / Inventory Permission | 13 |
| [[#ic_inventory_price]] | กำหนดราคาสินค้า / Inventory Price | 42 |
| [[#ic_inventory_price_formula]] | สูตรราคา / formula | 25 |
| [[#ic_inventory_purchase_price]] | กำหนดราคาซื้อสินค้า / Inventory Purchase Price | 31 |
| [[#ic_inventory_remark]] | หมายเหตุสินค้า / หมายเหตุสินค้า | 2 |
| [[#ic_inventory_replace]] | สินค้าทดแทน / Inventory Replace | 5 |
| [[#ic_inventory_replace_detail]] | รายละเอียดสินค้าทดแทน / Inventory Replace Detail | 6 |
| [[#ic_inventory_replacement]] | สินค้าใช้ทดแทน / Inventory Replacement | 6 |
| [[#ic_inventory_set]] | สินค้าชุด / Inventory Set | 5 |
| [[#ic_inventory_set_detail]] | รายละเอียดสินค้าชุด / Item Set Detail | 22 |
| [[#ic_inventory_suggest]] | รายการสินค้าแนะนำ / IC Inventory Suggest | 5 |
| [[#ic_inventory_wh]] | สินค้าตามคลัง / Inventory Warehouse | 5 |
| [[#ic_manufacturer_list]] | ผู้ผลิตสินค้า / ic_manufacturer_list | 5 |
| [[#ic_name_billing]] | ชื่อสินค้าสำหรับออกบิล / Item Name Billing | 5 |
| [[#ic_name_merket]] | ชื่อสินค้าในตลาด / Item Name Merket | 5 |
| [[#ic_name_pos]] | ชื่อสินค้าสำหรับขายหน้าร้าน / Item Name POS | 5 |
| [[#ic_name_short]] | ชื่อสินค้าอย่างย่อ / Item Name Short | 5 |
| [[#ic_opposite_unit]] | หน่วยนับขนาน / Opposite Unit | 6 |
| [[#ic_pattern_use]] | ชื่อรูปแบบสินค้า / Item Pattern | 5 |
| [[#ic_price_adjust_detail]] | รายละเอียดการปรับราคา / IC Price Adjust Detail | 58 |
| [[#ic_price_formula_template]] | รูปแบบสูตร / Table 290 | 10 |
| [[#ic_production_formula]] | สูตรการผลิต / Ic Production Formula | 6 |
| [[#ic_production_formula_material]] | ส่วนประกอบ / Table 420 | 6 |
| [[#ic_production_formula_product]] | ผลิตภัณฑ์หลัก / Ic Production Formula Product | 6 |
| [[#ic_purchase_permium]] | ของแถมซื้อ / Purchase Permium | 6 |
| [[#ic_purchase_permium_condition]] | เงื่อนไขของแถมซื้อตามสินค้า / Table 212 | 8 |
| [[#ic_purchase_permium_list]] | รายการที่แถม / Table 213 | 6 |
| [[#ic_report_sort_item]] | การเรียงข้อมูลสินค้าในรายงาน / Report Sort Item | 3 |
| [[#ic_resource]] | รายละเอียดข้อความ / Inventory Resource | 225 |
| [[#ic_serial]] | serial number / Serial Number | 16 |
| [[#ic_size_use]] | ขนาดสินค้าที่ใช้ / Item Size Use | 8 |
| [[#ic_standard_cost]] | ต้นทุนมาตรฐาน / ต้นทุนมาตรฐาน | 5 |
| [[#ic_unit_use]] | หน่วยนับสินค้าที่ใช้ / Item Unit Use | 14 |
| [[#ic_warehouse_location_group]] | กลุ่มที่เก็บ / Table 386 | 4 |
| [[#ic_warehouse_location_group_detail]] | กลุ่มที่เก็บเชื่อมกับที่เก็บ / Table 387 | 5 |
| [[#ic_wh_shelf]] | คลังและพื้นที่เก็บสินค้า / Warehouse Shelf | 11 |
| [[#singha_online_unit_maping]] | กำหนดหน่วยนับsinghaonline / singha online unit maping | 5 |

## ic_color_use

**สีสินค้าที่ใช้** — Item Color Use

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ *(resource only)* | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) *(resource only)* | Name (English) | varchar(100) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

index: `ic_color_use_PK_CODE`(code,ic_code)

## ic_description

**รายละเอียดสินค้า** — IC Description

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `description` | รายละเอียดสินค้า |  | varchar(5000) | ✓ |

index: `ic_description_ic_description_PK_PRIMARY`(ic_code)

## ic_discount_group

**กลุ่มส่วนลด** — IC Discount Group

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) |  |
| `name_2` | ชื่ออังกฤษ |  | varchar(255) | ✓ |
| `date_begin` | วันที่เริ่มต้น |  | smalldatetime | ✓ |
| `date_end` | วันที่สิ้นสุด |  | smalldatetime | ✓ |
| `status` | ใช้งาน |  | smallint | ✓ |
| `guid_code` | GUID |  | varchar(50) | ✓ |
| `discount_list` | ส่วนลด |  | varchar(500) | ✓ |

## ic_inventory

**สินค้า** — Inventory · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสสินค้า | Code | varchar(25) |  |
| `code_old` | รหัสสินค้าเก่า | Code Old | varchar(25) | ✓ |
| `name_1` | ชื่อสินค้า 1 | Name 1 | varchar(255) | ✓ |
| `name_2` | ชื่อสินค้า 2 | Name 2 | varchar(255) | ✓ |
| `name_eng_1` | ชื่อ (ภาษาอังกฤษ) 1 | Name (English) 1 | varchar(255) | ✓ |
| `name_eng_2` | ชื่อ (ภาษาอังกฤษ) 2 | Name (English) 2 | varchar(255) | ✓ |
| `name_market` | ชื่อทางการตลาด | Name Market | varchar(255) | ✓ |
| `name_for_bill` | ชื่อสำหรับออกบิล | Name for Bill | varchar(255) | ✓ |
| `short_name` | ชื่อสินค้าแบบย่อ | Short Name | varchar(255) | ✓ |
| `name_for_pos` | ชื่อสำหรับขายหน้าร้าน | Name for POS | varchar(255) | ✓ |
| `name_for_search` | ชื่อสำหรับการค้นหา | Name for Search | varchar(255) | ✓ |
| `item_type` | ประเภทสินค้า | Item Type | smallint | ✓ |
| `item_category` | หมวดสินค้า | Item Category | varchar(25) | ✓ |
| `group_main` | กลุ่มสินค้าหลัก | Item Group Main | varchar(25) | ✓ |
| `item_brand` | ยี่ห้อสินค้า | Item Brand | varchar(25) | ✓ |
| `item_pattern` | รูปแบบสินค้า | Item Pattern | varchar(25) | ✓ |
| `item_design` | รูปทรงสินค้า | Item Design | varchar(25) | ✓ |
| `item_grade` | เกรดสินค้า | Item Grade | varchar(25) | ✓ |
| `item_class` | ระดับสินค้า | Item Class | varchar(25) | ✓ |
| `item_size` | ขนาดสินค้า | Item Size | varchar(25) | ✓ |
| `item_color` | สีสินค้า | Item Color | varchar(25) | ✓ |
| `item_character` | ลักษณะสินค้า | Item Character | varchar(25) | ✓ |
| `item_status` | สถานะสินค้า | Item Status | smallint | ✓ |
| `unit_type` | ประเภทหน่วยนับ | Unit Type | smallint | ✓ |
| `cost_type` | ประเภทต้นทุน | Cost Type | smallint | ✓ |
| `tax_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `item_sale_type` | สินค้าฝากขาย | Sale Type | smallint | ✓ |
| `item_rent_type` | สินค้าเช่า | Rent Type | smallint | ✓ |
| `unit_standard` | หน่วยยอดคงเหลือ | Unit Standard | varchar(25) | ✓ |
| `unit_cost` | หน่วยต้นทุน | Unit Cost | varchar(25) | ✓ |
| `income_type` | ประเภทรายได้ | Income Type | varchar(25) | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `item_model` | รุ่นสินค้า | Item Model | varchar(50) | ✓ |
| `ic_serial_no` | สินค้ามี Serial | Serial No | smallint | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `last_movement_date` | วันที่เคลื่อนไหวล่าสุด | Last Movement Date | smalldatetime | ✓ |
| `ic_normal` | สินค้าทั่วไป *(resource only)* |  | char |  |
| `ic_service` | สินค้าบริการ (ไม่ทำสต๊อก) *(resource only)* |  | char |  |
| `ic_rent` | สินค้าให้เช่า *(resource only)* |  | char |  |
| `ic_consignment` | สินค้าฝากขาย *(resource only)* |  | char |  |
| `ic_set` | สินค้าชุด  (ไม่ทำสต๊อก) *(resource only)* |  | char |  |
| `average_cost` | ต้นทุนเฉลี่ย |  | float | ✓ |
| `standard_cost` | ต้นทุนมาตรฐาน *(resource only)* |  | char |  |
| `fifo_cost` | ต้นทุน LOT FIFO *(resource only)* | Costing lot fifo | char |  |
| `single_unit` | หน่วยนับเดี่ยว *(resource only)* |  | char |  |
| `many_unit` | หลายหน่วยนับ *(resource only)* |  | char |  |
| `double_unit` | หน่วยนับขนาน *(resource only)* |  | char |  |
| `many_unit_and_double_unit` | หลายหน่วยนับ+หน่วยนับขนาน *(resource only)* |  | char |  |
| `zero_vat` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `excise_vat` | ภาษีกรมสรรพสามิต *(resource only)* |  | char |  |
| `exc_vat` | ยกเว้นภาษี *(resource only)* |  | char |  |
| `normal_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `width_length_height` | กว้างxยาวxสูง *(resource only)* |  | char |  |
| `weight` | น้ำหนัก(กก) *(resource only)* |  | char |  |
| `item_in_stock` | จำนวนสินค้า |  | float | ✓ |
| `balance_qty` | ยอดคงเหลือ |  | float | ✓ |
| `accrued_in_qty` | ยอดค้างรับ |  | float | ✓ |
| `accrued_out_qty` | ยอดค้างส่ง |  | float | ✓ |
| `ic_color` | สูตรการผลิต *(resource only)* |  | char |  |
| `ic_color_mixed` | สีผสม *(resource only)* |  | char |  |
| `unit_standard_name` | หน่วยคงเหลือ |  | varchar(100) | ✓ |
| `update_price` | แก้ไขตารางราคา |  | smallint | ✓ |
| `update_detail` | แก้ไขรายละเอียดประกอบ |  | smallint | ✓ |
| `account_code_1` | รหัสผังบัญชีสินค้า |  | varchar(25) | ✓ |
| `account_code_2` | รหัสผังบัญชีต้นทุน |  | varchar(25) | ✓ |
| `account_code_3` | รหัสผังบัญชีรายได้ |  | varchar(25) | ✓ |
| `account_code_4` | รหัสผังบัญชีรับคืน |  | varchar(25) | ✓ |
| `book_out_qty` | ยอดค้างจอง |  | float | ✓ |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `unit_standard_stand_value` | อัตราส่วนยอดคงเหลือตัวตั้ง |  | float | ✓ |
| `unit_standard_divide_value` | อัตราส่วนยอดคงเหลือตัวหาร |  | float | ✓ |
| `sign_code` | เครื่องหมาย |  | varchar(25) | ✓ |
| `supplier_code` | ผู้จัดจำหน่ายหลัก |  | varchar(25) | ✓ |
| `have_point` | สะสมแต้ม *(resource only)* |  | char |  |
| `fixed_cost` | ต้นทุนคงที่ |  | float | ✓ |
| `drink_type` | ประเภทเครื่องดื่ม |  | smallint | ✓ |
| `average_cost_1` | ต้นทุนเฉลี่ยแฝงบริหาร |  | float | ✓ |
| `have_replacement` | มีสินค้าทดแทน *(resource only)* |  | char |  |
| `group_sub` | กลุ่มสินค้าย่อย | Item Group Sub | varchar(25) | ✓ |
| `use_expire` | ใช้ระบบหมดอายุ |  | smallint | ✓ |
| `expire_cost` | ต้นทุน FEFO (วันหมดอายุ) *(resource only)* | Costing fifo  ( expiration date) | char |  |
| `assign_cost` | ต้นทุน LOT กำหนดเอง *(resource only)* |  | char |  |
| `barcode_checker_print` | พิมพ์บาร์โค๊ดตรวจสอบ | Print document list separator | smallint | ✓ |
| `print_order_per_unit` | พิมพ์ใบจัดรายการแบบแยก | Print barcode checklist | smallint | ✓ |
| `production_period` | ระยะเวลาในการผลิต(นาที) | The duration of the production (minute) | smallint | ✓ |
| `is_new_item` | เป็นสินค้าใหม่ |  | smallint | ✓ |
| `commission_rate` | อัตราค่าคอมมิสชั่น | commissions | varchar(50) | ✓ |
| `is_eordershow` | แสดงในระบบ e-Order | Show in system e-order | smallint | ✓ |
| `no_discount` | สินค้าไม่ลดราคา |  | smallint | ✓ |
| `serial_no_format` | รูปแบบ Serial | Serial Number Format | varchar(255) | ✓ |
| `pos_no_sum` | ไม่รวมรายการในระบบ POS |  | smallint | ✓ |
| `item_promote` | เป็นสินค้าแนะนำ |  | smallint | ✓ |
| `sum_sale_1` | ยอดขายตามจำนวน |  | float | ✓ |
| `is_speech` | พูดรายการอาหาร |  | smallint | ✓ |
| `other_cost_1` | ต้นทุนแบบพิเศษ 1 *(resource only)* |  | smallint |  |
| `medicine_register_number` | เลขทะเบียนยา |  | varchar(50) | ✓ |
| `medicine_standard_code` | เลขทะเบียนยา 24 |  | varchar(50) | ✓ |
| `quantity` | ปริมาณ |  | varchar(50) | ✓ |
| `degree` | ดีกรี |  | varchar(50) | ✓ |
| `is_product_boonrawd` | สินค้าบุญรอด |  | smallint | ✓ |
| `is_premium` | สินค้าพรีเมี่ยม *(resource only)* |  | char |  |
| `tpu_code` | TPU |  | varchar(20) | ✓ |
| `gpu_code` | GPU |  | varchar(20) | ✓ |
| `group_sub2` | กลุ่มสินค้าย่อย2 | Item Group Sub | varchar(25) | ✓ |
| `ic_discount_group` | กลุ่มส่วนลด |  | varchar(25) | ✓ |
| `name_from_remark` | แสดงชื่อสินค้าจากหมายเหตุ |  | smallint | ✓ |
| `manufacturer_code` | ผู้ผลิต |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้าง | Create date time | datetime | ✓ |
| `last_update_date_time` | วันที่แก้ไขล่าสุด | Last update date time | datetime | ✓ |
| `create_code` | ผู้สร้าง | Create code | varchar(25) | ✓ |
| `last_update_code` | ผู้แก้ไขล่าสุด | Last update code | varchar(25) | ✓ |
| `have_take_away` | เลือภาชนะ ทานที่ร้าน/กลับบ้าน |  | smallint | ✓ |
| `topping_product` | เป็นสินค้า Topping | Product Topping | smallint | ✓ |
| `product_age` | อายุสินค้า/วัน | Product Age | smallint | ✓ |
| `qty_per_pallet` | จำนวนต่อพาเลท | QTY Per Pallet | smallint | ✓ |
| `qc_product` | เป็นสินค้าควบคุมคุณภาพ |  | smallint | ✓ |
| `qc_product_retest_day` | Retest Day | Retest Day | smallint | ✓ |
| `require_purchase_from_approve_vendor` | เป็นสินค้าที่ต้องซื้อจากผู้อนุมัติเท่านั้น |  | smallint | ✓ |
| `normal_vendor_max_purchase_qty` | จำนวนสูงสุดในการสั่งซื้อกับผู้ค้าทั่วไป |  | float | ✓ |
| `qc_product_retest_month` | Retest Month | Retest Month | smallint | ✓ |
| `qc_product_retest_year` | Retest Year | Retest Year | smallint | ✓ |
| `is_pharma_serialization` | ยา Serialize | Pharma Serialization | smallint | ✓ |
| `is_alcoholic_beverage` | เครื่องดื่มแอลกอฮอล์ | Alcohol Beverage | smallint | ✓ |

index: `ic_inventory_PK_CODE`(code), `PK_inventory_name_1`(name_1), `PK_inventory_unit_standard_name`(unit_standard_name), `PK_inventory_unit_standard`(unit_standard), `PK_inventory_unit_standard_stand_value`(unit_standard_stand_value), `PK_inventory_unit_standard_devide_value`(unit_standard_divide_value), `ic_inventory_item_type`(item_type), `ic_inventory_is_serial`(ic_serial_no), `ic_inventory_supplier_code`(supplier_code), `ic_inventory_avg_cost`(average_cost), `ic_inventory_balance_qty`(balance_qty), `ic_inventory_accrued_in_qty`(accrued_in_qty), `ic_inventory_accrued_out_qty`(accrued_out_qty), `ic_inventory_book_out_qty`(book_out_qty)

## ic_inventory_append

**สินค้าพ่วง** — Inventory Append

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_append_code` | รหัสสินค้า | Item Append Code | varchar(25) |  |
| `ic_append_name` | ชื่อสินค้า | Item Append Name | varchar(100) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ic_inventory_append_ic_append_code_idx`(ic_append_code)

## ic_inventory_append_detail

**รายละเอียดสินค้าพ่วง** — Inventory Append Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_append_code` | สินค้าพ่วง | Item Append Code | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

index: `ic_inventory_append_detail_PK_CODE`(ic_append_code,ic_code)

## ic_inventory_barcode

**บาร์โค้ดสินค้า** — Inventory Item Barcode

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `barcode` | บาร์โค้ด | Barcode | varchar(25) |  |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `wh_code` | คลังสินค้า | Warehouse | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า | Shelf | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `price` | ราคาทั่วไป | Price 1 | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |
| `price_2` | ราคาทั่วไป | Price 2 | float | ✓ |
| `price_3` | ราคาทั่วไป | Price 3 | float | ✓ |
| `price_4` | ราคาทั่วไป | Price 4 | float | ✓ |
| `stamp_count` | จำนวนดวง *(resource only)* |  | char |  |
| `barcode_new` | บาร์โค๊ดใหม่ *(resource only)* | New Barcode | char |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* | Unit Name | char |  |
| `hidden_text` | ไม่แสดง | Hidden | smallint | ✓ |
| `price_member` | ราคาสมาชิก | Member Price | float | ✓ |
| `price_member_2` | ราคาสมาชิก | Member Price 2 | float | ✓ |
| `price_member_3` | ราคาสมาชิก | Member Price 3 | float | ✓ |
| `price_member_4` | ราคาสมาชิก | Member Price 4 | float | ✓ |
| `price_group_1` | ราคากลุ่มที่ 1 *(resource only)* |  | char |  |
| `price_group_2` | ราคากลุ่มที่ 2 *(resource only)* |  | char |  |
| `price_group_3` | ราคากลุ่มที่ 3 *(resource only)* |  | char |  |
| `price_group_4` | ราคากลุ่มที่ 4 *(resource only)* |  | char |  |
| `price_formula_price_0` | ราคากลาง *(resource only)* |  | char |  |
| `no_point` | ไม่สะสมแต้ม |  | smallint | ✓ |
| `is_clearance` | barcode ลดราคา |  | smallint | ✓ |
| `from_date` | จากวันที่ |  | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ |  | smalldatetime | ✓ |

index: `ic_inventory_barcode_PK_CODE`(barcode), `ic_inventory_barcode_barcode`(barcode), `ic_inventory_barcode_ic_code`(ic_code), `ic_inventory_barcode_description`(description), `ic_inventory_barcode_code_unit`(ic_code,unit_code)

## ic_inventory_barcode_condition

**ic_inventory_barcode_condition** — ic_inventory_barcode_condition

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `condition_1` | ตัวเลือก 1 |  | varchar(255) | ✓ |
| `condition_2` | ตัวเลือก 2 |  | varchar(255) | ✓ |
| `condition_3` | ตัวเลือก 3 |  | varchar(255) | ✓ |
| `condition_4` | ตัวเลือก 4 |  | varchar(255) | ✓ |
| `condition_5` | ตัวเลือก 5 |  | varchar(255) | ✓ |
| `condition_6` | ตัวเลือก 6 |  | varchar(255) | ✓ |

index: `ic_inventory_barcode_condition_pk`(barcode), `ic_code`(ic_code)

## ic_inventory_barcode_price

**กำหนดส่วนลดหรือโปรโมชั่นตามบาร์โค๊ด** — Table 268

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `barcode` | Barcode |  | varchar(25) |  |
| `discount_type` | ประเภทส่วนลด |  | int | ✓ |
| `discount_word` | ส่วนลด |  | varchar(25) | ✓ |
| `qty_begin` | จากจำนวน |  | int | ✓ |
| `qty_end` | ถึงจำนวน |  | int | ✓ |
| `date_begin` | จากวันที่ |  | smalldatetime | ✓ |
| `date_end` | ถึงวันที่ |  | smalldatetime | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `priority` | ความสำคัญ |  | smallint | ✓ |
| `guid_code` | guid |  | varchar(35) | ✓ |
| `qty_condition` | เงื่อนไขจำนวน *(resource only)* |  | char |  |
| `date_condition` | เงื่อนไขวันที่ *(resource only)* |  | char |  |
| `price_name_1` | ลดพิเศษทั่วไป *(resource only)* |  | char |  |
| `price_name_2` | ลดพิเศษสมาชิก *(resource only)* |  | char |  |
| `price_name_3` | ลดโปรโมชั่น *(resource only)* |  | char |  |
| `price_name_4` | ลดสมาชิก *(resource only)* |  | char |  |
| `price_name_5` | ลดพนักงาน *(resource only)* |  | char |  |
| `lock_discount` | แบบเฉพาะ |  | smallint | ✓ |
| `lock_discount_1` | ทุกเครื่องในระบบ *(resource only)* |  | char |  |
| `lock_discount_2` | เฉพาะรหัสเครื่อง POS *(resource only)* |  | char |  |
| `lock_code_list` | รหัสเครื่อง POS |  | varchar(1000) | ✓ |
| `lock_day` | เฉพาะวัน |  | varchar(1000) | ✓ |

index: `idx_barcode`(barcode), `idx_barcode_priority`(priority)

## ic_inventory_bundle

**สินค้าพ่วง** — Table 340

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `line_number` | บรรทัด |  | smallint | ✓ |
| `ic_code_bundle` | รหัสสินค้าพ่วง |  | varchar(25) |  |
| `ic_name_bundle` | ชื่อสินค้าพ่วง *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวน |  | float | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | varchar |  |
| `barcode` | บาร์โค๊ด |  | varchar(25) | ✓ |

## ic_inventory_detail

**รายละเอียดสินค้า** — Inventory Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `formular` | รหัสสูตรการผลิต | Porduce Formular | varchar(25) | ✓ |
| `po_over` | รับเกินที่สั่งซื้อได้ | PO Over | int | ✓ |
| `so_over` | เบิกเกินสั่งขายได้ | SO Over | int | ✓ |
| `account_group` | รหัสกลุ่มบัญชี | Account Group Code | varchar(25) | ✓ |
| `serial_number` | serial number | Serial Number | varchar(25) | ✓ |
| `tax_import` | % ภาษีนำเข้า | Tax Import | varchar(100) | ✓ |
| `tax_rate` | พิกัดศุลกากร | Tax Rate | float | ✓ |
| `purchase_manager` | ผู้รับผิดชอบการซื้อ | Purchase Manager | varchar(25) | ✓ |
| `sale_manager` | ผู้รับผิดชอบการขาย | Sale Manager | varchar(25) | ✓ |
| `start_purchase_wh` | คลังเริ่มต้นซื้อ | Start Purchase Warehouse | varchar(25) | ✓ |
| `start_purchase_shelf` | ที่เก็บเริ่มต้นซื้อ | Start Purchase Shelf | varchar(25) | ✓ |
| `start_purchase_unit` | หน่วยเริ่มต้นซื้อ | Start Purchase Unit | varchar(25) | ✓ |
| `start_sale_wh` | คลังเริ่มต้นขาย | Start Sale Warehouse | varchar(25) | ✓ |
| `start_sale_shelf` | ที่เก็บเริ่มต้นขาย | Start Sale Shelf | varchar(25) | ✓ |
| `start_sale_unit` | หน่วยเริ่มต้นขาย | Start Sale Unit | varchar(25) | ✓ |
| `cost_produce` | ต้นทุนการผลิต | Cost Produce | float | ✓ |
| `cost_standard` | ต้นทุนมาตรฐาน | Cost Standard | float | ✓ |
| `unit_for_stock` | หน่วยนับสต็อก | Unit for Stock | varchar(25) | ✓ |
| `ic_out_wh` | คลังสินค้าชำรุด | Item Out Warehouse | varchar(25) | ✓ |
| `ic_out_shelf` | ที่เก็บสินค้าชำรุด | Item Out Shelf | varchar(25) | ✓ |
| `ic_reserve_wh` | คลังสินค้าจอง | Item Reserve Warehouse | varchar(25) | ✓ |
| `reserve_status` | สถานะการจอง | Reserve Status | smallint | ✓ |
| `discount` | ส่วนลดต่อรายการ | Discount | varchar(50) | ✓ |
| `purchase_point` | จุดสั่งซื้อ | Purchase Point | float | ✓ |
| `unit_2_code` | หน่วยนับที่ 2 | Unit(2) Code | varchar(25) | ✓ |
| `unit_2_qty` | ปริมาณหน่วยนับ 2 | Unit(2) Qty | int | ✓ |
| `unit_2_average` | เฉลี่ยค่าระหว่างหน่วยนับ | Unit(2) Average | smallint | ✓ |
| `unit_2_average_value` | ค่าเฉลี่ยระหว่างหน่วยนับ | Unit(2) Average Value | float | ✓ |
| `user_group_for_purchase` | กลุ่มผู้รับผิดชอบการซื้อ | User Group for Purchase | varchar(25) | ✓ |
| `user_group_for_sale` | กลุ่มผู้รับผิดชอบการขาย | User Group for Sale | varchar(25) | ✓ |
| `user_group_for_manage` | กลุ่มผู้รับผิดชอบการจัดการ | User Group for Manage | varchar(25) | ✓ |
| `user_group_for_warehouse` | กลุ่มผู้รับผิดชอบคลังสินค้า | User Group for Warehouse | varchar(25) | ✓ |
| `user_status` | สถานะผู้มีสิทธิใช้งาน | User Status | smallint | ✓ |
| `close_reason` | เหตุผลในการปิด | Close Reasonable | varchar(255) | ✓ |
| `close_date` | วันที่ปิด | Close Date | smalldatetime | ✓ |
| `ref_file_1` | ไฟล์อ้างอิง 1 | Reference File 1 | varchar(255) | ✓ |
| `ref_file_2` | ไฟล์อ้างอิง 2 | Reference File 2 | varchar(255) | ✓ |
| `ref_file_3` | ไฟล์อ้างอิง 3 | Reference File 3 | varchar(255) | ✓ |
| `ref_file_4` | ไฟล์อ้างอิง 4 | Reference File 4 | varchar(255) | ✓ |
| `ref_file_5` | ไฟล์อ้างอิง 5 | Reference File 5 | varchar(255) | ✓ |
| `dimension_1` | มิติ 1 | Dimension 1 | varchar(25) | ✓ |
| `dimension_2` | มิติ 2 | Dimension 2 | varchar(25) | ✓ |
| `dimension_3` | มิติ 3 | Dimension 3 | varchar(25) | ✓ |
| `dimension_4` | มิติ 4 | Dimension 4 | varchar(25) | ✓ |
| `dimension_5` | มิติ 5 | Dimension 5 | varchar(25) | ✓ |
| `dimension_6` | มิติ 6 | Dimension 6 | varchar(25) | ✓ |
| `dimension_7` | มิติ 7 | Dimension 7 | varchar(25) | ✓ |
| `dimension_8` | มิติ 8 | Dimension 8 | varchar(25) | ✓ |
| `dimension_9` | มิติ 9 | Dimension 9 | varchar(25) | ✓ |
| `dimension_10` | มิติ 10 | Dimension 10 | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `sale_price_1` | ราคาขาย 1 | Sale Price 1 | float | ✓ |
| `sale_price_2` | ราคาขาย 2 | Sale Price 2 | float | ✓ |
| `sale_price_3` | ราคาขาย 3 | Sale Price 3 | float | ✓ |
| `sale_price_4` | ราคาขาย 4 | Sale Price 4 | float | ✓ |
| `maximum_qty` | จุดสูงสุด | Maximum | float | ✓ |
| `minimum_qty` | จุดต่ำสุด | Minimum | float | ✓ |
| `dimension_11` | มิติ 11 | Dimension 11 | varchar(25) | ✓ |
| `dimension_12` | มิติ 12 | Dimension 12 | varchar(25) | ✓ |
| `dimension_13` | มิติ 13 | Dimension 13 | varchar(25) | ✓ |
| `dimension_14` | มิติ 14 | Dimension 14 | varchar(25) | ✓ |
| `dimension_15` | มิติ 15 | Dimension 15 | varchar(25) | ✓ |
| `dimension_16` | มิติ 16 | Dimension 16 | varchar(25) | ✓ |
| `dimension_17` | มิติ 17 | Dimension 17 | varchar(25) | ✓ |
| `dimension_18` | มิติ 18 | Dimension 18 | varchar(25) | ✓ |
| `dimension_19` | มิติ 19 | Dimension 19 | varchar(25) | ✓ |
| `dimension_20` | มิติ 20 | Dimension 20 | varchar(25) | ✓ |
| `accrued_control` | อนุญาติให้ขายสินค้าค้างส่ง |  | smallint | ✓ |
| `lock_price` | ห้ามแก้ราคาขาย |  | smallint | ✓ |
| `lock_discount` | ห้ามแก้ส่วนลดขาย |  | smallint | ✓ |
| `lock_cost` | ห้ามขายต่ำกว่าต้นทุน |  | smallint | ✓ |
| `is_end` | สินค้าเลิกผลิตแล้ว |  | smallint | ✓ |
| `is_hold_purchase` | สินค้าหยุดซื้อ |  | smallint | ✓ |
| `is_hold_sale` | สินค้าหยุดขาย |  | smallint | ✓ |
| `is_stop` | ห้ามใช้ |  | smallint | ✓ |
| `balance_control` | อนุญาติให้ยอดคงเหลือติดลบ |  | smallint | ✓ |
| `have_point` | เข้าสะสมแต้ม |  | smallint | ✓ |
| `start_unit_code` | หน่วยเริ่มต้นสินค้า |  | varchar(25) | ✓ |
| `dimension_21` | มิติ 21 |  | varchar(255) | ✓ |
| `dimension_22` | มิติ 22 |  | varchar(255) | ✓ |
| `dimension_23` | มิติ 23 |  | varchar(255) | ✓ |
| `dimension_24` | มิติ 24 |  | varchar(255) | ✓ |
| `dimension_25` | มิติ 25 |  | varchar(255) | ✓ |
| `is_premium` | สินค้าสมนาคุณ |  | smallint | ✓ |
| `dimension_26` | มิติ 26 |  | varchar(255) | ✓ |
| `dimension_27` | มิติ 27 |  | varchar(255) | ✓ |
| `dimension_28` | มิติ 28 |  | varchar(255) | ✓ |
| `dimension_29` | มิติ 29 |  | varchar(255) | ✓ |
| `dimension_30` | มิติ 30 |  | varchar(255) | ✓ |
| `dimension_31` | มิติ 31 |  | varchar(255) | ✓ |
| `dimension_32` | มิติ 32 |  | varchar(255) | ✓ |
| `dimension_33` | มิติ 33 |  | varchar(255) | ✓ |
| `dimension_34` | มิติ 34 |  | varchar(255) | ✓ |
| `dimension_35` | มิติ 35 |  | varchar(255) | ✓ |
| `dimension_36` | มิติ 36 |  | varchar(255) | ✓ |
| `dimension_37` | มิติ 37 |  | varchar(255) | ✓ |
| `dimension_38` | มิติ 38 |  | varchar(255) | ✓ |
| `dimension_39` | มิติ 39 |  | varchar(255) | ✓ |
| `dimension_40` | มิติ 40 |  | varchar(255) | ✓ |
| `dimension_41` | มิติ 41 |  | varchar(255) | ✓ |
| `dimension_42` | มิติ 42 |  | varchar(255) | ✓ |
| `dimension_43` | มิติ 43 |  | varchar(255) | ✓ |
| `dimension_44` | มิติ 44 |  | varchar(255) | ✓ |
| `dimension_45` | มิติ 45 |  | varchar(255) | ✓ |
| `before_sale_unit` | หน่วยช่วยขาย |  | varchar(25) | ✓ |
| `image_count` | จำนวนรูปภาพ |  | smallint | ✓ |

index: `ic_inventory_detail_PK_CODE`(ic_code)

## ic_inventory_discount

**กำหนดส่วนลดสินค้า** — Inventory Discount

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Product | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `from_qty` | จากจำนวน | From Qty | float | ✓ |
| `to_qty` | ถึงจำนวน | To Qty | float | ✓ |
| `from_date` | จากวันที่ | From Date | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ | To Date | smalldatetime | ✓ |
| `sale_type` | ประเภทการขาย | Sale Type | smallint | ✓ |
| `transport_type` | เงื่อนไขการส่ง | Transport Type | smallint | ✓ |
| `discount` | ส่วนลด | Discount | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `sell_cashier` | ขายเงินสด *(resource only)* | Sell Cashier | char |  |
| `sell_on_credit` | ขายเงินเชื่อ *(resource only)* | Sell no Credit | char |  |
| `sell_wholesale` | ขายส่ง *(resource only)* | Sell Whoesale | char |  |
| `sell_by_retail` | ขายปลีก *(resource only)* | Sell By Retail | char |  |
| `sell_for_a_lump_sum` | ขายขาด *(resource only)* | Sell For a Lump Sum | char |  |
| `sell_on_the_installment_plan` | ขายเงินผ่อน *(resource only)* | Sell on the Installment Plan | char |  |
| `to_be_responsible` | รับเอง *(resource only)* | To be Responsoble | char |  |
| `to_support` | ส่งให้ *(resource only)* | To Support | char |  |
| `tab_normal_price` | ราคาขายทั่วไป *(resource only)* | Tab Nomal | char |  |
| `tab_retail_price` | ราคาขายปลีก *(resource only)* | Tab Sell by Retial | char |  |
| `tab_cust_price` | ราคาขายตามลูกค้า *(resource only)* | Tab Sell by Customer | char |  |
| `tab_cust_group_price` | ราคาขายตามกลุ่มลูกค้า *(resource only)* | Tab Sell by Customer | char |  |
| `discount_type` | ประเภทราคา (0=ลดทั่วไป,1=ตามกลุ่มลูกค้า,2=ตามลูกค้า) | Discount Type | int | ✓ |
| `qty_condition` | เงื่อนไขตามจำนวน *(resource only)* | Qty Condition | char |  |
| `date_condition` | เงื่อนไขตามวันที่ *(resource only)* | Date Condition | char |  |
| `other_condition` | เงื่อนไขอื่นๆ *(resource only)* | Other Condition | char |  |
| `cust_code` | รหัสลูกค้า | Cust Code | varchar(25) | ✓ |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* | Unit Name | char |  |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `cust_group_1` | กลุ่มลูกค้าหลัก |  | varchar(25) | ✓ |
| `cust_group_2` | กลุ่มลูกค้าย่อย |  | varchar(25) | ✓ |
| `group_name_1` | ชื่อกลุ่มลูกค้าหลัก *(resource only)* |  | char |  |
| `group_name_2` | ชื่อกลุ่มลูกค้าย่อย *(resource only)* |  | char |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `discount_mode` | ประเภท (0=ราคาขายหลัก,1=ราคาขายทั่วไป) |  | smallint | ✓ |
| `tab_standard_price` | ราคามาตรฐาน *(resource only)* |  | char |  |
| `olddate` | olddate | olddate | varchar(55) | ✓ |
| `line_number` | หมายเลขบรรทัด | Line Number | int | ✓ |
| `price_currency` | ราคาสกุลเงิน |  | smallint | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |

index: `ic_inventory_discount_ic_code`(ic_code), `ic_inventory_discount_ic_code_unit_code`(ic_code,unit_code)

## ic_inventory_level

**ลำดับการค้นหาสินค้า** — Table 272

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `level_1` | ชั้นที่ 1 |  | varchar(50) | ✓ |
| `level_2` | ชั้นที่ 2 |  | varchar(50) | ✓ |
| `level_3` | ชั้นที่ 3 |  | varchar(50) | ✓ |
| `level_4` | ชั้นที่ 4 |  | varchar(50) | ✓ |
| `price` | ราคา |  | float | ✓ |
| `suggest_remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `option` | Option |  | varchar(255) | ✓ |
| `sort_order` | การเรียงลำดับ |  | float | ✓ |

index: `ic_inventory_level_ic_inventory_level_pk`(ic_code,unit_code,barcode), `ic_inventory_level_barcode`(barcode)

## ic_inventory_lot

**Lot สินค้า** — Inventory Lot

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code` |  |  | varchar(50) |  |
| `lot_number` |  |  | varchar(255) |  |
| `mfd_date` |  |  | smalldatetime | ✓ |
| `exp_date` |  |  | smalldatetime | ✓ |
| `mfn_name` |  |  | varchar(255) | ✓ |

## ic_inventory_permission

**กำหนดสิทธิ์สินค้า** — Inventory Permission

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `ib` | ยกมา |  | smallint | ✓ |
| `if` | รับสำเร็จรูป |  | smallint | ✓ |
| `rim` | โอน |  | smallint | ✓ |
| `wsdw` | เบิก |  | smallint | ✓ |
| `wsdd` | สินค้าฝาก |  | smallint | ✓ |
| `io` | เบิกสินค้า |  | smallint | ✓ |
| `pu` | ซื้อสินค้า |  | smallint | ✓ |
| `pa` | เพิ่มหนี้ |  | smallint | ✓ |
| `pi` | รับสินค้า |  | smallint | ✓ |
| `ir` | รับคืนจากการเบิก |  | smallint | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `st` | ลดหนี้ |  | smallint | ✓ |

## ic_inventory_price

**กำหนดราคาสินค้า** — Inventory Price

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Product | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `from_qty` | จากจำนวน | From Qty | float | ✓ |
| `to_qty` | ถึงจำนวน | To Qty | float | ✓ |
| `from_date` | จากวันที่ | From Date | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ | To Date | smalldatetime | ✓ |
| `sale_type` | ประเภทการขาย | Sale Type | smallint | ✓ |
| `transport_type` | เงื่อนไขการส่ง | Transport Type | smallint | ✓ |
| `sale_price1` | ราคาแยกภาษี | Sale Price | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `sell_cashier` | ขายเงินสด *(resource only)* | Sell Cashier | char |  |
| `sell_on_credit` | ขายเงินเชื่อ *(resource only)* | Sell no Credit | char |  |
| `sell_wholesale` | ขายส่ง *(resource only)* | Sell Whoesale | char |  |
| `sell_by_retail` | ขายปลีก *(resource only)* | Sell By Retail | char |  |
| `sell_for_a_lump_sum` | ขายขาด *(resource only)* | Sell For a Lump Sum | char |  |
| `sell_on_the_installment_plan` | ขายเงินผ่อน *(resource only)* | Sell on the Installment Plan | char |  |
| `to_be_responsible` | รับเอง *(resource only)* | To be Responsoble | char |  |
| `to_support` | ส่งให้ *(resource only)* | To Support | char |  |
| `tab_normal_price` | ราคาขายทั่วไป *(resource only)* | Tab Nomal | char |  |
| `tab_retail_price` | ราคาขายปลีก *(resource only)* | Tab Sell by Retial | char |  |
| `tab_cust_price` | ราคาขายตามลูกค้า *(resource only)* | Tab Sell by Customer | char |  |
| `tab_cust_group_price` | ราคาขายตามกลุ่มลูกค้า *(resource only)* | Tab Sell by Customer | char |  |
| `price_type` | ประเภทราคา | Price Type | int | ✓ |
| `qty_condition` | เงื่อนไขตามจำนวน *(resource only)* | Qty Condition | char |  |
| `date_condition` | เงื่อนไขตามวันที่ *(resource only)* | Date Condition | char |  |
| `other_condition` | เงื่อนไขอื่นๆ *(resource only)* | Other Condition | char |  |
| `cust_code` | รหัสลูกค้า | Cust Code | varchar(25) | ✓ |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* | Unit Name | char |  |
| `sale_price2` | ราคารวมภาษี | Price+Vat | float | ✓ |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `cust_group_1` | กลุ่มลูกค้าหลัก |  | varchar(25) | ✓ |
| `cust_group_2` | กลุ่มลูกค้าย่อย |  | varchar(25) | ✓ |
| `group_name_1` | ชื่อกลุ่มลูกค้าหลัก *(resource only)* |  | char |  |
| `group_name_2` | ชื่อกลุ่มลูกค้าย่อย *(resource only)* |  | char |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `price_mode` | ประเภท (0=ราคาขายหลัก,1=ราคาขายทั่วไป) |  | smallint | ✓ |
| `tab_standard_price` | ราคามาตรฐาน *(resource only)* |  | char |  |
| `olddate` | olddate | olddate | varchar(55) | ✓ |
| `line_number` | หมายเลขบรรทัด | Line Number | int | ✓ |
| `price_currency` | ราคาสกุลเงิน |  | smallint | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |
| `currency_name` | ชื่อสกุลเงิน *(resource only)* |  | char |  |

index: `ic_inventory_price_ic_code`(ic_code), `ic_inventory_price_ic_code_unit_code`(ic_code,unit_code)

## ic_inventory_price_formula

**สูตรราคา** — formula

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `sale_type` | ประเภทการขาย |  | smallint |  |
| `sale_1` | ขายเงินสด *(resource only)* |  | char |  |
| `sale_2` | ขายเงินเชื่อ *(resource only)* |  | char |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | varchar |  |
| `price_0` | ราคากลาง |  | varchar(50) | ✓ |
| `price_1` | ราคา 1 |  | varchar(50) | ✓ |
| `price_2` | ราคา 2 |  | varchar(50) | ✓ |
| `price_3` | ราคา 3 |  | varchar(50) | ✓ |
| `price_4` | ราคา 4 |  | varchar(50) | ✓ |
| `price_5` | ราคา 5 |  | varchar(50) | ✓ |
| `price_6` | ราคา 6 |  | varchar(50) | ✓ |
| `price_7` | ราคา 7 |  | varchar(50) | ✓ |
| `price_8` | ราคา 8 |  | varchar(50) | ✓ |
| `price_9` | ราคา 9 |  | varchar(50) | ✓ |
| `unit_name` | หน่วยนับ *(resource only)* |  | char |  |
| `tax_type` | ประเภทภาษี |  | smallint | ✓ |
| `tax_type_none` | ไม่เลือก *(resource only)* |  | char |  |
| `tax_type_exclude` | แยกนอก *(resource only)* |  | char |  |
| `tax_type_include` | รวมใน *(resource only)* |  | char |  |
| `tax_type_zero` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `price_currency` | ราคาสกุลเงิน |  | smallint | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |
| `currency_name` | ชื่อสกุลเงิน *(resource only)* |  | char |  |

index: `ic_inventory_price_formula_pk_primary_price_formula_2`(ic_code,unit_code,sale_type,tax_type), `ic_inventory_price_formula_ic_code`(ic_code), `unique_ic_inventory_price_formul`(ic_code,unit_code,sale_type,tax_type,currency_code)

## ic_inventory_purchase_price

**กำหนดราคาซื้อสินค้า** — Inventory Purchase Price

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Product | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `from_qty` | จากจำนวน | From Qty | float | ✓ |
| `to_qty` | ถึงจำนวน | To Qty | float | ✓ |
| `from_date` | จากวันที่ | From Date | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ | To Date | smalldatetime | ✓ |
| `sale_type` | ประเภทการขาย | Sale Type | smallint | ✓ |
| `transport_type` | เงื่อนไขการส่ง | Transport Type | smallint | ✓ |
| `sale_price1` | ราคาแยกภาษี | Sale Price | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `sell_cashier` | ขายเงินสด *(resource only)* | Sell Cashier | char |  |
| `sell_on_credit` | ขายเงินเชื่อ *(resource only)* | Sell no Credit | char |  |
| `sell_wholesale` | ขายส่ง *(resource only)* | Sell Whoesale | char |  |
| `sell_by_retail` | ขายปลีก *(resource only)* | Sell By Retail | char |  |
| `sell_for_a_lump_sum` | ขายขาด *(resource only)* | Sell For a Lump Sum | char |  |
| `sell_on_the_installment_plan` | ขายเงินผ่อน *(resource only)* | Sell on the Installment Plan | char |  |
| `to_be_responsible` | รับเอง *(resource only)* | To be Responsoble | char |  |
| `to_support` | ส่งให้ *(resource only)* | To Support | char |  |
| `tab_normal_price` | ราคาซื้อทั่วไป *(resource only)* | Tab Nomal | char |  |
| `tab_retail_price` | ราคาซื้อ *(resource only)* | Tab Sell by Retial | char |  |
| `tab_ap_price` | ราคาตามเจ้าหนี้ *(resource only)* | Tab Sell by Customer | char |  |
| `price_type` | ประเภทราคา | Price Type | int | ✓ |
| `qty_condition` | เงื่อนไขตามจำนวน *(resource only)* | Qty Condition | char |  |
| `date_condition` | เงื่อนไขตามวันที่ *(resource only)* | Date Condition | char |  |
| `other_condition` | เงื่อนไขอื่นๆ *(resource only)* | Other Condition | char |  |
| `supplier_code` | รหัสเจ้าหนี้ | Ap Code | varchar(25) | ✓ |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* | Unit Name | char |  |
| `sale_price2` | ราคารวมภาษี | Price+Vat | float | ✓ |
| `supplier_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `olddate` | olddate | olddate | varchar(55) | ✓ |
| `discount` | ส่วนลด | Discount | varchar(255) | ✓ |

## ic_inventory_remark

**หมายเหตุสินค้า** — หมายเหตุสินค้า

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `remark_code` | รหัสตัวย่อ |  | varchar(25) |  |
| `remark_desc` | หมายเหตุ |  | varchar(255) |  |

index: `ic_inventory_remark_idx`(remark_code)

## ic_inventory_replace

**สินค้าทดแทน** — Inventory Replace

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_replace_code` | รหัสสินค้า | Item Replace Code | varchar(25) |  |
| `ic_replace_name` | ชื่อสินค้า | Item Replace Name | varchar(100) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

## ic_inventory_replace_detail

**รายละเอียดสินค้าทดแทน** — Inventory Replace Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_replace_code` | สินค้าทดแทน | Item Replace Code | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

index: `ic_inventory_replace_detail_PK_CODE`(ic_replace_code,ic_code)

## ic_inventory_replacement

**สินค้าใช้ทดแทน** — Inventory Replacement

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้าทดแทน | IC Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint |  |
| `ic_replace_code` | รหัสสินค้า |  | varchar(25) |  |
| `ic_name` | ชื่อสินค้าทดแทน *(resource only)* |  | char |  |
| `line_number` | บรรทัด | Line Number | int |  |

## ic_inventory_set

**สินค้าชุด** — Inventory Set

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_set_code` | รหัสสินค้าชุด | Item Set Code | varchar(25) |  |
| `ic_set_neme` | ชื่อสินค้าชุด | Item Set Name | varchar(100) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

## ic_inventory_set_detail

**รายละเอียดสินค้าชุด** — Item Set Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_set_code` | รหัสสินค้าชุด | Item Set Code | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char(100) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `qty` | จำนวน | QTY | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* | Unit Name | char |  |
| `price` | ราคา | Price | float | ✓ |
| `sum_amount` | มูลค่า | Amount | float | ✓ |
| `wh_code` | wh_code *(resource only)* |  | varchar |  |
| `wh_name` | wh_name *(resource only)* |  | varchar |  |
| `shelf_name` | shelf_name *(resource only)* |  | varchar |  |
| `shelf_code` | shelf_code *(resource only)* |  | varchar |  |
| `stand_value` | stand_value *(resource only)* |  | float |  |
| `divide_value` | divide_value *(resource only)* |  | float |  |
| `item_type` | item_type *(resource only)* |  | char |  |
| `unit_type` | unit type *(resource only)* |  | char |  |
| `ic_set_name` | ชื่อสินค้าชุด *(resource only)* |  | char |  |
| `ic_set_unit` | หน่วยสินค้าชุด *(resource only)* |  | char |  |
| `barcode` | บาร์โค๊ด | Barcode | varchar(25) | ✓ |
| `price_ratio` | อัตราส่วนราคา |  | float | ✓ |

index: `ic_inventory_set_detail_PK_CODE`(ic_set_code,line_number), `ic_inventory_set_detail_ic_code`(ic_code), `ic_inventory_set_detail_ic_set_code`(ic_set_code)

## ic_inventory_suggest

**รายการสินค้าแนะนำ** — IC Inventory Suggest

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `ic_suggest_code` | รหัสสินค้าแนะนำ |  | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `line_number` | บรรทัด |  | smallint | ✓ |
| `status` | สถานะ |  | smallint | ✓ |

## ic_inventory_wh

**สินค้าตามคลัง** — Inventory Warehouse

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `wh_code` | คลังสินค้า | WH Code | varchar(25) |  |
| `shelf_code` | ที่เก็บสินค้า | Shelf Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

## ic_manufacturer_list

**ผู้ผลิตสินค้า** — ic_manufacturer_list

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `manufacturer_code` | รหัสผู้ผลิต |  | varchar(50) |  |
| `line_number` | LineNunber |  | smallint | ✓ |
| `manufacturer_name` | ชื่อผู้ผลิต *(resource only)* |  | char |  |
| `status` | สถานะ |  | smallint | ✓ |

## ic_name_billing

**ชื่อสินค้าสำหรับออกบิล** — Item Name Billing

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (Englosh) | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

index: `ic_name_billing_code_idx`(ic_code), `ic_name_billing_name_1_idx`(name_1)

## ic_name_merket

**ชื่อสินค้าในตลาด** — Item Name Merket

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (Englosh) | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

index: `ic_name_merket_code_idx`(ic_code), `ic_name_merket_name_1_idx`(name_1)

## ic_name_pos

**ชื่อสินค้าสำหรับขายหน้าร้าน** — Item Name POS

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (Englosh) | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

index: `ic_name_pos_code_idx`(ic_code), `ic_name_pos_name_1_idx`(name_1)

## ic_name_short

**ชื่อสินค้าอย่างย่อ** — Item Name Short

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (Englosh) | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

## ic_opposite_unit

**หน่วยนับขนาน** — Opposite Unit

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `unit_code` | รหัส | Unit Code | varchar(25) |  |
| `stand_value` | ตัวตั้ง | Stand Value | float | ✓ |
| `divide_value` | ตัวหาร | Divide Value | float | ✓ |
| `status` | สถานะ | Status | smallint |  |
| `unit_name` | ชื่อ *(resource only)* | Unit Name | varchar(255) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |

## ic_pattern_use

**ชื่อรูปแบบสินค้า** — Item Pattern

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ *(resource only)* | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) *(resource only)* | Name Eng | varchar(100) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `status` | สถานะ | Status | smallint | ✓ |

## ic_price_adjust_detail

**รายละเอียดการปรับราคา** — IC Price Adjust Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `price_mode` | ประเภทราคา *(resource only)* |  | smallint |  |
| `price_exclude_vat` | ราคาแยกภาษี *(resource only)* |  | char |  |
| `price_include_vat` | ราคารวมภาษี *(resource only)* |  | char |  |
| `barcode_price_1` | ราคาทั่วไป *(resource only)* |  | char |  |
| `barcode_price_2` | ราคาทั่วไป *(resource only)* |  | char |  |
| `barcode_price_3` | ราคาทั่วไป *(resource only)* |  | char |  |
| `barcode_price_4` | ราคาทั่วไป *(resource only)* |  | char |  |
| `barcode_member_price_1` | ราคาสมาชิก *(resource only)* |  | char |  |
| `barcode_member_price_2` | ราคาสมาชิก *(resource only)* |  | char |  |
| `barcode_member_price_3` | ราคาสมาชิก *(resource only)* |  | char |  |
| `barcode_member_price_4` | ราคาสมาชิก *(resource only)* |  | char |  |
| `price_group_1` | ราคากลุ่มที่ 1 *(resource only)* |  | char |  |
| `price_group_2` | ราคากลุ่มที่ 2 *(resource only)* |  | char |  |
| `price_group_3` | ราคากลุ่มที่ 3 *(resource only)* |  | char |  |
| `price_group_4` | ราคากลุ่มที่ 4 *(resource only)* |  | char |  |
| `price_0` | ราคากลาง *(resource only)* |  | char |  |
| `price_1` | ราคา 1 *(resource only)* |  | char |  |
| `price_2` | ราคา 2 *(resource only)* |  | char |  |
| `price_3` | ราคา 3 *(resource only)* |  | char |  |
| `price_4` | ราคา 4 *(resource only)* |  | char |  |
| `price_5` | ราคา 5 *(resource only)* |  | char |  |
| `price_6` | ราคา 6 *(resource only)* |  | char |  |
| `price_7` | ราคา 7 *(resource only)* |  | char |  |
| `price_8` | ราคา 8 *(resource only)* |  | char |  |
| `price_9` | ราคา 9 *(resource only)* |  | char |  |
| `price_formula` | ราคาตามสูตร *(resource only)* |  | char |  |
| `price_standard` | ราคาทั่วไปและมาตรฐาน *(resource only)* |  | char |  |
| `from_qty` | จากจำนวน *(resource only)* |  | char |  |
| `to_qty` | ถึงจำนวน *(resource only)* |  | char |  |
| `from_date` | จากวันที่ *(resource only)* |  | char |  |
| `to_date` | ถึงวันที่ *(resource only)* |  | char |  |
| `sale_type` | ประเภทการขาย *(resource only)* |  | char |  |
| `sale_type_1` | ขายสด *(resource only)* |  | char |  |
| `sale_type_2` | ขายเชื่อ *(resource only)* |  | char |  |
| `new_price_exclude_vat` | ราคาแยกภาษี *(resource only)* |  | char |  |
| `new_price_include_vat` | ราคารวมภาษี *(resource only)* |  | char |  |
| `new_barcode_price_1` | ราคาทั่วไป *(resource only)* |  | char |  |
| `new_barcode_price_2` | ราคาทั่วไป *(resource only)* |  | char |  |
| `new_barcode_price_3` | ราคาทั่วไป *(resource only)* |  | char |  |
| `new_barcode_price_4` | ราคาทั่วไป *(resource only)* |  | char |  |
| `new_barcode_member_price_1` | ราคาสมาชิก *(resource only)* |  | char |  |
| `new_barcode_member_price_2` | ราคาสมาชิก *(resource only)* |  | char |  |
| `new_barcode_member_price_3` | ราคาสมาชิก *(resource only)* |  | char |  |
| `new_barcode_member_price_4` | ราคาสมาชิก *(resource only)* |  | char |  |
| `new_price_0` | ราคากลาง *(resource only)* |  | char |  |
| `new_price_1` | ราคา 1 *(resource only)* |  | char |  |
| `new_price_2` | ราคา 2 *(resource only)* |  | char |  |
| `new_price_3` | ราคา 3 *(resource only)* |  | char |  |
| `new_price_4` | ราคา 4 *(resource only)* |  | char |  |
| `new_price_5` | ราคา 5 *(resource only)* |  | char |  |
| `new_price_6` | ราคา 6 *(resource only)* |  | char |  |
| `new_price_7` | ราคา 7 *(resource only)* |  | char |  |
| `new_price_8` | ราคา 8 *(resource only)* |  | char |  |
| `new_price_9` | ราคา 9 *(resource only)* |  | char |  |
| `new_price` | ราคาปรับปรุงใหม่ *(resource only)* |  | char |  |

## ic_price_formula_template

**รูปแบบสูตร** — Table 290

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `price_1` | ราคา 1 |  | varchar(50) | ✓ |
| `price_2` | ราคา 2 |  | varchar(50) | ✓ |
| `price_3` | ราคา 3 |  | varchar(50) | ✓ |
| `price_4` | ราคา 4 |  | varchar(50) | ✓ |
| `price_5` | ราคา 5 |  | varchar(50) | ✓ |
| `price_6` | ราคา 6 |  | varchar(50) | ✓ |
| `price_7` | ราคา 7 |  | varchar(50) | ✓ |
| `price_8` | ราคา 8 |  | varchar(50) | ✓ |
| `price_9` | ราคา 9 |  | varchar(50) | ✓ |

index: `ic_price_formula_template_PK_ic_price_formula_template`(code)

## ic_production_formula

**สูตรการผลิต** — Ic Production Formula

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(100) | ✓ |
| `name_2` | ชื่ออังกฤษ |  | varchar(100) | ✓ |
| `date_from` | วันที่เริ่มใช้ |  | smalldatetime |  |
| `date_to` | วันที่สิ้นสุด |  | smalldatetime |  |
| `guid_code` | GUID |  | varchar(50) | ✓ |

## ic_production_formula_material

**ส่วนประกอบ** — Table 420

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `item_name` | รายละเอียด *(resource only)* |  | varchar(255) |  |
| `unit_code` | หน่วยนับ |  | varchar(100) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `line_number` | หมายเลขบรรทัด |  | int | ✓ |
| `formula_code` | รหัสสูตรการผลิต |  | varchar(25) | ✓ |

## ic_production_formula_product

**ผลิตภัณฑ์หลัก** — Ic Production Formula Product

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `item_name` | รายละเอียด *(resource only)* |  | varchar(255) |  |
| `unit_code` | หน่วยนับ |  | varchar(100) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `line_number` | หมายเลขบรรทัด |  | int | ✓ |
| `formula_code` | รหัสสูตรการผลิต |  | varchar(25) | ✓ |

## ic_purchase_permium

**ของแถมซื้อ** — Purchase Permium

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `permium_code` | รหัสเงื่อนไข |  | varchar(25) |  |
| `name_1` | ชื่อเงื่อนไข |  | varchar(100) |  |
| `date_begin` | วันที่เริ่มต้น |  | smalldatetime |  |
| `date_end` | วันที่สิ้นสุด |  | smalldatetime |  |
| `important` | ลำดับ |  | smallint |  |
| `guid_code` | GUID |  | varchar(35) | ✓ |

## ic_purchase_permium_condition

**เงื่อนไขของแถมซื้อตามสินค้า** — Table 212

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `permium_code` | รหัสเงื่อนไข |  | varchar(25) |  |
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวนตามเงื่อนไข |  | float |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* |  | char |  |
| `stand_value` | ตัวตั้ง |  | float | ✓ |
| `divide_value` | ตัวหาร |  | float | ✓ |

## ic_purchase_permium_list

**รายการที่แถม** — Table 213

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `permium_code` | รหัสเงื่อนไข |  | varchar(25) |  |
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวน |  | float |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* |  | char |  |

index: `ic_purchase_permium_list_ic_code`(ic_code), `ic_purchase_permium_list_permiun_code`(permium_code)

## ic_report_sort_item

**การเรียงข้อมูลสินค้าในรายงาน** — Report Sort Item

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `line_number` | ลำดับ | Line Number | smallint | ✓ |

index: `ic_report_sort_item_ic_report_sort_ic_code`(ic_code)

## ic_resource

**รายละเอียดข้อความ** — Inventory Resource · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `ic_normal` | สินค้าทั่วไป *(resource only)* | Item Normal | char |  |
| `ic_service` | สินค้า (สินค้าบริการ) *(resource only)* | Item Service | char |  |
| `ic_for_rent` | สินค้าเช่า *(resource only)* | Item for Rent | char |  |
| `ic_for_sale` | สินค้าฝากขาย *(resource only)* | Item for Sale | char |  |
| `ic_set` | สินค้าชุด *(resource only)* | Item Set | char |  |
| `ic_special` | สินค้าพิเศษ(สุรา-บุหรี่) *(resource only)* | Item Special | char |  |
| `ic_color` | สี *(resource only)* | Item Color | char |  |
| `ic_size` | ขนาด *(resource only)* | Item Size | char |  |
| `ic_unit_code` | หน่วยนับ *(resource only)* | Item Unit | char |  |
| `wh_branch` | คลัง-สาขา *(resource only)* | WH-Branch | char |  |
| `account` | บัญชี *(resource only)* | Account | char |  |
| `zero_vat` | ภาษีอัตราศูนย์ *(resource only)* | Zero Vat | char |  |
| `excise_vat` | ภาษีกรมสรรพสามิต *(resource only)* | Excise Vat | char |  |
| `exc_vat` | ยกเว้นภาษี *(resource only)* | Except Vat | char |  |
| `average_cost` | ต้นทุนเฉลี่ย *(resource only)* | Average Cost | char |  |
| `fifo_cost` | ต้นทุน FIFO *(resource only)* | FIFO Cost | char |  |
| `standard_cost` | ต้นทุนมาตรฐาน *(resource only)* | Standard Cost | char |  |
| `single_unit` | หน่วยนับเดียว *(resource only)* | Single Unit | char |  |
| `many_unit` | หลายหน่วยนับ *(resource only)* | Many Unit | char |  |
| `double_unit` | หน่วยนับขนาน *(resource only)* | Double Unit | char |  |
| `detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `group_dimension` | กลุ่ม-มิติ *(resource only)* | Group Dimension | char |  |
| `name_billing` | ชื่อในการเปิดบิล *(resource only)* | Name Billing | char |  |
| `name_short` | ชื่อย่อ *(resource only)* | Name Short | char |  |
| `name_pos` | ชื่อหน้าร้าน *(resource only)* | Name POS | char |  |
| `replace` | สินค้าทดแทน *(resource only)* | Replace | char |  |
| `onhand_less_zero_y` | อนุญาติให้สินค้าในมือตํ่ากว่าศูนย์ได้ *(resource only)* | On hand Less than Zero (Yes) | char |  |
| `onhand_less_zero_n` | ไม่อนุญาติให้สินค้าในมือตํ่ากว่าศูนย์ได้ *(resource only)* | On hand Less than Zero (No) | char |  |
| `vat` | ภาษี *(resource only)* | Vat | char |  |
| `lifo_cost` | ต้นทุน LIFO *(resource only)* | LIFO Cost | char |  |
| `lot_cost` | ต้นทุน Lot  แบบกำหนดเเอง *(resource only)* | Lot Cost | char |  |
| `ic_serial_no_y` | สินค้ามี Serial *(resource only)* | Serial No. (Yes) | char |  |
| `ic_serial_no_n` | สินค้าไม่มี Serial *(resource only)* | Serial No. (No) | char |  |
| `tab_unit` | หน่วยนับ *(resource only)* | Unit | char |  |
| `tab_wh_branch` | คลัง-สาขา *(resource only)* | WH-Branch | char |  |
| `tab_account` | บัญชี *(resource only)* | Account | char |  |
| `tab_description` | รายละเอียด *(resource only)* | Description | char |  |
| `tab_groups_and_dimension` | กลุ่ม และ มิติ *(resource only)* | Groups And Dimension | char |  |
| `tab_name_market` | ชื่อการตลาด *(resource only)* | Name Merket | char |  |
| `tab_warehouse` | คลังสินค้า *(resource only)* | Warehouse | char |  |
| `tab_opposite_unit` | หน่วยนับขนาน *(resource only)* | Opposite Unit | char |  |
| `tab_standard_cost` | ต้นทุนมาตรฐาน *(resource only)* | Standard Cost | char |  |
| `tab_size` | ขนาดสินค้า *(resource only)* | Size | char |  |
| `active` | ใช้งาน *(resource only)* | Active | char |  |
| `inactive` | ไม่ใช้งาน *(resource only)* | Inactive | char |  |
| `tab_pattern` | รูปแบบสินค้า *(resource only)* |  | char |  |
| `tab_remark` | หมายเหตุ *(resource only)* |  | char |  |
| `tab_group_status` | สถานะ *(resource only)* |  | char |  |
| `tab_purchase_wh` | คลัง,พื้นที่เก็บประจำ *(resource only)* |  | char |  |
| `tab_color` | สี *(resource only)* |  | char |  |
| `tab_name_billing` | ชื่อสำหรับพิมพ์บิล *(resource only)* |  | char |  |
| `tab_pos_name` | ชื่อสำหรับระบบ POS *(resource only)* |  | char |  |
| `tab_short_name` | ชื่อย่อ,ชื่อเทียบเคียง *(resource only)* |  | char |  |
| `tab_group` | กลุ่ม,มิติ *(resource only)* |  | char |  |
| `tab_wh_shelf` | คลัง-พื้นที่เก็บ *(resource only)* |  | char |  |
| `tab_purchase_order` | ใบสั่งซื้อ *(resource only)* |  | char |  |
| `tab_deposit` | เงินมัดจำ *(resource only)* |  | char |  |
| `tab_purchase` | ใบซื้อ *(resource only)* |  | char |  |
| `tab_bill_payable` | ใบตั้งหนี้ *(resource only)* |  | char |  |
| `tab_payable_other` | ตั้งหนี้อื่นๆ *(resource only)* |  | char |  |
| `tab_payable_balance` | ยอดยกมาต้นปี *(resource only)* |  | char |  |
| `date_process` | ประมวลผลวันที่ *(resource only)* |  | char |  |
| `date_begin` | จากวันที่ *(resource only)* |  | char |  |
| `date_end` | ถึงวันที่ *(resource only)* |  | char |  |
| `ic_code` | รหัสสินค้า *(resource only)* |  | char |  |
| `ic_code_begin` | จากสินค้า *(resource only)* |  | char |  |
| `ic_code_end` | ถึงสินค้า *(resource only)* |  | char |  |
| `doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `shelf_detail` | ที่เก็บสินค้า *(resource only)* |  | char |  |
| `qty` | จำนวน *(resource only)* | Qty | char |  |
| `amount` | มูลค่า *(resource only)* | Amount | char |  |
| `balance_qty` | ยอดคงเหลือ *(resource only)* | Balance Qty | char |  |
| `balance_amount` | มูลค่าคงเหลือ *(resource only)* | Balance Amount | char |  |
| `ic_cost` | ต้นทุน *(resource only)* | Cost | char |  |
| `in` | เข้า *(resource only)* | In | char |  |
| `out` | ออก *(resource only)* | Out | char |  |
| `qty_in` | จำนวนเพิ่ม *(resource only)* |  | char |  |
| `qty_out` | จำนวนลด *(resource only)* |  | char |  |
| `cost_in` | ต้นทุนเพิ่ม *(resource only)* |  | char |  |
| `cost_out` | ต้นทุนลด *(resource only)* |  | char |  |
| `amount_in` | มูลค่าเพิ่ม *(resource only)* |  | char |  |
| `amount_out` | มูลค่าลด *(resource only)* |  | char |  |
| `trans_name` | ประเภทรายวัน *(resource only)* |  | char |  |
| `doc_time` | เวลา *(resource only)* |  | char |  |
| `qty_sale` | จำนวนขาย *(resource only)* |  | char |  |
| `amount_sale` | มูลค่าขาย *(resource only)* |  | char |  |
| `cost_sale` | ต้นทุนขาย *(resource only)* |  | char |  |
| `qty_sale_return` | จำนวนรับคืน *(resource only)* |  | char |  |
| `amount_sale_return` | มูลค่ารับคืน *(resource only)* |  | char |  |
| `cost_sale_return` | ต้นทุนรับคืน *(resource only)* |  | char |  |
| `cost_net` | ต้นทุนสุทธิ *(resource only)* |  | char |  |
| `amount_net` | มูลค่าสุทธิ *(resource only)* |  | char |  |
| `profit_lost_persent_by_cost` | % ต่อต้นทุน *(resource only)* |  | char |  |
| `profit_lost_amount` | กำไร(ขาดทุน) *(resource only)* |  | char |  |
| `profit_lost_persent_by_amount` | % ต่อยอดสุทธิ *(resource only)* |  | char |  |
| `sale` | ขาย *(resource only)* |  | char |  |
| `sale_return` | รับคืน *(resource only)* |  | char |  |
| `net` | สุทธิ *(resource only)* |  | char |  |
| `purchase_point` | จุดสั่งซื้อ *(resource only)* |  | char |  |
| `purchase_qty` | จำนวนที่สั่งซื้อ *(resource only)* |  | char |  |
| `purchase_last_date` | วันที่สั่งซื้อ *(resource only)* |  | char |  |
| `purchase_last_price` | ราคาสั่งซื้อ *(resource only)* |  | char |  |
| `purchase_last_unit` | หน่วยสั่งซื้อ *(resource only)* |  | char |  |
| `purchase_last_qty` | จำนวนสั่งซื้อ *(resource only)* |  | char |  |
| `buy_last_date` | วันที่ซื้อล่าสุด *(resource only)* |  | char |  |
| `buy_last_price` | ราคาซื้อล่าสุด *(resource only)* |  | char |  |
| `buy_last_unit` | หน่วยซื้อ *(resource only)* |  | char |  |
| `buy_last_qty` | จำนวนซื้อ *(resource only)* |  | char |  |
| `purchase_last_docno` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `buy_last_docno` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `purchase_last` | รายละเอียดการสั่งซื้อล่าสุด *(resource only)* |  | char |  |
| `buy_last` | รายละเอียดการซื้อล่าสุด *(resource only)* |  | char |  |
| `purchase_balance_qty` | ยอดค้างรับ *(resource only)* |  | char |  |
| `purchase_last_amount` | มูลค่าสั่งซื้อ *(resource only)* |  | char |  |
| `buy_last_amount` | มูลค่าสั่งซื้อ *(resource only)* |  | char |  |
| `details` | รายละเอียด *(resource only)* |  | char |  |
| `ap_detail` | รายละเอียดเจ้าหนี้ *(resource only)* |  | char |  |
| `purchase_last_discount` | ส่วนลดสั่งซื้อ *(resource only)* |  | char |  |
| `buy_last_discount` | ส่วนลดซื้อ *(resource only)* |  | char |  |
| `ar_code` | รหัสลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `ar_detail` | ชื่อลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `price_per_unit` | ราคาต่อหน่วย *(resource only)* |  | char |  |
| `sale_detail` | พนักงานขาย *(resource only)* |  | char |  |
| `ar_code_begin` | จากรหัสลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `ar_code_end` | ถึงรหัสลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `cust_code_begin` | จากรหัส *(resource only)* |  | char |  |
| `cust_code_end` | ถึงรหัส *(resource only)* |  | char |  |
| `ap_code_begin` | จากรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `ap_code_end` | ถึงรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `average_cost_in` | ต้นทุนเฉลี่ย *(resource only)* |  | char |  |
| `average_cost_out` | ต้นทุนเฉลี่ย *(resource only)* |  | char |  |
| `average_cost_end` | ต้นทุนเฉลี่ยปัจจุบัน *(resource only)* |  | char |  |
| `date_expire` | วันหมดอายุ *(resource only)* |  | char |  |
| `last_in_flag` | รายการรับเข้าล่าสุด *(resource only)* |  | char |  |
| `last_in_date` | วันที่รับเข้าล่าสุด *(resource only)* |  | char |  |
| `last_out_flag` | รายการออกล่าสุด *(resource only)* |  | char |  |
| `last_out_date` | วันที่ออกล่าสุด *(resource only)* |  | char |  |
| `last_sale_date` | วันที่ขายล่าสุด *(resource only)* |  | char |  |
| `no_movement_date` | จำนวนวันที่ไม่เคลื่อนไหว *(resource only)* |  | char |  |
| `count_day_from` | จำนวนวันจาก *(resource only)* |  | char |  |
| `count_day_to` | ถึง *(resource only)* |  | char |  |
| `balance_qty_first` | ยอดยกมา *(resource only)* |  | char |  |
| `trans_flag_12` | ซื้อ *(resource only)* |  | char |  |
| `trans_flag_48` | รับคืน *(resource only)* |  | char |  |
| `trans_flag_58` | รับคืนจากการเบิก *(resource only)* |  | char |  |
| `trans_flag_60` | รับสำเร็จรูป *(resource only)* |  | char |  |
| `trans_flag_66` | ปรับปรุงเพิ่ม *(resource only)* |  | char |  |
| `trans_flag_68` | ปรับปรุงลด *(resource only)* |  | char |  |
| `trans_flag_54` | ยกมาต้นปี *(resource only)* |  | char |  |
| `trans_flag_44` | ขาย *(resource only)* |  | char |  |
| `trans_flag_16` | ส่งคืน *(resource only)* |  | char |  |
| `trans_flag_56` | เบิก *(resource only)* |  | char |  |
| `profit_lost_persent` | % กำไรขั้นต้น *(resource only)* |  | char |  |
| `condition` | เงื่อนไขเพิ่มเติม *(resource only)* |  | char |  |
| `trans_discount` | ส่วนลดท้ายบิล *(resource only)* |  | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `department_code` | แผนก *(resource only)* |  | char |  |
| `doc_group` | กลุ่มเอกสาร *(resource only)* |  | char |  |
| `user_request` | ผู้ขออนุมัติ *(resource only)* |  | char |  |
| `approve_code` | กลุ่มผู้อนุมัติ *(resource only)* |  | char |  |
| `item_code` | รหัสสินค้า *(resource only)* |  | char |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ *(resource only)* | Unit Code | char |  |
| `price` | ราคา *(resource only)* | Price | char |  |
| `discount` | ส่วนลด *(resource only)* | Discount | char |  |
| `sum_amount` | รวมมูลค่า *(resource only)* | Sum Amount | char |  |
| `due_date` | วันที่ต้องการ *(resource only)* |  | char |  |
| `approve` | รออนุมัติ *(resource only)* |  | char |  |
| `no_approve` | ไม่อนุมัติ *(resource only)* |  | char |  |
| `cancel_approve` | ยกเลิก *(resource only)* |  | char |  |
| `amount_sale_debit` | มูลค่าเพิ่มหนี้ *(resource only)* |  | char |  |
| `cost_sale_debit` | ต้นทุนเพิ่มหนี้ *(resource only)* |  | char |  |
| `warehouse` | คลัง *(resource only)* | Warehouse | char |  |
| `location` | พื้นที่เก็บ *(resource only)* | Location | char |  |
| `lot_number` | หมายเลข LOT *(resource only)* |  | char |  |
| `balance_only` | แสดงเฉพาะที่มียอดคงเหลือ *(resource only)* | Only Have Stock | char |  |
| `doc_format_code` | รหัสเอกสาร *(resource only)* | Document Code | char |  |
| `doc_format` | รูปแบบเอกสาร *(resource only)* | Document Format | char |  |
| `barcode` | Barcode *(resource only)* | Barcode | char |  |
| `supplier_code` | รหัสผู้จัดจำหน่าย *(resource only)* | Supplier Code | char |  |
| `supplier_name` | ชื่อผู้จัดจำหน่าย *(resource only)* | Supplier Name | char |  |
| `tab_replacement` | สินค้าทดแทน *(resource only)* | Product Replacement | char |  |
| `tab_other` | อื่น ๆ *(resource only)* | Other | char |  |
| `tab_newinventory` | เพิ่มสินค้า *(resource only)* | New Inventory | char |  |
| `tab_interaction` | สินค้าที่มีปฏิกริยาต่อกัน *(resource only)* |  | char |  |
| `tab_bundle` | สินค้าพ่วง *(resource only)* |  | char |  |
| `ic_group` | กลุ่มสินค้า *(resource only)* | Product Group | char |  |
| `mfd_date` | วันที่ผลิต *(resource only)* | Manufacturing Date | char |  |
| `mfn_name` | ผู้ผลิต *(resource only)* | Manufacturing Name | char |  |
| `sort_order` | ลำดับ *(resource only)* | No | char |  |
| `lot_select` | การเลือก LOT *(resource only)* |  | char |  |
| `select_auto` | อัตโนมัติ *(resource only)* |  | char |  |
| `select_manual` | เลือกเองเท่านั้น *(resource only)* |  | char |  |
| `accrued_out_qty` | ยอดค้างส่ง *(resource only)* |  | char |  |
| `book_out_qty` | ยอดค้างจอง *(resource only)* |  | char |  |
| `expire_qty` | จำนวนหมดอายุ *(resource only)* |  | char |  |
| `expire_date` | วันที่หมดอายุ *(resource only)* |  | char |  |
| `receive` | รับ *(resource only)* |  | char |  |
| `send` | จ่าย *(resource only)* |  | char |  |
| `receive_date` | วันที่รับ *(resource only)* |  | char |  |
| `tab_normal_price` | ราคาทั่วไป *(resource only)* | Normal Price | char |  |
| `tab_standard_price` | ราคามาตาฐาน *(resource only)* | Standard Price | char |  |
| `tab_bracode_price` | ราคาบาร์โค๊ด *(resource only)* | Barcode Price | char |  |
| `tab_formula_price` | ราคาตามสูตร *(resource only)* | Formula Price | char |  |
| `doc_type` | ประเภทเอกสาร *(resource only)* | Doc Type | char |  |
| `trans_flag` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `big_qty` | หน่วยใหญ่ *(resource only)* |  | char |  |
| `small_qty` | หน่วยย่อย *(resource only)* |  | char |  |
| `premium` | แถม *(resource only)* | Premium | char |  |
| `tab_suggest` | สินค้าแนะนำ *(resource only)* |  | char |  |
| `doc_format_code_adjust_down` | รหัสเอกสารปรับปรุงลด *(resource only)* |  | char |  |
| `doc_format_code_adjust` | รหัสเอกสารปรับปรุงเพิ่ม *(resource only)* |  | char |  |
| `old_price` | ราคาเก่า *(resource only)* |  | char |  |
| `price_member_1` | ราคาสมาชิก 1 *(resource only)* |  | char |  |
| `price_member_2` | ราคาสมาชิก 2 *(resource only)* |  | char |  |
| `price_member_3` | ราคาสมาชิก 3 *(resource only)* |  | char |  |
| `price_member_4` | ราคาสมาชิก 4 *(resource only)* |  | char |  |
| `document_type` | ชนิดเอกสาร *(resource only)* |  | char |  |
| `date_of_import` | วันที่สินเค้าเข้า *(resource only)* |  | char |  |
| `show_all` | แสดงทั้งหมด *(resource only)* |  | char |  |
| `tab_manufacturer` | ผู้ผลิต *(resource only)* |  | char |  |
| `group_main` | กลุ่มสินค้าหลัก *(resource only)* |  | char |  |
| `group_sub` | กลุ่มสินค้าย่อย *(resource only)* |  | char |  |

## ic_serial

**serial number** — Serial Number

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `serial_number` | หมายเลขเครื่อง | Serial Number | varchar(50) |  |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `void_date` | วันที่หมดประกัน | Void Date | smalldatetime | ✓ |
| `ic_unit` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `product_year` | ปี |  | varchar(4) | ✓ |
| `product_week` | สัปดาห์ |  | varchar(2) | ✓ |
| `car_inventory` | CarInventory |  | varchar(50) | ✓ |
| `car_stockno` | เลขสต๊อก |  | varchar(50) | ✓ |
| `car_engineno` | เลขเครื่อง |  | varchar(100) | ✓ |
| `car_chassisno` | เลขแชสซีส์ |  | varchar(100) | ✓ |

index: `ic_serial_PK_PRIMARY`(ic_code,serial_number), `ic_serial_serial_number`(serial_number), `ic_serial_wh_code`(wh_code), `ic_serial_shelf_code`(shelf_code), `ic_serial_status`(status)

## ic_size_use

**ขนาดสินค้าที่ใช้** — Item Size Use

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ *(resource only)* | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) *(resource only)* | Name (English) | varchar(100) |  |
| `width_length_height` | กว้างxยาวxสูง | Width Length Height | varchar(100) | ✓ |
| `weight` | นํ้าหนัก | Weight | float | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

index: `ic_size_use_PK_CODE`(code,ic_code)

## ic_standard_cost

**ต้นทุนมาตรฐาน** — ต้นทุนมาตรฐาน

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `date_start` | วันที่ |  | smalldatetime | ✓ |
| `cost1` | ต้นทุน |  | float |  |
| `unit_name` | ชื่อหน่วย *(resource only)* |  | varchar |  |

index: `ic_standard_cost_pk_ic_standard_cost_pk`(ic_code,date_start), `pk_ic_standard_cost_2`(ic_code,unit_code,date_start)

## ic_unit_use

**หน่วยนับสินค้าที่ใช้** — Item Unit Use

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ *(resource only)* | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) *(resource only)* | Name (English) | varchar(100) |  |
| `line_number` | ลำดับ | Line Number | int | ✓ |
| `stand_value` | ตัวตั้ง | Stand Value | float | ✓ |
| `divide_value` | ตัวหาร | Divide Value | float | ✓ |
| `ratio` | อัตราส่วน | Ratio | float | ✓ |
| `row_order` | ลำดับที่ | Row Order | int | ✓ |
| `width_length_height` | กว้างxยาวxสูง | Width Length Height | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `weight` | น้ำหนัก(กก) | Weight | varchar(100) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `unit_size` | ขนาดสินค้า | Size | float | ✓ |

index: `ic_unit_use_PK_CODE`(code,ic_code), `ic_unit_use_code`(code), `ic_unit_use_ic_code`(ic_code), `ic_unit_use_iccode_code`(ic_code,code)

## ic_warehouse_location_group

**กลุ่มที่เก็บ** — Table 386

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `location_group` | กลุ่มที่เก็บ |  | varchar(25) | ✓ |
| `name_1` | ชื่อกลุ่มที่เก็บ |  | varchar(255) | ✓ |
| `guid_code` | GUID |  | varchar(50) | ✓ |

index: `ic_warehouse_location_group_pk_ic_wh_lc_group`(wh_code,location_group)

## ic_warehouse_location_group_detail

**กลุ่มที่เก็บเชื่อมกับที่เก็บ** — Table 387

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `location_group` | กลุ่มที่เก็บ |  | varchar(25) | ✓ |
| `location` | ที่เก็บ |  | varchar(25) | ✓ |
| `priolity` | ลำดับ |  | smallint | ✓ |
| `location_name` | ชื่อที่เก็บ *(resource only)* |  | char |  |

index: `ic_warehouse_location_group_detail_pk_ic_wh_lc_group_detail`(wh_code,location_group,location)

## ic_wh_shelf

**คลังและพื้นที่เก็บสินค้า** — Warehouse Shelf

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `wh_code` | รหัสคลัง | Warehouse Code | varchar(25) |  |
| `shelf_code` | รหัสพื้นที่เก็บ | Shelf Code | varchar(25) |  |
| `max_point` | จำนวนสูงสุด | Max Point | float | ✓ |
| `min_point` | จำนวนน้อยสุด | Min Point | int | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `shelf_name` | ชื่อพื้นที่เก็บ *(resource only)* | Shelf Name | char |  |
| `wh_name` | ชื่อคลัง *(resource only)* | Warehouse  Name | char |  |
| `grid_temp1` | temp1 *(resource only)* |  | char |  |
| `shelf_list` | ชั้นวาง |  | varchar(255) | ✓ |

index: `ic_wh_shelf_PK_CODE`(wh_code,shelf_code,ic_code), `ic_wh_shelf_IC_CODE`(ic_code)

## singha_online_unit_maping

**กำหนดหน่วยนับsinghaonline** — singha online unit maping

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `unit_sale` | หน่วยขาย |  | varchar(100) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(100) | ✓ |
| `qty_per_unit` | จำนวนต่อหน่วย |  | float | ✓ |
| `line_number` | หมายเลขบรรทัด |  | int | ✓ |

