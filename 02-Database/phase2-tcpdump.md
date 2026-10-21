---
tags: [sml, runbook, phase2, reverse-engineering]
date: 2026-10-21
---
# เฟส 2: ดักจับ SQL จริงด้วย tcpdump (ชุด AOY)

กลับไป [[00-Index]] · ความครบถ้วน [[00-Completeness]] · ชุดทดสอบ [[sql-capture-aoy]]

## หลักการ
- SMLJavaWebService (container `smljavawebservice-smljavawebservice-1`, IP ภายใน docker `172.18.0.5` ณ 2026-10-20) คุยกับ PostgreSQL (`sml_postgresql`) ผ่าน network ภายใน docker และ **PostgreSQL ตั้ง `ssl = off`** (ตรวจแล้ว) → SQL วิ่งเป็นข้อความธรรมดา ดักด้วย tcpdump บนเครื่อง host ได้ **โดยไม่แตะ container และไม่ต้อง restart**
- แปลงไฟล์ด้วย `scripts/parse_pg_pcap.py` (Python ล้วน ไม่ต้องลง tshark) — แยก database จาก StartupMessage และแบ่งช่วงด้วย marker `ZZMARK-xx`
- ⚠️ ไฟล์ .pcap มี SQL ของ**ทุกร้าน**ที่ใช้ web service ในช่วงนั้น + ข้อมูลธุรกิจจริง + hash การ login DB → เก็บใน `~/sml-sqllog/` เท่านั้น ลบจาก server ทันทีที่ copy เสร็จ **ห้ามใส่ vault**

## ขั้นที่ 0 — เตรียมบน server (`nextstep-node-2`, root)
```bash
which tcpdump                       # ถ้าไม่มี ต้องติดตั้ง (apt-get install -y tcpdump) — ขออนุญาตเจ้าของ server ก่อน
docker inspect smljavawebservice-smljavawebservice-1 -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}'
docker inspect sml_postgresql -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}'
mkdir -p /root/sml-capture && chmod 700 /root/sml-capture
```
จดค่า IP ของ web service (เรียกว่า `WS_IP`) — ปกติ `172.18.0.5`

## ขั้นที่ 1 — ตัด connection เดิมของชุด AOY (DBeaver, superuser)
web service เก็บ connection ไว้ใช้ซ้ำ ถ้าไม่ตัด จะดักไม่ได้ข้อความเปิด connection ที่บอกชื่อ database
```sql
SELECT pid, datname, client_addr, pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname IN ('aoy','smlerpmainaoy','aoy_images','aoy_logs') AND pid <> pg_backend_pid();
```

## ขั้นที่ 2 — เริ่มดักจับ (ทันทีหลังขั้นที่ 1)
```bash
tcpdump -i any -s 0 -U -w /root/sml-capture/aoy-run1.pcap "host $WS_IP and tcp port 5432"
```
- เปิดค้างไว้ใน terminal (หรือใช้ `tmux`) จนทดสอบเสร็จ
- `-s 0` เก็บทั้ง packet, `-U` เขียนลงไฟล์ทันที

## ขั้นที่ 3 — ทดสอบในโปรแกรม SML (เครื่อง Windows) พร้อม marker
**marker** = ค้นหาสินค้าด้วยข้อความ `ZZMARK-01`, `ZZMARK-02` … ในช่องค้นหาสินค้า/บาร์โค้ด **ก่อน**เริ่มแต่ละขั้น (หาไม่เจอไม่เป็นไร — คำค้นจะไปอยู่ใน SQL ใช้เป็นตัวแบ่งช่วง)

| ขั้น | ทำอะไร | marker ก่อนเริ่ม |
|---|---|---|
| 1 | Login provider AOY → เลือก database AOY → เข้าหน้าหลัก | ไม่ต้อง (ช่วงก่อน marker แรก = login) |
| 2 | เปิดเมนู ขาย → ขายสินค้าและบริการ (ยังไม่บันทึก) | `ZZMARK-02` |
| 3 | สร้างบิลขาย 1 ใบ สินค้า 2 รายการ แล้วบันทึก | `ZZMARK-03` |
| 4 | ยกเลิกบิลในขั้น 3 | `ZZMARK-04` |
| 5 | ขาย POS 1 บิล จ่ายเงินสด (พิมพ์ `ZZMARK-05` ในช่องบาร์โค้ดก่อน) | `ZZMARK-05` |
| 6 | ซื้อสินค้า 1 ใบ แล้วบันทึก | `ZZMARK-06` |
| 7 | เปิดรายงานยอดขาย 1 ตัว | `ZZMARK-07` |
| 8 | Logout | `ZZMARK-08` |

จดเวลาเริ่มแต่ละขั้นไว้ด้วย (สำรอง กรณี marker ไม่ถูกส่งเป็น SQL)

## ขั้นที่ 4 — หยุดและ copy ไฟล์
```bash
# บน server: กด Ctrl+C ที่ tcpdump แล้วดูขนาด
ls -lh /root/sml-capture/
```
```bash
# บน Mac
mkdir -p ~/sml-sqllog && scp root@nextstep-node-2:/root/sml-capture/aoy-run1.pcap ~/sml-sqllog/
```
```bash
# บน server หลัง copy สำเร็จ
rm /root/sml-capture/aoy-run1.pcap
```

## ขั้นที่ 5 — แปลงเป็น SQL (Claude ทำให้)
```bash
python3 ~/dev/sml-knowledge/scripts/parse_pg_pcap.py ~/sml-sqllog/aoy-run1.pcap \
  --db aoy --db smlerpmainaoy --db aoy_images --db aoy_logs --out ~/sml-sqllog/aoy-run1
```
- ได้ `statements.tsv` (SQL ดิบ มีข้อมูลจริง) และ `segments.md` (SQL แทนค่าด้วย `?` แยกตาม marker + ตารางที่อ่าน/เขียน)
- Claude สรุปผลลง vault เฉพาะโครงสร้าง (ลำดับคำสั่ง, ตาราง, เงื่อนไข) แล้วเปลี่ยนสถานะโน้ตที่ยืนยันได้เป็น `verified-runtime`

## ถ้ามีปัญหา
- ได้ 0 คำสั่งของ aoy → ลอง `--include-unknown` (connection เปิดก่อนเริ่มดัก) หรือทำขั้นที่ 1–2 ใหม่
- `WS_IP` เปลี่ยน → ใช้ค่าจาก `docker inspect` ในขั้นที่ 0
- ไฟล์ใหญ่มาก → หยุดดักให้เร็วขึ้น/ทดสอบทีละ 2–3 ขั้น
