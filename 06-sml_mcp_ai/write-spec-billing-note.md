---
tags: [sml, sml_mcp_ai, write-spec, ar, billing-note]
status: verified-runtime รอบ 4 (BL26100001) + from-code (กฎสถานะ) + ข้อมูลจริง
source: smlerp SMLProcess/_docFlowThread.cs (~115, ~147, ~269, ~1556), SMLAPARControl/_ar_ap_trans.cs + DB kbgtest/samai/aoy (2026-10-21)
---
# สเปกเอกสาร: ใบวางบิลลูกหนี้ (trans_flag 235)

กลับไป [[00-Index]] · รับชำระ [[write-spec-receipt]] · บิลขาย [[write-spec-sale-invoice]] · ฝั่งเจ้าหนี้ (213) [[write-spec-ap-payment]]

> ยืนยันด้วย SQL จริงแล้วในรอบ 4 (§0) · กฎสถานะมาจากโค้ดและตรงกับที่เห็นจริง

## 1. โครงสร้าง (ข้อมูลจริง)
| | kbgtest | samai | aoy |
|---|---|---|---|
| หัว `ap_ar_trans` trans_flag 235 | 31,108 | 12,106 | 15 |
| `trans_type` | 2 ทุกใบ | 2 | 2 |
| `cb_trans` | **0** (ไม่มีการรับเงิน) | 0 | 0 |
| `ap_ar_trans_detail.bill_type` (= trans_flag ของเอกสารที่วางบิล) | 44 = 129,088 · 46 = 36 · 48 = 4,788 · 93 = 1,317 · 97 = 68 · 101 = 4,213 · 103 = 2,901 | 44, 46, 48, 93 | 44 = 13 · 48 = 2 |
- บรรทัดใช้ `billing_no` (เลขบิล), `bill_type`, `sum_debt_amount`, `balance_ref`, `sum_pay_money` (ยอดที่วางบิล) — รูปแบบเดียวกับใบรับชำระ
- ใบลดหนี้ (48, 97, 103) อยู่ในใบวางบิลได้ (หักยอด)
- **ใบวางบิลไม่หักยอดลูกหนี้** — สูตรยอดลูกหนี้นับเฉพาะ 239 ([[write-spec-sale-invoice]] §1.3, [[write-spec-receipt]] §1)

## 2. ใบรับชำระที่รับตามใบวางบิล
- **`ap_ar_trans_detail.doc_ref` ของใบรับชำระ = เลขใบวางบิล** (kbgtest 103,923 แถว; aoy 10 แถว) — `billing_no`/`bill_type` ยังชี้ไปที่บิลขายตัวจริง (ไม่ใช่ 235)
- `ap_ar_trans.doc_ref` ของใบรับชำระว่าง และไม่มีแถวที่ `bill_type = 235`
- RC26100003 (capture) ไม่ได้รับตามใบวางบิล จึง `doc_ref = null`

## 3. กฎสถานะ (doc flow)
**ของบิลขายที่ถูกวางบิล** (`_docFlowThread.cs` ~147): `ic_trans.used_status_2 = 1` เมื่อมีแถว `ap_ar_trans_detail` ของ **235 หรือ 239** (`last_status=0`) อ้าง `billing_no` — ⇒ วางบิลแล้วบิลขายจะ**ยกเลิกด้วย 45 ไม่ได้** ([[write-spec-cancel]] A.1) เหมือนรับชำระแล้ว
- เอกสารที่ doc flow ของ 235 ไล่ปรับ: 44, 46, 48 (`~269`)

**ของตัวใบวางบิล** (`~1556`, ตาราง `ap_ar_trans where trans_flag = 235`):
- `last_status = 1` เมื่อมีใบยกเลิก **236** ที่ `doc_ref` = ใบวางบิล
- `used_status = 1` เมื่อมีแถว `ap_ar_trans_detail` (ของเอกสารที่ `last_status=0`) ที่ **`doc_ref` = ใบวางบิล** (คือใบรับชำระที่รับตามใบวางบิล)
- `doc_success = 1` เมื่อ **Σ `sum_pay_money` ของบรรทัดใบวางบิล − Σ `sum_pay_money` ของบรรทัดใบรับชำระ 239 (`last_status=0`) ที่ `billing_no` + `bill_type` ตรงกับบรรทัดใบวางบิล = 0** — นับใบรับชำระทุกใบที่จ่ายบิลเหล่านั้น ไม่ว่าจะรับตามใบวางบิลนี้หรือไม่
- ข้อมูลจริง kbgtest (`used/success/last`): 1/1/0 = 19,162 · 0/0/0 = 11,581 · 1/0/0 = 281 · 0/0/1 = 41 · ยกเลิก 236 = 45 ใบ

## 4. สำหรับ sml_mcp_ai
- **อ่าน (เปิดได้):** "บิลที่วางแล้วแต่ยังไม่รับเงิน" = ใบวางบิลที่ `last_status=0 and doc_success=0` + บรรทัดของมัน; "บิลที่ยังไม่วาง" = บิลขายเชื่อที่ยอดค้าง ≠ 0 และไม่มีบรรทัด 235 อ้าง
- **เขียน:** ทำตาม §0 ได้ (ใบวางบิล + ใบรับชำระตามใบวางบิล ยืนยันแล้ว)

## 5. ยังไม่ทราบ
- ลำดับ SQL ของการยกเลิกใบวางบิล (236)
- ใบรับชำระที่รับบางบิลในใบวางบิล / ปนบิลที่ไม่ได้วาง
- ใบรับวางบิลฝั่งเจ้าหนี้ (213) ใช้กฎเดียวกันหรือไม่ (โค้ด ~1530 มีโครงสร้างคล้ายกัน)

## 0. ยืนยันจากรอบ 4 (2026-10-21)
### ใบวางบิล BL26100001 (16:13:19) — 1 transaction
1. `insert ap_ar_trans` (15 คอลัมน์): `trans_type=2, trans_flag=235, doc_date, doc_no, cust_code, doc_format_code='BL', due_date, credit_day, doc_ref, doc_ref_date, remark, sale_code, total_net_value=90.00, creator_code, create_datetime`
2. `insert ap_ar_trans_detail` ต่อบิล (15 คอลัมน์): `trans_type=2, trans_flag=235, doc_date, doc_no, billing_no=<บิล>, billing_date, ref_doc_no=<ic_trans.doc_ref ของบิล>, ref_doc_date, due_date, sum_debt_amount, balance_ref, sum_pay_money (= ยอดที่วาง), doc_ref=null, bill_type=44, line_number`
3. `delete from ap_ar_trans_detail where sum_debt_amount=0 and coalesce(remark,'')='' and (billing_no='' or billing_no is null)` → `update ic_trans set due_date=date(doc_date)+credit_day … where doc_no=<เลขใบวางบิล>` → `COMMIT`
- **ไม่มีการลบก่อน insert** (ต่างจากใบรับชำระ) และไม่มี `cb_trans`
- doc flow 16:13:25–26: บิล BF-INV26100032/33 `used_status_2=1`
### ใบรับชำระตามใบวางบิล RC26100004 (16:15:06) — ดู [[write-spec-receipt]] §6
- doc flow 16:15:45: **`update ap_ar_trans set used_status=1, doc_success=1 where roworder=<BL>`** (รับครบ 90) ตรงกับกฎ §3

## ยืนยันจากรอบ 7.6: ยกเลิกใบวางบิล (EDCC26100001 ยกเลิก BL26100001, 15:41:56 วันที่ 2026-10-26) — ใบแรกของ AOY
เมนู ลูกหนี้ › รายงาน/ยกเลิก › ยกเลิกใบวางบิล (ลูกหนี้) (เลขเมนู 7.12.1) · ก่อนยกเลิก BL26100001 ไม่มีใบรับชำระที่ใช้งาน (ใบเดิมถูกยกเลิกรอบ 5.10)
- เลขที่: `erp_doc_format code='EDCC'` → `select doc_no from ap_ar_trans where doc_date >= '2026-01-01' and doc_no like 'EDCC2610%' and trans_flag = 236 …` ⇒ `EDCC26100001` (หน้าจอแสดงเลขถัดไป `EDCC26100002` หลังบันทึก — เหมือนยกเลิกใบรับชำระ)
- **Transaction:** `insert ap_ar_trans (trans_type=2, trans_flag=236, doc_date, doc_no, cust_code, doc_format_code='EDCC', doc_ref=<ใบวางบิล>, doc_ref_date=null, remark, creator_code, create_datetime)` + cleanup → `COMMIT` — หัวอย่างเดียว ไม่มี detail
- doc flow (1.5 วินาที): **`BL26100001` `last_status=1`** + `ap_ar_trans_detail` ของใบวางบิล `last_status=1` → ไล่ต่อบิลในใบวางบิล: **`BF-INV26100032`, `BF-INV26100033` `used_status_2=0`** (วางบิล/รับชำระใหม่ได้)
- รูปแบบเดียวกับยกเลิกใบรับชำระ ([[write-spec-receipt]] §8) — ยกเลิกเอกสารใน `ap_ar_trans` = หัวอย่างเดียว + `doc_ref`
