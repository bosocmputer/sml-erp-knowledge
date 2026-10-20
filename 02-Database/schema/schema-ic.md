---
tags: [sml, schema, ic, generated]
---
# ตารางกลุ่ม `ic` (kbyt)

กลับไป [[schema-index]]

## ic_account_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| income_acc_code | character varying(10) |
| item_acc_code | character varying(10) |
| cost_acc_code | character varying(10) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_attribute_thai7

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(50) |
| member_id | character varying(50) |
| attribute_name | character varying(200) |
| attribute_value | character varying(100) |
| date_save | date |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_brand

แถวโดยประมาณ: 201

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
| guid | uuid |

## ic_category

แถวโดยประมาณ: 35

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
| guid | uuid |

## ic_category_thai7

แถวโดยประมาณ: 0

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
| parent_code | integer |
| cate_type | integer |
| create_date_time_now | timestamp without time zone |

## ic_character

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

## ic_class

แถวโดยประมาณ: 5

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
| guid | uuid |

## ic_close_reason

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

## ic_color

แถวโดยประมาณ: 1

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
| guid | uuid |

## ic_color_use

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_cost_date

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| ic_code | character varying(25) |
| price | numeric |
| remark | character varying(500) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_date_adjust

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_group | character varying(25) |
| ap_ar_code | character varying(25) |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_date_adjust_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| bill_date | date |
| bill_no | character varying(25) |
| credit_day_old | integer |
| due_date_old | date |
| sending_date_old | date |
| credit_day_new | integer |
| due_date_new | date |
| sending_date_new | date |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_description

แถวโดยประมาณ: 86

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| description | character varying(5000) |
| create_date_time_now | timestamp without time zone |

## ic_design

แถวโดยประมาณ: 692

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
| guid | uuid |

## ic_dimension

แถวโดยประมาณ: 96

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| remark | character varying(255) |
| dimension_no | integer |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_dimension_name

แถวโดยประมาณ: 12

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| dimension_number | integer |
| name_1 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_discount_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| date_begin | date |
| date_end | date |
| status | smallint |
| guid_code | character varying(50) |
| discount_list | character varying(500) |
| create_date_time_now | timestamp without time zone |

## ic_extra_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_no | character varying(25) |
| doc_date | date |
| ic_code | character varying(25) |
| ic_name | character varying(25) |
| department_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| ic_color | character varying(25) |
| ic_size | character varying(25) |
| ic_character | character varying(25) |
| ic_pattern | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| doc_group | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_formular

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| wage | numeric |
| cost | numeric |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_formular_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| formular_code | character varying(25) |
| ic_code | character varying(25) |
| ic_name | character varying(100) |
| unit_code | character varying(10) |
| qty | numeric |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_grade

แถวโดยประมาณ: 4

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
| guid | uuid |

## ic_group

แถวโดยประมาณ: 8

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
| sort_order | smallint |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_group_sub

แถวโดยประมาณ: 220

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| sub_no | integer |
| status | smallint |
| guid_code | character varying(35) |
| main_group | character varying(25) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_group_sub2

แถวโดยประมาณ: 27

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| sub_no | integer |
| status | smallint |
| guid_code | character varying(35) |
| main_group | character varying(25) |
| ic_group_sub_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_hidden_cost_process

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying |
| doc_date | date |
| doc_time | character varying(10) |
| guid_code | character varying(50) |
| doc_format_code | character varying(50) |
| total_amount | numeric |
| remark | character varying(255) |
| branch_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| doc_no_adjust | character varying(25) |
| doc_format_code_adjust | character varying(50) |
| cal_hidden_cost_from | integer |
| net_worth | integer |
| value_before_tax | integer |
| cal_hidden_cost_follow | integer |
| product_value | integer |
| qty | integer |

## ic_hidden_cost_process_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| billing_no | character varying(50) |
| billing_date | date |
| remark | character varying(255) |
| item_code | character varying(50) |
| item_value | numeric |
| item_amount | numeric |
| adjust_amount | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| qty | numeric |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| branch_code | character varying(25) |
| stand_value | numeric |
| divide_value | numeric |

## ic_hidden_cost_process_ref

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| ref_type | smallint |
| doc_ref_type | smallint |
| doc_ref_date | date |
| doc_ref_no | character varying(50) |
| doc_ref_amount | numeric |
| create_date_time_now | timestamp without time zone |
| amount_before_vat | numeric |

## ic_import_duty

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

## ic_inventory

แถวโดยประมาณ: 20,485

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| code_old | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| name_eng_1 | character varying(255) |
| name_eng_2 | character varying(255) |
| name_market | character varying(255) |
| name_for_bill | character varying(255) |
| short_name | character varying(255) |
| name_for_pos | character varying(255) |
| name_for_search | character varying(255) |
| item_type | smallint |
| item_category | character varying(25) |
| group_main | character varying(25) |
| item_brand | character varying(25) |
| item_pattern | character varying(25) |
| item_design | character varying(25) |
| item_grade | character varying(25) |
| item_class | character varying(25) |
| item_size | character varying(25) |
| item_color | character varying(25) |
| item_character | character varying(25) |
| item_status | smallint |
| unit_type | smallint |
| cost_type | smallint |
| tax_type | smallint |
| item_sale_type | smallint |
| item_rent_type | smallint |
| unit_standard | character varying(25) |
| unit_cost | character varying(25) |
| income_type | character varying(25) |
| description | character varying(255) |
| item_model | character varying(50) |
| ic_serial_no | smallint |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| last_movement_date | date |
| average_cost | numeric |
| item_in_stock | numeric |
| balance_qty | numeric |
| accrued_in_qty | numeric |
| accrued_out_qty | numeric |
| unit_standard_name | character varying(100) |
| update_price | smallint |
| update_detail | smallint |
| account_code_1 | character varying(25) |
| account_code_2 | character varying(25) |
| account_code_3 | character varying(25) |
| account_code_4 | character varying(25) |
| book_out_qty | numeric |
| doc_format_code | character varying(25) |
| unit_standard_stand_value | numeric |
| unit_standard_divide_value | numeric |
| sign_code | character varying(25) |
| supplier_code | character varying(25) |
| fixed_cost | numeric |
| drink_type | smallint |
| average_cost_1 | numeric |
| group_sub | character varying(25) |
| use_expire | smallint |
| barcode_checker_print | smallint |
| print_order_per_unit | smallint |
| production_period | smallint |
| is_new_item | smallint |
| commission_rate | character varying(50) |
| is_eordershow | smallint |
| no_discount | smallint |
| serial_no_format | character varying(255) |
| pos_no_sum | smallint |
| item_promote | smallint |
| sum_sale_1 | numeric |
| is_speech | smallint |
| medicine_register_number | character varying(50) |
| medicine_standard_code | character varying(50) |
| quantity | character varying(50) |
| degree | character varying(50) |
| is_product_boonrawd | smallint |
| tpu_code | character varying(20) |
| gpu_code | character varying(20) |
| group_sub2 | character varying(25) |
| ic_discount_group | character varying(25) |
| name_from_remark | smallint |
| manufacturer_code | character varying(25) |
| create_datetime | timestamp without time zone |
| last_update_date_time | timestamp without time zone |
| create_code | character varying(25) |
| last_update_code | character varying(25) |
| have_take_away | smallint |
| create_date_time_now | timestamp without time zone |
| topping_product | smallint |
| guid | uuid |
| product_age | smallint |
| qty_per_pallet | smallint |
| qc_product | smallint |
| qc_product_retest_day | smallint |
| require_purchase_from_approve_vendor | smallint |
| normal_vendor_max_purchase_qty | numeric |
| qc_product_retest_month | smallint |
| qc_product_retest_year | smallint |
| is_pharma_serialization | smallint |

## ic_inventory_append

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_append_code | character varying(25) |
| ic_append_name | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_append_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_append_code | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_inventory_barcode

แถวโดยประมาณ: 13

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| barcode | character varying(30) |
| description | character varying(255) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| price | numeric |
| status | smallint |
| guid_code | character varying(35) |
| line_number | integer |
| price_2 | numeric |
| price_3 | numeric |
| price_4 | numeric |
| hidden_text | smallint |
| price_member | numeric |
| price_member_2 | numeric |
| price_member_3 | numeric |
| price_member_4 | numeric |
| no_point | smallint |
| create_date_time_now | timestamp without time zone |
| guid | uuid |
| creator_code | character varying(255) |
| doc_no | character varying(255) |
| is_clearance | smallint |
| from_date | date |
| to_date | date |

## ic_inventory_barcode_condition

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| barcode | character varying(25) |
| condition_1 | character varying(255) |
| condition_2 | character varying(255) |
| condition_3 | character varying(255) |
| condition_4 | character varying(255) |
| condition_5 | character varying(255) |
| condition_6 | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_barcode_price

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| barcode | character varying(25) |
| discount_type | integer |
| discount_word | character varying(25) |
| qty_begin | integer |
| qty_end | integer |
| date_begin | date |
| date_end | date |
| status | smallint |
| priority | smallint |
| guid_code | character varying(35) |
| lock_discount | smallint |
| lock_code_list | character varying(1000) |
| lock_day | character varying(1000) |
| create_date_time_now | timestamp without time zone |
| doc_no | character varying(255) |
| creator_code | character varying(255) |

## ic_inventory_barcode_price_temp

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| lock_code_list | character varying(255) |
| barcode | character varying(50) |
| qty_begin | integer |
| qty_end | integer |
| date_begin | date |
| date_end | date |
| discount_type | integer |
| discount_word | character varying(50) |
| status | smallint |
| priority | smallint |
| lock_discount | smallint |

## ic_inventory_bundle

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| line_number | smallint |
| ic_code_bundle | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| barcode | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_detail

แถวโดยประมาณ: 20,485

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| formular | character varying(25) |
| po_over | integer |
| so_over | integer |
| account_group | character varying(25) |
| serial_number | character varying(25) |
| tax_import | character varying(100) |
| tax_rate | numeric |
| purchase_manager | character varying(25) |
| sale_manager | character varying(25) |
| start_purchase_wh | character varying(25) |
| start_purchase_shelf | character varying(25) |
| start_purchase_unit | character varying(25) |
| start_sale_wh | character varying(25) |
| start_sale_shelf | character varying(25) |
| start_sale_unit | character varying(25) |
| cost_produce | numeric |
| cost_standard | numeric |
| unit_for_stock | character varying(25) |
| ic_out_wh | character varying(25) |
| ic_out_shelf | character varying(25) |
| ic_reserve_wh | character varying(25) |
| reserve_status | smallint |
| discount | character varying(50) |
| purchase_point | numeric |
| unit_2_code | character varying(25) |
| unit_2_qty | integer |
| unit_2_average | smallint |
| unit_2_average_value | numeric |
| user_group_for_purchase | character varying(25) |
| user_group_for_sale | character varying(25) |
| user_group_for_manage | character varying(25) |
| user_group_for_warehouse | character varying(25) |
| user_status | smallint |
| close_reason | character varying(255) |
| close_date | date |
| ref_file_1 | character varying(255) |
| ref_file_2 | character varying(255) |
| ref_file_3 | character varying(255) |
| ref_file_4 | character varying(255) |
| ref_file_5 | character varying(255) |
| dimension_1 | character varying(25) |
| dimension_2 | character varying(25) |
| dimension_3 | character varying(25) |
| dimension_4 | character varying(25) |
| dimension_5 | character varying(25) |
| dimension_6 | character varying(25) |
| dimension_7 | character varying(25) |
| dimension_8 | character varying(25) |
| dimension_9 | character varying(25) |
| dimension_10 | character varying(25) |
| sale_price_1 | numeric |
| sale_price_2 | numeric |
| sale_price_3 | numeric |
| sale_price_4 | numeric |
| maximum_qty | numeric |
| minimum_qty | numeric |
| dimension_11 | character varying(25) |
| dimension_12 | character varying(25) |
| dimension_13 | character varying(25) |
| dimension_14 | character varying(25) |
| dimension_15 | character varying(25) |
| dimension_16 | character varying(25) |
| dimension_17 | character varying(25) |
| dimension_18 | character varying(25) |
| dimension_19 | character varying(25) |
| dimension_20 | character varying(25) |
| accrued_control | smallint |
| lock_price | smallint |
| lock_discount | smallint |
| lock_cost | smallint |
| is_end | smallint |
| is_hold_purchase | smallint |
| is_hold_sale | smallint |
| is_stop | smallint |
| balance_control | smallint |
| have_point | smallint |
| start_unit_code | character varying(25) |
| dimension_21 | character varying(255) |
| dimension_22 | character varying(255) |
| dimension_23 | character varying(255) |
| dimension_24 | character varying(255) |
| dimension_25 | character varying(255) |
| is_premium | smallint |
| dimension_26 | character varying(255) |
| dimension_27 | character varying(255) |
| dimension_28 | character varying(255) |
| dimension_29 | character varying(255) |
| dimension_30 | character varying(255) |
| dimension_31 | character varying(255) |
| dimension_32 | character varying(255) |
| dimension_33 | character varying(255) |
| dimension_34 | character varying(255) |
| dimension_35 | character varying(255) |
| dimension_36 | character varying(255) |
| dimension_37 | character varying(255) |
| dimension_38 | character varying(255) |
| dimension_39 | character varying(255) |
| dimension_40 | character varying(255) |
| dimension_41 | character varying(255) |
| dimension_42 | character varying(255) |
| dimension_43 | character varying(255) |
| dimension_44 | character varying(255) |
| dimension_45 | character varying(255) |
| before_sale_unit | character varying(25) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |
| image_count | smallint |

## ic_inventory_discount

แถวโดยประมาณ: 218

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| from_qty | numeric |
| to_qty | numeric |
| from_date | date |
| to_date | date |
| sale_type | smallint |
| transport_type | smallint |
| discount | character varying(255) |
| status | smallint |
| discount_type | integer |
| cust_code | character varying(25) |
| cust_group_1 | character varying(25) |
| cust_group_2 | character varying(25) |
| discount_mode | smallint |
| olddate | character varying(55) |
| line_number | integer |
| create_date_time_now | timestamp without time zone |
| price_currency | smallint |
| currency_code | character varying(25) |

## ic_inventory_level

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| barcode | character varying(25) |
| level_1 | character varying(50) |
| level_2 | character varying(50) |
| level_3 | character varying(50) |
| level_4 | character varying(50) |
| price | numeric |
| suggest_remark | character varying(255) |
| option | character varying(255) |
| create_date_time_now | timestamp without time zone |
| sort_order | numeric |

## ic_inventory_lot

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| mfd_date | date |
| exp_date | date |
| mfn_name | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_package

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(50) |
| code | character varying(50) |
| stand_value | numeric |
| divide_value | numeric |
| price | numeric |
| create_date_time_now | timestamp without time zone |

## ic_inventory_permission

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| ib | smallint |
| if | smallint |
| rim | smallint |
| wsdw | smallint |
| wsdd | smallint |
| io | smallint |
| pu | smallint |
| pa | smallint |
| pi | smallint |
| ir | smallint |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| st | smallint |

## ic_inventory_pictures

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| ic_code | character varying(50) |
| member_id | character varying(50) |
| picture_name | character varying(100) |
| sort_list | smallint |
| date_save | date |
| create_date_time_now | timestamp without time zone |

## ic_inventory_price

แถวโดยประมาณ: 23,923

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| from_qty | numeric |
| to_qty | numeric |
| from_date | date |
| to_date | date |
| sale_type | smallint |
| transport_type | smallint |
| sale_price1 | numeric |
| status | smallint |
| price_type | integer |
| cust_code | character varying(25) |
| sale_price2 | numeric |
| cust_group_1 | character varying(25) |
| cust_group_2 | character varying(25) |
| price_mode | smallint |
| olddate | character varying(55) |
| line_number | integer |
| price_currency | smallint |
| currency_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| doc_no | character varying(255) |
| creator_code | character varying(255) |

## ic_inventory_price_formula

แถวโดยประมาณ: 19,501

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| sale_type | smallint |
| price_0 | character varying(50) |
| price_1 | character varying(50) |
| price_2 | character varying(50) |
| price_3 | character varying(50) |
| price_4 | character varying(50) |
| price_5 | character varying(50) |
| price_6 | character varying(50) |
| price_7 | character varying(50) |
| price_8 | character varying(50) |
| price_9 | character varying(50) |
| tax_type | smallint |
| price_currency | smallint |
| currency_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| creator_code | character varying(255) |
| doc_no | character varying(255) |

## ic_inventory_price_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| branch_code | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(50) |
| department_code | character varying(255) |
| sale_type | smallint |
| date_begin | date |
| date_end | date |
| price_0 | character varying(50) |
| price_1 | character varying(50) |
| price_2 | character varying(50) |
| price_3 | character varying(50) |
| price_4 | character varying(50) |
| price_5 | character varying(50) |
| price_6 | character varying(50) |
| price_7 | character varying(50) |
| price_8 | character varying(50) |
| price_9 | character varying(50) |
| vat_type | smallint |
| price_guid | character varying(255) |
| is_use | smallint |
| qty_begin | numeric |
| qty_end | numeric |
| is_promotion | smallint |
| price_promotion | character varying(255) |
| from_ar_group | character varying(255) |
| to_ar_group | character varying(255) |
| creator_code | character varying |
| doc_no | character varying(255) |
| currency_code | character varying(255) |
| exchange_rate | numeric |
| last_update_price | timestamp without time zone |

## ic_inventory_price_list_log

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| branch_code | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(50) |
| department_code | character varying(255) |
| sale_type | smallint |
| date_begin | date |
| date_end | date |
| price_0 | character varying(50) |
| price_1 | character varying(50) |
| price_2 | character varying(50) |
| price_3 | character varying(50) |
| price_4 | character varying(50) |
| price_5 | character varying(50) |
| price_6 | character varying(50) |
| price_7 | character varying(50) |
| price_8 | character varying(50) |
| price_9 | character varying(50) |
| vat_type | smallint |
| price_guid | character varying(255) |
| is_use | smallint |
| qty_begin | numeric |
| qty_end | numeric |
| is_promotion | smallint |
| price_promotion | character varying(255) |
| from_ar_group | character varying(255) |
| to_ar_group | character varying(255) |
| user_code | character varying(255) |
| exchange_rate | numeric |
| currency_code | character varying(255) |
| doc_no | character varying(255) |
| old_exchange_rate | numeric |
| old_currency_code | character varying(255) |
| old_price_0 | character varying(50) |
| old_price_1 | character varying(50) |
| old_price_2 | character varying(50) |
| old_price_3 | character varying(50) |
| old_price_4 | character varying(50) |
| old_price_5 | character varying(50) |
| old_price_6 | character varying(50) |
| old_price_7 | character varying(50) |
| old_price_8 | character varying(50) |
| old_price_9 | character varying(50) |
| price_promotion_old | character varying(255) |
| old_date_begin | date |
| old_date_end | date |
| old_qty_begin | numeric |
| old_qty_end | numeric |
| last_update_price | timestamp without time zone |
| roworder | integer |
| guid | uuid |

## ic_inventory_price_list_temp

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| branch_code | character varying(255) |
| item_code | character varying(255) |
| unit_code | character varying(50) |
| department_code | character varying(255) |
| sale_type | smallint |
| date_begin | date |
| date_end | date |
| price_0 | character varying(50) |
| price_1 | character varying(50) |
| price_2 | character varying(50) |
| price_3 | character varying(50) |
| price_4 | character varying(50) |
| price_5 | character varying(50) |
| price_6 | character varying(50) |
| price_7 | character varying(50) |
| price_8 | character varying(50) |
| price_9 | character varying(50) |
| vat_type | smallint |
| price_guid | character varying(255) |
| is_use | smallint |
| qty_begin | numeric |
| qty_end | numeric |
| is_promotion | smallint |
| price_promotion | character varying(255) |
| from_ar_group | character varying(255) |
| to_ar_group | character varying(255) |
| doc_no | character varying(255) |
| last_update_price | timestamp without time zone |

## ic_inventory_price_list_temp_doc

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| doc_date | date |
| user_create | character varying |
| is_approved | smallint |
| is_doc | smallint |
| is_active | smallint |
| time_approved | timestamp without time zone |
| last_update_price | timestamp without time zone |
| guid | uuid |
| remark | character varying(255) |

## ic_inventory_price_thai7

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| ic_code | character varying(50) |
| member_id | character varying(50) |
| price_name | character varying(200) |
| price | numeric |
| date_save | date |
| create_date_time_now | timestamp without time zone |

## ic_inventory_purchase_price

แถวโดยประมาณ: 14,186

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| from_qty | numeric |
| to_qty | numeric |
| from_date | date |
| to_date | date |
| sale_type | smallint |
| transport_type | smallint |
| sale_price1 | numeric |
| status | smallint |
| price_type | integer |
| supplier_code | character varying(25) |
| sale_price2 | numeric |
| olddate | character varying(55) |
| discount | character varying(255) |
| create_date_time_now | timestamp without time zone |
| doc_no | character varying(255) |
| creator_code | character varying(255) |

## ic_inventory_remark

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| remark_code | character varying(25) |
| remark_desc | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_replace

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_replace_code | character varying(25) |
| ic_replace_name | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_replace_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_replace_code | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_inventory_replacement

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| ic_replace_code | character varying(25) |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_inventory_set

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_set_code | character varying(25) |
| ic_set_neme | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_inventory_set_detail

แถวโดยประมาณ: 22

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_set_code | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| status | smallint |
| line_number | integer |
| price | numeric |
| sum_amount | numeric |
| barcode | character varying(25) |
| price_ratio | numeric |
| create_date_time_now | timestamp without time zone |

## ic_inventory_suggest

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| ic_suggest_code | character varying(25) |
| line_number | smallint |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_inventory_thai7

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| code | character varying(255) |
| name_1 | character varying(50) |
| item_detail | bytea |
| item_brand | character varying(50) |
| item_model | character varying(50) |
| item_category | character varying(50) |
| item_category_sub | character varying(50) |
| item_wide | character varying(200) |
| item_long | character varying(200) |
| item_high | character varying(200) |
| item_weight | character varying(200) |
| item_in_stock | integer |
| balance_qty | numeric |
| accrued_in_qty | numeric |
| accrued_out_qty | numeric |
| date_save | date |
| date_modified | date |
| affiliate_item | integer |
| import_item | integer |
| is_balance | integer |
| status | integer |
| price_out_qty | numeric |
| create_date_time_now | timestamp without time zone |

## ic_inventory_wh

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_issue_type

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

## ic_lot_manage

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(50) |
| lot_number | character varying(255) |
| sort_order | character varying(10) |
| lot_select | smallint |
| wh_code | character varying(50) |
| shelf_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| mfd_date | date |

## ic_manufacturer_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(50) |
| manufacturer_code | character varying(50) |
| line_number | smallint |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_model

แถวโดยประมาณ: 810

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
| guid | uuid |

## ic_name_billing

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_name_merket

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_name_pos

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_name_short

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_opposite_unit

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| unit_code | character varying(25) |
| stand_value | numeric |
| divide_value | numeric |
| status | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_package_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| trans_type | smallint |
| doc_no | character varying(50) |
| doc_date | date |
| cust_code | character varying(50) |
| doc_ref_no | character varying(50) |
| doc_ref_date | date |
| doc_time | character varying(25) |
| creator_code | character varying(50) |
| create_datetime | timestamp without time zone |
| last_editor_code | character varying(50) |
| lastedit_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## ic_package_trans_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| trans_type | smallint |
| doc_no | character varying(50) |
| doc_date | date |
| cust_code | character varying(25) |
| item_code | character varying(50) |
| item_name | character varying(500) |
| qty | numeric |
| stand_value | numeric |
| divide_value | numeric |
| create_date_time_now | timestamp without time zone |

## ic_pattern

แถวโดยประมาณ: 5

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
| guid | uuid |

## ic_pattern_use

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| ic_code | character varying(25) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_price_adjust_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_price_formula_template

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| price_1 | character varying(50) |
| price_2 | character varying(50) |
| price_3 | character varying(50) |
| price_4 | character varying(50) |
| price_5 | character varying(50) |
| price_6 | character varying(50) |
| price_7 | character varying(50) |
| price_8 | character varying(50) |
| price_9 | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_production_formula

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| date_from | date |
| date_to | date |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_production_formula_material

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| item_code | character varying(25) |
| unit_code | character varying(100) |
| qty | numeric |
| line_number | integer |
| formula_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_production_formula_product

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| item_code | character varying(25) |
| unit_code | character varying(100) |
| qty | numeric |
| line_number | integer |
| formula_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_promotion

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| promote_code | character varying(25) |
| promote_name | character varying(100) |
| promote_type | smallint |
| promote_start | date |
| promote_stop | date |
| description | character varying(255) |
| ar_type | smallint |
| ar_group | smallint |
| ar_code_1 | character varying(25) |
| ar_code_2 | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_promotion_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| promote_code | character varying(25) |
| promote_name | character varying(100) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| qty_1 | numeric |
| qty_2 | numeric |
| promote_price | numeric |
| promote_sum_price | numeric |
| free_ic_code | character varying(25) |
| free_ic_unit | character varying(25) |
| free_qty | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_promotion_formula

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| status | smallint |
| order_number | smallint |
| guid_code | character varying(35) |
| cust_code_condition | smallint |
| cust_group_condition | smallint |
| case_number | smallint |
| member_condition | smallint |
| auto_change_unitcode | smallint |
| lock_promotion | smallint |
| lock_code_list | character varying(1000) |
| is_no_discount | smallint |
| from_date | timestamp without time zone |
| to_date | timestamp without time zone |
| use_date_range | smallint |
| item_normal_price | smallint |
| lock_day | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## ic_promotion_formula_action

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| qty_from | numeric |
| qty_to | numeric |
| action_command | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_promotion_formula_condition

แถวโดยประมาณ: 34

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| condition_case | smallint |
| line_number | smallint |
| condition_from | character varying(50) |
| condition_to | character varying(50) |
| condition_value_from | numeric |
| condition_value_to | numeric |
| condition_type | smallint |
| condition_unit_code | character varying(25) |
| condition_value_qty_from | character(1) |
| unit_type | smallint |
| condition_group | smallint |
| create_date_time_now | timestamp without time zone |

## ic_promotion_formula_group_qty

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| qty | numeric |
| group_number | smallint |
| group_amount | numeric |
| create_date_time_now | timestamp without time zone |

## ic_promotion_formula_price_discount

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| item_code | character varying(50) |
| item_unit | character varying(25) |
| qty_start | numeric |
| price | numeric |
| discount | character varying(50) |
| unit_type | smallint |
| code | character varying(25) |
| line_number | smallint |
| qty_end | numeric |
| create_date_time_now | timestamp without time zone |

## ic_purchase_permium

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| permium_code | character varying(25) |
| name_1 | character varying(100) |
| date_begin | date |
| date_end | date |
| important | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_purchase_permium_condition

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| permium_code | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| stand_value | numeric |
| divide_value | numeric |
| create_date_time_now | timestamp without time zone |

## ic_purchase_permium_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| permium_code | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| create_date_time_now | timestamp without time zone |

## ic_purchase_price

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_group | character varying(25) |
| ap_code | character varying(25) |
| start_date | date |
| stop_date | date |
| tax_group | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_purchase_price_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| credit_code | character varying(25) |
| sending_type | smallint |
| from_qty | numeric |
| to_qty | numeric |
| price | numeric |
| discount | numeric |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_qc_config

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| transfer_quarantine_doc_format_code | character varying(50) |
| transfer_pass_doc_format_code | character varying(50) |
| transfer_reject_doc_format_code | character varying(50) |
| transfer_inprocess_doc_format_code | character varying(50) |
| quarantine_warehouse_code | character varying(50) |
| quarantine_location_code | character varying(50) |
| pass_warehouse_code | character varying(50) |
| pass_location_code | character varying(50) |
| reject_warehouse_code | character varying(50) |
| reject_location_code | character varying(50) |
| inprocess_warehouse_code | character varying(50) |
| inprocess_location_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_qc_container_adjust

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_qc_container_adjustment_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| qty | numeric |
| lab_no | character varying(50) |
| container_no | smallint |
| line_number | smallint |
| lot_number | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_qc_container_transaction

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| doc_date | date |
| item_code | character varying(50) |
| ref_line_number | smallint |
| lab_no | character varying(50) |
| container_no | smallint |
| qty | numeric |
| unit_code | character varying(50) |
| lot_number | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_qc_indentify

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| code | character varying(20) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| lab_no | character varying(50) |
| ref_lab_no | character varying(50) |
| item_code | character varying(50) |
| doc_ref | character varying(50) |
| doc_ref_date | date |
| cust_code | character varying(50) |
| lot_number | character varying(100) |
| mfn_name | character varying(255) |
| mfd_date | date |
| expire_date | date |
| retest_date | date |
| lab_status | smallint |
| ref_doc_type | smallint |
| create_date_time_now | timestamp without time zone |
| identify_by | character varying(255) |
| container_qty | numeric |
| qty | numeric |
| unit_code | character varying(50) |
| container_weight | numeric |
| create_date | date |
| doc_line_number | smallint |
| move_lab_status | smallint |
| move_lab_no | character varying(50) |

## ic_qc_lab_beginning_balance

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(50) |
| doc_no | character varying(50) |
| doc_date | date |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_beginning_balance_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(25) |
| qty | numeric |
| lot_number | character varying(50) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_beginning_balance_lab

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| ref_row | smallint |
| item_code | character varying(50) |
| lot_number | character varying(50) |
| lab_no | character varying(50) |
| retest_date | date |
| unit_code | character varying(25) |
| identify_by | character varying(255) |
| qty | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_beginning_balance_lab_container

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying |
| item_code | character varying |
| lab_no | character varying |
| container_no | smallint |
| qty | numeric |
| line_number | smallint |
| qc_status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_container

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| lab_no | character varying(50) |
| container_no | smallint |
| container_pack_size | numeric |
| line_number | smallint |
| lab_status | smallint |
| create_date_time_now | timestamp without time zone |
| container_balance_qty | numeric |

## ic_qc_lab_container_issue

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_cut

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(255) |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| remark | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_cut_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| item_code | character varying(50) |
| qty | numeric |
| unit_code | character varying(25) |
| line_number | smallint |
| lab_no | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_qc_lab_transaction

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| doc_date | date |
| item_code | character varying(50) |
| ref_line_number | smallint |
| lab_no | character varying(50) |
| lot_number | character varying(50) |
| qty | numeric |
| unit_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_qc_purchase_packing_size

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(50) |
| cust_code | character varying(50) |
| guid_code | character varying(50) |
| creator_code | character varying |
| create_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## ic_qc_purchase_packing_size_container

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| container_no | smallint |
| packing_size | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| unit_code | character varying(50) |

## ic_qc_purchase_packing_size_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| total_container | smallint |
| same_size | smallint |
| packing_size | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| unit_code | character varying(50) |
| qty_receive | numeric |
| qty_receive_unit | character varying(50) |
| total_receive_qty | numeric |

## ic_quality_control

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| trans_flag | smallint |
| ic_qc_status | smallint |
| ic_code | character varying(25) |
| lot_number | character varying(100) |
| mfd_date | date |
| exp_date | date |
| lab_no | character varying(100) |
| lab_retest | character varying(100) |
| line_number | smallint |
| mfn | character varying(255) |
| lab_retest_date | date |
| create_date_time_now | timestamp without time zone |
| doc_format_code | character varying(50) |
| guid_code | character varying(60) |
| retest_date | date |
| reject_reason | character varying(255) |
| pass_content | character varying(255) |
| is_not_retest | smallint |
| qty | numeric |
| unit_code | character varying(50) |
| total_container | smallint |
| prev_container | smallint |

## ic_quality_control_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(50) |
| trans_flag | smallint |
| container_no | smallint |
| container_pack_size | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| qty | numeric |
| lab_status | smallint |

## ic_relation

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| total_qty | numeric |
| total_amount | numeric |
| transection_flag | smallint |
| create_date_time_now | timestamp without time zone |

## ic_relation_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| ic_code_1 | character varying(25) |
| qty_1 | numeric |
| line_number_1 | integer |
| doc_ref | character varying(25) |
| ic_code_2 | character varying(25) |
| qty_2 | numeric |
| line_number_2 | integer |
| transection_flag | smallint |
| create_date_time_now | timestamp without time zone |

## ic_report_sort_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## ic_serial

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| serial_number | character varying(50) |
| description | character varying(255) |
| guid_code | character varying(35) |
| void_date | date |
| ic_unit | character varying(25) |
| status | smallint |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| product_year | character varying(4) |
| product_week | character varying(2) |
| car_inventory | character varying(50) |
| car_stockno | character varying(50) |
| car_engineno | character varying(100) |
| car_chassisno | character varying(100) |
| create_date_time_now | timestamp without time zone |

## ic_serial_dimension

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| remark | character varying(255) |
| dimension_no | integer |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_shelf

แถวโดยประมาณ: 469

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| whcode | character varying(10) |
| width | character varying(10) |
| weight | character varying(10) |
| height | character varying(10) |
| depth | character varying(10) |
| status | smallint |
| guid_code | character varying(35) |
| stock_control | smallint |
| remark | character varying(255) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_size

แถวโดยประมาณ: 10

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| width_length_height | character varying(100) |
| weight | character varying(100) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_size_use

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| width_length_height | character varying(100) |
| weight | numeric |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_specific_search

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(50) |
| keyword | character varying(500) |
| line_number | smallint |
| group_type | smallint |
| group_code | character varying(50) |
| sort_order | smallint |
| create_date_time_now | timestamp without time zone |

## ic_specific_search_word

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| keyword | character varying(500) |
| guid_code | character varying(35) |
| engine_valve | character varying(25) |
| displacement | character varying(25) |
| market_names | character varying(1000) |
| remark | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## ic_standard_cost

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| unit_code | character varying(25) |
| date_start | date |
| cost1 | numeric |
| create_date_time_now | timestamp without time zone |

## ic_stk_adjust_reason

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

## ic_stk_build

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
| ic_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| wage | numeric |
| cost | numeric |
| qty | numeric |
| person_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_stk_build_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| ic_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| unit_code | character varying(25) |
| qty | numeric |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_stock_count

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| doc_date | date |
| doc_time | time without time zone |
| trans_flag | smallint |
| cust_code | character varying(200) |
| wh_code | character varying(200) |
| branch_code | character varying(200) |
| creator_code | character varying(255) |
| create_datetime | timestamp without time zone |

## ic_stock_count_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| doc_date | date |
| doc_time | time without time zone |
| trans_flag | smallint |
| item_code | character varying(200) |
| item_name | character varying(200) |
| unit_code | character varying(200) |
| barcode | character varying(200) |
| qty | numeric |
| line_number | smallint |
| wh_code | character varying(200) |
| shelf_code | character varying(200) |
| creator_code | character varying(255) |
| create_datetime | timestamp without time zone |

## ic_trans

แถวโดยประมาณ: 16

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
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
| total_amount | numeric |
| balance_amount | numeric |
| adjust_reason | character varying(25) |
| approve_code | character varying(25) |
| approve_date | date |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| user_request | character varying(25) |
| expire_day | integer |
| send_mail | smallint |
| send_sms | smallint |
| doc_ref_trans | character varying(25) |
| credit_date | date |
| total_before_vat | numeric |
| doc_time | character varying(5) |
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
| doc_format_code | character varying(25) |
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
| address_name | character varying(255) |
| address | text |
| doc_copy_reason_type | smallint |

## ic_trans_additional

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| trans_flag | smallint |
| deliveryday | character varying(10) |
| ssfquantity | character varying(10) |
| cust_id | character varying(25) |
| custcode | character varying(25) |
| web_order_id | character varying(25) |
| district1_name | character varying(255) |
| district2_name | character varying(255) |
| province_name | character varying(255) |
| custlat | numeric |
| custlng | numeric |
| custemail | character varying(255) |
| custbusinesstel | character varying(100) |
| custmobile | character varying(100) |
| orderdetail | character varying(255) |
| ordertype | character varying(10) |
| firstorder | character varying(10) |
| orderpaymenttype | character varying(10) |
| deliveryaddressid | character varying(50) |
| orderdeliverydate | timestamp without time zone |
| custrefcode | character varying(25) |
| paymentdate | timestamp without time zone |
| orderdate | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail

แถวโดยประมาณ: 11

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| cust_code | character varying(25) |
| inquiry_type | smallint |
| item_code | character varying(25) |
| item_name | character varying(255) |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| discount | character varying(25) |
| sum_of_cost | numeric |
| sum_amount | numeric |
| due_date | date |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
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
| doc_time | character varying(5) |
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

## ic_trans_detail_allocate

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | integer |
| allocate_code | character varying(25) |
| ratio | numeric |
| amount | numeric |
| line_number | integer |
| doc_line_number | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_commission

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| trans_flag | smallint |
| item_code | character varying(50) |
| commission | character varying(25) |
| commission_amount | numeric |
| creator_code | character varying(25) |
| create_datetime | timestamp without time zone |
| last_editor_code | character varying(25) |
| lastedit_datetime | timestamp without time zone |
| line_number | smallint |
| remark | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_department

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| department_code | character varying(25) |
| ratio | numeric |
| amount | numeric |
| line_number | integer |
| doc_line_number | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_draft

แถวโดยประมาณ: 14

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| cust_code | character varying(25) |
| inquiry_type | smallint |
| item_code | character varying(25) |
| item_name | character varying(255) |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| discount | character varying(25) |
| sum_of_cost | numeric |
| sum_amount | numeric |
| due_date | date |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
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
| doc_time | character varying(5) |
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
| price_guid | character varying(60) |
| is_lock_cost | smallint |
| create_date_time_now | timestamp without time zone |
| discount_amount_2 | numeric |
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
| mfn_code | character varying(50) |
| promotion_code | character varying(50) |

## ic_trans_detail_jobs

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| job_code | character varying(25) |
| ratio | numeric |
| amount | numeric |
| line_number | smallint |
| doc_line_number | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_lot

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| doc_no | character varying(25) |
| doc_date | timestamp without time zone |
| lot_number | character varying(50) |
| item_code | character varying(25) |
| qty | numeric |
| price | numeric |
| amount | numeric |
| line_number | smallint |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| calc_flag | smallint |
| doc_time | character varying(5) |
| expire_date | date |
| mfd_date | date |
| mfn_name | character varying(255) |
| doc_line_number | smallint |
| product_year | character varying(25) |
| product_week | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_project

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| project_code | character varying(25) |
| ratio | numeric |
| amount | numeric |
| line_number | integer |
| doc_line_number | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_promotion

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| doc_ref | character varying(25) |
| doc_ref_date | date |
| trans_flag | smallint |
| promotion_code | character varying(25) |
| promotion_name | character varying(255) |
| qty | numeric |
| price | numeric |
| sum_amount | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_site

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| site_code | character varying |
| ratio | numeric |
| amount | numeric |
| line_number | integer |
| doc_line_number | smallint |
| ic_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ic_trans_detail_temp

แถวโดยประมาณ: 65

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| trans_flag | smallint |
| item_code | character varying(50) |
| item_name | character varying(500) |
| qty | numeric |
| price | numeric |
| sum_amount | numeric |
| line_number | smallint |
| time_add | timestamp without time zone |
| unit_code | character varying(25) |
| barcode | character varying(50) |
| doc_time | character varying(25) |
| wh_code | character varying(50) |
| shelf_code | character varying(50) |
| wh_code_2 | character varying(50) |
| shelf_code_2 | character varying(50) |
| user_code | character varying(50) |
| success_status | smallint |
| create_date_time_now | timestamp without time zone |

## ic_trans_discount_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| trans_flag | smallint |
| discount_group_code | character varying(25) |
| discount_group_name | character varying(255) |
| discount_word | character varying(100) |
| group_amount | numeric |
| discount_amount | numeric |
| create_date_time_now | timestamp without time zone |

## ic_trans_draft

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
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
| total_amount | numeric |
| balance_amount | numeric |
| adjust_reason | character varying(25) |
| approve_code | character varying(25) |
| approve_date | date |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| user_request | character varying(25) |
| expire_day | integer |
| send_mail | smallint |
| send_sms | smallint |
| doc_ref_trans | character varying(25) |
| credit_date | date |
| total_before_vat | numeric |
| doc_time | character varying(5) |
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
| doc_format_code | character varying(25) |
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
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
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
| cancel_code | character varying(25) |
| cancel_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
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
| doc_copy_reason_type | smallint |

## ic_trans_pos_campaign

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| doc_date | date |
| pos_id | character varying(50) |
| campaign_code | character varying(50) |
| qty | integer |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_trans_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## ic_trans_serial_number

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| serial_number | character varying(50) |
| ic_code | character varying(25) |
| description | character varying(255) |
| void_date | timestamp without time zone |
| doc_no | character varying(25) |
| trans_flag | integer |
| unit_code | character varying(25) |
| line_number | integer |
| doc_line_number | smallint |
| last_status | smallint |
| doc_date | date |
| doc_time | character varying(5) |
| calc_flag | smallint |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| wh_code_2 | character varying(25) |
| shelf_code_2 | character varying(25) |
| price | numeric |
| cust_code | character varying(25) |
| inquiry_type | smallint |
| product_year | character varying(4) |
| product_week | character varying(2) |
| car_inventory | character varying(50) |
| car_stockno | character varying(50) |
| car_engineno | character varying(100) |
| car_chassisno | character varying(100) |
| create_date_time_now | timestamp without time zone |

## ic_trans_shipment

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| trans_flag | smallint |
| cust_code | character varying(25) |
| transport_name | character varying(255) |
| transport_address | character varying(1000) |
| transport_telephone | character varying(100) |
| transport_fax | character varying(100) |
| transport_tambon | character varying(255) |
| transport_amper | character varying(255) |
| transport_province | character varying(255) |
| transport_country | character varying(255) |
| transport_code | character varying(25) |
| destination | character varying(255) |
| remark | character varying(255) |
| remark_2 | character varying(255) |
| ship_code | character varying(50) |
| logistic_area | character varying(50) |
| latitude | numeric |
| longitude | numeric |
| create_date_time_now | timestamp without time zone |
| zipcode | character varying(10) |

## ic_trans_temp

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| trans_flag | smallint |
| cust_code | character varying(50) |
| wh_code | character varying(50) |
| shelf_code | character varying(50) |
| location_code | character varying(255) |
| doc_time | character varying(10) |
| wh_code_2 | character varying(50) |
| shelf_code_2 | character varying(50) |
| creator_code | character varying(255) |
| last_editor_code | character varying(255) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
| branch_code | character varying(255) |
| user_code | character varying(255) |
| last_status | smallint |

## ic_type

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

## ic_unit

แถวโดยประมาณ: 113

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
| guid | uuid |

## ic_unit_type

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

## ic_unit_use

แถวโดยประมาณ: 20,842

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| line_number | integer |
| stand_value | numeric |
| divide_value | numeric |
| ratio | numeric |
| row_order | integer |
| width_length_height | character varying(100) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| weight | character varying(100) |
| status | smallint |
| unit_size | numeric |
| create_date_time_now | timestamp without time zone |
| guid | uuid |

## ic_warehouse

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| address | character varying(255) |
| telephone | character varying(50) |
| fax | character varying(50) |
| user_group | character varying(10) |
| wh_manager | character varying(25) |
| status | smallint |
| guid_code | character varying(35) |
| branch_code | character varying(25) |
| branch_use | character varying(500) |
| create_date_time_now | timestamp without time zone |
| guid | uuid |
| latitude | numeric |
| longitude | numeric |

## ic_warehouse_location_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| wh_code | character varying(25) |
| location_group | character varying(25) |
| name_1 | character varying(255) |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ic_warehouse_location_group_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| wh_code | character varying(25) |
| location_group | character varying(25) |
| location | character varying(25) |
| priolity | smallint |
| create_date_time_now | timestamp without time zone |

## ic_weight_cost

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
| weight_by | smallint |
| bill_start | character varying(25) |
| bill_stop | character varying(25) |
| weight_method | smallint |
| amount | numeric |
| description | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ic_weight_cost_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| bill_date | date |
| bill_no | character varying(25) |
| amount | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ic_wh_shelf

แถวโดยประมาณ: 469

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| max_point | numeric |
| min_point | integer |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| shelf_list | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ic_wms_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
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
| total_amount | numeric |
| balance_amount | numeric |
| adjust_reason | character varying(25) |
| approve_code | character varying(25) |
| approve_date | date |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| user_request | character varying(25) |
| expire_day | integer |
| send_mail | smallint |
| send_sms | smallint |
| doc_ref_trans | character varying(25) |
| credit_date | date |
| total_before_vat | numeric |
| doc_time | character varying(5) |
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
| doc_format_code | character varying(25) |
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
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| is_cancel | smallint |
| cancel_code | character varying(255) |
| cancel_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## ic_wms_trans_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| trans_flag | smallint |
| doc_group | character varying(25) |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| cust_code | character varying(25) |
| inquiry_type | smallint |
| item_code | character varying(25) |
| item_name | character varying(255) |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| discount | character varying(25) |
| sum_of_cost | numeric |
| sum_amount | numeric |
| due_date | date |
| remark | character varying(255) |
| status | smallint |
| line_number | smallint |
| ref_doc_no | character varying(25) |
| ref_doc_date | date |
| ref_line_number | smallint |
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
| doc_time | character varying(5) |
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
| lot_number_1 | character varying(25) |
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
| price_guid | character varying(50) |
| create_date_time_now | timestamp without time zone |
