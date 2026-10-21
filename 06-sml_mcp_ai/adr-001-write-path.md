---
tags: [sml, adr, sml_mcp_ai, write-api]
status: accepted (2026-10-21) — รายละเอียดการ implement ยังต้องคุยตาม CLAUDE.md ของ sml_mcp_ai
date: 2026-10-21
---
# ADR-001: sml_mcp_ai บันทึกเอกสารลง SML ด้วยทางไหน

กลับไป [[00-Index]] · หลักฐาน [[runtime-verified]] · [[document-engine]] · [[stock-cost]] · เป้าหมาย: sml_mcp_ai เป็น MCP/API มาตรฐานกลางของ smlerp (โปรเจกต์อื่นเป็นตัวอย่างเท่านั้น)

## บริบท
- business logic ของการบันทึกเอกสาร (ตรวจข้อมูล ~20 ขั้น, รันเลข, doc flow) อยู่ในโปรแกรม Windows (C#) — **ไม่มีบน server**
- SMLJavaWebService มีแค่การส่ง SQL ต่อ + งานสต็อก/ต้นทุน; endpoint รัน SQL ดิบไม่ตรวจสิทธิ์ และร้านเปิด port forward
- การบันทึก 1 ใบ = หลายตาราง ใน transaction เดียว + doc flow + log + งานสต็อกหลังบันทึก (ยืนยันจากการดักจับ SQL)

## ทางเลือกที่พิจารณา (ประชุมจำลอง 3 บทบาท)
| ทาง | สรุป | ผล |
|---|---|---|
| ก. เขียน PostgreSQL ตรงทั้งหมด รวมคำนวณต้นทุนเอง | คุมได้หมด แต่ต้องเขียนสูตรต้นทุน 5 วิธีใหม่ | ❌ ไม่เขียนสูตรต้นทุนเอง |
| ข. ผ่าน service ของ SML | service ไม่มี logic เอกสาร, ไม่มี transaction/log, ไม่ปลอดภัย | ❌ ไม่ใช้เป็นทางหลัก |
| **ค. ผสม** | เขียนเอกสาร/doc flow/log เองใน transaction เดียว, ให้ SML คำนวณต้นทุน | ✅ **เลือก** |

## คำตอบจากโค้ด (2026-10-21) ที่ทำให้ทาง ค ชัดขึ้น
1. **งานสต็อกหลังบันทึกแบ่งเป็น 2 ส่วน** (`smljavaws2 SMLICProcess._process_stock_balance` + `SMLProcess`):
   - **ส่วน 1 — ยอดคงเหลือ + ค้างรับ/ค้างส่ง/ค้างจอง:** เป็น **SQL ล้วน** (CTE ที่ดักจับได้ใน [[runtime-verified]] / [[stock-cost]]) รันทันทีเมื่อโปรแกรมเรียก SOAP `_process_stock_balance(itemList, calcFlag)`
   - **ส่วน 2 — ต้นทุน/ล็อต:** `_process_stock_balance` (ค่าเริ่มต้น `insertProcess = true`) **ใส่คิว** `process` (`process_name='IC'`) หรือส่งเข้า RabbitMQ/Redis ถ้าตั้ง `StockProcessQueueConfig` → worker ของ web service หยิบไปทำ `_process_stock_cost` แล้วลบแถวคิว
   - `processstockrequest` (REST) = ส่วน 2 แบบ synchronous + ส่วน 1 (`insertProcess=false`)
   - จากการดักจับ: web service poll ตาราง `process` ของร้านทุก ~10 วินาที **แม้ยังไม่มีใคร login** (เห็นตั้งแต่ 08:43 ก่อน login 08:48)
2. **ระบบเอกสารร่าง (`ic_trans_draft` …) ไม่ใช่ "บันทึกร่างทั่วไป"** — เป็นกลไก **ขออนุมัติวงเงินเครดิต** (`_companyProfile._request_ar_credit`): เมื่อยอดขายเกินวงเงิน โปรแกรมบันทึกเอกสารลงตารางร่าง + `erp_request_order` (รหัส OTP `approve_code`) → ผู้อนุมัติเห็นใน `_approveOrderControl` และอนุมัติ (`ic_trans_draft.approve_status = 1`) → ผู้ขายใส่ OTP แล้วบันทึกจริง → โปรแกรมลบร่าง
   - ⇒ **ไม่เหมาะเป็นช่องทาง "AI ร่าง คนกดบันทึก"** ทั่วไป (ผูกกับการอนุมัติเครดิต, เฉพาะเอกสารขาย)

## การตัดสินใจ
1. **ทางหลัก = ค (ผสม) แบบไม่ต้องเรียก endpoint ที่ไม่ตรวจสิทธิ์:**
   - ใน transaction เดียว: ตารางเอกสารตามสเปกต่อประเภท + doc flow ของเอกสารต้นทาง + `logs` + **SQL ส่วน 1** (ยอดคงเหลือ/ค้าง แบบเดียวกับ web service) + **ใส่คิว `process` 'IC'** ของสินค้าที่เกี่ยวข้อง
   - หลัง commit: `erp_logs` (อีก database) แบบมี reconcile
   - ต้นทุน/ล็อต: ให้ worker ของ SML ทำจากคิว (เหมือนโปรแกรม) → sml_mcp_ai ตรวจผลภายหลัง (`sum_of_cost` มีค่า, แถวคิวหายไป) และรายงานสถานะ `cost_status: pending|done|stuck`
   - **ทางสำรอง:** ถ้าร้านไม่มี worker ทำงาน (คิวค้างเกินเวลา) จึงเรียก `processstockrequest` ผ่าน network ภายในเท่านั้น
2. **AI agent ไม่สร้างเอกสารจริงในขั้นเดียว:** `preview_*` → คืนรายละเอียด + `confirmation_token` → คนยืนยัน → `commit_*`; staging/preview เก็บในฐานข้อมูลของ sml_mcp_ai เอง (ไม่ใช้ตารางร่างของ SML)
3. **API สำหรับระบบอื่น:** เขียนจริงได้ แต่ต้องมี idempotency key + hash ของ payload (เลขซ้ำ hash ต่าง → 409) + preview
4. **ทุกการเขียนต้องอ่านตัวเลือกร้านก่อน** (เช่น `gl_process_realtime`, `request_ar_credit`, `disable_ic_cost_process`) และปฏิเสธ/แจ้งเตือนเมื่อพฤติกรรมของ API ต่างจากโปรแกรม (เช่น ร้านที่ GL realtime, ร้านที่บังคับขออนุมัติเครดิต)
5. **เงื่อนไขก่อนเปิดใช้การเขียน:** แก้ช่องโหว่สิทธิ์ของ sml_mcp_ai (role จาก header), รองรับหลายร้าน, และมีชุดทดสอบเทียบกับ SQL จริงต่อประเภทเอกสาร (parity test)

## ผลที่ตามมา
- ต้องมี **สเปกการบันทึกต่อประเภทเอกสาร** ใน vault (ตาราง, field สำคัญ, doc flow, งานสต็อก, ตัวเลือกร้านที่เกี่ยว) ก่อนเขียนโค้ด
- ต้องยืนยันด้วยการรันจริง (ดักจับ SQL) อีก 2 เรื่องที่โค้ดตอบไม่ได้: (ก) server จริงใช้ worker แบบตาราง `process` หรือ queue ภายนอก (ข) คิวที่ใส่จากภายนอกถูกหยิบไปทำจริงในเวลาที่ยอมรับได้
- ลำดับประเภทเอกสาร: ใบสั่งขาย → ขาย (เชื่อ/เงินสด) → ยกเลิก/ลดหนี้ → รับชำระ แล้วค่อยขยาย
