---
tags: [sml, sml_mcp_ai, write-spec, cancel, verified-runtime]
status: ยกเลิกบิลขาย (45) verified-runtime · ยกเลิกใบสั่งขายทั้งหมด (37 type 1) verified-runtime รอบ 4 · 37 type 2 from-code
source: capture aoy-run1 (SIC00010001 ยกเลิก INV26100001, 08:57–08:59) + DB aoy/kbgtest/samai/debug_kbgds_data1/demo/wawacrm (2026-10-21) + smlerp _icTransControl.cs, _icTransScreenTopControl.cs, SMLProcess/_docFlowThread.cs, _processThread.cs
---
# สเปกการบันทึก: เอกสารยกเลิก (45 ยกเลิกบิลขาย, 37 ยกเลิกใบสั่งขาย)

กลับไป [[00-Index]] · บิลขาย [[write-spec-sale-invoice]] · ใบสั่งขาย [[write-spec-sale-order]] · สายเอกสาร [[doc-flow-rules]]

## หลักการ (ยืนยันแล้ว)
- **การยกเลิก = สร้างเอกสารใหม่อีกใบ** (trans_flag ยกเลิก) ที่ `doc_ref` = เลขเอกสารต้นทาง — **ไม่แก้/ไม่ลบ**แถวของต้นทางใน transaction ที่บันทึก
- ต้นทางถูกปิดทีหลังด้วย **doc flow**: `last_status = 1` ทั้งหัว รายการ และตารางที่เกี่ยวข้อง
- รายงาน/ยอดคงเหลือ/ยอดลูกหนี้กรองด้วย `last_status = 0` (สูตรใน [[stock-cost]] และ [[write-spec-sale-invoice]] §1.3)
- ⚠️ มีอีกกลไกหนึ่งในโค้ด `CancelDocumentQuery` (`_icTransControl.cs` ~8996): `update ic_trans set is_cancel=1, last_status=0, cancel_code, cancel_datetime …` + ลบ `gl_journal`/`gl_journal_detail` ของเอกสารนั้น — **ไม่ใช่เส้นทางของเมนูยกเลิกบิล 45** (บิลที่ยกเลิกด้วย 45 ทุกร้านที่ตรวจมี `is_cancel = 0`, `last_status = 1`: aoy 17, kbgtest 2,252, samai 2,446, debug_kbgds_data1 161) — ยังไม่ได้ไล่ว่าเมนูไหนใช้ `CancelDocumentQuery`

## A. ยกเลิกบิลขาย (45) — ขายสด INV26100001

### A.1 ก่อนบันทึก
- เลือกบิลของลูกค้า: `ic_trans where cust_code=? and trans_flag=44`
- อ่านสถานะต้นทาง `select doc_date, last_status, doc_success, used_status, used_status_2 from ic_trans where upper(doc_no)=?`
- **ห้ามยกเลิก** (`_icTransScreenTopControl.cs` ~5491, ข้อความ `__docWarning1..3` ~4718): `last_status=1` ("มีการยกเลิกไปแล้ว"), `doc_success=1` ("ปิดรายการไปแล้ว"), `used_status=1` หรือ `used_status_2=1` ("มีการอ้างอิงรายการไปแล้ว" — เช่น รับชำระแล้ว/ลดหนี้แล้ว) → ล้าง `doc_ref` และไม่ให้บันทึก
- เลขที่: `erp_doc_format code='SIC'` (AOY: `@YYMM####`) — รอบ 1 ได้ `SIC00010001` เพราะตอนออกเลข วันที่เอกสารยังเป็นค่าว่าง (SQL หาเลขล่าสุด `doc_date >= '1900-01-01' and doc_no like 'SIC0001%'` ⇒ YYMM = 0001) · รอบ 5.6 ได้ `SIC26100001` ตามรูปแบบ (`doc_date >= '2026-01-01' and like 'SIC2610%'`) + `select doc_no … like ? AND trans_flag = 45 …`

### A.2 Transaction หลัก (08:58:16.981–.986) — **หัวอย่างเดียว ไม่มีรายการ**
`insert into ic_trans (trans_type=2, trans_flag=45, status=0, doc_date, doc_time, cust_code, doc_no, doc_format_code='SIC', doc_ref='<เลขบิล>', doc_ref_date=null, remark, remark_2..5, is_pos=0, creator_code, create_datetime)` — 18 คอลัมน์ · `total_amount` = 0 (ตรวจใน DB) · `ic_trans_detail` ของ SIC = 0 แถว

### A.3 หลัง commit
1. `select item_code from ic_trans_detail where doc_no='<เลขบิล>'` — เอารายการสินค้าของบิลต้นทางไปประมวลผลสต็อก
2. `logs` / `erp_logs` (`screen_code=45`)
3. พิมพ์ (08:58:55 อ่าน `form_code`) — งานถัดไปรอจนปิดหน้าพิมพ์
4. **doc flow ปิดบิลต้นทาง** (transaction เดียว 08:58:56.022–.044):
   - `update ic_trans set last_status=1 where roworder=<บิล>`
   - `update ic_trans_detail set last_status=1 where doc_no=? and trans_flag in (44) and last_status<>1`
   - `update ap_ar_trans_detail set last_status=1 … trans_flag in (44)`
   - `update cb_trans set status=1 where doc_no=? and trans_flag=44 and status<>1` ← **การรับเงินของบิลสดถูกปิดด้วย `status`** (ตรวจใน DB: `cb_trans.status=1`, ยอด 590 ยังอยู่)
   - `update cb_trans_detail set last_status=1 …`
5. ล้าง `cb_chq_list`, serial, `_updateDateTimeForCalc`
6. **`_process_stock_balance(items, "44")`** — `_processThread._run` แปลงประเภท `ขาย_ขายสินค้าและบริการ_ยกเลิก` → `ขาย_ขายสินค้าและบริการ` ก่อนเรียก จึงคำนวณยอดคงเหลือใหม่ (บรรทัดบิลถูกตัดออกเพราะ `last_status=1`) + ค้างจอง/ส่ง + คิว `process` 'IC'
7. worker คำนวณต้นทุนใหม่ (08:59:01–02 ลบแถวคิว 1743, 1744)

### A.4 สิ่งที่**ไม่**ถูกแตะ
- `gl_journal_vat_sale` ของบิลยังอยู่ (ตรวจ DB: 1 แถว ยอด VAT 38.60) — รายงานภาษีขายแสดงแถวนี้เป็นยอด 0 เพราะเช็ค `last_status` ของบิล ([[tax-period]] §1)
- `cb_trans` ไม่ถูกลบ (แค่ `status=1`)
- **GL:** การประมวลผล GL แบบ batch เลือกเอกสารด้วย `coalesce(is_cancel,0)=0` (ไม่ดู `last_status`) → บิลที่ยกเลิกด้วย 45 **ยังถูกลง GL** (AOY: INV26100001 มี `gl_journal` 6 บรรทัด, ร้านอื่นก็เป็นแบบเดียวกัน) และ **GL กลับรายการเกิดจากตัวเอกสาร 45 เอง** ถ้ารูปแบบเอกสารยกเลิกตั้ง `gl_book` และถูกเลือกในการประมวลผล GL:
  | ร้าน | รูปแบบเอกสาร 45 | `gl_book` | `gl_journal` ของ 45 | `gl_journal` ของบิล 44 ที่ถูกยกเลิก |
  |---|---|---|---|---|
  | aoy | SIC | ว่าง | 0 | 3 |
  | kbgtest | SAC-* | 03 | 2,249 | 2,254 |
  | samai | SIC1 (ว่าง), SIC2 (02) | | 1,519 | 1,368 |
  | debug_kbgds_data1 | | | 160 | 160 |
  ⇒ ใน AOY (demo) บัญชีของบิลที่ยกเลิกไม่ถูกกลับรายการ เพราะการตั้งค่ารูปแบบเอกสาร — `erp_doc_format_gl` ของรูปแบบยกเลิกเป็น 0 แถวทุกร้าน จึงยังไม่ทราบว่า GL ของ 45 ใช้ผังบัญชีจากไหน

### A.5 ยืนยันจากรอบ 5.6: ยกเลิกบิลขาย**เชื่อ** (SIC26100001 ยกเลิก BF-INV26100039, 12:22:26 วันที่ 2026-10-26)
- **เหมือนขายสดทุกขั้น:** transaction มี `insert ic_trans` (หัว 18 คอลัมน์, `doc_ref=<บิล>`, `remark`) อย่างเดียว ไม่มี `ic_trans_detail` → `COMMIT`
- doc flow (1.5 วินาทีหลัง commit): `ic_trans.last_status=1` ของบิล + `ic_trans_detail`/`ap_ar_trans_detail` `last_status=1` + `update cb_trans/cb_trans_detail … status/last_status=1` (ไม่มีแถว จึงไม่มีผล)
- สต็อก: คิว `process` ของสินค้าในบิล → worker ลบแถวล็อตของบิล (`ic_trans_detail_lot`) และคำนวณต้นทุนใหม่ (AH-0001 227.30 → 226.68) · ตรวจ DB: `balance_qty` 122 → **123**
- `gl_journal_vat_sale` ของบิลยังอยู่ (ฐาน 224.30 ภาษี 15.70) เหมือน A.4
- บิลเชื่อที่ยกเลิกได้ต้องยังไม่วางบิล/รับชำระ/ลดหนี้ (`used_status=0, used_status_2=0`) ตาม A.1

## B. ยกเลิกใบสั่งขาย (37) — type 1 ยืนยันแล้ว (B.0) · type 2 from-code + ข้อมูลจริง
- เมนู ขาย › รายงาน/ยกเลิก › ยกเลิกใบสั่งขาย (`menu_so_sale_order_cancel`, `SMLERPSO._soSaleorderCancel`, [[menu-map]])
- หน้าจอมี `cancel_type` (`_icTransScreenTopControl.cs` ~452): **1 = ยกเลิกทั้งหมด, 2 = ยกเลิกรายสินค้า** (ป้ายจาก `smldatabase.xml`)
- ข้อมูลจริง (จำนวนเอกสาร 37 แยกตาม `cancel_type` / มีบรรทัดหรือไม่):
  | ร้าน | type 1 ไม่มีบรรทัด | type 1 มีบรรทัด | type 2 ไม่มีบรรทัด | type 2 มีบรรทัด |
  |---|---|---|---|---|
  | kbgtest | 1,668 | 6,007 | 57 | 1,202 |
  | wawacrm | 57 | 248 | 7 | 2,583 |
  | demo | 8 | 0 | 0 | 3 |
- กฎ doc flow ของใบสั่งขาย (`_docFlowThread.cs` ~2291):
  - **ยกเลิก (`last_status=1`)** นับเฉพาะ 37 ที่ `cancel_type = 1` ที่ `doc_ref` = ใบสั่งขาย
  - **ถูกใช้ (`used_status`)** = มี 52 (อนุมัติ) อ้าง หรือมีบรรทัดอื่นอ้าง `ref_doc_no`
  - **สิ้นสุด (`doc_success`)** = จำนวนที่ถูกตัดจากบรรทัด `trans_flag in (37, 44)` ที่ `ref_doc_no` = ใบสั่งขาย ≥ จำนวนในใบสั่งขาย ⇒ **ยกเลิกรายสินค้า (type 2) ทำงานเหมือน "ตัดจำนวน" ไม่ได้ปิดใบ**
  - ค้างส่ง (`accrued_out_qty`) ลดลงตามบรรทัด 37 ที่ `cancel_type = 2` (CTE `accout` ใน [[stock-cost]])
- สถานะใบสั่งขายหลังถูกยกเลิก (kbgtest, นับคู่ 37→36 ที่หาใบต้นทางเจอ): **type 1 → `last_status=1` ทุกใบ (7,600/7,600)**; type 2 → `last_status=0` 966 ใบ (ในนั้น `doc_success=1` 936) และ `last_status=1` 249 ใบ (ยังไม่ได้ตรวจว่ามี 37 type 1 อีกใบมาปิดหรือไม่) — ตรงกับกฎข้างบน
- Nexflow ยืนยันกับ AOY (2026-09-03) ว่ายกเลิก 37 ทำให้ 36 `used_status=1` ([[nexflow-lessons]])

## C. สำหรับ sml_mcp_ai
- `cancel_sale_invoice(doc_no)`: ตรวจกฎ A.1 → transaction เดียว: insert หัว 45 (A.2) **+ doc flow ปิดต้นทาง (A.3 ข้อ 4)** + SQL ส่วนที่ 1 ของสต็อกด้วย flag 44 + คิว `process` 'IC' → `logs`; หลัง commit `erp_logs`
  - ใส่ doc flow ในชุดเดียวกันได้เพราะเป็น `update` ที่กำหนดผลได้แน่นอน (ต่างจากโปรแกรมที่ทำแยกและทำหลังปิดหน้าพิมพ์ — ช่วงนั้นบิลยังนับเป็นยอดขาย/ยอดคงเหลืออยู่)
  - แจ้งผู้ใช้เรื่อง GL: ถ้ารูปแบบเอกสาร 45 ของร้านไม่มี `gl_book` บัญชีจะไม่ถูกกลับรายการ (พฤติกรรมเดียวกับโปรแกรม)
- `cancel_sale_order(doc_no)` แบบ**ยกเลิกทั้งหมด**: เปิดได้ตาม B.0 · แบบ**ยกเลิกรายสินค้า (type 2)**: ยังไม่เปิดจนกว่าจะ capture

## ยังไม่ทราบ
- ทำไมรอบ 1 วันที่เอกสารยังว่างตอนออกเลข (`SIC00010001`) — รอบ 5.6 ออกเลขปกติ อาจขึ้นกับลำดับการกดในหน้าจอ
- ผังบัญชีที่ใช้ลง GL ของเอกสาร 45 (ไม่มีใน `erp_doc_format_gl`)
- เมนูที่ใช้ `CancelDocumentQuery` (`is_cancel=1`)

## B.0 ยืนยันจากรอบ 4: ยกเลิกใบสั่งขายทั้งหมด (SSC26100001 ยกเลิก SO26100002, 16:10:01)
- **Transaction:** `insert ic_trans` 1 แถว (37 คอลัมน์) — **ไม่มีบรรทัด** (`ic_trans_detail` ของ SSC = 0)
  `trans_type=2, trans_flag=37, status=0, doc_date, doc_time, cust_code, doc_ref_date, doc_no, doc_format_code='SSC', doc_ref='SO26100002', user_approve=<ผู้ใช้>, vat_type=1, user_request=null, cancel_type=1, expire_day, expire_date, vat_rate, total_value=0, credit_day, credit_date, discount_word='100', total_discount=100.00, send_day, send_date, total_before_vat=0, total_vat_value=0, remark, total_after_vat=0, total_except_vat=-100.00, total_amount=-100.00, remark_2..5, is_pos=0, creator_code, create_datetime`
  - ค่า `discount_word`/`total_discount`/`total_amount = -100` เป็นค่าที่โปรแกรมเขียนจริงในใบนี้ — ยังไม่ทราบว่ามาจากไหน (ใบสั่งขายต้นทางไม่มีส่วนลดท้ายบิล)
- หลัง commit: `logs` → งานสต็อกของสินค้าใน SO (ค้างจอง/ค้างส่ง, คิว `process`) → **doc flow** (16:10:04): `update ic_trans set last_status=1 where roworder=<SO>`, `ic_trans_detail`/`ap_ar_trans_detail` ของ 36 `last_status=1` → (16:10:05) ใบเสนอราคาต้นทาง **`used_status=0`** และ reset `last_status` ของ 30
- ผลใน DB: SO26100002 `last_status=1`; QT26090001 `used_status=0, doc_success=0` (กลับมาใช้ได้)

## B.1 ยืนยันจากรอบ 5.7: ยกเลิกใบสั่งขาย**รายสินค้า** (SSC26100002 ยกเลิกบรรทัด 2 ของ SO26100003, 12:29:19 วันที่ 2026-10-26)
ใบสั่งขาย SO26100003 (12:27:21): `ZZTEST-0001` 1 ชิ้น × 20 + `AH-0001` 1 กล่อง × 240 · หน้าจอเลือก "ประเภทการยกเลิก: ยกเลิกรายสินค้า" แล้วตารางแสดงเฉพาะบรรทัดที่ยกเลิก
- **Transaction (ต่างจาก type 1 ที่มีแต่หัว):** `ic_trans` → `ic_trans_detail` ต่อบรรทัดที่ยกเลิก → `ap_ar_trans_detail` → `COMMIT`
  - `ic_trans` (37 คอลัมน์ ชุดเดียวกับ B.0): **`cancel_type=2`**, `doc_ref='SO26100003'`, `doc_ref_date`, `user_approve=<ผู้ใช้>`, `vat_type=1`, **ยอดเท่ากับบรรทัดที่ยกเลิก** (`total_value=240, total_before_vat=224.30, total_vat_value=15.70, total_amount=240`)
  - `ic_trans_detail`: `trans_flag=37`, **`calc_flag=-1`**, `doc_ref_type=0`, **`ref_doc_no='SO26100003'`, `ref_row=1`** (line_number ของบรรทัดใน SO), `item_code`, `wh_code/shelf_code`, `unit_code`, `qty=1`, `price=240`, `sum_amount=240`, `line_number=0`
  - `ap_ar_trans_detail` (แท็บเอกสารอ้างอิง): `calc_flag=-1, trans_type=2, trans_flag=37, doc_no=<SSC>, billing_no=<SO>, billing_date, line_number=0`
- หลัง commit: ซ่อมค้างจอง/ค้างส่ง → คิว `process` → **doc flow: `SO26100003` `used_status=1` เท่านั้น** (`last_status=0`, `doc_success=0`) ⇒ ใบสั่งขายยังเปิดอยู่สำหรับบรรทัดที่เหลือ — ตรงกับกฎ "ยกเลิกบางรายการนับเป็นการอ้างอิง ไม่ใช่การยกเลิก"
- ตรวจ DB: `accrued_out_qty` (ค้างส่ง) `ZZTEST-0001` = 1 (บรรทัดที่เหลือ), `AH-0001` = 1 (กลับเท่าก่อนสร้าง SO — บรรทัดที่ยกเลิกไม่นับแล้ว) · `balance_qty` ไม่เปลี่ยน
