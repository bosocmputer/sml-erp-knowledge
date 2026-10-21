---
tags: [sml, stock, cost, core]
source: smljavaws2 SMLWebService/SMLICProcess.java, StockProcess/*, SMLWebService/_transDetailClass.java
status: from-code, formula verified-on-aoy
date: 2026-10-20
---
# ยอดคงเหลือและต้นทุนสินค้า (คำนวณที่ web service)

กลับไป [[00-Index]] · เรียกจาก [[document-engine]] หลังบันทึกเอกสาร · คอลัมน์ดู [[dictionary-index]]

## ใครเรียก
**ยืนยันจากการรันจริง (2026-10-21):** เอกสารที่บันทึกจะ `insert into process (process_name, wherein)` 1 แถวต่อสินค้า แล้ว web service poll ตาราง `process` ทุก ~10 วินาที หยิบงาน (`last_guid`, `last_process_time`) คำนวณล็อต/ต้นทุน แล้วลบแถวคิว ดู [[runtime-verified]] — คำอธิบายด้านล่างเป็นจากโค้ด

หลังบันทึกเอกสารสำเร็จ โปรแกรม Windows เรียก SOAP `_process_stock_balance(...)` / `_process_stock_cost(database, itemCode, processMode, dateBegin, dateEnd)` / `_process_stock_cost_finish(...)` ใน `SMLICProcess.java` (ปิดได้ด้วยตัวเลือก `disable_ic_cost_process` ดู [[company-options]]) และส่งผ่าน queue ได้ (`processstockrequest`, RabbitMQ/Redis/PubSub)

## ทิศทางสต็อก
- `ic_trans_detail.calc_flag`: **1 = รับเข้า (ApplyStock)**, ค่าอื่น (−1) = **จ่ายออก (Reduce)** (`_transDetailClass.StockCalcType()`)
- จำนวนหน่วยฐาน = `qty * (stand_value / divide_value)` (แปลงหน่วยนับ)

## สูตรยอดคงเหลือ `ic_inventory.balance_qty` (คัดจากโค้ด)
```sql
select item_code, sum((qty * calc_flag) * (stand_value/divide_value)) as qty
from ic_trans_detail
where trans_flag in (12,310,14,311,16,44,46,48,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73)
  and last_status = 0                 -- ไม่ถูกยกเลิก
  and item_type in (0,4,6)            -- เฉพาะสินค้าที่นับสต็อก
  and not (trans_flag in (14,16,311) and inquiry_type in (1,3))  -- เพิ่ม/ลดหนี้ซื้อแบบราคาอย่างเดียว ไม่กระทบสต็อก
  and not (trans_flag = 46 and inquiry_type <> 0)                -- เพิ่มหนี้ขาย (ไม่ใช่สินค้า) ไม่กระทบสต็อก
  and not (trans_flag = 48 and inquiry_type > 1)                 -- ลดหนี้ขายแบบราคา ไม่กระทบสต็อก
  and is_doc_copy = 0
group by item_code
```
**สำคัญสำหรับ tool ที่คำนวณสต็อกเอง (เช่น sml_mcp_ai):** ต้องใช้เงื่อนไขชุดนี้ ไม่งั้นยอดจะไม่ตรงกับโปรแกรม — หรืออ่าน `ic_inventory.balance_qty` ที่ web service คำนวณไว้แล้ว (ขึ้นกับว่ากระบวนการรันล่าสุดเมื่อไร)

**ยืนยันกับ AOY (2026-10-21):**
- `calc_flag` ตรงตามโค้ด: รับเข้า = 1 (12 ซื้อ, 48 รับคืน, 54 ยกมา, 70 โอนเข้า), จ่ายออก = −1 (44 ขาย, 46 เพิ่มหนี้, 68 ปรับปรุงขาด, 72 โอนออก); เอกสารที่ไม่กระทบสต็อก (เช่น 6 สั่งซื้อ) มี calc_flag แต่ถูกตัดด้วยรายการ trans_flag
- สูตรข้างบนให้ผล **ตรงกับ `ic_inventory.balance_qty` 57 จาก 60 สินค้า (95%)** — 3 ตัวที่ไม่ตรงเป็นสินค้า**ติดลบ**ที่เคลื่อนไหวล่าสุด ก.ย.–ต.ค. ค่าที่เก็บ (`balance_qty`) น่าจะยังไม่ได้อัปเดต → ถ้าต้องการตัวเลขล่าสุดให้คำนวณจากสูตร

## ยอดค้าง
- **ค้างรับ** `accrued_in_qty` = ใบสั่งซื้อ (6) − (ซื้อ 12, 310 + ยกเลิกสั่งซื้อ 7) อ้างอิงผ่าน `ref_doc_no` รายใบ ไม่ติดลบ
- **ค้างจอง** `book_out_qty` = ใบสั่งจอง (34) − (สั่งขาย + ขาย + ยกเลิกจอง 39)
- **ค้างส่ง** `accrued_out_qty` = จากใบสั่งขาย (36, 37) และสั่งจอง (34, 39) หักที่ส่ง/ขายแล้ว
- ตรงกับคอลัมน์ "ค้างจอง / ค้างส่ง / ค้างรับ" ในตารางสิทธิ์ของ sml_mcp_ai ดู [[mcp-project]]

## วิธีคิดต้นทุน — `ic_inventory.cost_type`
| cost_type | วิธี | คลาส |
|---|---|---|
| 0 | ถัวเฉลี่ย (Average) | `StockProcess.AverageCostStockCalculator` |
| 1 | Lot FIFO | `LotFIFOStockProcess` |
| 2 | Lot กำหนดเอง (LotSelector) | `LotManualStockProcess` |
| 3 | Lot ตามวันหมดอายุ (FEFO / LotExpire) | ใช้ตระกูล Lot |
| 4 | ต้นทุนมาตรฐาน (StandardCost) | `_standardCostClass` |

- คำนวณแยกคลัง (`SplitWarehouseCost`) หรือรวมทุกคลัง (`MixWarehouseCost`) ตามตัวเลือกบริษัท (`_costByWarehouse`)
- ถัวเฉลี่ย: รับเข้า → บวกจำนวน/มูลค่าเข้าคลัง ปรับทุนเฉลี่ย; จ่ายออก → ตัดด้วยทุนเฉลี่ย ณ ขณะนั้น; มี "ทุนแฝง" (amount with hidden cost) แยกอีกชุด (`average_cost_1`, `sum_of_cost_1`)
- ถ้าสต็อกไม่พอ จะจัดการตาม `IgnoreStockLack` (ยอมให้ติดลบหรือไม่)
- ผลลัพธ์เขียนกลับ: `ic_trans_detail.sum_of_cost` / `sum_of_cost_1` / `average_cost` (ต้นทุนต่อรายการ), `ic_inventory.average_cost`, `balance_qty`; ใช้ตาราง `process` เป็นคิว/สถานะการคำนวณ

## processMode ของ `_process_stock_cost(db, item, processMode, dateBegin, dateEnd)`
- **0** = คำนวณแล้วเขียนผลลง DB (หลังบันทึกเอกสาร) · **1** = คำนวณสดเพื่อทำรายงาน **ไม่เขียน DB** (เช่น รายงานเคลื่อนไหวสินค้า `SMLERPICReport._report_ic_stk_movement` เรียกด้วย 1 ตั้งแต่ 1998-1-1 ถึงวันสิ้นสุด) · **10 / 11** = คู่เดียวกันในเส้นทางที่มีล็อต · (comment ในโค้ดระบุ 2 = รายงานไม่มีหัว)
- ผล: รายงานเคลื่อนไหวสินค้าคำนวณต้นทุนใหม่ทุกครั้งที่เปิด ส่วน `sum_of_cost` ในเอกสารเป็นค่าที่บันทึกครั้งล่าสุด

## ข้อควรรู้เวลาวิเคราะห์กำไร
- กำไรขั้นต้น = ยอดขาย − `sum_of_cost` ของรายการขาย → ถูกต้องเมื่อกระบวนการต้นทุนรันครบแล้ว
- ถ้าร้านปิด `disable_ic_cost_process` ต้นทุนอาจไม่อัปเดตทันที
- README ของ web service: ถ้าปิดระบบคำนวณต้นทุน โปรแกรมจะอัปเดตต้นทุนเฉพาะเอกสารวันปัจจุบัน

## รายละเอียดแต่ละวิธี (จากโค้ด)

**ถัวเฉลี่ย (0)** — ดูด้านบน

**Lot FIFO (1)** — `StockProcess/LotFIFOStockProcess.java`
- รับเข้าแต่ละครั้ง → สร้างล็อตใหม่ (เลขล็อตรันอัตโนมัติ) ราคาทุน = ราคาของเอกสารรับ
- เอกสารรับที่อ้างอิงเอกสารเดิม (เช่น รับคืน/ลดหนี้) → ใช้ทุนจากรายการต้นทางที่อ้างถึง (`HasCostFromDocRef` → `FindRefDoc`) ถ้าหาไม่เจอใช้ทุนเฉลี่ยของคลัง
- จ่ายออก → `reduceLotFIFO` ตัดล็อตที่เก่าที่สุดก่อน; ใบเดียวอาจตัดหลายล็อต → สร้าง movement หลายแถว (เลขเอกสารในรายงานเติม `+` นำหน้าแถวถัดไป)
- ผลต่อล็อตเก็บที่ `ic_trans_detail_lot` (lot_number, expire_date, mfd_date, mfn_name) ผ่าน `ICStockLotDataDetailProcess`

**Lot กำหนดเอง (2)** — `StockProcess/LotManualStockProcess.java`
- ผู้ใช้เลือกล็อตเองในเอกสารจ่าย (`ic_trans_detail.lot_number_1`) → ตัดล็อตนั้นโดยตรง
- ตัวเลือก: `cn_actual_cost` (ลดหนี้ที่หาเอกสารอ้างอิงไม่เจอให้ใช้ทุนจริง), `lot_manual_by_year` (ล็อตแยกตามปี), ยอมให้ล็อตติดลบได้ตามค่า `IgnoreLotError`

**Lot ตามวันหมดอายุ / FEFO (3)** — `SMLWebService/ICStockCostProcess.java` (เส้นทางเดียวกับ FIFO แบบเดิม)
- **เลขล็อต = วันหมดอายุ** ของรายการรับเข้า (ยกเว้นโอนเข้า 70 ใช้เลขล็อตที่ระบุ `lot_number_1`)
- ก่อนตัดสต็อกเรียงรายการล็อตตามเลขล็อต (`Collections.sort` บน `_lotNumber`) → **ล็อตที่หมดอายุก่อนถูกตัดก่อน**
- FIFO (1) แบบเดิมใช้เลขล็อตรัน `00001, 00002 …` ตามลำดับรับเข้า; รับคืนจากขาย (48) ที่อ้างอิงบิลใช้ทุนจากบิลเดิม

**ต้นทุนมาตรฐาน (4)** — อ่าน `ic_standard_cost (ic_code, date_start, cost1)` เรียงวันที่ใหม่สุดก่อน → ใช้ต้นทุนมาตรฐานที่มีผล ณ วันที่ของเอกสาร

**ร้านยา / FEFO ในการขาย:** เหมาะกับ product แจ้งเตือนยาใกล้หมดอายุ — ข้อมูลล็อต + วันหมดอายุอยู่ที่ `ic_trans_detail_lot` (AOY มี 544 แถว)

## ยังไม่ได้ไล่
