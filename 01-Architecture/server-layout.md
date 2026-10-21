---
tags: [sml, server, docker, verified-runtime]
source: SSH เข้า server ทดสอบ (read-only, ผู้ใช้ไม่ใช่ root) + compose files + /proc + smljavaws2 source — สำรวจ 2026-10-21
---
# โครงสร้าง server ที่รัน SML (server ทดสอบ/demo)

กลับไป [[00-Index]] · ภาพรวม [[architecture]] · ฐานข้อมูลแต่ละร้าน [[tenants-overview]]

> **ไม่เก็บ host, IP สาธารณะ, port ที่เปิดออกนอก, user/password ใน vault** — ค่าจริงอยู่ใน `~/dev/sml-connect/` ของเจ้าของเท่านั้น
> ดูเฉพาะส่วนของ SML ERP ตามที่ผู้ใช้อนุญาต (ไม่สำรวจบริการอื่นบนเครื่อง)

## โฟลเดอร์บริการ (`/mnt/data/nextstep-node-2/smlservice/`, เป็น git repo ของ deploy)

แต่ละโฟลเดอร์มี `docker-compose.yml` ของตัวเอง ทุกตัวใช้ network ภายนอกชื่อ `sml_service_network` และ reverse proxy คือ traefik (route ตาม `PathPrefix`)

| โฟลเดอร์ | image / หน้าที่ (จาก compose) | รันอยู่ไหม (2026-10-21) |
|---|---|---|
| `traefik_proxy` | traefik — route `/SMLJavaWebService`, `/SMLJavaRESTService`, `/rabbitmq` | **รัน** (process `traefik`, uptime 16 วัน) |
| `smljavawebservice` | `ghcr.io/smlsoft/smljavawebservice:3.9.7` (Tomcat), volume `../tomcat/temp:/usr/local/tomcat/temp`, **ไม่มี env `SML_NEXT_PROCESS_*`** | **รัน** — container `657d8c47fdf6` (ยืนยันจาก `docker ps` ที่ผู้ใช้ส่งมา + cgroup ของ process Java OpenJDK) |
| `postgresql` | `ghcr.io/smlsoft/smlpostgres:11-thai` (`sml_postgresql`) + `smlpgbackup:11` (backup ทุกวัน 23:00, `BACKUPHOUR=23`) | **รัน** (ต่อ DB ได้) |
| `smljavarestservice` | `smlsoft/smljavarestservice:3.0.3` (Tomcat), volume `../tomcat/temp` เดียวกัน | ยังไม่ทราบ — มี Tomcat ตัวที่ 2 (Java 1.8, container `ada03f941bd7`) รันอยู่ แต่ยังไม่ได้ยืนยันว่าเป็น image ไหน |
| `smljavawebservice_process` | `rabbitmq_smlprocess` (rabbitmq:management) + `sml_ws_process` (smljavawebservice 3.9.7 กับ `STOCK_PROCESS_CONSUMER_PROVIDER=RABBITMQ`, topic `when-request-stock-process`) | **ไม่รัน** — ไม่มี process `beam.smp` (RabbitMQ) และมี Java แค่ 2 ตัว (Tomcat ทั้งคู่) |
| `smlstockprocess` | `smlsoft/smlstockprocess:latest` (`SML_PROCESS_QUEUE=rabbitmq`) | **ไม่รัน** (ไม่มี process ที่ตรง และ RabbitMQ ไม่รัน) |
| `smlsendstockprocessjob` | `smlsoft/smlstockprocessjob` อ่าน `conf/jobs.yml` (README: cron ส่งงานคำนวณสต็อกเข้า RabbitMQ ต่อ provider/database) | ไม่มีไฟล์ `conf/jobs.yml` (มีแค่ `.keep`) |
| อื่น ๆ ของ SML | `smlreportservice`, `smlpricecenter`, `smlapprove`, `pickandpack`, `smlcloudservice`, `smlmis`, `smlphp`, `mobilestockweb`, `smlslideshow`, `smlrestservicedocs`, `tms` | ไม่ได้ตรวจ |

- สคริปต์เปิดเครื่อง `dockerrunallcontainer.sh` / `dockerrunallcontainer3.sh` สั่ง `up -d` แค่ **traefik_proxy → smljavawebservice → postgresql**
- การตรวจว่ารันอยู่ไหมใช้ `ps`/`/proc/<pid>/cgroup` (ผู้ใช้ ubuntu อ่านได้) เพราะ `docker ps` ต้องใช้ sudo — ชื่อ container ของ Tomcat ตัวที่ 2 จึงยังไม่ทราบ

## `tomcat/temp` = config ของ SMLJavaWebService (`java.io.tmpdir`)

ทุกไฟล์ owner root สิทธิ์ 640 (ผู้ใช้ ubuntu อ่านเนื้อหาไม่ได้ — บันทึกได้แค่ชื่อและหน้าที่จากโค้ด)

| ไฟล์ | หน้าที่ (จากโค้ด smljavaws2) |
|---|---|
| `SMLConfig<PROVIDER>.xml` × 6: AOY, CUS, CUSMS, DEMO, KBYT, NEXT | config ต่อ provider: `<server> <port> <user> <password> <main_database> <main_database_struct> <database_config> <database_id>` (รูปแบบจาก `src/test/.../config/SMLConfigTest.java`; `database_id` 1 = PostgreSQL) |
| `SML_STRUCT_<PROVIDER>.XML` × 6 | ใช้ตอนตรวจโครงสร้าง DB (`_loadXmlFile` ข้ามถ้ามี `verifyskip.xml`) |
| `smlmaindatabase.xml`, `smldatabase.xml` (~1.8 MB), `smllogsdatabase.xml`, `smldatabaseverify.xml` | โครงสร้างตารางของ main / data / logs database ที่ client ส่งมาให้ server ตรวจ-สร้าง |
| `smlerpview.xml`, `smlerpviewtemplate.xml` | view ของระบบ |
| `providerlist.txt` | รายชื่อ provider ที่หน้า admin ของ web service จัดการ (`Routine._providerLoad/_providerSave`, ต้องผ่าน `_systemLogin`) |
| `pickandpackconf.xml`, `pickandpackconst.xml` | ของบริการ pickandpack |
| `*.gzip` (31 ไฟล์ ชื่อเป็น GUID) | ไฟล์ชั่วคราวของ web service (ยังไม่ได้ไล่ว่าใครสร้าง) |

ไฟล์ที่ **ไม่มี** (ตรวจ 2026-10-21) และผลตามโค้ด:
- `skip_process_cost.xml` ไม่มี → client `_isServerSkipProcess()` = false → **โปรแกรม Windows เริ่ม thread หยิบคิวต้นทุน** ([[stock-cost]] § ใครเป็นคนหยิบคิว); ฝั่ง server `SMLWSConfig.skipStockProcess` = false (ถ้าไม่ได้ตั้ง system property `SML_PROCESS_SKIP`)
- `smlstockprocess.cfg` ไม่มี และ compose ไม่ได้ตั้ง `SML_NEXT_PROCESS_SERVER`/`_PORT` → `SMLWSConfig.SendStockProcessNext` = false → **web service ใช้คิวแบบตาราง `process` ไม่ส่ง RabbitMQ** (`SMLWebService/Config/SMLWSConfig.java` `LoadConfigNextProcess`) — สอดคล้องกับ capture ที่เห็น `insert into process` ([[runtime-verified]])
- `verifyskip.xml`, `skipgetserverip.xml` ไม่มี

## client ของ PostgreSQL ที่เห็นจาก capture (เครือข่าย docker)
ดู [[runtime-verified]] — `172.18.0.3` = SMLJavaWebService (JDBC) ให้บริการทุก tenant; IP อื่นใน network เดียวกันต่อ database ของ SML ตรง ๆ (ยังไม่ทราบว่าเป็น container ไหน)

## ยังไม่ทราบ (ต้องใช้ sudo — ผู้ใช้ต้องรันเอง)
- ชื่อ/image ของ container Tomcat ตัวที่ 2 และ container ของ IP `172.18.0.2/.5/.10/.15`
- เนื้อหา `SMLConfig*.xml` (เพื่อยืนยัน `main_database` ของแต่ละ provider — ตอนนี้ยืนยันได้เฉพาะ NEXT → `smlerpmainnext` จาก SQL จริง [[login-flow]])
- environment ที่ส่งเข้า container smljavawebservice จริง (compose ไม่มี `SML_PROCESS_SKIP`; ยังไม่ได้ตรวจว่า image ตั้ง property นี้ไว้หรือไม่)
