---
tags: [sml, schema, singha, generated]
---
# ตารางกลุ่ม `singha` (kbyt)

กลับไป [[schema-index]]

## singha_online_billing_status

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
| create_date_time_now | timestamp without time zone |

## singha_online_unit_maping

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_sale | character varying(100) |
| unit_code | character varying(100) |
| qty_per_unit | numeric |
| line_number | integer |
| create_date_time_now | timestamp without time zone |
