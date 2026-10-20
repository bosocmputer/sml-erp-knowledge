---
tags: [sml, dictionary, e-tax, generated]
module: E-Tax
---
# พจนานุกรม: E-Tax — e-Tax

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#e_tax_transaction]] | E-Tax Transaction  | 4 |

## e_tax_transaction

**E-Tax Transaction**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | ประเภทรายการ |  | smallint | ✓ |
| `doc_no` | เลขที่เอกสาร |  | varchar(55) | ✓ |
| `transaction_id` | Transaction ID |  | varchar(255) |  |
| `send_date_time` | วันที่ส่ง |  | datetime |  |

index: `e_tax_transaction_trans_flag_doc_no_pk`(trans_flag,doc_no)

