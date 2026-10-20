---
tags: [sml, schema, pp, generated]
---
# ตารางกลุ่ม `pp` (kbyt)

กลับไป [[schema-index]]

## pp_config

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| serial_id | character varying(50) |
| wh_code | character varying(25) |
| location_list | character varying(500) |
| auto_mode | smallint |
| create_date_time_now | timestamp without time zone |

## pp_no_approve

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| wh_list | character varying |
| shelf_list | character varying |

## pp_plan

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| ref_doc_no | character varying(25) |
| status | smallint |
| remark | character varying(255) |
| cust_code | character varying(25) |
| transport_destination_code | character varying(25) |
| priority | smallint |
| doc_time | character varying(5) |
| create_date_time_now | timestamp without time zone |

## pp_plan_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| row_number | smallint |
| doc_no | character varying(25) |
| ic_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| transport_type | smallint |
| transport_date | date |
| transport_time | character varying(5) |
| priority | smallint |
| create_date_time_now | timestamp without time zone |

## pp_shipment

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_time | character varying(10) |
| trans_flag | smallint |
| doc_format_code | character varying(25) |
| doc_ref | character varying(25) |
| doc_ref_date | date |
| transport_type | character varying(25) |
| remark | character varying(500) |
| cust_code | character varying(25) |
| guid_code | character varying(50) |
| is_cancel | smallint |
| cancel_code | character varying(255) |
| cancel_datetime | timestamp without time zone |
| last_status | smallint |
| create_date_time_now | timestamp without time zone |
| status | smallint |

## pp_shipment_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| trans_flag | smallint |
| line_number | smallint |
| doc_ref_type | smallint |
| item_code | character varying(50) |
| remark | character varying(50) |
| cust_code | character varying(500) |
| ref_doc_no | character varying(50) |
| ref_doc_date | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## pp_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| ref_code | character varying(25) |
| ref_date | date |
| due_date | date |
| cust_code | character varying(25) |
| sale_code | character varying(25) |
| status | integer |
| persent | numeric |
| remark | character varying(255) |
| row_number | integer |
| is_cancel | smallint |
| cancel_code | character varying(255) |
| create_date_time_now | timestamp without time zone |
| sale_type | integer |
| department_code | character varying(255) |
| send_type | integer |
| creator_code | character varying(255) |
| branch_code | character varying(255) |
| create_date_time | character varying(255) |
| last_editor_code | character varying(255) |
| last_edit_date | time without time zone |
| confirm_code | character varying(255) |
| confirm_date_time | timestamp without time zone |
| cancel_date_time | character varying(255) |
| trans_flag | integer |
| last_status | integer |
| total_amount | numeric |
| confirm_date | date |
| confirm_time | time without time zone |
| e_doc_no | character varying(255) |
| is_close | integer |
| close_time | timestamp without time zone |
| b_doc_no | character varying(255) |
| wh_code | character varying(255) |
| shelf_code | character varying(255) |
| is_print | integer |
| is_confirm | integer |
| car_code | character varying(255) |
| tms_que_shipment_code | character varying(255) |
| lastedit_datetime | timestamp without time zone |

## pp_trans_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| row_number | integer |
| doc_no | character varying(25) |
| ic_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| event_qty | numeric |
| event_date_time | date |
| create_date_time_now | timestamp without time zone |
| department_code | character varying(255) |
| branch_code | character varying(255) |
| ref_code | character varying(255) |
| doc_date | date |
| ref_date | date |
| line_number | integer |
| status | integer |
| remark | character varying(255) |
| sum_amount | numeric |
| price | numeric |
| is_confirm | integer |
| tms_que_shipment_code | character varying(255) |
| car_code | character varying(255) |

## pp_trans_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| ref_code | character varying(255) |
| user_code | character varying(255) |
| trans_flag | integer |
| action | integer |
| create_datetime | timestamp without time zone |

## pp_user_active

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| login_time | timestamp without time zone |
| session_id | character varying(255) |
| last_accessed_time | timestamp without time zone |
| user_code | character varying(255) |
