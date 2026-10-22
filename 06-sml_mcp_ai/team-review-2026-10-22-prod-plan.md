---
tags: [sml_mcp_ai, decision, team-review, production, deploy]
date: 2026-10-22
status: ข้อสรุปจากการประชุมจำลอง (บทบาทสมมติ) — แผนงานอยู่ใน ~/dev/smlmcpconnect/task.md
---
# ประชุมทีม (จำลอง) ครั้งที่ 2: แผน prod และการติดตั้ง — 2026-10-22

กลับไป [[00-Index]] · ครั้งที่ 1 [[team-review-2026-10-22-prod]] · ADR [[adr-001-write-path]] · ยังไม่ได้ทดสอบ [[00-Unverified]]

> ผู้เข้าร่วม 10 บทบาทจำลองเหมือนครั้งที่ 1 (PM, BA บัญชี, Tech Lead, Backend, SML Specialist, AI Engineer, Security, QA, DevOps/SRE, Customer Success) — ความเห็น/โหวตจำลองโดย Claude

## โจทย์จากเจ้าของ (ยืนยันแล้ว)
- ผู้ใช้: ทุกกลุ่ม ทยอยปล่อย (อ่านก่อน → ระบบอื่นเขียน → AI ร่างเอกสาร)
- ติดตั้งแบบผสม: ร้านบน server ของเรา → ศูนย์กลาง; ร้านที่มี server เอง → ติดตั้งแยก
- เริ่มที่ demo ไม่มีกำหนดเวลา; ติดตั้ง prod ที่ `192.168.2.109` ห้ามกระทบโปรเจกต์ที่รันอยู่

## ข้อเท็จจริงของ 192.168.2.109 (สำรวจอ่านอย่างเดียว 2026-10-22)
- Ubuntu 24.04.4, 4 core, RAM 7.6 GB (ว่าง ~3.9 GB), ดิสก์ 109 GB ใช้ 85% (เหลือ 17 GB); ผู้ใช้อยู่กลุ่ม `docker`, `sudo`
- container ที่รัน: ai-bcc-v2 (api, worker, frontend, assistant×2, egress×2, sentinel, postgres), ai-business-command-center (api, web, worker, db), openclaw-admin (+postgres `0.0.0.0:5432`), **smlmcpconnect (ตัวเก่า)**
- **smlmcpconnect ตัวเก่า:** `/home/bosscatdog/smlmcpconnect` (ไม่ใช่ git checkout, version-info 1.0.0), `127.0.0.1:3515`, `restart=unless-stopped`, ต่อ `kbgtest` บน nextstep ด้วย **`postgres`**, `MCP_ACCESS_MODE=admin`, รูปสินค้าผ่าน nginx `127.0.0.1:3516` → cloudflared quick tunnel
- โปรเจกต์ที่อ้างถึง smlmcpconnect: openclaw-admin, openclaw runtime/src, parts-lookup-chatbot (compose); billflow `.env` ชี้ `192.168.2.248:3515` (อีกเครื่อง)
- nginx: site `bossboard` (`:80` → `127.0.0.1:3003`) และ product-images proxy `127.0.0.1:3516`; cloudflared quick tunnel 4 ตัว (6324, 3055, 18789, 3516)
- port ที่ใช้: 22, 80, 3000, 3055, 3515, 3516, 4000, 4055, 5432, 6324, 18789, 20241–20244
- `docker-compose.yml` ของ repo มี **`container_name: smlmcpconnect`** ตายตัว ⇒ ใช้ไฟล์นี้ติดตั้งตัวที่สองบนเครื่องเดียวกันจะชนตัวเก่า

## การอภิปรายและโหวต
**M1 ที่ติดตั้ง** — DevOps: แยกโฟลเดอร์ `~/sml-mcp-prod`, compose project `smlmcp-prod`, ชื่อ container/network ใหม่, `mem_limit`+`cpus`, หมุน log (ดิสก์เหลือน้อย); Security: ห้ามใช้ network เดียวกับตัวเก่า — **10/0/0**

**M2 การเข้าถึงจากภายนอก** — Security: quick tunnel ไม่มี auth ชั้นนอกและ URL สุ่ม ห้ามใช้กับ MCP; ตัวเลือก (ก) LAN เท่านั้น + API key, (ข) Cloudflare named tunnel + Access ตั้งแต่แรก
- เห็นด้วย (ก) 8: เฟสแรกผู้ใช้อยู่ใน LAN, ลดพื้นผิวโจมตี
- ไม่เห็นด้วย 1 (PM): อยากให้เจ้าของร้านเรียกจากนอกออฟฟิศได้เร็ว
- งด 1 (CS)
- ⇒ มติ (ก) และเปิด (ข) ในเฟส 4

**M3 บัญชี database** — Security+BA: ตัวเก่าใช้ `postgres` เสี่ยงสูงสุด (เขียน/ลบได้ทุก database ของทุกร้าน); prod ใช้ `sml_mcp_ro` และ `sml_mcp_rw` แยก — **10/0/0** · หมายเหตุ: การสร้าง role ต้องเขียนบน PostgreSQL ของ nextstep ⇒ ต้องได้อนุมัติจากเจ้าของ

**M4 ที่เก็บข้อมูลของ sml_mcp_ai** (API key, tenant, idempotency, preview token, audit)
- Postgres แยก 6 (Tech Lead, Backend, QA, Security, AI, BA): ต้องการ transaction/unique constraint สำหรับ idempotency และ preview token ตอนเฟส 2, เครื่องมือเดียวกับ SML
- SQLite 4 (DevOps, CS, PM, SML Specialist): ดิสก์/RAM เครื่องจำกัด, ง่ายกว่าสำหรับร้านที่ติดตั้งแยก
- ⇒ มติ Postgres 1 container (`postgres:16-alpine`, ไม่ publish port) — ข้อกังวลทรัพยากรรับมือด้วย `mem_limit` และ `shared_buffers` ต่ำ
- ทุกคนเห็นตรงกัน: **ห้ามเก็บข้อมูลของ sml_mcp_ai ใน database ของ SML**

**M5 การออกเวอร์ชัน** — branch `release/prod`, tag `prod-vX.Y.Z`, build บน server จาก tag, เก็บ image ก่อนหน้าไว้ rollback — **9/0/1**

**M6 tenant** — Tech Lead: tenant = (provider, data_code) ตาม [[tenants-overview]]; API key ผูก tenant + role — **10/0/0**

**M7 secret** — `.env` chmod 600 บน server, ไม่อยู่ใน git, key เก็บ hash, log ห้ามมี secret — **10/0/0** · Security เสนอเพิ่ม: เปลี่ยนรหัสผ่าน SSH ของ .109 ที่ถูกพิมพ์ในแชท และเปลี่ยนเป็น SSH key

**M8 ตัวเก่า** — ไม่แตะในแผนนี้ ย้ายผู้ใช้มา prod เป็นแผนแยกหลังเฟส 1 — **9/0/1** · Security บันทึกความเสี่ยง: ตัวเก่ายังเปิด role admin + superuser ต่อไป

**M9 ลำดับการเขียน** — ใบสั่งขาย → บิลจาก SO → ใบวางบิล → รับชำระ ทีละประเภท
- เห็นด้วย 8
- ไม่เห็นด้วย 2 (BA, QA): อยากปิดเฟส 3 ที่ใบสั่งขายอย่างเดียวก่อน แล้วค่อยตัดสินใจรอบใหม่
- ⇒ มติตามลำดับ แต่ต้องผ่าน parity test ก่อนเปิดตัวถัดไป (ข้อกังวลของ BA/QA ถูกรวมเป็นเงื่อนไข)

## ข้อสรุป
- แผนงาน 5 เฟส + ขั้นตอนติดตั้ง + rollback อยู่ใน `~/dev/smlmcpconnect/task.md`
- prod แรก = **เฟส 1 อ่านแบบหลายร้านใน LAN ด้วย API key** บน .109 โดยไม่แตะตัวเก่า
- การเขียนเริ่มเฟส 3 หลัง write engine (เฟส 2) และ parity test

## เรื่องที่รอเจ้าของ
1. อนุมัติสร้าง role `sml_mcp_ro` / `sml_mcp_rw` บน nextstep
2. port `3520` บน LAN และรายชื่อเครื่องที่จะเรียก
3. วันเริ่มเฟส 0
