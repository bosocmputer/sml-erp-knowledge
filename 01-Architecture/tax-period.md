---
tags: [sml, tax, vat, period, lock]
status: from-code + ข้อมูลจริง (2026-10-21)
source: smlerp SMLERPGL/_report/_tax/_reportVatSale.cs (~409–448), _reportVatBuy.cs (~269–313), SMLERPGlobal/_global.cs (`_checkPeriod` ~3934, `_accountPeriodGet`, `_checkOpenPeriod` ~3983), SMLInventoryControl/_icTransControl.cs, _icTransScreenTopControl.cs (~295), SMLAPARControl/_ar_ap_trans.cs (~2113), SMLERPGlobal/_smlOption.cs (~127) + DB aoy/kbgtest/samai/wawacrm
---
# รายงานภาษี และ การปิดงวด / ล็อกวันที่

กลับไป [[00-Index]] · ภาษีตอนออกเอกสาร [[write-spec-sale-invoice]] §2.5, [[write-spec-purchase]] §1.3 · ยกเลิก [[write-spec-cancel]] · GL [[pricing-vat-gl]]

## 1. รายงานภาษีขาย (`_reportVatSale`)
- เลือกจาก `gl_journal_vat_sale` ด้วย **`vat_effective_year = <ปี พ.ศ.> and vat_effective_period = <เดือน>`** (ไม่ใช่ `doc_date`) และ **`vat_type = 0`**
- **เอกสารที่ถูกยกเลิกยังแสดงแถว แต่ฐานภาษีและภาษี = 0**: `case when <last_status ของเอกสารต้นทาง> = 0 then base_caltax_amount * vat_calc else 0 end` (เหมือนกันกับ `amount`)
  - `last_status` อ่านจาก `ic_trans` (หรือ `as_trans`) ตาม `doc_date + doc_no + trans_flag`; ถ้า trans_flag เป็น 239/19 อ่านจาก `ap_ar_trans`; trans_flag 1999 (JV) ถือว่า 0
  - ⇒ บิลที่ยกเลิกด้วย 45 (`last_status=1`) แสดงเป็นแถวยอด 0 — ตรงกับที่แถว `gl_journal_vat_sale` ของบิลยังอยู่หลังยกเลิก ([[write-spec-cancel]] A.4)
- **คูณด้วย `vat_calc`**: ใบลดหนี้ที่ `vat_calc = −1` จึงเป็นยอดติดลบในรายงาน ([[write-spec-credit-note]])
- หมายเหตุ: ใช้ `ic_trans.remark` หรือ `doc_reason`; มี `is_doc_copy` (ใบกำกับสำเนา); กรองสาขา/รูปแบบเอกสารได้

## 2. รายงานภาษีซื้อ (`_reportVatBuy`)
- เลือกจาก `gl_journal_vat_buy` ด้วยปี/เดือนมีผล เช่นกัน และยอด `vat_base_amount * vat_calc`, `vat_amount * vat_calc`
- **ตัดแถวของเอกสารที่ยกเลิกออก** (`… last_status … = 0` อยู่ใน WHERE) — **ต่างจากภาษีขาย**ที่ยังแสดงแถวยอด 0
- ประเภทรายงาน `report_vat_type = 2` = **ภาษีซื้อไม่ถึงกำหนดชำระ** → `vat_type = 1`; อื่น ๆ → `vat_type = 0`
- ⇒ ความหมาย `gl_journal_vat_*.vat_type`: **0 = ภาษีปกติ (ถึงกำหนด), 1 = ภาษียังไม่ถึงกำหนด** (ตอบคำถามค้างใน [[write-spec-sale-invoice]] §5: บิลขายเขียน `vat_type = 0` ในตารางภาษีแม้หัวบิล `vat_type = 1` ซึ่งเป็นคนละความหมาย — หัวบิลคือ "รวมใน/แยกนอก")

## 3. งวดบัญชี (`erp_account_period`)
- คอลัมน์ที่โปรแกรมอ่าน: `date_start, date_end, period_number, period_year, status` (`_accountPeriodGet`); โปรแกรมเติม `period_year = ปี ค.ศ. + 543` ถ้าว่าง (เห็นใน capture ทุกครั้งที่เปิดหน้าจอเอกสาร)
- **`_checkOpenPeriod(วันที่)`**: หางวดที่วันที่อยู่ใน `[date_start 00:00:00, date_end 23:59:59]` → ผ่านเมื่อ **`status = 0`**; ถ้างวดปิด (`status ≠ 0`) **หรือไม่พบงวดเลย** → `false` + คำเตือน "วันที่ปัจจุบัน หรือที่เอกสารที่กำหนด ได้ถูกปิดงวด…"
- ไม่มีงวดเลย → `_checkPeriod()` เตือน "ยังไม่ได้กำหนดงวดบัญชี"
- **จุดที่บังคับจริง** (เฉพาะ edition SMLAccount/AccountPOS/AccountPro/**AccountPOSPro**/CM):
  | หน้าจอ | บันทึกใหม่/แก้ | ยกเลิก | ลบ |
  |---|---|---|---|
  | ลูกหนี้/เจ้าหนี้ `_ar_ap_trans` (รับชำระ, จ่ายชำระ, วางบิล …) | **ห้าม** (`_is_save_data = _checkOpenPeriod(doc_date)` ~2113) | ห้าม (~1734) และห้ามคืนสถานะยกเลิก (~1826) | ห้าม (`_dataList__deleteData` ~3255) |
  | เอกสารสินค้า `_icTransControl` (ขาย, ซื้อ, สั่งขาย, สต็อก …) | **ไม่พบการตรวจตอนบันทึก** (เตือนตอนเปิดหน้าจอ ~1503 เท่านั้น) | ห้าม (~8642) และห้ามคืนสถานะยกเลิก (~8730) | ห้าม (`_dataList__deleteData` ~10981, ~11068) |
  | มัดจำ `_po_so_deposit_control` | เตือนตอนเปิดแก้ไข (`_checkEditData` ~480) | | ห้าม (`_dataList__deleteData` ~1059, ~1067) |
- ข้อมูลจริง: aoy 12 งวด (2026) เปิดทั้งหมด · kbgtest 36 งวด (2025–2027) ปิด 5 · samai 121 งวด (2016–2028) ปิด 79

## 4. ล็อกวันที่ / เลขที่เอกสาร
- **`erp_option.disable_edit_doc_no_doc_date`** (ทั้งร้าน) หรือ **`erp_user.disable_edit_doc_no_doc_date_user`** (รายผู้ใช้) = 1 → หน้าจอตั้ง `doc_date = วันทำงาน`, `doc_time = เวลาปัจจุบัน` แล้ว**ปิดช่อง** วันที่/เวลา/เลขที่ (`_icTransScreenTopControl.cs` ~295; หน้าจอลูกหนี้/เจ้าหนี้ ~3481, มัดจำ ~56)
  - ข้อมูลจริง: ระดับร้านเปิดเฉพาะ wawacrm; ระดับผู้ใช้ aoy 1/5, kbgtest 248/380, samai 10/42, wawacrm 9/60
- **`erp_option.lock_date_back`**: มีแค่นิยามชื่อคอลัมน์ (`SMLERPGlobal/_data.cs` ~1366) **ไม่พบโค้ดที่ใช้** ใน smlerp และ smljavaws2 ⇒ ตัวเลือกนี้ไม่มีผล (ทุก tenant = 0 อยู่แล้ว [[tenants-overview]])
- `erp_option.lock_sale_day_interval`: ไม่พบการใช้นอกการโหลดค่า

## 5. สำหรับ sml_mcp_ai
- **ต้องตรวจงวดเองก่อนเขียนทุกเอกสาร** — โปรแกรมไม่ตรวจตอนบันทึกเอกสารสินค้า แต่ตรวจที่หน้าจอลูกหนี้/เจ้าหนี้; API ควรใช้กฎที่เข้มกว่า: ห้ามเขียนถ้า `doc_date` ไม่อยู่ในงวดที่ `status = 0`
- ถ้าผู้ใช้ที่ผูกกับ API มี `disable_edit_doc_no_doc_date_user = 1` หรือร้านเปิด `disable_edit_doc_no_doc_date` → บังคับ `doc_date = วันนี้` (ห้ามลงวันที่ย้อน/ล่วงหน้า)
- รายงานภาษีของ API: ภาษีขายแสดงแถวยกเลิกเป็น 0, ภาษีซื้อตัดทิ้ง, คูณ `vat_calc`, เลือกตาม `vat_effective_*` — ทำให้ตรงกับรายงาน SML

## 6. ยังไม่ทราบ
- หน้าจอปิดงวด (`SMLERPConfig/_accountPeriod`) ทำอะไรเพิ่มนอกจากตั้ง `status`
- ค่า `status` อื่นนอกจาก 0/1
- `vat_effective_period/year` ของบิลที่วันที่ใบกำกับต่างจากวันที่เอกสาร
