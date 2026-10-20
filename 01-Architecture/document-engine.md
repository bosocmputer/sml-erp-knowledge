---
tags: [sml, document, ic_trans, core]
source: smlerp/SMLInventoryControl/_icTransControl.cs, smljavaws2 Routine._queryList
status: from-code
date: 2026-10-20
---
# เครื่องยนต์เอกสาร: `SMLInventoryControl._icTransControl`

กลับไป [[00-Index]] · ภาพรวม [[architecture]] · เมนูที่ใช้ [[menu-map]] · เลขเอกสาร [[trans_flag]]

## มันคืออะไร
- UserControl ตัวเดียว (~18,500 บรรทัด) ที่เป็น **หน้าจอเอกสารเกือบทุกประเภท**: ขาย, ซื้อ, สั่งขาย/สั่งซื้อ, เสนอราคา, รับคืน/ลดหนี้, เพิ่มหนี้, เบิก/รับคืน/โอน/ปรับปรุงสต็อก, ยกมา, POS ฝั่งหลังร้าน ฯลฯ
- ประเภทเอกสารกำหนดด้วย property `_transControlType` (`_g.g._transControlTypeEnum`) → แปลงเป็นเลข `trans_flag` ด้วย `_g.g._transFlagGlobal._transFlag()`
- เข้าถึงได้ 2 แบบ (ดู [[screen-classes]]):
  - หน้าจอเฉพาะโมดูลที่ฝัง `_icTransControl` ไว้ใน Designer และตั้ง `_transControlType` เช่น `SMLERPSO._soInvoice` (ขาย 44), `_soQuotation`, `_soSaleorder` — ~138 เมนู
  - `SMLInventoryControl._clone_icTrans(transType, menuName)` สร้าง control ให้ตามประเภทที่ส่งเข้า — ~104 เมนู (โมดูลสินค้า/คลังส่วนใหญ่)
- ตัวกรองเพิ่ม: เช่นเมนู `menu_so_invoice` ส่ง `is_pos=0` (ขายปกติ) ส่วน `pos_invoice_list_pos` ใช้คลาสเดียวกันแต่ `is_pos=1` แบบอ่านอย่างเดียว → **บิล POS ก็คือ ic_trans flag 44 ที่ `is_pos=1`**

## ลำดับการบันทึก `_saveData(saveACopy)` (บรรทัด ~13063–17431)

1. **ตรวจข้อมูล** (`#region` ตามลำดับ): สถานะลูกค้า (OEM SINGHA) → ประเภทเอกสาร → ช่องบังคับ → สาขา → แผนก → ใบกำกับภาษี → สิทธิ์ → งวดบัญชี (ปิดงวดแล้วห้ามบันทึก) → Lot กำหนดเอง → ยอดรวม → Serial number → วันหมดอายุ (+ตัวเลือกบริษัท) → เกินกำหนดชำระ → การเฉลี่ยโครงการ/จัดสรร → คลังและที่เก็บ → หัก ณ ที่จ่าย → ขายต่ำกว่าทุน → ยอดห้ามติดลบ (เฉพาะเพิ่มใหม่) → **วงเงินเครดิต** (อาจสร้างคำขออนุมัติเครดิต `erp_credit_request`) → เงินมัดจำห้ามเกินราคาขาย
2. **ปรับข้อมูลก่อนบันทึก** และ **รันเลขที่เอกสาร** (ขายสินค้าและบริการ)
3. **สร้างชุดคำสั่ง SQL ทั้งหมดเป็นข้อความเดียว** (`__queryStr`) — ไม่ได้ยิงทีละคำสั่ง:
   - หัวเอกสาร `ic_trans` (insert / update / delete-แล้ว-insert เมื่อแก้ไข)
   - รายการ `ic_trans_detail`, `ic_trans_serial_number`, `ic_trans_shipment`
   - การกระจาย: `ic_trans_detail_department`, `_project`, `_jobs`, `_allocate`, `_site`
   - การรับ/จ่ายเงินในเอกสาร: `cb_trans`, `cb_trans_detail` (ล้าง `cb_trans_detail_draft`)
   - ลูกหนี้/เจ้าหนี้: `ap_ar_trans_detail`
   - ภาษี: `gl_journal_vat_sale` / `gl_journal_vat_buy`
   - เคลียร์ร่าง/คำขอ: `ic_trans_draft`, `ic_trans_detail_draft`, `erp_request_order`, `order_item`/`order_cart` (e-order), คูปอง `coupon_list`, log อนุมัติเครดิต `erp_credit_approved_logs`
4. **GL Auto** (`#region GL Auto`): สร้างรายการบัญชีจากเอกสาร (ถ้าตั้งค่าไว้ จะเตือน/ให้แก้ผ่านฟอร์ม GL ก่อน)
5. **ส่งทั้งหมดในครั้งเดียว** `_myFrameWork._queryList(databaseName, __queryStr)` → web service `Routine._queryList` เปิด connection, `setAutoCommit(false)`, รันทุกคำสั่ง, `commit` (ผิดพลาด → `rollback`) → **ทั้งเอกสารบันทึกแบบ atomic ใน transaction เดียว**
6. **หลังบันทึกสำเร็จ**
   - ถ้า `_companyProfile._gl_process_realtime` = true และไม่ได้ทำ GL มือ → `_processGLByTrans(...)` แล้ว `_saveToDatabase` ลง `gl_journal` / `gl_journal_detail`
   - คำนวณต้นทุน/สต็อก (เว้นแต่ปิดด้วย `_companyProfile._disable_ic_cost_process`): ฟอร์ม `_utils._waitProcessFrom` → `SMLProcess._docFlow._processAll(transType, items, docNos)` (อัปเดตสถานะเอกสารต้นทาง/ยอดค้าง ตามสายเอกสาร) + `_smlFrameWork._process_stock_cost(...)` (เรียก web service ไปคำนวณต้นทุนสินค้าที่เกี่ยวข้อง) + `_process_stock_cost_finish`
   - โค้ดเก่าที่คำนวณยอดคงเหลือฝั่ง client ถูก comment ไว้ → ย้ายไปทำที่ web service แล้ว
7. `_saveLog(mode)` บันทึก log การทำรายการ

## ผลต่อการทำ product
- เอกสาร 1 ใบ = หลายตารางที่ต้องสอดคล้องกัน + ขั้นหลังบันทึก (GL, ต้นทุน, สถานะเอกสารต้นทาง) ที่รันฝั่ง client → **การเขียนเอกสารจากภายนอกด้วย SQL ตรงจะได้ข้อมูลไม่ครบ** ต้องให้ SML สร้าง/อนุมัติเอง (เอกสารก่อนอนุมัติ) — ดู [[product-ideas]]
- การอ่านข้อมูล: ยอดสต็อก/ต้นทุนที่ถูกต้องขึ้นกับว่ากระบวนการคำนวณต้นทุนรันแล้วหรือยัง

## ยังไม่ได้ไล่
- รายละเอียดสูตรใน `SMLProcess._docFlow._processAll` และ `ICStockCostProcess` (web service)
- การลบ/ยกเลิกเอกสาร (`_glDeleteQuery`, หน้าจอ `_cancelControl`)
- ส่วน POS หน้าร้าน (`SMLPOSClient`) ซึ่งเป็นหน้าจอแยก
