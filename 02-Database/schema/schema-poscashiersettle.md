---
tags: [sml, schema, poscashiersettle, generated]
---
# ตารางกลุ่ม `poscashiersettle` (kbyt)

กลับไป [[schema-index]]

## poscashiersettle

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| docno | character varying(25) |
| docdate | timestamp without time zone |
| cashiercode | character varying(25) |
| machinecode | character varying(10) |
| pos_id | character varying(30) |
| cashamount | numeric |
| creditcardamount | numeric |
| coupongamount | numeric |
| chqamount | numeric |
| transferamount | numeric |
| manager_code | character varying(25) |
| trans_type | smallint |
| doc_time | character varying(5) |
| remark | character varying(255) |
| total_amount | numeric |
| total_cancel | numeric |
| total_balance | numeric |
| total_diff | numeric |
| total_credit_card | numeric |
| total_coupon | numeric |
| total_cash | numeric |
| total_sum | numeric |
| sum_amount | numeric |
| total_in | numeric |
| total_out | numeric |
| begin_date | timestamp without time zone |
| begin_time | character varying(25) |
| end_date | timestamp without time zone |
| end_time | character varying(25) |
| begin_user_code | character varying(25) |
| end_user_code | character varying(25) |
| total_out_credit | numeric |
| total_out_coupon | numeric |
| guid_code | character varying(35) |
| total_point | numeric |
| total_advance | numeric |
| total_after_advance | numeric |
| deposit_cash_amount | numeric |
| deposit_credit_amount | numeric |
| deposit_return_cash_amount | numeric |
| branch_code | character varying(25) |
| sale_credit_amount | numeric |
| order_amount | numeric |
| total_credit_charge | numeric |
| total_service_amount | numeric |
| total_vat_amount | numeric |
| transfer_amount | numeric |
| wallet_amount | numeric |
| total_currency_amount | numeric |
| total_currency_charge_amount | numeric |
| create_date_time_now | timestamp without time zone |

## poscashiersettle_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| bill_number | character varying(25) |
| banknotes_value | character varying(255) |
| number | character varying(255) |
| currency | character varying(255) |
| rate | character varying(255) |
| total_amount | character varying(255) |
| create_date_time_now | timestamp without time zone |
