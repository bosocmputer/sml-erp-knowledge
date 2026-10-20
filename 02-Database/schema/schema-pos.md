---
tags: [sml, schema, pos, generated]
---
# ตารางกลุ่ม `pos` (kbyt)

กลับไป [[schema-index]]

## pos_id

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| machinecode | character varying(10) |
| pos_id | character varying(30) |
| status | smallint |
| guid_code | character varying(35) |
| pos_config_number | smallint |
| price_number | smallint |
| doc_format | character varying(50) |
| doc_format_vat_full | character varying(50) |
| doc_format_cancel | character varying(50) |
| doc_format_fillmoney | character varying(50) |
| doc_format_cashiersettle | character varying(50) |
| pos_ic_wht | character varying(25) |
| pos_ic_shelf | character varying(25) |
| pos_type_invoice | smallint |
| pos_save_e_journal | smallint |
| slip_number | smallint |
| close_form_number | smallint |
| doc_running_inv | character varying(100) |
| doc_running_vat_full | character varying(100) |
| doc_running_cancel | character varying(100) |
| doc_running_fillmoney | character varying(100) |
| doc_running_cashiersettle | character varying(100) |
| doc_format_code | character varying(25) |
| doc_format_deposit | character varying(50) |
| doc_running_deposit | character varying(100) |
| doc_format_deposit_return | character varying(50) |
| doc_running_deposit_return | character varying(100) |
| doc_format_deposit_cancel | character varying(25) |
| branch_code | character varying(10) |
| doc_format_deposit_return_cancel | character varying(25) |
| use_credit_sale | smallint |
| show_order_detail | smallint |
| show_in_copy | smallint |
| no_remark_sendmoney | smallint |
| pos_header | character varying(1000) |
| doc_format_credit | character varying(50) |
| doc_running_credit | character varying(100) |
| doc_format_code_credit | character varying(10) |
| doc_format_code_tax_inv | character varying(50) |
| doc_format_code_doc_cancel | character varying(50) |
| doc_format_code_fill_money | character varying(50) |
| doc_format_code_send_money | character varying(50) |
| department_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| bcel_mcid | character varying(255) |
| bcel_mcc | character varying(255) |
| close_check_credit_sale_customer | smallint |
| order_of_sales_summary | smallint |
| sml_kbank_qr_api_config | smallint |
| sml_kbank_qr_credit | smallint |
| sml_kbank_qr_api_token | character varying(255) |
| sml_kbank_qr_api_uat_mode | smallint |

## pos_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| user_code | character varying(25) |
| datetime | timestamp without time zone |
| command | character varying(255) |
| message | character varying(500) |
| approve_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| amount | numeric |
| command_type | character varying(50) |

## pos_period

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| machine_code | character varying(10) |
| begin_date | timestamp without time zone |
| begin_time | character varying(10) |
| end_date | timestamp without time zone |
| end_time | character varying(10) |
| period_status | smallint |
| begin_user_code | character varying(25) |
| end_user_code | character varying(25) |
| period_guid | character varying(50) |
| create_date_time_now | timestamp without time zone |

## pos_point_condition

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| birth_month | numeric |
| birth_day | numeric |
| birth_month_use | smallint |
| birth_day_use | smallint |
| create_date_time_now | timestamp without time zone |

## pos_point_period

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| from_date | timestamp without time zone |
| to_date | timestamp without time zone |
| amount | numeric |
| point_value | numeric |
| point_value_condition | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## pos_point_special_day

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| from_date | timestamp without time zone |
| to_date | timestamp without time zone |
| multiply_point | numeric |
| description | character varying(100) |
| day_1 | smallint |
| day_2 | smallint |
| day_3 | smallint |
| day_4 | smallint |
| day_5 | smallint |
| day_6 | smallint |
| day_7 | smallint |
| day_0 | smallint |
| order_condition | smallint |
| create_date_time_now | timestamp without time zone |

## pos_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## pos_settle_bill_cancel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| pos_id | character varying(50) |
| ref_doc_no | character varying(50) |
| ref_doc_date | date |
| ref_amount | numeric |
| period_guid | character varying(50) |
| invoice_doc_no | character varying(50) |
| invoice_doc_date | date |
| create_date_time_now | timestamp without time zone |

## pos_settle_bill_discount

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| pos_id | character varying(50) |
| ref_doc_no | character varying(50) |
| ref_doc_date | date |
| sum_amount | numeric |
| discount_amount | numeric |
| total_amount | numeric |
| period_guid | character varying(50) |
| discount_item | numeric |
| create_date_time_now | timestamp without time zone |

## pos_settle_group_discount

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| pos_id | character varying(50) |
| discount_group_code | character varying(50) |
| discount_group_amount | numeric |
| discount_group_discount | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## pos_slip_campaign

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(255) |
| name_1 | character varying(255) |
| guid_code | character varying(50) |
| enable | smallint |
| date_begin | date |
| time_begin | character varying(10) |
| date_end | date |
| time_end | character varying(10) |
| sale_amount | numeric |
| display_wording | text |
| create_date_time_now | timestamp without time zone |
| bill_limit | numeric |

## pos_slip_campaign_brand

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| campaign_code | character varying(50) |
| code | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## pos_slip_campaign_category

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| campaign_code | character varying(50) |
| code | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## pos_slip_campaign_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| campaign_code | character varying(50) |
| group_main | character varying(50) |
| group_sub1 | character varying(50) |
| group_sub2 | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## pos_slip_campaign_items

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| campaign_code | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## pos_sync_device

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| command | character varying(255) |
| command_guid | character varying(50) |
| last_status | smallint |
| cust_code | character varying(50) |
| food_discount | character varying(50) |
| is_promotion | smallint |
| total_discount | character varying(100) |
| sale_code | character varying(50) |
| table_number | character varying(50) |
| result1 | character varying(50000) |
| result2 | character varying(50000) |
| service_charge | character varying(100) |
| create_date_time_now | timestamp without time zone |

## pos_view_column

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| screen_group | integer |
| screen_code | character varying(50) |
| column_number | integer |
| column_name | character varying(255) |
| column_name_2 | character varying(255) |
| column_field_name | character varying(500) |
| column_field_sort | character varying(500) |
| column_width | integer |
| column_type | integer |
| column_align | integer |
| column_format | character varying(255) |
| create_date_time_now | timestamp without time zone |

## pos_view_table

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| screen_code | character varying(50) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| table_name | character varying(255) |
| table_list | character varying(255) |
| sort | character varying(255) |
| filter | character varying(255) |
| width_persent | integer |
| create_date_time_now | timestamp without time zone |
