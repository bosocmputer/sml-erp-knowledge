---
tags: [sml, schema, cb, generated]
---
# ตารางกลุ่ม `cb` (kbyt)

กลับไป [[schema-index]]

## cb_chq_list

แถวโดยประมาณ: 2

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| chq_get_date | date |
| chq_type | smallint |
| chq_number | character varying(100) |
| chq_due_date | date |
| chq_description | character varying(255) |
| doc_ref | character varying(25) |
| book_code | character varying(25) |
| pass_book_code | character varying(25) |
| bank_code | character varying(25) |
| bank_branch | character varying(100) |
| bank_description | character varying(255) |
| amount | numeric |
| currency_code | character varying(25) |
| owner_name | character varying(100) |
| person_code | character varying(25) |
| side_code | character varying(25) |
| department_code | character varying(25) |
| ap_ar_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| trans_type | smallint |
| trans_flag | smallint |
| no_approved | character varying(25) |
| credit_card_type | character varying(25) |
| charge | numeric |
| sum_amount | numeric |
| ap_ar_type | smallint |
| doc_line_number | smallint |
| external_chq | smallint |
| create_date_time_now | timestamp without time zone |

## cb_credit_card

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_type | smallint |
| credit_get_date | date |
| credit_card_type | character varying(25) |
| credit_card_no | character varying(25) |
| credit_card_code | character varying(25) |
| owner_name | character varying(100) |
| credit_money | numeric |
| credit_card_expire | date |
| credit_due_date | date |
| doc_ref | character varying(25) |
| book_code | character varying(25) |
| pass_book_code | character varying(25) |
| bank_code | character varying(25) |
| bank_branch | character varying(100) |
| bank_description | character varying(255) |
| amount | numeric |
| currency_code | character varying(25) |
| person_code | character varying(25) |
| ar_code | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| date_cut | date |
| no_approved | character varying(255) |
| sum_amount | numeric |
| charge | numeric |
| trans_flag | smallint |
| create_date_time_now | timestamp without time zone |

## cb_petty_cash

แถวโดยประมาณ: 14

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(100) |
| name_2 | character varying(100) |
| credit_money | numeric |
| balance_money | numeric |
| chart_of_account | character varying(25) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| currency_code | character varying(25) |
| create_date_time_now | timestamp without time zone |

## cb_resource

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| create_date_time_now | timestamp without time zone |

## cb_trans

แถวโดยประมาณ: 6

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
| book_code | character varying(25) |
| description | character varying(255) |
| currency_code | character varying(25) |
| exchange_rate | numeric |
| total_amount | numeric |
| total_fee_amount | numeric |
| total_other_amount | numeric |
| total_tax_at_pay | numeric |
| total_net_amount | numeric |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(35) |
| cash_amount | numeric |
| chq_amount | numeric |
| tranfer_amount | numeric |
| card_amount | numeric |
| total_amount_pay | numeric |
| total_income_amount | numeric |
| deposit_amount | numeric |
| advance_amount | numeric |
| petty_cash_amount | numeric |
| doc_time | character varying(5) |
| ap_ar_code | character varying(25) |
| pay_type | smallint |
| doc_format_code | character varying(25) |
| pay_cash_amount | numeric |
| money_change | numeric |
| coupon_amount | numeric |
| point_amount | numeric |
| point_qty | numeric |
| point_rate | numeric |
| total_credit_charge | numeric |
| branch_code | character varying(25) |
| cashier_code | character varying(25) |
| sale_shift_id | character varying(50) |
| discount_amount | numeric |
| total_income_other | numeric |
| total_expense_other | numeric |
| total_other_currency | numeric |
| is_doc_copy | smallint |
| wallet_amount | numeric |
| total_other_currency_charge | numeric |
| create_date_time_now | timestamp without time zone |

## cb_trans_detail

แถวโดยประมาณ: 4

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
| trans_number | character varying(100) |
| chq_ref | character varying(25) |
| pass_book_code | character varying(25) |
| bank_code | character varying(25) |
| bank_branch | character varying(100) |
| exchange_rate | numeric |
| amount | numeric |
| fee_amount | numeric |
| other_amount | numeric |
| tax_at_pay | numeric |
| sum_amount | numeric |
| period_number | smallint |
| approve_code | character varying(100) |
| approve_date | date |
| remark | character varying(255) |
| status | smallint |
| line_number | smallint |
| chq_date | date |
| chq_due_date | date |
| no_approved | character varying(100) |
| credit_card_type | character varying(25) |
| charge | numeric |
| doc_type | smallint |
| balance_amount | numeric |
| doc_date_ref | date |
| doc_time | character varying(5) |
| trans_number_type | smallint |
| ap_ar_type | smallint |
| ap_ar_code | character varying(25) |
| last_status | smallint |
| sale_shift_id | character varying(50) |
| external_chq | smallint |
| chq_on_hand | smallint |
| currency_code | character varying(25) |
| is_doc_copy | smallint |
| ref1 | character varying(50) |
| ref2 | character varying(50) |
| sum_amount_2 | numeric |
| create_date_time_now | timestamp without time zone |
| lost_profit_exchange_amount | numeric |
| exchange_rate_old | numeric |
| amount_2 | numeric |
| charge_2 | numeric |

## cb_trans_detail_draft

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
| trans_number | character varying(25) |
| chq_ref | character varying(25) |
| pass_book_code | character varying(25) |
| bank_code | character varying(25) |
| bank_branch | character varying(100) |
| exchange_rate | numeric |
| amount | numeric |
| fee_amount | numeric |
| other_amount | numeric |
| tax_at_pay | numeric |
| sum_amount | numeric |
| period_number | smallint |
| approve_code | character varying(25) |
| approve_date | date |
| remark | character varying(255) |
| status | smallint |
| line_number | smallint |
| chq_date | date |
| chq_due_date | date |
| no_approved | character varying(25) |
| credit_card_type | character varying(25) |
| charge | numeric |
| doc_type | smallint |
| balance_amount | numeric |
| doc_date_ref | date |
| doc_time | character varying(5) |
| trans_number_type | smallint |
| ap_ar_type | smallint |
| ap_ar_code | character varying(25) |
| last_status | smallint |
| sale_shift_id | character varying(50) |
| external_chq | smallint |
| chq_on_hand | smallint |
| create_date_time_now | timestamp without time zone |
| currency_code | character varying(25) |
| is_doc_copy | smallint |
| ref1 | character varying(50) |
| ref2 | character varying(50) |
| sum_amount_2 | numeric |
| lost_profit_exchange_amount | numeric |
| exchange_rate_old | numeric |
| amount_2 | numeric |
| charge_2 | numeric |
