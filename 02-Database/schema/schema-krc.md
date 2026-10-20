---
tags: [sml, schema, krc, generated]
---
# ตารางกลุ่ม `krc` (kbyt)

กลับไป [[schema-index]]

## krc_permission

แถวโดยประมาณ: 14

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| user_code | character varying(255) |
| receive_screen | smallint |
| admin_screen | smallint |
| history_screen | smallint |
| create_datetime | timestamp without time zone |

## krc_trans

แถวโดยประมาณ: 718

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| doc_date | date |
| doc_time | time without time zone |
| wh_code | character varying(255) |
| location_code | character varying(255) |
| creator_code | character varying(255) |
| remark | text |
| create_datetime | timestamp without time zone |
| status | smallint |
| is_approve | smallint |
| user_approve | character varying(255) |
| approve_date_time | timestamp without time zone |
| branch_code | character varying(255) |
| doc_ref | character varying(255) |
| is_close | character varying(255) |
| user_close | character varying(255) |
| close_date_time | timestamp without time zone |
| cust_code | character varying(255) |
| sale_code | character varying(255) |

## krc_trans_detail

แถวโดยประมาณ: 1,840

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| barcode | character varying(255) |
| item_year | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(255) |
| wh_code | character varying(255) |
| location_code | character varying(255) |
| qty | numeric |
| so_qty | numeric |
| create_datetime | timestamp without time zone |
| remark | text |
| line_number | integer |
