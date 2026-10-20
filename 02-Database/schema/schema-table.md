---
tags: [sml, schema, table, generated]
---
# ตารางกลุ่ม `table` (kbyt)

กลับไป [[schema-index]]

## table_master

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| number | character varying(25) |
| name_1 | character varying(50) |
| status | smallint |
| guid_code | character varying(35) |
| level_1 | character varying(50) |
| level_2 | character varying(50) |
| level_3 | character varying(50) |
| level_4 | character varying(50) |
| open_date | timestamp without time zone |
| open_time | character varying(5) |
| trans_guid | character varying(50) |
| priority | smallint |
| last_member_code | character varying(25) |
| last_discount | character varying(50) |
| last_service_charge | character varying(50) |
| table_qrcode | character varying(50) |
| table_barcode | character varying(25) |
| create_date_time_now | timestamp without time zone |

## table_order

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| table_number | character varying(25) |
| item_code | character varying(25) |
| unit_code | character varying(25) |
| barcode | character varying(25) |
| doc_no | character varying(25) |
| price | numeric |
| qty | numeric |
| discount_word | character varying(25) |
| discount_amount | numeric |
| sum_amount | numeric |
| guid_line | character varying(50) |
| last_status | smallint |
| qty_send | smallint |
| order_type | smallint |
| remark | character varying(255) |
| doc_date | timestamp without time zone |
| doc_time | character varying(5) |
| line_number | smallint |
| trans_guid | character varying(50) |
| kitchen_code | character varying(25) |
| qty_cancel | numeric |
| qty_balance | numeric |
| as_item_name | character varying(255) |
| confirm_guid | character varying(50) |
| confirm_status | smallint |
| isspeech | smallint |
| order_number_barcode | character varying(25) |
| old_doc_no | character varying(25) |
| create_date_time_now | timestamp without time zone |
| topping_list | character varying(255) |

## table_order_cancel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| table_number | character varying(25) |
| guid_line | character varying(50) |
| qty | numeric |
| remark | character varying(100) |
| item_code | character varying(25) |
| unit_code | character varying(25) |
| line_number | smallint |
| price | numeric |
| sum_amount | numeric |
| cancel_guid | character varying(50) |
| doc_date | timestamp without time zone |
| doc_time | character varying(25) |
| sale_code | character varying(25) |
| cancel_flag | smallint |
| table_number_2 | character varying(50) |
| create_date_time_now | timestamp without time zone |

## table_order_doc

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | timestamp without time zone |
| doc_time | character varying(5) |
| table_number | character varying(25) |
| sale_code | character varying(25) |
| order_status | smallint |
| cust_code | character varying(25) |
| sum_amount | numeric |
| qty | numeric |
| trans_guid | character varying(50) |
| last_status | smallint |
| device_type | smallint |
| order_number_barcode | character varying(25) |
| cashier_doc_no | character varying(25) |
| cashier_doc_date | date |
| create_date_time_now | timestamp without time zone |

## table_order_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| date_time | timestamp without time zone |
| command1 | character varying(255) |
| message | character varying(1000) |
| sale_code | character varying(25) |
| qty | numeric |
| create_date_time_now | timestamp without time zone |

## table_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_guid | character varying(50) |
| open_doc_date | timestamp without time zone |
| open_doc_time | character varying(5) |
| open_sale_code | character varying(25) |
| close_doc_date | timestamp without time zone |
| close_doc_time | character varying(5) |
| close_sale_code | character varying(25) |
| cashier_doc_date | timestamp without time zone |
| cashier_doc_time | character varying(5) |
| cashier_sale_code | character varying(25) |
| cashier_doc_no | character varying(50) |
| table_number | character varying(25) |
| table_number_2 | character varying(25) |
| cust_code | character varying(25) |
| food_discount | character varying(25) |
| total_discount | character varying(25) |
| print_count | smallint |
| ispromotion_process | smallint |
| service_charge | character varying(25) |
| customer_count | smallint |
| discount_group | character varying(500) |
| create_date_time_now | timestamp without time zone |
