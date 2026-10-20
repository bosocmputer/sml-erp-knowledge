---
tags: [sml, schema, ar, generated]
---
# ตารางกลุ่ม `ar` (kbyt)

กลับไป [[schema-index]]

## ar_channel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_close_reason

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| save_code | character varying(25) |
| save_date | date |
| edit_code | character varying(25) |
| edit_date | date |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_contact_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_contactor

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| name | character varying(100) |
| address | character varying(255) |
| telephone | character varying(50) |
| mobile | character varying(50) |
| email | character varying(50) |
| work_title | character varying(100) |
| work_department | character varying(100) |
| officer_group | character varying(25) |
| line_number | integer |
| group_contactor | character varying(25) |
| remark_1 | character varying(255) |
| remark_2 | character varying(255) |
| remark_3 | character varying(255) |
| remark_4 | character varying(255) |
| remark_5 | character varying(255) |
| remark_6 | character varying(255) |
| create_date_time_now | timestamp without time zone |

## ar_credit_approve

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

## ar_credit_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| credit_money | numeric |
| credit_max | numeric |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_credit_group_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| credit_group | character varying(25) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ar_credit_pay_bill

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| credit_day | smallint |
| day_to_due | smallint |
| month_to_due | smallint |
| day_to_close | smallint |
| month_to_close | smallint |
| line_number | integer |
| day_to_noties | smallint |
| month_to_noties | smallint |
| day_to_noties_2 | smallint |
| month_to_noties_2 | smallint |
| create_date_time_now | timestamp without time zone |

## ar_customer

แถวโดยประมาณ: 27,790

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
| address | character varying(255) |
| address_eng | character varying(255) |
| tambon | character varying(25) |
| amper | character varying(25) |
| province | character varying(25) |
| zip_code | character varying(10) |
| telephone | character varying(150) |
| fax | character varying(50) |
| email | character varying(150) |
| website | character varying(150) |
| description | character varying(255) |
| birth_day | date |
| ar_type | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| ar_status | smallint |
| doc_format_code | character varying(25) |
| prefixname | character varying(15) |
| first_name | character varying(50) |
| last_name | character varying(70) |
| price_level | smallint |
| point_balance | numeric |
| sale_shift_id | character varying(50) |
| sms_phonenumber | character varying(255) |
| home_address | character varying(255) |
| home_name | character varying(255) |
| moo | character varying(25) |
| soi | character varying(255) |
| road | character varying(255) |
| room_no | character varying(50) |
| floor | character varying(25) |
| building | character varying(50) |
| sex | smallint |
| country | character varying(255) |
| register_date | date |
| arm_code | character varying(25) |
| ar_code_main | character varying(50) |
| ar_branch_code | character varying(50) |
| arm_approve | smallint |
| arm_approve_date | date |
| nfc_id | character varying(255) |
| arm_tier | smallint |
| last_update_time | timestamp without time zone |
| interco | character varying(255) |
| arm_register_date | date |
| arm_register | smallint |
| create_datetime | timestamp without time zone |
| last_update_date_time | timestamp without time zone |
| create_code | character varying(50) |
| last_update_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| cis | character varying(255) |
| code_ref1 | character varying(255) |
| guid | uuid |
| ar_tier_code | character varying(25) |
| user_code | character varying(255) |
| password | character varying(255) |
| question_choose | character varying |
| question_answer | character varying(255) |

## ar_customer_cashier_list

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(50) |
| sale_code | character varying(255) |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## ar_customer_connected

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(255) |
| ar_webservice_name | character varying(255) |
| ar_provider_code | character varying(100) |
| ar_database_name | character varying(100) |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ar_customer_detail

แถวโดยประมาณ: 27,791

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| area_code | character varying(25) |
| sale_code | character varying(25) |
| logistic_area | character varying(25) |
| pay_bill_code | character varying(25) |
| keep_chq_code | character varying(25) |
| pay_bill_date | smallint |
| keep_chq_date | smallint |
| sale_price_level | smallint |
| credit_sale | smallint |
| credit_code | character varying(25) |
| form_name | character varying(255) |
| pay_bill_condition | character varying(25) |
| keep_money_condition | character varying(25) |
| payment_person | character varying(25) |
| credit_person | character varying(25) |
| keep_money_person | character varying(25) |
| discount_item | character varying(50) |
| discount_bill | character varying(50) |
| credit_group | smallint |
| credit_group_code | character varying(25) |
| credit_money | numeric |
| credit_money_max | numeric |
| credit_day | integer |
| credit_reason | character varying(25) |
| credit_status | smallint |
| credit_date | date |
| credit_status_reason | character varying(25) |
| trade_license | character varying(50) |
| vat_license | character varying(50) |
| tax_id | character varying(50) |
| tax_type | smallint |
| tax_rate | numeric |
| account_code | character varying(25) |
| shipping_type | smallint |
| close_reason | character varying(255) |
| close_date | date |
| group_main | character varying(25) |
| group_sub_1 | character varying(25) |
| group_sub_2 | character varying(25) |
| group_sub_3 | character varying(25) |
| group_sub_4 | character varying(25) |
| picture_3 | character varying(255) |
| picture_4 | character varying(255) |
| ref_doc_1 | character varying(255) |
| ref_doc_2 | character varying(255) |
| ref_doc_3 | character varying(255) |
| dimension_1 | character varying(100) |
| dimension_2 | character varying(100) |
| dimension_3 | character varying(100) |
| dimension_4 | character varying(100) |
| dimension_5 | character varying(100) |
| currency_code | character varying(20) |
| latitude | numeric |
| longitude | numeric |
| card_id | character varying(100) |
| passbook_code | character varying(25) |
| set_tax_type | smallint |
| branch_type | smallint |
| branch_code | character varying(25) |
| area_paybill | character varying(25) |
| reason_disable_credit | character varying(500) |
| close_credit_date | date |
| close_reason_1 | smallint |
| close_reason_2 | smallint |
| close_reason_3 | smallint |
| close_reason_4 | smallint |
| dimension_6 | character varying(255) |
| dimension_7 | character varying(255) |
| dimension_8 | character varying(255) |
| dimension_9 | character varying(255) |
| dimension_10 | character varying(255) |
| disable_auto_close_credit | smallint |
| ap_code_ref | character varying(25) |
| sale_type | smallint |
| line_id | character(1) |
| facebook | character(1) |
| customer_type_code | character varying(25) |
| ar_channel_code | character varying(25) |
| ar_location_type_code | character varying(25) |
| br_cust_code | character varying(25) |
| ar_sub_type_1_code | character varying(25) |
| ar_vehicle_code | character varying(25) |
| ar_equipment_code | character varying(25) |
| ar_sub_equipment | character varying(25) |
| ar_project_code | character varying(25) |
| ar_shoptype1_code | character varying(25) |
| ar_shoptype2_code | character varying(25) |
| ar_shoptype3_code | character varying(25) |
| ar_shoptype4_code | character varying(25) |
| ar_shoptype5_code | character varying(25) |
| sub_ar_shoptype5_code | character varying(25) |
| ar_project_code_name | smallint |
| ar_shoptype6_code | character varying(25) |
| ar_shoptype7_code | character varying(25) |
| ar_project_date_end | date |
| create_date_time_now | timestamp without time zone |
| nfc_asset | character varying(255) |
| past_due_day | integer |
| mobile_sales | smallint |
| close_over_credit_warning | smallint |

## ar_dealer

แถวโดยประมาณ: 27,788

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| regist_date | date |
| expire_date | date |
| asso_code | character varying(25) |
| asso_regist_date | date |
| asso_expire_date | date |
| ar_code | character varying(25) |
| branch_code | character varying(25) |
| sex | smallint |
| nationality | character varying(25) |
| mstatus | smallint |
| blood_group | character varying(5) |
| address | character varying(25) |
| moo | character varying(25) |
| building | character varying(50) |
| floor | character varying(25) |
| room_no | character varying(25) |
| soi | character varying(50) |
| road | character varying(50) |
| home_phone_extend | character varying(25) |
| off_phone | character varying(25) |
| off_phone_extend | character varying(25) |
| mobile_phone | character varying(25) |
| guid_code | character varying(40) |
| is_staff | smallint |
| create_date_time_now | timestamp without time zone |

## ar_dimension

แถวโดยประมาณ: 6

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

## ar_equipment

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_group

แถวโดยประมาณ: 11

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

## ar_group_sub

แถวโดยประมาณ: 9

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| sub_no | smallint |
| status | smallint |
| main_group | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_item_by_customer

แถวโดยประมาณ: 241

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ar_keep_chq_condition

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

## ar_keep_money_condition

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

## ar_location_type

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_logistic_area

แถวโดยประมาณ: 38,248

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

## ar_open_reason

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

## ar_pay_bill_condition

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

## ar_paybill_area

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## ar_project

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_sale_area

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

## ar_sale_group

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

## ar_shoptype1

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype2

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype3

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype4

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype5

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype6

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_shoptype7

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_sub_equipment

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_sub_type_1

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_tier

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

## ar_type

แถวโดยประมาณ: 3

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

## ar_vehicle

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ar_work_title

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| staus | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |
