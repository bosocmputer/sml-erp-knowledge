# Database ของ SML

## รูปแบบต่อกิจการ (provider)

| Database | หน้าที่ |
|---|---|
| `smlerpmain<provider>` | ฐานควบคุม: รายชื่อ data DB (`sml_database_list`: data_code, data_name, data_database_name, data_group), ผู้ใช้/กลุ่ม/สิทธิ์ (`sml_user_list`, `sml_group_list`, `sml_permissions_*`, `sml_access_list`), session (`sml_guid`), ภาษา, `sml_screen_capture` |
| `<db>` | ข้อมูลธุรกิจ ~600 ตาราง schema `public` |
| `<db>_images` | รูป: `images` (image_id = รหัสสินค้า, guid_code, image_file bytea), `sml_doc_images`, `images_erp_user` |
| `<db>_logs` | `erp_logs` |

provider หนึ่งมีได้หลาย data DB และ **data DB เดียวลงทะเบียนได้หลาย provider** (aoy อยู่ทั้ง AOY และ NEXT) — ดู `sml_database_list` ใน `smlerpmain<provider>` เสมอ และอย่าสรุปว่า main database = `smlerpmain<ชื่อร้าน>`

> **อัปเดต 2026-10-21:** ได้สิทธิ์ superuser (ใช้แบบอ่านอย่างเดียว) แล้ว — ภาพรวมทุกร้าน, provider map และตัวเลือกร้าน ดู [[tenants-overview]] · ข้อมูลด้านล่างเป็นบันทึกวันที่ 2026-10-20 ตอนยังใช้ user read-only (บางตัวเลขเปลี่ยนแล้ว เช่น kbyt ic_trans เหลือ 2 ใบ)

## DB สำเนาของผู้ใช้ (สำรวจ 2026-10-20)

- PostgreSQL **11.1**, user แบบ read-only (ไม่ใช่ superuser) — **host, port, user, password ไม่เก็บใน vault** ขอจากผู้ใช้แล้วตั้งเป็น env `PGHOST`/`PGPORT`/`PGUSER`/`PGPASSWORD`
- Server เดียวกันมี DB ของกิจการอื่นอีกราว 60 ตัว และ user นี้มองเห็นรายชื่อทั้งหมด → แตะเฉพาะ DB ที่ผู้ใช้ระบุ
- ผู้ใช้อนุญาต: `kbyt`, `kbyt_images`, `kbyt_logs`, `smlerpmainkbyt`, `postgres`
- `smlerpmainkbyt.sml_database_list` ลงทะเบียน **KBYT และ KBYT_V** → `kbyt_v`, `kbyt_v_images`, `kbyt_v_logs` มีอยู่บน server แต่ user read-only ถูกปฏิเสธสิทธิ์อ่านตาราง (`permission denied for table ar_customer`)
- `kbyt` (1.5 GB): master data ครบ (ic_inventory ~20.5k, ar_customer ~27.8k, ap_supplier 848, ic_warehouse 3) แต่ **ธุรกรรมน้อยมาก** — ic_trans 16 ใบ (2026), gl_journal 0, erp_branch_list 0; มีตารางสำรอง `ic_trans_detail_20250209_111929` 583k แถว (doc_date 2021-01-04 ถึง 2025-02-08) และ `ic_trans_detail_20250209_111845`
- ตารางแถวเยอะ: erp_print_logs ~1.78M, gl_journal_allocate_list ~1.0M, gl_journal_job_list ~0.9M
- `kbyt_images` 2.6 GB: images ~13.9k แถว
- `kbgtest` คือ DB ที่ sml_mcp_ai/OpenClaw production ใช้ (พร้อม `kbgtest_images`)

- ชุด AOY (`smlerpmainaoy`, `aoy`, `aoy_images`, `aoy_logs`): ต่อได้ครบ 2026-10-20 มีธุรกรรมหลากหลายกว่า kbyt (ic_trans 923 ใบ) — ใช้เป็นชุดทดสอบหลัก ดู [[sql-capture-aoy]]

## Query ตัวอย่าง (อ่านอย่างเดียว, สรุปผล)

```bash
export PGHOST=<host> PGPORT=<port> PGUSER=<user> PGPASSWORD=<password> PGCONNECT_TIMEOUT=10  # ขอจากผู้ใช้ ห้าม commit
psql -d smlerpmainkbyt -c "select data_code, data_database_name from sml_database_list;"
psql -d kbyt -Atc "select trans_flag, count(*), min(doc_date), max(doc_date) from ic_trans group by 1 order by 2 desc;"
psql -d kbyt -Atc "select relname, n_live_tup from pg_stat_user_tables order by 2 desc limit 20;"
```

หมายเหตุ: ส่ง `-h ... -p ...` ผ่านตัวแปร shell เดียวใน zsh จะไม่แตกคำ — ใช้ env `PGHOST`/`PGPORT` แทน
