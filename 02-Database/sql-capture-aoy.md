---
tags: [sml, database, runbook, aoy]
---
# ทดสอบเก็บ SQL กับชุด AOY (ทีละขั้นตอน)

ใช้ร่วมกับ [[sql-capture-runbook]] — ข้อมูลชุด AOY สำรวจ 2026-10-20 ดูด้านล่าง

## สถานะชุด AOY (ตรวจแล้ว 2026-10-20 ด้วย user read-only)

| Database | ผล |
|---|---|
| `smlerpmainaoy` | ต่อได้, 17 ตาราง, ลงทะเบียน data DB เดียว: group `SML` / code `AOY` → ครบ ไม่มี DB ตกหล่น |
| `aoy` | ต่อได้, 521 ตาราง, 60 MB |
| `aoy_images` | ต่อได้, 3 ตาราง |
| `aoy_logs` | ต่อได้, 1 ตาราง |

ข้อมูลใน `aoy`: ic_trans 923 ใบ (2026-04-01 ถึง 2026-10-20), ic_trans_detail 1,754, สินค้า 67, ลูกค้า 15, ผู้จำหน่าย 18, คลัง 2, สาขา 0, gl_journal 188, ic_trans_detail_lot 544
trans_flag ที่มีมากสุด: 44 ขาย (649), 12 ซื้อ (43), 260 (42), 54 ยกมา (24), 48 ลดหนี้ (23), 45 ยกเลิกขาย (16), 250, 68, 410, 411, 451, 110, 40, 10, 11, 6, 70, 72, 4, 2, 30, 36, 46, 8, 32 — ดูความหมายที่ [[trans_flag]]
ข้อสังเกต: `is_cancel` = 0 ทุกใบ แต่มีเอกสาร flag 45 → การยกเลิกบันทึกเป็นเอกสารแยก; `sale_shift_id` ว่างทุกใบ → ร้านนี้ไม่ได้ใช้ระบบกะ

ค่า log ปัจจุบันของ server: `log_statement = none`, `log_destination = stderr`, `logging_collector = off`, `log_line_prefix = '%m [%p] '` → log ออก stderr ของ process/container

---

## ขั้นที่ 0 — เตรียม
- [ ] เครื่อง Windows (หรือ VM) ที่ลง SML Account POS Professional เวอร์ชันเดียวกับที่ลูกค้าใช้
- [ ] SMLJavaWebService (Tomcat หรือ docker `smlsoft/smljavawebservice`) ที่**ต่อกับ server สำเนาเท่านั้น**
- [ ] user ที่เป็น superuser ของ server สำเนา (ใช้ตั้งค่า log)
- [ ] สิทธิ์ดู log ของ PostgreSQL (`docker logs` หรือไฟล์ log)
- [ ] (แนะนำ) backup `aoy` ก่อน เพราะการทดสอบจะเขียนข้อมูลจริง:
  ```bash
  mkdir -p ~/sml-sqllog
  PGPASSWORD='<superuser password>' pg_dump -h <host> -p <port> -U <superuser> -Fc -d aoy -f ~/sml-sqllog/aoy-before-test.dump
  ```
  ต้องใส่ `-h/-p/-U` เสมอ ไม่งั้น pg_dump จะต่อ socket ในเครื่องตัวเอง; pg_dump 14 dump server 11 ได้ แต่ restore ต้องใช้ pg_restore 14

## ขั้นที่ 1 — เปิด log เฉพาะชุด AOY
ต่อ psql ด้วย superuser แล้วรัน:
```sql
ALTER SYSTEM SET log_line_prefix = '%m [%p] db=%d user=%u app=%a client=%h ';
SELECT pg_reload_conf();

ALTER DATABASE aoy           SET log_statement = 'all';
ALTER DATABASE smlerpmainaoy SET log_statement = 'all';
ALTER DATABASE aoy_images    SET log_statement = 'all';
ALTER DATABASE aoy_logs      SET log_statement = 'all';
```
**ตรวจ:** บอก Claude — Claude จะเปิด connection ใหม่แล้วเช็ก `show log_statement` ต้องได้ `all` และ `show log_line_prefix` ต้องมี `db=%d`

## ขั้นที่ 2 — ให้ web service ใช้ connection ใหม่
**ทางที่ใช้ได้โดยไม่ต้องเข้า server (ทำแล้ว 2026-10-20):** ตัด connection เดิมใน DBeaver ด้วย superuser แล้ว web service จะต่อใหม่เอง
```sql
SELECT pid, datname, usename, application_name, client_addr, backend_start, pg_terminate_backend(pid) AS terminated
FROM pg_stat_activity
WHERE datname IN ('aoy','smlerpmainaoy','aoy_images','aoy_logs') AND pid <> pg_backend_pid();
```
ข้อสังเกต: connection ของ SMLJavaWebService มาจาก `172.18.0.5` (network ภายใน docker → web service เป็น container บนเครื่องเดียวกับ PostgreSQL) และค้างอยู่หลายนาที → เวอร์ชันที่รันจริงเก็บ connection ไว้ใช้ซ้ำ (ต่างจากโค้ด v3.9.14 ที่ `HasConnectionPoolConfig()` คืน false)

**ทางเดิม (ถ้าเข้า server ได้):** restart web service
ค่าใหม่มีผลกับ connection ใหม่เท่านั้น → restart SMLJavaWebService (Tomcat/container) ที่ชี้ server สำเนา
**ตรวจ:** เปิด `http://<ws-host>:<port>/SMLJavaWebService/health` (หรือ path health ที่ใช้อยู่) ต้องตอบปกติ และ config ต้องชี้ host สำเนา ไม่ใช่ production

## ขั้นที่ 3 — ตั้งโปรแกรมฝั่ง Windows
1. เปิด SML Account POS Professional → หน้า Login
2. ตั้ง web service server = ตัวในขั้นที่ 2
3. Provider = `AOY`, Data group = `SML`, กรอก user/password ของโปรแกรม
4. **ยังไม่กด Login** — บอก Claude ว่าพร้อม

## ขั้นที่ 4 — บันทึกทีละขั้นพร้อม marker
ทำทีละข้อ: **บอก Claude ชื่อขั้น → รอ Claude ตอบว่า "MARK ส่งแล้ว" → ทำขั้นนั้นในโปรแกรม → บอกว่าเสร็จ**
(Claude ส่ง `select 'MARK: <ชื่อขั้น>'` เข้า DB `aoy` และ `smlerpmainaoy`)

ชุดแรกที่แนะนำ (ใช้เวลาประมาณ 20–30 นาที):

| # | ขั้น | สิ่งที่อยากเห็น |
|---|---|---|
| 1 | Login + เลือก DB AOY | ยืนยัน [[login-flow]] และ query ตอนเปิดหน้าหลัก |
| 2 | เปิดเมนู ขาย → ขายสินค้าและบริการ (ยังไม่บันทึก) | query โหลดหน้าจอเอกสาร |
| 3 | สร้างบิลขาย 1 ใบ สินค้า 2 รายการ แล้วบันทึก | ตารางที่ถูกเขียน (ic_trans, detail, ap_ar, gl, vat…) |
| 4 | ยกเลิกบิลในข้อ 3 | ยกเลิก = เอกสาร 45 หรืออัปเดตสถานะ |
| 5 | ขาย POS 1 บิล (เงินสด) | ความต่างระหว่าง POS กับขายปกติ |
| 6 | ซื้อสินค้า 1 ใบ | ฝั่งซื้อ + การคำนวณต้นทุน |
| 7 | เปิดรายงานยอดขาย 1 ตัว | query ของรายงาน |
| 8 | Logout | ปิด session (sml_guid) |

## ขั้นที่ 5 — ส่ง log ให้ Claude
ต้องเข้าเครื่อง server ได้ (log ออก stderr ของ container PostgreSQL) — ถ้าเข้าไม่ได้ ใช้แผน B: audit trigger เก็บ `current_query()` ของ INSERT/UPDATE/DELETE ลงตาราง `zz_sql_capture` ใน `aoy` (อ่านผ่าน user read-only ได้, ไม่ได้ SELECT)

```bash
mkdir -p ~/sml-sqllog
docker logs --since 2h <postgres-container> > ~/sml-sqllog/aoy-$(date +%Y%m%d-%H%M).log 2>&1
```
(ถ้าไม่ใช่ docker: copy ไฟล์ stderr/log ของ PostgreSQL ช่วงเวลาทดสอบ) — **ไม่วางไฟล์ไว้ใน vault**
บอก Claude path ของไฟล์ → Claude แยก SQL ตาม MARK แล้วเขียนผลลง vault (เฉพาะโครงสร้าง SQL/ตาราง ไม่คัดลอกข้อมูลลูกค้า)

## ขั้นที่ 6 — ปิด log (rollback)
```sql
ALTER DATABASE aoy           RESET log_statement;
ALTER DATABASE smlerpmainaoy RESET log_statement;
ALTER DATABASE aoy_images    RESET log_statement;
ALTER DATABASE aoy_logs      RESET log_statement;
ALTER SYSTEM RESET log_line_prefix;
SELECT pg_reload_conf();
```
(ถ้าอยากคืนข้อมูลก่อนทดสอบ: `pg_restore -h <host> -p <port> -U <superuser> --clean -d aoy ~/sml-sqllog/aoy-before-test.dump`)
