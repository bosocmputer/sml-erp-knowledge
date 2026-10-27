---
tags: [sml, sml_mcp_ai, write-spec, inventory, verified-runtime]
status: verified-runtime รอบ 10.1 (โอนสินค้า), 10.2 (ปรับเพิ่ม), 10.3 (ปรับลด) · รอบ 10.4–10.6 รอทดสอบ
source: capture aoy-run10-1 (2026-10-27 15:46) + DB aoy
---
# สเปกการบันทึก: เอกสารสินค้า/คลัง (โอน, ปรับปรุง, เบิก, ตรวจนับ)

กลับไป [[00-Index]] · สต็อก/ต้นทุน [[stock-cost]] · เมนู [[module-inventory]] · ยังไม่ได้ทดสอบ [[00-Unverified]]

## 1. โอนสินค้า (72 + 70) — ยืนยันรอบ 10.1 (TF26100002, 15:46:16 วันที่ 2026-10-27)
หน้าจอ: 2.18 โอนสินค้า/วัตถุดิบ (`menu_ic_transfer_wh_out`) · AH-0011 2 แท่ง AB-1/001 → AB-2/002
- **เอกสารเดียว เลขเดียว แต่ 2 หัว 2 ชุดบรรทัด** (transaction เดียว):
  1. `insert ic_trans (trans_type=3, trans_flag=72, status=0, doc_date, doc_time, doc_no, doc_format_code='TF', doc_ref_date, doc_ref, sale_code, wh_from, location_from, wh_to, location_to, remark, is_pos=0, remark_2..5, creator_code, create_datetime)` — โอนออก
  2. `insert ic_trans (… trans_flag=70 …)` — โอนเข้า หัวเหมือนกันทุกช่อง
  3. `insert ic_trans_detail` flag **72**: `calc_flag=-1`, **`wh_code/shelf_code` = ต้นทาง** (AB-1/001), **`wh_code_2/shelf_code_2` = ปลายทาง**, `item_code, item_name, unit_code, qty, stand_value, divide_value`, `ref_row=-1`, `ref_guid`
  4. `insert ic_trans_detail` flag **70**: `calc_flag=1`, `wh_code/shelf_code` = **ปลายทาง**, `wh_code_2/shelf_code_2` = ต้นทาง (สลับกับข้อ 3), `ref_guid` เดียวกัน
  5. `logs` (`menu_name='menu_ic_transfer_wh_out'`, `screen_code=72`, `function_code=1`, `doc_qty=2`)
- ไม่มีราคา/มูลค่าตอนบันทึก (`price`, `sum_amount` ไม่ถูกส่ง) · `wh_from`/`wh_to` ที่หัวเป็น null เมื่อเลือกคลังที่บรรทัด
- ข้อสังเกต: `doc_time` ของบรรทัด 70 เป็น 15:46 ขณะที่หัวและบรรทัด 72 เป็น 15:45 (เวลาปัจจุบันตอนสร้างแถว)
- หลัง commit: reset `last_status` ทั้ง 70/72 → คำนวณต้นทุน: **ทั้งสองบรรทัดได้ `sum_of_cost=242.98`, `average_cost=121.49`** (โอนพาต้นทุนเฉลี่ยไปด้วย) → ตรวจ `accrued_in/book_out/accrued_out` → คิว `process` 'IC' → **`update ic_trans set total_amount = <มูลค่าต้นทุน>`** ทั้ง 70 และ 72 (ตรวจ DB: 242.98)
- ผลตรวจ DB: AB-1/001 13 → **11**, AB-2/002 0 → **2**, `ic_inventory.balance_qty` รวมยังเป็น 13
- **สำหรับ sml_mcp_ai:** เขียน 2 หัว + 2 บรรทัดต่อสินค้า (คลังสลับกันใน `wh_code`/`wh_code_2`), `calc_flag` −1/+1, ใส่คิว `process` 'IC'; `total_amount` ปล่อยให้โปรแกรมคำนวณจากต้นทุน
- ยังไม่ทราบ: ตัวเลือก `transfer_stock_control` (ห้ามโอนติดลบ), โอนหลายรายการ, ยกเลิก (73/71 — รอบ 10.6)

## 2. ปรับปรุงสต็อก (เพิ่ม) 66 — ยืนยันรอบ 10.2 (IA26100002, 15:51:21 วันที่ 2026-10-27)
หน้าจอ: 2.20 ปรับปรุงสต็อกสินค้า/วัตถุดิบ (เพิ่ม) (`menu_ic_stk_adjust`) · AH-0011 +1 แท่ง AB-1/001
- เปิดหน้าจอ: ล้างบรรทัดกำพร้า `delete from ic_trans_detail where trans_flag=66 and not exists (หัว)`
- เลือกสินค้า: อ่าน `ic_inventory.average_cost` (+ `stand_value/divide_value` ของหน่วยต้นทุน) → **ราคาที่เติมให้ = ต้นทุนเฉลี่ยปัจจุบัน** (121.49) · คลัง/ชั้นเก็บเริ่มต้น = **ชั้นเก็บแรกเมื่อเรียงตาม `whcode`** (`select whcode, code from ic_shelf order by whcode limit 1`)
- transaction: `insert ic_trans (trans_type=3, trans_flag=66, status=0, doc_format_code='IA', inquiry_type=0, wh_from, location_from, remark, is_pos=0, …)` → `insert ic_trans_detail` (`calc_flag=1`, `wh_code, shelf_code, unit_code, qty, price=121.49, sum_amount=121.49, price_exclude_vat, sum_amount_exclude_vat`, `ref_row=-1`, `stand_value/divide_value`) → `logs` (`menu_ic_stk_adjust`, `screen_code=66`)
- หลัง commit: คำนวณต้นทุน (บรรทัดได้ `sum_of_cost=121.49`, `average_cost=121.49` — ต้นทุนเฉลี่ยไม่เปลี่ยนเพราะใช้ราคาเท่าเดิม) → reset `last_status` → ตรวจค้างรับ/จอง/ส่ง → คิว `process` 'IC' → `update ic_trans set total_amount` (= 121.49)
- ผลตรวจ DB: AB-1 11 → **12**, รวม 13 → **14**
- **สำหรับ sml_mcp_ai:** ราคาปรับเพิ่มมีผลต่อต้นทุนเฉลี่ย — ถ้าไม่ระบุ ให้ใช้ `ic_inventory.average_cost` แบบโปรแกรม; ราคาที่ต่างจากต้นทุนเฉลี่ยจะเปลี่ยนต้นทุนของสินค้า (ยังไม่ได้ทดสอบ)

## 3. ปรับปรุงสต็อก (ลด) 68 — ยืนยันรอบ 10.3 (IS26100001, 15:55:59 วันที่ 2026-10-27)
หน้าจอ: 2.21 ปรับปรุงสต็อกสินค้า/วัตถุดิบ (ลด) (`menu_ic_stk_adjust_subtract`) · AH-0011 −1 แท่ง AB-1/001
- หน้าจอ**ไม่แสดงต้นทุน** (ผู้ใช้ปล่อยว่าง) — เปิดหน้าจอยังล้างบรรทัดกำพร้าของ flag **66** (ไม่ใช่ 68)
- transaction: `insert ic_trans (trans_type=3, trans_flag=68, status=0, doc_format_code='IS', wh_from, location_from, remark, is_pos=0, …)` — **ไม่มี `inquiry_type` ที่หัว** (ต่างจาก 66) → `insert ic_trans_detail` (`calc_flag=-1`, `wh_code, shelf_code, unit_code, qty=1`, **`price=0, sum_amount=0`**, `ref_row=-1`) → `logs` (`menu_ic_stk_adjust_subtract`, `screen_code=68`)
- หลัง commit (~14 วินาทีต่อมา): คำนวณต้นทุนเติมให้บรรทัด `price = sum_amount = sum_of_cost = 121.49`, `average_cost=121.49` → ซ่อม `cb_chq_list` (ทำทุกครั้ง ไม่เกี่ยวกับเอกสารนี้) → คิว `process` 'IC' → `update ic_trans set total_amount` (= 121.49)
- ผลตรวจ DB: AB-1 12 → **11**, รวม 14 → **13**, ต้นทุนเฉลี่ยคง 121.49
- **สำหรับ sml_mcp_ai:** ส่ง `price=0, sum_amount=0` ได้ โปรแกรมเติมต้นทุนเองตอนคำนวณต้นทุน (เหมือนโอน) — ถ้าคิว `process` ค้าง มูลค่าจะยังเป็น 0
