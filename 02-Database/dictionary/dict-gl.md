---
tags: [sml, dictionary, gl, generated]
module: GL
---
# พจนานุกรม: GL — บัญชีแยกประเภท

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#gl_account_close]] | gl_account_close / gl_account_close | 24 |
| [[#gl_account_close_detail]] | รายละเอียการปิดบัญชีสินค้าล / gl_account_close_detail | 12 |
| [[#gl_account_cost]] | ประเภทต้นทุน / Account Cost | 4 |
| [[#gl_account_group]] | กลุ่มบัญชี / Account group | 4 |
| [[#gl_account_type]] | ประเภทบัญชี / Account type | 4 |
| [[#gl_cash_flow_group]] | กลุ่มบัญชีกระแสเงินสด / Cash flow Group | 4 |
| [[#gl_chart_of_account]] | ผังบัญชี / Chart of account | 50 |
| [[#gl_chart_of_account_allocate_list]] | ผังบัญชีแยกตามการจัดสรร / Account Allocate list | 2 |
| [[#gl_chart_of_account_depart_list]] | ผังบัญชีแยกตามแผนก / Account department list | 2 |
| [[#gl_chart_of_account_job_list]] | ผังบัญชีแยกตามงาน / Account Job list | 2 |
| [[#gl_chart_of_account_project_list]] | ผังบัญชีแยกตามโครงการ / Account Project list | 2 |
| [[#gl_chart_of_account_side_list]] | ผังบัญชีแยกตามหน่วยงาน / Account Side list | 2 |
| [[#gl_design_report]] | สร้างงบการเงิน / Report design | 4 |
| [[#gl_journal]] | ข้อมูลรายวัน / Journal | 32 |
| [[#gl_journal_allocate_list]] | ข้อมูลรายวันแยกตามการจัดสรร / Allocate | 15 |
| [[#gl_journal_book]] | สมุดบัญชี / Journal book | 5 |
| [[#gl_journal_depart_list]] | ข้อมูลรายวันแยกตามแผนก / Department List | 15 |
| [[#gl_journal_detail]] | รายละเอียดเอกสารย่อย / Journal detail | 19 |
| [[#gl_journal_job_list]] | ข้อมูลรายวันแยกตามงาน / Job List | 15 |
| [[#gl_journal_project_list]] | ข้อมูลรายวันแยกตามงาน / Project | 15 |
| [[#gl_journal_side_list]] | ข้อมูลรายวันแยกหน่วยงาน / Journal Side | 15 |
| [[#gl_journal_summary]] | รายการสรุปยอดบัญชี  | 44 |
| [[#gl_journal_summary_detail]] | รายละเอียดการสรุปยอดบัญชี  | 21 |
| [[#gl_journal_vat_buy]] | ภาษีซื้อ / Vat | 44 |
| [[#gl_journal_vat_sale]] | ภาษีขาย / Vat Sale | 40 |
| [[#gl_list_view]] | บัญชีแยกประเภท / gl list view | 16 |
| [[#gl_recurring]] | ข้อมูลไม่จำเป็น / GL Recurring | 3 |
| [[#gl_resource]] | รายละเอียดข้อความ / gl resource | 55 |
| [[#gl_sap_account_code]] | gl_sap_account_code / gl_sap_account_code | 3 |
| [[#gl_summary_close_account_detaiil]] | gl_summary_close_account_detaiil / gl_summary_close_account_detaiil | 6 |
| [[#gl_tax_group]] | กลุ่มภาษี / Tax Group | 6 |
| [[#gl_tax_type]] | ประเภทภาษี / Tax Type | 4 |
| [[#gl_trans]] | รายวันบัญชี / GL Trans | 19 |
| [[#gl_trans_detail]] | รายละเอียดรายวันบัญชี  | 9 |
| [[#gl_wht_list]] | ภาษีหัก ณ. ที่จ่าย / gl_wht_list | 24 |
| [[#gl_wht_list_detail]] | รายละเอียดภาษีหัก ณ ที่จ่าย / WHT List Detail | 15 |

## gl_account_close

**gl_account_close** — gl_account_close

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(20) |  |
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(20) |  |
| `creator_code` | ผู้สร้าง |  | varchar(50) | ✓ |
| `create_datetime` | วันที่สร้าง |  | datetime | ✓ |
| `last_editor_code` | ผู้แก้ไข |  | varchar(50) | ✓ |
| `lastedit_datetime` | วันที่แก้ไข |  | datetime | ✓ |
| `account_year` | ปี |  | smallint | ✓ |
| `account_month` | เดือน |  | smallint | ✓ |
| `account_period` | งวดบัญชี |  | smallint | ✓ |
| `guid_code` | GUID |  | varchar(50) | ✓ |
| `product_balance_amount` | มูลค่าสินค้าต้นงวด |  | float | ✓ |
| `product_next_amount` | มูลค่าซื้อ |  | float | ✓ |
| `purchase_amount` | มูลค่าสินค้าปลายงวด |  | float | ✓ |
| `sale_cost` | ต้นทุนขาย |  | float | ✓ |
| `sale_cost_account` | ผังบัญชีต้นทุนขาย |  | varchar(50) | ✓ |
| `from_date` | จากวันที่ |  | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ |  | smalldatetime | ✓ |
| `gl_entry_type` | วิธีการลงบัญชี |  | smallint | ✓ |
| `entry_normal` | ปรกติ *(resource only)* |  | char |  |
| `entry_compound` | คอมปาว *(resource only)* |  | char |  |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `tab_gl` | GL *(resource only)* |  | char |  |

index: `gl_account_close_pk_doc_no`(doc_no)

## gl_account_close_detail

**รายละเอียการปิดบัญชีสินค้าล** — gl_account_close_detail

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `doc_time` | เวลา |  | varchar(10) |  |
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) |  |
| `ref_doc_type` | ประเภทรายการ |  | smallint | ✓ |
| `account_code` | รหัสบัญชี |  | varchar(50) | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(500) | ✓ |
| `balance_mode` | ด้านบัญชี |  | smallint | ✓ |
| `account_type` | ประเภทบัญชี |  | smallint | ✓ |
| `amount` | มูลค่า |  | float | ✓ |
| `amount_2` | มูลค่า(ลด) |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |

## gl_account_cost

**ประเภทต้นทุน** — Account Cost · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ | Name | varchar(255) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name (English) | varchar(255) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `gl_account_cost_PK_CODE`(code)

## gl_account_group

**กลุ่มบัญชี** — Account group · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อกลุ่ม | Name | varchar(100) | ✓ |
| `name_2` | ชื่อกลุ่ม (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `gl_account_group_PK_CODE`(code)

## gl_account_type

**ประเภทบัญชี** — Account type · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | code | varchar(25) |  |
| `name_1` | ชื่อ | Name | varchar(100) |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) | Name 2 | varchar(100) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `gl_account_type_PK_CODE`(code)

## gl_cash_flow_group

**กลุ่มบัญชีกระแสเงินสด** — Cash flow Group · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อกลุ่ม | Name | varchar(100) | ✓ |
| `name_2` | ชื่อกลุ่ม (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `gl_cash_flow_group_PK_CODE`(code)

## gl_chart_of_account

**ผังบัญชี** — Chart of account · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสบัญชี | Account code | varchar(25) |  |
| `account_level` | ระดับบัญชี | Account level | smallint | ✓ |
| `name_1` | ชื่อบัญชี | Account name | varchar(100) |  |
| `name_2` | ชื่อบัญชี (ภาษาอังกฤษ) | Account name (2) | varchar(100) | ✓ |
| `main_code` | ผังบัญชีหลัก | Account main code | varchar(25) | ✓ |
| `account_group` | กลุ่มบัญชี | Account group code | varchar(25) | ✓ |
| `cash_flow_group` | รหัสบัญชีกระแสเงินสด | Cash flow group | varchar(25) | ✓ |
| `status` | สถานะบัญชี | Account status | smallint | ✓ |
| `account_type` | ประเภทบัญชี | Account type | smallint | ✓ |
| `balance_mode` | ด้านบัญชี | Balance mode | smallint | ✓ |
| `side_status` | แยกหน่วยงาน | Side status | smallint | ✓ |
| `department_status` | แยกแผนก | Department status | smallint | ✓ |
| `allocate_status` | แยกการจัดสรร | Allocate status | smallint | ✓ |
| `project_status` | แยกโครงการ | Project status | smallint | ✓ |
| `job_status` | แยกงาน | Job status | smallint | ✓ |
| `active_status` | ใช้งาน | Active status | smallint | ✓ |
| `account_close` | ปิดเข้าบัญชี | Close account to | varchar(25) | ✓ |
| `work_in_process_status` | งานระหว่างทำ (JOB) | Work in process | smallint | ✓ |
| `balance_sheet_status` | ผลกระทบต่องบการเงิน | Balance sheet effect | smallint | ✓ |
| `tax_type` | เกี่ยวข้องกับภาษี | Tax Releation | smallint | ✓ |
| `none` | ไม่เกี่ยวข้อง *(resource only)* | None | varchar |  |
| `vat_sale` | ภาษีขาย *(resource only)* | Sale Tax | varchar |  |
| `vat_buy` | ภาษีซื้อ *(resource only)* | Buy Tax | varchar |  |
| `wht_in` | หัก ณ. ที่จ่าย *(resource only)* | Wht In | varchar |  |
| `wht_out` | ถูกหัก ณ. ที่จ่าย *(resource only)* | Wht Out | varchar |  |
| `balance_sheet_effect_normal` | ทั่วไป *(resource only)* | Normal | varchar |  |
| `balance_sheet_effect_sale_cost` | ต้นทุนขาย *(resource only)* | Sale Cost | varchar |  |
| `balance_sheet_effect_produce` | การผลิต *(resource only)* | Produce | varchar |  |
| `balance_sheet_effect_expense` | ค่าใช้จ่าย *(resource only)* | Expensed | varchar |  |
| `balance_sheet_effect_non_expense` | ค่าใช้จ่ายที่ไม่รวมเป็นค่าใช้จ่าย *(resource only)* |  | char |  |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `account_level_0` | บัญชีหลัก *(resource only)* | Main Account | varchar |  |
| `account_level_1` | ระดับที่ 1 *(resource only)* | Level 1 | varchar |  |
| `account_level_2` | ระดับที่ 2 *(resource only)* | Level 2 | varchar |  |
| `account_level_3` | ระดับที่ 3 *(resource only)* | Level 3 | varchar |  |
| `account_level_4` | ระดับที่ 4 *(resource only)* | Level 4 | varchar |  |
| `account_level_5` | ระดับที่ 5 *(resource only)* | Level 5 | varchar |  |
| `account_level_6` | ระดับที่ 6 *(resource only)* | Level 6 | varchar |  |
| `account_level_7` | ระดับที่ 7 *(resource only)* | Level 7 | varchar |  |
| `account_status_normal` | บัญชีทั่วไป *(resource only)* | Normal | varchar |  |
| `account_status_main` | บัญชีหลัก *(resource only)* | Main | varchar |  |
| `account_type_asset` | สินทรัพย์ *(resource only)* | Asset | varchar |  |
| `account_type_debt` | หนี้สิน *(resource only)* | Debt | varchar |  |
| `account_type_capital` | ทุน *(resource only)* | Capital | varchar |  |
| `account_type_income` | รายได้ *(resource only)* | Income | varchar |  |
| `account_type_expense` | ค่าใช้จ่าย *(resource only)* | Expense | varchar |  |
| `balance_mode_debit` | เดบิต *(resource only)* | Debit | varchar |  |
| `balance_mode_credit` | เครดิต *(resource only)* | Credit | varchar |  |
| `interco` | INTERCO | INTERCO | varchar(255) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |

index: `gl_chart_of_account_PK_CODE`(code)

## gl_chart_of_account_allocate_list

**ผังบัญชีแยกตามการจัดสรร** — Account Allocate list · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | รหัสผังบัญชี | Account code | varchar(25) |  |
| `allocate_code` | รหัสการจัดสรร | Allocate code | varchar(10) |  |

index: `gl_chart_of_account_allocate_list__pk`(account_code,allocate_code)

## gl_chart_of_account_depart_list

**ผังบัญชีแยกตามแผนก** — Account department list · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | รหัสผังบัญชี | Account code | varchar(25) |  |
| `department_code` | รหัสแผนก | Department code | varchar(25) |  |

index: `gl_chart_of_account_depart_list__pk`(account_code,department_code)

## gl_chart_of_account_job_list

**ผังบัญชีแยกตามงาน** — Account Job list · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | รหัสผังบัญชี | Account code | varchar(25) |  |
| `job_code` | รหัสงาน | Job code | varchar(25) |  |

index: `gl_chart_of_account_job_list__pk`(account_code,job_code)

## gl_chart_of_account_project_list

**ผังบัญชีแยกตามโครงการ** — Account Project list · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | รหัสผังบัญชี | Account code | varchar(25) |  |
| `project_code` | รหัสโครงการ | Project code | varchar(10) |  |

index: `gl_chart_of_account_project_list__pk`(account_code,project_code)

## gl_chart_of_account_side_list

**ผังบัญชีแยกตามหน่วยงาน** — Account Side list · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | รหัสผังบัญชี | Account code | varchar(25) |  |
| `side_code` | รหัสหน่วยงาน | Side code | varchar(25) |  |

index: `gl_chart_of_account_side_list__pk`(account_code,side_code)

## gl_design_report

**สร้างงบการเงิน** — Report design · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name1` | ชื่องบ | Name 1 | varchar(588) | ✓ |
| `name2` | ชื่องบ (อังกฤษ) | Name 2 | varchar(588) | ✓ |
| `data` | ข้อมูล | Data | text | ✓ |

index: `gl_design_report_gl_design_code`(code)

## gl_journal

**ข้อมูลรายวัน** — Journal · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book code | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `ref_no` | เอกสารอ้างอิงเลขที่ | Reference Number | varchar(25) | ✓ |
| `ref_date` | เอกสารอ้างอิงวันที่ | Reference Date | smalldatetime | ✓ |
| `description` | คำอธิบาย | Description | varchar(5000) | ✓ |
| `debit` | ยอดเดบิต | Debit | float | ✓ |
| `credit` | ยอดเครดิต | Credit | float | ✓ |
| `period_number` | อยู่ในงวด | Period Number | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน | Journal Type | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `clear_screen_after_save` | ล้างหน้าจอหลังการบันทึกข้อมูล *(resource only)* | Clear Screen After Save | varchar |  |
| `auto_running_doc_number` | เลขที่เอกสารอัตโนมัติ *(resource only)* | Auto Document Number | varchar |  |
| `daily` | ข้อมูลรายวัน *(resource only)* | Dialy Data | varchar |  |
| `balance_period` | ยอดยกมา *(resource only)* | Brought forword | varchar |  |
| `close_period` | ปิดบัญชี *(resource only)* | Close | varchar |  |
| `adjust_account` | ปรับปรุงรายการ(ต้นงวด) *(resource only)* | Account Adjust | char |  |
| `carry_forword` | ยอดยกไป *(resource only)* | Carry forword | char |  |
| `ap_ar_code` | รหัสเจ้าหนี้/ลูกหนี้ | AP AR Code | varchar(20) | ✓ |
| `ap_ar_originate_from` | มาจากหน้าจอ | AP AR Originate From | varchar(255) | ✓ |
| `doc_code` | รหัสหน้าจอ |  | varchar(25) | ✓ |
| `trans_flag` | ประเภทเอกสาร |  | int | ✓ |
| `amount` | มูลค่า *(resource only)* | Amount | char |  |
| `remark` | หมายเหตุ *(resource only)* | Remark | char |  |
| `is_pass` | สถานะผ่านรายการ |  | smallint | ✓ |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `trans_direct` | บันทึกรายการบัญชีตรง |  | smallint | ✓ |
| `trans_format` | รูปแบบการเชื่อม *(resource only)* |  | char |  |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `account_year` | ปีบัญชี | Financial Year | tinyint | ✓ |
| `account_period` | งวดบัญชี *(resource only)* | Financial Month | char |  |
| `create_code` | ผู้สร้าง | Create Code | varchar(25) | ✓ |

index: `gl_journal_pk_code`(doc_date,book_code,doc_no,trans_flag), `pk_gl_journal_is_pass`(is_pass), `pk_gl_journal_doc_no`(doc_no), `pk_gl_journal_doc_date`(doc_date), `idx_gl_journal_trans_direct`(trans_direct)

## gl_journal_allocate_list

**ข้อมูลรายวันแยกตามการจัดสรร** — Allocate · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | tinyint |  |
| `line_number_detail` | เลขที่บรรทัด | Line Number | tinyint |  |
| `allocate_code` | รหัสจัดสรร | Allocate Code | varchar(25) | ✓ |
| `allocate_name` | ชื่อจัดสรร | Allocate Name | varchar(100) | ✓ |
| `allocate_persent` | เปอร์เซ็นต์ | Persent | float | ✓ |
| `allocate_amount` | มูลค่า | Amount | float | ✓ |
| `account_code` | รหัสบัญชี | Account Code | varchar(25) | ✓ |
| `period_number` | งวด | Period | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | trans_flag |  | smallint | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(100) | ✓ |
| `account_year` | ปีภาษี |  | tinyint | ✓ |

index: `gl_journal_allocate_list__pk`(doc_date,book_code,doc_no,line_number,line_number_detail)

## gl_journal_book

**สมุดบัญชี** — Journal book · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) |  |
| `name_1` | ชื่อ | Name | varchar(100) |  |
| `name_2` | ชือ (ภาษาอังกฤษ) | Name (2) | varchar(100) | ✓ |
| `word_begin` | ตัวอักษรนำหน้า | Word begin | varchar(25) | ✓ |
| `guid_code` | GUID | guid | varchar(35) | ✓ |

index: `gl_journal_book_PK_CODE`(code)

## gl_journal_depart_list

**ข้อมูลรายวันแยกตามแผนก** — Department List · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | int |  |
| `line_number_detail` | เลขที่บรรทัด | Line Number | int |  |
| `department_code` | รหัสแผนก | Department Code | varchar(25) | ✓ |
| `department_name` | ชื่อแผนก | Department Name | varchar(100) | ✓ |
| `allocate_persent` | เปอร์เซ็นต์ | Persent | float | ✓ |
| `allocate_amount` | มูลค่า | Amount | float | ✓ |
| `account_code` | รหัสบัญชี | Account Code | varchar(25) | ✓ |
| `period_number` | งวด | Period | smallint | ✓ |
| `journal_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | trans_flag |  | smallint | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(100) | ✓ |
| `account_year` | ปีภาษี |  | smallint | ✓ |

index: `gl_journal_depart_list__pk`(doc_date,book_code,doc_no,line_number,line_number_detail)

## gl_journal_detail

**รายละเอียดเอกสารย่อย** — Journal detail · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | tinyint | ✓ |
| `account_code` | รหัสบัญชี | Account Code | varchar(25) |  |
| `account_name` | ชื่อบัญชี | Account Name | varchar(100) | ✓ |
| `description` | รายละเอียด | Description | varchar(5000) | ✓ |
| `credit` | เครดิต | Credit | float | ✓ |
| `debit` | เดบิต | Debit | float | ✓ |
| `period_number` | งวด | Period Number | tinyint | ✓ |
| `debit_or_credit` | 0=Debit,1=Credit | 0=Debit,1=Credit | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน | Journal Type | smallint | ✓ |
| `difference_debit_credit` | ผลต่างระหว่างยอดเดบิตหักยอดเครดิต *(resource only)* | Differance Debit and Credit | varchar(255) |  |
| `amount` | มูลค่า *(resource only)* | Amount | char |  |
| `dimension` | มิติ *(resource only)* | Dime | char |  |
| `trans_flag` | trand_flag |  | int | ✓ |
| `is_pass` | สถานะผ่านรายการ |  | smallint | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `account_year` | ปีบัญชี |  | tinyint | ✓ |

index: `pk_gl_journal_detail_is_pass`(is_pass), `pk_gl_journal_detail_doc_date`(doc_date), `pk_gl_journal_detail_doc_no`(doc_no), `pk_gl_journal_detail_account_code_doc_date`(account_code,doc_date), `pk_gl_journal_detail_account_code`(account_code)

## gl_journal_job_list

**ข้อมูลรายวันแยกตามงาน** — Job List · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | tinyint |  |
| `line_number_detail` | เลขที่บรรทัด | Line Number | tinyint |  |
| `job_code` | รหัสงาน | Side Code | varchar(25) | ✓ |
| `job_name` | ชื่องาน | Side Name | varchar(100) | ✓ |
| `allocate_persent` | เปอร์เซ็นต์ | Persent | float | ✓ |
| `allocate_amount` | มูลค่า | Amount | float | ✓ |
| `account_code` | รหัสบัญชี | Account Code | varchar(25) | ✓ |
| `period_number` | งวด | Period | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | trans_flag |  | smallint | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(100) | ✓ |
| `account_year` | ปีบัญชี |  | tinyint | ✓ |

index: `gl_journal_job_list__pk`(doc_date,book_code,doc_no,line_number,line_number_detail)

## gl_journal_project_list

**ข้อมูลรายวันแยกตามงาน** — Project · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | tinyint |  |
| `line_number_detail` | เลขที่บรรทัด | Line Number | tinyint |  |
| `project_code` | รหัสโครงการ | Project Code | varchar(25) | ✓ |
| `project_name` | ชื่อโครงการ | Project Name | varchar(100) | ✓ |
| `allocate_persent` | เปอร์เซ็นต์ | Persent | float | ✓ |
| `allocate_amount` | มูลค่า | Amount | float | ✓ |
| `account_code` | รหัสบัญชี | Account code | varchar(25) | ✓ |
| `period_number` | งวด | Period | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | trans_flag |  | smallint | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(100) | ✓ |
| `account_year` | ปีภาษี |  | tinyint | ✓ |

index: `gl_journal_project_list__pk`(doc_date,book_code,doc_no,line_number,line_number_detail)

## gl_journal_side_list

**ข้อมูลรายวันแยกหน่วยงาน** — Journal Side · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime |  |
| `book_code` | สมุดรายวัน | Book Number | varchar(25) |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `line_number` | เลขที่บรรทัด | Line Number | tinyint |  |
| `line_number_detail` | เลขที่บรรทัด | Line Number | tinyint |  |
| `side_code` | รหัสหน่วยงาน | Side Code | varchar(25) |  |
| `side_name` | ชื่อหน่วยงาน | Side Name | varchar(100) | ✓ |
| `allocate_persent` | เปอร์เซ็นต์ | Persent | float | ✓ |
| `allocate_amount` | มูลค่า | Amount | float | ✓ |
| `account_code` | รหัสบัญชี | Account code | varchar(25) | ✓ |
| `period_number` | งวด | Period | tinyint | ✓ |
| `journal_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | trans_flag |  | smallint | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(100) | ✓ |
| `account_year` | ปีบัญชี |  | tinyint | ✓ |

index: `gl_journal_side_list__pk`(doc_date,book_code,doc_no,line_number,line_number_detail)

## gl_journal_summary

**รายการสรุปยอดบัญชี**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `guid_code` | GUID |  | varchar(55) | ✓ |
| `account_year` | ปีบัญชี |  | smallint | ✓ |
| `account_month` | เดือนบัญชี |  | smallint | ✓ |
| `account_period` | งวดบัญชี |  | smallint | ✓ |
| `from_date` | จากวันที่ |  | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ |  | smalldatetime | ✓ |
| `total_debit` | Debit |  | float | ✓ |
| `total_credit` | Credit |  | float | ✓ |
| `creator_code` | ผู้สร้าง |  | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้าง |  | datetime | ✓ |
| `last_editor_code` | ผู้แก้ไขล่าสุด |  | varchar(255) | ✓ |
| `lastedit_datetime` | วันที่แก้ไขล่าสุด |  | datetime | ✓ |
| `doc_format_code` | รหัสเอกสาร |  | varchar(50) | ✓ |
| `doc_type` | ประเภทเอกสาร |  | smallint | ✓ |
| `doc_type_summary` | สรุปยอดบัญชี *(resource only)* |  | char |  |
| `doc_type_balance` | สรุปยอดยกมา *(resource only)* |  | char |  |
| `book_code` | สมุดบัญชี |  | varchar(25) | ✓ |
| `process_from_date` | จากวันที่ |  | smalldatetime | ✓ |
| `process_to_date` | ถึงวันที่ |  | smalldatetime | ✓ |
| `close_account_type_1` | รายการปิดบัญชี |  | smallint | ✓ |
| `close_account_type_2` | รายการปิดบัญชี |  | smallint | ✓ |
| `close_account_type_3` | รายการปิดบัญชี |  | smallint | ✓ |
| `close_account_type_4` | รายการปิดบัญชี |  | smallint | ✓ |
| `close_account_type_5` | รายการปิดบัญชี |  | smallint | ✓ |
| `close_from_account_1` | ผังบัญชี |  | varchar(255) | ✓ |
| `close_from_account_2` | ผังบัญชี |  | varchar(255) | ✓ |
| `close_from_account_3` | ผังบัญชี |  | varchar(255) | ✓ |
| `close_from_account_4` | ผังบัญชี |  | varchar(255) | ✓ |
| `close_from_account_5` | ผังบัญชี |  | varchar(255) | ✓ |
| `close_to_account_1` | ปิดเข้าบัญชี |  | varchar(255) | ✓ |
| `close_to_account_2` | ปิดเข้าบัญชี |  | varchar(255) | ✓ |
| `close_to_account_3` | ปิดเข้าบัญชี |  | varchar(255) | ✓ |
| `close_to_account_4` | ปิดเข้าบัญชี |  | varchar(255) | ✓ |
| `close_to_account_5` | ปิดเข้าบัญชี |  | varchar(255) | ✓ |
| `close_account_type` | รายการปิดบัญชี *(resource only)* |  | char |  |
| `close_account_code` | ผังบัญชี *(resource only)* |  | char |  |
| `product_final_balance` | รายการสินค้าปลายงวด *(resource only)* |  | char |  |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `close_all_balance` | สรุปยอดรวมรายการยกมา |  | smallint | ✓ |
| `income_expense` | รายได้/ค่าใช้จ่าย *(resource only)* |  | char |  |
| `have_product_balance_first` | บันทึกสินค้าต้นงวด |  | smallint | ✓ |

index: `gl_journal_summary_PK_doc_no`(doc_no)

## gl_journal_summary_detail

**รายละเอียดการสรุปยอดบัญชี**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(50) |  |
| `doc_date` | เอกสารวันที่ |  | smalldatetime |  |
| `line_number` | Line Number |  | smallint | ✓ |
| `account_code` | รหัสผังบัญชี |  | varchar(255) | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(255) | ✓ |
| `balance_debit` | เดบิต |  | float | ✓ |
| `balance_credit` | เครดิต |  | float | ✓ |
| `debit_amount` | เดบิต |  | float | ✓ |
| `credit_amount` | เครดิต |  | float | ✓ |
| `adjust_debit` | เดบิต |  | float | ✓ |
| `adjust_credit` | เครดิต |  | float | ✓ |
| `total_debit` | เดบิต |  | float | ✓ |
| `total_credit` | เครดิต |  | float | ✓ |
| `balance_summery` | ยอดยกมา *(resource only)* |  | char |  |
| `period_summery` | ยอดประจำงวด *(resource only)* |  | char |  |
| `adjust_summary` | ยอดปรับปรุง *(resource only)* |  | char |  |
| `total_summary` | ยอดรวม *(resource only)* |  | char |  |
| `balance_mode` | ด้านบัญชี |  | smallint | ✓ |
| `period_debit` | เดบิต *(resource only)* |  | char |  |
| `period_credit` | เครดิต *(resource only)* |  | char |  |
| `close_summary` | ยอดปิดบัญชี *(resource only)* |  | char |  |

## gl_journal_vat_buy

**ภาษีซื้อ** — Vat

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่รายวัน | Document Date | smalldatetime |  |
| `doc_no` | เลขที่เอกสารรายวัน | Document Number | varchar(25) |  |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) |  |
| `line_number` | บรรทัด | Line Number | tinyint | ✓ |
| `vat_date` | วันที่ | Date | smalldatetime |  |
| `vat_new_number` | เลขที่ออกใหม่ | New Number | varchar(25) | ✓ |
| `vat_doc_no` | เลขที่ใบกำกับ | Tax Number | varchar(25) |  |
| `vat_group` | กลุ่มภาษี | Vat Group | varchar(25) | ✓ |
| `vat_description` | รายละเอียด | Desctiption | varchar(255) | ✓ |
| `vat_base_amount` | ฐานภาษี | Base Amount | float | ✓ |
| `vat_rate` | อัตราภาษี | Vat Rate | float | ✓ |
| `vat_total_amount` | ยอดรวม | Amount | float | ✓ |
| `vat_type` | ประเภทภาษี | Tax Type | tinyint | ✓ |
| `vat_amount` | เงินภาษี | Vat Amount | float | ✓ |
| `vat_except_amount_1` | ยอดยกเว้น | Vat Except Amount | float | ✓ |
| `vat_claim_amount` | เครม | Claim | float | ✓ |
| `vat_average` | เฉลี่ยภาษี | Vat Average | int | ✓ |
| `vat_effective_period` | เดือนภาษี | Vat Period | tinyint | ✓ |
| `vat_claim_rate` | เครม % | Claim % | float | ✓ |
| `is_add` | ยื่นเพิ่มเติม |  | smallint | ✓ |
| `vat_normal` | ปรกติ *(resource only)* |  | char |  |
| `vat_no_return` | ขอคืนไม่ได้ *(resource only)* |  | char |  |
| `vat_out_due` | ไม่ถึงกำหนดชำระ *(resource only)* |  | char |  |
| `trans_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | ประเภทระบบ |  | smallint | ✓ |
| `ap_code` | รหัสเจ้าหนี้ |  | varchar(25) | ✓ |
| `ap_name` | ชื่อผู้ขายสินค้า/ผู้ให้บริการ |  | varchar(255) | ✓ |
| `vat_calc` | มีค่าบวกหรือลบ |  | smallint | ✓ |
| `total` | รวมทั้งสิ้น *(resource only)* |  | char |  |
| `vat_count` | ลำดับ *(resource only)* |  | char |  |
| `total_amount` | มูลค่าสินค้า/บริการ *(resource only)* |  | char |  |
| `total_vat` | จำนวนเงินภาษี *(resource only)* |  | char |  |
| `vat_effective_year` | ปีภาษี |  | smallint | ✓ |
| `doc_status` | สถานะ *(resource only)* |  | char |  |
| `ref_vat_no` | ใบกำกับภาษีอ้างอิงเลขที่ |  | varchar(25) | ✓ |
| `ref_vat_date` | ใบกำกับภาษีอ้างอิงวันที่ |  | smalldatetime | ✓ |
| `ref_doc_no` | เลขที่เอกสารอ้างอิง |  | varchar(25) | ✓ |
| `ref_doc_date` | วันที่เอกสารอ้างอิง |  | smalldatetime | ✓ |
| `tax_no` | เลขประจำตัวผู้เสียภาษี |  | varchar(25) | ✓ |
| `branch_type` | สถานประกอบการ |  | smallint | ✓ |
| `headquarters` | สำนักงานใหญ่ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `branch_code` | เลขที่สาขา |  | varchar(25) | ✓ |
| `manual_add` | เพิ่มเอง |  | smallint | ✓ |

index: `PK_ap_code_tax_no`(ap_code,vat_doc_no,vat_calc), `gl_journal_vat_buy_eff_per`(vat_effective_period), `gl_journal_vat_buy_eff_year`(vat_effective_year), `gl_journal_vat_buy_doc_no_trans_flag`(doc_no,trans_flag)

## gl_journal_vat_sale

**ภาษีขาย** — Vat Sale · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่รายวัน | Document Date | smalldatetime |  |
| `doc_no` | เอกสารเลขที่ | Document Number | varchar(25) |  |
| `book_code` | สมุดรายวัน | Book Code | varchar(25) |  |
| `line_number` | บรรทัด | Line Number | tinyint | ✓ |
| `vat_number` | เลขที่ใบกำกับภาษี | Vat Number | varchar(25) |  |
| `tax_group` | กลุ่มภาษี | Tax Group | varchar(25) | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `base_caltax_amount` | ฐานภาษี | Base Amount | float | ✓ |
| `tax_rate` | อัตราภาษี | Rate | float | ✓ |
| `amount` | ยอดภาษี | Amount | float | ✓ |
| `except_tax_amount` | ยอดยกเว้นภาษี | Except Amount | float | ✓ |
| `period_number` | เดือนภาษี | Period Number | tinyint | ✓ |
| `is_add` | ยื่นเพิ่มเติม |  | smallint | ✓ |
| `vat_date` | วันที่ใบกำกับภาษี |  | smalldatetime | ✓ |
| `trans_type` | ประเภทรายวัน |  | smallint | ✓ |
| `trans_flag` | ประเภทระบบ |  | smallint | ✓ |
| `vat_effective_period` | มีผลงวดที่ |  | smallint | ✓ |
| `vat_count` | ลำดับ *(resource only)* |  | char |  |
| `ar_code` | รหัสลูกหนี้ |  | varchar(25) | ✓ |
| `ar_name` | ชื่อผู้ซื้อสินค้า/ผู้รับบริการ |  | varchar(255) | ✓ |
| `total_amount` | มูลค่าสินค้า/บริการ *(resource only)* |  | char |  |
| `total_vat` | จำนวนเงินภาษี *(resource only)* |  | char |  |
| `vat_calc` | มีค่าบวกหรือลบ |  | smallint | ✓ |
| `total` | รวมทั้งสิ้น *(resource only)* |  | char |  |
| `vat_effective_year` | ปีภาษี |  | tinyint | ✓ |
| `doc_status` | สถานะ *(resource only)* |  | char |  |
| `branch_type` | สถานประกอบการ |  | smallint | ✓ |
| `headquarters` | สำนักงานใหญ่ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `branch_code` | ลำดับที่สาขา |  | varchar(25) | ✓ |
| `tax_no` | เลขประจำตัวผู้เสียภาษี |  | varchar(25) | ✓ |
| `manual_add` | เพิ่มเอง |  | smallint | ✓ |
| `is_doc_copy` | เป็นเอกสารออกแทน |  | smallint | ✓ |
| `vat_type` | ประเภทภาษี |  | smallint | ✓ |
| `vat_normal` | ปรกติ *(resource only)* |  | char |  |
| `vat_out_due` | ไม่ถึงกำหนดชำระ *(resource only)* |  | char |  |
| `ref_vat_no` | อ้างอิงใบกำกับ |  | varchar(25) | ✓ |
| `ref_vat_date` | อ้างอิงวันที่ใบกำกับ |  | smalldatetime | ✓ |
| `ref_doc_no` | อ้างอิงเลขที่เอกสาร |  | varchar(25) | ✓ |
| `ref_doc_date` | อ้างอิงวันที่เอกสาร |  | smalldatetime | ✓ |

index: `gl_journal_vat_sale_eff_period`(vat_effective_period), `gl_journal_vat_sale_vat_date`(vat_date), `gl_journal_vat_sale_eff_year`(vat_effective_year), `gl_journal_vat_sale_doc_no_trans_flag_idx`(doc_no,trans_flag)

## gl_list_view

**บัญชีแยกประเภท** — gl list view · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `account_code` | เลขที่บัญชี *(resource only)* | Account code | varchar(25) |  |
| `journal_date` | วันที่ *(resource only)* | Date | smalldatetime |  |
| `journal_doc_no` | เอกสารเลขที่ *(resource only)* | Doc No | varchar(25) |  |
| `journal_description` | รายละเอียด *(resource only)* | Description | varchar(255) |  |
| `period_number` | ประจำงวด *(resource only)* | Period | int |  |
| `debit` | เดบิต *(resource only)* | Debit | float |  |
| `credit` | เครดิต *(resource only)* | Credit | float |  |
| `balance` | ยอดคงเหลือ *(resource only)* | Balance | float |  |
| `book_code` | รหัสสมุดรายวัน *(resource only)* | Book Code | varchar(100) |  |
| `account_name` | ชื่อบัญชี *(resource only)* | Account name | varchar(100) |  |
| `account_status` | สถานะบัญชี *(resource only)* | Account Status | int |  |
| `account_level` | ระดับบัญชี *(resource only)* | Account Level | int |  |
| `prev_debit` | เดบิต *(resource only)* | Debit | int |  |
| `prev_credit` | เครดิต *(resource only)* | Credit | int |  |
| `balance_debit` | เดบิต *(resource only)* | Debit | int |  |
| `balance_credit` | เครดิต *(resource only)* | Credit | int |  |

## gl_recurring

**ข้อมูลไม่จำเป็น** — GL Recurring · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(50) |  |
| `gl_desc` | รายละเอียด | GL Description | varchar(255) | ✓ |
| `xmlstring` | ชุดข้อมูล | XML String | varchar(5000) | ✓ |

index: `gl_recurring_PK_CODE`(code)

## gl_resource

**รายละเอียดข้อความ** — gl resource · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `date_begin` | วันที่เริ่มต้น *(resource only)* | Date begin | char |  |
| `date_end` | วันที่สิ้นสุด *(resource only)* | Date end | char |  |
| `account_code` | เลขที่บัญชี *(resource only)* | Account Code | char |  |
| `period` | ประจำงวด *(resource only)* | Period number | char |  |
| `all_data_check` | แสดงรายการทั้งหมด *(resource only)* | All Record | char |  |
| `debit_credit` | แสดงยอดสุทธิ *(resource only)* | Debit-Credit | char |  |
| `doc_begin` | เอกสารเริ่มต้น *(resource only)* | Doc Number Begin | char |  |
| `doc_end` | เอกสารสิ้นสุด *(resource only)* | Doc Number End | char |  |
| `book_select` | เลือกสมุดรายวัน *(resource only)* | Select Book | char |  |
| `sort_by_date` | เรียงตามวันที่ *(resource only)* | Sort by Date | char |  |
| `sort_by_doc_no` | เรียงตามเลขที่เอกสาร *(resource only)* | Sort by Doc Number | char |  |
| `total_end_date` | แสดงยอดรวมระหว่างวัน *(resource only)* | Total end Date | char |  |
| `select_all_account` | ต้องการแสดงทุกผังบัญชี *(resource only)* | All Account | char |  |
| `select_account_balance` | ต้องการแสดงยอดสุทธิ *(resource only)* | Balance | char |  |
| `select_account_adj` | ต้องการแสดงยอดปรับปรุง *(resource only)* | Adjust | char |  |
| `sort_by` | ต้องการเรียงข้อมูลแบบใด *(resource only)* | Sort By | char |  |
| `sort_order_by_doc_no` | เรียงตามเลขที่เอกสาร *(resource only)* | Order By Doc Number | char |  |
| `sort_order_by_doc_date` | เรียงตามวันที่เอกสาร *(resource only)* | Order By Doc Date | char |  |
| `account_code_begin` | เริ่มจากบัญชีเลขที่ *(resource only)* | Account code begin | char |  |
| `account_code_end` | ถึงบัญชีเลขที่ *(resource only)* | Account code end | char |  |
| `code` | รหัส *(resource only)* | Code | char |  |
| `name_1` | ชื่อ *(resource only)* | Name | char |  |
| `name_2` | ชื่อ (ภาษาอังกฤษ) *(resource only)* | Name (English) | char |  |
| `check` | เลือก *(resource only)* | Check | char |  |
| `side` | หน่วยงาน *(resource only)* | Side | char |  |
| `department` | แผนก *(resource only)* | Department | char |  |
| `project` | โครงการ *(resource only)* | Project | char |  |
| `allocate` | จัดสรร *(resource only)* | Allocate | char |  |
| `job` | งาน *(resource only)* | Job | char |  |
| `select_code` | เลือกรหัส *(resource only)* | Select code | char |  |
| `change_account_code_to` | เปลี่ยนเป็นรหัส *(resource only)* | Change to code | char |  |
| `check_name` | หัวข้อตรวจสอบ *(resource only)* | Check name | char |  |
| `check_desc` | รายละเอียด *(resource only)* | Check result | char |  |
| `clear_doc_all` | ล้างข้อมูลทั้งหมดเพื่อโอนใหม่ (ตามประเภทรายวัน) *(resource only)* | Clear Data | char |  |
| `is_pass` | ผ่านรายการแล้ว *(resource only)* |  | char |  |
| `tab_template` | รูปแบบรายงาน *(resource only)* | Template | char |  |
| `tab_journal` | รายวัน *(resource only)* | Journal | char |  |
| `book_code` | สมุดบัญชี *(resource only)* | Book Code | char |  |
| `account_name` | ชื่อบัญชี *(resource only)* |  | char |  |
| `period_1` | ช่วงที่ 1 *(resource only)* |  | char |  |
| `period_2` | ช่วงที่ 2 *(resource only)* |  | char |  |
| `period_3` | ช่วงที่ 3 *(resource only)* |  | char |  |
| `period_4` | ช่วงที่ 4 *(resource only)* |  | char |  |
| `period_5` | ช่วงที่ 5 *(resource only)* |  | char |  |
| `period_6` | ช่วงที่ 6 *(resource only)* |  | char |  |
| `period_7` | ช่วงที่ 7 *(resource only)* |  | char |  |
| `period_8` | ช่วงที่ 8 *(resource only)* |  | char |  |
| `period_9` | ช่วงที่ 9 *(resource only)* |  | char |  |
| `period_10` | ช่วงที่ 10 *(resource only)* |  | char |  |
| `period_11` | ช่วงที่ 11 *(resource only)* |  | char |  |
| `period_12` | ช่วงที่ 12 *(resource only)* |  | char |  |
| `except_close_account` | ไม่รวมรายการปิดบัญชี *(resource only)* |  | char |  |
| `include_cutoff` | รวมรายการปิดบัญชี *(resource only)* | Include cut off | char |  |
| `include_carry_forword` | รวมรายการยกไป *(resource only)* | Include carry forword | char |  |
| `show_total_main_account` | แสดงยอดรวมผังบัญชีหลัก *(resource only)* | Show total main account | char |  |

## gl_sap_account_code

**gl_sap_account_code** — gl_sap_account_code

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | code | code | varchar(255) | ✓ |
| `sap_code` | sap_code | sap_code | varchar(255) | ✓ |
| `guid_code` | guid_code | guid_code | varchar(35) | ✓ |

## gl_summary_close_account_detaiil

**gl_summary_close_account_detaiil** — gl_summary_close_account_detaiil

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_no` | เอกสารเลขที่ |  | varchar(255) |  |
| `account_code` | รหัสบัญชี |  | varchar(255) |  |
| `account_name` | ชื่อบัญชี *(resource only)* |  | char |  |
| `amount` | มูลค่าปลายงวด |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `balance_frist_amount` | มูลค่าสินค้าต้นงวด |  | float | ✓ |

## gl_tax_group

**กลุ่มภาษี** — Tax Group

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสกลุ่ม | Code | varchar(25) |  |
| `name_1` | ชื่อกลุ่ม | Name | varchar(100) |  |
| `name_2` | ชื่อกลุ่ม (ภาษาอังกฤษ) | Name (English) | varchar(100) | ✓ |
| `tax_rate` | อัตราภาษี | Tax Rate | float | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `guid_code` | GUID | GUID | varchar(35) | ✓ |

## gl_tax_type

**ประเภทภาษี** — Tax Type · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสประเภท | Tax Type Code | varchar(25) |  |
| `name_1` | ชื่อประเภท | Tax Type Name | varchar(100) |  |
| `name_2` | ชื่อประเภท (ภาษาอังกฤษ) | Tax Type Name (English) | varchar(100) | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |

index: `gl_tax_type_PK_CODE`(code)

## gl_trans

**รายวันบัญชี** — GL Trans

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `doc_format_code` | รหัสเอกสาร |  | varchar(25) | ✓ |
| `from_date` | จากวันที่ |  | smalldatetime | ✓ |
| `to_date` | ถึงวันที่ |  | smalldatetime | ✓ |
| `account_period` | งวดบัญชี |  | smallint | ✓ |
| `account_year` | ปีบัญชี |  | smallint | ✓ |
| `branch_code` | สาขา |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(500) | ✓ |
| `book_code` | สมุดรายวัน |  | varchar(25) | ✓ |
| `close_to_account` | ปิดเข้าบัญชี |  | varchar(25) | ✓ |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `tab_gl` | GL *(resource only)* |  | char |  |
| `doc_time` | เวลา |  | varchar(10) | ✓ |
| `guid_code` | GUID |  | varchar(50) | ✓ |
| `close_account_type` | รายการปิดบัญชี *(resource only)* |  | char |  |
| `close_account_code` | ผังบัญชี *(resource only)* |  | char |  |
| `product_final_balance` | รายการสินค้าปลายงวด *(resource only)* |  | char |  |

index: `gl_trans_gl_trans_pk_doc_no_trans_flag`(doc_no,trans_flag)

## gl_trans_detail

**รายละเอียดรายวันบัญชี**

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | วันที่เอกสาร |  | smalldatetime |  |
| `doc_no` | เลขที่เอกสาร |  | varchar(25) |  |
| `trans_flag` | ประเภทรายวัน |  | smallint |  |
| `account_code` | รหัสบัญชี |  | varchar(25) | ✓ |
| `account_name` | ชื่อบัญชี |  | varchar(255) | ✓ |
| `debit` | เดบิต |  | float | ✓ |
| `credit` | เครดิต |  | float | ✓ |
| `line_number` | Line Number |  | smallint | ✓ |
| `amount` | มูลค่า *(resource only)* |  | char |  |

## gl_wht_list

**ภาษีหัก ณ. ที่จ่าย** — gl_wht_list

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime | ✓ |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) | ✓ |
| `amount` | จำนวนเงิน | Amount | float | ✓ |
| `tax_value` | มูลค่าภาษีหัก ณ ที่จ่าย | Tax Value | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `trans_flag` | เอกสารต้นทาง |  | smallint | ✓ |
| `due_date` | วันที่หัก ณ ที่จ่าย |  | smalldatetime | ✓ |
| `line_number` | บรรทัดที่ |  | int | ✓ |
| `cust_code` | รหัสลูกหนี้/เจ้าหนี้ |  | varchar(35) | ✓ |
| `ap_code` | เจ้าหนี้ *(resource only)* |  | char |  |
| `ar_code` | ลูกหนี้ *(resource only)* |  | char |  |
| `due_month` | เดือนที่ยื่นภาษี *(resource only)* |  | smallint |  |
| `due_year` | ปีที่ยื่นภาษี *(resource only)* |  | smallint |  |
| `card_number` | เลขที่บัตรประชาชน |  | varchar(50) | ✓ |
| `tax_number` | เลขประจำตัวผู้เสียภาษี |  | varchar(50) | ✓ |
| `cust_tax_type` | ประเภท |  | smallint | ✓ |
| `cust_name` | ชื่อ |  | varchar(255) | ✓ |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `ar_name` | ชื่อลูกหนี้ *(resource only)* |  | char |  |
| `tax_doc_no` | เอกสารเลขที่ |  | varchar(25) |  |
| `object` | object *(resource only)* |  | char |  |
| `cust_address` | ที่อยู่ |  | varchar(1000) | ✓ |
| `juristic_person` | นิติบุคคบล *(resource only)* |  | char |  |
| `personality` | บุคคลธรรมดา *(resource only)* |  | char |  |

index: `gl_wht_list_gl_wht_list_doc_no`(tax_doc_no), `gl_wht_list_doc_no_trans_flag_idx`(doc_no,trans_flag)

## gl_wht_list_detail

**รายละเอียดภาษีหัก ณ ที่จ่าย** — WHT List Detail · edition: `SMLGL+SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `doc_date` | เอกสารวันที่ | Document Date | smalldatetime | ✓ |
| `doc_no` | เอกสารเลขที่ | Document No | varchar(25) | ✓ |
| `income_type` | รายละเอียด | Income Type | varchar(100) | ✓ |
| `tax_rate` | อัตราภาษี | Tax Rate | float | ✓ |
| `amount` | ฐานภาษี | Amount | float | ✓ |
| `tax_value` | ภาษีหัก ณ ที่จ่าย | Tax Value | float | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `trans_flag` | เอกสารต้นทาง |  | smallint | ✓ |
| `due_date` | วันที่ยื่น |  | smalldatetime | ✓ |
| `line_number` | บรรทัดที่ |  | int | ✓ |
| `cust_code` | รหัสลูกหนี้/เจ้าหนี้ |  | varchar(35) | ✓ |
| `ap_code` | เจ้าหนี้ *(resource only)* |  | char |  |
| `ar_code` | ลูกหนี้ *(resource only)* |  | char |  |
| `sum_amount` | ยอดสุทธิ |  | float | ✓ |
| `tax_doc_no` | เอกสารเลขที่ |  | varchar(25) | ✓ |

index: `gl_wht_list_detail_doc_no_trans_flag_idx`(doc_no,trans_flag)

