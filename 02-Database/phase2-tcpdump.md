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
- รอบ 4 (16:03–16:29): ใบสั่งขายจากใบเสนอราคา/แก้ไข/ยกเลิก, ใบวางบิล, รับชำระตามใบวางบิล+โอน, รับคืนเชื่อ 2 ใบ, จ่ายชำระ, สร้างสินค้า — ผลดู [[runtime-verified]] § รอบ 4
ผลดู [[runtime-verified]], [[write-spec-sale-order]]

## รอบ 4 (2026-10-21) — แผนที่ใช้ (ทำแล้ว 16:03–16:29; ขั้น 8 ทำเป็นรับคืนเชื่อแทน, ขั้น 11 ไม่ได้ทำ)
เป้าหมาย: เปลี่ยนสถานะเป็น verified-runtime สำหรับ [[write-spec-sale-order]] (ดึงจากใบเสนอราคา/แก้ไข/ยกเลิก), [[write-spec-billing-note]], [[write-spec-receipt]] (ตามใบวางบิล + โอน), [[write-spec-credit-note]], [[write-spec-ap-payment]], [[write-spec-master-product]]

สถานะก่อนเริ่ม (ตรวจ 2026-10-21, อ่านอย่างเดียว):
- `QT26090001` 2 รายการ (10 กล่อง, 1 ครั้ง) `used_status=0, doc_success=0, last_status=0`
- ลูกค้า ก: `BF-INV26100032` (60), `BF-INV26100033` (30), `BF-INV26100034` (48) — ขายเชื่อ ยังไม่วางบิล/ไม่รับชำระ
- ลูกค้า ข: `BF-INV26100035` (318), `BF-INV26100036` (315), `BF-INV26100038` (318) — ขายเชื่อ 2 รายการต่อใบ `used_status=0`
- ผู้ขาย: `PU26100001` (260) ซื้อเชื่อ ยังไม่จ่าย
- `erp_pass_book` 4 บัญชี · ไม่มีสินค้ารหัส `ZZ%` และบาร์โค้ด `8859999%`

| ขั้น | ทำอะไร | ยืนยันอะไร |
|---|---|---|
| 1 | Login provider **NEXT** → AOY | (login) |
| 2 | ขาย › บันทึกใบสั่งขาย › ใบใหม่ อ้างอิง `QT26090001` ดึง 2 รายการ ไม่แก้จำนวน › บันทึก › ปิดหน้าพิมพ์ — จดเลขที่ (SO-A) | สั่งขายจากใบเสนอราคา |
| 3 | เปิด SO-A › แก้รายการแรก 10 → 6 › บันทึก › ปิดหน้าพิมพ์ | แก้ไขเอกสาร (mode 2) |
| 4 | ขาย › รายงาน/ยกเลิก › ยกเลิกใบสั่งขาย › เลือก SO-A › **ยกเลิกทั้งหมด** › บันทึก — จดเลขที่ | ยกเลิก 37 (type 1) |
| 5 | ลูกหนี้ › ใบวางบิล › ลูกค้าของ `BF-INV26100032` › เลือก `BF-INV26100032` + `BF-INV26100033` › บันทึก — จดเลขที่ (BN-A) | ใบวางบิล 235 |
| 6 | ลูกหนี้ › รับชำระหนี้ › ลูกค้าเดียวกัน › **รับตามใบวางบิล BN-A** (90 บาท) › ช่องทาง**โอนเงิน**เข้าบัญชีใดก็ได้ › บันทึก — จดเลขที่ | รับชำระตามใบวางบิล + โอน (`cb_trans_detail` doc_type 1) |
| 7 | ขาย › รับคืนสินค้า/ลดหนี้ › ลูกค้าของ `BF-INV26100035` › ประเภท **รับคืนจากขายเงินเชื่อ** › อ้าง `BF-INV26100035` คืน 1 หน่วยของรายการแรก › บันทึก — จดเลขที่ | ลดหนี้ 48 inquiry 0 |
| 8 | ขาย › รับคืนสินค้า/ลดหนี้ › ลูกค้าเดียวกัน › ประเภท **ลดหนี้จากขายเงินเชื่อ (ไม่กระทบสต๊อก)** › อ้าง `BF-INV26100036` ลดราคา 15 บาท › บันทึก — จดเลขที่ | ลดหนี้ 48 inquiry 2 |
| 9 | เจ้าหนี้ › จ่ายชำระหนี้ › ผู้ขายของ `PU26100001` › เลือก `PU26100001` (260) › จ่าย**เงินสด** › บันทึก — จดเลขที่ | จ่ายชำระ 19 |
| 10 | สินค้า › ข้อมูลสินค้า › เพิ่ม `ZZTEST-0001` ชื่อ "ทดสอบ" หลายหน่วยนับ: ชิ้น (1/1, หน่วยมาตรฐาน+ต้นทุน), แพ็ค (6/1); บาร์โค้ด `8859999000011` (ชิ้น), `8859999000028` (แพ็ค); คลัง/ที่เก็บ 1 แถว › บันทึก | สร้างสินค้า |
| 11 | สินค้า › กำหนดบาร์โค้ดสินค้า › `ZZTEST-0001` › เพิ่ม `8859999000035` (ชิ้น) › บันทึก | หน้าจอบาร์โค้ด |
| 12 | ปิดโปรแกรม | logout |

- ทุกขั้นที่มีหน้าพิมพ์: **ปิดหน้าพิมพ์ทันที** (งานหลังบันทึกรอจนปิด)
- เอกสารที่สร้างอยู่ใน database demo AOY ของผู้ใช้ — ไม่ต้องยกเลิกภายหลัง
- หลังรอบนี้ Claude parse แบบไม่กรอง database แล้วเทียบสถานะ `QT26090001`, SO-A, บิลของลูกค้า ก/ข, `PU26100001`, สินค้า `ZZTEST-0001` ใน DB (อ่านอย่างเดียว) กับสถานะก่อนเริ่ม

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
