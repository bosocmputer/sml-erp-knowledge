---
tags: [sml, schema, sale, generated]
---
# ตารางกลุ่ม `sale` (kbyt)

กลับไป [[schema-index]]

## sale_doc_trans_detail_temp

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| doc_no | character varying(255) |
| doc_date | date |
| branch_code | character varying(255) |
| cust_code | character varying(255) |
| item_code | character varying(255) |
| item_name | character varying(255) |
| unit_code | character varying(255) |
| unit_name | character varying(255) |
| line_number | numeric |
| stand_value | numeric |
| divide_value | numeric |
| purchases | numeric |
| ratio | numeric |
| cost_qty | numeric |
| cost_weight | numeric |
| cost_sum_weight | numeric |
| cost_factory_price | numeric |
| cost_sum_cost | numeric |
| exp_discount | numeric |
| exp_car | numeric |
| exp_other | numeric |
| exp_doc | numeric |
| exp_tax | numeric |
| exp_other2 | numeric |
| exp_each | numeric |
| sale_sum_lao_cost | numeric |
| sale_sum_cost | numeric |
| sale_price | numeric |
| sale_discount | character varying(255) |
| sale_sum_amount | numeric |
| sale_profit | numeric |
| sale_percent_profit | numeric |
| selling_price | numeric |
| create_datetime | timestamp without time zone |

## sale_doc_trans_temp

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| roworder | integer |
| trans_flag | numeric |
| doc_no | character varying(255) |
| doc_date | date |
| cust_code | character varying(255) |
| contactor | character varying(255) |
| branch_code | character varying(255) |
| sale_type | numeric |
| vat_type | numeric |
| vat_rate | numeric |
| total_cost_qty | numeric |
| total_cost_weight | numeric |
| total_cost_sum_weight | numeric |
| total_cost_purchases | numeric |
| total_cost_factory_price | numeric |
| total_cost_sum_cost | numeric |
| total_exp_discount | numeric |
| total_exp_car | numeric |
| total_exp_other | numeric |
| total_exp_doc | numeric |
| total_exp_tax | numeric |
| total_exp_other2 | numeric |
| total_exp_each | numeric |
| total_sale_sum_lao_cost | numeric |
| total_sale_sum_cost | numeric |
| total_sale_price | numeric |
| total_sale_sum_amount | numeric |
| total_sale_profit | numeric |
| total_sale_percent_profit | numeric |
| total_selling_price | numeric |
| cmd | character varying(255) |
| reason | character varying(255) |
| doc_time | time without time zone |
| status | smallint |
| project_name | character varying(255) |
| contact | character varying(255) |
| is_rival | smallint |
| alert | smallint |
| remark | character varying(255) |
| creator_code | character varying(255) |
| saler_code | character varying(255) |
| create_datetime | timestamp without time zone |
