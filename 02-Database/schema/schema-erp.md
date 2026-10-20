---
tags: [sml, schema, erp, generated]
---
# ตารางกลุ่ม `erp` (kbyt)

กลับไป [[schema-index]]

## erp_account_period

แถวโดยประมาณ: 36

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| period_number | integer |
| date_start | date |
| date_end | date |
| status | integer |
| period_year | smallint |
| create_date_time_now | timestamp without time zone |

## erp_allocate_list

แถวโดยประมาณ: 3

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

## erp_amper

แถวโดยประมาณ: 999

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| province | character varying(25) |
| status | smallint |
| guid_code | character varying(35) |
| lat | numeric |
| lng | numeric |
| create_date_time_now | timestamp without time zone |

## erp_bank

แถวโดยประมาณ: 24

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
| chq_income_account_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## erp_bank_branch

แถวโดยประมาณ: 5,904

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| bank_code | character varying(25) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_book_bank_trans_type

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

## erp_branch_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| number | integer |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| address_1 | character varying(255) |
| address_2 | character varying(255) |
| telephone | character varying(100) |
| fax | character varying(100) |
| remark | character varying(255) |
| guid_code | character varying(35) |
| serial_list | character varying(255) |
| phone_number_approve | character varying(255) |
| sale_hub_approve | character varying(500) |
| arm_code | character varying(50) |
| arm_send_cancel_doc | smallint |
| arm_send_cancel_doc_to | character varying(1000) |
| arm_send_cn | smallint |
| arm_send_cn_to | character varying(1000) |
| arm_send_ar_change | smallint |
| arm_send_ar_change_to | character varying(1000) |
| branch_type | smallint |
| create_date_time_now | timestamp without time zone |

## erp_cancel_logs

แถวโดยประมาณ: 110

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| user_code | character varying(25) |
| cancel_flag | smallint |
| cancel_datetime | timestamp without time zone |
| cancel_reason | character varying(500) |
| create_date_time_now | timestamp without time zone |

## erp_cn_reason

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| cn_type | smallint |
| name_1 | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_company_profile

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| company_name_1 | character varying(100) |
| company_name_2 | character varying(100) |
| business_name_1 | character varying(100) |
| business_name_2 | character varying(100) |
| address_1 | character varying(255) |
| address_2 | character varying(255) |
| house | character varying(255) |
| room_no | character varying(255) |
| floor_no | character varying(255) |
| village | character varying(255) |
| house_no | character varying(255) |
| crowd_no | character varying(255) |
| lane | character varying(255) |
| road | character varying(255) |
| locality | character varying(255) |
| amphur | character varying(255) |
| province | character varying(255) |
| postcode | character varying(255) |
| telephone_number | character varying(100) |
| fax_number | character varying(100) |
| tax_number | character varying(100) |
| branch_status | smallint |
| workplace_1 | character varying(200) |
| workplace_2 | character varying(200) |
| last_backup | timestamp without time zone |
| branch_type | smallint |
| branch_code | character varying(25) |
| agent_code | character varying(50) |
| sap_code | character varying(50) |
| region | character varying(255) |
| club | character varying(255) |
| arm_code | character varying(50) |
| profit_ctr | character varying(255) |
| cost_ctr | character varying(255) |
| entity | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_credit

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| start_date | date |
| stop_date | date |
| remark | character varying(255) |
| formular | character varying(100) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_credit_approve_level

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| from_amount | numeric |
| to_amount | numeric |
| user_approve | character varying(255) |
| phone_number_approve | character varying(255) |
| sale_hub_auth | character varying(500) |
| guid_code | character varying(100) |
| branch_code | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_credit_approved_logs

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
| ref_no | character varying(50) |
| creator_code | character varying(50) |
| approve_user | character varying(50) |
| create_datetime | timestamp without time zone |
| approve_status | smallint |
| create_date_time_now | timestamp without time zone |

## erp_credit_request

แถวโดยประมาณ: 55,653

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| credit_money | numeric |
| credit_money_max | numeric |
| chq_amount | numeric |
| advance_amount | numeric |
| ar_balance_amount | numeric |
| sr_amount | numeric |
| ss_amount | numeric |
| bill_amount | numeric |
| over_amount | numeric |
| over_percent | numeric |
| credit_status | smallint |
| user_approve_status | character varying(50) |
| user_approve_status_date | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## erp_credit_type

แถวโดยประมาณ: 5

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| charge_rate | character varying(100) |
| guid_code | character varying(35) |
| account_code | character varying(25) |
| use_charge_rate | smallint |
| create_date_time_now | timestamp without time zone |

## erp_currency

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
| symbol | character varying(25) |
| exchange_rate_present | numeric |
| create_date_time_now | timestamp without time zone |

## erp_data_center

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| datacenter_server | character varying(150) |
| datacenter_provider_name | character varying(100) |
| datacenter_database_name | character varying(150) |
| datacenter_database_type | smallint |
| shop_code | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_delivery_order

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| order_no | character varying(55) |
| order_date | date |
| doc_no | character varying(255) |
| doc_date | date |
| created_at | timestamp without time zone |
| created_by | character varying(255) |
| cust_code | character varying(50) |
| cust_name | character varying(255) |
| cust_contact | character varying(100) |
| cust_address | character varying(255) |
| cust_province_id | character varying(10) |
| cust_amphur_id | character varying(10) |
| cust_tumbon_id | character varying(10) |
| cust_zip_code | character varying(5) |
| cust_telephone | character varying(50) |
| is_cod | smallint |
| cod_amount | numeric |
| remark | character varying(255) |
| receive_date | date |
| receive_time | character varying(20) |
| delivery_date | date |
| delivery_time | character varying(20) |
| cust_latitude | numeric |
| cust_longitude | numeric |
| cod_payment_type | character varying(100) |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |
| is_cancel | smallint |
| canceled_at | timestamp without time zone |
| canceled_by | character varying(255) |
| cancel_reason | character varying(255) |

## erp_delivery_order_item

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| order_no | character varying(25) |
| doc_no | character varying(255) |
| line_number | smallint |
| item_code | character varying(50) |
| item_name | character varying(255) |
| qty | numeric |
| unit_code | character varying(50) |
| width | numeric |
| length | numeric |
| height | numeric |
| weight | numeric |
| create_date_time_now | timestamp without time zone |
| warehouse_code | character varying(50) |

## erp_delivery_order_transaction_logs

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| order_no | character varying(50) |
| order_date | date |
| job_id | character varying(255) |
| mobillyst_order_no | character varying(255) |
| mobillyst_referance_id | character varying(255) |
| create_date_time_now | timestamp without time zone |
| created_at | timestamp without time zone |
| data | json |

## erp_department_list

แถวโดยประมาณ: 6

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| ref_side_code | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_doc_approve

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

## erp_doc_format

แถวโดยประมาณ: 1,007

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| guid_code | character varying(35) |
| format | character varying(100) |
| screen_code | character varying(10) |
| form_code | character varying(1000) |
| gl_book | character varying(10) |
| gl_description | character varying(255) |
| form_code_1 | character varying(1000) |
| form_code_2 | character varying(100) |
| form_code_3 | character varying(100) |
| form_code_4 | character varying(100) |
| form_code_5 | character varying(100) |
| tax_format | character varying(100) |
| doc_running | character varying(100) |
| use_branch_select | smallint |
| branch_list | character varying(255) |
| scan_folder | character varying(255) |
| scan_computer_id | character varying(100) |
| vat_type | smallint |
| create_date_time_now | timestamp without time zone |

## erp_doc_format_etax

แถวโดยประมาณ: 90

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_format_code | character varying(25) |
| etax_document_type | smallint |
| etax_document_type_code | character varying(55) |
| etax_document_name | character varying(255) |
| create_date_time_now | timestamp without time zone |
| send_etax | smallint |
| etax_form_code | character varying(255) |

## erp_doc_format_gl

แถวโดยประมาณ: 10,456

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| condition_number | integer |
| condition_name | character varying(255) |
| account_code_debit | character varying(25) |
| account_name | character varying(255) |
| account_code_credit | character varying(25) |
| doc_code | character varying(10) |
| line_number | integer |
| account_name2 | character varying(255) |
| code_compare | character varying(100) |
| condition_case | character varying(50) |
| create_date_time_now | timestamp without time zone |

## erp_doc_group

แถวโดยประมาณ: 14

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

## erp_exchange_rate

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| country | character varying(100) |
| sign | character varying(10) |
| import | numeric |
| export | numeric |
| bank | character varying(10) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_expenses_list

แถวโดยประมาณ: 443

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| gl_account_code | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_images

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| image_id | character varying(50) |
| image_file | bytea |
| system_id | character varying(10) |
| guid_code | character varying(100) |
| create_date_time_now | timestamp without time zone |

## erp_income_list

แถวโดยประมาณ: 279

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| gl_account_code | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_insure_type

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
| status | smallint |
| create_date_time_now | timestamp without time zone |

## erp_job_list

แถวโดยประมาณ: 16

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

## erp_job_type

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

## erp_option

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| year_type | integer |
| vat_type | integer |
| vat_rate | numeric |
| gl_no_decimal | integer |
| use_log_book | integer |
| use_print_slip | integer |
| use_doc_group | integer |
| use_department | integer |
| use_job | integer |
| use_allocate | integer |
| use_unit | integer |
| use_work_in_process | integer |
| use_project | integer |
| item_qty_decimal | integer |
| item_price_decimal | integer |
| item_amount_decimal | integer |
| wht_rate | numeric |
| vat_type_1 | integer |
| warning_price_1 | integer |
| warning_price_2 | integer |
| warning_price_3 | integer |
| purchase_credit_note_type | smallint |
| printer_top_margin | numeric |
| gl_trans_type | integer |
| column_price_enable | smallint |
| stock_balance_control | smallint |
| manual_total | smallint |
| use_barcode | smallint |
| sync_webservice_url | character varying(100) |
| sync_product | smallint |
| stock_accrued_control | smallint |
| sale_auto_packing | smallint |
| warning_low_cost | smallint |
| pr_approve_lock | smallint |
| ar_bill_inform | smallint |
| count_stock_sum | smallint |
| cost_warehouse | smallint |
| doc_sale_order_edit | smallint |
| use_expire | smallint |
| balance_control_type | smallint |
| ic_stock_control | smallint |
| auto_insert_time | smallint |
| perm_wh_shelf | smallint |
| mis_center_pw | character varying(100) |
| count_stock_display_saleprice | smallint |
| item_hidden_cost_1 | smallint |
| item_hidden_income_1 | smallint |
| warning_credit_money | smallint |
| lock_credit_money | smallint |
| password_ar_credit | smallint |
| get_last_price_type | smallint |
| active_sync_active | smallint |
| active_sync_server | character varying(150) |
| active_sync_access_code | character varying(100) |
| active_sync_branch_code | character varying(100) |
| active_sync_database_name | character varying(100) |
| active_sync_provider_name | character varying(100) |
| transfer_stock_control | smallint |
| shop_time_open | character varying(10) |
| shop_time_close | character varying(10) |
| barcode_picture | smallint |
| discout_type | smallint |
| use_point_center | smallint |
| auto_run_docno_sale | smallint |
| doc_sale_tax_number_fixed | smallint |
| promotion_fixed_unitcode | smallint |
| issue_stock_control | smallint |
| ic_price_formula_control | smallint |
| disable_ic_cost_process | smallint |
| deposit_format_from_pos | smallint |
| sale_real_price | smallint |
| use_serial_no_duplicate | smallint |
| use_sale_shift | smallint |
| sale_shift_id | character varying(50) |
| next_process_time | smallint |
| save_logs | smallint |
| use_reference_pr | smallint |
| default_sale_type | smallint |
| get_purchase_price | smallint |
| use_order_checker | smallint |
| process_serial_device | character varying(255) |
| ignore_all_case | smallint |
| ap_bill_inform | smallint |
| fix_item_set_price | smallint |
| lock_low_cost | smallint |
| add_item_color | smallint |
| sync_database_name | character varying(255) |
| sync_provider_code | character varying(50) |
| manual_customer_code | smallint |
| show_branch_doc_only | smallint |
| voucher_form_code | character varying(255) |
| count_customer_table | smallint |
| find_lot_auto | smallint |
| print_packing_pos_order | smallint |
| disable_edit_doc_no_doc_date | smallint |
| filter_pay_bill | smallint |
| disable_edit_order | smallint |
| print_pos_settle_bill_detail | character(1) |
| disable_auto_stock_process | smallint |
| auto_open_table | smallint |
| check_input_vat | smallint |
| sale_order_banalce_control | smallint |
| disable_item_cost | smallint |
| sum_point_all | smallint |
| order_on_internet | smallint |
| order_after_open_table | smallint |
| join_money_credit | smallint |
| join_money_credit_list | character varying(1000) |
| check_lot_auto | smallint |
| warning_discount_1 | smallint |
| stock_reserved_control | smallint |
| report_font | character varying(255) |
| report_font_header_1 | character varying(255) |
| report_font_header_2 | character varying(255) |
| stock_reserved_control_location | smallint |
| round_type | smallint |
| digital_barcode_scale | smallint |
| calc_point_from_pay | smallint |
| orders_speech | smallint |
| orders_speech_format | character varying(500) |
| lock_change_customer | smallint |
| real_doc_date_doc_time | smallint |
| save_user_order | smallint |
| inventory_gl_post | smallint |
| multi_currency | smallint |
| warning_reorder_point | smallint |
| home_currency | character varying(25) |
| warning_product_expire | smallint |
| warning_bill_overdue | smallint |
| cn_actual_cost | smallint |
| disable_sync_time | smallint |
| gl_process_realtime | smallint |
| search_cheque_other_cust_code | smallint |
| check_ar_status_credit | smallint |
| print_invoice_one_time | smallint |
| check_ar_duplicate_name | smallint |
| tax_from_invoice | smallint |
| running_doc_no_only | smallint |
| warning_branch_input | smallint |
| lock_date_back | smallint |
| lock_direct_journal | smallint |
| request_ar_credit | smallint |
| request_credit_type | smallint |
| ar_credit_chq_outstanding | smallint |
| finishgoods_cost_auto | smallint |
| phone_number_approve | character varying(255) |
| sale_hub_approve | character varying(500) |
| customer_by_branch | smallint |
| show_menu_by_permission | smallint |
| calc_item_price_discount | smallint |
| issue_return_real_cost | smallint |
| warning_department | smallint |
| hidden_price_formula | smallint |
| quotation_expire | smallint |
| ref_po_approve | smallint |
| sr_ss_credit_check | smallint |
| use_price_center | smallint |
| price_list_server | character varying(255) |
| price_list_serial_process | character varying(100) |
| price_list_branch | character varying(100) |
| price_list_key | character varying(100) |
| mobile_sale_url | character varying(350) |
| mobile_bypasskey | character varying(350) |
| close_warning_backup | smallint |
| ss_ref_po_only | smallint |
| warning_input_customer | smallint |
| inv_disable_quotation | smallint |
| use_credit_pay_bill_calc | smallint |
| pr_disable_price | smallint |
| stock_accured_level | smallint |
| ar_pay_from_bill_note | smallint |
| ap_pay_from_bill_note | smallint |
| close_ar_status_auto | smallint |
| check_refer_wh_shelf | smallint |
| arm_send_cancel_doc | smallint |
| arm_send_cancel_doc_to | character varying(1000) |
| arm_send_cn | smallint |
| arm_send_cn_to | character varying(1000) |
| arm_send_ar_change | smallint |
| arm_send_ar_change_to | character varying(1000) |
| purchase_zero_vat_use_price1 | smallint |
| pr_wh_shelf | smallint |
| cn_request_doc_ref | smallint |
| send_area_check | smallint |
| use_sml_eorder | smallint |
| sml_eorder_api_key | character varying(255) |
| check_status_sr_print | smallint |
| exchange_rate_decimal | smallint |
| check_so_dr_balande | smallint |
| coupon_full_amount | smallint |
| cost_over_sale_rate | character varying(255) |
| check_branch_status_word | character varying(2000) |
| report_webservice_url | character varying(500) |
| cn_coupon_only | smallint |
| lock_pu_gr | smallint |
| pu_from_po_only | smallint |
| sync_master_url | character varying(255) |
| show_serial_tire | smallint |
| show_serial_car | smallint |
| warehouse_on_the_way | character varying(255) |
| shelf_on_the_way | character varying(255) |
| lock_sale_day_interval | smallint |
| sale_day_interval | smallint |
| lock_bill_auto | smallint |
| lock_bill_auto_interval | smallint |
| begin_date_import_inv | date |
| end_date_import_inv | date |
| check_edit_project | smallint |
| change_customer_not_clear_detail | smallint |
| print_every_case | smallint |
| print_table_move | smallint |
| receive_more_po | smallint |
| wallet_lugent_store_id | character varying(255) |
| wallet_lugent_terminal_id | character varying(255) |
| wallet_lugent_merchant_name | character varying(255) |
| wallet_lugent_access_code | character varying(255) |
| wallet_bcel_mcid | character varying(255) |
| wallet_bcel_mcc | character varying(255) |
| wallet_bcel_contact | character varying(255) |
| discount_step_round_off | smallint |
| select_branch_first | smallint |
| currency_exchange_decimal | integer |
| discount_vat_type | smallint |
| use_compare_unit | smallint |
| create_date_time_now | timestamp without time zone |
| wallet_lugent_biller_id | character varying(255) |
| change_price_formula | smallint |
| sap_inv_docformate | character varying(255) |
| input_credit_card_charge | smallint |
| enable_all_ic_wh_shelf | smallint |
| not_choose_project | smallint |
| check_expiration_date | smallint |
| check_delivery_date | smallint |
| gen_doc_no_auto | smallint |
| warning_overdue | smallint |
| check_overdue | smallint |
| check_overdue_order | smallint |
| check_overdue_sell | smallint |
| show_stock_balance_branch_login | smallint |
| sap_inv_docformate_cn | character varying(255) |
| sap_inv_docformate_pa | character varying(255) |
| import_inv_auto | smallint |
| allow_sale_over_reserve | smallint |
| credit_sale_include_deposit | smallint |
| edi_wh_code | character varying(25) |
| edi_shelf_code | character varying(25) |
| check_credit_sale_reserve_sale_order | smallint |
| stock_issue_show_cost | smallint |
| skip_cn_over_due | smallint |
| display_lot_column | smallint |
| rim_request_doc_ref | smallint |
| not_use_inv_auto | smallint |
| wallet_notification_server_url | character varying(500) |
| wallet_lugent_domain | character varying(500) |
| sale_auto_input_qty | smallint |
| fill_sale_deposit | smallint |
| sync_start_date | date |
| doc_ref_salesorder_approve | smallint |
| use_quality_control_system | smallint |
| doc_ref_reservation_approve | smallint |
| no_coppy | smallint |
| productlotbyyear | smallint |
| approve_order_so_befor_print | smallint |
| quotation_wh_shelf | smallint |
| show_stock_balance_wh | smallint |
| check_qty_over_doc_ref | smallint |
| lock_edit_product_name_in_detail | smallint |
| withdraw_enable_amount | smallint |
| purchase_request_approve_until_end | smallint |
| wallet_bcel_merchant_name | character varying(25) |
| wallet_book_code | character varying(25) |
| cn_pos_over_day | smallint |
| check_qty | smallint |
| hide_price_item_set | smallint |
| disable_capture_screen | smallint |
| dohome_dealer_code | character varying(255) |
| dohome_username | character varying(255) |
| dohome_password | character varying(255) |
| use_notification_debt_product_receipt | smallint |
| sml_kbank_qr_api_token | character varying(255) |
| sml_kbank_qr_api_uat_mode | smallint |
| enable_sml_kbank_api | smallint |
| sml_kbank_qr_credit | smallint |
| tiger_app_id | character varying(255) |
| tiger_x_api_key | character varying(255) |
| tiger_end_point | character varying(255) |
| show_item_remark | smallint |
| show_stock_available | smallint |
| pay_bill_over | smallint |
| ref_pr_approve | smallint |
| open_cash_drawer_after_sale | smallint |
| order_table_url | character varying(255) |
| hide_pr_amount | smallint |
| disable_ar_autorun | smallint |
| user_barcode_clearance | smallint |

## erp_option_etax_inet

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| authorization_code | character varying(255) |
| uat_mode | smallint |
| pdf_attach | smallint |
| send_email | smallint |
| api_key | character varying(255) |
| create_date_time_now | timestamp without time zone |
| uat_email_to | character varying(255) |

## erp_option_mobillyst

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| enable_service | smallint |
| api_key | character varying(255) |
| latitude | numeric |
| longitude | numeric |
| take_photo_receive | smallint |
| take_photo_receive_title | character varying(100) |
| take_photo_delivery | smallint |
| take_photo_delivery_title | character varying(100) |
| receive_contact_name | character varying(100) |
| receive_contact_remark | character varying(100) |
| receive_telephone | character varying(100) |
| cod_type_list | character varying(255) |
| is_poc | smallint |
| create_date_time_now | timestamp without time zone |

## erp_package_reason

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| guid_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## erp_pass_book

แถวโดยประมาณ: 6

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| bank_code | character varying(25) |
| bank_branch | character varying(100) |
| book_type | character varying(25) |
| book_number | character varying(25) |
| tax_number | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| account_code_1 | character varying(25) |
| account_code_2 | character varying(25) |
| chq_fee_rate | numeric |
| chq_fee_rate_amount | numeric |
| min_chq_fee_rate | numeric |
| min_chq_fee_amount | numeric |
| max_chq_fee_rate | numeric |
| max_chq_fee_amount | numeric |
| mobile_use | integer |
| currency_code | character varying(25) |
| create_date_time_now | timestamp without time zone |
| singhaonline_use | integer |

## erp_pass_book_type

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_print_logs

แถวโดยประมาณ: 1,780,161

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| trans_flag | smallint |
| user_code | character varying(50) |
| print_datetime | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## erp_print_station

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| printer_name | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_project_list

แถวโดยประมาณ: 56

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

## erp_province

แถวโดยประมาณ: 78

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
| lat | numeric |
| lng | numeric |
| create_date_time_now | timestamp without time zone |

## erp_qr_payment

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| guid_code | character varying(35) |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| pass_book_code | character varying(25) |
| qr_type | smallint |
| promptpay | character varying(25) |
| biller_id | character varying(99) |
| terminal_id | character varying(99) |
| store_id | character varying(99) |
| merchant_name | character varying(10) |
| credit_card_type | character varying(25) |
| qr_template | text |
| active | smallint |
| create_date_time_now | timestamp without time zone |

## erp_ref_document

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_name | character varying(100) |
| file_type | character varying(50) |
| file_name | character varying(100) |
| system_id | character varying(10) |
| code | character varying(25) |
| guid_code | character varying(35) |
| create_date_time_now | timestamp without time zone |

## erp_request_order

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_flag | smallint |
| trans_type | smallint |
| doc_no | character varying(50) |
| req_datetime | timestamp without time zone |
| approve_code | character varying(50) |
| send_success | smallint |
| cust_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## erp_sale_plan

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| begin_date | date |
| end_date | date |
| guid_code | character varying(50) |
| remark | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## erp_sale_plan_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| plan_code | character varying(25) |
| sale_area_code | character varying(25) |
| sale_code | character varying(25) |
| item_code | character varying(25) |
| sale_plan_amount | numeric |
| remark | character varying(1000) |
| create_date_time_now | timestamp without time zone |

## erp_send_message

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| send_type | smallint |
| send_to | character varying(1500) |
| send_message | text |
| send_date | timestamp without time zone |
| send_status | smallint |
| date_add | timestamp without time zone |
| send_to_date | timestamp without time zone |
| send_title | character varying(1000) |
| send_process_guid | character varying(100) |
| send_process_time | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## erp_side_list

แถวโดยประมาณ: 16

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

## erp_tambon

แถวโดยประมาณ: 8,873

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| amper | character varying(25) |
| province | character varying(25) |
| status | smallint |
| guid_code | character varying(35) |
| lat | numeric |
| lng | numeric |
| create_date_time_now | timestamp without time zone |
| zip_code | character varying(10) |

## erp_thai_qr_config

แถวโดยประมาณ: 1

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| promp_pay_telephone_number | character varying(10) |
| promp_pay_wallet_id | character varying(15) |
| merchant_name | character varying(25) |
| service_code | character varying(26) |
| company_biller_id | character varying(15) |
| company_terminal_id | character varying(26) |
| company_store_id | character varying(26) |
| config_type | smallint |
| pos_id | character varying(25) |
| create_date_time_now | timestamp without time zone |
| ref_1_format | character varying(500) |
| ref_2_format | character varying(500) |
| prompt_pay_book_code | character varying(25) |

## erp_user

แถวโดยประมาณ: 19

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
| mobile | character varying(50) |
| id_card | character varying(15) |
| side | character varying(10) |
| department | character varying(10) |
| title | character varying(255) |
| salary | numeric |
| save_code | character varying(25) |
| save_date | date |
| edit_code | character varying(25) |
| edit_date | date |
| cancel_code | character varying(25) |
| cancel_date | date |
| status | smallint |
| guid_code | character varying(35) |
| price_level_1 | smallint |
| price_level_2 | smallint |
| password | character varying(100) |
| pos_cashier | smallint |
| discount_level_1 | smallint |
| cancel_pos_bill_level | smallint |
| ic_wht | character varying(10) |
| ic_shelf | character varying(10) |
| discount_bill_pos | smallint |
| open_cash_drawer | smallint |
| show_total_balance | smallint |
| branch_code | character varying(25) |
| change_branch_code | smallint |
| lock_bill | smallint |
| parent_code | character varying(25) |
| approve_ar_credit | smallint |
| show_item_cost | smallint |
| disable_edit_doc_no_doc_date_user | smallint |
| delete_item_pos | smallint |
| area_code | character varying(25) |
| area_paybill | character varying(25) |
| reset_print_log | smallint |
| is_login_user | smallint |
| signature_1 | text |
| picture_1 | text |
| po_approve_from | numeric |
| po_approve_to | numeric |
| sr_approve_from | numeric |
| sr_approve_to | numeric |
| ss_approve_from | numeric |
| ss_approve_to | numeric |
| cr_approve_from | numeric |
| cr_approve_to | numeric |
| max_cr_approve | numeric |
| sr_approve_from_percent | numeric |
| sr_approve_to_percent | numeric |
| load_approve_percent | numeric |
| mobile_user | smallint |
| sale_hub_user | character varying(255) |
| create_date_time_now | timestamp without time zone |
| is_copy_doc | smallint |
| guid | uuid |

## erp_user_group

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
| is_po | smallint |
| is_so | smallint |
| is_wh | smallint |
| is_sale_group | smallint |
| is_pr_approve | smallint |
| is_po_approve | smallint |
| is_price_list_approve | smallint |
| is_so_approve | smallint |
| is_change_masterdata | smallint |
| create_date_time_now | timestamp without time zone |

## erp_user_group_approve

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| group_code | character varying(50) |
| user_code | character varying(50) |
| approve_flag | smallint |
| create_date_time_now | timestamp without time zone |

## erp_user_group_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| group_code | character varying(25) |
| user_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## erp_user_group_wh_shelf

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| group_code | character varying(25) |
| wh_code | character varying(25) |
| shelf_code | character varying(25) |
| screen_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## erp_view_column

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
| column_format | character varying(500) |
| column_resource | character varying(500) |
| column_field_search | character varying(500) |
| create_date_time_now | timestamp without time zone |

## erp_view_column_custom

แถวโดยประมาณ: 289

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
| column_format | character varying(500) |
| column_resource | character varying(500) |
| column_field_search | character varying(500) |
| column_no_search | smallint |
| create_date_time_now | timestamp without time zone |

## erp_view_document

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| screen_code | character varying(50) |
| code | character varying(10) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| create_date_time_now | timestamp without time zone |

## erp_view_table

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
| sort_mode | smallint |
| create_date_time_now | timestamp without time zone |

## erp_view_table_custom

แถวโดยประมาณ: 30

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
| guid_code | character varying(50) |
| sort_mode | smallint |
| create_date_time_now | timestamp without time zone |

## erp_wallet_list

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| name_1 | character varying(255) |
| guid_code | character varying(50) |
| name_2 | character varying(255) |
| account_code | character varying(25) |
| credit_period | smallint |
| create_date_time_now | timestamp without time zone |
