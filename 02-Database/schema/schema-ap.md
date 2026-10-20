---
tags: [sml, schema, ap, generated]
---
# ตารางกลุ่ม `ap` (kbyt)

กลับไป [[schema-index]]

## ap_ar_debt_balance

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| doc_group | character varying(25) |
| debt_type | smallint |
| ar_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| sale_code | character varying(25) |
| area_code | character varying(25) |
| credit_code | character varying(25) |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| sum_debt_value | numeric |
| book_code | character varying(25) |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| job_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| doc_group | character varying(25) |
| billing_flag | smallint |
| ap_ar_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| person_code | character varying(25) |
| total_debt_value | numeric |
| total_discount | numeric |
| total_after_discount | numeric |
| total_money | numeric |
| total_debt_balance | numeric |
| bill_no | character varying(25) |
| bill_date | date |
| tax_value | numeric |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing_cut

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| doc_group | character varying(25) |
| billing_type | smallint |
| ap_ar_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| person_code | character varying(25) |
| total_debt_value | numeric |
| total_discount | numeric |
| total_after_discount | numeric |
| total_money | numeric |
| total_debt_balance | numeric |
| bill_no | character varying(25) |
| bill_date | date |
| tax_value | numeric |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing_cut_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| billing_no | character varying(25) |
| billing_date | date |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| debt_value | numeric |
| debt_cut_value | numeric |
| sum_debt_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| billing_no | character varying(25) |
| billing_date | date |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| sum_value | numeric |
| sum_money | numeric |
| sum_debt_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing_temp

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(25) |
| doc_group | character varying(25) |
| billing_flag | smallint |
| ap_ar_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| person_code | character varying(25) |
| total_debt_value | numeric |
| total_discount | numeric |
| total_after_discount | numeric |
| total_money | numeric |
| total_debt_balance | numeric |
| bill_no | character varying(25) |
| bill_date | date |
| tax_value | numeric |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_ar_debt_billing_temp_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| billing_no | character varying(25) |
| billing_date | date |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| sum_value | numeric |
| sum_money | numeric |
| sum_debt_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_ar_deposit_money

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| doc_ref | character varying(255) |
| doc_group | character varying(25) |
| deposit_type | smallint |
| ap_ar_code | character varying(25) |
| bill_no | character varying(25) |
| bill_date | date |
| vat_type | smallint |
| credit_day | integer |
| due_date | date |
| sale_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| vat_rate | numeric |
| total_value | numeric |
| total_vat_value | numeric |
| total_after_vat | numeric |
| total_net_value | numeric |
| amount | numeric |
| money_balance | numeric |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_ar_pay_bill

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
| ap_ar_code | character varying(25) |
| credit_day | integer |
| due_date | date |
| sale_code | character varying(25) |
| department_code | character varying(25) |
| total_value | numeric |
| debt_decrease | numeric |
| debt_increase | numeric |
| total_net_value | numeric |
| total_debt_balance | numeric |
| remark | character varying(255) |
| transection_flag | smallint |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_ar_pay_bill_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| bill_type | smallint |
| bill_no | character varying(25) |
| bill_date | date |
| bill_ref | character varying(25) |
| due_date | date |
| debt_value | numeric |
| pay_bill_value | numeric |
| value_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_ar_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## ap_ar_trans

แถวโดยประมาณ: 7

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
| cust_code | character varying(25) |
| project_code | character varying(25) |
| allocate_code | character varying(25) |
| job_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| sale_area_code | character varying(25) |
| sale_code | character varying(25) |
| credit_code | character varying(25) |
| credit_day | integer |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| discount_word | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| po_debt_balance | integer |
| po_cn_balance | integer |
| po_purchase | integer |
| po_addition_debt | integer |
| so_billing | integer |
| so_addition_debt | integer |
| so_debt_balance | integer |
| so_cn_balance | integer |
| currency_money | numeric |
| vat_type | smallint |
| vat_rate | numeric |
| total_value | numeric |
| total_vat_value | numeric |
| total_after_vat | numeric |
| total_net_value | numeric |
| amount | numeric |
| money_balance | numeric |
| book_no | character varying(100) |
| payment_method | character varying(100) |
| pay_installments | character varying(100) |
| delivery_date | date |
| sum_pay_money_cash | numeric |
| sum_pay_money_chq | numeric |
| sum_pay_money_credit | numeric |
| sum_pay_money_transfer | numeric |
| total_before_vat | numeric |
| total_discount | numeric |
| total_pay_money | numeric |
| total_debt_balance | numeric |
| total_after_discount | numeric |
| last_status | smallint |
| used_status | smallint |
| doc_success | smallint |
| total_pay_tax | numeric |
| total_debt_value | numeric |
| sum_pay_money_diff | numeric |
| doc_time | character varying(5) |
| doc_format_code | character varying(25) |
| sale_shift_id | character varying(50) |
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| branch_code | character varying(25) |
| is_manual_vat | smallint |
| is_cancel | smallint |
| cancel_code | character varying(25) |
| cancel_datetime | timestamp without time zone |
| total_net_value_2 | numeric |
| lost_profit_exchange_amount | numeric |
| create_date_time_now | timestamp without time zone |
| ref_doc_type | character varying(50) |

## ap_ar_trans_detail

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
| doc_ref | character varying(255) |
| billing_no | character varying(25) |
| billing_date | date |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| sum_debt_value | numeric |
| sum_tax_value | numeric |
| sum_debt_amount | numeric |
| sum_discount | numeric |
| sum_after_discount | numeric |
| sum_pay_money_cash | numeric |
| sum_pay_money_chq | numeric |
| sum_pay_money_credit | numeric |
| sum_pay_money_transfer | numeric |
| sum_debt_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | smallint |
| bill_type | smallint |
| sum_pay_money | numeric |
| sum_before_vat | numeric |
| sum_value | numeric |
| balance_ref | numeric |
| vat_rate | numeric |
| final_amount | numeric |
| last_status | smallint |
| calc_flag | smallint |
| ref_doc_no | character varying(255) |
| ref_doc_date | date |
| sale_shift_id | character varying(50) |
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| cust_code | character varying(25) |
| bill_tax_no | character varying(255) |
| bill_tax_date | date |
| sum_debt_amount_2 | numeric |
| balance_ref_2 | numeric |
| sum_pay_money_2 | numeric |
| lost_profit_exchange_amount | numeric |
| exchange_rate_old | numeric |
| create_date_time_now | timestamp without time zone |

## ap_ar_trans_detail_draft

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
| billing_no | character varying(25) |
| billing_date | date |
| due_date | date |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| sum_debt_value | numeric |
| sum_tax_value | numeric |
| sum_debt_amount | numeric |
| sum_discount | numeric |
| sum_after_discount | numeric |
| sum_pay_money_cash | numeric |
| sum_pay_money_chq | numeric |
| sum_pay_money_credit | numeric |
| sum_pay_money_transfer | numeric |
| sum_debt_balance | numeric |
| remark | character varying(255) |
| status | smallint |
| line_number | smallint |
| bill_type | smallint |
| sum_pay_money | numeric |
| sum_before_vat | numeric |
| sum_value | numeric |
| balance_ref | numeric |
| vat_rate | numeric |
| final_amount | numeric |
| last_status | smallint |
| calc_flag | smallint |
| ref_doc_no | character varying(255) |
| ref_doc_date | date |
| sale_shift_id | character varying(50) |
| creator_code | character varying(25) |
| last_editor_code | character varying(25) |
| create_datetime | timestamp without time zone |
| lastedit_datetime | timestamp without time zone |
| cust_code | character varying(25) |
| bill_tax_no | character varying(255) |
| bill_tax_date | date |
| create_date_time_now | timestamp without time zone |
| sum_debt_amount_2 | numeric |
| balance_ref_2 | numeric |
| sum_pay_money_2 | numeric |
| lost_profit_exchange_amount | numeric |
| exchange_rate_old | numeric |

## ap_ar_transport_label

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cust_code | character varying(50) |
| name_1 | character varying(255) |
| address | character varying(255) |
| telephone | character varying(255) |
| fax | character varying(255) |
| email | character varying(255) |
| guid_code | character varying(35) |
| ar_ap_type | smallint |
| home_address | character varying(255) |
| home_name | character varying(255) |
| moo | character varying(25) |
| soi | character varying(255) |
| road | character varying(255) |
| tambon | character varying(25) |
| amper | character varying(25) |
| province | character varying(25) |
| zip_code | character varying(10) |
| room_no | character varying(50) |
| floor | character varying(25) |
| building | character varying(50) |
| home_phone | character varying(50) |
| mobile1 | character varying(50) |
| mobile2 | character varying(50) |
| transport_type | character varying(25) |
| receive_day | character varying(255) |
| time_period | character varying(100) |
| remark_1 | character varying(255) |
| remark_2 | character varying(255) |
| country | character varying(255) |
| ship_code | character varying(50) |
| branch_type | smallint |
| branch_code | character varying(25) |
| tax_id | character varying(50) |
| logistic_area | character varying(50) |
| latitude | numeric |
| longitude | numeric |
| create_date_time_now | timestamp without time zone |
| ship_code_ref | character varying(255) |

## ap_contactor

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ap_code | character varying(25) |
| name | character varying(100) |
| address | character varying(255) |
| telephone | character varying(50) |
| mobile | character varying(50) |
| email | character varying(50) |
| work_title | character varying(100) |
| work_department | character varying(100) |
| officer_group | character varying(25) |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_dimension

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

## ap_group

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

## ap_group_sub

แถวโดยประมาณ: 0

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
| main_group | character varying(10) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## ap_item_by_supplier

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ap_code | character varying(25) |
| ic_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| line_number | integer |
| create_date_time_now | timestamp without time zone |

## ap_supplier

แถวโดยประมาณ: 848

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
| prefixname | character varying(15) |
| firstname | character varying(50) |
| lastname | character varying(70) |
| address | character varying(255) |
| address_eng | character varying(255) |
| tambon | character varying(25) |
| amper | character varying(25) |
| province | character varying(25) |
| zip_code | character varying(10) |
| telephone | character varying(150) |
| fax | character varying(50) |
| email | character varying(255) |
| website | character varying(255) |
| description | character varying(255) |
| ap_type | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| debt_balance | numeric |
| chq_balance | numeric |
| bill_balance | numeric |
| ap_status | smallint |
| doc_format_code | character varying(25) |
| country | character varying(255) |
| interco | character varying(255) |
| create_datetime | timestamp without time zone |
| last_update_date_time | timestamp without time zone |
| create_code | character varying(50) |
| last_update_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| use_partners | smallint |
| ap_web_service | character varying(255) |
| ap_database_name | character varying(255) |
| use_ar_code | character varying(255) |

## ap_supplier_connected

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(255) |
| ap_code | character varying(255) |
| ap_web_service | character varying(255) |
| ap_database_name | character varying(255) |
| use_ar_code | character varying(255) |
| create_date_time_now | timestamp without time zone |
| guid_code | character varying(35) |
| ap_provider | character varying(255) |
| start_date | date |

## ap_supplier_detail

แถวโดยประมาณ: 848

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ap_code | character varying(25) |
| staff_pay_code | character varying(25) |
| payment_way | character varying(255) |
| pay_bill_way | character varying(25) |
| pay_condition | character varying(255) |
| credit_purchase | smallint |
| credit_code | character varying(25) |
| form_name | character varying(255) |
| discount_item | character varying(50) |
| discount_bill | character varying(50) |
| credit_day | integer |
| trade_license | character varying(50) |
| tax_id | character varying(50) |
| tax_type | character varying(25) |
| tax_rate | numeric |
| account_code | character varying(25) |
| shipping_type | character varying(25) |
| close_reason | character varying(255) |
| close_date | date |
| group_main | character varying(25) |
| group_sub_1 | character varying(25) |
| group_sub_2 | character varying(25) |
| group_sub_3 | character varying(25) |
| group_sub_4 | character varying(25) |
| picture_1 | character varying(255) |
| picture_2 | character varying(255) |
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
| currency_code | character varying(25) |
| card_id | character varying(50) |
| passbook_code | character varying(25) |
| set_tax_type | smallint |
| branch_type | smallint |
| branch_code | character varying(25) |
| dimension_6 | character varying(255) |
| dimension_7 | character varying(255) |
| dimension_8 | character varying(255) |
| dimension_9 | character varying(255) |
| dimension_10 | character varying(255) |
| lead_time | smallint |
| create_date_time_now | timestamp without time zone |
| is_vendor_approved | smallint |

## ap_type

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
