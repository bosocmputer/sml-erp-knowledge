---
tags: [sml, dictionary, temp, generated]
module: Temp
---
# พจนานุกรม: Temp — ตารางชั่วคราว

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#expire_date_temp]] | สินค้าหมดอายุ / Table 306 | 11 |
| [[#ic_trans_detail_temp]] | รายละเอียดรายวัน(ชั่วคราว) / IC Trans Detail temp | 19 |
| [[#ic_trans_temp]] | รายวัน(ชัวคราว) / IC Trans Temp | 15 |
| [[#kitchen_print_count]] | kitchen_print_count / kitchen_print_count | 4 |
| [[#order_cart]] | รถเข็น / Table 312 | 10 |
| [[#order_item]] | รายการสินค้า / Table 313 | 16 |
| [[#order_message]] | order message / order message | 7 |
| [[#sml_image_document]] | sml_image_document / sml_image_document | 10 |
| [[#stock_expire_temp]] | สินค้าหมดอายุ / Table 307 | 11 |
| [[#stock_expire_warehouse_temp]] | สินค้าหมดอายุ / Table 307 | 12 |
| [[#temp_cash_movement]] | เคลื่อนไหวเงินสด / Table 310 | 9 |

## expire_date_temp

**สินค้าหมดอายุ** — Table 306

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` |  |  | datetime | ✓ |
| `doc_no` |  |  | varchar(25) | ✓ |
| `ic_code` |  |  | varchar(50) | ✓ |
| `ic_name` |  |  | varchar(50) | ✓ |
| `unit_code` |  |  | varchar(50) | ✓ |
| `expire_qty` |  |  | float(50) | ✓ |
| `expire_date` |  |  | varchar(50) | ✓ |
| `cust_code` |  |  | varchar(50) | ✓ |
| `cust_name` |  |  | varchar(50) | ✓ |
| `balance_qty` |  |  | varchar(50) | ✓ |
| `balance_unit_code` |  |  | varchar(50) | ✓ |

## ic_trans_detail_temp

**รายละเอียดรายวัน(ชั่วคราว)** — IC Trans Detail temp

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า |  | varchar(500) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `sum_amount` | รวม |  | float | ✓ |
| `line_number` | บรรทัด |  | smallint | ✓ |
| `time_add` | เวลาเพิ่มรายการ |  | datetime | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `barcode` | บาร์โค๊ด |  | varchar(50) | ✓ |
| `doc_time` | เวลา |  | varchar(25) | ✓ |
| `wh_code` | คลัง |  | varchar(50) | ✓ |
| `shelf_code` | ที่เก็บ |  | varchar(50) | ✓ |
| `wh_code_2` | เข้าคลัง |  | varchar(50) | ✓ |
| `shelf_code_2` | เข้าที่เก็บ |  | varchar(50) | ✓ |
| `user_code` | User Code |  | varchar(50) | ✓ |
| `success_status` | Success Status |  | smallint | ✓ |

## ic_trans_temp

**รายวัน(ชัวคราว)** — IC Trans Temp

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `cust_code` | ลูกหนี้/เจ้าหนี้ |  | varchar(50) | ✓ |
| `wh_code` | คลังสินค้า |  | varchar(50) | ✓ |
| `shelf_code` | ที่เก็บสินค้า |  | varchar(50) | ✓ |
| `location_code` | ชั้นวาง |  | varchar(255) | ✓ |
| `doc_time` | เวลา |  | varchar(10) | ✓ |
| `wh_code_2` | เข้าคลัง |  | varchar(50) | ✓ |
| `shelf_code_2` | เข้าที่เก็บ |  | varchar(50) | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(255) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันแก้ไขล่าสุด |  | datetime | ✓ |
| `branch_code` | สาขา |  | varchar(255) | ✓ |

index: `ic_trans_temp_ic_trans_temp_pk`(doc_no,trans_flag)

## kitchen_print_count

**kitchen_print_count** — kitchen_print_count

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `kitchen_code` | ห้องครัว/บาร์น้ำ |  | varchar(50) |  |
| `print_count` | ลำดับ |  | smallint | ✓ |

index: `kitchen_print_count_doc_date_kitchen_code`(doc_date,kitchen_code)

## order_cart

**รถเข็น** — Table 312

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `user_owner` | เจ้าของ |  | varchar(25) |  |
| `cart_number` | หมายเลขรถเข็น |  | varchar(5) |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) |  |
| `status` | สถานะ |  | smallint | ✓ |
| `amount` | ยอดรวม |  | float | ✓ |
| `trans_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `bill_type` | ประเภทการขาย |  | smallint | ✓ |
| `tax_type` | ประเภทภาษี |  | smallint | ✓ |
| `branch_code` | branch code |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |

index: `order_cart_pk_order_cart_user_number`(user_owner,cart_number)

## order_item

**รายการสินค้า** — Table 313

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `user_owner` | เจ้าของ |  | varchar(25) |  |
| `cart_number` | หมายเลขรถเข็น |  | varchar(5) |  |
| `item_code` | รหัสสินค้า |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวน |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `discount_word` | ส่วนลด |  | varchar(25) | ✓ |
| `amount` | ยอดรวม |  | float | ✓ |
| `remark` | หมายเหตุ |  | varchar(100) | ✓ |
| `order_date` | วันที่สั่ง |  | datetime | ✓ |
| `order_time` | เวลาที่สั่ง |  | varchar(5) | ✓ |
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บ |  | varchar(25) | ✓ |
| `barcode` | barcode |  | varchar(25) | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `lot_number` | Lot Number |  | varchar(255) | ✓ |

index: `pk_order_item_1`(user_owner,cart_number)

## order_message

**order message** — order message

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cart_number` | cart number |  | varchar(25) | ✓ |
| `user_owner` | user owner |  | varchar(25) | ✓ |
| `cust_code` | cust code |  | varchar(25) | ✓ |
| `order_item` | order item |  | varchar(25) | ✓ |
| `is_read` | is read |  | smallint | ✓ |
| `is_notification` | is notification |  | smallint | ✓ |
| `message` | message |  | text | ✓ |

## sml_image_document

**sml_image_document** — sml_image_document

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `image_id` | รหัสรูปภาพ |  | varchar(100) |  |
| `image_file` | ไฟล์ภาพ |  | image |  |
| `system_id` | ระบบ |  | varchar(50) |  |
| `guid` | GUID |  | varchar(60) |  |
| `latitude` | Latitude |  | float |  |
| `longitude` | Longtitude |  | float |  |
| `mac_address` | หมายเลขเครื่อง |  | varchar(588) |  |
| `user_code` | รหัสพนักงาน |  | varchar(255) |  |
| `refer_doc_no` | อ้างอิงเอกสารเลขที่ |  | varchar(50) | ✓ |
| `refer_trans_flag` | อ้างอิงเอกสารวันที่ |  | smallint | ✓ |

## stock_expire_temp

**สินค้าหมดอายุ** — Table 307

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | datetime | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) | ✓ |
| `ic_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `ic_name` | ชื่อสินค้า |  | varchar(255) | ✓ |
| `unit_code` | หน่วยซื้อ |  | varchar(25) | ✓ |
| `cust_code` | รหัสผู้จำหน่าย |  | varchar(50) | ✓ |
| `cust_name` | ชื่อผู้จำหน่าย |  | varchar(255) | ✓ |
| `expire_qty` | จำนวนซื้อ |  | float | ✓ |
| `expire_date` | วันหมดอายุ |  | datetime | ✓ |
| `balance_qty` | ยอดคงเหลือ |  | float | ✓ |
| `balance_unit_code` | หน่วยคงเหลือ |  | varchar(25) | ✓ |

## stock_expire_warehouse_temp

**สินค้าหมดอายุ** — Table 307

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | datetime | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) | ✓ |
| `ic_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `ic_name` | ชื่อสินค้า |  | varchar(255) | ✓ |
| `unit_code` | หน่วยซื้อ |  | varchar(25) | ✓ |
| `cust_code` | รหัสผู้จำหน่าย |  | varchar(50) | ✓ |
| `cust_name` | ชื่อผู้จำหน่าย |  | varchar(255) | ✓ |
| `expire_qty` | จำนวนซื้อ |  | float | ✓ |
| `expire_date` | วันหมดอายุ |  | datetime | ✓ |
| `balance_qty` | ยอดคงเหลือ |  | float | ✓ |
| `balance_unit_code` | หน่วยคงเหลือ |  | varchar(25) | ✓ |
| `warehouse` | คลังสินค้า |  | varchar(25) | ✓ |

## temp_cash_movement

**เคลื่อนไหวเงินสด** — Table 310

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | datetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) | ✓ |
| `ap_ar_code` | รหัสลูกหนี้/เจ้าหนี้ |  | varchar(50) | ✓ |
| `trans_flag` | ประเภทเอกสาร |  | smallint | ✓ |
| `trans_detail` | รายละเอียด |  | varchar(255) | ✓ |
| `amount_in` | ยอดรับ |  | float | ✓ |
| `amount_out` | ยอดจ่าย |  | float | ✓ |
| `amount_balance` | ยอดคงเหลือ |  | float | ✓ |

