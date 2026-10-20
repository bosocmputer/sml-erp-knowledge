---
tags: [sml, schema, as, generated]
---
# ตารางกลุ่ม `as` (kbyt)

กลับไป [[schema-index]]

## as_asset

แถวโดยประมาณ: 155

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| code_old | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| name_eng_1 | character varying(100) |
| name_eng_2 | character varying(100) |
| unit_code | character varying(25) |
| as_type | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| as_location | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| user_code | character varying(25) |
| depreciation_account_code | character varying(25) |
| depreciation_sum_account_code | character varying(25) |
| account_code | character varying(25) |
| branch_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## as_asset_detail

แถวโดยประมาณ: 155

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| as_code | character varying(25) |
| as_buy_date | date |
| as_buy_price | numeric |
| as_buy_from | character varying(255) |
| as_buy_description | character varying(255) |
| doc_buy_ref | character varying(25) |
| doc_buy_date | date |
| calc_type | smallint |
| as_age | numeric |
| as_rate | numeric |
| as_start_cut | numeric |
| start_calc_date | date |
| stop_calc_date | date |
| as_calc_value | numeric |
| as_value_balance | numeric |
| as_sum_value_balance | numeric |
| as_dead_value | numeric |
| as_dead_calc | smallint |
| as_sale_date | date |
| as_sale_price | numeric |
| as_sale_to | character varying(255) |
| as_sale_description | character varying(255) |
| depreciate_balance | numeric |
| doc_sale_ref | character varying(25) |
| doc_sale_date | date |
| insure_no | character varying(25) |
| safety_code | character varying(25) |
| insure_company | character varying(100) |
| insure_money | numeric |
| insure_age | numeric |
| insure_start_date | date |
| insure_stop_date | date |
| picture_1 | character varying(255) |
| picture_2 | character varying(255) |
| picture_3 | character varying(255) |
| picture_4 | character varying(255) |
| remark | character varying(255) |
| status | smallint |
| as_buy_year | smallint |
| derived_from | character varying(255) |
| asset_status | character varying(255) |
| asset_province | character varying(25) |
| as_model | character varying(255) |
| as_description | character varying(255) |
| as_price_group | character varying(255) |
| as_budget | character varying(255) |
| create_date_time_now | timestamp without time zone |

## as_asset_location

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(10) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_maintain

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_maintain_unit

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_maintenance

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| branch_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| total_maintain_value | numeric |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_maintenance_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| as_code | character varying(25) |
| maintain_code | character varying(25) |
| maintain_name | character varying(100) |
| maintain_unit | character varying(25) |
| maintain_date | date |
| maintain_location | character varying(100) |
| maintain_price | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## as_asset_result

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| as_code | character varying(25) |
| maintain_code | character varying(25) |
| maintain_name | character varying(100) |
| maintain_unit | character varying(25) |
| description | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## as_asset_retire

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_sale

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_group | character varying(25) |
| doc_ref | character varying(25) |
| bill_no | character varying(25) |
| bill_date | date |
| ar_code | character varying(25) |
| sale_type | character varying(25) |
| sale_date | date |
| side_code | character varying(25) |
| department_code | character varying(25) |
| total_value | numeric |
| total_depreciate_value | numeric |
| after_depreciate_value | numeric |
| total_sale_price | numeric |
| total_vat_value | numeric |
| total_net_value | numeric |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_asset_sale_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| as_code | character varying(25) |
| as_value | numeric |
| depreciate_value | numeric |
| after_depreciate | numeric |
| sale_price | numeric |
| vat_value | numeric |
| net_value | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## as_asset_type

แถวโดยประมาณ: 9

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## as_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## as_trans

แถวโดยประมาณ: 34

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| doc_format_code | character varying(25) |
| total_amount | numeric |
| remark | character varying(500) |
| trans_flag | smallint |
| from_as_code | character varying(25) |
| to_as_code | character varying(25) |
| from_as_type | character varying(25) |
| to_as_type | character varying(25) |
| from_as_department | character varying(25) |
| to_as_department | character varying(25) |
| from_as_period | smallint |
| to_as_period | smallint |
| department_split | smallint |
| date_begin | date |
| date_end | date |
| by_year | smallint |
| trans_type | smallint |
| process_mode | smallint |
| process_by | smallint |
| doc_group | character varying(25) |
| doc_ref | character varying(255) |
| doc_ref_date | date |
| tax_doc_no | character varying(25) |
| tax_doc_date | date |
| inquiry_type | smallint |
| vat_type | smallint |
| cust_code | character varying(25) |
| contactor | character varying(25) |
| branch_code | character varying(25) |
| project_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| sale_area_code | character varying(25) |
| sale_code | character varying(25) |
| send_type | smallint |
| send_day | integer |
| send_date | date |
| expire_date | date |
| credit_day | integer |
| due_date | date |
| answer_type | smallint |
| transport_value | numeric |
| discount_word | character varying(25) |
| vat_rate | numeric |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| total_cost | numeric |
| total_value | numeric |
| total_discount | numeric |
| total_vat_value | numeric |
| total_after_vat | numeric |
| total_except_vat | numeric |
| balance_amount | numeric |
| adjust_reason | character varying(25) |
| approve_code | character varying(25) |
| approve_date | date |
| status | smallint |
| user_request | character varying(25) |
| expire_day | integer |
| send_mail | smallint |
| send_sms | smallint |
| doc_ref_trans | character varying(25) |
| credit_date | date |
| total_before_vat | numeric |
| allocate_code | character varying(25) |
| job_code | character varying(25) |
| delivery_date | date |
| pay_amount | numeric |
| money | numeric |
| sum_pay_money_diff | numeric |
| currency_money | numeric |
| total_debt_amount | numeric |
| cancel_type | integer |
| last_status | smallint |
| used_status | smallint |
| doc_success | smallint |
| total_manual | smallint |
| on_hold | smallint |
| extra_word | character varying(100) |
| transport_code | character varying(25) |
| want_day | smallint |
| want_date | date |
| deposit_day | smallint |
| deposit_date | date |
| sale_group | character varying(25) |
| not_approve_1 | smallint |
| user_approve | character varying(25) |
| approve_status | smallint |
| expire_status | smallint |
| advance_amount | numeric |
| used_status_2 | smallint |
| remark_2 | character varying(255) |
| remark_3 | character varying(255) |
| ref_amount | numeric |
| ref_new_amount | numeric |
| ref_diff | numeric |
| sum_point | numeric |
| cashier_code | character varying(25) |
| is_pos | smallint |
| pos_id | character varying(25) |
| member_code | character varying(25) |
| doc_no_guid | character varying(25) |
| pos_bill_type | smallint |
| pos_bill_change | smallint |
| doc_type | smallint |
| recheck_count_day | numeric |
| recheck_count | smallint |
| wh_from | character varying(25) |
| location_from | character varying(25) |
| wh_to | character varying(25) |
| location_to | character varying(25) |
| auto_create | smallint |
| payable_sub_type_1_1 | character(1) |
| payable_sub_type_1_2 | character(1) |
| payable_sub_type_3 | character(1) |
| payable_sub_type_4 | character(1) |
| invoice_add_cash_other | character(1) |
| invoice_add_cash_service_other | character(1) |
| send_to_pick_and_pack | smallint |
| service_charge_word | character varying(25) |
| total_service_charge | numeric |
| sale_shift_id | character varying(50) |
| creator_code | character varying(255) |
| last_editor_code | character varying(255) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| table_number | character varying(25) |
| period_guid | character varying(50) |
| branch_code_to | character varying(25) |
| allocate_code_to | character varying(25) |
| project_code_to | character varying(25) |
| job_code_to | character varying(25) |
| side_code_to | character varying(25) |
| department_code_to | character varying(25) |
| point_telephone | character varying(25) |
| sum_point_2 | numeric |
| remark_4 | character varying(255) |
| remark_5 | character varying(255) |
| is_manual_vat | smallint |
| pass_book_code | character varying(25) |
| total_amount_2 | numeric |
| sender_code | character varying(25) |
| is_cancel | smallint |
| cancel_code | character varying(255) |
| cancel_datetime | timestamp without time zone |
| is_hold | smallint |
| auto_approved | smallint |
| pos_transfer | smallint |
| doc_close | smallint |
| ref_doc_type | character varying(50) |
| is_doc_copy | smallint |
| doc_reason | character varying(500) |
| discount_word_2 | character varying(50) |
| total_discount_2 | numeric |
| total_value_2 | numeric |
| total_amout_old | numeric |
| lost_profit_exchange_amount | numeric |
| create_date_time_now | timestamp without time zone |
| doc_copy_reason_type | smallint |

## as_trans_detail

แถวโดยประมาณ: 2,358

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| item_code | character varying(50) |
| item_name | character varying(255) |
| sum_amount | numeric |
| remark | character varying(500) |
| trans_flag | smallint |
| line_number | smallint |
| trans_type | smallint |
| doc_group | character varying(25) |
| doc_ref | character varying(25) |
| cust_code | character varying(25) |
| inquiry_type | smallint |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| discount | character varying(25) |
| sum_of_cost | numeric |
| due_date | date |
| status | smallint |
| ref_doc_no | character varying(25) |
| ref_doc_date | date |
| ref_line_number | integer |
| ref_cust_code | character varying(25) |
| branch_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| wh_code_2 | character varying(25) |
| shelf_code_2 | character varying(25) |
| department_code | character varying(25) |
| total_vat_value | numeric |
| cancel_qty | numeric |
| total_qty | numeric |
| stand_value | numeric |
| divide_value | numeric |
| ratio | numeric |
| ic_pattern | character varying(25) |
| ic_color | character varying(25) |
| ic_size | character varying(25) |
| priority_level | integer |
| calc_flag | integer |
| last_status | integer |
| set_ref_line | character varying(40) |
| set_ref_price | numeric |
| set_ref_qty | numeric |
| item_type | integer |
| vat_type | integer |
| doc_ref_type | smallint |
| item_code_main | character varying(25) |
| ref_row | smallint |
| ref_guid | character varying(40) |
| is_permium | smallint |
| is_get_price | smallint |
| average_cost | numeric |
| sum_amount_exclude_vat | numeric |
| doc_date_calc | date |
| doc_time_calc | character varying(5) |
| discount_amount | numeric |
| price_exclude_vat | numeric |
| user_approve | character varying(25) |
| price_type | smallint |
| price_mode | smallint |
| temp_float_1 | numeric |
| temp_float_2 | numeric |
| temp_string_1 | character varying(25) |
| is_serial_number | smallint |
| bank_name | character varying(25) |
| bank_branch | character varying(25) |
| chq_number | character varying(25) |
| barcode | character varying(25) |
| discount_number | smallint |
| price_changed | smallint |
| discount_changed | smallint |
| price_default | numeric |
| tax_type | smallint |
| is_pos | smallint |
| auto_create | smallint |
| date_expire | date |
| hidden_cost_1 | numeric |
| hidden_cost_1_exclude_vat | numeric |
| hidden_cost_2 | numeric |
| hidden_cost_2_exclude_vat | numeric |
| sum_of_cost_1 | numeric |
| average_cost_1 | numeric |
| sale_code | character varying(25) |
| sale_group | character varying(25) |
| date_due | timestamp without time zone |
| lot_number_1 | character varying(50) |
| item_code_2 | character varying(25) |
| bank_name_2 | character varying(25) |
| bank_branch_2 | character varying(25) |
| sale_shift_id | character varying(50) |
| price_base | numeric |
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| fee_amount | numeric |
| transfer_amount | numeric |
| price_set_ratio | numeric |
| mfd_date | date |
| mfn_name | character varying(255) |
| price_2 | numeric |
| sum_amount_2 | numeric |
| price_guid | character varying(55) |
| discount_amount_2 | numeric |
| is_lock_cost | smallint |
| sum_of_cost_fix | numeric |
| profit_lost_cost_amount | numeric |
| is_doc_copy | smallint |
| bat_date | date |
| bat_number | character varying(255) |
| product_year | character varying(10) |
| product_week | character varying(10) |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| qty_2 | numeric |
| unit_code_2 | character varying(25) |
| total_size | numeric |
| unit_size | numeric |
| exchange_rate_old | numeric |
| create_date_time_now | timestamp without time zone |
| mfn_code | character varying(50) |
| promotion_code | character varying(50) |
