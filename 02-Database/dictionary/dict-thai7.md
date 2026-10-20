---
tags: [sml, dictionary, thai7, generated]
module: Thai7
---
# พจนานุกรม: Thai7 — Thai7

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ic_attribute_thai7]] | เก็บขอมูลคุณลักษณะของสินค้า / item attribute | 6 |
| [[#ic_category_thai7]] | หมวดสินค้า / Item Category | 7 |
| [[#ic_inventory_pictures]] | รูปภาพสินค้า / inventory pictures | 6 |
| [[#ic_inventory_price_thai7]] | ราคาสินค้า / inventory price | 6 |
| [[#ic_inventory_thai7]] | สินค้า / Inventory thai7 | 27 |
| [[#resource_thai7]] | resource thai7 / resource thai7 | 22 |
| [[#thai7_process]] | ประมวลผล / thai7 process | 7 |

## ic_attribute_thai7

**เก็บขอมูลคุณลักษณะของสินค้า** — item attribute · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `member_id` | รหัสสมาชิก |  | varchar(50) |  |
| `attribute_name` | คุณลักษณะ |  | varchar(200) | ✓ |
| `attribute_value` | ค่าคุณลักษณะ |  | varchar(100) | ✓ |
| `date_save` | วันที่บันทึกข้อมูล |  | smalldatetime | ✓ |
| `guid_code` | รหัส |  | varchar(50) | ✓ |

## ic_category_thai7

**หมวดสินค้า** — Item Category · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(10) |  |
| `name_1` | ชื่อ | Name | varchar(100) | ✓ |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | GUID | varchar(35) | ✓ |
| `parent_code` | ลูกข่าย |  | int |  |
| `cate_type` | ประเภท |  | int | ✓ |

index: `ic_category_thai7_PK_CODE`(code)

## ic_inventory_pictures

**รูปภาพสินค้า** — inventory pictures · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | รหัส |  | varchar(50) |  |
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `member_id` | รหัสสมาชิก |  | varchar(50) |  |
| `picture_name` | ชื่อรูปภาพ |  | varchar(100) |  |
| `sort_list` | ลำดับ |  | smallint |  |
| `date_save` | วันที่บันทึก |  | smalldatetime |  |

## ic_inventory_price_thai7

**ราคาสินค้า** — inventory price · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | รหัส |  | varchar(50) |  |
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `member_id` | รหัสสมาชิก |  | varchar(50) |  |
| `price_name` | ชื่อราคา |  | varchar(200) | ✓ |
| `price` | ราคา |  | float | ✓ |
| `date_save` | วันที่บันทึก |  | smalldatetime | ✓ |

## ic_inventory_thai7

**สินค้า** — Inventory thai7 · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | รหัสสินค้า(MD5) |  | varchar(50) | ✓ |
| `code` | รหัสสินค้า |  | varchar(255) |  |
| `name_1` | ชื่อสินค้า |  | varchar(50) | ✓ |
| `item_detail` | รายละเอียดสินค้า |  | image | ✓ |
| `item_brand` | รหัสยี่ห้อ |  | varchar(50) | ✓ |
| `item_model` | รุ่นสินค้า |  | varchar(50) | ✓ |
| `item_category` | รหัสกลุ่ม |  | varchar(50) | ✓ |
| `item_category_sub` | รหัสกลุ่มย่อย |  | varchar(50) | ✓ |
| `item_wide` | ความกว้าง |  | varchar(200) | ✓ |
| `item_long` | ความยาว |  | varchar(200) | ✓ |
| `item_high` | ความสูง |  | varchar(200) | ✓ |
| `item_weight` | น้ำหนัก |  | varchar(200) | ✓ |
| `item_in_stock` | จำนวนสินค้า |  | int | ✓ |
| `balance_qty` | ยอดคงเหลือ |  | float | ✓ |
| `accrued_in_qty` | ยอดค้างรับ |  | float | ✓ |
| `accrued_out_qty` | ยอดค้างส่ง |  | float | ✓ |
| `date_save` | วันที่บันทึก |  | smalldatetime | ✓ |
| `date_modified` | วันที่แก้ไข |  | smalldatetime | ✓ |
| `affiliate_item` | ประเภทที่มา |  | int | ✓ |
| `import_item` | sml |  | int | ✓ |
| `is_balance` | newedit |  | int | ✓ |
| `status` | สถานะ |  | int | ✓ |
| `price_out_qty` | มูลค่าค้างส่ง |  | float | ✓ |
| `tab_detail` | รายละเอียดสินค้า *(resource only)* |  | char |  |
| `tab_price` | ราคาสินค้า *(resource only)* |  | char |  |
| `tab_attribute` | คุณลักษณะสินค้า *(resource only)* |  | char |  |
| `tab_image` | รูปสินค้า *(resource only)* |  | char |  |

## resource_thai7

**resource thai7** — resource thai7 · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `login_code` | User Name *(resource only)* |  | char |  |
| `login_pass` | Password *(resource only)* |  | char |  |
| `shop_name` | ชื่อร้านค้า(ใน Thai7) *(resource only)* |  | char |  |
| `select` | เลือก *(resource only)* |  | char |  |
| `shop_description` | รายละเอียดร้านค้า *(resource only)* |  | char |  |
| `status` | สถานะ *(resource only)* |  | char |  |
| `ic_code` | รหัสสินค้า *(resource only)* |  | char |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `sml` | SML *(resource only)* |  | char |  |
| `thai7` | THAI7 *(resource only)* |  | char |  |
| `new_date` | วันที่เพิ่ม *(resource only)* |  | char |  |
| `edit_date` | วันที่แก้ใข *(resource only)* |  | char |  |
| `ic_description` | รายละเอียดสินค้า *(resource only)* |  | char |  |
| `item_category` | รหัสกลุ่ม *(resource only)* |  | varchar |  |
| `item_category_sub` | รหัสกลุ่มย่อย *(resource only)* |  | varchar |  |
| `doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `contactor` | ผู้ติดต่อ *(resource only)* |  | char |  |
| `qty` | จำนวน *(resource only)* |  | char |  |
| `amount` | จำนวนเงิน *(resource only)* |  | char |  |
| `send_type` | ประเภทการส่ง *(resource only)* |  | char |  |
| `query_condition` | เงื่อนไขเพิ่มเติม *(resource only)* |  | char |  |

## thai7_process

**ประมวลผล** — thai7 process · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสสินค้า |  | varchar(50) |  |
| `name_1` | ชื่อสินค้า |  | varchar(255) |  |
| `unit_standard` | หน่วยยอดคงเหลือ |  | varchar(255) |  |
| `balance_qty` | ยอดคงเหลือ |  | float |  |
| `accrued_out_qty` | ยอดค้างส่ง |  | float |  |
| `accrued_in_qty` | ยอดค้างรับ |  | float |  |
| `guid_code` | GUID |  | varchar(50) |  |

