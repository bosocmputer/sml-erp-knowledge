---
tags: [sml, runbook, phase2, reverse-engineering]
date: 2026-10-21
---
# เฟส 2: ดักจับ SQL จริงด้วย tcpdump (ชุด AOY)

กลับไป [[00-Index]] · ความครบถ้วน [[00-Completeness]] · ชุดทดสอบ [[sql-capture-aoy]]

## หลักการ
- SMLJavaWebService (`smljavawebservice-smljavawebservice-1`, IP ใน docker `172.18.0.3`) คุยกับ PostgreSQL (`sml_postgresql`, `172.18.0.7`) ผ่าน network `sml_service_network` และ **PostgreSQL ตั้ง `ssl = off`** → SQL วิ่งเป็นข้อความธรรมดา ดักด้วย tcpdump บน host ได้ **โดยไม่แตะ container และไม่ต้อง restart** (IP ยืนยันด้วย `docker network inspect` 2026-10-21 ดู [[server-layout]])
- **กรองด้วย IP ของ PostgreSQL ไม่ใช่ของ web service** — บันทึกเดิมระบุ web service = `172.18.0.5` ซึ่งผิด (`.5` คือ `nexflow-sml-api-bybos`); รอบ 2–3 ใช้ `host 172.18.0.7` และได้ SQL ครบ
- แปลงไฟล์ด้วย `scripts/parse_pg_pcap.py` (Python ล้วน) — แยก database จาก StartupMessage; แบ่งช่วงด้วย marker `ZZMARK-xx` หรือเวลาที่ผู้ใช้จด
- ⚠️ ไฟล์ .pcap มี SQL ของ**ทุกร้าน**บน server + ข้อมูลธุรกิจจริง + hash การ login DB → เก็บใน `~/sml-sqllog/` (chmod 700) เท่านั้น ลบจาก server ทันทีที่ copy เสร็จ **ห้ามใส่ vault**

## ขั้นที่ 0 — เตรียมบน server (ผู้ใช้ ubuntu)
```bash
mkdir -p ~/sml-capture && chmod 700 ~/sml-capture && echo READY
```

## ขั้นที่ 1 — เริ่มดักจับ (ค้างไว้ใน terminal จนทดสอบเสร็จ)
```bash
sudo tcpdump -i any -s 0 -U -Z ubuntu -w ~/sml-capture/aoy-runN.pcap "host 172.18.0.7 and tcp port 5432"
```
- รอจนขึ้น `listening on any …` แล้วค่อยทำขั้นที่ 2 · `-Z ubuntu` ให้ไฟล์เป็นของ ubuntu (scp ได้โดยไม่ต้องใช้ root)

## ขั้นที่ 2 — ตัด connection เดิม (DBeaver, superuser, กด Alt+X)
web service เก็บ connection ไว้ใช้ซ้ำ ถ้าไม่ตัด จะไม่เห็น StartupMessage ที่บอกชื่อ database
```sql
SELECT pid, datname, client_addr, pg_terminate_backend(pid) AS terminated
FROM pg_stat_activity
WHERE datname IN ('aoy','aoy_images','aoy_logs','smlerpmainaoy','smlerpmainnext')
  AND pid <> pg_backend_pid();
```
- ต้องมี `smlerpmainnext` ด้วย เพราะการทดสอบ AOY login ผ่าน provider NEXT ([[login-flow]])

## ขั้นที่ 3 — ทดสอบในโปรแกรม SML พร้อมจดเวลา
จดเวลาเริ่มแต่ละขั้น (นาที:วินาที ถ้าได้) และเลขที่เอกสารที่ได้ — marker `ZZMARK-xx` (พิมพ์ในช่องค้นหาสินค้าก่อนเริ่มขั้น) ใช้เสริมได้
ชุดขั้นตอนของแต่ละรอบอยู่ในหัวข้อ "รอบที่ดักแล้ว / รอบถัดไป" ด้านล่าง

## ขั้นที่ 4 — หยุดและ copy ไฟล์
```bash
# บน server: Ctrl+C ที่ tcpdump แล้วดูขนาด
ls -lh ~/sml-capture/
```
```bash
# บน Mac: copy แล้วลบไฟล์บน server ทันที
mkdir -p ~/sml-sqllog && chmod 700 ~/sml-sqllog && scp <ubuntu@server>:sml-capture/aoy-runN.pcap ~/sml-sqllog/ && ssh <ubuntu@server> rm -r sml-capture
```

## รอบที่ดักแล้ว
- รอบ 1 (2026-10-21 08:48–09:05): login, ขายสด/เชื่อ, ยกเลิกบิล, POS, ซื้อ, รายงาน
- รอบ 2 (09:43–10:15): ใบสั่งขาย SO26100001, บิลจากใบสั่งขาย, รับชำระ, ปรับปรุง/โอนสต็อก, ส่งเงิน POS, ประมวลผล GL
- รอบ 3 (10:39–10:44): รับชำระ, โอนสต็อก ซ้ำ
ผลดู [[runtime-verified]], [[write-spec-sale-order]]

## รอบ 4 (รอบถัดไป) — ใบสั่งขาย: ดึงจากใบเสนอราคา → แก้ไข → ยกเลิก
สถานะก่อนเริ่ม (ตรวจ 2026-10-21): `QT26090001` (2 รายการ: 10 กล่อง, 1 ครั้ง) `used_status=0, doc_success=0`, ไม่ถูกยกเลิก · ตัวเลือก `quotation_expire=0` (ดึงใบเสนอราคาที่เลยวันหมดอายุได้), `check_qty_over_doc_ref=0`

| ขั้น | ทำอะไร | สิ่งที่อยากเห็น |
|---|---|---|
| 1 | Login provider **NEXT** → data AOY | (ช่วงก่อนเริ่ม = login) |
| 2 | ขาย › **บันทึกใบสั่งขาย** → ใบใหม่ → อ้างอิงใบเสนอราคา `QT26090001` ดึงทั้ง 2 รายการ ไม่แก้จำนวน → บันทึก → ปิดหน้าพิมพ์ทันที → **จดเลขที่ใบสั่งขาย** | `doc_ref`/`doc_ref_type`/`ref_doc_no`/`ref_row` ของบรรทัด, doc flow ที่อัปเดต QT (`used_status`, `doc_success`) |
| 3 | เปิดใบสั่งขายจากขั้น 2 → **แก้ไข** จำนวนรายการแรก 10 → 6 → บันทึก → ปิดหน้าพิมพ์ | mode 2: ลบ/ใส่ใหม่ หรือ update, `logs` แบบ old/new, QT `doc_success` กลับเป็น 0 หรือไม่ |
| 4 | ขาย › รายงาน/ยกเลิก › **ยกเลิกใบสั่งขาย** → เลือกใบสั่งขายจากขั้น 2 → บันทึก → **จดเลขที่เอกสารยกเลิก** | เอกสาร 37 (`doc_ref`), สถานะใบสั่งขาย (`used_status`, `last_status`), QT กลับมาใช้ได้หรือไม่, ค้างส่ง |
| 5 | ปิดโปรแกรม | logout |

หลังรอบนี้ Claude ตรวจสถานะ QT26090001 และใบสั่งขายใน DB (อ่านอย่างเดียว) เทียบกับก่อนเริ่ม แล้วเติม [[write-spec-sale-order]] § แก้ไข / ยกเลิก / ดึงจากใบเสนอราคา

## ขั้นที่ 5 — แปลงเป็น SQL (Claude ทำให้)
```bash
python3 -I ~/dev/sml-knowledge/scripts/parse_pg_pcap.py ~/sml-sqllog/aoy-runN.pcap --out ~/sml-sqllog/aoy-runN-all
```
- **อย่ากรอง `--db` ตอน parse ครั้งแรก** — main database อาจไม่ใช่ `smlerpmain<ชื่อร้าน>` (AOY ใช้ `smlerpmainnext`) ตอนแรกกรองไว้จึงพลาด SQL login ทั้งหมด ([[login-flow]]) ให้ parse ทั้งหมดแล้วค่อยกรองตอนวิเคราะห์
- capture มี SQL ของ tenant อื่นที่ใช้ server เดียวกันปนมา (cus_ms, kbyt, samai ฯลฯ) — วิเคราะห์เฉพาะ database ของร้านที่ทดสอบ + main database ของ provider นั้น
- ได้ `statements.tsv` (SQL ดิบ มีข้อมูลจริง) และ `segments.md` (SQL แทนค่าด้วย `?` แยกตาม marker + ตารางที่อ่าน/เขียน)
- Claude สรุปผลลง vault เฉพาะโครงสร้าง (ลำดับคำสั่ง, ตาราง, เงื่อนไข) แล้วเปลี่ยนสถานะโน้ตที่ยืนยันได้เป็น `verified-runtime`

## ถ้ามีปัญหา
- ได้ 0 คำสั่งของ aoy → ลอง `--include-unknown` (connection เปิดก่อนเริ่มดัก) หรือทำขั้นที่ 1–2 ใหม่ · **อย่าใส่ `--db` ตอน parse ครั้งแรก**
- IP ของ PostgreSQL เปลี่ยน (container ถูกสร้างใหม่) → ดูใหม่ด้วย `sudo docker network inspect sml_service_network --format '{{range .Containers}}{{.Name}}  {{.IPv4Address}}{{"\n"}}{{end}}'`
- ไฟล์ใหญ่มาก → หยุดดักให้เร็วขึ้น/ทดสอบทีละ 2–3 ขั้น
