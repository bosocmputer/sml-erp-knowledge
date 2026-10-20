---
tags: [sml, schema, order, generated]
---
# ตารางกลุ่ม `order` (kbyt)

กลับไป [[schema-index]]

## order_cart

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| user_owner | character varying(25) |
| cart_number | character varying(5) |
| cust_code | character varying(25) |
| status | smallint |
| amount | numeric |
| trans_type | smallint |
| bill_type | smallint |
| tax_type | smallint |
| branch_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| remark | character varying(255) |

## order_checker

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| guid_line | character varying(50) |
| guid_confirm | character varying(50) |
| cofirm_date | timestamp without time zone |
| confirm_time | character varying(10) |
| confirm_status | smallint |
| order_qty | numeric |
| create_date_time_now | timestamp without time zone |

## order_device_id

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| device_id | character varying(10) |
| device_name | character varying(50) |
| doc_format_order | character varying(255) |
| device_status | smallint |
| guid_code | character varying(50) |
| price_number | smallint |
| close_form_number | smallint |
| pos_config_number | smallint |
| device_disable_password | smallint |
| device_android | smallint |
| print_from_center | smallint |
| device_html | smallint |
| user_access | character varying(255) |
| create_date_time_now | timestamp without time zone |

## order_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| user_owner | character varying(25) |
| cart_number | character varying(5) |
| item_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| discount_word | character varying(25) |
| amount | numeric |
| remark | character varying(100) |
| order_date | timestamp without time zone |
| order_time | character varying(5) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| barcode | character varying(25) |
| branch_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| lot_number | character varying(255) |

## order_message

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_number | character varying(25) |
| user_owner | character varying(25) |
| cust_code | character varying(25) |
| order_item | character varying(25) |
| is_read | smallint |
| is_notification | smallint |
| message | text |
| create_date_time_now | timestamp without time zone |
