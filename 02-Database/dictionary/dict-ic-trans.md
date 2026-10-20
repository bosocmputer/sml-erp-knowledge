---
tags: [sml, dictionary, ic-trans, generated]
module: IC_Trans
---
# พจนานุกรม: IC_Trans — เอกสารสินค้า (ic_trans)

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#barcode_import_list]] | ยิงต่อเนื่องจาก handheld / Table 298 | 8 |
| [[#barcode_import_list_detail]] | สำหรับเชื่อมกับ handheld / Table 297 | 12 |
| [[#ic_date_adjust]] | ปรับปรุงวันที่รับ/ส่งสินค้า / Date Adjust | 8 |
| [[#ic_date_adjust_detail]] | รายละเอียดปรับปรุงวันที่รับ/ส่งสินค้า / Date Adjust Detail | 12 |
| [[#ic_extra_detail]] | รายละเอียด / PO SO Extra | 17 |
| [[#ic_hidden_cost_process]] | ic_hidden_cost_process  | 16 |
| [[#ic_hidden_cost_process_item]] | ic_hidden_cost_process_item / ic_hidden_cost_process_item | 17 |
| [[#ic_hidden_cost_process_ref]] | ic_hidden_cost_process_ref / ic_hidden_cost_process_ref | 7 |
| [[#ic_promotion]] | โปรโมชั่นสินค้า / Item Promotion | 13 |
| [[#ic_promotion_detail]] | รายละเอียดโปรโมชั่นสินค้า / Promotion Detail | 15 |
| [[#ic_purchase_price]] | กำหนดราคาซื้อ / Purchase Price | 10 |
| [[#ic_purchase_price_detail]] | รายละเอียดราคาซื้อ / Purchase Price Detail | 12 |
| [[#ic_relation]] | เอกสารเกี่ยวข้อง / Relation | 6 |
| [[#ic_relation_detail]] | รายละเอียดเอกสารเกี่ยวข้อง / Relation Detail | 10 |
| [[#ic_stk_build]] | จัดชุดสินค้า / Item Build | 16 |
| [[#ic_stk_build_detail]] | รายละเอียดจัดชุดสินค้า / Item Build Detial | 10 |
| [[#ic_trans]] | รายวันทั้งหมด / IC - Transection | 343 |
| [[#ic_trans_additional]] | รายละเอียดเพิ่มเติมรายวัน / IC Trans Addtitional | 24 |
| [[#ic_trans_detail]] | รายละเอียดรายวัน / IC - Transection Detail | 191 |
| [[#ic_trans_detail_allocate]] | รายละเอียดรายวันการจัดสรร  | 10 |
| [[#ic_trans_detail_department]] | รายละเอียดรายวันแผนก  | 10 |
| [[#ic_trans_detail_jobs]] | รายละเอียดรายวันงาน / Table 335 | 10 |
| [[#ic_trans_detail_lot]] | Table 237 / Table 237 | 19 |
| [[#ic_trans_detail_project]] | รายละเอียดรายวันโครงการ  | 10 |
| [[#ic_trans_detail_promotion]] | รายละเอียดโปรโมชั่น / IC Trans Detail Promotion | 11 |
| [[#ic_trans_detail_site]] | รายละเอียดรายวันฝ่าย  | 10 |
| [[#ic_trans_pos_campaign]] | Inventory Transaction POS Campaign / Inventory Transaction POS Campaign | 7 |
| [[#ic_trans_resource]] | รายละเอียดข้อความ / Inventory Transfer Resource | 12 |
| [[#ic_trans_serial_number]] | serial number (รายวัน) / Serial Number Result | 28 |
| [[#ic_trans_shipment]] | การจัดส่ง / Table 342 | 21 |
| [[#ic_weight_cost]] | ต้นทุนแฝง / Weight Cost | 12 |
| [[#ic_weight_cost_detail]] | รายละเอียดต้นทุนแฝง / Weight Cost Detail | 8 |
| [[#take_order_temp]] | take order / Table 344 | 8 |

## barcode_import_list

**ยิงต่อเนื่องจาก handheld** — Table 298

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่ |  | datetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `qty` | จำนวนชิ้น |  | float | ✓ |
| `machine_name` | ชื่อเครื่อง |  | varchar(50) | ✓ |
| `get_success` | สถานะ |  | smallint | ✓ |
| `wh_code` | คลังสินค้า |  | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า |  | varchar(25) | ✓ |

index: `barcode_import_list_barcode_import_list_idx`(doc_no)

## barcode_import_list_detail

**สำหรับเชื่อมกับ handheld** — Table 297

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `doc_date` | วันที่เอกสาร |  | datetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) | ✓ |
| `lot_number` | Lot Number |  | varchar(25) | ✓ |
| `expire_date` | Expire Date |  | smalldatetime | ✓ |
| `mfd_date` | MFD Date |  | smalldatetime | ✓ |
| `mfn_name` | Manufacturing |  | varchar(255) | ✓ |

index: `barcode_import_list_detail_idx`(doc_no)

## ic_date_adjust

**ปรับปรุงวันที่รับ/ส่งสินค้า** — Date Adjust

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ic_date_adjust_PK_CODE`(doc_no)

## ic_date_adjust_detail

**รายละเอียดปรับปรุงวันที่รับ/ส่งสินค้า** — Date Adjust Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `bill_date` | วันที่บิล | Bill Date | smalldatetime |  |
| `bill_no` | เลขที่บิล | Bill No | varchar(25) |  |
| `credit_day_old` | เครดิตเดิม (วัน) | Credit Day Old | int | ✓ |
| `due_date_old` | วันที่ครบกำหนดเดิม | Due Date Old | smalldatetime | ✓ |
| `sending_date_old` | วันที่รับ/ส่งสินค้าเดิม | Sending Date Old | smalldatetime | ✓ |
| `credit_day_new` | เครดิตใหม่ (วัน) | Credit Day New | int | ✓ |
| `due_date_new` | วันที่ครบกำหนดใหม่ | Due Date New | smalldatetime | ✓ |
| `sending_date_new` | วันที่รับ/ส่งสินค้าใหม่ | Sending Date New | smalldatetime | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ic_extra_detail

**รายละเอียด** — PO SO Extra

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint | ✓ |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint | ✓ |
| `doc_no` | เอกสารเลขที่ | Doc No | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Doc Date | smalldatetime | ✓ |
| `ic_code` | รหัสสินค้า | IC Code | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า | IC Name | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `ic_color` | สีสินค้า | Color | varchar(25) | ✓ |
| `ic_size` | ขนาดสินค้า | Size | varchar(25) | ✓ |
| `ic_character` | ลักษณะสินค้า | Charecter | varchar(25) | ✓ |
| `ic_pattern` | รูปแบบสินค้า | Pattern | varchar(25) | ✓ |
| `remark` | คำอธิบาย | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |
| `doc_group` | กลุ่มเอกสาร | Doc Group | varchar(25) | ✓ |

## ic_hidden_cost_process

**ic_hidden_cost_process**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) | ✓ |
| `guid_code` | GUID Code |  | varchar(50) | ✓ |
| `doc_format_code` | ประเภทเอกสาร |  | varchar(50) | ✓ |
| `total_amount` | มูลค่าสุทธิ |  | float | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `branch_code` | สาขา |  | varchar(50) | ✓ |
| `doc_no_adjust` | รหัสเอกสารปรับปรุง |  | varchar(25) | ✓ |
| `doc_format_code_adjust` | ประเภทเอกสารปรับปรุง |  | varchar(50) | ✓ |
| `cal_hidden_cost_from` | เฉลี่ยต้นทุนแฝงด้วย |  | int | ✓ |
| `net_worth` | มูลค่าสุทธิ |  | int | ✓ |
| `value_before_tax` | มูลค่าก่อนภาษี |  | int | ✓ |
| `cal_hidden_cost_follow` | เฉลี่ยต้นทุนแฝงตาม |  | int | ✓ |
| `product_value` | มูลค่าสินค้า |  | int | ✓ |
| `qty` | จำนวน |  | int | ✓ |

## ic_hidden_cost_process_item

**ic_hidden_cost_process_item** — ic_hidden_cost_process_item

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Doc No |  | varchar(50) |  |
| `billing_no` | บิลซื้อ |  | varchar(50) |  |
| `billing_date` | วันที่เอกสาร |  | smalldatetime |  |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `item_value` | ปริมาณ/มูลค่า |  | float | ✓ |
| `item_amount` | มูลค่า |  | float | ✓ |
| `adjust_amount` | ยอดที่ตัดได้ |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `wh_code` | คลังสินค้า |  | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า |  | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `stand_value` | ตัวตั้ง |  | float | ✓ |
| `divide_value` | ตัวหาร |  | float | ✓ |

## ic_hidden_cost_process_ref

**ic_hidden_cost_process_ref** — ic_hidden_cost_process_ref

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | Doc No |  | varchar(50) |  |
| `ref_type` | Ref Type |  | smallint |  |
| `doc_ref_type` | ประเภทเอกสาร |  | smallint |  |
| `doc_ref_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_ref_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_ref_amount` | มูลค่า |  | float | ✓ |
| `amount_before_vat` | มูลค่าก่อนภาษี |  | float | ✓ |

## ic_promotion

**โปรโมชั่นสินค้า** — Item Promotion

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `promote_code` | รหัสโปรโมชั่น | Promote Code | varchar(25) |  |
| `promote_name` | ชื่อโปรโมชั่น | Promote Name | varchar(100) | ✓ |
| `promote_type` | ประเภทโปรโมชั่น | Promote Type | smallint | ✓ |
| `promote_start` | วันที่เริ่มต้นโปรโมชั่น | Promote Start | smalldatetime | ✓ |
| `promote_stop` | วันที่สิ้นสุดโปรโมชั่น | Promote Stop | smalldatetime | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `ar_type` | ประเภทลูกหนี้ | AR Type | smallint | ✓ |
| `ar_group` | กลุ่มลูกหนี้ | AR Group | smallint | ✓ |
| `ar_code_1` | จากรหัสลูกหนี้ | AR Code 1 | varchar(25) | ✓ |
| `ar_code_2` | ถึงรหัสลูกหนี้ | AR Code 2 | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ic_promotion_PK_CODE`(promote_code)

## ic_promotion_detail

**รายละเอียดโปรโมชั่นสินค้า** — Promotion Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `promote_code` | รหัสโปรโมชั่น | Promotion Code | varchar(25) | ✓ |
| `promote_name` | ชื่อโปรโมชั่น | Promotion Name | varchar(100) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | varchar(100) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `qty_1` | จากจำนวน | from Qty | float | ✓ |
| `qty_2` | ถึงจำนวน | to Qty | float | ✓ |
| `promote_price` | ราคาโปรโมชั่น (ต่อหน่วย) | Promotion Price | float | ✓ |
| `promote_sum_price` | ราคาโปรโมชั่น (รวม) | Promotion Sum Price | float | ✓ |
| `free_ic_code` | สินค้าแถม | Free Item Code | varchar(25) | ✓ |
| `free_ic_unit` | หน่วยนับสินค้าแถม | Free Item Unit | varchar(25) | ✓ |
| `free_qty` | จำนวนแถม | Free Qty | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ic_purchase_price

**กำหนดราคาซื้อ** — Purchase Price · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `ap_code` | เจ้าหนี้ | AP Code | varchar(25) | ✓ |
| `start_date` | วันที่เริ่มต้น | Start Date | smalldatetime | ✓ |
| `stop_date` | วันที่สิ้นสุด | Stop Date | smalldatetime | ✓ |
| `tax_group` | กลุ่มภาษี | Tax Group | varchar(25) | ✓ |
| `remark` | หมยเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

## ic_purchase_price_detail

**รายละเอียดราคาซื้อ** — Purchase Price Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `credit_code` | รหัสเครดิต | Credit Code | varchar(25) | ✓ |
| `sending_type` | ประเภทการส่ง | Sending Type | smallint | ✓ |
| `from_qty` | จากจำนวน | From Qty | float | ✓ |
| `to_qty` | ถึงจำนวน | To Qty | float | ✓ |
| `price` | ราคาซื้อ | Price | float | ✓ |
| `discount` | ส่วนลด | Discount | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ic_relation

**เอกสารเกี่ยวข้อง** — Relation

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Doc Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Doc No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Doc Reference | varchar(25) | ✓ |
| `total_qty` | จำนวนทั้งหมด | Total Qty | float | ✓ |
| `total_amount` | ราคาทั้งหมด | Total Amount | float | ✓ |
| `transection_flag` | รายวันระบบ | Transection Flag | smallint | ✓ |

## ic_relation_detail

**รายละเอียดเอกสารเกี่ยวข้อง** — Relation Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Doc Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Doc No | varchar(25) |  |
| `ic_code_1` | รหัสสินค้า 1 | Item Code 1 | varchar(25) | ✓ |
| `qty_1` | จำนวน 1 | Qty 1 | float | ✓ |
| `line_number_1` | บรรทัด 1 | Line Number 1 | int | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Doc Reference | varchar(25) | ✓ |
| `ic_code_2` | รหัสสินค้า 2 | Item Code 2 | varchar(25) | ✓ |
| `qty_2` | จำนวน 2 | Qty 2 | float | ✓ |
| `line_number_2` | บรรทัด 2 | Line Number 2 | int | ✓ |
| `transection_flag` | รายวันระบบ | Transection Flag | smallint | ✓ |

## ic_stk_build

**จัดชุดสินค้า** — Item Build

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | varchar(100) |  |
| `wh_code` | คลังสินค้า | Warehouse | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า | Shelf | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `wage` | ค่าแรง | Wage | float | ✓ |
| `cost` | โสหุ้ย | Cost | float | ✓ |
| `qty` | จำนวน | Qty | float | ✓ |
| `person_code` | ผู้ออกใบประกอบ | Person Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ic_stk_build_PK_CODE`(doc_no)

## ic_stk_build_detail

**รายละเอียดจัดชุดสินค้า** — Item Build Detial

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | varchar(100) |  |
| `wh_code` | คลังสินค้า | Warehouse | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า | Shelf | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `qty` | จำนวน | Qty | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ic_trans

**รายวันทั้งหมด** — IC - Transection · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Doc Reference | varchar(255) | ✓ |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ | Doc Reference Date | smalldatetime | ✓ |
| `tax_doc_no` | เลขที่ใบกำกับ | Tax No | varchar(25) | ✓ |
| `tax_doc_date` | วันที่ใบกำกับ | Tax Date | smalldatetime | ✓ |
| `inquiry_type` | ประเภทรายการ | Inquiry Type | smallint | ✓ |
| `vat_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `cust_code` | ลูกหนี้/เจ้าหนี้ | AP/AR Code | varchar(25) | ✓ |
| `contactor` | ผู้ติดต่อ | Contactor | varchar(25) | ✓ |
| `branch_code` | สาขา | Branch Code | varchar(25) | ✓ |
| `project_code` | โครงการ | Project Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | Department | varchar(25) | ✓ |
| `sale_area_code` | เขตการขาย | Sale Area | varchar(25) | ✓ |
| `sale_code` | พนักงานขาย | Sale | varchar(25) | ✓ |
| `send_type` | ประเภทการส่ง | Sending Type | smallint | ✓ |
| `send_day` | รับ/ส่ง ภายใน(วัน) | Send/Receive Day | int | ✓ |
| `send_date` | วันที่รับ/ส่งสินค้า | Send Date | smalldatetime | ✓ |
| `expire_date` | วันที่หมดอายุ | Expire Date | smalldatetime | ✓ |
| `credit_day` | วันเครดิต | Credit Day | int | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `answer_type` | ลูกค้าตอบกลับ | Answer Type | smallint | ✓ |
| `transport_value` | ค่าขนส่ง | Transport Value | float | ✓ |
| `discount_word` | ส่วนลด | Discount | varchar(25) | ✓ |
| `vat_rate` | อัตราภาษี | Vat Rate | float | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `total_cost` | ต้นทุนสินค้า | Total Cost | float | ✓ |
| `total_value` | มูลค่าสินค้า | Total Value | float | ✓ |
| `total_discount` | มูลค่าส่วนลด | Total Discount | float | ✓ |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `total_after_vat` | มูลค่าหลังคิดภาษี | Total After Vat | float | ✓ |
| `total_except_vat` | มูลค่ายกเว้นภาษี | Total Except Vat | float | ✓ |
| `total_amount` | มูลค่าสุทธิ | Total Net Value | float | ✓ |
| `balance_amount` | ยอดเงินคงเหลือ | Balance Amount | float | ✓ |
| `adjust_reason` | เหตุผลการปรับปรุง | Adjust Reason | varchar(25) | ✓ |
| `approve_code` | กลุ่มผู้อนุมัติ | Approve User Group | varchar(25) | ✓ |
| `approve_date` | วันที่อนุมัติ | Approve Date | smalldatetime | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `ar_code` | รหัสลูกค้า/ลูกหนี้ *(resource only)* | Ar Code | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | Ap Code | char |  |
| `user_request` | ผู้ขออนุมัติ | User Request | varchar(25) | ✓ |
| `expire_day` | จำนวนวันหมดอายุ | Expire Day | int | ✓ |
| `send_mail` | แจ้งส่งทาง อีเมล์ | Warning Email | smallint | ✓ |
| `send_sms` | แจ้งส่งทาง SMS | Warning SMS | smallint | ✓ |
| `doc_ref_trans` | อ้างอิงเอกสาร | Ref | varchar(25) | ✓ |
| `doc_ref_requisition` | เลขที่ใบเบิก *(resource only)* | Ref Requisition No | char |  |
| `condition_pack_1` | แยกตามหน่วยนับ *(resource only)* | Pack | char |  |
| `doc_ref_check_stock` | เลขที่ใบขอตรวจนับ *(resource only)* |  | char |  |
| `doc_ref_transfer_out` | เลขที่ใบโอนออก *(resource only)* |  | char |  |
| `zero_vat` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `exc_vat` | ยกเว้นภาษี *(resource only)* |  | char |  |
| `normal_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `exclude_vat` | ภาษีแยกนอก *(resource only)* |  | char |  |
| `include_vat` | ภาษีรวมใน *(resource only)* |  | char |  |
| `credit_date` | วันที่ครบกำหนด |  | smalldatetime | ✓ |
| `ownreceive` | รับเอง *(resource only)* |  | char |  |
| `sendto` | ส่งให้ *(resource only)* |  | char |  |
| `total_before_vat` | ยอดก่อนภาษี |  | float | ✓ |
| `credit_purchase` | ซื้อสินค้าเงินเชื่อ *(resource only)* |  | char |  |
| `cash_purchase` | ซื้อสินค้าเงินสด *(resource only)* |  | char |  |
| `credit_purchase_service` | ซื้อสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_purchase_service` | ซื้อสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_purchase_other` | ค่าใช้จ่ายเงินเชื่อ *(resource only)* |  | char |  |
| `cash_purchase_other` | ค่าใช้จ่ายเงินสด *(resource only)* |  | char |  |
| `credit_purchase_service_other` | ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_purchase_service_other` | ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_sale` | ขายเงินเชื่อ *(resource only)* |  | char |  |
| `cash_sale` | ขายเงินสด *(resource only)* |  | char |  |
| `credit_sale_service` | ขายสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_sale_service` | ขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `credit_sale_other` | รายได้เงินเชื่อ *(resource only)* |  | char |  |
| `cash_sale_other` | รายได้เงินสด *(resource only)* |  | char |  |
| `credit_sale_service_other` | รายได้เงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `cash_sale_service_other` | รายได้เงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `job_code` | งาน | Job | varchar(25) | ✓ |
| `delivery_date` | วันที่ส่งของ | Date of delivery | smalldatetime | ✓ |
| `deposit_no` | เลขที่ใบจ่ายเงินล่วงหน้า *(resource only)* | Deposit No | varchar(25) |  |
| `pay_amount` | เงินชำระ | Pay amount | float | ✓ |
| `money` | จำนวนเงินคืน | Money | float | ✓ |
| `sum_pay_money_cash` | รับ/จ่ายชำระหนี้ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq` | รับ/จ่ายชำระหนี้ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit` | รับ/จ่ายชำระหนี้ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer` | รับ/จ่ายชำระหนี้ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_cash_in` | รับชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_in` | รับชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_in` | รับชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_in` | รับชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_cash_out` | จ่ายชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_out` | จ่ายชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_out` | จ่ายชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_out` | จ่ายชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_diff` | ผลต่างยอดชำระ | Diff | float | ✓ |
| `ret_cash` | รับคืนจากขายเงินสด *(resource only)* |  | char |  |
| `ret_credit` | รับคืนจากขายเงินเชื่อ *(resource only)* |  | char |  |
| `ret_cash_1` | ลดหนี้จากขายเงินสด (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `ret_credit_1` | ลดหนี้จากขายเงินเชื่อ (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `ret_cash_service` | รับคืนจากขายสินค้าเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_service` | รับคืนจากขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_other` | ลดหนี้รายได้เงินเชื่อ *(resource only)* |  | char |  |
| `ret_cash_other` | ลดหนี้รายได้เงินสด *(resource only)* |  | char |  |
| `ret_cash_service_other` | ลดหนี้รายได้เงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `ret_credit_service_other` | ลดหนี้รายได้เงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_credit` | เพิ่มหนี้จากการขายเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_credit_1` | เพิ่มหนี้จากการขายเงินเชื่อ (ไม่กระทบสต๊อก) *(resource only)* |  | char |  |
| `invoice_add_credit_service` | เพิ่มหนี้จากการขายสินค้าเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_credit_other` | เพิ่มหนี้จากรายได้อื่นเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_credit_service_other` | เพิ่มหนี้จากรายได้อื่นเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `reduction_expense_other_credit` | ลดหนี้ค่าใช้จ่ายเงินเชื่อ *(resource only)* | Reduce debt Expenditures on credit | char |  |
| `reduction_expense_other_cash` | ลดหนี้ค่าใช้จ่ายเงินสด *(resource only)* | Reduce debt Cash expenditures | char |  |
| `reduction_expense_other_credit_service` | ลดหนี้ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* | Reduce debt Expenditures on credit (service) | char |  |
| `reduction_expense_other_cash_service` | ลดหนี้ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* | Reduce debt Cash expenditures (service) | char |  |
| `invoice_add_expense_other_credit` | เพิ่มหนี้ค่าใช้จ่ายเงินเชื่อ *(resource only)* |  | char |  |
| `invoice_add_expense_other_cash` | เพิ่มหนี้ค่าใช้จ่ายเงินสด *(resource only)* |  | char |  |
| `invoice_add_expense_other_credit_service` | เพิ่มหนี้ค่าใช้จ่ายเงินเชื่อ (สินค้าบริการ) *(resource only)* |  | char |  |
| `invoice_add_expense_other_cash_service` | เพิ่มหนี้ค่าใช้จ่ายเงินสด (สินค้าบริการ) *(resource only)* |  | char |  |
| `currency_money` | ยอดคงเหลือ(ตามสกุลเงิน) | Currency Money | float | ✓ |
| `total_debt_amount` | ยอดหนี้รวมภาษี | Total Debt Amount | float | ✓ |
| `sale_name` | ชื่อพนักงานขาย *(resource only)* | Sale Name | char |  |
| `buy_deposit` | เลขที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `buy_deposit2` | เลขที่ใบจ่ายมัดจำ *(resource only)* |  | char |  |
| `sell_deposit` | เลขที่ใบรับล่วงหน้า *(resource only)* |  | char |  |
| `sell_deposit2` | เลขที่ใบรับมัดจำ *(resource only)* |  | char |  |
| `pay_deposit_buy` | จำนวนจ่ายเงินล่วงหน้า *(resource only)* |  | char |  |
| `pay_deposit_buy2` | จำนวนเงินจ่ายมัดจำ *(resource only)* |  | char |  |
| `pay_deposit_sell` | จำนวนเงินรับล่วงหน้า *(resource only)* |  | char |  |
| `pay_deposit_sell2` | จำนวนเงินรับมัดจำ *(resource only)* |  | char |  |
| `deposit_buy` | จ่ายคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `deposit_buy2` | จ่ายคืนเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_sell` | รับคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `deposit_sell2` | รับคืนเงินมัดจำ *(resource only)* |  | char |  |
| `po_debt_balance` | ตั้งหนี้ยกมา *(resource only)* | OP Debt Balance | char |  |
| `po_cn_balance` | ลดหนี้ยกมา *(resource only)* | PO CN Balance | char |  |
| `po_purchase` | ซื้อสินค้า *(resource only)* | PO Purchase | char |  |
| `po_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | PO Addition Debt | char |  |
| `so_billing` | บิลขาย *(resource only)* | SO Billing | char |  |
| `so_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | SO Addition Debt | char |  |
| `so_debt_balance` | ตั้งหนี้ *(resource only)* | SO Debt Balance | char |  |
| `so_cn_balance` | ลดหนี้ *(resource only)* | SO CN Balance | char |  |
| `sale_type` | ประเภทการขาย *(resource only)* |  | char |  |
| `payable_add_type` | ประเภทการส่งคืน *(resource only)* |  | char |  |
| `payable_add_type_1` | เพิ่มหนี้เจ้าหนี้, เพิ่มสินค้า *(resource only)* |  | char |  |
| `payable_add_type_2` | เพิ่มหนี้เจ้าหนี้, ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `payable_sub_type_1` | ลดหนี้เจ้าหนี้, ลดสินค้า *(resource only)* |  | char |  |
| `payable_sub_type_2` | ลดหนี้เจ้าหนี้, ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `doc_no_po` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_date_po` | วันที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `cancel_type` | ประเภทการยกเลิก |  | int | ✓ |
| `cancel_type_1` | ยกเลิกทั้งหมด *(resource only)* |  | char |  |
| `cancel_type_2` | ยกเลิกรายสินค้า *(resource only)* |  | char |  |
| `last_status` | สถานะ |  | smallint | ✓ |
| `used_status` | มีการอ้างอิงแล้ว |  | smallint | ✓ |
| `doc_success` | สิ้นสุด |  | smallint | ✓ |
| `doc_advance_in_no` | เลขที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_in_date` | วันที่ใบจ่ายล่วงหน้า *(resource only)* |  | char |  |
| `doc_purchase_no` | เลขที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_purchase_date` | วันที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_purchase_debit_no` | ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_purchase_debit_date` | วันที่เพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_purchase_credit_no` | ใบลดหนี้ *(resource only)* |  | char |  |
| `doc_purchase_credit_date` | วันที่ลดหนี้ *(resource only)* |  | char |  |
| `doc_quotation_no` | ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_quotation_date` | วันที่ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_inquiry_no` | เลขที่ใบสั่งจอง *(resource only)* |  | char |  |
| `doc_inquiry_date` | วันที่ใบสั่งจอง *(resource only)* |  | char |  |
| `doc_saleorder_no` | เลขที่ใบสั่งขาย *(resource only)* |  | char |  |
| `doc_saleorder_date` | วันที่ใบสั่งขาย *(resource only)* |  | char |  |
| `doc_advance_so_no` | เลขที่ใบรับเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_date` | วันที่ใบรับเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_return_no` | เลขที่ใบคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_advance_so_return_date` | วันที่ใบคืนเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_invoice_no` | เลขที่ใบขายสินค้า/บริการ *(resource only)* |  | char |  |
| `doc_invoice_date` | วันที่ใบขายสินค้า/บริการ *(resource only)* |  | char |  |
| `doc_ar_debit_note_no` | เลขที่ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_ar_debit_note_date` | วันที่ใบเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_ar_credit_note_no` | เลขที่ใบลดหนี้ *(resource only)* |  | char |  |
| `doc_ar_credit_note_date` | วันที่ใบลดหนี้ *(resource only)* |  | char |  |
| `sale_add_type` | ประเภทการเพิ่มหนี้ *(resource only)* |  | char |  |
| `total_manual` | บันทึกยอดรวมเอง |  | smallint | ✓ |
| `total_after_discount` | มูลค่าหลังหักส่วนลด *(resource only)* |  | char |  |
| `cust_name` | ชื่อลูกหนี้/เจ้าหนี้ *(resource only)* |  | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `sum_total` | ยอดรวม *(resource only)* |  | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* |  | char |  |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `tab_more` | เพิ่มเติม *(resource only)* |  | char |  |
| `on_hold` | ระงับชั่วคราว |  | smallint | ✓ |
| `extra_word` | ข้อความเพิ่มเติม |  | varchar(100) | ✓ |
| `transport_code` | ขนส่งโดย |  | varchar(25) | ✓ |
| `purchase_name` | ผู้สั่งซื้อ *(resource only)* |  | char |  |
| `tab_pay_out` | รายละเอียดการจ่ายเงิน *(resource only)* |  | char |  |
| `tab_pay_in` | รายละเอียดการรับเงิน *(resource only)* |  | char |  |
| `want_day` | ต้องการภายใน (วัน) |  | smallint | ✓ |
| `want_date` | ต้องการภายใน (วันที่) |  | smalldatetime | ✓ |
| `deposit_day` | ระยะเวลาภายใน (วัน) |  | smallint | ✓ |
| `deposit_date` | ระยะเวลาภายใน (วันที่) |  | smalldatetime | ✓ |
| `remark2` | หมายเหตุ *(resource only)* |  | char |  |
| `tab_wht_in` | ภาษีหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `tab_wht_out` | ภาษีถูกหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `tab_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `sale_group` | กลุ่มพนักงานขาย |  | varchar(25) | ✓ |
| `doc_po_request` | เลขที่ใบเสนอซื้อ *(resource only)* |  | char |  |
| `not_approve_1` | ไม่อนุมัติ |  | smallint | ✓ |
| `user_approve` | ผู้อนุมัติ |  | varchar(25) | ✓ |
| `user_cancel` | ผู้ยกเลิก *(resource only)* |  | char |  |
| `sale_return_type` | ประเภทการรับคืน *(resource only)* |  | char |  |
| `approve_status` | สถานะการอนุมัติ |  | smallint | ✓ |
| `expire_status` | สถานะหมดอายุ |  | smallint | ✓ |
| `sum_pay_rounding` | ปัดเศษ *(resource only)* |  | char |  |
| `sum_petty_cash` | เงินสดย่อย *(resource only)* |  | char |  |
| `sum_deposit` | เงินรับล่วงหน้า *(resource only)* |  | char |  |
| `sum_advance` | เงินมัดจำ *(resource only)* |  | float |  |
| `sum_used` | ยอดเงินนำไปใช้ *(resource only)* |  | char |  |
| `advance_amount` | ตัดเงินมัดจำ |  | float | ✓ |
| `tab_advance` | เงินมัดจำ *(resource only)* |  | char |  |
| `doc_ref_name_1` | เลขที่ใบรับคืนจ่ายเงินล่วงหน้า *(resource only)* |  | char |  |
| `doc_ref_name_2` | เลขที่ใบรับคืนเงินมัดจำ *(resource only)* |  | char |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `tab_pay` | รายละเอียดการจ่าย *(resource only)* |  | char |  |
| `tab_wht` | ภาษีหัก ณ. ที่จ่าย *(resource only)* |  | char |  |
| `used_status_2` | สถานะ 2 |  | smallint | ✓ |
| `remark_2` | หมายเหตุ 2 |  | varchar(255) | ✓ |
| `remark_3` | หมายเหตุ 3 |  | varchar(255) | ✓ |
| `return_type` | ประเภทการลดหนี้ *(resource only)* |  | char |  |
| `ref_amount` | มูลค่าเอกสารเดิม |  | float | ✓ |
| `ref_new_amount` | มูลค่าที่ถูกต้อง |  | float | ✓ |
| `ref_diff` | ผลต่าง |  | float | ✓ |
| `sum_point` | แต้ม |  | float | ✓ |
| `cashier_code` | Cashier |  | varchar(25) | ✓ |
| `is_pos` | จากระบบ POS |  | smallint | ✓ |
| `pos_id` | หมายเลขเครื่อง POS |  | varchar(25) | ✓ |
| `member_code` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `doc_no_guid` | เลขที่เอกสารเปรียบเทียบ |  | varchar(25) | ✓ |
| `pos_bill_type` | 0=อย่างย่อ,1=อย่างเต็ม |  | smallint | ✓ |
| `pos_bill_change` | 0=ปรกติ,1=ใบแทน |  | smallint | ✓ |
| `doc_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `doc_type_purchase` | ซื้อสินค้า *(resource only)* |  | char |  |
| `doc_type_finish_good` | รับสินค้าสำเร็จรูป *(resource only)* |  | char |  |
| `wh_in_1` | รับจากใบสั่งซื้อ *(resource only)* |  | char |  |
| `wh_in_2` | รับจากการซื้อ *(resource only)* |  | char |  |
| `wh_in_3` | รับจากการเพิ่มหนี้ *(resource only)* |  | char |  |
| `wh_in` | ประเภทเอกสารรับ *(resource only)* |  | char |  |
| `wh_out_1` | ส่งคืนจากใบรับสินค้า (คลัง) *(resource only)* |  | char |  |
| `wh_out_2` | ส่งคืนจากใบส่งคืน (บัญชี) *(resource only)* |  | char |  |
| `wh_out_3` | ส่งคืนจากใบลดหนี้ (บัญชี) *(resource only)* |  | char |  |
| `wh_out` | ประเภทเอกสารออก *(resource only)* |  | char |  |
| `wh_in_4` | รับสินค้าสำเร็จรูป *(resource only)* |  | char |  |
| `wh_in_5` | รับคืนวัตถุดิบ *(resource only)* |  | char |  |
| `recheck_count_day` | เตือนย้อนหลัง (วัน) |  | float | ✓ |
| `recheck_count` | เปิดระบบเตือนตรวจนับซ้ำ |  | smallint | ✓ |
| `wh_from` | คลัง |  | varchar(25) | ✓ |
| `location_from` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `wh_to` | คลังปลายทาง |  | varchar(25) | ✓ |
| `location_to` | ที่เก็บปลายทาง |  | varchar(25) | ✓ |
| `auto_create` | สร้างโดยโปรแกรม |  | smallint | ✓ |
| `payable_sub_type_1_1` | ส่งคืนสินค้า *(resource only)* |  | char |  |
| `payable_sub_type_1_2` | ราคาผิด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `payable_sub_type_3` | ส่งคืนเงินสด *(resource only)* |  | char |  |
| `payable_sub_type_4` | ราคาผิดเงินสด (ไม่มีผลกับสต๊อกสินค้า) *(resource only)* |  | char |  |
| `invoice_add_cash_other` | เพิ่มหนี้รายได้อื่นๆ เงินสด *(resource only)* |  | char |  |
| `invoice_add_cash_service_other` | เพิ่มหนี้รายได้อื่นๆเงินสด (ค่าบริการ) *(resource only)* |  | char |  |
| `total_dept_amount` | ยอดตั้งหนี้ *(resource only)* |  | char |  |
| `debt_reduction_amount` | ยอดลดหนี้ *(resource only)* |  | char |  |
| `increase_the_debt_amount` | ยอดเพิ่มหนี้ *(resource only)* |  | char |  |
| `pay_debt_amount` | ยอดจ่ายชำระ *(resource only)* |  | char |  |
| `due_day_over` | เกินกำหนด *(resource only)* |  | char |  |
| `send_to_pick_and_pack` | สั่งจัดสินค้า |  | smallint | ✓ |
| `tab_gl` | GL *(resource only)* | GL | char |  |
| `cust_name_en` | ชื่อลูกค้า (อังกฤษ) *(resource only)* |  | char |  |
| `service_charge_word` | Service Charge |  | varchar(25) | ✓ |
| `total_service_charge` | มูลค่า Service Charge |  | float | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(255) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `deposit_doc` | เลขที่ใบรับเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_doc_date` | วันที่ใบรับเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_return_doc` | เลขที่ใบคืนเงินมัดจำ *(resource only)* |  | char |  |
| `deposit_return_doc_date` | วันที่ใบคืนเงินมัดจำ *(resource only)* |  | char |  |
| `table_number` | หมายเลขโต๊ะ |  | varchar(25) | ✓ |
| `period_guid` | GUID กะ |  | varchar(50) | ✓ |
| `branch_code_to` | ถึงสาขา | To Branch | varchar(25) | ✓ |
| `allocate_code_to` | ถึงการจัดสรร |  | varchar(25) | ✓ |
| `project_code_to` | ถึงโครงการ |  | varchar(25) | ✓ |
| `job_code_to` | ถึงงาน |  | varchar(25) | ✓ |
| `side_code_to` | ถึงฝ่าย |  | varchar(25) | ✓ |
| `department_code_to` | ถึงแผนก |  | varchar(25) | ✓ |
| `point_telephone` | หมายเลขโทรศัพท์ |  | varchar(25) | ✓ |
| `sum_point_2` | ยอดแต้มสะสมระบบกลาง |  | float | ✓ |
| `tab_shipment` | การจัดส่ง *(resource only)* |  | char |  |
| `remark_4` | หมายเหตุ 4 |  | varchar(255) | ✓ |
| `remark_5` | หมายเหตุ 5 |  | varchar(255) | ✓ |
| `tab_vat_buy` | ภาษีซื้อ *(resource only)* |  | char |  |
| `tab_vat_sale` | ภาษีขาย *(resource only)* |  | char |  |
| `is_manual_vat` | บันทึกรายการภาษีเอง |  | smallint | ✓ |
| `pass_book_code` | สมุดเงินฝาก |  | varchar(25) | ✓ |
| `total_amount_2` | มูลค่าสุทธิ(สกุลเงิน) |  | float | ✓ |
| `sender_code` | พนักงานขนส่ง |  | varchar(25) | ✓ |
| `is_cancel` | เอกสารยกเลิก |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิกเอกสาร |  | varchar(255) | ✓ |
| `cancel_datetime` | เวลายกเลิกเอกสาร |  | datetime | ✓ |
| `deposit_payment_cash` | จ่ายมัดจำเงินสด *(resource only)* |  | char |  |
| `deposit_payment_credit` | จ่ายมัดจำเงินเชื่อ *(resource only)* |  | char |  |
| `user_request_transfer` | ผู้ขอโอน *(resource only)* |  | char |  |
| `is_hold` | ระงับเอกสาร |  | smallint | ✓ |
| `auto_approved` | อนุมัติโดยอัตโนมัติ |  | smallint | ✓ |
| `pos_transfer` | โอนมาจากPOS |  | smallint | ✓ |
| `doc_close` | ปิดเอกสาร |  | smallint | ✓ |
| `ref_doc_type` | ประเภทเอกสาร |  | varchar(50) | ✓ |
| `is_arm` | ARM *(resource only)* | ARM | char |  |
| `adjust_normal` | ปรับปรุงสินค้า *(resource only)* |  | char |  |
| `adjust_stock_balance` | ปรับปรุงยกมาสินค้า *(resource only)* |  | char |  |
| `adjust_end_product` | ปรับปรุงปิดสินค้า *(resource only)* |  | char |  |
| `is_doc_copy` | เป็นเอกสารที่ออกแทน |  | smallint | ✓ |
| `doc_reason` | เหตุผล |  | varchar(500) | ✓ |
| `cn_reason` | เหตุผลการลดหนี้ *(resource only)* |  | char |  |
| `dn_reason` | เหตุผลการเพิ่มหนี้ *(resource only)* |  | char |  |
| `no_tax` | ไม่กระทบภาษี *(resource only)* |  | char |  |
| `doc_format_code_adjust` | รหัสเอกสารปรับปรุงเพิ่ม *(resource only)* |  | char |  |
| `deposit_balance` | เงินมัดจำคงเหลือ *(resource only)* |  | char |  |
| `discount_word_2` | ส่วนลด(สกุลเงิน) |  | varchar(50) | ✓ |
| `total_discount_2` | มูลค่าส่วนลด(สกุลเงิน) |  | float | ✓ |
| `total_value_2` | มูลค่าสินค้า(สกุลเงิน) |  | float | ✓ |
| `total_amout_old` | มูลค่าสุทธิเดิม |  | float | ✓ |
| `lost_profit_exchange_amount` | ผลต่างจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `expense` | ค่าใช้จ่าย *(resource only)* |  | char |  |
| `inquiry_type_product` | สินค้า *(resource only)* |  | char |  |
| `inquiry_type_service` | บริการ *(resource only)* |  | char |  |
| `delivery_on` | วันที่สินค้าถึงร้าน *(resource only)* |  | char |  |
| `total_cheque_amount` | รวมมูลค่าเช็ค *(resource only)* |  | char |  |
| `doc_copy_reason_type` | ประเภทการออกเอกสารแทน |  | smallint | ✓ |
| `bank_code` | ธนาคาร *(resource only)* |  | char |  |
| `bank_branch` | สาขาธนาคาร *(resource only)* |  | char |  |
| `is_lab_cut` | บันทึกการตัด Lab *(resource only)* |  | char |  |

index: `ic_trans_IC_TRANS_PK_PRIMARY`(doc_no,trans_flag), `PK_ic_trans_last_status`(last_status), `PK_ic_trans_used_status`(used_status), `ic_trans_cust_code`(cust_code), `ic_trans_total_amount`(total_amount), `PK_used_status_2`(used_status_2), `ic_trans_doc_success`(doc_success), `ic_trans_trans_flag`(trans_flag), `ic_trans_not_approve_1`(not_approve_1), `ic_trans_on_hold`(on_hold), `ic_trans_approve_status`(approve_status), `ic_trans_is_pos`(is_pos), `ic_trans_pos_bill_type`(pos_bill_type), `ic_trans_pos_bill_change`(pos_bill_change), `ic_trans_auto_create`(auto_create), `ic_trans_advance_amount`(advance_amount), `ic_trans_advance_pos_id`(pos_id), `ic_trans_due_date`(due_date), `ic_trans_due_date_trans_type`(trans_type), `ic_trans_doc_ref`(doc_ref), `ic_trans_expire_date`(expire_date), `ic_trans_expire_status`(expire_status), `ic_trans_cancel_type`(cancel_type), `ic_trans_doc_time`(doc_time), `ic_trans_cashier_code`(cashier_code), `ic_trans_doc_format_code`(doc_format_code), `ic_trans_doc_ref_cancel_type_idx`(doc_ref,trans_flag,cancel_type), `ic_trans_guid_code_idx`(guid_code), `ic_trans_used_status_trans_flag_doc_no_idx`(used_status,trans_flag,doc_no)

## ic_trans_additional

**รายละเอียดเพิ่มเติมรายวัน** — IC Trans Addtitional

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `deliveryday` | DeliveryDay |  | varchar(10) | ✓ |
| `ssfquantity` | SSFQuantity |  | varchar(10) | ✓ |
| `cust_id` | Cust_ID |  | varchar(25) | ✓ |
| `custcode` | CustCode |  | varchar(25) | ✓ |
| `web_order_id` | web_order_id |  | varchar(25) | ✓ |
| `district1_name` | District1_Name |  | varchar(255) | ✓ |
| `district2_name` | District2_Name |  | varchar(255) | ✓ |
| `province_name` | Province_Name |  | varchar(255) | ✓ |
| `custlat` | CustLat |  | float | ✓ |
| `custlng` | CustLng |  | float | ✓ |
| `custemail` | CustEmail |  | varchar(255) | ✓ |
| `custbusinesstel` | CustBusinessTel |  | varchar(100) | ✓ |
| `custmobile` | CustMobile |  | varchar(100) | ✓ |
| `orderdetail` | OrderDetail |  | varchar(255) | ✓ |
| `ordertype` | OrderType |  | varchar(10) | ✓ |
| `firstorder` | FirstOrder |  | varchar(10) | ✓ |
| `orderpaymenttype` | OrderPaymentType |  | varchar(10) | ✓ |
| `deliveryaddressid` | DeliveryAddressID |  | varchar(50) | ✓ |
| `orderdeliverydate` | OrderDeliveryDate |  | datetime | ✓ |
| `custrefcode` | CustRefCode |  | varchar(25) | ✓ |
| `paymentdate` | PayMentDate |  | datetime | ✓ |
| `orderdate` | OrderDate |  | datetime | ✓ |

## ic_trans_detail

**รายละเอียดรายวัน** — IC - Transection Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `cust_code` | ลูกหนี้/เจ้าหนี้ | AP/AR Code | varchar(25) | ✓ |
| `inquiry_type` | ประเภทการซื้อ | Inquiry Type | smallint | ✓ |
| `item_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `item_name` | ชื่อสินค้า | Item Name | varchar(255) | ✓ |
| `unit_code` | หน่วยนับ | Unit | varchar(25) | ✓ |
| `cost` | ต้นทุน *(resource only)* | Cost | float |  |
| `qty` | จำนวน | Qty | float | ✓ |
| `price` | ราคา | Price | float | ✓ |
| `discount` | ส่วนลด | Discount | varchar(25) | ✓ |
| `sum_of_cost` | รวมต้นทุน | Sum of Cost | float | ✓ |
| `sum_amount` | รวมมูลค่า | Sum Amount | float | ✓ |
| `due_date` | วันที่ต้องการ | Due Date | smalldatetime | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |
| `ref_doc_no` | อ้างอิง | Ref Doc No | varchar(25) | ✓ |
| `ref_doc_date` | อ้างอิง วันที่ | Ref Date | smalldatetime | ✓ |
| `ref_line_number` | อ้างอิง บรรทัด | Ref Line Number | int | ✓ |
| `ref_cust_code` | อ้างอิง เจ้าหนี้/ลูกหนี้ | Ref Cust Code | varchar(25) | ✓ |
| `branch_code` | สาขา | Branch Code | varchar(25) | ✓ |
| `wh_code` | คลัง | Warehouse | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ | Shelf | varchar(25) | ✓ |
| `wh_code_2` | คลัง | Warehouse | varchar(25) | ✓ |
| `shelf_code_2` | พื้นที่เก็บ | Shelf | varchar(25) | ✓ |
| `department_code` | แผนกที่ขออนุมัติ | Department Code | varchar(25) | ✓ |
| `approval_qty` | จำนวนอนุมัติ *(resource only)* | Approval Qty | float |  |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `cancel_qty` | จำนวนยกเลิก | Cancel Qty | float | ✓ |
| `total_qty` | จำนวนคงเหลือ | Total Qty | float | ✓ |
| `stand_value` | ตัวตั้ง | Stand Value | float | ✓ |
| `divide_value` | ตัวหาร | Divide Value | float | ✓ |
| `ratio` | อัตราส่วน | Ratio | float | ✓ |
| `dimension` | มิติ *(resource only)* | Dime | char |  |
| `ic_pattern` | รูปแบบสินค้า | Pattern | varchar(25) | ✓ |
| `ic_color` | สีสินค้า | Color | varchar(25) | ✓ |
| `ic_size` | ขนาดสินค้า | Size | varchar(25) | ✓ |
| `approval_unit` | หน่วยนับที่ใช้ *(resource only)* | Unit Use | varchar(25) |  |
| `extra` | เพิ่มเติม *(resource only)* | Extra | char |  |
| `priority_level` | ความสำคัญ | Priority | int | ✓ |
| `priority_level_1` | ปรกติ *(resource only)* | Normal | char |  |
| `priority_level_2` | ด่วน *(resource only)* | Level 1 | char |  |
| `priority_level_3` | ด่วนมาก *(resource only)* | Level 2 | char |  |
| `priority_level_4` | ด่วนมากพิเศษ *(resource only)* | Level 3 | char |  |
| `check_stock_1` | ยอดที่ตรวจนับได้ *(resource only)* |  | char |  |
| `check_stock_2` | ผลต่าง *(resource only)* |  | char |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* |  | char |  |
| `wh_name` | ชื่อคลัง *(resource only)* |  | char |  |
| `shelf_name` | ชื่อพื้นที่เก็บ *(resource only)* |  | char |  |
| `unit_type` | ประเภทหน่วยนับ *(resource only)* |  | char |  |
| `calc_flag` | บวกหรือลบ (1=บวก,-1=ลบ) |  | int | ✓ |
| `last_status` | สถานะล่าสุด (0=Normal,1=ยกเลิก) |  | int | ✓ |
| `wh_name_out` | จากคลัง *(resource only)* |  | char |  |
| `shelf_name_out` | จากที่เก็บ *(resource only)* |  | char |  |
| `wh_name_in` | เข้าคลัง *(resource only)* |  | char |  |
| `shelf_name_in` | เข้าที่เก็บ *(resource only)* |  | char |  |
| `doc_ref_requisition` | เลขที่ใบเบิก *(resource only)* |  | char |  |
| `wh_name_2` | ชื่อคลัง *(resource only)* |  | char |  |
| `shelf_name_2` | ชื่อพื้นที่เก็บ *(resource only)* |  | char |  |
| `set_ref_line` | บรรทัดอ้างอิง (สินค้าชุด) |  | varchar(40) | ✓ |
| `set_ref_price` | ราคาอ้างอิง (สินค้าชุด) |  | float | ✓ |
| `set_ref_qty` | จำนวนอ้างอิง (สินค้าชุด) |  | float | ✓ |
| `item_type` | ประเภทสินค้า |  | int | ✓ |
| `doc_ref_purchase_order` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_sale_order` | เลขที่ใบเสนอราคา *(resource only)* |  | char |  |
| `vat_type` | ประเภทภาษี (0=แยกนอก,1=รวมใน,2=อัตรา 0) |  | int | ✓ |
| `doc_ref_purchase` | เลขที่ใบซื้อสินค้า/สินค้าบริการ *(resource only)* |  | char |  |
| `doc_ref_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `item_code_main` | สินค้าหลัก |  | varchar(25) | ✓ |
| `ref_row` | ref_row |  | smallint | ✓ |
| `ref_guid` | ref_guid |  | varchar(40) | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `is_permium` | 1=ของแถม |  | smallint | ✓ |
| `is_get_price` | ให้ดึงราคาขาย (1=ดึง) |  | smallint | ✓ |
| `average_cost` | ราคาทุนเฉลี่ย |  | float | ✓ |
| `sum_amount_exclude_vat` | รวมมูลค่า |  | float | ✓ |
| `doc_date_calc` | วันที่สำหรับคำนวณ |  | smalldatetime | ✓ |
| `doc_time_calc` | เวลาสำหรับคำนวณ |  | varchar(5) | ✓ |
| `profit` | กำไรขั้นต้น *(resource only)* |  | char |  |
| `discount_amount` | มูลค่าส่วนลด |  | float | ✓ |
| `price_exclude_vat` | ราคาไม่รวมภาษี |  | float | ✓ |
| `ar_detail` | รายละเอียดลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `ap_detail` | รายละเอียดเจ้าหนี้ *(resource only)* |  | char |  |
| `vat_type_word` | ประเภทภาษี *(resource only)* |  | char |  |
| `user_approve` | รหัสผู้อนุมัติ |  | varchar(25) | ✓ |
| `price_type` | ประเภทราคา |  | smallint | ✓ |
| `price_mode` | กลุ่มราคา |  | smallint | ✓ |
| `approval_price` | ราคาอนุมัติ *(resource only)* |  | float |  |
| `temp_float_1` | ตัวเลข 1 |  | float | ✓ |
| `temp_float_2` | ตัวเลข 2 |  | float | ✓ |
| `temp_string_1` | ตัวอักษร 1 |  | varchar(25) | ✓ |
| `po_qty` | จำนวนสั่งซื้อ *(resource only)* |  | char |  |
| `po_qty_2` | จำนวนสั่งซื้อคงเหลือ *(resource only)* |  | char |  |
| `doc_ref_receive_no` | เลขที่ใบรับ *(resource only)* |  | char |  |
| `approval_sum_amount` | มูลค่าอนุมัติ *(resource only)* |  | char |  |
| `approval_discount` | ส่วนลดอนุมัติ *(resource only)* |  | char |  |
| `expense_code` | รหัสค่าใช้จ่าย *(resource only)* |  | char |  |
| `expense_name` | ชื่อค่าใช้จ่าย *(resource only)* |  | char |  |
| `detail` | คำอธิบายรายการ *(resource only)* |  | char |  |
| `amount2` | จำนวนเงิน *(resource only)* |  | char |  |
| `average_cost_stand` | หน่วยต้นทุนตัวตั้ง *(resource only)* |  | char |  |
| `average_cost_div` | หน่วยต้นทุนตัวหาร *(resource only)* |  | char |  |
| `serial_number` | หมายเลขเครื่อง *(resource only)* |  | char |  |
| `income_code` | รหัสรายได้ *(resource only)* |  | char |  |
| `income_name` | ชื่อรายได้ *(resource only)* |  | char |  |
| `is_serial_number` | มีหมายเลขเครื่อง |  | smallint | ✓ |
| `cash_sub_code` | รหัสเงินสดย่อย *(resource only)* |  | char |  |
| `cash_sub_name` | ชื่อเงินสดย่อย *(resource only)* |  | char |  |
| `book_bank_code` | สมุดเงินฝาก *(resource only)* |  | char(25) |  |
| `bank_name` | ธนาคาร |  | varchar(25) | ✓ |
| `bank_branch` | สาขา |  | varchar(25) | ✓ |
| `chq_number` | เลขที่เช็ค |  | varchar(100) | ✓ |
| `chq_flag` | สถานะ *(resource only)* |  | smallint |  |
| `expense` | ค่าใช้จ่าย *(resource only)* |  | char |  |
| `credit_card_no` | เลขที่บัตรเครดิต *(resource only)* |  | char |  |
| `barcode` | Barcode |  | varchar(25) | ✓ |
| `discount_number` | หมายเลขส่วนลด |  | smallint | ✓ |
| `price_changed` | มีการแก้ไขราคา |  | smallint | ✓ |
| `discount_changed` | มีการแก้ไขส่วนลด |  | smallint | ✓ |
| `price_default` | ราคาเริ่มต้น |  | float | ✓ |
| `tax_type` | ประเภทภาษี (0=มีภาษี,1=ยกเว้น) |  | smallint | ✓ |
| `is_pos` | จาก POS |  | smallint | ✓ |
| `auto_create` | สร้างโดยโปรแกรม |  | smallint | ✓ |
| `date_expire` | หมดอายุ |  | smalldatetime | ✓ |
| `hidden_cost_1` | ต้นทุนแฝงบริหาร |  | float | ✓ |
| `hidden_cost_1_exclude_vat` | ต้นทุนแฝงบริหารไม่รวมภาษี |  | float | ✓ |
| `hidden_cost_2` | ต้นทุนแฝงบัญชี |  | float | ✓ |
| `hidden_cost_2_exclude_vat` | ต้นทุนแฝงบัญชีไม่รวมภาษี |  | float | ✓ |
| `sum_of_cost_1` | ต้นทุนรวมต้นทุนแฝงบริหาร |  | float | ✓ |
| `hidden_cost_1_name_1` | ทุนแฝง *(resource only)* |  | char |  |
| `average_cost_1` | ราคาทุนเฉลี่ยแฝง |  | float | ✓ |
| `hidden_cost_1_name_2` | รายได้แฝง *(resource only)* |  | char |  |
| `doc_ref_partial` | ใบรับสินค้า *(resource only)* |  | char |  |
| `sale_code` | รหัสพนักงานขาย |  | varchar(25) | ✓ |
| `sale_group` | กลุ่มพนักงานขาย |  | varchar(25) | ✓ |
| `date_due` | วันครบกำหนด |  | datetime | ✓ |
| `lot_number_1` | เลข LOT |  | varchar(50) | ✓ |
| `item_name_en` | ชื่อสินค้า (อังกฤษ) *(resource only)* |  | char |  |
| `unit_name_en` | หน่วยนับ (อังกฤษ) *(resource only)* |  | char |  |
| `item_code_2` | รหัสสินค้า |  | varchar(25) | ✓ |
| `book_bank_code_out` | จากสมุดเงินฝาก *(resource only)* |  | char |  |
| `book_bank_code_in` | เข้าสมุดเงินฝาก *(resource only)* |  | char |  |
| `bank_name_2` | ธนาคาร |  | varchar(25) | ✓ |
| `bank_branch_2` | สาขา |  | varchar(25) | ✓ |
| `use_expire` | ใช้ระบบวันหมดอายุ *(resource only)* |  | char |  |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `price_base` | ราคากลาง |  | float | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `fee_amount` | ค่าธรรมเนียม |  | float | ✓ |
| `transfer_amount` | ยอดโอนเงิน |  | float | ✓ |
| `price_set_ratio` | อัตราส่วนราคาสินค้าชุด |  | float | ✓ |
| `print_qty` | จำนวนพิมพ์ *(resource only)* |  | char |  |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |
| `mfn_code` | รหัสผู้ผลิต |  | varchar(50) | ✓ |
| `mfn_name` | ผู้ผลิต |  | varchar(255) | ✓ |
| `start_qty` | จำนวนเริ่มต้น *(resource only)* |  | char |  |
| `end_qty` | จำนวนสินสุด *(resource only)* |  | char |  |
| `department` | แผนก *(resource only)* |  | char |  |
| `allocate` | การจัดสรร *(resource only)* |  | char |  |
| `project` | โครงการ *(resource only)* |  | char |  |
| `price_2` | ราคา | Price | float | ✓ |
| `sum_amount_2` | รวมมูลค่า | Sum Amount | float | ✓ |
| `price_guid` | Price Guid |  | varchar(55) | ✓ |
| `discount_amount_2` | มูลค่าส่วนลด |  | float | ✓ |
| `is_lock_cost` | กำหนดต้นทุนเอง | Lock Cost | smallint | ✓ |
| `sum_of_cost_fix` | ต้นทุน |  | float | ✓ |
| `profit_lost_cost_amount` | กำไรขาดทุน | Profit Lost Cost Amount | float | ✓ |
| `is_doc_copy` | เป็นเอกสารที่ออกแทน |  | smallint | ✓ |
| `bat_date` | bat date | bat date | smalldatetime | ✓ |
| `bat_number` | bat number | bat number | varchar(255) | ✓ |
| `product_year` | ปีที่ผลิต |  | varchar(10) | ✓ |
| `product_week` | สัปดาห์ที่ผลิต |  | varchar(10) | ✓ |
| `currency_code` | สกุลเงิน |  | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน |  | float | ✓ |
| `qty_2` | จำนวนขาย |  | float | ✓ |
| `unit_code_2` | หน่วยช่วยขาย |  | varchar(25) | ✓ |
| `total_size` | รวมหน่วยนับ 2 |  | float | ✓ |
| `unit_size` | ขนาดสินค้า |  | float | ✓ |
| `unit_name_2` | ชื่อหน่วยนับ 2 *(resource only)* |  | char |  |
| `exchange_rate_old` | อัตราแลกเปลี่ยนเดิม |  | float | ✓ |
| `total_packaging_qty` | จำนวน Packaging *(resource only)* |  | char |  |
| `promotion_code` | รหัสโปรโมชั่น |  | varchar(50) | ✓ |
| `lab_no` | Lab No. *(resource only)* |  | char |  |

index: `ic_trans_detail_trans_type`(trans_type), `ic_trans_detail_trans_flag`(trans_flag), `ic_trans_detail_cust_code`(cust_code), `ic_trans_detail_item_code`(item_code), `ic_trans_detail_doc_no`(doc_no), `ic_trans_detail_process_cost`(doc_date,doc_time,doc_no,line_number), `ic_trans_detail_last_status`(last_status), `ic_trans_detail_doc_date`(doc_date), `ic_trans_detail_doc_time`(doc_time), `ic_trans_detail_doc_date_and_time`(doc_date,doc_time), `ic_trans_detail_docno_trans_flag`(doc_no,trans_flag), `ic_trans_detail_process_cost_2`(doc_date_calc,doc_time_calc,trans_flag,doc_no,line_number), `ic_trans_detail_doc_date_and_time_2`(doc_date_calc,doc_time_calc), `ic_trans_detail_doc_date_2`(doc_date_calc), `ic_trans_detail_doc_time_2`(doc_time_calc), `ic_trans_detail_taxtype`(tax_type), `ic_trans_detail_icpos`(is_pos), `ic_trans_detail_barcode_1`(barcode), `ic_trans_detail_barcode_2`(barcode,cust_code), `ic_trans_detail_auto_create`(auto_create), `ic_trans_detail_stand_value`(stand_value), `ic_trans_detail_divide_value`(divide_value), `ic_trans_detail_item_type`(item_type), `ic_trans_detail_is_serial_number`(is_serial_number), `ic_trans_detail_vat_type`(vat_type), `ic_trans_detail_barcode_3`(barcode,cust_code,doc_date,doc_time), `ic_trans_detail_ref_doc_no`(ref_doc_no), `ic_trans_detail_inquiry_type`(inquiry_type), `ic_trans_detail_line_number`(line_number), `ic_trans_detail_whcode`(wh_code), `ic_trans_detail_selfcode`(shelf_code), `ic_trans_detail_whcode_shelfcode`(wh_code,shelf_code), `ic_trans_detail_unit_code`(unit_code), `ic_trans_detail_chq_number`(chq_number), `ic_trans_detail_doc_ref_idx`(doc_ref), `ic_trans_detail_chq_process_idx`(last_status,chq_number,trans_flag,doc_ref,ref_row), `ic_trans_detail_item_code_trans_flag_idx`(item_code,trans_flag), `ic_trans_detail_trans_flag_last_status`(trans_flag,last_status), `ic_trans_detail_ref_doc_no_trans_flag`(ref_doc_no,trans_flag), `ic_trans_detail_ref_row`(ref_row), `ic_trans_detail_sale_code`(sale_code), `ic_trans_detail_ref_doc_item_trans_flag_last_status`(ref_doc_no,item_code,trans_flag,last_status)

## ic_trans_detail_allocate

**รายละเอียดรายวันการจัดสรร**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | int |  |
| `allocate_code` | รหัสการจัดสรร |  | varchar(25) | ✓ |
| `allocate_name` | ชื่อการจัดสรร *(resource only)* |  | char |  |
| `ratio` | อัตราส่วน (%) |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | Line |  | int | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `ic_code` | รหัสหลัก |  | varchar(25) | ✓ |

## ic_trans_detail_department

**รายละเอียดรายวันแผนก**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `department_code` | รหัสแผนก |  | varchar(25) | ✓ |
| `department_name` | ชื่ีอแผนก *(resource only)* |  | char |  |
| `ratio` | อัตราส่วน (%) |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | Line |  | int | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `ic_code` | รหัสอ้างอิง |  | varchar(25) | ✓ |

## ic_trans_detail_jobs

**รายละเอียดรายวันงาน** — Table 335

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `job_code` | รหัสงาน |  | varchar(25) |  |
| `job_name` | ชื่องาน *(resource only)* |  | char |  |
| `ratio` | อัตราส่วน |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | Line |  | smallint | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `ic_code` | รหัสหลัก |  | varchar(25) | ✓ |

## ic_trans_detail_lot

**Table 237** — Table 237

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | รายวันระบบ |  | smallint | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | วันที่เอกสาร |  | datetime |  |
| `lot_number` | หมายเลข lot |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(25) |  |
| `qty` | จำนวน |  | float | ✓ |
| `price` | ราคา |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | บรรทัดที่ |  | smallint | ✓ |
| `wh_code` | warehouse |  | varchar(25) | ✓ |
| `shelf_code` | shelf |  | varchar(25) | ✓ |
| `calc_flag` | calc flag |  | smallint | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `expire_date` | วันหมดอายุ |  | smalldatetime | ✓ |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |
| `mfn_name` | ผู้ผลิต |  | varchar(255) | ✓ |
| `doc_line_number` | หมายเลขบรรทัดอ้างอิง |  | smallint | ✓ |
| `product_year` | ปีที่ผลิต |  | varchar(25) | ✓ |
| `product_week` | สัปดาห์ที่ผลิต |  | varchar(25) | ✓ |

index: `pk_lot_number`(lot_number), `PK_item_code_lot`(item_code,lot_number), `PK_doc_no`(doc_no)

## ic_trans_detail_project

**รายละเอียดรายวันโครงการ**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `project_code` | รหัสโครงการ |  | varchar(25) | ✓ |
| `project_name` | ชื่อโครงการ *(resource only)* |  | char |  |
| `ratio` | อัตราส่วน (%) |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | Line |  | int | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `ic_code` | รหัสหลัก |  | varchar(25) | ✓ |

## ic_trans_detail_promotion

**รายละเอียดโปรโมชั่น** — IC Trans Detail Promotion

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(25) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `doc_ref` | เอกสารอ้างอิง |  | varchar(25) | ✓ |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ |  | smalldatetime | ✓ |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `promotion_code` | รหัสโปรโมชั่น |  | varchar(25) |  |
| `promotion_name` | ชื่อโปรโมชั่น |  | varchar(255) |  |
| `qty` | จำนวน |  | float |  |
| `price` | ราคา |  | float |  |
| `sum_amount` | ยอดรวม |  | float |  |
| `line_number` | หมายเลขบรรทัด |  | smallint |  |

## ic_trans_detail_site

**รายละเอียดรายวันฝ่าย**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `site_code` | รหัสฝ่าย |  | varchar |  |
| `site_name` | ชื่อฝ่าย *(resource only)* |  | char |  |
| `ratio` | อัตราส่วน (%) |  | float | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `line_number` | Line |  | int | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `ic_code` | รหัสหลัก |  | varchar(25) | ✓ |

## ic_trans_pos_campaign

**Inventory Transaction POS Campaign** — Inventory Transaction POS Campaign

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `trans_flag` | ประเภทเอกสาร |  | smallint |  |
| `doc_date` | วันที่ |  | smalldatetime |  |
| `pos_id` | รหัสเครื่อง POS |  | varchar(50) | ✓ |
| `campaign_code` | รหัสแคมเปญ |  | varchar(50) |  |
| `qty` | จำนวนที่ได้รับ |  | int |  |
| `line_number` | Line Number |  | int | ✓ |

## ic_trans_resource

**รายละเอียดข้อความ** — Inventory Transfer Resource · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `from_doc_no` | จากเลขที่เอกสาร *(resource only)* | From Document No | char |  |
| `to_doc_no` | ถึงเลขที่เอกสาร *(resource only)* | To Document No | char |  |
| `from_doc_date` | จากวันที่เอกสาร *(resource only)* | From Document Date | char |  |
| `to_doc_date` | ถึงวันที่เอกสาร *(resource only)* | To Document Date | char |  |
| `from_cust_code` | จากรหัสเจ้าหนี้/ลูกหนี้ *(resource only)* | From Customer Code | char |  |
| `to_cust_code` | ถึงรหัสเจ้าหนี้/ลูกหนี้ *(resource only)* | To Customer Code | char |  |
| `from_department` | จากแผนก *(resource only)* | From Department | char |  |
| `to_department` | ถึงแผนก *(resource only)* | To Department | char |  |
| `from_item` | จากสินค้า *(resource only)* | From Item | char |  |
| `to_item` | ถึงสินค้า *(resource only)* | To Item | char |  |
| `doc_format_code` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `doc_format` | รูปแบบเลขที่เอกสาร *(resource only)* |  | char |  |

## ic_trans_serial_number

**serial number (รายวัน)** — Serial Number Result

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `serial_number` | หมายเลขเครื่อง | Serial Number | varchar(50) |  |
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `description` | รายละเอียด |  | varchar(255) | ✓ |
| `void_date` | วันที่หมดประกัน |  | datetime | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | ประเภท |  | int |  |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `line_number` | Line |  | int | ✓ |
| `doc_line_number` | Line |  | smallint | ✓ |
| `last_status` | status |  | smallint | ✓ |
| `doc_date` | วันที่ |  | smalldatetime | ✓ |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `calc_flag` | การคำนวณ |  | smallint | ✓ |
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `wh_code_2` | คลัง |  | varchar(25) | ✓ |
| `shelf_code_2` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `cust_name` | ชิ้อเจ้าหนี้/ลูกหนี้/ลูกค้า *(resource only)* |  | char |  |
| `price` | ราคาซื้อ/ขาย |  | float | ✓ |
| `cust_code` | รหัสเจ้าหนี้/ลูกหนี้/ลูกค้า |  | varchar(25) | ✓ |
| `inquiry_type` | inquiry_type |  | smallint | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `product_year` | ปี |  | varchar(4) | ✓ |
| `product_week` | สัปดาห์ |  | varchar(2) | ✓ |
| `car_inventory` | CarInventory |  | varchar(50) | ✓ |
| `car_stockno` | เลขสต๊อก |  | varchar(50) | ✓ |
| `car_engineno` | เลขเครื่อง |  | varchar(100) | ✓ |
| `car_chassisno` | เลขแชสซีส์ |  | varchar(100) | ✓ |

index: `idx_doc_no`(doc_no), `idx_serial_number`(serial_number), `idx_doc_date_time`(doc_date,doc_time), `idx_doc_date`(doc_date), `ic_trans_serial_number_wh_code`(wh_code), `ic_trans_serial_number_shelf`(shelf_code), `ic_trans_serial_number_ic_code`(ic_code), `ic_trans_serial_number_last_status`(last_status), `ic_trans_serial_number_cust_code`(cust_code), `ic_trans_serial_number_trans_flag`(trans_flag)

## ic_trans_shipment

**การจัดส่ง** — Table 342

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(25) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `transport_name` | ชื่อผู้รับ |  | varchar(255) | ✓ |
| `transport_address` | ที่อยู่ |  | varchar(1000) | ✓ |
| `transport_telephone` | โทรศัทพ์ |  | varchar(100) | ✓ |
| `transport_fax` | แฟกซ์ |  | varchar(100) | ✓ |
| `transport_tambon` | ตำบล |  | varchar(255) | ✓ |
| `transport_amper` | อำเภอ |  | varchar(255) | ✓ |
| `transport_province` | จังหวัด |  | varchar(255) | ✓ |
| `transport_country` | ประเทศ |  | varchar(255) | ✓ |
| `transport_code` | ประเภทขนส่ง |  | varchar(25) | ✓ |
| `destination` | ปลายทาง |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `remark_2` | หมายเหตุ 2 |  | varchar(255) | ✓ |
| `ship_code` | Ship Code |  | varchar(50) | ✓ |
| `logistic_area` | เขตการขนส่ง |  | varchar(50) | ✓ |
| `latitude` | ละติจูด | Latitude | float | ✓ |
| `longitude` | ลองจิจูด | Longitude | float | ✓ |
| `zipcode` | รหัสไปรษณีย์ | Zip Code | varchar(10) | ✓ |

index: `ic_trans_shipment_ic_trans_shipment_pk_doc_no_trans_flag`(doc_no,trans_flag), `ic_trans_shipment_cust_code_transport_name`(cust_code,transport_name)

## ic_weight_cost

**ต้นทุนแฝง** — Weight Cost · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Document Ref | varchar(25) | ✓ |
| `weight_by` | เฉลี่ยตาม | Weight By | smallint | ✓ |
| `bill_start` | จากบิลซื้อ | From Bill No | varchar(25) | ✓ |
| `bill_stop` | ถึงบิลซื้อ | To Bill No | varchar(25) | ✓ |
| `weight_method` | วิธีคิดต้นทุนแฝง | Weight Method | smallint | ✓ |
| `amount` | มูลค่า | Amount | float | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ic_weight_cost_PK_CODE`(doc_no)

## ic_weight_cost_detail

**รายละเอียดต้นทุนแฝง** — Weight Cost Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `bill_date` | วันที่บิลซื้อ | Bill Date | smalldatetime | ✓ |
| `bill_no` | เลขที่บิลซื้อ | Bill No | varchar(25) |  |
| `amount` | มูลค่าคำนวณได้ | Amount | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## take_order_temp

**take order** — Table 344

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `barcode` | Barcode |  | varchar(50) |  |
| `qty` | จำนวน |  | float |  |
| `price` | ราคา |  | float |  |
| `amount` | มูลค่า |  | float |  |
| `id` | ID |  | varchar(25) |  |
| `order_date` | Date |  | datetime | ✓ |
| `order_time` | Time |  | varchar(5) | ✓ |
| `remark` | Remark |  | varchar(500) | ✓ |

index: `take_order_temp_idx_1`(id), `take_order_temp_idx_2`(id,order_date,order_time)

