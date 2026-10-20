---
tags: [sml, schema, sml, generated]
---
# ตารางกลุ่ม `sml` (kbyt)

กลับไป [[schema-index]]

## sml_agent

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name | character varying(100) |
| password | character varying(25) |
| email | character varying(50) |
| servername | character varying(50) |
| branchdatabasename | character varying(50) |
| windowservername | character varying(50) |
| transall | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## sml_barcode_print_format

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(100) |
| name | character varying(100) |
| formatdata | bytea |
| guid_code | character varying(10) |
| create_date_time_now | timestamp without time zone |

## sml_doc_images

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| image_id | character varying(50) |
| image_file | bytea |
| system_id | character varying(10) |
| guid_code | character varying(100) |
| image_order | smallint |
| create_date_time_now | timestamp without time zone |
| image_url | text |

## sml_fastreport

แถวโดยประมาณ: 571

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| menuid | character varying(100) |
| menuname | character varying(255) |
| reportdata | bytea |
| guid_code | character varying(40) |
| timeupdate | character varying(50) |
| report_type | smallint |
| is_system_report | smallint |
| owner_code | character varying(50) |
| ref_no | character varying(255) |
| create_date_time_now | timestamp without time zone |

## sml_group_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## sml_group_location

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| group_code | character varying(255) |
| whcode | character varying(200) |
| location | character varying(200) |
| name | character varying(255) |

## sml_group_system

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| group_code | character varying(255) |
| system_id | character varying(100) |

## sml_image_document

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| image_id | character varying(100) |
| image_file | bytea |
| system_id | character varying(50) |
| guid | character varying(60) |
| latitude | numeric |
| longitude | numeric |
| mac_address | character varying(588) |
| user_code | character varying(255) |
| refer_doc_no | character varying(50) |
| refer_trans_flag | smallint |
| create_date_time_now | timestamp without time zone |

## sml_permissions_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## sml_permissions_user

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## sml_posdesign

แถวโดยประมาณ: 5

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| screen_code | character varying(255) |
| screen_name | character varying(255) |
| screen_data | bytea |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## sml_tooltip

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| name_3 | character varying(255) |
| name_4 | character varying(255) |
| name_5 | character varying(255) |
| name_6 | character varying(255) |
| status | smallint |
| data_group | character varying(25) |
| create_date_time_now | timestamp without time zone |

## sml_user_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |
