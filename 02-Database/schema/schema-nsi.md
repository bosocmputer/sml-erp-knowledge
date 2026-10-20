---
tags: [sml, schema, nsi, generated]
---
# ตารางกลุ่ม `nsi` (kbyt)

กลับไป [[schema-index]]

## nsi_app_settings

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| key | character varying(120) |
| value | jsonb |
| updated_by | character varying(25) |
| updated_at | timestamp without time zone |

## nsi_app_users

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | bigint |
| erp_user_code | character varying(25) |
| display_name | character varying(120) |
| role | character varying(20) |
| is_active | boolean |
| created_at | timestamp without time zone |
| updated_at | timestamp without time zone |

## nsi_audit_logs

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | bigint |
| user_code | character varying(25) |
| action | character varying(80) |
| resource_type | character varying(80) |
| resource_id | character varying(120) |
| before_data | jsonb |
| after_data | jsonb |
| ip_address | character varying(80) |
| user_agent | text |
| created_at | timestamp without time zone |

## nsi_document_locks

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| doc_no | character varying(80) |
| batch_id | bigint |
| locked_by | character varying(25) |
| status | character varying(20) |
| locked_at | timestamp without time zone |
| expires_at | timestamp without time zone |

## nsi_document_snapshots

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | bigint |
| batch_id | bigint |
| original_doc_no | character varying(80) |
| current_doc_no | character varying(80) |
| snapshot_data | jsonb |
| created_by | character varying(25) |
| created_at | timestamp without time zone |
| rolled_back_at | timestamp without time zone |
| rolled_back_by | character varying(25) |

## nsi_reflow_batch_items

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | bigint |
| batch_id | bigint |
| doc_no | character varying(80) |
| new_doc_no | character varying(80) |
| status | character varying(20) |
| message | text |
| before_data | jsonb |
| after_data | jsonb |
| removed_lines | jsonb |
| created_at | timestamp without time zone |
| updated_at | timestamp without time zone |

## nsi_reflow_batches

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| id | bigint |
| batch_no | character varying(40) |
| user_code | character varying(25) |
| status | character varying(20) |
| config | jsonb |
| total_count | integer |
| ready_count | integer |
| warning_count | integer |
| blocked_count | integer |
| applied_count | integer |
| failed_count | integer |
| started_at | timestamp without time zone |
| finished_at | timestamp without time zone |
| created_at | timestamp without time zone |
| updated_at | timestamp without time zone |

## nsi_schema_migrations

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| version | integer |
| name | character varying(120) |
| checksum | character varying(120) |
| applied_at | timestamp without time zone |
| applied_by | character varying(80) |
