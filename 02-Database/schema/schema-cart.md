---
tags: [sml, schema, cart, generated]
---
# ตารางกลุ่ม `cart` (kbyt)

กลับไป [[schema-index]]

## cart_user_order_bill

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| billing_no | character varying(255) |
| doc_ref | character varying(255) |
| user_code | character varying(255) |
| cust_code | character varying(255) |
| addr_name | character varying(255) |
| addr | character varying(255) |
| wh_code | character varying(255) |
| sum_amount | character varying(255) |
| send_date | date |
| create_date_time | timestamp without time zone |

## cart_user_order_bill_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| billing_no | character varying(255) |
| doc_ref | character varying(255) |
| user_code | character varying(255) |
| cust_code | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(255) |
| qty | numeric |
| price | numeric |
| amount | numeric |
| create_date_time | timestamp without time zone |
| remark | character varying(255) |

## cart_user_order_temp

แถวโดยประมาณ: 86

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| user_code | character varying(255) |
| cust_code | character varying(255) |
| addr_name | character varying(255) |
| addr | character varying(255) |
| wh_code | character varying(255) |
| send_date | date |
| create_date_time | timestamp without time zone |
| telephone | character varying(255) |
| inquiry_type | smallint |
| vat_type | smallint |
| logistic_area | character varying(255) |
| latitude | character varying(255) |

## cart_user_order_temp_detail

แถวโดยประมาณ: 32

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| user_code | character varying(255) |
| cust_code | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(255) |
| qty | numeric |
| create_date_time | timestamp without time zone |
| remark | character varying(255) |
| discount_word | character varying(255) |
| wh_code | character varying(255) |
