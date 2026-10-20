---
tags: [sml, schema, sync, generated]
---
# ตารางกลุ่ม `sync` (kbyt)

กลับไป [[schema-index]]

## sync_access_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| branch_code | character varying(100) |
| date_time | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## sync_branch_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| branch_code | character varying(100) |
| access_code | character varying(100) |
| branch_computer_name | character varying(100) |
| active | smallint |
| wait_time | smallint |
| branch_name | character varying(100) |
| sync_time_active | smallint |
| start_sync_time | character varying(10) |
| end_sync_time | character varying(10) |
| create_date_time_now | timestamp without time zone |

## sync_branch_list_server

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| branch_code | character varying(100) |
| server_url | character varying(255) |
| provider_code | character varying(100) |
| db_name | character varying(100) |
| create_date_time_now | timestamp without time zone |

## sync_change_code

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| change_mode | character varying(50) |
| old_code | character varying(25) |
| new_code | character varying(25) |
| branch_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## sync_field_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| table_name | character varying(100) |
| field_name | character varying(100) |
| default_value | character varying(100) |
| create_date_time_now | timestamp without time zone |

## sync_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| date_time | timestamp without time zone |
| message | character varying(100000) |
| branch_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## sync_receive_data

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| branch_code | character varying(100) |
| table_name | character varying(100) |
| sync_count | smallint |
| create_date_time_now | timestamp without time zone |

## sync_reset_receive_data

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| branch_code | character varying(100) |
| table_name | character varying(100) |

## sync_send_data

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| branch_code | character varying(100) |
| table_name | character varying(100) |
| command_mode | integer |
| guid | uuid |

## sync_send_data_truncate_table

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| branch_code | character varying(100) |
| table_name | character varying(100) |

## sync_table_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| table_name | character varying(100) |
| trans_type | smallint |
| trans_command | character varying(255) |
| always_sync | smallint |
| create_date_time_now | timestamp without time zone |
| sync_filter | character varying(2000) |
