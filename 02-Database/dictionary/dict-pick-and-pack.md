---
tags: [sml, dictionary, pick-and-pack, generated]
module: Pick_and_Pack
---
# พจนานุกรม: Pick_and_Pack — Pick and Pack

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#pp_config]] | กำหนดเครื่องสำหรับคุมคลัง / Table 302 | 4 |
| [[#pp_plan]] | แผนการจัดสินค้า / Table 309 | 11 |
| [[#pp_plan_detail]] | แผนการจัดสินค้า (รายละเอียด) / Table 310 | 12 |
| [[#pp_shipment]] | การจัดส่งสินค้า / pp_shipment | 19 |
| [[#pp_shipment_detail]] | รายละเอียกการจัดส่ง / Shipment Detail | 10 |
| [[#pp_trans]] | รายการจัดสินค้า / pp_trans | 14 |
| [[#pp_trans_detail]] | รายละเอียด / pp_trans_detail | 10 |

## pp_config

**กำหนดเครื่องสำหรับคุมคลัง** — Table 302

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `serial_id` | หมายเลขเครื่อง |  | varchar(50) |  |
| `wh_code` | คลัง |  | varchar(25) |  |
| `location_list` | ที่เก็บ |  | varchar(500) | ✓ |
| `auto_mode` | ทำงานอัตโนมัติ |  | smallint | ✓ |

## pp_plan

**แผนการจัดสินค้า** — Table 309

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `ref_doc_no` | เลขที่เอกสารอ้างอิง |  | varchar(25) |  |
| `status` | สถานะ |  | smallint |  |
| `remark` | หมายเหตุ |  | varchar(255) |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `transport_destination_code` | รหัสสถานที่ส่ง |  | varchar(25) | ✓ |
| `transport_destination_detail` | สถานที่ส่ง *(resource only)* |  | varchar(100) |  |
| `priority` | ระดับความสำคัญ |  | smallint | ✓ |
| `doc_time` | เวลา |  | varchar(5) |  |

index: `pp_plan_PK_PRIMARY`(doc_no)

## pp_plan_detail

**แผนการจัดสินค้า (รายละเอียด)** — Table 310

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `row_number` | ลำดับที่ |  | smallint |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `wh_code` | คลัง |  | varchar(25) |  |
| `shelf_code` | ที่เก็บ |  | varchar(25) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวน |  | float |  |
| `transport_type` | วิธีรับมอบสินค้า |  | smallint | ✓ |
| `transport_date` | วันที่รับมอบ |  | smalldatetime | ✓ |
| `transport_time` | เวลา |  | varchar(5) | ✓ |
| `transport_destination_code` | สถานที่ส่ง *(resource only)* |  | varchar(25) |  |
| `priority` | ความสำคัญ |  | smallint | ✓ |

index: `pp_plan_detail_idx1`(doc_no)

## pp_shipment

**การจัดส่งสินค้า** — pp_shipment

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `trans_flag` | ประเภทรายการ |  | smallint |  |
| `doc_format_code` | ประเภทเอกสาร |  | varchar(25) | ✓ |
| `doc_ref` | เลขที่เอกสารอ้างอิง |  | varchar(25) | ✓ |
| `doc_ref_date` | วันที่เอกสารอ้างอิง |  | smalldatetime | ✓ |
| `transport_type` | ประเภทขนส่ง |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(500) | ✓ |
| `cust_code` | รหัสลูกค้า/ลูกหนี้ |  | varchar(25) | ✓ |
| `tab_description` | รายละเอียด *(resource only)* |  | char |  |
| `guid_code` | GUID | GUID | varchar(50) | ✓ |
| `tab_shipment_address` | รายละเอียดการจัดส่ง *(resource only)* |  | char |  |
| `tab_more` | เพิ่มเติม *(resource only)* |  | char |  |
| `is_cancel` | ยกเลิกเอกสาร |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิก |  | varchar(255) | ✓ |
| `cancel_datetime` | วันเวลายกเลิก |  | datetime | ✓ |
| `last_status` | สถานะเอกสาร |  | smallint | ✓ |
| `status` | สถานะ |  | smallint | ✓ |

index: `pp_shipment_pp_shipment_doc_no_trans_flag_pk`(doc_no,trans_flag)

## pp_shipment_detail

**รายละเอียกการจัดส่ง** — Shipment Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `trans_flag` | ประเภทรายกาย |  | smallint |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `doc_ref_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `item_code` | รหัส |  | varchar(50) | ✓ |
| `remark` | หมายเหตุ |  | varchar(50) | ✓ |
| `cust_code` | รหัสลูกค้า/ลูกหนี้ |  | varchar(500) | ✓ |
| `ref_doc_no` | เลขที่เอกสาร |  | varchar(50) | ✓ |
| `ref_doc_date` | เอกสารวันที่ |  | datetime | ✓ |

## pp_trans

**รายการจัดสินค้า** — pp_trans

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ | Doc No | varchar(25) |  |
| `doc_date` | เอกสารวันที่ | Doc Date | smalldatetime |  |
| `ref_code` | เอกสารอ้างอิงเลขที่ | Ref Code | varchar(25) |  |
| `ref_date` | เอกสารอ้างอิงวันที่ | Ref Date | smalldatetime |  |
| `due_date` | วันที่มารับ | Due Date | smalldatetime | ✓ |
| `cust_code` | รหัสลูกค้า | Customer Code | varchar(25) |  |
| `sale_code` | รหัสพนักงานขาย | Sale Code | varchar(25) | ✓ |
| `status` | สถานะ | Status | int | ✓ |
| `persent` | เปอร์เชน | Persent | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `row_number` | ลำดับที่ | Row Number | int | ✓ |
| `flag` | เลือก *(resource only)* | Flag | char |  |
| `is_cancel` | เอกสารยกเลิก |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิก |  | varchar(255) | ✓ |

index: `pp_trans_PK_PRIMARY`(doc_no)

## pp_trans_detail

**รายละเอียด** — pp_trans_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `row_number` | ลำดับที่ | Row Number | int |  |
| `doc_no` | เอกสารเลขที่ | Doc No | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) |  |
| `wh_code` | คลังสินค้า | WH Code | varchar(25) | ✓ |
| `shelf_code` | ที่เก็บสินค้า | Shelf Code | varchar(25) | ✓ |
| `unit_code` | หน่วยนับ | Unit Code | varchar(25) | ✓ |
| `qty` | จำนวน | QTY | float | ✓ |
| `event_qty` | จำนวนที่จัด | Even QTY | float(25) | ✓ |
| `event_date_time` | วันและเวลาที่ทำรายการ | Date And Time | smalldatetime | ✓ |
| `flag` | เลือก *(resource only)* | Flag | char | ✓ |

index: `pp_trans_detail_idx1`(doc_no), `pp_trans_detail_idx2`(ic_code)

