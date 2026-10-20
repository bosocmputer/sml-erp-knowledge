---
tags: [sml, dictionary, form, generated]
module: Form
---
# พจนานุกรม: Form — ฟอร์มพิมพ์

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#form_print_detail_temp]] | บันทึกการพิมพ์รายการ / Form Report Detail | 6 |
| [[#resource_form_purchase_order]] | ฟอร์มใบสั่งซื้อ / Purchase Order Form | 26 |
| [[#resource_form_quotation]] | ฟอร์มใบเสนอราคา / Quotation Form | 28 |
| [[#resource_form_sale_order]] | ฟอร์มใบสั่งขาย / Sale Order Form | 3 |

## form_print_detail_temp

**บันทึกการพิมพ์รายการ** — Form Report Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_flag` | รายวันระบบ | Transection Flag | smallint | ✓ |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) | ✓ |
| `doc_date` | วันที่เอกสาร | Document Date | smalldatetime | ✓ |
| `print_date` | วันที่พิมพ์ | Print Form Date | smalldatetime | ✓ |
| `print_no` | จำนวนครั้งที่พิมพ์ | Print No | int | ✓ |
| `user_code` | ผู้จัดพิมพ์ | User Code | varchar(25) | ✓ |

## resource_form_purchase_order

**ฟอร์มใบสั่งซื้อ** — Purchase Order Form

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `report_po_title` | ใบสั่งซื้อ *(resource only)* | Purchase Order | char |  |
| `report_po_pages` | หน้าที่ *(resource only)* | Pages | char |  |
| `report_po_copy_no` | พิมพ์ซ้ำครั้งที่ *(resource only)* | Copy No | char |  |
| `report_po_ap_name` | ชื่อเจ้าหนี้ *(resource only)* | Ap Name | char |  |
| `report_po_address` | ที่อยู่ *(resource only)* | Address | char |  |
| `report_po_tel` | โทรศัพท์ *(resource only)* | Tel | char |  |
| `report_po_fax` | โทรสาร *(resource only)* | Fax | char |  |
| `report_po_doc_no` | เลขที่เอกสาร/No *(resource only)* | Document No | char |  |
| `report_po_doc_date` | วันที่/Date *(resource only)* | Document Date | char |  |
| `report_po_expire_date` | วันครบกำหนด/Duedate *(resource only)* | Expire Date | char |  |
| `report_po_credit_day` | เครดิต/Credit Day *(resource only)* | Credit Day | char |  |
| `report_po_code` | รหัสสินค้า *(resource only)* | Code | char |  |
| `report_po_name` | รายการสินค้า *(resource only)* | Name | char |  |
| `report_po_unit` | หน่วย *(resource only)* | Unit | char |  |
| `report_po_qty` | จำนวน *(resource only)* | Qty | char |  |
| `report_po_price` | ราคาซื้อ *(resource only)* | Price | char |  |
| `report_po_discount` | ส่วนลด *(resource only)* | Discount | char |  |
| `report_po_amount` | จำนวนเงิน *(resource only)* | Amount | char |  |
| `report_po_remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `report_po_money_title` | ยอดเงินตัวหนังสือ *(resource only)* | ยอดเงินตัวหนังสือ | char |  |
| `report_po_total_amount` | รวมจำนวนเงิน *(resource only)* | Total Amount | char |  |
| `report_po_total_value` | ราคาสินค้า/บริการ *(resource only)* | Total Value | char |  |
| `report_po_total_vat_rate` | ภาษีมูลค่าเพิ่ม *(resource only)* | Total Vat Rate | char |  |
| `report_po_total_net_value` | จำนวนเงินรวมทั้งสิ้น *(resource only)* | Total Net Value | char |  |
| `report_po_user_approve` | ผู้สั่งซื้อ *(resource only)* | User Approve | char |  |
| `report_po_approve` | ผู้อนุมัติ *(resource only)* | Approve By | char |  |

## resource_form_quotation

**ฟอร์มใบเสนอราคา** — Quotation Form

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `report_quotation_title` | ใบเสนอราคา *(resource only)* | QUOTATION | char |  |
| `report_quotation_pages` | หน้าที่ *(resource only)* | Pages | char |  |
| `report_quotation_copy_no` | พิมพ์ซ้ำครั้งที่ *(resource only)* | Copy No | char |  |
| `report_quotation_ar_name` | ชื่อลูกค้า *(resource only)* | Ar Name | char |  |
| `report_quotation_address` | ที่อยู่ *(resource only)* | Address | char |  |
| `report_quotation_tel` | โทรศัพท์ *(resource only)* | Telephone | char |  |
| `report_quotation_fax` | โทรสาร *(resource only)* | Fax | char |  |
| `report_quotation_doc_no` | เลขที่เอกสาร/No *(resource only)* | Document No | char |  |
| `report_quotation_doc_date` | วันที่/Date *(resource only)* | Document Date | char |  |
| `report_quotation_expire_date` | วันครบกำหนด/Duedate *(resource only)* | Expire Date | char |  |
| `report_quotation_credit_day` | เครดิต/Credit Day *(resource only)* | Credit Day | char |  |
| `report_quotation_sale` | พนักงานขาย *(resource only)* | Sale | char |  |
| `report_quotation_code` | รหัสสินค้า *(resource only)* | Code | char |  |
| `report_quotation_name` | รายการสินค้า *(resource only)* | Name | char |  |
| `report_quotation_unit` | หน่วย *(resource only)* | Unit | char |  |
| `report_quotation_qty` | จำนวน *(resource only)* | Qty | char |  |
| `report_quotation_price` | ราคาขาย *(resource only)* | Price | char |  |
| `report_quotation_discount` | ส่วนลด *(resource only)* | Discount | char |  |
| `report_quotation_amount` | จำนวนเงิน *(resource only)* | Amount | char |  |
| `report_quotation_remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `report_quotation_money_title` | ยอดเงินตัวหนังสือ *(resource only)* | ยอดเงินตัวหนังสือ | char |  |
| `report_quotation_total_amount` | รวมจำนวนเงิน *(resource only)* | Total Amount | char |  |
| `report_quotation_total_value` | ราคาสินค้า/บริการ *(resource only)* | Total Value | char |  |
| `report_quotation_total_vat_rate` | ภาษีมูลค่าเพิ่ม *(resource only)* | Vat Rate | char |  |
| `report_quotation_total_net_value` | จำนวนเงินรวมทั้งสิ้น *(resource only)* | Total Net Value | char |  |
| `report_quotation_approve` | ผู้อนุมัติ/APPROVE *(resource only)* | APPROVE BY | char |  |
| `report_quotation_sale_approve` | พนักงานขาย/SALE *(resource only)* | SALE APPROVE | char |  |
| `report_quotation_date` | วันที่ *(resource only)* | Date | char |  |

## resource_form_sale_order

**ฟอร์มใบสั่งขาย** — Sale Order Form

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `report_so_title` |  *(resource only)* |  | char |  |
| `report_so_pages` |  *(resource only)* |  | char |  |
| `report_so_copy_no` |  *(resource only)* |  | char |  |

