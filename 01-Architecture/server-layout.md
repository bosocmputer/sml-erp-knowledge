---
tags: [sml, server, docker, verified-runtime]
source: SSH เข้า server ทดสอบ (read-only) + compose files + /proc + smljavaws2 source + ผลคำสั่ง sudo ที่ผู้ใช้รันให้ (docker ps -a, docker network inspect, SMLConfig*.xml แบบปิดรหัส, env ของ container) — สำรวจ 2026-10-21
---
# โครงสร้าง server ที่รัน SML (server ทดสอบ/demo)

กลับไป [[00-Index]] · ภาพรวม [[architecture]] · ฐานข้อมูลแต่ละร้าน [[tenants-overview]]

> **ไม่เก็บ host, IP สาธารณะ, port ที่เปิดออกนอก, user/password ใน vault** — ค่าจริงอยู่ใน `~/dev/sml-connect/` ของเจ้าของเท่านั้น
> ดูเฉพาะส่วนของ SML ERP ตามที่ผู้ใช้อนุญาต (ไม่สำรวจบริการอื่นบนเครื่อง)

## โฟลเดอร์บริการ (`<deploy-root>/smlservice/`, เป็น git repo ของ deploy)

แต่ละโฟลเดอร์มี `docker-compose.yml` ของตัวเอง ทุกตัวใช้ network ภายนอกชื่อ `sml_service_network` และ reverse proxy คือ traefik (route ตาม `PathPrefix`)

| โฟลเดอร์ | image / หน้าที่ (จาก compose) | รันอยู่ไหม (2026-10-21) |
|---|---|---|
| `traefik_proxy` | traefik — route `/SMLJavaWebService`, `/SMLJavaRESTService`, `/rabbitmq` | **รัน** — `traefik_proxy-traefik-1` (traefik:v2.5) |
| `smljavawebservice` | `ghcr.io/smlsoft/smljavawebservice:3.9.7` (Tomcat), volume `../tomcat/temp:/usr/local/tomcat/temp`, **ไม่มี env `SML_NEXT_PROCESS_*`** | **รัน** — `smljavawebservice-smljavawebservice-1` (`657d8c47fdf6`), IP ใน network `172.18.0.3`; env ไม่มี `SML_*`/`STOCK_*`/`JAVA_OPTS`/`CATALINA_OPTS` และ command line ของ JVM ไม่มี `-D` ของ SML |
| `postgresql` | `ghcr.io/smlsoft/smlpostgres:11-thai` (`sml_postgresql`) + `smlpgbackup:11` (backup ทุกวัน 23:00, `BACKUPHOUR=23`) | **รัน** — `sml_postgresql` (Up 7 วัน ณ 2026-10-21, IP `172.18.0.7`) + `sml_postgresql_autobackup` |
| `smljavarestservice` | `smlsoft/smljavarestservice:3.0.3` (Tomcat), volume `../tomcat/temp` เดียวกัน | **ไม่มี container นี้** (`docker ps -a` ไม่พบ) — Tomcat ตัวที่ 2 (Java 1.8, `ada03f941bd7`) ไม่ใช่ image ของ SML ตามรายการที่กรอง (ชื่อไม่ตรง `sml|rabbit|postgres|traefik`) |
| `smljavawebservice_process` | `rabbitmq_smlprocess` (rabbitmq:management) + `sml_ws_process` (smljavawebservice 3.9.7 กับ `STOCK_PROCESS_CONSUMER_PROVIDER=RABBITMQ`, topic `when-request-stock-process`) | **ไม่มี container** (`docker ps -a` ไม่พบ `rabbitmq_smlprocess` / `sml_ws_process`) |
| `smlstockprocess` | `smlsoft/smlstockprocess:latest` (`SML_PROCESS_QUEUE=rabbitmq`) | **ไม่มี container** (`docker ps -a` ไม่พบ `sml_stockprocess`) |
| `smlsendstockprocessjob` | `smlsoft/smlstockprocessjob` อ่าน `conf/jobs.yml` (README: cron ส่งงานคำนวณสต็อกเข้า RabbitMQ ต่อ provider/database) | **ไม่มี container** และไม่มีไฟล์ `conf/jobs.yml` (มีแค่ `.keep`) |
| อื่น ๆ ของ SML | `smlreportservice`, `smlpricecenter`, `smlapprove`, `pickandpack`, `smlcloudservice`, `smlmis`, `smlphp`, `mobilestockweb`, `smlslideshow`, `smlrestservicedocs`, `tms` | ไม่ได้ตรวจ |

- สคริปต์เปิดเครื่อง `dockerrunallcontainer.sh` / `dockerrunallcontainer3.sh` สั่ง `up -d` แค่ **traefik_proxy → smljavawebservice → postgresql**
- ⇒ **บน server นี้ส่วน SML ที่รันมีแค่ 4 ตัว:** traefik, smljavawebservice, sml_postgresql, sml_postgresql_autobackup (ตรงกับสคริปต์เปิดเครื่อง) — ไม่มีตัวคำนวณต้นทุนแยก, ไม่มี RabbitMQ, ไม่มี SMLJavaRESTService
- container อื่นบนเครื่อง (บริการของโปรเจกต์อื่น) ไม่ใช่ส่วนของ SML ERP — ไม่ได้สำรวจ ยกเว้นตัวที่ต่อ database ของ SML (ตารางด้านล่าง)

## `tomcat/temp` = config ของ SMLJavaWebService (`java.io.tmpdir`)

ทุกไฟล์ owner root สิทธิ์ 640 (ผู้ใช้ ubuntu อ่านเนื้อหาไม่ได้ — บันทึกได้แค่ชื่อและหน้าที่จากโค้ด)

| ไฟล์ | หน้าที่ (จากโค้ด smljavaws2) |
|---|---|
| `SMLConfig<PROVIDER>.xml` × 6: AOY, CUS, CUSMS, DEMO, KBYT, NEXT | config ต่อ provider: `<server> <port> <user> <password> <main_database> <main_database_struct> <database_config> <database_id>` — **ค่าจริง (ปิด server/user/password):** `main_database` = `smlerpmain` + ชื่อ provider ตัวเล็ก ทุกไฟล์ (aoy, cus, cusms, demo, kbyt, next), `port` ว่าง, `main_database_struct` = `smlmaindatabase.xml`, `database_id` = 1 (PostgreSQL) |
| `SML_STRUCT_<PROVIDER>.XML` × 6 | ใช้ตอนตรวจโครงสร้าง DB (`_loadXmlFile` ข้ามถ้ามี `verifyskip.xml`) |
| `smlmaindatabase.xml`, `smldatabase.xml` (~1.8 MB), `smllogsdatabase.xml`, `smldatabaseverify.xml` | โครงสร้างตารางของ main / data / logs database ที่ client ส่งมาให้ server ตรวจ-สร้าง |
| `smlerpview.xml`, `smlerpviewtemplate.xml` | view ของระบบ |
| `providerlist.txt` | รายชื่อ provider ที่หน้า admin ของ web service จัดการ (`Routine._providerLoad/_providerSave`, ต้องผ่าน `_systemLogin`) |
| `pickandpackconf.xml`, `pickandpackconst.xml` | ของบริการ pickandpack |
| `*.gzip` (31 ไฟล์ ชื่อเป็น GUID) | ไฟล์ชั่วคราวของ web service (ยังไม่ได้ไล่ว่าใครสร้าง) |

ไฟล์ที่ **ไม่มี** (ตรวจ 2026-10-21) และผลตามโค้ด:
- `skip_process_cost.xml` ไม่มี → client `_isServerSkipProcess()` = false → **โปรแกรม Windows เริ่ม thread หยิบคิวต้นทุน** ([[stock-cost]] § ใครเป็นคนหยิบคิว); ฝั่ง server `SMLWSConfig.skipStockProcess` = false (ยืนยันแล้วว่าไม่ได้ตั้ง `SML_PROCESS_SKIP` ทั้งใน env และ `-D` ของ JVM)
- `smlstockprocess.cfg` ไม่มี และไม่ได้ตั้ง `SML_NEXT_PROCESS_SERVER`/`_PORT` (ไม่มีใน compose, env ของ container และ `-D` ของ JVM) → `SMLWSConfig.SendStockProcessNext` = false → **web service ใช้คิวแบบตาราง `process` ไม่ส่ง RabbitMQ** (`SMLWebService/Config/SMLWSConfig.java` `LoadConfigNextProcess`) — สอดคล้องกับ capture ที่เห็น `insert into process` ([[runtime-verified]])
- `verifyskip.xml`, `skipgetserverip.xml` ไม่มี

## client ของ database SML ใน `sml_service_network` (ชื่อจาก `docker network inspect` + พฤติกรรมจาก capture 3 รอบ)

| บริการ | database ของ SML ที่ใช้ | ทำอะไร (นับชนิดคำสั่ง, ไม่ดูค่า) |
|---|---|---|
| SMLJavaWebService (`smljavawebservice`) | ทุก tenant + main database ทุก provider | โปรแกรม SML ทั้งหมด (JDBC) |
| API ภายนอก A | tenant ทดสอบ 3 ตัว | อ่านอย่างเดียวในช่วง capture (`-- ping` + query) |
| API ภายนอก B (ระบบสมาชิก) | tenant ทดสอบ 2 ตัว (+ database ของตัวเอง) | อ่าน + **เขียนตรงเข้าตาราง SML**: `UPDATE ar_customer SET website …` |
| API ภายนอก C | tenant ทดสอบ 1 ตัว | อ่านอย่างเดียวในช่วง capture |
| API ภายนอก D | tenant ทดสอบ 1 ตัว | อ่านอย่างเดียวในช่วง capture |

- IP ใน docker เปลี่ยนได้เมื่อ container ถูกสร้างใหม่ — mapping นี้ใช้ได้กับ capture วันที่ 2026-10-21 เพราะ container เหล่านี้ Up ≥ 7 วันก่อน capture
- โปรเจกต์เหล่านี้เป็น**ตัวอย่างอ้างอิงเท่านั้น** (ไม่แก้) — แต่ยืนยันว่ามีหลายระบบเขียน/อ่าน database ของ SML ตรง ๆ โดยไม่ผ่าน web service ซึ่งเป็นเหตุผลที่ sml_mcp_ai ต้องเป็นมาตรฐานกลาง ([[mcp-project]])
- การเขียนตรงแบบนี้ไม่ผ่าน `logs`/`erp_logs`, ไม่มีแถวใน `sml_access_list` และไม่ใส่คิว `process` (เฉพาะที่เห็นใน capture)

## ยังไม่ทราบ
- Tomcat ตัวที่ 2 (Java 1.8, `ada03f941bd7`) เป็น container ไหน — ไม่อยู่ในรายการที่กรองด้วยชื่อ SML จึงไม่ใช่ส่วนของ SML ERP ตามขอบเขตที่ผู้ใช้กำหนด (ไม่ไล่ต่อ)
- `.gzip` ใน `tomcat/temp` ใครสร้าง
