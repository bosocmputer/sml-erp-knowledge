---
tags: [sml, dictionary, sync, generated]
module: Sync
---
# พจนานุกรม: Sync — Sync

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#sync_branch_list]] | Table 294 / Table 294 | 9 |
| [[#sync_field_list]] | Table 293 / Table 293 | 3 |
| [[#sync_log]] | Table 295 / Table 295 | 3 |
| [[#sync_table_list]] | Table 292 / Table 292 | 11 |

## sync_branch_list

**Table 294** — Table 294

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `branch_code` | รหัสสาขา |  | varchar(100) |  |
| `access_code` | รหัสสำหรับสาขา |  | varchar(100) |  |
| `branch_computer_name` | Serial เครื่องคอมพิวเตอร์ |  | varchar(100) |  |
| `active` | พร้อม Sync |  | smallint |  |
| `wait_time` | ระยะเวลาส่ง (วินาที) |  | smallint | ✓ |
| `branch_name` | ชื่อสาขา |  | varchar(100) | ✓ |
| `sync_time_active` | Sync ช่วงเวลา |  | smallint | ✓ |
| `start_sync_time` | เวลาเริ่ม |  | varchar(10) | ✓ |
| `end_sync_time` | ถึวเวลา |  | varchar(10) | ✓ |

## sync_field_list

**Table 293** — Table 293

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `table_name` | ชื่อ Table |  | varchar(100) |  |
| `field_name` | ชื่อ Field |  | varchar(100) |  |
| `default_value` | ค่า Default |  | varchar(100) | ✓ |

index: `sync_field_list_sync_field_list_idx_pk`(table_name,field_name), `sync_field_list_table_name`(table_name)

## sync_log

**Table 295** — Table 295

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `date_time` | วันที่ |  | datetime |  |
| `message` | รายละเอียด |  | varchar(100000) | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |

## sync_table_list

**Table 292** — Table 292

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `table_name` | ชื่อ Table |  | varchar(100) |  |
| `trans_type` | คำสั่ง |  | smallint |  |
| `send` | ส่งใหม่ทั้งหมด *(resource only)* |  | smallint |  |
| `received` | รับใหม่ทั้งหมด *(resource only)* |  | smallint |  |
| `sync_count` | จำนวนรายการ *(resource only)* |  | smallint |  |
| `trans_command` | Command |  | varchar(255) | ✓ |
| `sync_send_count` | รายการค้างส่ง *(resource only)* |  | char |  |
| `sync_receive_count` | รายการค้างรับ *(resource only)* |  | char |  |
| `always_sync` | Always Sync |  | smallint | ✓ |
| `sync_filter` | Sync Filter |  | varchar(2000) | ✓ |
| `sync_branch` | Sync Branch *(resource only)* |  | char |  |

index: `sync_table_list_sync_table_list_idx`(table_name)

