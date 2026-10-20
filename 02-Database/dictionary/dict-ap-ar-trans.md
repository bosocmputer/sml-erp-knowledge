---
tags: [sml, dictionary, ap-ar-trans, generated]
module: AP_AR_Trans
---
# พจนานุกรม: AP_AR_Trans — เอกสารลูกหนี้/เจ้าหนี้

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ap_ar_debt_balance]] | ตั้งหนี้ / AP AR Debt Balance | 23 |
| [[#ap_ar_debt_billing]] | รับ/จ่ายชำระหนี้ / AP AR Debt Billing | 23 |
| [[#ap_ar_debt_billing_cut]] | ตัดหนี้สูญ / AP AR Debt Billing Cut | 23 |
| [[#ap_ar_debt_billing_cut_detail]] | รายละเอียดการตัดหนี้สูญ / AP AR Debt Billing Cut Detail | 13 |
| [[#ap_ar_debt_billing_detail]] | รายละเอียดรับ/จ่ายชำระหนี้ / AP AR Debt Billing Detail | 13 |
| [[#ap_ar_debt_billing_temp]] | เตรียมชำระหนี้/ใบเสร็จชั่วคราว / AP AR Debt Billing Temp | 23 |
| [[#ap_ar_debt_billing_temp_detail]] | รายละเอียดเตรียมชำระหนี้/ใบเสร็จชั่วคราว / AP AR Debt Billing Temp Detail | 13 |
| [[#ap_ar_deposit_money]] | เงินล่วงหน้า/เงินมัดจำ / AP AR - Deposit Money | 29 |
| [[#ap_ar_pay_bill]] | วางบิล/รับวางบิล / Pay Bill | 18 |
| [[#ap_ar_pay_bill_detail]] | รายละเอียดใบวางบิล / Pay Bill Detail | 13 |
| [[#ap_ar_resource]] | รายละเอียดข้อความ / AP/AR Resource | 152 |
| [[#ap_ar_trans]] | รายวันทั้งหมด / AP AR - Transection | 144 |
| [[#ap_ar_trans_detail]] | รายละเอียดรายวัน / AP AR - Transection Detail | 73 |

## ap_ar_debt_balance

**ตั้งหนี้** — AP AR Debt Balance

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Documnet Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `debt_type` | ประเภทหนี้ยกมา | Debt Type | smallint | ✓ |
| `ar_code` | รหัสลูกค้า | Customer Code | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `sale_code` | พนักงานขาย | Sale | varchar(25) | ✓ |
| `area_code` | เขตการขาย | Sale Area | varchar(25) | ✓ |
| `credit_code` | รหัสเครดิต | Credit Code | varchar(25) | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `sum_debt_value` | มูลค่าหนี้ยกมา | Sum Debt Value | float | ✓ |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `job_code` | งาน | Job | varchar(25) | ✓ |

index: `ap_ar_debt_balance_PK_CODE`(doc_no)

## ap_ar_debt_billing

**รับ/จ่ายชำระหนี้** — AP AR Debt Billing · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `billing_flag` | ประเภทการชำระหนี้ | Billing Flag | smallint | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `person_code` | ผู้รับ/จ่ายชำระหนี้ | Person Code | varchar(25) | ✓ |
| `total_debt_value` | ยอดหนี้ | Total Debt Value | float | ✓ |
| `total_discount` | ส่วนลด | Total Discount | float | ✓ |
| `total_after_discount` | ยอดหนี้หลังหักส่วนลด | Total After Discount | float | ✓ |
| `total_money` | รับ/จ่ายชำระ | Total Money | float | ✓ |
| `total_debt_balance` | ยอดหนี้คงเหลือ | Total Debt Balance | float | ✓ |
| `bill_no` | เลขที่ใบกำกับ | Bill No | varchar(25) | ✓ |
| `bill_date` | วันที่ใบกำกับ | Bill Date | smalldatetime | ✓ |
| `tax_value` | มูลค่าภาษี | Tax Value | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ap_ar_debt_billing_PK_CODE`(doc_no)

## ap_ar_debt_billing_cut

**ตัดหนี้สูญ** — AP AR Debt Billing Cut

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `billing_type` | ประเภทการชำระหนี้ | Billing Type | smallint | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `person_code` | ผู้รับ/จ่ายชำระหนี้ | Person Code | varchar(25) | ✓ |
| `total_debt_value` | รวมยอดหนี้ | Total Debt Value | float | ✓ |
| `total_discount` | รวมส่วนลด | Total Discount Value | float | ✓ |
| `total_after_discount` | ยอดหนี้หลังหักส่วนลด | Total After Discount | float | ✓ |
| `total_money` | รับ/จ่ายชำระ | Total Money | float | ✓ |
| `total_debt_balance` | ยอดหนี้คงเหลือ | Total Debt Balance | float | ✓ |
| `bill_no` | เลขที่ใบกำกับ | Bill No | varchar(25) | ✓ |
| `bill_date` | วันที่ใบกำกับ | Bill Date | smalldatetime | ✓ |
| `tax_value` | มูลค่าภาษี | Tax Value | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ap_ar_debt_billing_cut_PK_CODE`(doc_no)

## ap_ar_debt_billing_cut_detail

**รายละเอียดการตัดหนี้สูญ** — AP AR Debt Billing Cut Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `billing_no` | เลขที่บิลซื้อ/ขาย | Billing No | varchar(25) | ✓ |
| `billing_date` | วันที่บิลซื้อ/ขาย | Billing Date | smalldatetime | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `debt_value` | รวมมูลค่าหนี้ | Debt Value | float | ✓ |
| `debt_cut_value` | มูลค่าตัดหนี้ | Debt Cut Value | float | ✓ |
| `sum_debt_balance` | ยอดหนี้คงเหลือ | Sum Debt Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_ar_debt_billing_detail

**รายละเอียดรับ/จ่ายชำระหนี้** — AP AR Debt Billing Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `billing_no` | เลขที่บิลซื้อ/ขาย | Billing No | varchar(25) | ✓ |
| `billing_date` | วันที่บิลซื้อ/ขาย | Billing Date | smalldatetime | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `sum_value` | รวมมูลค่า | Sum Value | float | ✓ |
| `sum_money` | รับ/จ่ายชำระหนี้ | Sum Money | float | ✓ |
| `sum_debt_balance` | ยอดหนี้คงเหลือ | Sum Debt Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_ar_debt_billing_temp

**เตรียมชำระหนี้/ใบเสร็จชั่วคราว** — AP AR Debt Billing Temp

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `billing_flag` | ประเภทการชำระหนี้ | Billing Flag | smallint | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `person_code` | ผู้รับ/จ่ายชำระหนี้ | Person Code | varchar(25) | ✓ |
| `total_debt_value` | รวมยอดหนี้ | Total Debt Value | float | ✓ |
| `total_discount` | รวมส่วนลด | Total Discount Value | float | ✓ |
| `total_after_discount` | ยอดหนี้หลังหักส่วนลด | Total After Discount | float | ✓ |
| `total_money` | รับ/จ่ายชำระ | Total Money | float | ✓ |
| `total_debt_balance` | ยอดหนี้คงเหลือ | Total Debt Balance | float | ✓ |
| `bill_no` | เลขที่ใบกำกับ | Bill No | varchar(25) | ✓ |
| `bill_date` | วันที่ใบกำกับ | Bill Date | smalldatetime | ✓ |
| `tax_value` | มูลค่าภาษี | Tax Value | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ap_ar_debt_billing_temp_PK_CODE`(doc_no)

## ap_ar_debt_billing_temp_detail

**รายละเอียดเตรียมชำระหนี้/ใบเสร็จชั่วคราว** — AP AR Debt Billing Temp Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `billing_no` | เลขที่บิลซื้อ/ขาย | Billing No | varchar(25) | ✓ |
| `billing_date` | วันที่บิลซื้อ/ขาย | Billing Date | smalldatetime | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `sum_value` | รวมมูลค่า | Sum Value | float | ✓ |
| `sum_money` | รับ/จ่ายชำระหนี้ | Sum Money | float | ✓ |
| `sum_debt_balance` | ยอดหนี้คงเหลือ | Sum Debt Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_ar_deposit_money

**เงินล่วงหน้า/เงินมัดจำ** — AP AR - Deposit Money

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(255) | ✓ |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `deposit_type` | ประเภทเงินรับ/จ่าย | Deposit Type | smallint | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `bill_no` | เลขที่ใบกำกับ | Bill No | varchar(25) | ✓ |
| `bill_date` | วันที่ใบกำกับ | Bill Date | smalldatetime | ✓ |
| `vat_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `credit_day` | จำนวนวันเครดิต | Credit Day | int | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `sale_code` | พนักงานขาย | Sale Code | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `vat_rate` | อัตราภาษี | Vat Rate | float | ✓ |
| `total_value` | มูลค่าสินค้า | Total Value | float | ✓ |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `total_after_vat` | มูลค่ารวมภาษี | Total After Vat | float | ✓ |
| `total_net_value` | มูลค่าทั้งสิ้น | Total Net Value | float | ✓ |
| `amount` | ยอดเงินชำระ | Amount | float | ✓ |
| `money_balance` | ยอดเงินคงเหลือ | Money Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ap_ar_deposit_money_PK_CODE`(doc_no)

## ap_ar_pay_bill

**วางบิล/รับวางบิล** — Pay Bill

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `ap_ar_code` | เจ้าหนี้/ลูกหนี้ | AP/AR Code | varchar(25) | ✓ |
| `credit_day` | วันเครดิต | Credit Day | int | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `sale_code` | พนักงานขาย | Sale | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) |  |
| `total_value` | มูลค่าทั้งหมด | Total Value | float | ✓ |
| `debt_decrease` | มูลค่าลดหนี้ | Debt Decrease | float | ✓ |
| `debt_increase` | มูลค่าเพิ่มหนี้ | Debt Increase | float | ✓ |
| `total_net_value` | มูลค่าสุทธิ | Total Net Value | float | ✓ |
| `total_debt_balance` | ยอดหนี้คงค้าง | Total Debt Balance | float |  |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `transection_flag` | รายวันของระบบ | Transection Flag | smallint | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `ap_ar_pay_bill_PK_CODE`(doc_no)

## ap_ar_pay_bill_detail

**รายละเอียดใบวางบิล** — Pay Bill Detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `bill_type` | ประเภทเอกสาร | Bill Type | smallint | ✓ |
| `bill_no` | เลขที่บิล | Bill No | varchar(25) | ✓ |
| `bill_date` | วันที่บิล | Bill Date | smalldatetime | ✓ |
| `bill_ref` | อ้างอิงบิล | Bill Reference | varchar(25) | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `debt_value` | รวมมูลค่าหนี้ | Debt Value | float | ✓ |
| `pay_bill_value` | มูลค่าที่วางบิล | Pay Value | float | ✓ |
| `value_balance` | รวมยอดคงค้าง | Value Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_ar_resource

**รายละเอียดข้อความ** — AP/AR Resource · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `customer` | ลูกค้า *(resource only)* | Customer | char |  |
| `target_customer` | ลูกค้าเป้าหมาย *(resource only)* | Target Customer | char |  |
| `ap_ar_name` | ชื่อเจ้าหนี้/ลูกหนี้ *(resource only)* | AP AR Name | char |  |
| `tax_out` | ภาษีแยกนอก *(resource only)* | Ext Tax | char |  |
| `tax_in` | ภาษีรวมใน *(resource only)* | Inc Tax | char |  |
| `tax_zero` | ภาษีอัตราศูนย์ *(resource only)* | No Tax | char |  |
| `deposit_date` | วันที่เงินมัดจำ *(resource only)* | Deposit Date | char |  |
| `deposit_doc` | เลขที่เงินมัดจำ *(resource only)* | Deposit Doc | char |  |
| `prepaid_money` | เงินล่วงหน้า *(resource only)* | Prepaid Money | char |  |
| `deposit_money` | มูลค่าเงินมัดจำ *(resource only)* | Deposit Money | char |  |
| `deposit_value` | จำนวนเงินมัดจำ *(resource only)* | Deposit Value | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* | AP Name | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* | AR Name | char |  |
| `to_receive` | รับ *(resource only)* | Receive | char |  |
| `send_to` | ส่ง *(resource only)* | Send | char |  |
| `tab_detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `tab_paybill` | การจ่ายเงิน *(resource only)* | Paybill | char |  |
| `tab_dimension` | มิติ *(resource only)* | Dimension | char |  |
| `tab_contact` | ติดต่ออ้างอิง *(resource only)* | Contact Detail | char |  |
| `tab_item` | สินค้า *(resource only)* | Item | char |  |
| `tab_logistic_area` | สถานที่ส่งสินค้า *(resource only)* | Logistic Area | char |  |
| `tab_credit_group` | กลุ่มเครดิต *(resource only)* | Credit Group | char |  |
| `close_credit` | ปิด *(resource only)* | Close | char |  |
| `open_credit` | เปิด *(resource only)* | Open | char |  |
| `stop_credit` | ปิด(ชั่วคราว) *(resource only)* | Stop | char |  |
| `active` | ติดต่อ *(resource only)* | Active | char |  |
| `inactive` | ยกเลิก *(resource only)* | Inactive | char |  |
| `sale_name` | ชื่อพนักงานขาย *(resource only)* | Sale Name | char |  |
| `po_debt_balance` | ตั้งหนี้ *(resource only)* | OP Debt Balance | char |  |
| `po_cn_balance` | ลดหนี้ *(resource only)* | PO CN Balance | char |  |
| `po_purchase` | บิลซื้อ *(resource only)* | PO Purchase | char |  |
| `po_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | PO Addition Debt | char |  |
| `so_billing` | บิลขาย *(resource only)* | SO Billing | char |  |
| `so_addition_debt` | เพิ่มสินค้า/เพิ่มหนี้ *(resource only)* | SO Addition Debt | char |  |
| `so_debt_balance` | ตั้งหนี้ *(resource only)* | SO Debt Balance | char |  |
| `so_cn_balance` | ลดหนี้ *(resource only)* | SO CN Balance | char |  |
| `tab_image` | รูปภาพ *(resource only)* | Image | char |  |
| `from_doc_date` | จากวันที่ *(resource only)* | From Doc Date | char |  |
| `to_doc_date` | ถึงวันที่ *(resource only)* | To Doc Date | char |  |
| `from_doc_no` | จากเลขที่เอกสาร *(resource only)* | From Doc No | char |  |
| `to_doc_no` | ถึงเลขที่เอกสาร *(resource only)* | To Doc No | char |  |
| `from_customer` | จากลูกค้า *(resource only)* | From Customer | char |  |
| `to_customer` | ถึงลูกค้า *(resource only)* | To Customer | char |  |
| `ap_ar_debt_type` | ประเภท *(resource only)* | Debt Type | char |  |
| `tab_cash` | รายละเอียด *(resource only)* | Cash | char |  |
| `tab_credit` | บัตรเครดิต *(resource only)* | Credit Card | char |  |
| `tab_cheque` | เช็ค *(resource only)* | Cheque | char |  |
| `cash_money` | เงินสด *(resource only)* | Cash Money | char |  |
| `transfer_payment` | เงินโอน *(resource only)* | Transfer payment | char |  |
| `total_receive_money` | จำนวนเงิน *(resource only)* | Total Receive Money | char |  |
| `receive_type` | ประเภทการชำระ *(resource only)* | Receive Type | char |  |
| `cheque_type` | ประเภทเช็ค *(resource only)* | Cheque Type | char |  |
| `book_bank` | เลขที่บัญชี *(resource only)* | Book Bank | char |  |
| `transfer_date` | วันที่โอน *(resource only)* | Transfer Date | char |  |
| `amount` | จำนวนเงิน *(resource only)* | Amount | char |  |
| `bank_code` | ธนาคาร *(resource only)* | bank_code | char |  |
| `order_by` | เรียงตาม *(resource only)* |  | char |  |
| `order_by_customer` | ตามลูกค้า *(resource only)* |  | char |  |
| `order_by_docno` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `order_by_duedate` | วันที่ครบกำหนด *(resource only)* |  | char |  |
| `ar_code_begin` | จากรหัสลูกหนี้ *(resource only)* |  | char |  |
| `ar_code_end` | ถึงรหัสลูกหนี้ *(resource only)* |  | char |  |
| `date_begin` | จากวันที่ *(resource only)* |  | char |  |
| `date_end` | ถึงวันที่ *(resource only)* |  | char |  |
| `term_1_begin` | ช่วงที่ 1 *(resource only)* |  | char |  |
| `term_1_end` | ถึง *(resource only)* |  | char |  |
| `term_2_begin` | ช่วงที่ 2 *(resource only)* |  | char |  |
| `term_2_end` | ถึง *(resource only)* |  | char |  |
| `term_3_begin` | ช่วงที่ 3 *(resource only)* |  | char |  |
| `term_3_end` | ถึง *(resource only)* |  | char |  |
| `term_4_begin` | ช่วงที่ 4 *(resource only)* |  | char |  |
| `term_4_end` | ถึง *(resource only)* |  | char |  |
| `term_5_end` | เกินกว่า *(resource only)* |  | char |  |
| `total_deposit` | ยอดเงินล่วงหน้า *(resource only)* |  | char |  |
| `total_discount` | ยอดลดหนี้ *(resource only)* |  | char |  |
| `term_due` | ช่วง *(resource only)* |  | char |  |
| `day_due` | วัน *(resource only)* |  | char |  |
| `over_due` | เกิน *(resource only)* |  | char |  |
| `out_due` | ยังไม่ครบกำหนด *(resource only)* |  | char |  |
| `ar_code` | รหัสลูกหนี้ *(resource only)* |  | char |  |
| `ar_balance` | ยอดคงค้าง *(resource only)* |  | char |  |
| `term_1` | ช่วงที่ 1 *(resource only)* |  | char |  |
| `term_2` | ช่วงที่ 2 *(resource only)* |  | char |  |
| `term_3` | ช่วงที่ 3 *(resource only)* |  | char |  |
| `term_4` | ช่วงที่ 4 *(resource only)* |  | char |  |
| `term_5` | ช่วงที่ 5 *(resource only)* |  | char |  |
| `term_6` | มากกว่า *(resource only)* |  | char |  |
| `doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `by_doc_no` | เลขที่เอกสาร *(resource only)* |  | char |  |
| `by_due_date` | วันที่ครบกำหนด *(resource only)* |  | char |  |
| `total_debit_note` | ยอดเพิ่มหนี้ *(resource only)* |  | char |  |
| `doc_type` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `debit_amount` | เดบิต *(resource only)* |  | char |  |
| `credit_amount` | เครดิต *(resource only)* |  | char |  |
| `vat_no` | เลขที่ใบกำกับ *(resource only)* |  | char |  |
| `credit_day` | เครดิต (วัน) *(resource only)* |  | char |  |
| `ref_no` | เอกสารอ้างอิง *(resource only)* |  | char |  |
| `due_date_select` | เงื่อนไขวันที่ครบกำหนด *(resource only)* |  | char |  |
| `by_doc_date` | วันที่เอกสาร *(resource only)* |  | char |  |
| `term_0` | ปัจจุบัน *(resource only)* |  | char |  |
| `due_date` | ครบกำหนด *(resource only)* |  | char |  |
| `due_day` | เกินกำหนด(วัน) *(resource only)* |  | char |  |
| `balance_first` | ยอดยกมา *(resource only)* |  | char |  |
| `debit_1` | ยอดตั้งหนี้ *(resource only)* |  | char |  |
| `debit_2` | ยอดเพิ่มหนี้ *(resource only)* |  | char |  |
| `credit_1` | ยอดลดหนี้ *(resource only)* |  | char |  |
| `credit_2` | ยอดตัดชำระหนี้ *(resource only)* |  | char |  |
| `balance_end` | ยอดยกไป *(resource only)* |  | char |  |
| `ap_code_begin` | จากรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `ap_code_end` | ถึงรหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `by_ar_code` | ลูกหนี้ *(resource only)* |  | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* |  | char |  |
| `select` | เลือก *(resource only)* |  | char |  |
| `doc_type_number` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `tab_transfer` | เงินโอน *(resource only)* |  | char |  |
| `tab_deposit` | เงินล่วงหน้า *(resource only)* |  | char |  |
| `tab_advance` | เงินมัดจำ *(resource only)* |  | char |  |
| `tab_petty_cash` | เงินสดย่อย *(resource only)* |  | char |  |
| `balance_amount` | ยอดคงเหลือ *(resource only)* |  | char |  |
| `use_amount` | ยอดหักแล้ว *(resource only)* |  | char |  |
| `status` | สถานะ *(resource only)* |  | char |  |
| `tab_coupon` | คูปอง *(resource only)* |  | char |  |
| `credit_money` | วงเงินเครดิต *(resource only)* |  | char |  |
| `credit_money_max` | วงเงินเครดิตสูงสุด *(resource only)* |  | char |  |
| `ref_doc_no` | เอกสารอ้างอิง *(resource only)* |  | char |  |
| `ref_doc_date` | วันที่อ้างอิง *(resource only)* |  | char |  |
| `point_balance` | แต้มคงเหลือ *(resource only)* |  | char |  |
| `tab_remark` | หมายเหตุ *(resource only)* |  | char |  |
| `tab_creditsale` | ขายเงินเชื่อ *(resource only)* |  | char |  |
| `branch_code` | สาขา *(resource only)* |  | char |  |
| `tax_doc_no` | เลขที่ใบกำกับภาษี *(resource only)* |  | char |  |
| `tax_doc_date` | วันที่ใบกำกับภาษี *(resource only)* |  | char |  |
| `tab_expense` | ค่าใช้จ่ายอื่น *(resource only)* |  | char |  |
| `tab_income` | รายได้อื่น *(resource only)* |  | char |  |
| `tab_payother` | จ่ายอื่น ๆ *(resource only)* |  | char |  |
| `tab_subtract` | หักอื่น ๆ *(resource only)* |  | char |  |
| `remark` | หมายเหตุ *(resource only)* |  | char |  |
| `tab_currency_other` | สกุลเงินอื่น ๆ *(resource only)* |  | char |  |
| `close_credit_date_from` | จากวันที่ปิดสถานะเครดิต *(resource only)* |  | char |  |
| `close_credit_date_to` | ถึงวันที่ปิดสถานะเครดิต *(resource only)* |  | char |  |
| `doc_credit_day` | เครดิต (วัน) *(resource only)* |  | char |  |
| `debt_bill_no` | เลขที่ใบวางบิล *(resource only)* |  | char |  |
| `from_credit_day` | จากวันเครดิต *(resource only)* |  | char |  |
| `to_credit_day` | ถึงวันเครดิต *(resource only)* |  | char |  |
| `tab_pay_wallet` | Wallet Payment *(resource only)* |  | char |  |
| `currency_code` | สกุลเงิน *(resource only)* | Currency Code | char |  |
| `currency_amount` | มูลค่าตามสกุลเงิน *(resource only)* | Currency Amount | char |  |
| `exchange_rate` | อัตราแลกเปลี่ยน *(resource only)* | Exchange Rate | char |  |
| `ship_code` | Ship Code *(resource only)* |  | char |  |
| `ar_balance_2` | ยอดคงเหลือ 2 *(resource only)* |  | char |  |
| `currency_balance_amount` | ยอดคงเหลือตามสกุลเงิน *(resource only)* |  | char |  |

## ap_ar_trans

**รายวันทั้งหมด** — AP AR - Transection · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Documnet Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(25) | ✓ |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ | Doc Reference Date | smalldatetime | ✓ |
| `tax_doc_no` | เลขที่ใบกำกับ | Tax Document No | varchar(25) | ✓ |
| `tax_doc_date` | วันที่ใบกำกับ | Tax Document Date | smalldatetime | ✓ |
| `cust_code` | เจ้าหนี้/ลูกหนี้ | Customer Code | varchar(25) | ✓ |
| `project_code` | โครงการ | Project | varchar(25) | ✓ |
| `allocate_code` | การจัดสรร | Allocate | varchar(25) | ✓ |
| `job_code` | งาน | Job | varchar(25) | ✓ |
| `side_code` | ฝ่าย | Side | varchar(25) | ✓ |
| `department_code` | แผนก | department | varchar(25) | ✓ |
| `sale_area_code` | เขตการขาย | Sale Area Code | varchar(25) | ✓ |
| `sale_code` | พนักงานขาย | Sale | varchar(25) | ✓ |
| `credit_code` | รหัสเครดิต | Credit Code | varchar(25) | ✓ |
| `credit_day` | วันเครดิต | Credit Day | int | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `discount_word` | ส่วนลด | Discount Word | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `customer` | ลูกค้า *(resource only)* | Customer | char |  |
| `target_customer` | ลูกค้าเป้าหมาย *(resource only)* | Target Customer | char |  |
| `ap_ar_name` | ชื่อเจ้าหนี้/ลูกหนี้ *(resource only)* | AP AR Name | char |  |
| `tax_out` | ภาษีแยกนอก *(resource only)* | Ext Tax | char |  |
| `tax_in` | ภาษีรวมใน *(resource only)* | Inc Tax | char |  |
| `tax_zero` | ภาษีอัตราศูนย์ *(resource only)* | No Tax | char |  |
| `deposit_date` | วันที่เงินมัดจำ *(resource only)* | Deposit Date | char |  |
| `deposit_doc` | เลขที่เงินมัดจำ *(resource only)* | Deposit Doc | char |  |
| `prepaid_money` | เงินล่วงหน้า *(resource only)* | Prepaid Money | char |  |
| `deposit_money` | มูลค่าเงินมัดจำ *(resource only)* | Deposit Money | char |  |
| `deposit_value` | จำนวนเงินมัดจำ *(resource only)* | Deposit Value | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* | AP Name | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* | AR Name | char |  |
| `to_receive` | รับ *(resource only)* | Receive | char |  |
| `send_to` | ส่ง *(resource only)* | Send | char |  |
| `tab_detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `tab_credit` | เครดิต *(resource only)* | Credit | char |  |
| `tab_paybill` | การจ่ายเงิน *(resource only)* | Paybill | char |  |
| `tab_dimension` | มิติ *(resource only)* | Dimension | char |  |
| `tab_contact` | ติดต่ออ้างอิง *(resource only)* | Contact Detail | char |  |
| `tab_item` | สินค้า *(resource only)* | Item | char |  |
| `tab_logistic_area` | สถานที่ส่งสินค้า *(resource only)* | Logistic Area | char |  |
| `tab_credit_group` | กลุ่มเครดิต *(resource only)* | Credit Group | char |  |
| `close_credit` | ปิด *(resource only)* | Close | char |  |
| `open_credit` | เปิด *(resource only)* | Open | char |  |
| `stop_credit` | ปิด(ชั่วคราว) *(resource only)* | Stop | char |  |
| `active` | ติดต่อ *(resource only)* | Active | char |  |
| `inactive` | ยกเลิก *(resource only)* | Inactive | char |  |
| `sale_name` | ชื่อพนักงานขาย *(resource only)* | Sale Name | char |  |
| `po_debt_balance` | ตั้งหนี้ยกมา | OP Debt Balance | int | ✓ |
| `po_cn_balance` | ลดหนี้ยกมา | PO CN Balance | int | ✓ |
| `po_purchase` | ซื้อสินค้า | PO Purchase | int | ✓ |
| `po_addition_debt` | ซื้อเพิ่ม/เพิ่มหนี้ | PO Addition Debt | int | ✓ |
| `so_billing` | ขายสินค้า | SO Billing | int | ✓ |
| `so_addition_debt` | ขายเพิ่ม/เพิ่มหนี้ | SO Addition Debt | int | ✓ |
| `so_debt_balance` | ตั้งหนี้ยกมา | SO Debt Balance | int | ✓ |
| `so_cn_balance` | ลดหนี้ยกมา | SO CN Balance | int | ✓ |
| `tab_image` | รูปภาพ *(resource only)* | Image | char |  |
| `from_doc_date` | จากวันที่ *(resource only)* | From Doc Date | char |  |
| `to_doc_date` | ถึงววันที่ *(resource only)* | To Doc Date | char |  |
| `from_doc_no` | จากเลขที่เอกสาร *(resource only)* | From Doc No | char |  |
| `to_doc_no` | ถึงเลขที่เอกสาร *(resource only)* | To Doc No | char |  |
| `from_customer` | จากลูกค้า *(resource only)* | From Customer | char |  |
| `to_customer` | ถึงลูกค้า *(resource only)* | To Customer | char |  |
| `ap_ar_debt_type` | ประเภท *(resource only)* | Debt Type | char |  |
| `ap_code` | รหัสเจ้าหนี้ *(resource only)* | Supplier Code | char |  |
| `ar_code` | รหัสลูกหนี้ *(resource only)* | Customer Code | char |  |
| `currency_money` | ยอดคงเหลือ(ตามสกุลเงิน) | Currency Money | float | ✓ |
| `cust_name` | ชื่อ *(resource only)* | Cust name | char |  |
| `po_debt_balance_other` | ตั้งหนี้อื่นๆ *(resource only)* | OP Debt Balance Other | char |  |
| `po_cn_balance_other` | ลดหนี้อื่นๆ *(resource only)* | PO CN Balance Other | char |  |
| `so_debt_balance_other` | ตั้งหนี้อื่นๆ *(resource only)* | SO Debt Balance Other | char |  |
| `so_cn_balance_other` | ลดหนี้อื่นๆ *(resource only)* | SO CN Balance Other | char |  |
| `vat_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `vat_rate` | อัตราภาษี | Vat Rate | float | ✓ |
| `total_value` | มูลค่าสินค้า | Total Value | float | ✓ |
| `total_vat_value` | ภาษีมูลค่าเพิ่ม | Total Vat Value | float | ✓ |
| `total_after_vat` | มูลค่ารวมภาษี | Total After Vat | float | ✓ |
| `total_net_value` | มูลค่าทั้งสิ้น | Total Net Value | float | ✓ |
| `amount` | ยอดเงินชำระ | Amount | float | ✓ |
| `money_balance` | ยอดเงินคงเหลือ | Money Balance | float | ✓ |
| `book_no` | เลขที่ใบสั่งจอง | Book No | varchar(100) | ✓ |
| `payment_method` | วิธีชำระเงิน | Payment method | varchar(100) | ✓ |
| `pay_installments` | จ่ายส่วนที่เหลือภายใน/วัน | Pay Installments | varchar(100) | ✓ |
| `delivery_date` | วันที่ส่งของ | Date of delivery | smalldatetime | ✓ |
| `sum_pay_money_cash` | เงินสด | Sum Pay Money (Cash) | float | ✓ |
| `sum_pay_money_chq` | เช็ค | Sum Pay Money (Cheque) | float | ✓ |
| `sum_pay_money_credit` | บัตรเครดิต | Sum Pay Money (Credit Card) | float | ✓ |
| `sum_pay_money_transfer` | เงินโอน | Sum Pay Money (Transfer) | float | ✓ |
| `po_pay_bill` | ใบรับวางบิล *(resource only)* | Pay Bill | char |  |
| `so_pay_bill` | ใบรับวางบิล *(resource only)* | Pay Bill | char |  |
| `po_cn_debt` | ส่งคืนสินค้า/ลดหนี้ *(resource only)* | CN Debt | char |  |
| `so_cn_debt` | ส่งคืนสินค้า/ลดหนี้ *(resource only)* | CN Debt | char |  |
| `po_increase_debt` | เพิ่มหนี้ยกมา *(resource only)* | Increase Debt | char |  |
| `so_increase_debt` | เพิ่มหนี้ยกมา *(resource only)* | Increase Debt | char |  |
| `total_before_vat` | ยอดก่อนภาษี |  | float | ✓ |
| `total_discount` | ส่วนลด |  | float | ✓ |
| `total_pay_money` | ยอดชำระ |  | float | ✓ |
| `total_debt_balance` | ยอดคงเหลือ |  | float | ✓ |
| `total_after_discount` | ยอดรวมหลังหักส่วนลด |  | float | ✓ |
| `pay_bill_no_1` | เลขที่ใบจ่ายชำระหนี้ *(resource only)* |  | char |  |
| `pay_bill_no_2` | เลขที่ใบรับชำระหนี้ *(resource only)* |  | char |  |
| `last_status` | สถานะล่าสุด (0=Normal,1=ยกเลิก) |  | smallint | ✓ |
| `used_status` | มีการอ้างอิงแล้ว |  | smallint | ✓ |
| `doc_success` | สิ้นสุด |  | smallint | ✓ |
| `total_pay_tax` | ภาษีหัก ณ ที่จ่าย |  | float | ✓ |
| `total_debt_value` | รวมมูลค่า |  | float | ✓ |
| `sum_pay_money_diff` | ผลต่าง |  | float | ✓ |
| `due_pay_date` | วันที่นัดชำระ *(resource only)* |  | smalldatetime |  |
| `sum_pay_money_cash_in` | รับชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_in` | รับชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_in` | รับชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_in` | รับชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_cash_out` | จ่ายชำระ (เงินสด) *(resource only)* | Sum Pay Money (Cash) | float |  |
| `sum_pay_money_chq_out` | จ่ายชำระ (เช็ค) *(resource only)* | Sum Pay Money (Cheque) | float |  |
| `sum_pay_money_credit_out` | จ่ายชำระ (บัตรเครดิต) *(resource only)* | Sum Pay Money (Credit Card) | float |  |
| `sum_pay_money_transfer_out` | จ่ายชำระ (เงินโอน) *(resource only)* | Sum Pay Money (Transfer) | float |  |
| `sum_pay_money_1` | จำนวนเงินวางบิล *(resource only)* |  | char |  |
| `doc_time` | เวลา |  | varchar(5) | ✓ |
| `doc_format_code` | รูปแบบเอกสาร |  | varchar(25) | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `tab_more` | เพิ่มเติม *(resource only)* |  | char |  |
| `employee` | พนักงาน *(resource only)* |  | char |  |
| `is_manual_vat` | บันทึกรายการภาษีเอง |  | smallint | ✓ |
| `is_cancel` | ยกเลิกเอกสาร |  | smallint | ✓ |
| `cancel_code` | ผู้ยกเลิกเอกสาร |  | varchar(25) | ✓ |
| `cancel_datetime` | เวลายกเลิกเอกสาร |  | datetime | ✓ |
| `receipt_doc_no` | เลขที่ใบเสร็จ *(resource only)* |  | char |  |
| `receipt_doc_date` | วันที่ใบเสร็จ *(resource only)* |  | char |  |
| `total_net_value_2` | มูลค่าทั้งสิ้น |  | float | ✓ |
| `total_net_value_old` | มูลค่าตามอัตราแลกเปลี่ยนเดิม *(resource only)* |  | char |  |
| `lost_profit_exchange_amount` | ผลต่างจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `ref_doc_type` | ประเภทเอกสาร |  | varchar(50) | ✓ |

index: `ap_ar_trans_AP_AR_TRANS_PK_PRIMARY`(doc_no), `ap_ar_trans_doc_ref`(doc_ref), `ap_ar_trans_last_status`(trans_flag,last_status), `ap_ar_trans_last_status2`(last_status), `ap_ar_trans_used_status`(used_status), `ap_ar_trans_trans_flag_trans_type_idx`(trans_flag,trans_type), `ap_ar_trans_doc_date_idx`(doc_date), `ap_ar_trans_trans_flag_idx`(trans_flag), `ap_ar_trans_cust_code_idx`(cust_code), `ap_ar_trans_doc_no_trans_flag_idx`(doc_no,trans_flag)

## ap_ar_trans_detail

**รายละเอียดรายวัน** — AP AR - Transection Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `trans_type` | ประเภทรายวัน | Transection Type | smallint |  |
| `trans_flag` | รายวันระบบ | Transection Flag | smallint |  |
| `doc_group` | กลุ่มเอกสาร | Document Group | varchar(25) | ✓ |
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) |  |
| `doc_ref` | เอกสารอ้างอิง | Document Reference | varchar(255) | ✓ |
| `billing_no` | เอกสารเลขที่ | Billing No | varchar(25) | ✓ |
| `billing_date` | เอกสารวันที่ | Billing Date | smalldatetime | ✓ |
| `due_date` | วันที่ครบกำหนด | Due Date | smalldatetime | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `exchange_rate` | อัตราแลกเปลี่ยน | Exchange Rate | float | ✓ |
| `sum_debt_value` | รวมมูลค่า | Sum Value | float | ✓ |
| `sum_tax_value` | มูลค่าภาษี | Sum Tax Value | float | ✓ |
| `sum_debt_amount` | จำนวนเงิน | Sum Debt Amount | float | ✓ |
| `sum_discount` | ส่วนลด | Sum Discount | float | ✓ |
| `sum_after_discount` | ยอดหนี้หลังหักส่วนลด | Sum After Discount | float | ✓ |
| `sum_pay_money_cash` | รับ/จ่ายชำระหนี้ (เงินสด) | Sum Pay Money (Cash) | float | ✓ |
| `sum_pay_money_chq` | รับ/จ่ายชำระหนี้ (เช็ค) | Sum Pay Money (Cheque) | float | ✓ |
| `sum_pay_money_credit` | รับ/จ่ายชำระหนี้ (บัตรเครดิต) | Sum Pay Money (Credit Card) | float | ✓ |
| `sum_pay_money_transfer` | รับ/จ่ายชำระหนี้ (เงินโอน) | Sum Pay Money (Transfer) | float | ✓ |
| `sum_debt_balance` | ยอดหนี้คงเหลือ | Sum Debt Balance | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | smallint | ✓ |
| `doc_ref_requisition` | เลขที่ใบเบิกสินค้า *(resource only)* |  | char |  |
| `doc_ref_purchase` | เลขที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_ref_purchase_date` | วันที่ใบซื้อ *(resource only)* |  | char |  |
| `doc_ref_requisition_date` | วันที่ใบเบิกสินค้า *(resource only)* |  | char |  |
| `doc_ref_purchase_order` | เลขที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_purchase_order_date` | วันที่ใบสั่งซื้อ *(resource only)* |  | char |  |
| `doc_ref_date` | เอกสารอ้างอิงวันที่ *(resource only)* |  | char |  |
| `bill_type` | ประเภทรายวัน | Bill Type | smallint | ✓ |
| `doc_ref_quotation` | เลขที่ใบเสนอราคา *(resource only)* |  | char |  |
| `doc_ref_quotation_date` | วันที่ใบเสนอราคา *(resource only)* |  | char |  |
| `sum_pay_money` | ยอดชำระ | Pay Money | float | ✓ |
| `sum_before_vat` | ยอดก่อนภาษี | Sum Debt Tax | float | ✓ |
| `doc_ref_debt_billing_ap` | เลขใบรับวางบิล (เจ้าหนี้) *(resource only)* |  | char |  |
| `doc_ref_debt_billing_ar` | ใบวางบิล (ลูกหนี้) *(resource only)* |  | char |  |
| `sum_value` | มูลค่าสินค้า |  | float | ✓ |
| `balance_ref` | ยอดคงเหลือ |  | float | ✓ |
| `vat_rate` | อัตราภาษี |  | float | ✓ |
| `sum_pay_money_1` | จำนวนเงินวางบิล *(resource only)* |  | char |  |
| `description` | รายละเอียด *(resource only)* |  | char |  |
| `bill_type_name` | ประเภทเอกสาร *(resource only)* |  | char |  |
| `doc_ref_pr_approval` | เลขที่ใบอนุมัติเสนอซื้อ *(resource only)* |  | char |  |
| `ref_amount_debit` | มูลค่าเพิ่มหนี้ *(resource only)* |  | char |  |
| `ref_amount_credit` | มูลค่าลดหนี้ *(resource only)* |  | char |  |
| `final_amount` | มูลค่าที่ถูกต้อง |  | float | ✓ |
| `last_status` | สถานะล่าสุด |  | smallint | ✓ |
| `calc_flag` | (1,-1) |  | smallint | ✓ |
| `doc_ref_partial` | เลขที่ใบรับ *(resource only)* |  | char |  |
| `doc_ref_partial_date` | วันที่ใบรับ *(resource only)* |  | char |  |
| `ref_doc_no` | เลขที่เอกสารอ้างอิงบิล |  | varchar(255) | ✓ |
| `ref_doc_date` | วันที่เอกสารอ้างอิงบิล |  | smalldatetime | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `doc_ref_po_requrest` | เลขที่ใบเสนอซื้อ *(resource only)* |  | char |  |
| `creator_code` | ผู้สร้างเอกสาร |  | varchar(25) | ✓ |
| `last_editor_code` | ผู้แก้ไขเอกสารล่าสุด |  | varchar(25) | ✓ |
| `create_datetime` | วันที่สร้างเอกสาร |  | datetime | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `cust_name` | ชื่อลูกค้า *(resource only)* |  | char |  |
| `cust_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `doc_ref_pre_requisition` | เลขที่ใบขอเบิก *(resource only)* |  | char |  |
| `doc_ref_product_deposit` | เลขที่ใบฝากสินค้า *(resource only)* |  | char |  |
| `bill_tax_no` | เลขที่ใบกำกับภาษี |  | varchar(255) | ✓ |
| `bill_tax_date` | วันที่ใบกำกับภาษี |  | smalldatetime | ✓ |
| `receipt_doc_no` | เลขที่ใบเสร็จ *(resource only)* |  | char |  |
| `receipt_doc_date` | วันที่ใบเสร็จ *(resource only)* |  | char |  |
| `sum_debt_amount_2` | จำนวนเงิน |  | float | ✓ |
| `balance_ref_2` | ยอดคงเหลือ |  | float | ✓ |
| `sum_pay_money_2` | ยอดชำระ |  | float | ✓ |
| `lost_profit_exchange_amount` | กำไรขาดทุนจากอัตราแลกเปลี่ยน |  | float | ✓ |
| `exchange_rate_old` | อัตราแลกเปลี่ยนเดิม |  | float | ✓ |

index: `pk_ap_ar_trans_detail_laststatus`(last_status), `pk_ap_ar_trans_detail_docno`(doc_no), `pk_ap_ar_trans_detail_trans_flag`(trans_flag), `ap_ar_trans_detail_doc_ref`(doc_ref), `ap_ar_trans_detail_billing_no`(billing_no), `ap_ar_trans_detail_doc_no_trans_flag_idx`(doc_no,trans_flag), `ap_ar_trans_billing_no_trans_flag`(billing_no,trans_flag)

