---
tags: [sml, dictionary, imex, generated]
module: IMEX
---
# พจนานุกรม: IMEX — IMEX (OEM)

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ic_cost_date]] | ic_cost_date / ic_cost_date | 5 |
| [[#ic_lot_manage]] | จัดการ LOT สินค้า / Inventory LOT Manage | 9 |
| [[#ic_qc_config]] | ic_qc_config / ic_qc_config | 12 |
| [[#ic_qc_container_adjust]] | ปรับจำนวน Container / ic_qc_container_adjust | 3 |
| [[#ic_qc_container_adjustment_detail]] | ic_qc_container_adjustment_detail / ic_qc_container_adjustment_detail | 10 |
| [[#ic_qc_container_transaction]] | QC Container Transaction  | 12 |
| [[#ic_qc_indentify]] | QC Indentify / QC Indentify | 4 |
| [[#ic_qc_lab]] | รายละเอียด Lab / Inventory Quality Lab | 27 |
| [[#ic_qc_lab_beginning_balance]] | Lab คงเหลือยกมา / Table 515 | 6 |
| [[#ic_qc_lab_beginning_balance_detail]] | รายละเอียด Lab ยกมา / Table 516 | 7 |
| [[#ic_qc_lab_beginning_balance_lab]] | รายละเอียด Lab ยกมา / Table 517 | 10 |
| [[#ic_qc_lab_beginning_balance_lab_container]] | รายละเอียด Container ยกมา / Table 518 | 7 |
| [[#ic_qc_lab_container]] | รายละเอียด Lab Container / Table 490 | 9 |
| [[#ic_qc_lab_container_issue]] | IC QC Lab Container Issue / Table 501 | 3 |
| [[#ic_qc_lab_cut]] | Table 509 / Table 509 | 5 |
| [[#ic_qc_lab_cut_detail]] | ic_qc_lab_cut_detail / Table 510 | 7 |
| [[#ic_qc_lab_transaction]] | Table 500 / Table 500 | 10 |
| [[#ic_qc_purchase_packing_size]] | IC QC Purchase Packing Size  | 6 |
| [[#ic_qc_purchase_packing_size_container]] | IC QC Purchase Packing Size Container  | 8 |
| [[#ic_qc_purchase_packing_size_item]] | IC QC Receive Container / Table 487 | 13 |
| [[#ic_quality_control]] | ic_quality_control  | 31 |
| [[#ic_quality_control_detail]] | IC Quality Control Detail  | 8 |
| [[#ic_specific_search]] | กำหนดการค้นหาสินค้าเฉพาะเจาะจง / IC Specific Search | 8 |
| [[#ic_specific_search_word]] | คำค้นหาสินค้าเฉพาะเจาะจง / Specific Search Word | 7 |
| [[#ic_trans_detail_commission]] | ค่าส่งเสริมการขาย / IC Trans Detail Commission | 27 |
| [[#qc_approved_vendor_list]] | ผู้ผลิตที่ได้รับการอนุมัติแล้ว / Approved Vendor List | 8 |

## ic_cost_date

**ic_cost_date** — ic_cost_date

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่ |  | smalldatetime |  |
| `ic_code` | สินค้า |  | varchar(25) |  |
| `price` | ราคา |  | float | ✓ |
| `remark` | หมายเหตุ |  | varchar(500) | ✓ |
| `line_number` | line_number |  | smallint | ✓ |

index: `ic_cost_date_ic_code`(ic_code), `ic_cost_date_doc_date`(doc_date)

## ic_lot_manage

**จัดการ LOT สินค้า** — Inventory LOT Manage

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `lot_number` | หมายเลข LOT |  | varchar(255) |  |
| `sort_order` | การเรียงลำดับ |  | varchar(10) | ✓ |
| `lot_select` | การเลือก |  | smallint | ✓ |
| `select_auto` | อัตโนมัติ *(resource only)* |  | char |  |
| `select_manual` | เลือกเองเท่านั้น *(resource only)* |  | char |  |
| `wh_code` | คลังสินค้า |  | varchar(50) | ✓ |
| `shelf_code` | ที่เก็บสินค้า |  | varchar(50) | ✓ |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |

index: `ic_lot_manage_ic_lot_manage_pk_ic_code_lot_number`(ic_code,lot_number,wh_code,shelf_code,mfd_date), `ic_lot_manage_ic_code`(ic_code), `ic_lot_manage_lot_select`(lot_select), `ic_lot_manage_sort_order`(sort_order)

## ic_qc_config

**ic_qc_config** — ic_qc_config

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `transfer_quarantine_doc_format_code` | กลุ่มเอกสารโอน Quarantine |  | varchar(50) | ✓ |
| `transfer_pass_doc_format_code` | กลุ่มเอกสารโอน Pass |  | varchar(50) | ✓ |
| `transfer_reject_doc_format_code` | กลุ่มเอกสารโอน Reject |  | varchar(50) | ✓ |
| `transfer_inprocess_doc_format_code` | กลุ่มเอกสารโอน InProcess |  | varchar(50) | ✓ |
| `quarantine_warehouse_code` | คลัง Quarantine |  | varchar(50) | ✓ |
| `quarantine_location_code` | ที่เก็บ Quarantine |  | varchar(50) | ✓ |
| `pass_warehouse_code` | คลัง Pass |  | varchar(50) | ✓ |
| `pass_location_code` | ที่เก็บ Pass |  | varchar(50) | ✓ |
| `reject_warehouse_code` | คลัง Reject |  | varchar(50) | ✓ |
| `reject_location_code` | ที่เก็บ Reject |  | varchar(50) | ✓ |
| `inprocess_warehouse_code` | คลัง Inprocess |  | varchar(50) | ✓ |
| `inprocess_location_code` | ที่เก็บ Inprocess |  | varchar(50) | ✓ |

## ic_qc_container_adjust

**ปรับจำนวน Container** — ic_qc_container_adjust

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `guid_code` | GUID Code |  | varchar(50) | ✓ |

## ic_qc_container_adjustment_detail

**ic_qc_container_adjustment_detail** — ic_qc_container_adjustment_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ |  | varchar(50) |  |
| `qty` | จำนวน |  | float |  |
| `lab_no` | Lab No |  | varchar(50) |  |
| `container_no` | Container No |  | smallint |  |
| `line_number` | Line Number |  | smallint |  |
| `lot_number` | หมายเลข LOT |  | varchar(50) |  |

## ic_qc_container_transaction

**QC Container Transaction**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `trans_flag` | ประเภทเอกสาร |  | smallint |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `ref_line_number` | อ้างอิงบรรทัด |  | smallint | ✓ |
| `lab_no` | Lab No |  | varchar(50) | ✓ |
| `container_no` | Container No |  | smallint | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `lot_number` | หมายเลข LOT |  | varchar(50) | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |

## ic_qc_indentify

**QC Indentify** — QC Indentify

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | GUID Code |  | varchar(50) | ✓ |
| `code` | รหัส |  | varchar(20) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่ออังกฤษ |  | varchar(255) | ✓ |

## ic_qc_lab

**รายละเอียด Lab** — Inventory Quality Lab

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `lab_no` | Lab No |  | varchar(50) |  |
| `ref_lab_no` | Ref Lab No. |  | varchar(50) | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `doc_ref` | เลขที่อ้างอิง |  | varchar(50) | ✓ |
| `doc_ref_date` | วันที่อ้างอิง |  | smalldatetime | ✓ |
| `cust_code` | เจ้าหนี้ |  | varchar(50) | ✓ |
| `lot_number` | Lot Number |  | varchar(100) | ✓ |
| `mfn_name` | ผู้ผลิต |  | varchar(255) | ✓ |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |
| `expire_date` | วันหมดอายุ |  | smalldatetime | ✓ |
| `retest_date` | Retest Date |  | smalldatetime | ✓ |
| `lab_status` | สถานะ |  | smallint | ✓ |
| `status_quarantine` | Quarantine *(resource only)* |  | char |  |
| `status_pass` | Pass *(resource only)* |  | char |  |
| `status_reject` | Reject *(resource only)* |  | char |  |
| `status_inprocess` | InProcess *(resource only)* |  | char |  |
| `ref_doc_type` | Ref Doc Type |  | smallint | ✓ |
| `identify_by` | Identify By |  | varchar(255) | ✓ |
| `container_qty` | จำนวน Container |  | float | ✓ |
| `qty` | จำนวนรับ |  | float | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `container_weight` | ขนาด Container |  | float | ✓ |
| `create_date` | create_date |  | smalldatetime | ✓ |
| `doc_line_number` | Document Line Number |  | smallint | ✓ |
| `move_lab_status` | ย้ายไป Lab ใหม่ |  | smallint | ✓ |
| `move_lab_no` | หมายเลข Lab ใหม่ |  | varchar(50) | ✓ |

index: `ic_qc_lab_pk_lab_no`(lab_no,item_code)

## ic_qc_lab_beginning_balance

**Lab คงเหลือยกมา** — Table 515

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | GUID Code |  | varchar(50) | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `tab_product` | รายละเอียดสินค้า *(resource only)* |  | char |  |
| `tab_lab` | Lab *(resource only)* |  | char |  |
| `tab_container` | Container *(resource only)* |  | char |  |

index: `ic_qc_lab_beginning_balance_PK_PRIMARY`(doc_no)

## ic_qc_lab_beginning_balance_detail

**รายละเอียด Lab ยกมา** — Table 516

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `unit_code` | หน่วยนับ |  | varchar(25) |  |
| `qty` | จำนวน |  | float |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `lot_number` | Lot Number |  | varchar(50) | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |

## ic_qc_lab_beginning_balance_lab

**รายละเอียด Lab ยกมา** — Table 517

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `ref_row` | บรรทัดอ้างอิง |  | smallint |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `lot_number` | หมายเลข Lot |  | varchar(50) |  |
| `lab_no` | Lab No |  | varchar(50) |  |
| `retest_date` | Retest Date |  | smalldatetime |  |
| `unit_code` | หน่วยบรรจุ |  | varchar(25) |  |
| `identify_by` | Identify By |  | varchar(255) | ✓ |
| `qty` | จำนวน |  | float |  |
| `line_number` | Line |  | smallint | ✓ |

## ic_qc_lab_beginning_balance_lab_container

**รายละเอียด Container ยกมา** — Table 518

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar |  |
| `item_code` | รหัสสินค้า |  | varchar |  |
| `lab_no` | Lab No |  | varchar |  |
| `container_no` | Container |  | smallint |  |
| `qty` | จำนวน |  | float |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `qc_status` | QC Status |  | smallint |  |

## ic_qc_lab_container

**รายละเอียด Lab Container** — Table 490

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `lab_no` | Lab No |  | varchar(50) |  |
| `container_no` | Container No |  | smallint | ✓ |
| `container_pack_size` | ขนาดบรรจุ |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `lab_status` | สถานะ |  | smallint | ✓ |
| `qty` | จำนวน *(resource only)* |  | char |  |
| `unit_pack` | หน่วยบรรจุ *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ *(resource only)* |  | char |  |
| `container_balance_qty` | จำนวนคงเหลือ |  | float | ✓ |

## ic_qc_lab_container_issue

**IC QC Lab Container Issue** — Table 501

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `guid_code` | GUID Code |  | varchar(50) | ✓ |

## ic_qc_lab_cut

**Table 509** — Table 509

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `guid_code` | GUID |  | varchar(255) | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime | ✓ |
| `doc_time` | เวลา |  | varchar(10) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |

index: `ic_qc_lab_cut_ic_qc_lab_cut_pk`(doc_no)

## ic_qc_lab_cut_detail

**ic_qc_lab_cut_detail** — Table 510

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `qty` | จำนวน |  | float | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(25) | ✓ |
| `line_number` | หมายเลขบรรทัด |  | smallint | ✓ |
| `lab_no` | Lab No |  | varchar(255) |  |

## ic_qc_lab_transaction

**Table 500** — Table 500

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `trans_flag` | ประเภทเอกสาร |  | smallint |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `ref_line_number` | อ้างอิงบรรทัด |  | smallint |  |
| `lab_no` | Lab No |  | varchar(50) |  |
| `lot_number` | Lot Number |  | varchar(50) | ✓ |
| `qty` | จำนวน |  | float |  |
| `unit_code` | หน่วยนับ |  | varchar(50) |  |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |

## ic_qc_purchase_packing_size

**IC QC Purchase Packing Size**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `cust_code` | เจ้าหนี้ |  | varchar(50) | ✓ |
| `guid_code` | GUID Code |  | varchar(50) | ✓ |
| `creator_code` |  |  | varchar | ✓ |
| `create_datetime` |  |  | datetime | ✓ |

## ic_qc_purchase_packing_size_container

**IC QC Purchase Packing Size Container**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `lot_number` | หมายเลข Lot |  | varchar(255) |  |
| `container_no` | Container No |  | smallint |  |
| `packing_size` | ขนาดบรรจุ |  | float |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |

## ic_qc_purchase_packing_size_item

**IC QC Receive Container** — Table 487

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `lot_number` | Lot Number |  | varchar(255) | ✓ |
| `total_container` | จำนวน Container |  | smallint | ✓ |
| `same_size` | บรรจุเท่ากัน |  | smallint | ✓ |
| `packing_size` | ขนาดบรรจุ |  | float | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `qty_receive` | จำนวนรับ |  | float | ✓ |
| `qty_receive_unit` | หน่วยรับ |  | varchar(50) | ✓ |
| `total_receive_qty` | รวมจำนวน |  | float | ✓ |

## ic_quality_control

**ic_quality_control**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `trans_flag` | ประเภทเอกสาร |  | smallint |  |
| `ic_qc_status` | สถานะ |  | smallint |  |
| `ic_qc_quarantine` | Quarantine *(resource only)* |  | char |  |
| `ic_qc_pass` | Pass *(resource only)* |  | char |  |
| `ic_qc_reject` | Reject *(resource only)* |  | char |  |
| `ic_qc_inprocess` | InProcess *(resource only)* |  | char |  |
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `lot_number` | Lot No. |  | varchar(100) | ✓ |
| `mfd_date` | วันที่ผลิต |  | smalldatetime | ✓ |
| `exp_date` | วันหมดอายุ |  | smalldatetime | ✓ |
| `lab_no` | Lab NO. |  | varchar(100) | ✓ |
| `lab_retest` | LAB Retest |  | varchar(100) | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `mfn` | ชื่อผู้ผลิต |  | varchar(255) | ✓ |
| `lab_retest_date` | Retest Date |  | smalldatetime | ✓ |
| `print_qty` | จำนวนพิมพ์ *(resource only)* |  | char |  |
| `start_qty` | จำนวนเริ่มต้น *(resource only)* |  | char |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(50) | ✓ |
| `guid_code` | GUID Code |  | varchar(60) | ✓ |
| `retest_date` | Retest Date |  | smalldatetime | ✓ |
| `reject_reason` | สาเหตุ |  | varchar(255) | ✓ |
| `pass_content` | Content |  | varchar(255) | ✓ |
| `is_not_retest` | Not Retest |  | smallint | ✓ |
| `container_no` | Container No *(resource only)* |  | char |  |
| `qty` | Quantity |  | float | ✓ |
| `unit_code` | Unit Code |  | varchar(50) | ✓ |
| `total_container` | total_container |  | smallint | ✓ |
| `prev_container` | prev_container |  | smallint | ✓ |

index: `ic_quality_control_PK_PRIMARY`(doc_no)

## ic_quality_control_detail

**IC Quality Control Detail**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(50) |  |
| `trans_flag` | ประเภทเอกสาร |  | smallint |  |
| `container_no` | หมายเลข Container |  | smallint | ✓ |
| `container_pack_size` | ขนาดบรรจุ |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `lab_status` | สถานะ |  | smallint | ✓ |

## ic_specific_search

**กำหนดการค้นหาสินค้าเฉพาะเจาะจง** — IC Specific Search

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(50) |  |
| `keyword` | คำค้นหา |  | varchar(500) |  |
| `ic_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `group_type` | Group Type |  | smallint | ✓ |
| `group_code` | กลุ่มสินค้า |  | varchar(50) | ✓ |
| `group_name` | ชื่อกลุ่มสินค้า *(resource only)* |  | char |  |
| `sort_order` | ลำดับ |  | smallint | ✓ |

## ic_specific_search_word

**คำค้นหาสินค้าเฉพาะเจาะจง** — Specific Search Word

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `keyword` | รหัสเครื่องยนต์ | Engine Code | varchar(500) |  |
| `guid_code` | GUID Code |  | varchar(35) | ✓ |
| `engine_valve` | จำนวนของวาล์ว | Number Of Engine Valve | varchar(25) | ✓ |
| `displacement` | ปริมาณ | Displacement (cc) | varchar(25) | ✓ |
| `market_names` | ชื่อตลาด | Market Names | varchar(1000) | ✓ |
| `remark` | โน๊ต | Note | varchar(1000) | ✓ |
| `description` | Description *(resource only)* | Description | char |  |

## ic_trans_detail_commission

**ค่าส่งเสริมการขาย** — IC Trans Detail Commission

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | รายวันระบบ |  | smallint |  |
| `item_code` | รหัสสินค้า |  | varchar(50) |  |
| `commission` | ค่าส่งเสริมการขาย |  | varchar(25) | ✓ |
| `commission_amount` | Commission |  | float | ✓ |
| `creator_code` |  |  | varchar(25) | ✓ |
| `create_datetime` |  |  | datetime | ✓ |
| `last_editor_code` |  |  | varchar(25) | ✓ |
| `lastedit_datetime` |  |  | datetime | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `wh_code` | คลัง *(resource only)* |  | char |  |
| `shelf_code` | พื้นที่เก็บ *(resource only)* |  | char |  |
| `unit_code` | หน่วยนับ *(resource only)* |  | char |  |
| `qty` | จำนวน *(resource only)* |  | char |  |
| `price` | ราคา *(resource only)* |  | char |  |
| `discount_word` | ส่วนลด *(resource only)* |  | char |  |
| `sum_amount` | รวมมูลค่า *(resource only)* |  | char |  |
| `discount` | ส่วนลด *(resource only)* |  | char |  |
| `wh_name` | คลัง *(resource only)* |  | char |  |
| `shelf_name` | พื้นที่เก็บ *(resource only)* |  | char |  |
| `unit_name` | หน่วยนับ *(resource only)* |  | char |  |
| `sum_amount_exclude_vat` | ยอดก่อนภาษี *(resource only)* |  | char |  |
| `discount_doc_word` | ลดท้ายรายการ *(resource only)* |  | char |  |
| `discount_doc_amount` | มูลค่าลดท้ายรายการ *(resource only)* |  | char |  |
| `commission_base` | สุทธิ *(resource only)* |  | char |  |
| `remark` | หมายเหตุ |  | varchar(1000) | ✓ |

index: `doc_no_trans_flag_item_code`(doc_no,trans_flag,item_code), `line_number`(line_number)

## qc_approved_vendor_list

**ผู้ผลิตที่ได้รับการอนุมัติแล้ว** — Approved Vendor List

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `item_code` | รหัสสินค้า |  | varchar(255) |  |
| `guid_code` | GUID |  | varchar(255) | ✓ |
| `supplier_code` | Supplier Code |  | varchar(255) |  |
| `manufacturer_code` | Manufacturer Code |  | varchar(255) |  |
| `is_cancel` | ยกเลิก |  | smallint | ✓ |
| `cancel_date` | วันที่ยกเลิก |  | smalldatetime | ✓ |

