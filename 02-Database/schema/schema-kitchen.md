---
tags: [sml, schema, kitchen, generated]
---
# ตารางกลุ่ม `kitchen` (kbyt)

กลับไป [[schema-index]]

## kitchen_command

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | character varying(50) |
| doc_time | character varying(25) |
| doc_type | smallint |
| kitchen_data | text |
| create_date_time_now | timestamp without time zone |

## kitchen_master

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| guid_code | character varying(35) |
| printer_name | character varying(100) |
| printer_mode | smallint |
| print_to_kitchen | smallint |
| print_summery | smallint |
| served_control | smallint |
| slip_header_font | character varying(255) |
| slip_sub_header_font | character varying(255) |
| slip_detail_font | character varying(255) |
| last_member_code | character varying(25) |
| printer_manual_feed | smallint |
| printer_slip_width | numeric |
| barcode_print | smallint |
| print_order_for_check | smallint |
| print_order_per_unit | smallint |
| kitchen_ready | smallint |
| print_tableopen | smallint |
| print_order_number_barcode | smallint |
| print_barcode | smallint |
| print_copy | smallint |
| print_copy_mode | smallint |
| print_copy_name | character varying(255) |
| print_number_order_check | smallint |
| print_language_index | smallint |
| no_price_print | smallint |
| speech_serial | character varying(25) |
| no_number_order_for_check | smallint |
| hide_table_footer_bill | smallint |
| hide_repeat_order_bill | smallint |
| create_date_time_now | timestamp without time zone |

## kitchen_master_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| kitchen_code | character varying(25) |
| food_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## kitchen_master_order_id

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| kitchen_code | character varying(25) |
| order_device | character varying(25) |
| create_date_time_now | timestamp without time zone |

## kitchen_master_pos_id

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| kitchen_code | character varying(25) |
| pos_id | character varying(25) |
| selected | smallint |
| create_date_time_now | timestamp without time zone |

## kitchen_print_cancel_copy

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| kitchen_code | character varying(25) |
| print_mode | smallint |
| print_name | character varying(250) |
| status | smallint |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## kitchen_print_copy

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| kitchen_code | character varying(25) |
| print_mode | smallint |
| print_name | character varying(250) |
| status | smallint |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## kitchen_print_count

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| kitchen_code | character varying(50) |
| print_count | smallint |
| create_date_time_now | timestamp without time zone |
