---
tags: [sml, dictionary, edi, generated]
module: EDI
---
# พจนานุกรม: EDI — EDI

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#edi_ar_list]] | EDI AR List / EDI AR List | 7 |
| [[#edi_barcode_list]] | EDI Barcode List / EDI Barcode List | 5 |
| [[#edi_external]] | EDI External / EDI External | 18 |
| [[#edi_product_list]] | EDI Product List / Table 360 | 7 |
| [[#edi_so_alert_config]] | EDI SO Alert Config / edi so alert config | 3 |
| [[#edi_status]] | EDI Status / EDI Status | 20 |
| [[#edi_unit_list]] | EDI Unit List / EDI Unit List | 6 |
| [[#singha_online_billing_status]] | Singha Online Billing Status / Singha Online Billing Status | 17 |

## edi_ar_list

**EDI AR List** — EDI AR List

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `edi_code` | EDI External Code |  | varchar(25) |  |
| `ar_code` | รหัสลูกค้า/รหัสลูกหนี้ |  | varchar(25) |  |
| `ar_name` | ชื่อลูกค้า/ชื่อลูกหนี้ *(resource only)* |  | char |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `ship_code` | Ship Code |  | varchar(25) | ✓ |
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ |  | varchar(25) | ✓ |

index: `edi_ar_list_edi_ar_list_ar_code`(ar_code)

## edi_barcode_list

**EDI Barcode List** — EDI Barcode List

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `edi_code` | EDI External Code |  | varchar(25) |  |
| `edi_barcode` | External Barcode |  | varchar(25) |  |
| `barcode` | บารโค๊ด |  | varchar(25) |  |
| `line_number` | Line Number |  | smallint |  |
| `price` | ราคา |  | float | ✓ |

## edi_external

**EDI External** — EDI External

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | Buyer Code/External Code |  | varchar(25) |  |
| `name_1` | External Name |  | varchar(255) |  |
| `trading_partner_id` | Partner ID |  | varchar(50) | ✓ |
| `supplier_ean_code` | Supplier Code |  | varchar(50) | ✓ |
| `ar_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `dc_code` | รหัสศูนย์กระจายสินค้า DC |  | varchar(50) | ✓ |
| `export_format` | Export Format |  | smallint | ✓ |
| `tab_product` | สินค้า *(resource only)* |  | char |  |
| `tab_barcode` | บาร์โค๊ด *(resource only)* |  | char |  |
| `tab_unitcode` | หน่วยนับ *(resource only)* |  | char |  |
| `guid_code` | GUID |  | varchar(50) | ✓ |
| `format_0` | CP *(resource only)* |  | char |  |
| `format_1` | BIGC *(resource only)* |  | char |  |
| `format_2` | TIMS *(resource only)* |  | char |  |
| `tab_customer` | ลูกค้า *(resource only)* |  | char |  |
| `wh_code` | คลัง |  | varchar(25) | ✓ |
| `shelf_code` | พื้นที่เก็บ |  | varchar(25) | ✓ |
| `use_price` | Use Price |  | smallint | ✓ |

## edi_product_list

**EDI Product List** — Table 360

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `edi_code` | EDI External Code |  | varchar(25) |  |
| `item_code` | External Product Code |  | varchar(25) |  |
| `item_name` | External Product Name |  | varchar(255) | ✓ |
| `ic_code` | Product Code |  | varchar(25) | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `ic_name` | Product Name *(resource only)* |  | char |  |
| `item_packsize` | Pack Size |  | float | ✓ |

## edi_so_alert_config

**EDI SO Alert Config** — edi so alert config

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า/รหัสลูกหนี้ | AR Code | varchar(25) | ✓ |
| `ar_name` | ชื่อลูกค้า/ชื่อลูกหนี้ | AR Name | varchar(25) | ✓ |
| `start_date` | วันที่เริ่มใช้งาน | start Date | smalldatetime | ✓ |

## edi_status

**EDI Status** — EDI Status

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `order_date` | Order Date |  | smalldatetime | ✓ |
| `order_no` | Order No |  | varchar(25) | ✓ |
| `order_type` | Order Type |  | varchar(25) | ✓ |
| `address` | Address |  | varchar(25) | ✓ |
| `invoice_date` | Invoice Date |  | smalldatetime | ✓ |
| `invoice_no` | Invoice No |  | varchar(25) | ✓ |
| `packing_date_time` | Packing date time |  | datetime | ✓ |
| `confirm_packing_user` | Packing user |  | varchar(25) | ✓ |
| `in_transit_date_time` | In transit date time |  | datetime | ✓ |
| `confirm_in_transit_user` | In transit user |  | varchar(25) | ✓ |
| `delivered_date_time` | Delivered date time |  | datetime | ✓ |
| `confirm_delivered_user` | Delivered user |  | varchar(25) | ✓ |
| `cancel_date_time` | Cancel date time |  | datetime | ✓ |
| `confirm_cancel_user` | Cancel user |  | varchar(25) | ✓ |
| `receive_date_time` | Receive date time |  | datetime | ✓ |
| `confirm_receive_user` | Receive user |  | varchar(25) | ✓ |
| `good_recieipt_id_date_time` | Good Recieipt ID date time |  | datetime | ✓ |
| `good_recieipt_id` | Good Recieipt ID |  | varchar(255) | ✓ |
| `confirm_good_recieipt_id_user` | Good Recieipt ID user |  | varchar(25) | ✓ |

## edi_unit_list

**EDI Unit List** — EDI Unit List

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `edi_code` | EDI External Code |  | varchar(25) |  |
| `edi_unit_code` | External Unit Code |  | varchar(25) |  |
| `edi_unit_name` | External Unit Name |  | varchar(255) | ✓ |
| `unit_code` | รหัสหน่วยนับ |  | varchar(25) |  |
| `unit_name` | ชื่อหน่วยนับ *(resource only)* |  | char |  |
| `line_number` | Line Number |  | smallint |  |

## singha_online_billing_status

**Singha Online Billing Status** — Singha Online Billing Status

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `order_date` | Order Date |  | smalldatetime | ✓ |
| `order_no` | Order No |  | varchar(25) | ✓ |
| `order_type` | Order Type |  | varchar(25) | ✓ |
| `address` | Address |  | varchar(255) | ✓ |
| `invoice_date` | Invoice Date |  | smalldatetime | ✓ |
| `invoice_no` | Invoice No |  | varchar(25) | ✓ |
| `packing_date_time` | Packing date time |  | datetime | ✓ |
| `confirm_packing_user` | Packing user |  | varchar(25) | ✓ |
| `in_transit_date_time` | In transit date time |  | datetime | ✓ |
| `confirm_in_transit_user` | In transit user |  | varchar(25) | ✓ |
| `delivered_date_time` | Delivered date time |  | datetime | ✓ |
| `confirm_delivered_user` | Delivered user |  | varchar(25) | ✓ |
| `cancel_date_time` | Cancel date time |  | datetime | ✓ |
| `confirm_cancel_user` | Cancel user |  | varchar(25) | ✓ |
| `receive_date_time` | Receive date time |  | datetime | ✓ |
| `confirm_receive_user` | Confirm receive user |  | varchar(25) | ✓ |

