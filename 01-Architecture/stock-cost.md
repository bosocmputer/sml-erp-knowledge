---
tags: [sml, stock, cost, core]
source: smljavaws2 SMLWebService/SMLICProcess.java, StockProcess/*, SMLWebService/_transDetailClass.java
status: from-code
date: 2026-10-20
---
# ยอดคงเหลือและต้นทุนสินค้า (คำนวณที่ web service)

กลับไป [[00-Index]] · เรียกจาก [[document-engine]] หลังบันทึกเอกสาร · คอลัมน์ดู [[dictionary-index]]

## ใครเรียก
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

## ข้อควรรู้เวลาวิเคราะห์กำไร
- กำไรขั้นต้น = ยอดขาย − `sum_of_cost` ของรายการขาย → ถูกต้องเมื่อกระบวนการต้นทุนรันครบแล้ว
- ถ้าร้านปิด `disable_ic_cost_process` ต้นทุนอาจไม่อัปเดตทันที
- README ของ web service: ถ้าปิดระบบคำนวณต้นทุน โปรแกรมจะอัปเดตต้นทุนเฉพาะเอกสารวันปัจจุบัน

## ยังไม่ได้ไล่
- สูตร Lot FIFO/FEFO ทีละขั้น และ Standard cost
- เงื่อนไข `processMode` (0, 10 …) และการคำนวณย้อนหลังตามช่วงวันที่
