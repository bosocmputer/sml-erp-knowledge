---
tags: [sml, database, runbook, reverse-engineering]
---
# Runbook: เก็บ SQL ที่โปรแกรม SML ส่งจริง (บน DB สำเนา)

เป้าหมาย: กดเมนู/ทำรายการในโปรแกรม แล้วเห็น SQL ทุกคำสั่งที่เกิดขึ้น → map เมนู → หน้าจอ → ตาราง → กฎธุรกิจ ได้แม่นยำ — กลับไป [[00-Index]] · ดู [[login-flow]]

> ทำ **เฉพาะบน server/DB สำเนา** เท่านั้น และ log จะมีข้อมูลธุรกิจจริงอยู่ในคำสั่ง SQL → **ห้าม commit ไฟล์ log เข้า vault**

## 1. เปิด log เฉพาะ DB ของ KBYT (ต้องใช้ superuser)

ตั้งระดับ database จะไม่เก็บ log ของกิจการอื่นบน server เดียวกัน และไม่ต้อง restart

```sql
-- prefix: เวลา, pid, db, user, application, client
ALTER SYSTEM SET log_line_prefix = '%m [%p] db=%d user=%u app=%a client=%h ';
SELECT pg_reload_conf();

ALTER DATABASE kbyt           SET log_statement = 'all';
ALTER DATABASE smlerpmainkbyt SET log_statement = 'all';
ALTER DATABASE kbyt_images    SET log_statement = 'all';
ALTER DATABASE kbyt_logs      SET log_statement = 'all';
-- ถ้าอยากได้เวลาที่ใช้ของแต่ละ query ด้วย ใช้แทน log_statement:
-- ALTER DATABASE kbyt SET log_min_duration_statement = 0;
```

มีผลกับ **connection ใหม่** เท่านั้น → restart SMLJavaWebService (หรือ Tomcat) หลังตั้งค่า เพื่อให้ connection pool ต่อใหม่

## 2. ชี้โปรแกรมไปที่ DB สำเนา

1. รัน SMLJavaWebService ที่ config (`SMLConfig<provider>.xml`) ชี้ host/port ของ server สำเนา — **ตรวจให้แน่ใจว่าไม่ได้ชี้ production**
2. เครื่อง Windows (หรือ VM) ที่ลง SML Account POS Professional ตั้ง web service server เป็นตัวในข้อ 1
3. Login provider `KBYT` เลือก database `KBYT`

## 3. ใส่ "ป้ายกำกับ" ก่อนทำแต่ละขั้น

ก่อนกดเมนูแต่ละครั้ง ส่ง marker เข้า log จะได้รู้ว่า SQL ช่วงไหนเป็นของเมนูไหน:

```bash
psql -d kbyt -c "select 'MARK: POS เปิดกะ'"
```

(Claude ส่ง marker ให้ได้ผ่าน user read-only เพราะ log_statement ใช้กับทุก session ของ DB นั้น)

แนะนำทำเป็นชุดสั้น ๆ ต่อรอบ เช่น POS: เปิดกะ → ขาย 1 บิล → ยกเลิกบิล → พักบิล → ปิดกะ

## 4. เอา log ออกมาให้ Claude อ่าน

PostgreSQL 11 จาก docker image ปกติเขียน log ไป stderr:

```bash
docker logs --since 30m <postgres-container> > ~/sml-sqllog/kbyt-$(date +%Y%m%d-%H%M).log 2>&1
```

ถ้าเปิด `logging_collector` ไว้ ให้ copy ไฟล์จาก `log_directory` แทน วางไฟล์ไว้ในโฟลเดอร์ที่ **ไม่ใช่** vault เช่น `~/sml-sqllog/` แล้วบอก Claude

## 5. ปิดเมื่อเสร็จ (rollback)

```sql
ALTER DATABASE kbyt           RESET log_statement;
ALTER DATABASE smlerpmainkbyt RESET log_statement;
ALTER DATABASE kbyt_images    RESET log_statement;
ALTER DATABASE kbyt_logs      RESET log_statement;
-- ALTER DATABASE kbyt RESET log_min_duration_statement;
ALTER SYSTEM RESET log_line_prefix;
SELECT pg_reload_conf();
```

## ข้อควรระวัง
- log โตเร็ว (โปรแกรม query บ่อย เช่น ping/GUID) — เปิดเฉพาะช่วงที่ทดสอบ
- ทำรายการทดสอบจะ **เขียนข้อมูลลง DB สำเนา** — ถ้าต้องการ DB สะอาดสำหรับรอบถัดไปให้ backup ก่อน
- ไม่แนะนำ grant `pg_read_file` ให้ user read-only เพื่ออ่าน log ผ่าน SQL เพราะจะอ่านไฟล์ใดก็ได้บน server
- ทางเลือกเสริม (ยังไม่ยืนยันว่า log SQL): web service มี log4j debug ตาม README ของ smljavaws2 (`LOG4J_CONFIGURATION_FILE=classpath:debug-log4j2.properties`)
