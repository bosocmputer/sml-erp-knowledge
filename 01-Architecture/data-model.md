---
tags: [sml, data-model, verified]
source: smlerp code + AOY database (aggregate counts only)
status: verified-on-aoy
date: 2026-10-20
---
# เอกสารแต่ละประเภทเก็บที่ตารางไหน (ยืนยันกับข้อมูล AOY)

กลับไป [[00-Index]] · เครื่องยนต์เอกสาร [[document-engine]] · เลขเอกสาร [[trans_flag]]

## หลักการ
- **`trans_flag` เป็นภาษากลางของทุกตาราง** — ตารางลูก (`cb_trans`, `gl_journal`, `ap_ar_trans`) เก็บ trans_flag ของ **เอกสารต้นทาง** และเชื่อมกันด้วย `doc_no`
- เอกสารแต่ละกลุ่มมี "ตารางหัว" ของตัวเอง:

| กลุ่มเอกสาร | ตารางหัว / รายการ | trans_flag ที่พบใน AOY | หน้าจอหลัก |
|---|---|---|---|
| ซื้อ ขาย สต็อก (รวมบิล POS) | `ic_trans` / `ic_trans_detail` | 44 ขาย (649), 12 ซื้อ (43), 48 ลดหนี้, 45 ยกเลิกขาย, 54 ยกมา, 68 ปรับปรุงขาด, 70/72 โอน, 2/4 เสนอซื้อ, 6/8 สั่งซื้อ, 30/32 เสนอราคา, 36 สั่งขาย, 10/40/110 เงินล่วงหน้า/มัดจำ | `SMLInventoryControl._icTransControl` |
| รายได้อื่น / รายจ่ายอื่น | `ic_trans` (!) + `cb_trans` | 250 รายได้อื่น, 260 รายจ่ายอื่น | หน้าจอ cashbank |
| ลูกหนี้ / เจ้าหนี้ (วางบิล, รับชำระ, จ่ายชำระ) | `ap_ar_trans` / `ap_ar_trans_detail` | 239 รับชำระหนี้ (37), 235 ใบวางบิลลูกหนี้, 213 รับวางบิลเจ้าหนี้, 19 จ่ายชำระหนี้ | `SMLAPARControl._ar_ap_trans` |
| การรับ/จ่ายเงินของเอกสาร | `cb_trans` / `cb_trans_detail` (+ เช็ค `cb_chq_list`) | 44 (180 ใบขายที่มีการรับเงิน), 239, 12, 48, 250, 260, 19, 110, 40, 10 | ฝังใน `_icTransControl` และ `SMLERPControl._bank._bankControl` |
| เช็ค (ฝาก/ผ่าน) | `ic_trans` + `cb_chq_list` | 410 เช็ครับ_ฝาก, 411 เช็ครับ_ผ่าน, 451 เช็คจ่าย_ผ่าน | หน้าจอ cashbank |
| บัญชีแยกประเภท | `gl_journal` / `gl_journal_detail` | 44 (133), 260, 239, 12, 48, 72, 40, 10 — 176 จาก 188 ใบผูก `doc_no` กับ `ic_trans` | GL auto จากเอกสาร / `SMLERPGLControl._journalScreen` |
| ภาษีซื้อ/ขาย | `gl_journal_vat_buy` / `gl_journal_vat_sale` | — | สร้างพร้อมเอกสาร |

## ข้อเท็จจริงที่ยืนยันแล้วจากการรันจริง (2026-10-21)
- **ขายเชื่อ**ไม่สร้าง `cb_trans` แต่สร้าง `ap_ar_trans_detail` (calc_flag −1, billing_no, ref_doc_no) เป็นยอดตั้งลูกหนี้ ส่วนขายเงินสดสร้าง `cb_trans` ดู [[runtime-verified]]

## ข้อเท็จจริงที่ยืนยันแล้ว (AOY, 2026-10-20)
- **บิล POS = `ic_trans` flag 44 ที่ `is_pos = 1`** (132 จาก 649 ใบขาย) ส่วนขายหน้าจอปกติ `is_pos = 0`
- **การยกเลิกเป็นเอกสารแยก** (flag 45 = ยกเลิกขาย มี 16 ใบ) ขณะที่ `is_cancel` = 0 ทุกใบ
- **ไม่ใช่ทุกใบขายจะมี `cb_trans`** (180/649) — น่าจะเฉพาะที่มีการรับเงินทันที ส่วนขายเชื่อไปตั้งหนี้แล้วรับชำระด้วย 239
- **ไม่ใช่ทุกเอกสารจะมี GL** (gl_journal 188 รายการ) — ขึ้นกับตัวเลือก GL realtime และประเภทเอกสาร
- ร้าน AOY ไม่ใช้ระบบกะ (`sale_shift_id` ว่าง) แต่ใช้ล็อต (`ic_trans_detail_lot` 544 แถว)

## การเขียนข้อมูลของ control หลัก (จากโค้ด)
- `_icTransControl`: ดู [[document-engine]]
- `SMLAPARControl._ar_ap_trans` (~4,200 บรรทัด): ส่งชุดคำสั่งด้วย `_queryList`, ลบ/สร้าง `ap_ar_trans_detail`, GL ผ่าน `_processGLByTrans`, เรียก `_process_ap_ar_flow` (อัปเดตยอดค้างของเอกสารที่ถูกชำระ) และ `_process_stock_balance`, บันทึก `erp_print_logs`, `erp_cancel_logs`
- `SMLERPControl._bank._bankControl` (~4,300 บรรทัด): ฝังในหน้าจอเงินสด/ธนาคาร เขียน `cb_trans`, `cb_chq_list` (ทะเบียนเช็ค)
- `MyLib._manageMasterCodeFull`: หน้าจอข้อมูลหลักแบบทั่วไป ตั้งค่าใน `SMLERPGlobal/_selectMenu.cs` ด้วย `_dataTableName = _g.d.<table>._table` + `_addColumn(...)` → 1 เมนู = 1 ตาราง (เช่น `menu_setup_ic_brand` → `ic_brand`) ~74 เมนู

## Query ตรวจซ้ำ (read-only, สรุปผล)
```sql
select trans_flag, is_pos, count(*) from ic_trans group by 1,2 order by 3 desc;
select trans_flag, count(*) from ap_ar_trans group by 1 order by 2 desc;
select trans_flag, count(*) from cb_trans group by 1 order by 2 desc;
select trans_flag, count(*) from gl_journal group by 1 order by 2 desc;
```
