---
tags: [sml, schema, edi, generated]
---
# ตารางกลุ่ม `edi` (kbyt)

กลับไป [[schema-index]]

## edi_ar_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| edi_code | character varying(25) |
| ar_code | character varying(25) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| ship_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |

## edi_barcode_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| edi_code | character varying(25) |
| edi_barcode | character varying(25) |
| barcode | character varying(25) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| price | numeric |

## edi_external

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| trading_partner_id | character varying(50) |
| supplier_ean_code | character varying(50) |
| ar_code | character varying(25) |
| dc_code | character varying(50) |
| export_format | smallint |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| use_price | smallint |

## edi_product_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| edi_code | character varying(25) |
| item_code | character varying(25) |
| item_name | character varying(255) |
| ic_code | character varying(25) |
| line_number | smallint |
| item_packsize | numeric |
| create_date_time_now | timestamp without time zone |

## edi_so_alert_config

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| ar_name | character varying(25) |
| start_date | date |
| create_date_time_now | timestamp without time zone |

## edi_status

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| order_date | date |
| order_no | character varying(25) |
| order_type | character varying(25) |
| address | character varying(255) |
| invoice_date | date |
| invoice_no | character varying(25) |
| packing_date_time | timestamp without time zone |
| confirm_packing_user | character varying(25) |
| in_transit_date_time | timestamp without time zone |
| confirm_in_transit_user | character varying(25) |
| delivered_date_time | timestamp without time zone |
| confirm_delivered_user | character varying(25) |
| cancel_date_time | timestamp without time zone |
| confirm_cancel_user | character varying(25) |
| receive_date_time | timestamp without time zone |
| confirm_receive_user | character varying(25) |
| good_recieipt_id_date_time | timestamp without time zone |
| good_recieipt_id | character varying(255) |
| confirm_good_recieipt_id_user | character varying(25) |
| create_date_time_now | timestamp without time zone |

## edi_unit_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| edi_code | character varying(25) |
| edi_unit_code | character varying(25) |
| edi_unit_name | character varying(255) |
| unit_code | character varying(25) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
