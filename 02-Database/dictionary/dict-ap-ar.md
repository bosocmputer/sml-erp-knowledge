---
tags: [sml, dictionary, ap-ar, generated]
module: AP_AR
---
# พจนานุกรม: AP_AR — ลูกหนี้/เจ้าหนี้

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#ap_ar_transport_label]] | ที่อยู่จัดส่ง / Transport Label | 48 |
| [[#ap_contactor]] | ผู้ติดต่อ (เจ้าหนี้) / Contactor | 10 |
| [[#ap_item_by_supplier]] | สินค้าตามผู้จำหน่าย / Item by Supplier | 5 |
| [[#ap_supplier]] | เจ้าหนี้ / Supplier | 60 |
| [[#ap_supplier_connected]] | คู่ค้า / Supplier Connected | 8 |
| [[#ap_supplier_detail]] | รายละเอียดเจ้าหนี้ / Supplier Detail | 57 |
| [[#ar_channel]] | Channel / Channel | 4 |
| [[#ar_contactor]] | ผู้ติดต่อ (ลูกหนี้) / Contactor | 17 |
| [[#ar_credit_group_detail]] | กลุ่มวงเงินเครดิตลูกหนี้ / Credit Group Detail | 4 |
| [[#ar_customer]] | ลูกหนี้ / customer | 111 |
| [[#ar_customer_cashier_list]] | พนักงานเก็บเงินตามลูกค้า / AR Customer Chshier Lists | 4 |
| [[#ar_customer_connected]] | รายละเอียดคู่ค้า(ลูกหนี้) / AR Customer Connected | 5 |
| [[#ar_customer_detail]] | รายละเอียดลูกหนี้ / Customer Detail | 158 |
| [[#ar_dealer]] | รายละเอียดสมาชิก / Dealer | 39 |
| [[#ar_equipment]] | Equipment / Equipment | 4 |
| [[#ar_item_by_customer]] | สินค้าตามลูกค้า / Item by Customer | 5 |
| [[#ar_location_type]] | สถานที่ตั้ง / Ar Location | 4 |
| [[#ar_project]] | Ar Project / Ar Project | 5 |
| [[#ar_shoptype1]] | AR Shoptype1 / AR Shoptype1 | 5 |
| [[#ar_shoptype2]] | AR Shoptype2 / AR Shoptype2 | 5 |
| [[#ar_shoptype3]] | AR Shoptype3 / AR Shoptype3 | 5 |
| [[#ar_shoptype4]] | AR Shoptype4 / AR Shoptype4 | 5 |
| [[#ar_shoptype5]] | AR Shoptype5 / AR Shoptype5 | 5 |
| [[#ar_shoptype6]] | AR Shoptype6 / AR Shoptype6 | 5 |
| [[#ar_shoptype7]] | AR Shoptype7 / AR Shoptype7 | 5 |
| [[#ar_sub_equipment]] | Sub Equipment / Sub Equipment | 4 |
| [[#ar_sub_type_1]] | Sub Type 1 / Sub Type 1 | 4 |
| [[#ar_vehicle]] | Vehicle / Vehicle | 4 |
| [[#customer_type]] | Type / Type | 5 |
| [[#sub_ar_shoptype5]] | Sub AR Shoptype5 / Sub AR Shoptype5 | 6 |

## ap_ar_transport_label

**ที่อยู่จัดส่ง** — Transport Label

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `cust_code` | รหัสเจ้าหนี้/ลูกหนี้ |  | varchar(50) |  |
| `name_1` | ชื่อผู้รับ |  | varchar(255) |  |
| `address` | ที่อยู่ |  | varchar(255) | ✓ |
| `telephone` | โทรศัพท์ |  | varchar(255) | ✓ |
| `fax` | แฟกซ์ |  | varchar(255) | ✓ |
| `email` | อีเมลล์ |  | varchar(255) | ✓ |
| `guid_code` | GUID |  | varchar(35) | ✓ |
| `ar_ap_type` | AR AP Type |  | smallint | ✓ |
| `ar_name` | ชื่อลูกค้า/ลูกหนี้ *(resource only)* |  | char |  |
| `ap_name` | ชื่อเจ้าหนี้ *(resource only)* |  | char |  |
| `receivename` | ชื่อผู้รับ *(resource only)* |  | char |  |
| `label_count` | จำนวนดวง *(resource only)* |  | char |  |
| `home_address` | บ้านเลขที่ | Address | varchar(255) | ✓ |
| `home_name` | หมู่บ้าน |  | varchar(255) | ✓ |
| `moo` | หมู่ |  | varchar(25) | ✓ |
| `soi` | ซอย |  | varchar(255) | ✓ |
| `road` | ถนน |  | varchar(255) | ✓ |
| `tambon` | ตำบล |  | varchar(25) | ✓ |
| `amper` | อำเภอ |  | varchar(25) | ✓ |
| `province` | จังหวัด |  | varchar(25) | ✓ |
| `zip_code` | รหัสไปรษณีย์ |  | varchar(10) | ✓ |
| `room_no` | ห้อง | Room | varchar(50) | ✓ |
| `floor` | ชั้น |  | varchar(25) | ✓ |
| `building` | อาคาร |  | varchar(50) | ✓ |
| `tab_main` | ทั่วไป *(resource only)* |  | char |  |
| `tab_detail` | รายละเอียด *(resource only)* |  | char |  |
| `home_phone` | เบอร์บ้าน | Phone Home | varchar(50) | ✓ |
| `mobile1` | โทรศัพท์มือถือ 1 | Mobile Phone 1 | varchar(50) | ✓ |
| `mobile2` | โทรศัพท์มือถือ 2 | Mobile Phone 2 | varchar(50) | ✓ |
| `transport_type` | ประเภทการขนส่ง |  | varchar(25) | ✓ |
| `tab_receive` | การรับสินค้า *(resource only)* |  | char |  |
| `receive_day` | วันเปิดทำการ | Day Opening | varchar(255) | ✓ |
| `time_period` | ช่วงเวลา | Distance | varchar(100) | ✓ |
| `remark_1` | หมายเหตุ 1 | Remark 1 | varchar(255) | ✓ |
| `remark_2` | หมายเหตุ 2 | Remark 2 | varchar(255) | ✓ |
| `country` | ประเทศ |  | varchar(255) | ✓ |
| `ship_code` | Ship Code |  | varchar(50) | ✓ |
| `branch_type` | สถานประกอบการ |  | smallint | ✓ |
| `headquarters` | สำนักงานใหญ่ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `branch_code` | เลขที่สาขา |  | varchar(25) | ✓ |
| `tax_id` | เลขประจำตัวผู้เสียภาษี | Tax ID | varchar(50) | ✓ |
| `logistic_area` | เขตการขนส่ง |  | varchar(50) | ✓ |
| `latitude` | ละติจูด | Latitude | float | ✓ |
| `longitude` | ลองจิจูด | Longitude | float | ✓ |
| `from_label` | จากดวงที่ *(resource only)* |  | char |  |
| `box_count` | จำนวนทั้งหมด *(resource only)* |  | char |  |
| `ship_code_ref` | ship code ref | ship code ref | varchar(255) | ✓ |

## ap_contactor

**ผู้ติดต่อ (เจ้าหนี้)** — Contactor

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_code` | รหัสเจ้าหนี้ | AP Code | varchar(25) |  |
| `name` | ชื่อผู้ติดต่อ | Name | varchar(100) | ✓ |
| `address` | ที่อยู่ | Address | varchar(255) | ✓ |
| `telephone` | หมายเลขโทรศัพท์ | Telephone | varchar(50) | ✓ |
| `mobile` | โทรศัพท์มือถือ | Mobile Phone | varchar(50) | ✓ |
| `email` | อีเมล์ | Email | varchar(50) | ✓ |
| `work_title` | ตำแหน่งงาน | Work Title | varchar(100) | ✓ |
| `work_department` | แผนก | Work Department | varchar(100) | ✓ |
| `officer_group` | กลุ่มพนักงาน | Officer Group | varchar(25) | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_item_by_supplier

**สินค้าตามผู้จำหน่าย** — Item by Supplier

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_code` | รหัสเจ้าหนี้ | Supplier Code | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ap_supplier

**เจ้าหนี้** — Supplier · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | AP Code | varchar(25) |  |
| `code_old` | รหัสเก่า | AP Code Old | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 | AP Name 1 | varchar(100) | ✓ |
| `name_2` | ชื่อ 2 | AP Name 2 | varchar(100) | ✓ |
| `name_eng_1` | ชื่อ (ภาษาอังกฤษ) 1 | AP Name (English) 1 | varchar(100) | ✓ |
| `name_eng_2` | ชื่อ (ภาษาอังกฤษ) 2 | AP Name (English) 2 | varchar(100) | ✓ |
| `prefixname` | คำนำหน้า | Prefix Name | varchar(50) | ✓ |
| `firstname` | ชื่อ | First Name | varchar(255) | ✓ |
| `lastname` | นามสกุล | Last Name | varchar(255) | ✓ |
| `address` | ที่อยู่ | Address | varchar(255) | ✓ |
| `address_eng` | ที่อยู่ (ภาษาอังกฤษ) | Address (English) | varchar(255) | ✓ |
| `tambon` | ตำบล/แขวง | Tambon | varchar(25) | ✓ |
| `amper` | อำเภอ/เขต | Amper | varchar(25) | ✓ |
| `province` | จังหวัด | Province | varchar(25) | ✓ |
| `zip_code` | รหัสไปรษณีย์ | Zip Code | varchar(10) | ✓ |
| `telephone` | หมายเลขโทรศัพท์ | Telephone | varchar(150) | ✓ |
| `fax` | หมายเลขโทรสาร | Fax | varchar(50) | ✓ |
| `email` | อีเมล์ | Email | varchar(255) | ✓ |
| `website` | เวบไซด์ | Website | varchar(255) | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `ap_type` | ประเภทเจ้าหนี้ | AP Type | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | AP Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `tab_detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `tab_credit` | เครดิต *(resource only)* | Credit | char |  |
| `tab_paybill` | การจ่ายเงิน *(resource only)* | Paybill | char |  |
| `tab_dimension` | มิติ *(resource only)* | Dimension | char |  |
| `tab_contact` | ติดต่ออ้างอิง *(resource only)* | Contact Detail | char |  |
| `tab_item` | สินค้า *(resource only)* | Item | char |  |
| `tab_logistic_area` | สถานที่ส่งสินค้า *(resource only)* | Logistic Area | char |  |
| `tab_credit_group` | กลุ่มเครดิต *(resource only)* | Credit Group | char |  |
| `debt_balance` | ยอดคงเหลือ | Balance | float | ✓ |
| `chq_balance` | ยอดเช็ครอขึ้นเงิน | Chq Banalce | float | ✓ |
| `bill_balance` | ยอดรับวางบิลรอจ่าย | Bill Balance | float | ✓ |
| `active` | ใช้งาน *(resource only)* | Active | char |  |
| `inactive` | ไม่ใช้งาน *(resource only)* | Inactive | char |  |
| `tab_image` | รูปภาพ *(resource only)* | Image | char |  |
| `ap_status` | ชนิดเจ้าหนี้ | AP Status | smallint | ✓ |
| `juristic_person` | นิติบุคคล *(resource only)* | Juristic Person | char |  |
| `personality` | บุคคลธรรมดา *(resource only)* | Personality | char |  |
| `doc_format_code` | รหัสเอกสาร | Doc Format Code | varchar(25) | ✓ |
| `tab_ap_master` | รายละเอียดหลัก *(resource only)* | Master | char |  |
| `tab_ap_detail` | รายละเอียดเพิ่มเติม *(resource only)* | Detail | char |  |
| `country` | ประเทศ |  | varchar(255) | ✓ |
| `card_id` | เลขที่บัตรประชาชน *(resource only)* | Card ID | char |  |
| `tax_id` | เลขประจำตัวผู้เสียภาษี *(resource only)* | Tax ID | char |  |
| `branch_type` | สถานประกอบการ *(resource only)* | Branch Type | char |  |
| `headquarters` | สำนักงานใหญ่ *(resource only)* | Headquarters | char |  |
| `branch` | สาขา *(resource only)* | Branch | char |  |
| `branch_code` | เลขที่สาขา *(resource only)* | Branch Code | char |  |
| `interco` | INTERCO | INTERCO | varchar(255) | ✓ |
| `create_datetime` | วันที่สร้าง | Create date time | datetime | ✓ |
| `last_update_date_time` | วันที่แก้ไขล่าสุด | Last update date time | datetime | ✓ |
| `create_code` | ผู้สร้าง | Create Code | varchar(50) | ✓ |
| `last_update_code` | ผู้แก้ไขล่าสุด | Last update code | varchar(50) | ✓ |
| `use_partners` | ใช้ระบบคู่ค้า | Partners | smallint | ✓ |
| `ap_web_service` | web service url | WEB Service URL | varchar(255) | ✓ |
| `ap_database_name` | ชื่อฐานข้อมูล | Database Name | varchar(255) | ✓ |
| `use_ar_code` | รหัสลูกนี้ที่ใช้กับคู่ค้า | Customer Code | varchar(255) | ✓ |

index: `ap_supplier_PK_CODE`(code), `pk_ap_supplier_dept_balance`(debt_balance)

## ap_supplier_connected

**คู่ค้า** — Supplier Connected

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(255) | ✓ |
| `ap_code` | รหัสผู้จำหน่าย | Supplier Code | varchar(255) | ✓ |
| `ap_web_service` | Web Service URL | Web Service URL | varchar(255) | ✓ |
| `ap_database_name` | ชื่อฐานข้อมูลคู่ค้า | Database Name | varchar(255) | ✓ |
| `use_ar_code` | รหัสลูกนี้ที่ใช้กับคู่ค้า | Customer Code | varchar(255) | ✓ |
| `guid_code` | guid code | guid code | varchar(35) | ✓ |
| `ap_provider` | รหัสผู้ให้บริการคู่ค้า | Provider | varchar(255) | ✓ |
| `start_date` | วันที่เริ่มใช้งาน | Start date | smalldatetime | ✓ |

## ap_supplier_detail

**รายละเอียดเจ้าหนี้** — Supplier Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ap_code` | รหัสผู้จำหน่าย | Supplier Code | varchar(25) |  |
| `staff_pay_code` | พนักงานเตรียมจ่าย | Staff Pay Code | varchar(25) | ✓ |
| `payment_way` | ช่องทางการจ่ายเงิน | Payment Way | varchar(255) | ✓ |
| `pay_bill_way` | ช่องทางการวางบิล | Pay Bill Way | varchar(25) | ✓ |
| `pay_condition` | เงิ่อนไขการจ่ายเงิน | Pay Condition | varchar(255) | ✓ |
| `credit_purchase` | เครดิตซื้อ | Credit Purchase | smallint | ✓ |
| `credit_code` | รหัสเครดิต | Credit Code | varchar(25) | ✓ |
| `form_name` | ชื่อฟอร์มรายเจ้าหนี้ | Form Name | varchar(255) | ✓ |
| `discount_item` | ส่วนลดต่อรายการ | Discount Item Rate | varchar(50) | ✓ |
| `discount_bill` | ส่วนลดท้ายบิล | Discount Bill Rate | varchar(50) | ✓ |
| `credit_day` | จำนวนวันเครดิต | Credit Day | int | ✓ |
| `trade_license` | ทะเบียนการค้า | Trade License | varchar(50) | ✓ |
| `tax_id` | เลขประจำตัวผู้เสียภาษี | Tax ID | varchar(50) | ✓ |
| `tax_type` | ประเภทภาษี | Tax Type | varchar(25) | ✓ |
| `tax_rate` | อัตราภาษี | Tax Rate | float | ✓ |
| `account_code` | บัญชีเจ้าหนี้รายตัว | Account Code | varchar(25) | ✓ |
| `shipping_type` | ประเภทการส่งมอบ | Shipping Type | varchar(25) | ✓ |
| `close_reason` | เหตุผลในการปิด | Close Reasonable | varchar(255) | ✓ |
| `close_date` | วันที่ปิด | Close Date | smalldatetime | ✓ |
| `group_main` | กลุ่มหลัก | Group Main | varchar(25) | ✓ |
| `group_sub_1` | กลุ่มย่อย 1 | Group Sub 1 | varchar(25) | ✓ |
| `group_sub_2` | กลุ่มย่อย 2 | Group Sub 2 | varchar(25) | ✓ |
| `group_sub_3` | กลุ่มย่อย 3 | Group Sub 3 | varchar(25) | ✓ |
| `group_sub_4` | กลุ่มย่อย 4 | Group Sub 4 | varchar(25) | ✓ |
| `picture_1` | รูปภาพ 1 | Picture 1 | varchar(255) | ✓ |
| `picture_2` | รูปภาพ 2 | Picture 2 | varchar(255) | ✓ |
| `picture_3` | รูปภาพ 3 | Picture 3 | varchar(255) | ✓ |
| `picture_4` | รูปภาพ 4 | Picture 4 | varchar(255) | ✓ |
| `ref_doc_1` | เอกสารอ้างอิง 1 | Reference Document 1 | varchar(255) | ✓ |
| `ref_doc_2` | เอกสารอ้างอิง 2 | Reference Document 2 | varchar(255) | ✓ |
| `ref_doc_3` | เอกสารอ้างอิง 3 | Reference Document 3 | varchar(255) | ✓ |
| `dimension_1` | มิติ 1 | Dimension 1 | varchar(100) | ✓ |
| `dimension_2` | มิติ 2 | Dimension 2 | varchar(100) | ✓ |
| `dimension_3` | มิติ 3 | Dimension 3 | varchar(100) | ✓ |
| `dimension_4` | มิติ 4 | Dimension 4 | varchar(100) | ✓ |
| `dimension_5` | มิติ 5 | Diemnsion 5 | varchar(100) | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(25) | ✓ |
| `tax_out` | ภาษีแยกนอก *(resource only)* | Ext Tax | char |  |
| `tax_in` | ภาษีรวมใน *(resource only)* | Inc Tax | char |  |
| `tax_zero` | ภาษีอัตราศูนย์ *(resource only)* | No Tax | char |  |
| `prepaid_money` | เงินล่วงหน้า *(resource only)* | Prepaid Money | char |  |
| `deposit_money` | มูลค่าเงินมัดจำ *(resource only)* | Deposit Money | char |  |
| `deposit_value` | จำนวนเงินมัดจำ *(resource only)* | Deposit Value | char |  |
| `card_id` | เลขที่บัตรประชาชน |  | varchar(50) | ✓ |
| `passbook_code` | สมุดเงินฝาก | Pass Book Code | varchar(25) | ✓ |
| `set_tax_type` | ระบุประเภทภาษี | Specify category TAX | smallint | ✓ |
| `branch_type` | สถานประกอบการ |  | smallint | ✓ |
| `headquarters` | สำนักงานใหญ่ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `branch_code` | เลขที่สาขา |  | varchar(25) | ✓ |
| `dimension_6` | มิติ 6 |  | varchar(255) | ✓ |
| `dimension_7` | มิติ 7 |  | varchar(255) | ✓ |
| `dimension_8` | มิติ 8 |  | varchar(255) | ✓ |
| `dimension_9` | มิติ 9 |  | varchar(255) | ✓ |
| `dimension_10` | มิติ 10 |  | varchar(255) | ✓ |
| `lead_time` | ระยะเวลาสั่งสินค้า |  | smallint | ✓ |
| `is_vendor_approved` | เป็นผู้ขายที่ได้รับการอนุมัติแล้ว | Vendor Approved | smallint | ✓ |

index: `ap_supplier_detail_PK_CODE`(ap_code)

## ar_channel

**Channel** — Channel

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Channel Code | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 | Channel Name | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 | Channel Name 2 | varchar(255) | ✓ |
| `guid_code` | guid_code | guid_code | varchar(35) | ✓ |

## ar_contactor

**ผู้ติดต่อ (ลูกหนี้)** — Contactor · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า | Customer Code | varchar(25) |  |
| `name` | ชื่อผู้ติดต่อ | Name | varchar(100) | ✓ |
| `address` | ที่อยู่ | Address | varchar(255) | ✓ |
| `telephone` | หมายเลขโทรศัพท์ | Telephone | varchar(50) | ✓ |
| `mobile` | โทรศัพท์มือถือ | Mobile Phone | varchar(50) | ✓ |
| `email` | อีเมล์ | Email | varchar(50) | ✓ |
| `work_title` | ตำแหน่งงาน | Work Title | varchar(100) | ✓ |
| `work_department` | แผนก | Work Department | varchar(100) | ✓ |
| `officer_group` | กลุ่มพนักงาน | Officer Group | varchar(25) | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |
| `group_contactor` | กลุ่ม | Group | varchar(25) | ✓ |
| `remark_1` | หมายเหตุ 1 | Remark 1 | varchar(255) | ✓ |
| `remark_2` | หมายเหตุ 2 | Remark 2 | varchar(255) | ✓ |
| `remark_3` | หมายเหตุ 3 | Remark 3 | varchar(255) | ✓ |
| `remark_4` | หมายเหตุ 4 | Remark 4 | varchar(255) | ✓ |
| `remark_5` | หมายเหตุ 5 | Remark 5 | varchar(255) | ✓ |
| `remark_6` | หมายเหตุ 6 | Remark 6 | varchar(255) | ✓ |

## ar_credit_group_detail

**กลุ่มวงเงินเครดิตลูกหนี้** — Credit Group Detail · edition: `ALL`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า | Customer Code | varchar(25) |  |
| `credit_group` | กลุ่มวงเงินเครดิต | Credit Group | varchar(25) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ar_customer

**ลูกหนี้** — customer · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Customer Code | varchar(25) |  |
| `code_old` | รหัสเก่า | Customer Code Old | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 | Customer Name 1 | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 | Customer Name 2 | varchar(255) | ✓ |
| `name_eng_1` | ชื่อ (ภาษาอังกฤษ) 1 | Customer Name (English) 1 | varchar(255) | ✓ |
| `name_eng_2` | ชื่อ (ภาษาอังกฤษ) 2 | Customer Name (English) 2 | varchar(255) | ✓ |
| `address` | ที่อยู่ | Address | varchar(255) | ✓ |
| `address_eng` | ที่อยู่ (ภาษาอังกฤษ) | Address (English) | varchar(255) | ✓ |
| `tambon` | ตำบล/แขวง | Tambon | varchar(25) | ✓ |
| `amper` | อำเภอ/เขต | Amper | varchar(25) | ✓ |
| `province` | จังหวัด | Province | varchar(25) | ✓ |
| `zip_code` | รหัสไปรษณีย์ | Zipcode | varchar(10) | ✓ |
| `telephone` | หมายเลขโทรศัพท์ | Telephone | varchar(150) | ✓ |
| `fax` | หมายเลขโทรสาร | Fax | varchar(50) | ✓ |
| `email` | อีเมล์ | Eamil | varchar(150) | ✓ |
| `website` | เวบไซด์ | WebSite | varchar(150) | ✓ |
| `description` | รายละเอียด | Description | varchar(255) | ✓ |
| `birth_day` | วันเกิด/วันที่จดทะเบียน | Birth Day/Regist Date | smalldatetime | ✓ |
| `ar_type` | ประเภทลูกหนี้ | Customer Type | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Customer Status | smallint | ✓ |
| `guid_code` | GUID | guid_code | varchar(35) | ✓ |
| `active` | ใช้งาน *(resource only)* | Active | char |  |
| `inactive` | ไม่ใช้งาน *(resource only)* | Inactive | char |  |
| `close_credit` | ปิด *(resource only)* | Close | char |  |
| `open_credit` | เปิด *(resource only)* | Open | char |  |
| `stop_credit` | ปิด(ชั่วคราว) *(resource only)* | Stop | char |  |
| `tab_detail` | รายละเอียด *(resource only)* | Detail | char |  |
| `tab_credit` | เครดิต *(resource only)* | Credit | char |  |
| `tab_paybill` | การจ่ายเงิน *(resource only)* | Paybill | char |  |
| `tab_dimension` | มิติ *(resource only)* | Dimension | char |  |
| `tab_contact` | ติดต่ออ้างอิง *(resource only)* | Contact Detail | char |  |
| `tab_item` | สินค้า *(resource only)* | Item | char |  |
| `tab_logistic_area` | สถานที่ส่งสินค้า *(resource only)* | Logistic Area | char |  |
| `tab_credit_group` | กลุ่มเครดิต *(resource only)* | Credit Group | char |  |
| `tab_image` | รูปภาพ *(resource only)* | Image | char |  |
| `ar_status` | ชนิดลูกค้า | AR Status | smallint | ✓ |
| `juristic_person` | นิติบุคคล *(resource only)* | Juristic Person | char |  |
| `personality` | บุคคลธรรมดา *(resource only)* | Personality | char |  |
| `doc_format_code` | รหัสเอกสาร | Doc Format Code | varchar(25) | ✓ |
| `group_main` | กลุ่มหลัก *(resource only)* |  | char |  |
| `prefixname` | คำนำหน้า |  | varchar(15) | ✓ |
| `first_name` | ชื่อ |  | varchar(50) | ✓ |
| `last_name` | นามสกุล |  | varchar(70) | ✓ |
| `tab_ar_main` | รายละเอียดหลัก *(resource only)* |  | char |  |
| `tab_ar_detail` | รายละเอียดเพิ่มเติม *(resource only)* |  | char |  |
| `price_level` | ระดับราคาขาย |  | smallint | ✓ |
| `price_level_0` | ราคากลาง *(resource only)* |  | char |  |
| `price_level_1` | ราคาที่ 1 *(resource only)* |  | char |  |
| `price_level_2` | ราคาที่ 2 *(resource only)* |  | char |  |
| `price_level_3` | ราคาที่ 3 *(resource only)* |  | char |  |
| `price_level_4` | ราคาที่ 4 *(resource only)* |  | char |  |
| `price_level_5` | ราคาที่ 5 *(resource only)* |  | char |  |
| `price_level_6` | ราคาที่ 6 *(resource only)* |  | char |  |
| `price_level_7` | ราคาที่ 7 *(resource only)* |  | char |  |
| `price_level_8` | ราคาที่ 8 *(resource only)* |  | char |  |
| `price_level_9` | ราคาที่ 9 *(resource only)* |  | char |  |
| `point_balance` | แต้มสะสม |  | float | ✓ |
| `sale_shift_id` | รอบการขาย |  | varchar(50) | ✓ |
| `sms_phonenumber` | หมายเลข SMS | Number SMS | varchar(10) | ✓ |
| `home_address` | บ้านเลขที่ |  | varchar(255) | ✓ |
| `home_name` | หมู่บ้าน |  | varchar(255) | ✓ |
| `moo` | หมู่ |  | varchar(25) | ✓ |
| `soi` | ซอย |  | varchar(255) | ✓ |
| `road` | ถนน |  | varchar(255) | ✓ |
| `room_no` | ห้อง |  | varchar(50) | ✓ |
| `floor` | ชั้น |  | varchar(25) | ✓ |
| `building` | อาคาร |  | varchar(50) | ✓ |
| `sex` | เพศ |  | smallint | ✓ |
| `sex_male` | ชาย *(resource only)* |  | char |  |
| `sex_female` | หญิง *(resource only)* |  | char |  |
| `country` | ประเทศ |  | varchar(255) | ✓ |
| `register_date` | วันลงทะเบียน | Register Date | smalldatetime | ✓ |
| `card_id` | เลขที่บัตรประชาชน *(resource only)* | Card ID | varchar(100) |  |
| `tax_id` | เลขประจำตัวผู้เสียภาษี *(resource only)* | Tax ID | varchar(50) |  |
| `branch_type` | สถานประกอบการ *(resource only)* | Branch Type | smallint |  |
| `headquarters` | สำนักงานใหญ่ *(resource only)* | HeadQueaters | char |  |
| `branch` | สาขา *(resource only)* | Branch | char |  |
| `branch_code` | เลขที่สาขา *(resource only)* | Branch Code | varchar(25) |  |
| `arm_code` | รหัสสมาชิก | ARM Code | varchar(25) | ✓ |
| `ar_code_main` | รหัสลูกค้าหลัก | Main Code | varchar(50) | ✓ |
| `ar_branch_code` | ใช้เฉพาะสาขา |  | varchar(50) | ✓ |
| `arm_approve` | อนุมัติโครงการ |  | smallint | ✓ |
| `arm_approve_date` | วันที่อนุมัติ ARM Code |  | smalldatetime | ✓ |
| `nfc_id` | NFC ID |  | varchar(255) | ✓ |
| `arm_tier` | Tier | Tier | smallint | ✓ |
| `tier_0` | None *(resource only)* | None | char |  |
| `tier_1` | Silver *(resource only)* | Silver | char |  |
| `tier_2` | Gold *(resource only)* | Gold | char |  |
| `tier_3` | Platinum *(resource only)* | Platinum | char |  |
| `tier_4` | Diamond *(resource only)* | Diamond | char |  |
| `last_update_time` | วันเวลาทีแก้ไขล่าสุด | Last Update Time | datetime | ✓ |
| `interco` | INTERCO | INTERCO | varchar(255) | ✓ |
| `tab_ar_picture` | รูปภาพ *(resource only)* |  | char |  |
| `tab_certificate_book` | หนังสือรับรองบริษัท *(resource only)* |  | char |  |
| `tab_pp20` | ภ.พ.20 *(resource only)* |  | char |  |
| `tab_Identity_card` | บัตรประจำตัวประชาชน *(resource only)* |  | char |  |
| `tab_liquor_license` | ใบอนุญาตขายสุรา *(resource only)* |  | char |  |
| `tab_other_picture1` | อื่นๆ 1 *(resource only)* |  | char |  |
| `tab_other_picture2` | อื่นๆ 2 *(resource only)* |  | char |  |
| `tab_customer` | รายละเอียดสมาชิก *(resource only)* |  | char |  |
| `arm_register_date` | วันที่สมัคร ARM Code |  | smalldatetime | ✓ |
| `arm_register` | สมัคร อาร์ม | Register | smallint | ✓ |
| `create_datetime` | วันที่สร้าง | Create date time | datetime | ✓ |
| `last_update_date_time` | วันที่แก้ไขล่าสุด | Last update date time | datetime | ✓ |
| `create_code` | ผู้สร้าง | Create code | varchar(50) | ✓ |
| `last_update_code` | ผู้แก้ไขล่าสุด | Last update code | varchar(50) | ✓ |
| `cis` | CIS | CIS | varchar(255) | ✓ |
| `code_ref1` | code ref1 | code ref1 | varchar(255) | ✓ |
| `tab_cashier` | พนักงานเก็บเงิน *(resource only)* | Cashier | char |  |
| `ar_tier_code` | Tier | Tier | varchar(25) | ✓ |

index: `ar_customer_PK_CODE`(code), `ar_customer_tambon`(tambon), `ar_customer_amper`(amper), `ar_customer_province`(province)

## ar_customer_cashier_list

**พนักงานเก็บเงินตามลูกค้า** — AR Customer Chshier Lists

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | ลูกค้า |  | varchar(50) |  |
| `sale_code` | รหัสพนักงาน |  | varchar(255) |  |
| `sale_name` | ชื่อพนักงาน *(resource only)* |  | char |  |
| `line_number` | บรรทัด |  | smallint |  |

index: `ar_customer_cashier_list_ar_customer_cashier_list_pk`(ar_code,sale_code)

## ar_customer_connected

**รายละเอียดคู่ค้า(ลูกหนี้)** — AR Customer Connected

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกหนี้ |  | varchar(255) |  |
| `ar_webservice_name` | Web Service URL |  | varchar(255) | ✓ |
| `ar_provider_code` | รหัสผู้ให้บริการ |  | varchar(100) | ✓ |
| `ar_database_name` | ชื่อฐานข้อมูล |  | varchar(100) | ✓ |
| `guid_code` | GUID |  | varchar(50) | ✓ |

index: `ar_customer_connected_ar_customer_connected_pk`(ar_code)

## ar_customer_detail

**รายละเอียดลูกหนี้** — Customer Detail · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า | Customer Code | varchar(25) |  |
| `area_code` | เขตการขาย | Sale Area Code | varchar(25) | ✓ |
| `sale_code` | รหัสพนักงานขาย | Sale Code | varchar(25) | ✓ |
| `logistic_area` | เขตการขนส่ง | Logistic Area | varchar(25) | ✓ |
| `pay_bill_code` | รหัสวางบิล | Pay Bill Code | varchar(25) | ✓ |
| `keep_chq_code` | รหัสเก็บเช็ค | Keep Chq Code | varchar(25) | ✓ |
| `pay_bill_date` | วางบิลได้ทุกวันที่ | Pay Bill Date | smallint | ✓ |
| `keep_chq_date` | เก็บเช็คได้ทุกวันที่ | Keep Chq Date | smallint | ✓ |
| `sale_price_level` | ระดับราคาขาย | Sale Price Level | smallint | ✓ |
| `credit_sale` | ขายเครดิต | Credit Sale | smallint | ✓ |
| `credit_code` | รหัสเครดิต | Credit Code | varchar(25) | ✓ |
| `form_name` | ชื่อฟอร์มรายลูกค้า | Form Name | varchar(255) | ✓ |
| `pay_bill_condition` | เงื่อนไขการวางบิล | Pay Bill Condition | varchar(25) | ✓ |
| `keep_money_condition` | เงื่อนไขการเก็บเงิน | Keep Money Condition | varchar(25) | ✓ |
| `payment_person` | กลุ่มพนักงานวางบิล | Payment Person Group | varchar(25) | ✓ |
| `credit_person` | กลุ่มพนักงานสินเชื่อ | Credit Person Group | varchar(25) | ✓ |
| `keep_money_person` | กลุ่มพนักงานเก็บเงิน | Keep Money Person Group | varchar(25) | ✓ |
| `discount_item` | ส่วนลดต่อรายการ | Discount Item Rate | varchar(50) | ✓ |
| `discount_bill` | ส่วนลดท้ายบิล | Discount Bill Rate | varchar(50) | ✓ |
| `credit_group` | ใช้วงเงินกลุ่ม | Credit Group | smallint | ✓ |
| `credit_group_code` | รหัสกลุ่มวงเงิน | Credit Group Code | varchar(25) | ✓ |
| `credit_money` | วงเงินเครดิต | Credit Money | float | ✓ |
| `credit_money_max` | วงเงินเครดิตสูงสุด | Credit Money Max | float | ✓ |
| `credit_day` | จำนวนวันเครดิต | Credit Day | int | ✓ |
| `credit_reason` | เหตุผลลงเครดิต | Credit Reason | varchar(25) | ✓ |
| `credit_status` | สถานะเครดิต | Credit Status | smallint | ✓ |
| `credit_date` | วันที่ลงสถานะเครดิต | Credit Post Date | smalldatetime | ✓ |
| `credit_status_reason` | เหตุผลลงสถานะเครดิต | Credit Status Reason | varchar(25) | ✓ |
| `trade_license` | ทะเบียนการค้า | Trade License | varchar(50) | ✓ |
| `vat_license` | ทะเบียนภาษีมูลค่าเพิ่ม | Vat License | varchar(50) | ✓ |
| `tax_id` | เลขประจำตัวผู้เสียภาษี | Tax ID | varchar(50) | ✓ |
| `tax_type` | ประเภทภาษี | Tax Type | smallint | ✓ |
| `tax_rate` | อัตราภาษี | Tax Rate | float | ✓ |
| `account_code` | บัญชีลูกค้ารายตัว | Account Code | varchar(25) | ✓ |
| `shipping_type` | ประเภทการส่งมอบ | Shipping Type | smallint | ✓ |
| `close_reason` | เหตุผลในการปิด | Close Reasonable | varchar(255) | ✓ |
| `close_date` | วันที่ปิด | Close Date | smalldatetime | ✓ |
| `group_main` | กลุ่มหลัก | Group Main | varchar(25) | ✓ |
| `group_sub_1` | กลุ่มย่อย 1 | Group Sub 1 | varchar(25) | ✓ |
| `group_sub_2` | กลุ่มย่อย 2 | Group Sub 2 | varchar(25) | ✓ |
| `group_sub_3` | กลุ่มย่อย 3 | Group Sub 3 | varchar(25) | ✓ |
| `group_sub_4` | กลุ่มย่อย 4 | Group Sub 4 | varchar(25) | ✓ |
| `picture_3` | รูปภาพ 3 | Picture 3 | varchar(255) | ✓ |
| `picture_4` | รูปภาพ 4 | Picture 4 | varchar(255) | ✓ |
| `ref_doc_1` | เอกสารอ้างอิง 1 | Reference Document 1 | varchar(255) | ✓ |
| `ref_doc_2` | เอกสารอ้างอิง 2 | Reference Document 2 | varchar(255) | ✓ |
| `ref_doc_3` | เอกสารอ้างอิง 3 | Reference Document 3 | varchar(255) | ✓ |
| `dimension_1` | มิติ 1 | Dimension 1 | varchar(100) | ✓ |
| `dimension_2` | มิติ 2 | Dimension 2 | varchar(100) | ✓ |
| `dimension_3` | มิติ 3 | Dimension 3 | varchar(100) | ✓ |
| `dimension_4` | มิติ 4 | Dimension 4 | varchar(100) | ✓ |
| `dimension_5` | มิติ 5 | Dimension 5 | varchar(100) | ✓ |
| `currency_code` | รหัสสกุลเงิน | Currency Code | varchar(20) | ✓ |
| `latitude` | ละติจูด | Latitude | float | ✓ |
| `longitude` | ลองจิจูด | Longitude | float | ✓ |
| `close_credit` | ปิด *(resource only)* | Close | char |  |
| `open_credit` | เปิด *(resource only)* | Open | char |  |
| `stop_credit` | ปิด(ชั่วคราว) *(resource only)* | Stop | char |  |
| `to_be_responsible` | รับเอง *(resource only)* | To be Responsoble | char |  |
| `to_support` | ส่งให้ *(resource only)* | To Support | char |  |
| `other` | อื่นๆ *(resource only)* | Other | char |  |
| `zero_vat` | ภาษีอัตราศูนย์ *(resource only)* |  | char |  |
| `excise_vat` | ภาษีกรมสรรพสามิต *(resource only)* |  | char |  |
| `exc_vat` | ยกเว้นภาษี *(resource only)* |  | char |  |
| `normal_vat` | ภาษีมูลค่าเพิ่ม *(resource only)* |  | char |  |
| `01` | 01 *(resource only)* | 01 | char |  |
| `02` | 02 *(resource only)* | 02 | char |  |
| `03` | 03 *(resource only)* | 03 | char |  |
| `04` | 04 *(resource only)* | 04 | char |  |
| `05` | 05 *(resource only)* | 05 | char |  |
| `06` | 06 *(resource only)* | 06 | char |  |
| `07` | 07 *(resource only)* | 07 | char |  |
| `08` | 08 *(resource only)* | 08 | char |  |
| `09` | 09 *(resource only)* | 09 | char |  |
| `10` | 10 *(resource only)* | 10 | char |  |
| `11` | 11 *(resource only)* | 11 | char |  |
| `12` | 12 *(resource only)* | 12 | char |  |
| `13` | 13 *(resource only)* | 13 | char |  |
| `14` | 14 *(resource only)* | 14 | char |  |
| `15` | 15 *(resource only)* | 15 | char |  |
| `16` | 16 *(resource only)* | 16 | char |  |
| `17` | 17 *(resource only)* | 17 | char |  |
| `18` | 18 *(resource only)* | 18 | char |  |
| `19` | 19 *(resource only)* | 19 | char |  |
| `20` | 20 *(resource only)* | 20 | char |  |
| `21` | 21 *(resource only)* | 21 | char |  |
| `22` | 22 *(resource only)* | 22 | char |  |
| `23` | 23 *(resource only)* | 23 | char |  |
| `24` | 24 *(resource only)* | 24 | char |  |
| `25` | 25 *(resource only)* | 25 | char |  |
| `26` | 26 *(resource only)* | 26 | char |  |
| `27` | 27 *(resource only)* | 27 | char |  |
| `28` | 28 *(resource only)* | 28 | char |  |
| `tax_out` | ภาษีแยกนอก *(resource only)* | Ext Tax | char |  |
| `tax_in` | ภาษีรวมใน *(resource only)* | Inc Tax | char |  |
| `tax_zero` | ภาษีอัตราศูนย์ *(resource only)* | No Tax | char |  |
| `card_id` | เลขที่บัตรประชาชน |  | varchar(100) | ✓ |
| `passbook_code` | สมุดเงินฝาก | Pass Book Code | varchar(25) | ✓ |
| `set_tax_type` | ระบุประเภทภาษี |  | smallint | ✓ |
| `branch_type` | สถานประกอบการ |  | smallint | ✓ |
| `headquarters` | สำนักงานใหญ่ *(resource only)* |  | char |  |
| `branch` | สาขา *(resource only)* |  | char |  |
| `branch_code` | เลขที่สาขา |  | varchar(25) | ✓ |
| `area_paybill` | เขตเก็บเงิน |  | varchar(25) | ✓ |
| `reason_disable_credit` | เหตุผลปิดวงเงินชั่วคราว |  | varchar(500) | ✓ |
| `close_credit_date` | วันที่ปิดเครดิต | Close Credit Date | smalldatetime | ✓ |
| `close_reason_1` | ชำระเช็คเกินกำหนด |  | smallint | ✓ |
| `close_reason_2` | ใหม่ยอดเกินวงเงินเครดิต |  | smallint | ✓ |
| `close_reason_3` | ผิดเงื่อนไขการชำระ |  | smallint | ✓ |
| `close_reason_4` | อื่น ๆ |  | smallint | ✓ |
| `29` | 29 *(resource only)* | 29 | char |  |
| `30` | 30 *(resource only)* | 30 | char |  |
| `31` | 31 *(resource only)* | 31 | char |  |
| `no_select` | ไม่เลือก *(resource only)* | No Select | char |  |
| `dimension_6` | มิติ 6 |  | varchar(255) | ✓ |
| `dimension_7` | มิติ 7 |  | varchar(255) | ✓ |
| `dimension_8` | มิติ 8 |  | varchar(255) | ✓ |
| `dimension_9` | มิติ 9 |  | varchar(255) | ✓ |
| `dimension_10` | มิติ 10 |  | varchar(255) | ✓ |
| `disable_auto_close_credit` | ไม่คำณวนปิดสถานะเครดิต |  | smallint | ✓ |
| `ap_code_ref` | อ้างอิงรหัสเจ้าหนี้ |  | varchar(25) | ✓ |
| `sale_type` | ประเภทการขาย |  | smallint | ✓ |
| `sale_type_0` | ไม่เลือก *(resource only)* |  | char |  |
| `sale_type_1` | ขายสด *(resource only)* |  | char |  |
| `sale_type_2` | ขายเชื่อ *(resource only)* |  | char |  |
| `line_id` | line id |  | char(255) | ✓ |
| `facebook` | facebook |  | char(255) | ✓ |
| `customer_type_code` | Type |  | varchar(25) | ✓ |
| `ar_channel_code` | Channel |  | varchar(25) | ✓ |
| `ar_location_type_code` | ประเภทสถานที่ตั้ง |  | varchar(25) | ✓ |
| `br_cust_code` | รหัสกลาง |  | varchar(25) | ✓ |
| `ar_sub_type_1_code` | Sub Type 1 |  | varchar(25) | ✓ |
| `ar_vehicle_code` | Vehicle |  | varchar(25) | ✓ |
| `ar_equipment_code` | Equipment |  | varchar(25) | ✓ |
| `ar_sub_equipment` | Sub Equipment |  | varchar(25) | ✓ |
| `ar_project_code` | ชื่อโครงการ |  | varchar(25) | ✓ |
| `ar_shoptype1_code` | ค้าส่ง |  | varchar(25) | ✓ |
| `ar_shoptype2_code` | ค้าปลีก |  | varchar(25) | ✓ |
| `ar_shoptype3_code` | ห้างท้องถิ่น |  | varchar(25) | ✓ |
| `ar_shoptype4_code` | On-Premise,HORECA |  | varchar(25) | ✓ |
| `ar_shoptype5_code` | ช่องทางพิเศษ |  | varchar(25) | ✓ |
| `sub_ar_shoptype5_code` | ช่องทางพิเศษย่อย |  | varchar(25) | ✓ |
| `arm_tier` | Tier *(resource only)* |  | char |  |
| `arm_approve_date` | วันที่อนุมัติ ARM Code *(resource only)* |  | char |  |
| `tier_0` | None *(resource only)* | None | char |  |
| `tier_1` | Silver *(resource only)* | Silver | char |  |
| `tier_2` | Gold *(resource only)* | Gold | char |  |
| `tier_3` | Platinum *(resource only)* | Platinum | char |  |
| `tier_4` | Diamond *(resource only)* | Diamond | char |  |
| `ar_customer_channel` | Customer Channel *(resource only)* | Customer Channel | char |  |
| `ar_project_code_name` | โครงการ |  | smallint | ✓ |
| `ar_shoptype6_code` | Modern Trade |  | varchar(25) | ✓ |
| `ar_shoptype7_code` | อื่นๆ |  | varchar(25) | ✓ |
| `ar_project_date_end` | วันที่สินสุดโครงการ |  | smalldatetime | ✓ |
| `nfc_asset` | NFC Asset | NFC Asset | varchar(255) | ✓ |
| `past_due_day` | จำนวนวันที่เกินกำหนดชำระได้ | Day past due | int | ✓ |
| `mobile_sales` | Mobile Sales | Mobile Sales | smallint | ✓ |
| `close_over_credit_warning` | ไม่เตือนเมื่อเกินวงเงิน |  | smallint | ✓ |

index: `ar_customer_detail_PK_CODE`(ar_code)

## ar_dealer

**รายละเอียดสมาชิก** — Dealer · edition: `SMLERP`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | เลขที่สมาชิก | Code | varchar(25) |  |
| `regist_date` | วันที่เริ่มต้นสมาชิก | Regist Date | smalldatetime | ✓ |
| `expire_date` | วันหมดอายุสมาชิก | Expire Date | smalldatetime | ✓ |
| `asso_code` | เลขที่สมาชิก (สมาคมช่างสี) | Asso Code | varchar(25) | ✓ |
| `asso_regist_date` | วันที่เริ่มต้นสมาชิก (สมาคมช่างสี) | Asso Regist Date | smalldatetime | ✓ |
| `asso_expire_date` | วันหมดอายุสมาขิก (สมาคมช่างสี) | Asso Expire Date | smalldatetime | ✓ |
| `ar_code` | รหัสลูกหนี้ | AR Code | varchar(25) |  |
| `branch_code` | รหัสสาขา | Branch Code | varchar(25) | ✓ |
| `sex` | เพศ |  | smallint | ✓ |
| `nationality` | สัญชาติ |  | varchar(25) | ✓ |
| `mstatus` | สถานะสมรส |  | smallint | ✓ |
| `blood_group` | กลุ่มเลือด |  | varchar(5) | ✓ |
| `address` | เลขที่บ้าน |  | varchar(25) | ✓ |
| `moo` | หมู่ |  | varchar(25) | ✓ |
| `building` | หมู่บ้าน/อาคาร |  | varchar(50) | ✓ |
| `floor` | ชั้น |  | varchar(25) | ✓ |
| `room_no` | เลขที่ห้อง |  | varchar(25) | ✓ |
| `soi` | ซอย |  | varchar(50) | ✓ |
| `road` | ถนน |  | varchar(50) | ✓ |
| `home_phone_extend` | เบอร์ต่อที่บ้าน |  | varchar(25) | ✓ |
| `off_phone` | เบอร์โทรที่ทำงาน |  | varchar(25) | ✓ |
| `off_phone_extend` | เบอร์ต่อที่ทำงาน |  | varchar(25) | ✓ |
| `mobile_phone` | เบอร์โทรมือถือ |  | varchar(25) | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* |  | char |  |
| `sex_man` | ชาย *(resource only)* | Men | char |  |
| `sex_women` | หญิง *(resource only)* | Women | char |  |
| `mstatus_single` | โสด *(resource only)* | Single | char |  |
| `mstatus_married` | สมรส *(resource only)* | Married | char |  |
| `mstatus_divorce` | หย่า *(resource only)* | Divorce | char |  |
| `tab_image` | รูปภาพ *(resource only)* | Image | char |  |
| `tab_dealer_detail` | รายละเอียดสมาชิกเพิ่มเติม *(resource only)* |  | char |  |
| `tab_m_congenital_disease` | โรคประจำตัว *(resource only)* |  | char |  |
| `tab_m_allergic` | ประวัติแพ้ยา *(resource only)* |  | char |  |
| `tab_dealer_main` | รายละเอียดสมาชิก *(resource only)* |  | char |  |
| `ar_address` | ที่อยู่ *(resource only)* |  | char |  |
| `telephone` | โทรศัพท์ *(resource only)* |  | char |  |
| `is_staff` | เป็นพนักงาน |  | smallint | ✓ |
| `tab_m_yourhealthy` | ข้อมูลสุขภาพ *(resource only)* |  | char |  |

index: `ar_dealer_PK_CODE`(code), `ar_dealer_ar_code`(ar_code)

## ar_equipment

**Equipment** — Equipment

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `guid_code` | guid_code |  | varchar(35) | ✓ |

## ar_item_by_customer

**สินค้าตามลูกค้า** — Item by Customer

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า | Customer Code | varchar(25) |  |
| `ic_code` | รหัสสินค้า | Item Code | varchar(25) | ✓ |
| `remark` | หมายเหตุ | Remark | varchar(255) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |
| `line_number` | บรรทัด | Line Number | int | ✓ |

## ar_location_type

**สถานที่ตั้ง** — Ar Location

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | code | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 | Ar Location Name 1 | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 | Ar Location Name 2 | varchar(255) | ✓ |
| `guid_code` | guid_code | guid_code | varchar(35) | ✓ |

## ar_project

**Ar Project** — Ar Project

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype1

**AR Shoptype1** — AR Shoptype1

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype2

**AR Shoptype2** — AR Shoptype2

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype3

**AR Shoptype3** — AR Shoptype3

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype4

**AR Shoptype4** — AR Shoptype4

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype5

**AR Shoptype5** — AR Shoptype5

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype6

**AR Shoptype6** — AR Shoptype6

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_shoptype7

**AR Shoptype7** — AR Shoptype7

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

## ar_sub_equipment

**Sub Equipment** — Sub Equipment

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `guid_code` | guid_code |  | varchar(35) | ✓ |

## ar_sub_type_1

**Sub Type 1** — Sub Type 1

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `guid_code` | guid_code |  | varchar(35) | ✓ |

## ar_vehicle

**Vehicle** — Vehicle

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `guid_code` | guid_code |  | varchar(35) | ✓ |

## customer_type

**Type** — Type

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | Code | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 | Customer type Name 1 | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 | Customer type Name 2 | varchar(255) | ✓ |
| `guid_code` | guid code | Guid Code | varchar(35) | ✓ |
| `status` | สถานะ | Status | smallint | ✓ |

## sub_ar_shoptype5

**Sub AR Shoptype5** — Sub AR Shoptype5

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) | ✓ |
| `ar_shoptype5_code` | รหัส AR Shoptype5 |  | varchar(25) | ✓ |
| `name_1` | ชื่อ 1 |  | varchar(255) | ✓ |
| `name_2` | ชื่อ 2 |  | varchar(255) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid code |  | varchar(35) | ✓ |

