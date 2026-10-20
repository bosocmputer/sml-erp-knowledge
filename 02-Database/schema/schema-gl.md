---
tags: [sml, schema, gl, generated]
---
# ตารางกลุ่ม `gl` (kbyt)

กลับไป [[schema-index]]

## gl_account_close

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_time | character varying(20) |
| doc_no | character varying(50) |
| doc_format_code | character varying(20) |
| creator_code | character varying(50) |
| create_datetime | timestamp without time zone |
| last_editor_code | character varying(50) |
| lastedit_datetime | timestamp without time zone |
| account_year | smallint |
| account_month | smallint |
| account_period | smallint |
| guid_code | character varying(50) |
| product_balance_amount | numeric |
| product_next_amount | numeric |
| purchase_amount | numeric |
| sale_cost | numeric |
| sale_cost_account | character varying(50) |
| from_date | date |
| to_date | date |
| gl_entry_type | smallint |
| create_date_time_now | timestamp without time zone |

## gl_account_close_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_time | character varying(10) |
| doc_no | character varying(50) |
| doc_format_code | character varying(25) |
| ref_doc_type | smallint |
| account_code | character varying(50) |
| account_name | character varying(500) |
| balance_mode | smallint |
| account_type | smallint |
| amount | numeric |
| amount_2 | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## gl_account_cost

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

## gl_account_group

แถวโดยประมาณ: 38

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

## gl_account_type

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

## gl_cash_flow_group

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

## gl_chart_of_account

แถวโดยประมาณ: 675

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| account_level | smallint |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| main_code | character varying(25) |
| account_group | character varying(25) |
| cash_flow_group | character varying(25) |
| status | smallint |
| account_type | smallint |
| balance_mode | smallint |
| side_status | smallint |
| department_status | smallint |
| allocate_status | smallint |
| project_status | smallint |
| job_status | smallint |
| active_status | smallint |
| account_close | character varying(25) |
| work_in_process_status | smallint |
| balance_sheet_status | smallint |
| tax_type | smallint |
| guid_code | character varying(35) |
| interco | character varying(255) |
| remark | character varying(255) |
| create_date_time_now | timestamp without time zone |

## gl_chart_of_account_allocate_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| account_code | character varying(25) |
| allocate_code | character varying(10) |
| create_date_time_now | timestamp without time zone |

## gl_chart_of_account_depart_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| account_code | character varying(25) |
| department_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## gl_chart_of_account_job_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| account_code | character varying(25) |
| job_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## gl_chart_of_account_project_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| account_code | character varying(25) |
| project_code | character varying(10) |
| create_date_time_now | timestamp without time zone |

## gl_chart_of_account_side_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| account_code | character varying(25) |
| side_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## gl_design_report

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name1 | character varying(588) |
| name2 | character varying(588) |
| data | text |
| create_date_time_now | timestamp without time zone |

## gl_journal

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| ref_no | character varying(25) |
| ref_date | date |
| description | character varying(5000) |
| debit | numeric |
| credit | numeric |
| period_number | smallint |
| journal_type | smallint |
| guid_code | character varying(35) |
| ap_ar_code | character varying(20) |
| ap_ar_originate_from | character varying(255) |
| doc_code | character varying(25) |
| trans_flag | integer |
| is_pass | smallint |
| doc_format_code | character varying(25) |
| trans_direct | smallint |
| branch_code | character varying(25) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |
| create_code | character varying(25) |

## gl_journal_allocate_list

แถวโดยประมาณ: 1,043,858

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | smallint |
| line_number_detail | smallint |
| allocate_code | character varying(25) |
| allocate_name | character varying(100) |
| allocate_persent | numeric |
| allocate_amount | numeric |
| account_code | character varying(25) |
| period_number | smallint |
| journal_type | smallint |
| trans_flag | smallint |
| account_name | character varying(100) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_book

แถวโดยประมาณ: 5

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| word_begin | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## gl_journal_depart_list

แถวโดยประมาณ: 97,727

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | integer |
| line_number_detail | integer |
| department_code | character varying(25) |
| department_name | character varying(100) |
| allocate_persent | numeric |
| allocate_amount | numeric |
| account_code | character varying(25) |
| period_number | smallint |
| journal_type | smallint |
| trans_flag | smallint |
| account_name | character varying(100) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | smallint |
| account_code | character varying(25) |
| account_name | character varying(100) |
| description | character varying(5000) |
| credit | numeric |
| debit | numeric |
| period_number | smallint |
| debit_or_credit | smallint |
| journal_type | smallint |
| trans_flag | integer |
| is_pass | smallint |
| branch_code | character varying(25) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_job_list

แถวโดยประมาณ: 911,254

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | smallint |
| line_number_detail | smallint |
| job_code | character varying(25) |
| job_name | character varying(100) |
| allocate_persent | numeric |
| allocate_amount | numeric |
| account_code | character varying(25) |
| period_number | smallint |
| journal_type | smallint |
| trans_flag | smallint |
| account_name | character varying(100) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_project_list

แถวโดยประมาณ: 1,634

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | smallint |
| line_number_detail | smallint |
| project_code | character varying(25) |
| project_name | character varying(100) |
| allocate_persent | numeric |
| allocate_amount | numeric |
| account_code | character varying(25) |
| period_number | smallint |
| journal_type | smallint |
| trans_flag | smallint |
| account_name | character varying(100) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_side_list

แถวโดยประมาณ: 755,085

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| book_code | character varying(25) |
| doc_no | character varying(25) |
| line_number | smallint |
| line_number_detail | smallint |
| side_code | character varying(25) |
| side_name | character varying(100) |
| allocate_persent | numeric |
| allocate_amount | numeric |
| account_code | character varying(25) |
| period_number | smallint |
| journal_type | smallint |
| trans_flag | smallint |
| account_name | character varying(100) |
| account_year | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_summary

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| guid_code | character varying(55) |
| account_year | smallint |
| account_month | smallint |
| account_period | smallint |
| from_date | date |
| to_date | date |
| total_debit | numeric |
| total_credit | numeric |
| creator_code | character varying(255) |
| create_datetime | timestamp without time zone |
| last_editor_code | character varying(255) |
| lastedit_datetime | timestamp without time zone |
| doc_format_code | character varying(50) |
| doc_type | smallint |
| create_date_time_now | timestamp without time zone |
| book_code | character varying(25) |
| process_from_date | date |
| process_to_date | date |
| close_account_type_1 | smallint |
| close_account_type_2 | smallint |
| close_account_type_3 | smallint |
| close_account_type_4 | smallint |
| close_account_type_5 | smallint |
| close_from_account_1 | character varying(255) |
| close_from_account_2 | character varying(255) |
| close_from_account_3 | character varying(255) |
| close_from_account_4 | character varying(255) |
| close_from_account_5 | character varying(255) |
| close_to_account_1 | character varying(255) |
| close_to_account_2 | character varying(255) |
| close_to_account_3 | character varying(255) |
| close_to_account_4 | character varying(255) |
| close_to_account_5 | character varying(255) |
| branch_code | character varying(25) |
| remark | character varying(255) |
| close_all_balance | smallint |
| have_product_balance_first | smallint |

## gl_journal_summary_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| line_number | smallint |
| account_code | character varying(255) |
| account_name | character varying(255) |
| balance_debit | numeric |
| balance_credit | numeric |
| debit_amount | numeric |
| credit_amount | numeric |
| adjust_debit | numeric |
| adjust_credit | numeric |
| total_debit | numeric |
| total_credit | numeric |
| balance_mode | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_vat_buy

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| book_code | character varying(25) |
| line_number | smallint |
| vat_date | date |
| vat_new_number | character varying(25) |
| vat_doc_no | character varying(25) |
| vat_group | character varying(25) |
| vat_description | character varying(255) |
| vat_base_amount | numeric |
| vat_rate | numeric |
| vat_total_amount | numeric |
| vat_type | smallint |
| vat_amount | numeric |
| vat_except_amount_1 | numeric |
| vat_claim_amount | numeric |
| vat_average | integer |
| vat_effective_period | smallint |
| vat_claim_rate | numeric |
| is_add | smallint |
| trans_type | smallint |
| trans_flag | smallint |
| ap_code | character varying(25) |
| ap_name | character varying(255) |
| vat_calc | smallint |
| vat_effective_year | smallint |
| ref_vat_no | character varying(25) |
| ref_vat_date | date |
| ref_doc_no | character varying(25) |
| ref_doc_date | date |
| tax_no | character varying(25) |
| branch_type | smallint |
| branch_code | character varying(25) |
| manual_add | smallint |
| create_date_time_now | timestamp without time zone |

## gl_journal_vat_sale

แถวโดยประมาณ: 3

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| book_code | character varying(25) |
| line_number | smallint |
| vat_number | character varying(25) |
| tax_group | character varying(25) |
| description | character varying(255) |
| base_caltax_amount | numeric |
| tax_rate | numeric |
| amount | numeric |
| except_tax_amount | numeric |
| period_number | smallint |
| is_add | smallint |
| vat_date | date |
| trans_type | smallint |
| trans_flag | smallint |
| vat_effective_period | smallint |
| ar_code | character varying(25) |
| ar_name | character varying(255) |
| vat_calc | smallint |
| vat_effective_year | smallint |
| branch_type | smallint |
| branch_code | character varying(25) |
| tax_no | character varying(25) |
| manual_add | smallint |
| is_doc_copy | smallint |
| create_date_time_now | timestamp without time zone |
| vat_type | smallint |
| ref_vat_no | character varying(25) |
| ref_vat_date | date |
| ref_doc_no | character varying(25) |
| ref_doc_date | date |

## gl_list_view

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## gl_recurring

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| gl_desc | character varying(255) |
| xmlstring | character varying(5000) |
| create_date_time_now | timestamp without time zone |

## gl_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## gl_sap_account_code

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(255) |
| sap_code | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## gl_summary_close_account_detaiil

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(255) |
| account_code | character varying(255) |
| amount | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |
| balance_frist_amount | numeric |

## gl_tax_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| tax_rate | numeric |
| remark | character varying(255) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## gl_tax_type

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

## gl_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| doc_format_code | character varying(25) |
| from_date | date |
| to_date | date |
| account_period | smallint |
| account_year | smallint |
| branch_code | character varying(25) |
| remark | character varying(500) |
| book_code | character varying(25) |
| close_to_account | character varying(25) |
| doc_time | character varying(10) |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## gl_trans_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| trans_flag | smallint |
| account_code | character varying(25) |
| account_name | character varying(255) |
| debit | numeric |
| credit | numeric |
| line_number | smallint |
| create_date_time_now | timestamp without time zone |

## gl_wht_list

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| amount | numeric |
| tax_value | numeric |
| status | smallint |
| trans_flag | smallint |
| due_date | date |
| line_number | integer |
| cust_code | character varying(35) |
| card_number | character varying(50) |
| tax_number | character varying(50) |
| cust_tax_type | smallint |
| cust_name | character varying(255) |
| tax_doc_no | character varying(25) |
| cust_address | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## gl_wht_list_detail

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_date | date |
| doc_no | character varying(25) |
| income_type | character varying(100) |
| tax_rate | numeric |
| amount | numeric |
| tax_value | numeric |
| status | smallint |
| trans_flag | smallint |
| due_date | date |
| line_number | integer |
| cust_code | character varying(35) |
| sum_amount | numeric |
| tax_doc_no | character varying(25) |
| create_date_time_now | timestamp without time zone |
