---
tags: [sml, schema, barcode, generated]
---
# ตารางกลุ่ม `barcode` (kbyt)

กลับไป [[schema-index]]

## barcode_import_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | timestamp without time zone |
| doc_time | character varying(5) |
| doc_no | character varying(25) |
| qty | numeric |
| machine_name | character varying(50) |
| get_success | smallint |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## barcode_import_list_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| barcode | character varying(25) |
| item_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| doc_date | timestamp without time zone |
| doc_time | character varying(5) |
| doc_no | character varying(25) |
| lot_number | character varying(25) |
| expire_date | date |
| mfd_date | date |
| mfn_name | character varying(255) |
| create_date_time_now | timestamp without time zone |
