---
tags: [sml, dictionary, mobillyst-tms, generated]
module: Mobillyst_TMS
---
# พจนานุกรม: Mobillyst_TMS — Mobillyst TMS

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#erp_delivery_order]] | คำสั่งส่งสินค้า / ERP Delivery Order | 30 |
| [[#erp_delivery_order_item]] | รายละเอียดคำสั่งส่งสินค้า / Delivery Order Item | 12 |
| [[#erp_delivery_order_transaction_logs]] | Delivery Order Transaction Logs / Delivery Order Transaction Logs | 7 |

## erp_delivery_order

**คำสั่งส่งสินค้า** — ERP Delivery Order

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `order_no` | เลขที่ใบจัดส่ง |  | varchar(55) |  |
| `order_date` | วันที่ |  | smalldatetime |  |
| `doc_no` | เลขที่ใบขาย |  | varchar(255) |  |
| `doc_date` | วันที่ใบขาย |  | smalldatetime |  |
| `created_at` | วันที่สร้าง |  | datetime | ✓ |
| `created_by` | ผู้สร้าง |  | varchar(255) | ✓ |
| `cust_code` | รหัสลูกค้า |  | varchar(50) | ✓ |
| `cust_name` | ชื่อลูกค้า |  | varchar(255) | ✓ |
| `cust_contact` | ผู้ติดต่อ |  | varchar(100) | ✓ |
| `cust_address` | ที่อยู่ |  | varchar(255) | ✓ |
| `cust_province_id` | จังหวัด |  | varchar(255) | ✓ |
| `cust_amphur_id` | อำเภอ |  | varchar(255) | ✓ |
| `cust_tumbon_id` | ตำบล |  | varchar(255) | ✓ |
| `cust_zip_code` | รหัสไปรษณย์ |  | varchar(5) | ✓ |
| `cust_telephone` | โทรศัพท์ |  | varchar(50) | ✓ |
| `is_cod` | COD |  | smallint | ✓ |
| `cod_amount` | COD Amount |  | float | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `receive_date` | วันที่รับสินค้า |  | smalldatetime | ✓ |
| `receive_time` | เวลารับสินค้า |  | varchar(20) | ✓ |
| `delivery_date` | วันที่ส่งสินค้า |  | smalldatetime | ✓ |
| `delivery_time` | เวลาส่งสินค้า |  | varchar(20) | ✓ |
| `cust_latitude` | ละติจูด |  | float | ✓ |
| `cust_longitude` | ลองจิจูด |  | float | ✓ |
| `cod_payment_type` | COD Payment Type |  | varchar(100) | ✓ |
| `guid_code` | guid_code |  | varchar(50) | ✓ |
| `is_cancel` | Is cancel |  | smallint | ✓ |
| `canceled_at` | Canceled At |  | datetime | ✓ |
| `canceled_by` | Canceled By |  | varchar(255) | ✓ |
| `cancel_reason` | Cancel Reason |  | varchar(255) | ✓ |

## erp_delivery_order_item

**รายละเอียดคำสั่งส่งสินค้า** — Delivery Order Item

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `order_no` | เลขที่ใบจัดส่ง |  | varchar(25) |  |
| `doc_no` | เลขที่ใบขาย |  | varchar(255) |  |
| `line_number` | ลำดับ |  | smallint | ✓ |
| `item_code` | รหัสสินค้า |  | varchar(50) | ✓ |
| `item_name` | ชื่อสินค้า |  | varchar(255) | ✓ |
| `qty` | จำนวน |  | float | ✓ |
| `unit_code` | หน่วยนับ |  | varchar(50) | ✓ |
| `width` | กว้าง |  | float | ✓ |
| `length` | ยาว |  | float | ✓ |
| `height` | สูง |  | float | ✓ |
| `weight` | น้ำหนัก |  | float | ✓ |
| `warehouse_code` | คลังสินค้า |  | varchar(50) | ✓ |

## erp_delivery_order_transaction_logs

**Delivery Order Transaction Logs** — Delivery Order Transaction Logs

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `order_no` | order_no |  | varchar(50) |  |
| `order_date` | order_date |  | smalldatetime |  |
| `job_id` | job_id |  | varchar(255) |  |
| `mobillyst_order_no` | mobillyst_order_no |  | varchar(255) |  |
| `mobillyst_referance_id` | mobillyst_referance_id |  | varchar(255) |  |
| `created_at` | Created At |  | datetime | ✓ |
| `data` | Data |  | json | ✓ |

