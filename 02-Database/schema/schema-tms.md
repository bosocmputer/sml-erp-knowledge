---
tags: [sml, schema, tms, generated]
---
# ตารางกลุ่ม `tms` (kbyt)

กลับไป [[schema-index]]

## tms_car_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name | character varying(255) |

## tms_car_maintenance

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| tran_flag | character varying(25) |
| doc_no | character varying(25) |
| doc_date | date |
| car_license_no | character varying(25) |
| car_description | character varying(255) |
| car_type_code | character varying(25) |
| po_no | integer |
| po_date | date |
| exp_no | character varying(20) |
| exp_date | date |
| car_owner | smallint |
| car_driver | character varying(25) |
| car_dep_code | character varying(25) |
| car_branch_code | character varying(25) |
| lubricator_change | smallint |
| oil_filter_change | smallint |
| air_filter_change | smallint |
| chang_date | date |
| mile_change | integer |
| mile_next_ma | integer |
| next_ma_date | date |
| ap_code | character varying(25) |
| total_expense | numeric |
| spare_part_cost | numeric |
| overhead_cost | numeric |
| description | character varying(255) |
| remark | character varying(255) |
| complete_date | date |
| mile_gas | numeric |
| mile_last | numeric |
| mile_number | numeric |
| gas_amount | numeric |
| lite_number | numeric |
| lite_price | numeric |
| km_per_lite | numeric |
| consumption | numeric |
| lite_expectation_fill | numeric |
| gas_lost | numeric |
| gas_type | character varying(50) |
| from_date | timestamp without time zone |
| to_date | timestamp without time zone |
| reason_code | character varying(25) |
| reason_name | character varying(255) |
| lite_price_before | numeric |
| lite_number_before | numeric |
| lite_total_price | numeric |
| doc_ref | character varying(25) |
| branch_code | character varying(25) |
| is_complete | smallint |

## tms_car_master

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| car_license_no | character varying(25) |
| car_description | character varying(255) |
| car_type_code | character varying(25) |
| car_brand | character varying(25) |
| car_model | character varying(25) |
| car_axle | smallint |
| car_cc | smallint |
| car_hp | smallint |
| car_owner | smallint |
| car_driver | character varying(25) |
| car_weight_institutions | smallint |
| car_branch_code | character varying(25) |
| province | character varying(50) |
| car_group_code | character varying(25) |
| is_disable | smallint |
| car_caretaker | character varying(25) |
| car_use_by | character varying(25) |
| std_val_per_km | numeric |

## tms_car_master_image

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| car_license_no | character varying(25) |
| image_file | bytea |
| guid | character varying(35) |
| created_at | timestamp without time zone |
| updated_at | timestamp without time zone |

## tms_car_type

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| car_type_code | character varying(25) |
| car_type_name | character varying(255) |

## tms_config_date

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| begin_date | date |
| date_flag | integer |
| code | character varying(255) |
| ignore_sync | integer |
| is_lock_record | integer |

## tms_driver_master

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| code | character varying(25) |
| first_name | character varying(200) |
| last_name | character varying(200) |
| gender | smallint |
| address | character varying(255) |
| phone_no | character varying(50) |
| line_id | character varying(50) |
| id_card | character varying(50) |
| branch_code | character varying(25) |
| is_disable | smallint |

## tms_que_shipment

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| req_que_date | date |
| branch | character varying(25) |
| req_del_date | date |
| round_no | integer |
| actual_del_date | date |
| car_code | character varying(25) |
| car_cate_code | character varying(25) |
| driver_code | character varying(25) |
| item_weight | integer |
| weight_capacity | integer |
| available_weight | integer |
| start_location | character varying(100) |
| end_location | character varying(100) |
| start_latitude | character varying(10) |
| start_longitude | character varying(10) |
| end_latitude | character varying(10) |
| end_longitude | character varying(10) |
| shipment_status | smallint |
| start_mile_number | integer |
| end_mile_number | integer |
| distance | integer |
| time | time without time zone |
| no_staff | smallint |
| creator_code | character varying(25) |
| create_date_time | timestamp without time zone |
| last_editor_code | character varying(25) |
| last_edit_date | timestamp without time zone |
| confirm_code | character varying(25) |
| confirm_date_time | timestamp without time zone |
| cancel_code | character varying(25) |
| cancel_date_time | timestamp without time zone |
| finished_code | character varying(25) |
| finished_date_time | timestamp without time zone |
| shipping_pay | numeric |
| shipping_recieve | numeric |
| remark | character varying(255) |
| route_code | character varying(25) |
| approve_car_code | character varying(25) |
| approve_car_date_time | timestamp without time zone |
| car_group_code | character varying(25) |
| reason_code | character varying(25) |
| reason_name | character varying(255) |
| expect_date | timestamp without time zone |
| receive_date | timestamp without time zone |
| remark_special | character varying(255) |
| special_total_mile | integer |
| sum_amount | numeric |
| sum_amount_discount | numeric |

## tms_que_shipment_department

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| department_code | character varying(25) |

## tms_que_shipment_details

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| req_del_date | date |
| actual_del_date | date |
| ref_doc_no | character varying(25) |
| ar_code | character varying(25) |
| shipment_sequense | smallint |
| line_number | smallint |
| item_code | character varying(25) |
| item_name | character varying(255) |
| item_weight | integer |
| qty | numeric |
| qty_stale | numeric |
| qty_deliver | numeric |
| unit_code | character varying(25) |
| shipment_status | smallint |
| creator_code | character varying(25) |
| create_date_time | date |
| last_editor_code | character varying(25) |
| last_edit_date | timestamp without time zone |
| confirm_code | character varying(25) |
| confirm_date_time | timestamp without time zone |
| cancel_code | character varying(25) |
| cancel_date_time | timestamp without time zone |
| finished_code | character varying(25) |
| finished_date_time | timestamp without time zone |
| ar_logistic_area_code | character varying(25) |
| department_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| line_number_origin | smallint |
| price | numeric |
| sum_amount | numeric |
| trans_flag | smallint |
| approve_car_code | character varying(25) |
| approve_car_date_time | timestamp without time zone |
| sale_code | character varying(25) |
| item_guid | uuid |
| is_pos | smallint |
| ref_send_date | date |
| discount | character varying(200) |
| sum_amount_discount | numeric |
| item_type | smallint |
| reason_code | character varying(25) |
| reason_name | character varying(255) |
| remark | character varying(255) |

## tms_que_shipment_log

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | integer |
| doc_no | character varying(25) |
| expect_date | timestamp without time zone |
| shipment_status | integer |
| car_code | character varying(25) |
| car_round | integer |
| user_code | character varying(25) |
| brach_login | character varying(25) |
| action_name | character varying(30) |
| transaction_at | timestamp without time zone |
| doc_detail | character varying |

## tms_que_shipment_staff

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| staff_code | character varying(25) |

## tms_reason

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| reason_flag | smallint |
| code | character varying(25) |
| name | character varying(255) |

## tms_refuel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_no_request | character varying(25) |
| branch_code | character varying(25) |

## tms_request_refuel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| car_license_no | character varying(25) |
| oil_type | character varying(50) |
| oil_price | numeric |
| oil_qty | numeric |
| oil_price_before | numeric |
| oil_qty_before | numeric |
| mile_number | integer |
| mile_number_before | integer |
| total_price | numeric |
| creator_code | character varying(25) |
| create_at | timestamp without time zone |
| is_use | smallint |
| branch_code | character varying(25) |

## tms_route

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| route_code | character varying(25) |
| route_name | character varying(255) |
| route_branch | character varying(25) |

## tms_route_details

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| route_code | character varying(25) |
| route_area | character varying(25) |
| line_number | smallint |

## tms_route_sub

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| route_code | character varying(25) |
| route_sub_code | character varying(25) |

## tms_send_assign

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| doc_no | character varying(25) |
| doc_date | date |
| inquiry_type | smallint |
| cust_code | character varying(25) |
| branch_code | character varying(25) |
| department_code | character varying(25) |
| sale_code | character varying(25) |
| send_type | smallint |
| send_date | date |
| total_amount | numeric |
| creator_code | character varying(25) |
| create_datetime | timestamp without time zone |
| logistic_area | character varying(25) |
| is_pos | smallint |
| guid | uuid |
| doc_mode | smallint |
| create_by | character varying(25) |
| create_at | timestamp without time zone |
| last_edit_by | character varying(25) |
| last_edit_at | timestamp without time zone |
| remark | character varying(255) |
| assign_remark | character varying(255) |
| ref_doc_no | character varying(25) |

## tms_send_assign_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| doc_no | character varying(25) |
| doc_date | date |
| inquiry_type | smallint |
| item_code | character varying(25) |
| item_name | character varying(255) |
| unit_code | character varying(25) |
| qty | numeric |
| price | numeric |
| sum_amount | numeric |
| line_number | integer |
| branch_code | character varying(25) |
| logistic_area | character varying(50) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| department_code | character varying(25) |
| sale_code | character varying(25) |
| creator_code | character varying(25) |
| create_datetime | timestamp without time zone |
| assign_guid | uuid |
| guid | uuid |
| discount | character varying(200) |
| item_type | smallint |
| ref_doc_no | character varying(25) |

## tms_service_job

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| job_name_code | character varying(25) |
| que_doc_code | character varying(25) |
| user_service | character varying(100) |
| start_location | character varying(100) |
| end_location | character varying(100) |
| distance | integer |
| remark | character varying(2555) |

## tms_service_job_name

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| code | character varying(25) |
| name | character varying(2555) |
| is_deleted | smallint |
