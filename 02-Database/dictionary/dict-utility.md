---
tags: [sml, dictionary, utility, generated]
module: Utility
---
# พจนานุกรม: Utility — Utility

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#device_uuid]] | device_uuid  | 2 |
| [[#erp_send_message]] | ส่งข้อความ / ERP Send Message | 10 |

## device_uuid

**device_uuid**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `uuid` | UUID |  | varchar(255) | ✓ |
| `gen_code_1` | GEN Code 1 |  | varchar(255) | ✓ |

## erp_send_message

**ส่งข้อความ** — ERP Send Message

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `send_type` | ประเภทการส่ง |  | smallint |  |
| `send_to` | ส่งถึง |  | varchar(1500) |  |
| `send_message` | ข้อความ |  | text |  |
| `send_date` | วันที่ให้ทำการส่ง |  | datetime | ✓ |
| `send_status` | สถานะการส่ง |  | smallint | ✓ |
| `date_add` | วันที่เพิ่ม |  | datetime | ✓ |
| `send_to_date` | วันเวลาที่ทำการส่ง |  | datetime | ✓ |
| `send_title` | หัวข้อ |  | varchar(1000) | ✓ |
| `send_process_guid` | guid เครื่องส่ง |  | varchar(100) | ✓ |
| `send_process_time` | เวลาทำการ process |  | datetime | ✓ |

