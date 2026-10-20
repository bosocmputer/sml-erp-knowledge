---
tags: [sml, schema, wms, generated]
---
# ตารางกลุ่ม `wms` (kbyt)

กลับไป [[schema-index]]

## wms_boxes

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| wide | numeric |
| long | numeric |
| high | numeric |
| image_src | bytea |
| status | smallint |
| shelf_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## wms_boxes_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| box_code | character varying(50) |
| ref_doc_no | character varying(50) |
| is_from_cart | smallint |
| item_code | character varying(50) |
| qty | numeric |
| unit_code | character varying(50) |
| status | smallint |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_boxes_lot_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| box_code | character varying(50) |
| ref_doc_no | character varying(50) |
| is_from_cart | smallint |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| qty | numeric |
| last_update_date_time_now | timestamp without time zone |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## wms_boxes_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_guid | character varying(50) |
| from_box_code | character varying(50) |
| from_shelf_code | character varying(50) |
| to_box_code | character varying(50) |
| to_shelf_code | character varying(50) |
| created_at | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_boxes_trans_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_guid | character varying(50) |
| item_code | character varying(50) |
| qty | numeric |
| unit_code | character varying(50) |
| created_at | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_boxes_trans_lot

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| trans_guid | character varying(50) |
| ref_doc_no | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| qty | numeric |
| created_at | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_cart

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_guid | character varying(50) |
| receive_doc_no | character varying(50) |
| ref_doc_no | character varying(50) |
| creator_code | character varying(50) |
| create_datetime | timestamp without time zone |
| last_update_datetime | timestamp without time zone |
| last_update_user_code | character varying(50) |
| device_id | character varying(150) |
| remark | character varying(1000) |
| supplier_code | character varying(50) |
| cart_type | smallint |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| warehouse_code | character varying(50) |
| shelf_code | character varying(50) |
| branch_code | character varying(50) |
| worker_code | character varying(100) |

## wms_cart_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_guid | character varying(50) |
| ref_doc_no | character varying(50) |
| item_code | character varying(50) |
| qty | numeric |
| unit_code | character varying(25) |
| price | numeric |
| sum_amount | numeric |
| discount | character varying(100) |
| discount_amount | numeric |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_cart_lot

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_guid | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(50) |
| qty | integer |
| create_date_time_now | timestamp without time zone |
| last_update_date_time_now | timestamp without time zone |

## wms_cart_ref

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_guid | character varying(50) |
| ref_doc_no | character varying(25) |
| line_order | smallint |
| create_date_time_now | timestamp without time zone |

## wms_cart_serial

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| cart_guid | character varying(50) |
| item_code | character varying(50) |
| serial_number | character varying(255) |
| create_date_time_now | timestamp without time zone |
| last_update_date_time_now | timestamp without time zone |

## wms_job

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| box_code | character varying(50) |
| from_shelf | character varying(50) |
| to_shelf | character varying(50) |
| worker_code | character varying(50) |
| job_date | date |
| job_time | character varying(20) |
| remark | character varying(255) |
| last_update_date_time_now | timestamp without time zone |
| status | smallint |
| job_name | character varying(255) |
| is_readed | boolean |
| job_code | character varying(50) |
| job_type | character varying(10) |
| to_box_code | character varying(50) |
| box_type | character varying(10) |
| ref_doc_no | character varying(50) |
| is_manual | smallint |
| create_date_time_now | timestamp without time zone |

## wms_job_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| job_code | character varying(50) |
| box_code | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| qty | numeric |
| from_shelf | character varying(50) |
| to_shelf | character varying(50) |
| created_at | timestamp without time zone |
| to_box_code | character varying(50) |
| item_name | character varying(250) |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_job_lot_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| job_code | character varying(50) |
| box_code | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(50) |
| qty | numeric |
| from_shelf | character varying(50) |
| to_shelf | character varying(50) |
| created_at | timestamp without time zone |
| to_box_code | character varying(50) |
| create_date_time_now | timestamp without time zone |

## wms_location

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| branch_code | character varying(50) |
| warehouse_code | character varying(50) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## wms_pracel

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| pracel_guid | character(1) |
| ref_doc_no | character(1) |
| cust_code | character(1) |
| address | character(1) |
| cust_name | character(1) |
| create_date_time_now | timestamp without time zone |

## wms_product_adj_stock

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(20) |
| doc_type | character varying(15) |
| remark | character varying(255) |
| create_datetime | timestamp without time zone |
| creator_code | character varying(50) |
| last_update_datetime | timestamp without time zone |
| last_update_user_code | character varying(50) |
| status | smallint |
| create_date_time_now | timestamp without time zone |

## wms_product_adj_stock_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| box_code | character varying(50) |
| shelf_code | character varying(50) |
| qty | numeric |
| current_qty | numeric |
| diff_qty | numeric |
| last_update_datetime | timestamp without time zone |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_product_adj_stock_lot_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| box_code | character varying(50) |
| shelf_code | character varying(50) |
| qty | numeric |
| current_qty | numeric |
| diff_qty | numeric |
| last_update_datetime | timestamp without time zone |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_product_out

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| status | smallint |
| warehouse_code | character varying(32) |
| branch_code | character varying(32) |
| customer_code | character varying(25) |
| remark | character varying(255) |
| create_datetime | timestamp without time zone |
| creator_code | character varying(50) |
| last_update_datetime | timestamp without time zone |
| last_update_user_code | character varying(50) |
| total_amount | numeric |
| ref_doc_no | character varying(50) |
| doc_type | smallint |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_out_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| doc_time | character varying(20) |
| item_code | character varying(50) |
| item_name | character varying(255) |
| unit_code | character varying(50) |
| qty | numeric |
| price | numeric |
| discount | character varying(100) |
| discount_amount | numeric |
| sum_amount | numeric |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
| last_update_datetime | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_out_lot_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_out_doc | character varying |
| ref_out_date | date |
| item_code | character varying |
| lot_number | character varying |
| product_week | smallint |
| product_year | smallint |
| mfd_date | date |
| mfd_name | character varying(255) |
| expire_date | date |
| qty | smallint |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_out_ref

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| ref_doc_no | character varying(50) |
| line_order | smallint |
| create_date_time_now | timestamp without time zone |

## wms_product_out_serial_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_out_doc | character varying(50) |
| ref_out_date | date |
| item_code | character varying(50) |
| serial_number | character varying(255) |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_product_receive

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| doc_date | date |
| doc_time | character varying(10) |
| status | smallint |
| warehouse_code | character varying(32) |
| branch_code | character varying(32) |
| supplier_code | character varying(25) |
| remark | character varying(255) |
| create_datetime | timestamp without time zone |
| creator_code | character varying(50) |
| last_update_datetime | timestamp without time zone |
| last_update_user_code | character varying(50) |
| total_amount | numeric |
| ref_doc_no | character varying(50) |
| doc_type | smallint |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_receive_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(25) |
| doc_date | date |
| doc_time | character varying(20) |
| item_code | character varying(50) |
| item_name | character varying(255) |
| unit_code | character varying(50) |
| qty | numeric |
| price | numeric |
| discount | character varying(100) |
| discount_amount | numeric |
| sum_amount | numeric |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_receive_lot_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_rec_doc | character varying(50) |
| ref_rec_date | date |
| item_code | character varying(50) |
| lot_number | character varying(255) |
| product_week | smallint |
| product_year | smallint |
| mfd_date | date |
| mfd_name | character varying(255) |
| expire_date | date |
| qty | smallint |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |
| box_code | character varying(50) |
| shelf_code | character varying(50) |

## wms_product_receive_ref

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| doc_no | character varying(50) |
| ref_doc_no | character varying(50) |
| line_order | smallint |
| create_date_time_now | timestamp without time zone |

## wms_product_receive_serial_detail

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_rec_doc | character varying(50) |
| ref_rec_date | date |
| item_code | character varying(50) |
| serial_number | character varying(255) |
| product_week | smallint |
| product_year | smallint |
| mfd_date | date |
| mfd_name | character varying(255) |
| expire_date | date |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_product_trans

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_doc_no | character varying(50) |
| from_box_code | character varying(50) |
| to_box_code | character varying(50) |
| from_shelf_code | character varying(50) |
| to_shelf_code | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| qty | numeric |
| created_at | timestamp without time zone |
| ref_doc_type | character varying(50) |
| trans_guid | character varying(50) |
| create_date_time_now | timestamp without time zone |

## wms_product_trans_lot

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_doc_no | character varying(50) |
| item_code | character varying(50) |
| unit_code | character varying(50) |
| lot_number | character varying(255) |
| qty | numeric |
| created_at | timestamp without time zone |
| from_box_code | character varying(50) |
| to_box_code | character varying(50) |
| from_shelf_code | character varying(50) |
| to_shelf_code | character varying(50) |
| trans_guid | character varying(50) |
| create_date_time_now | timestamp without time zone |

## wms_serial_master

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ref_rec_doc | character varying(50) |
| ref_rec_date | date |
| item_code | character varying(50) |
| product_week | smallint |
| product_year | smallint |
| mfd_date | date |
| mfd_name | character varying(255) |
| expire_date | date |
| serial_number | character varying(255) |
| last_update_date_time_now | timestamp without time zone |
| create_date_time_now | timestamp without time zone |

## wms_workers

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(50) |
| name_1 | character varying(255) |
| description | character varying(255) |
| user_code | character varying(50) |
| status | smallint |
| create_date_time_now | timestamp without time zone |
