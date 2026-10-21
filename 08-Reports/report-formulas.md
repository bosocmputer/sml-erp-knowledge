---
tags: [sml, reports, formulas]
status: รวมสูตรที่ยืนยันแล้ว + from-code (ระบุต่อหัวข้อ)
source: capture aoy-run1 (รายงานยอดขาย 09:04), capture aoy-run2/3 (ยอดลูกหนี้, บิลค้าง), smlerp SMLERPARInfo/_process.cs (`_createQuery`, `_arAgeing` ~982, `_arBalanceDoc`), SMLERPGL/_report/_tax/*, smljavaws2 SMLICProcess.java
---
# สูตรของรายงานหลัก

กลับไป [[00-Index]] · รายการรายงานทั้งหมด [[reports]] · รายงานในโค้ด [[code-reports]]

> ใช้หน้านี้เมื่อ sml_mcp_ai หรือ AI ต้อง**ตอบตัวเลขให้ตรงกับรายงานของ SML** — ทุกสูตรระบุว่ายืนยันแล้วหรือมาจากโค้ด

| รายงาน | สูตร / เงื่อนไข | สถานะ | ที่อยู่รายละเอียด |
|---|---|---|---|
| **ยอดขาย** (รายงานการขายสินค้าและบริการ `menu_so_report_invoice`) | เงื่อนไขหัวเอกสารจาก SQL จริง | ✅ verified | [[runtime-verified]] §5 |
| **ยอดลูกหนี้คงค้าง (รวม)** | Σ ขายเชื่อ/เพิ่มหนี้/อื่น − ลดหนี้ − รับชำระ 239 (`last_status=0`) | ✅ verified (SQL ตรวจวงเงิน) | [[write-spec-sale-invoice]] §1.3 |
| **ยอดลูกหนี้คงค้างรายบิล** | `total_amount − Σ(sum_pay_money + lost_profit_exchange_amount)` ของ 239 ที่ `billing_no` + `bill_type` ตรง | ✅ verified (หน้าจอรับชำระ) | [[write-spec-receipt]] §1 |
| **ยอดเจ้าหนี้คงค้างรายบิล** | ฟังก์ชันเดียวกัน กิ่งเจ้าหนี้ (12/14/16/81–91/260–264/315–317, หักด้วย 19) | 🔶 from-code (โค้ดร่วมกับฝั่งที่ verified) | [[write-spec-ap-payment]] §1 |
| **อายุลูกหนี้ / อายุเจ้าหนี้** | ยอดค้างรายบิลข้างบน แล้วแบ่งช่วงตาม `วันที่ถึง − due_date` (หรือ `doc_date` ถ้าเลือกนับจากวันที่เอกสาร `dateMode ≠ 0`) | 🔶 from-code | ด้านล่าง |
| **สินค้าคงเหลือ (จำนวน)** | `Σ qty × calc_flag × stand_value/divide_value` ของ flag สต็อก `last_status=0`, `item_type in (0,4,6)` + ข้อยกเว้น | ✅ verified (ตรง 57/60 ใน AOY) | [[stock-cost]] |
| **ค้างรับ / ค้างส่ง / ค้างจอง** | CTE `accin` / `accout` / `bookout` | ✅ verified (SQL จริง) | [[stock-cost]], [[write-spec-sale-order]] §3 |
| **ต้นทุน / กำไรขั้นต้น** | ยอดขาย − `ic_trans_detail.sum_of_cost` ของบรรทัดขาย (เขียนโดย worker) | ✅ ที่มาของ `sum_of_cost` verified · ⚠️ ถูกต้องเฉพาะเมื่อคิวต้นทุนรันครบ | [[stock-cost]] § ข้อควรรู้ |
| **ภาษีขาย / ภาษีซื้อ** | ตาม `vat_effective_year/period`, × `vat_calc`, ยกเลิก: ขาย = แถวยอด 0 / ซื้อ = ตัดทิ้ง | 🔶 from-code | [[tax-period]] §1–2 |
| **เช็คในมือ (ฝั่งลูกหนี้)** | `cb_chq_list where chq_type = 1 and status not in (2, 7, 8)` | 🔶 from-code | [[cash-bank]] §2 |
| **ใบวางบิลค้างรับ** | ใบวางบิล `last_status=0 and doc_success=0` | 🔶 from-code | [[write-spec-billing-note]] |

## อายุลูกหนี้ (`SMLERPARAPInfo._process._arAgeing`, ~982)
- ฐาน = ผลของ `_createQuery(mode, dateMode, …)` (ยอดค้างรายบิล) ณ วันที่สิ้นสุดที่เลือก
- `__dueDate = (dateMode == 0) ? due_date : doc_date`
- ช่วง (คอลัมน์ผลลัพธ์ `ap_ar_resource._term_0..5`):
  | คอลัมน์ | เงื่อนไข (`วันที่ถึง − __dueDate`) |
  |---|---|
  | `out_due` (ยังไม่ถึงกำหนด) | `< 0` |
  | `term_0` | `= 0` |
  | `term_1` … `term_4` | `between term_n_begin and term_n_end` (ผู้ใช้กำหนดช่วงเอง) |
  | `term_5` | `> term_4_end` |
  | `ar_balance` | ผลรวมทั้งหมด |
- มีการหักยอด "คืนเงินล่วงหน้า" (`ic_trans` ประเภทคืนเงินล่วงหน้า) ในส่วนรวม (~990) — ยังไม่ได้ไล่ละเอียด

## ข้อควรระวังเวลาสร้างรายงานเอง
- กรอง `last_status = 0` ทุกครั้ง (เอกสารยกเลิก = `last_status = 1`) — ยกเว้นรายงานภาษีขายที่ SML แสดงแถวยกเลิกเป็นยอด 0
- อย่าใช้ `is_cancel` เป็นตัวกรองการยกเลิกของบิลที่ยกเลิกด้วย 45 (ค่าเป็น 0) ([[write-spec-cancel]])
- `doc_date` บางร้านมีเอกสารลงวันที่ล่วงหน้า (cus_ms, kbgtest ถึง 2026-10-27) ([[tenants-overview]] §5)
- กำไรต้องระบุว่าคิวต้นทุนค้างหรือไม่ (`process` ของร้าน)

## ยังไม่ทราบ
- สูตรของรายงาน FastReport แต่ละตัว (รู้ตารางที่อ่านแล้วใน [[reports]] แต่สูตรอยู่ในแบบรายงาน `sml_fastreport`)
- การ์ดสินค้า (stock card) และมูลค่าสินค้าคงเหลือ ณ วันที่
- รายงานกำไรขาดทุนจาก GL / งบทดลอง
