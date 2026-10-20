---
tags: [sml, reports, generated]
---
# รายงานทั้งหมด

> สร้างอัตโนมัติด้วย `scripts/gen_reports.py aoy` — เก็บเฉพาะชื่อรายงานและชื่อตาราง ไม่มีข้อมูลธุรกิจ กลับไป [[00-Index]] · [[module-reports]]

## เครื่องมือรายงาน 3 แบบ

1. **FastReport** — เมนู tag `fastreport` → `SMLFastReport._designer._load(menuName)` โหลดแบบรายงานจากตาราง `sml_fastreport` (คอลัมน์ `reportdata` เป็น zip ที่มี template + SQL) ซึ่ง sync มาจาก master server `ws.smlaccount.com` / DB `SMLMASTER` ตาม `timeupdate`
2. **รายงานเอกสารตาม trans_flag** — `SMLERPReportTool._reportTrans(reportEnum, transType, screenName)` และตระกูล `_reportCashBankTrans`, `_reportArApTrans` (เขียนในโค้ด)
3. **รายงานเฉพาะ** — คลาสใน `SMLERP*Report`, `SINGHAReport` ที่สืบจาก `SMLReport._report._viewReport` หรือ UserControl

## FastReport ใน `aoy` (562 รายงาน)

`report_type` (จาก `SMLFastReport/_designer.cs`, `_selectMenu.cs`): 0 ทั่วไป, 1 สินค้า, 2 ซื้อ, 3 ขาย, 4 เจ้าหนี้, 5 ลูกหนี้, 6 เงินสด/ธนาคาร, 7 สินทรัพย์, 8 GL — รายงานที่ไม่อยู่ในเมนูหลัก (เช่น menuid ตัวเลขที่ผู้ใช้/SML สร้างเพิ่ม) เปิดจากเมนู "รายงานอื่น ๆ" ของแต่ละโมดูล (`menu_fastreport_other_*`) ซึ่งกรองตาม report_type · `is_system_report` = รายงานมาตรฐานของระบบ (ยังไม่ยืนยัน)

| menuid | ชื่อ | type | system | จำนวน SELECT | ตารางที่อ่าน | อยู่ในเมนู |
|---|---|---|---|---|---|---|
| `10002` | รายงานรายละเอียดสินทรัพย์ (คุรุภัณฑ์) | 7 สินทรัพย์ | 0 | 7 | as_asset, erp_side_list, as_asset_location, erp_department_list, erp_user, erp_province | รายงานอื่น ๆ (`menu_fastreport_other_asset`) |
| `1001` | รายงานบาร์โค๊ดพร้อมราคากลุ่มที่ 1 | 1 สินค้า | 0 | 4 | ic_inventory, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `1002` | รายงานยอดคงเหลือสินค้า (แสดงทุกสินค้า) | 1 สินค้า | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `1003` | รายงานสินค้าแสดงราคาขายและราคาสมาชิก | 0 ทั่วไป | 0 | 6 | pos_id, ic_inventory_barcode |  |
| `1004` | รายงานสินค้าแสดงราคาขาย ราคาสมาชิก ราคาตามสูตร | 1 สินค้า | 0 | 36 | ic_inventory_price_formula, ic_inventory, ic_inventory_barcode, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `1005` | รายงานบาร์โค๊ดพร้อมราคากลุ่มที่ 2 | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_inventory_barcode |  |
| `1006` | รายงานสินค้าต่ำกว่าทุน | 3 ขาย | 0 | 5 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `2001` | รายงานการขายแยกตามพนักงานขาย (หักส่วนลด) | 3 ขาย | 0 | 14 | ic_trans_detail, erp_user, ar_customer, ic_trans, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `2002` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามวันที่ | 0 ทั่วไป | 0 | 5 | ic_inventory, ic_trans_detail, ic_unit |  |
| `2003` | รายงานบาร์โค๊ดสินค้าซ้ำ | 1 สินค้า | 0 | 3 | ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2005` | รายงานสินค้าคงเหลือตามคลัง แสดงราคาขายตามบาร์โค้ด | 1 สินค้า | 0 | 14 | ic_inventory_barcode, ic_warehouse, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2006` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้า | 1 สินค้า | 1 | 11 | ic_inventory, ic_group | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2007` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้า (แยกตามคลัง) | 1 สินค้า | 0 | 10 | ic_inventory, ic_group | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2008` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้า (แยกตามคลัง ที่เก็บ) | 1 สินค้า | 0 | 22 | ic_inventory, ic_group, ic_trans_detail, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2009` | รายงานบาร์โค้ดสินค้าตามผู้จัดจำหน่ายหลัก | 1 สินค้า | 0 | 2 | ic_inventory_barcode, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2010` | รายงานสินค้าคงเหลือแสดงตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 10 | ic_inventory, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2010-1` | รายงานสินค้าคงเหลือแสดงตามผู้จำหน่ายหลัก แสดงยอดคงเหลือศูนย์ | 1 สินค้า | 0 | 10 | ic_inventory, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2011` | รายงานยอดคงเหลือสินค้าแสดงตามผู้จำหน่ายหลัก (รหัสสินค้า,บาร์โค๊ด) | 1 สินค้า | 0 | 12 | ic_inventory, ap_supplier, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2012` | รายงานจุดต่ำสุดสูงสุดสินค้า | 1 สินค้า | 1 | 5 | ic_wh_shelf, ic_inventory, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2013` | รายงานบาร์โค๊ดสินค้า | 1 สินค้า | 0 | 2 | ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2014` | รายงานยอดคงเหลือสินค้า แสดงยอดคงเหลือตามหน่วย | 1 สินค้า | 0 | 3 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2015` | รายงานยอดคงเหลือสินค้าตามคลัง แสดงยอดคงเหลือตามหน่วย | 1 สินค้า | 0 | 26 | ic_inventory, ic_trans_detail, ic_unit_use, ic_warehouse | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2016` | รายงานยอดคงเหลือสินค้าตามที่เก็บสินค้า แสดงยอดคงเหลือตามหน่วย | 1 สินค้า | 0 | 4 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2017` | รายงานสินค้าคงเหลือตามคลัง-ที่เก็บ | 1 สินค้า | 0 | 9 | ic_warehouse, ic_shelf, ic_inventory, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2018` | รายการสินค้าที่ไม่พบหน่วยนับ | 1 สินค้า | 0 | 3 | ic_inventory, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2019` | รายงานสินค้าถึงจุดสั่งซื้อเรียงตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 16 | ic_inventory_detail, ap_supplier, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2020` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้าย่อย | 1 สินค้า | 0 | 10 | ic_inventory, ic_group_sub | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2021` | รายงานข้อมูลสินค้าพบอัตราส่วนหน่วยต้นทุนผิด | 1 สินค้า | 0 | 10 | ic_unit_use, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2022` | รายงานราคาขายสินค้าตามสูตร | 1 สินค้า | 0 | 6 | ic_inventory, ic_inventory_price_formula | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2023` | สินค้าไม่พบ barcode | 1 สินค้า | 0 | 4 | ic_inventory, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2024` | รายงานยอดคงเหลือสินค้าติดลบ | 1 สินค้า | 0 | 3 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2025` | รายงานยอดคงเหลือสินค้าติดลบตามคลังสินค้า | 1 สินค้า | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2026` | รายงานยอดคงเหลือสินค้าติดลบตามพืันที่เก็บสินค้า | 1 สินค้า | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2027` | รายงานยอดคงเหลือสินค้าหักยอดจอง | 1 สินค้า | 0 | 6 | ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2028` | รายงานบาร์โค๊ดสินค้าทีไม่แสดงในใบเสร็จ | 1 สินค้า | 0 | 2 | ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2029` | รายงานรายการสินค้าที่จะตรวจนับ | 1 สินค้า | 0 | 2 | ic_wh_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2030` | รายงานสินค้าหลายหน่วยนับ | 1 สินค้า | 0 | 5 | ic_inventory, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2031` | รายงานปริมาณการสั่งซื้อสินค้าเทียบกับยอดสูงสุด | 1 สินค้า | 0 | 12 | ic_inventory_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2032` | รายงานสินค้าคงเหลือตามคลัง แสดงตามผุ้จำหน่ายหลัก | 1 สินค้า | 0 | 9 | ic_warehouse, ic_inventory_barcode, ap_supplier, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2033` | รายงานสินค้าคงเหลือตามคลัง-ที่เก็บ แสดงตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 6 | ic_warehouse, ic_shelf, ic_inventory, ic_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2034` | รายงานรายละเอียดสินค้าแสดงจุดต่ำสุด สุงสุด | 1 สินค้า | 0 | 3 | ic_inventory_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2035` | รายงานสินค้าที่ไม่มีการเคลื่อนไหว ตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 63 | ic_trans, ic_trans_detail, ic_inventory, ic_unit, ic_unit_use, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2036` | รายงาน LOT Error | 1 สินค้า | 0 | 3 | ic_trans_detail_lot, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2037` | รายงานจุดต่ำสุดสูงสุดสินค้า ตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 8 | ic_wh_shelf, ic_inventory, ap_supplier, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2038` | รายงานสินค้าแสดงยอดคงเหลือสินค้าตามผู้จำหน่าย | 1 สินค้า | 0 | 9 | ic_inventory_barcode, ic_warehouse, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2039` | รายงานกำไรขั้นต้นประจำเดือน แสดงต้นงวด | 1 สินค้า | 0 | 10 | ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2040` | รายงานสินค้าแสดง หน่วยนับ บาร์โค๊ด ราคา | 1 สินค้า | 0 | 2 | ic_inventory, ic_unit_use, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2041` | รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง-จุดเก็บ ตามผู้จำหน่ายหลัก | 1 สินค้า | 0 | 5 | ap_supplier, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2042` | รายงานราคาขายสินค้าตามสูตร แสดงบาร์โค๊ด | 1 สินค้า | 0 | 6 | ic_inventory, ic_inventory_price_formula | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2043` | รายงานการโอนสินค้า ตามคลังที่เก็บ | 1 สินค้า | 0 | 7 | ic_trans_detail, ic_trans, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2044` | ใบตรวจสอบราคาขายก่อนเสนอลูกค้าและใบตรวจสอบราคาหลังการขาย | 1 สินค้า | 0 | 24 | ic_inventory, ic_trans_detail, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2045` | รายงานยอดคงเหลือสินค้าแสดงตามยี่ห้อ | 1 สินค้า | 0 | 10 | ic_inventory, ap_supplier, ic_brand | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2046` | รายงานกำไรขั้นต้นตามพนักงานขาย | 1 สินค้า | 0 | 18 | erp_user, ic_trans_detail, ic_trans, ar_customer, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2047` | รายงานข้อมูลสินค้า (แสดงครัว) | 1 สินค้า | 0 | 4 | kitchen_master_item, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2048` | รายงานรายการสินค้าที่อนูญาติให้ติดลบ | 1 สินค้า | 0 | 4 | ic_inventory, ic_inventory_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2049` | รายงานสินค้าที่ยังไม่ได้ตรวจนับ | 1 สินค้า | 0 | 4 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2050` | รายงานสินค้าคงเหลือตามคลัง-ที่เก็บ เรียงตามสินค้า | 1 สินค้า | 0 | 8 | ic_warehouse, ic_shelf, ic_inventory_barcode, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2051` | รายงานตรวจสอบยอดคงเหลือสินค้ากับ Serial | 1 สินค้า | 0 | 10 | ic_serial, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2052` | รายงานตรวจสอบข้อมูลคลังสาขา | 1 สินค้า | 0 | 8 | ic_warehouse, ic_wms_trans, ic_wms_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2053` | รายงานยอดคงเหลือสินค้าแสดงตามผู้จำหน่ายหลัก (รหัสสินค้า,บาร์โค๊ด) แสดงราคาทุน | 1 สินค้า | 0 | 20 | ic_inventory, ic_trans_detail, ap_supplier, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2054` | รายงาน Lot สินค้า - แสดงราคา | 1 สินค้า | 0 | 12 | ic_trans_detail_lot, ic_inventory, ic_unit, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2055` | รายงานตรวจสอบสถานะรายการยกเลิก | 1 สินค้า | 0 | 6 | ic_trans, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2056` | รายงานรายละเอียดสินค้า - ตามกลุ่มสินค้าและหมวดสินค้า | 1 สินค้า | 0 | 8 | ic_group, ic_group_sub, ic_category, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2057` | รายงานจุดต่ำสุดสูงสุดสินค้า แสดงยอดคงเหลือ | 1 สินค้า | 0 | 10 | ic_inventory_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2058` | รายงานรายละเอียดสินค้า - แสดงราคาขายทั่วไป | 1 สินค้า | 0 | 6 | ic_inventory, ic_inventory_price | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2059` | รายงานสถานะสินค้า - ตามคลัง | 1 สินค้า | 0 | 14 | ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2060` | รายงานเคลื่อนไหวสินค้า ตามคลัง | 1 สินค้า | 0 | 19 | ic_trans_detail, ic_inventory, ic_trans, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2061` | รายงานการตรวจสอบการแก้ไขข้อมูลย้อนหลัง | 1 สินค้า | 0 | 14 | ap_ar_trans, ic_trans, logs | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2062` | รายงานการตรวจสอบการแก้ไขข้อมูลหลักย้อนหลัง | 1 สินค้า | 0 | 2 | master_logs | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2063` | รายงานขอเบิกสินค้าและวัตถุดิบ | 1 สินค้า | 0 | 20 | erp_branch_list, ic_trans, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2064` | รายงานการเคลื่อนไหวตามมูลค่า | 1 สินค้า | 0 | 42 | ic_trans_detail, ic_trans, ic_unit, ic_unit_use, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2065` | รายละเอียดสินค้า ตรวจสอบรูปภาพ | 1 สินค้า | 0 | 14 | ic_inventory, images | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2066` | รายงานยอดคงเหลือสินค้า แสดงชั้นวาง | 1 สินค้า | 0 | 20 | ic_inventory, ic_unit_use, ic_wh_shelf, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2067` | รายงานยอดคงเหลือสินค้า-ตามหมวดสินค้า | 1 สินค้า | 0 | 11 | ic_inventory, ic_group, ic_category | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2068` | รายงานเบิกสินค้าและวัตถุดิบ แยกแผนก | 1 สินค้า | 0 | 18 | ic_trans, erp_department_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2069` | รายงานเบิกสินค้าและวัตถุดิบ แยกโครงการ | 1 สินค้า | 0 | 18 | ic_trans, erp_project_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2070` | รายงานเบิกสินค้าและวัตถุดิบ แยกกลุ่มเอกสาร | 1 สินค้า | 0 | 18 | ic_trans, erp_doc_group, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2071` | รายงานเบิกสินค้าและวัตถุดิบ แยกหน่วยงาน | 1 สินค้า | 0 | 18 | ic_trans, erp_side_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2072` | รายงานเบิกสินค้าและวัตถุดิบ แยกการจัดสรร | 1 สินค้า | 0 | 18 | ic_trans, erp_allocate_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2073` | รายงานเบิกสินค้าและวัตถุดิบ แยกงาน | 1 สินค้า | 0 | 18 | ic_trans, erp_job_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2074` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกแผนก | 1 สินค้า | 0 | 18 | ic_trans, erp_department_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2075` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกโครงการ | 1 สินค้า | 0 | 18 | ic_trans, erp_project_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2076` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกกลุ่มเอกสาร | 1 สินค้า | 0 | 18 | ic_trans, erp_doc_group, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2077` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกหน่วยงาน | 1 สินค้า | 0 | 18 | ic_trans, erp_side_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2078` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกการจัดสรร | 1 สินค้า | 0 | 18 | ic_trans, erp_allocate_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2079` | รายงานรับคืนจากการเบิกสินค้าและวัตถุดิบ แยกงาน | 1 สินค้า | 0 | 18 | ic_trans, erp_job_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2080` | รายละเอียดสินค้า ตรวจสอบกลุ่มสินค้า | 1 สินค้า | 0 | 7 | ic_group, ic_group_sub, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2081` | รายงานรายละเอียดสินค้า แสดงชื่อสินค้า2 | 1 สินค้า | 0 | 6 | ic_unit, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2082` | รายงานเคลื่อนไหวสินค้าต้นทุนมาตราฐาน ตามคลัง | 1 สินค้า | 0 | 26 | ic_inventory, ic_trans_detail, ic_trans, ap_supplier, ar_customer, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2083` | รายงานยอดคงเหลือสินค้า (ต้นทุนแฝง) | 1 สินค้า | 0 | 20 | ic_inventory, ic_trans_detail, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2084` | รายงานกำไรขั้นต้น (เอกสาร) หักส่วนลดท้ายบิล | 1 สินค้า | 0 | 16 | ic_trans_detail, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2085` | รายงานข้อมูลสินค้า แสดงฝังบัญชี | 1 สินค้า | 0 | 6 | gl_chart_of_account, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2086` | รายงานตรวจสอบโปรโมชั่น | 1 สินค้า | 0 | 8 | ic_inventory, ic_promotion_formula_condition, ic_promotion_formula | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2087` | รายงานประวัติการพิมพ์ | 1 สินค้า | 0 | 4 | erp_print_logs, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2088` | รายงานรายละเอียดคูปอง | 1 สินค้า | 0 | 10 | cb_trans_detail, ar_customer, coupon_list | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2089` | รายงานสถานะคูปอง | 1 สินค้า | 0 | 10 | cb_trans_detail, ar_customer, coupon_list | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2090` | รายงานเคลื่อนไหวคูปอง | 1 สินค้า | 0 | 14 | ar_customer, coupon_list, ap_ar_trans, ic_trans, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2091` | รายงานสินค้าที่ไม่มีการเคลื่อนไหว ตามกลุ่มสินค้าหลัก | 1 สินค้า | 0 | 62 | ic_trans, ic_trans_detail, ic_group, ic_unit, ic_unit_use, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2092` | รายงานสินค้าคงเหลือ แสดงเฉพาะสินค้าบริการ | 1 สินค้า | 0 | 20 | ic_inventory, ic_trans_detail, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2093` | รายงานการเบิกสินค้าและวัตถุดิบ แสดงหมายเหตุ แยกตามเอกสาร | 1 สินค้า | 0 | 8 | ic_trans, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2094` | รายงานกำไรขั้นต้น (สินค้า) | 1 สินค้า | 0 | 20 | ic_trans_detail, ic_unit, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2095` | รายงานการใช้โปรโมชั่น | 1 สินค้า | 0 | 2 | ic_trans_detail_promotion, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2096` | รายงานกำไรขั้นต้น (สินค้า) ตามกลุ่มสินค้า | 1 สินค้า | 0 | 11 | ic_inventory, ic_unit, ic_group, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2097` | รายงานสินค้า หยุดซื้อ หยุดขาย | 1 สินค้า | 0 | 4 | ic_unit, ic_inventory_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `212` | 212 | 6 เงินสด/ธนาคาร | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `2901` | รายงานข้อมูลสินค้าสำหรับนำเข้า | 1 สินค้า | 0 | 2 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2902` | รายงานรายละเอียดหน่วยนับสินค้านำเข้า | 1 สินค้า | 0 | 2 | ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2903` | รายงานรายละเอียดหน่วยนับนำเข้า | 1 สินค้า | 0 | 2 | ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2904` | รายงานรายละเอียดบาร์โค๊ดนำเข้า | 1 สินค้า | 0 | 2 | ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `2905` | รายงานรายละเอียดราคาตามสูตรนำเข้า | 1 สินค้า | 0 | 2 | ic_inventory_price_formula | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `3001` | รายงานใบสังซื้อสินค้าที่ค้างรับ-ตามเจ้าหนี้ | 2 ซื้อ | 0 | 9 | ic_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3002` | รายงานเปรียบเทียบต้นทุนการซื้อล่าสุด | 2 ซื้อ | 0 | 3 | ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3003` | รายงานวิเคราะห์ใบสั่งซื้อเรียงตามสินค้า-Supplier | 2 ซื้อ | 0 | 4 | ic_trans_detail, ap_supplier, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3004` | รายงานวิเคราะห์ใบสั่งซื้อเรียงตาม Supplier-สินค้า | 2 ซื้อ | 0 | 4 | ic_trans_detail, ap_supplier, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3005` | รายงานสถานะใบสั่งซื้อตามสินค้า | 2 ซื้อ | 0 | 6 | ap_supplier, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3006` | รายงานราคาซื้อสินค้าล่าสุดแสดงตามผู้จำหน่ายหลัก | 2 ซื้อ | 0 | 12 | ic_trans_detail, ap_supplier, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3007` | รายงานใบสังซื้อสินค้าที่ค้างรับ-ตามเจ้าหนี้ แสดงหมายเหตุ | 2 ซื้อ | 0 | 9 | ic_trans_detail, ap_supplier, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3008` | รายงานสรุปใบสั่งซื้อ แยกแผนก | 2 ซื้อ | 0 | 6 | erp_department_list, ap_supplier, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3009` | รายงานซื้อสินค้า แยกแผนก | 2 ซื้อ | 0 | 18 | ic_trans, erp_department_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3010` | รายงานซื้อสินค้า แยกโครงการ | 2 ซื้อ | 0 | 19 | ic_trans, ic_trans_detail, erp_project_list, ap_supplier, ic_inventory, ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3011` | รายงานซื้อสินค้า แยกกลุ่มเอกสาร | 2 ซื้อ | 0 | 18 | ic_trans, erp_doc_group, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3012` | รายงานซื้อสินค้า แยกหน่วยงาน | 2 ซื้อ | 0 | 18 | ic_trans, erp_side_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3013` | รายงานซื้อสินค้า แยกการจัดสรร | 2 ซื้อ | 0 | 18 | ic_trans, erp_allocate_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3014` | รายงานซื้อสินค้า แยกงาน | 2 ซื้อ | 0 | 18 | ic_trans, erp_job_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3015` | รายงานใบสั่งซื้อ แยกแผนก | 2 ซื้อ | 0 | 18 | ic_trans, erp_department_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3016` | รายงานใบสั่งซื้อ แยกโครงการ | 2 ซื้อ | 0 | 18 | ic_trans, erp_project_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3017` | รายงานใบสั่งซื้อ แยกกลุ่มเอกสาร | 2 ซื้อ | 0 | 18 | ic_trans, erp_doc_group, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3018` | รายงานใบสั่งซื้อ แยกหน่วยงาน | 2 ซื้อ | 0 | 18 | ic_trans, erp_side_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3019` | รายงานใบสั่งซื้อ แยกการจัดสรร | 2 ซื้อ | 0 | 18 | ic_trans, erp_allocate_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3020` | รายงานใบสั่งซื้อ แยกงาน | 2 ซื้อ | 0 | 18 | ic_trans, erp_job_list, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3021` | รายงานสถานะใบเสนอซื้อ แสดงสถานะ | 2 ซื้อ | 0 | 28 | ic_trans_detail, ic_trans, ap_supplier, ic_inventory, ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3022` | รายงานสรุปยอดซื้อ-ตามวันที่ | 2 ซื้อ | 0 | 3 | ic_trans, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3023` | รายงานสรุปมูลค่าการซื้อ 12 เดือน แยกตามเจ้าหนี้ | 2 ซื้อ | 0 | 12 | ic_inventory, ic_trans_detail, ar_customer, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3024` | รายงานเปรียบเทียบยอดซื้อสินค้า 12 เดือน ตามเจ้าหนี้ | 2 ซื้อ | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3025` | รายงานรับสินค้าแบบทะยอยรับ ค้างตั้งหนี้ | 2 ซื้อ | 0 | 9 | ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3026` | รายงานรับสินค้าแบบทะยอยรับ มูลค่าค้างตั้งหนี้ | 2 ซื้อ | 0 | 10 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `3027` | รายงานใบตั้งหนี้จากการซื้อแบบสรุป-ตามโครงการ | 2 ซื้อ | 0 | 4 | erp_project_list, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `4001` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามสมาชิก | 3 ขาย | 0 | 14 | ic_trans, ar_customer, ic_inventory, ar_dealer, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4002` | รายงานการขายแสดง รายละเอียดการรับเงิน | 3 ขาย | 0 | 22 | ic_trans, ar_customer, cb_trans, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4003` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามสินค้า | 3 ขาย | 0 | 6 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4004` | สรุปยอดขายตามคลังสินค้า | 3 ขาย | 0 | 10 | ic_inventory, ic_warehouse, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4005` | รายงานสรุปยอดขายสินค้า - ตามรหัสเครือง POS | 3 ขาย | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4006` | รายงานใบสั่งขายสินค้าที่ค้างส่ง-ตามลูกค้า | 3 ขาย | 0 | 10 | ic_trans_detail, ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4007` | รายงานสรุปยอดขาย (มูลค่าสุทธิของเอกสาร) - ตามวันที่ | 3 ขาย | 1 | 3 | ic_trans, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4009` | รายงานการยกเลิกอาหาร | 3 ขาย | 0 | 3 | table_order_cancel, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4011` | รายงานสรุปยอดขายตามวันที่/รหัสเครื่อง POS | 3 ขาย | 0 | 2 | ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4012` | รายงานวิเคราะห์ จำนวนยอดขายสินค้า แจกแจงรายเดือน | 3 ขาย | 0 | 11 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4013` | รายงานใบสังจองสินค้าที่ค้างส่ง-ตามลูกค้า | 3 ขาย | 0 | 8 | ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4014` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มสินค้าย่อย | 3 ขาย | 0 | 12 | ic_inventory, ar_customer, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4015` | รายงานแสดงยอดคอมมิสชั่น-ตามพนักงานขาย | 3 ขาย | 0 | 9 | ic_inventory, ic_trans_detail, erp_user, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4016` | รายงานแสดงสถานะการเปิด-ปิด กะ เรียงตามหมายเลขบรรทัด | 3 ขาย | 0 | 4 | pos_period, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4017` | รายงานสรุปมูลค่าการขาย 12 เดือน แยกตามลูกค้า | 3 ขาย | 0 | 5 | gl_journal_detail, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4018` | รายงานใบส่งสินค้าและการวางบิล | 3 ขาย | 0 | 7 | ap_ar_trans_detail, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4019` | สรุปข้อมูลใบสั่งจองสินค้า | 3 ขาย | 0 | 3 | ic_trans_detail, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4020` | รายงานเปรียบเทียบการขาย จัดอันดับยอดขายลูกค้า-ตามจังหวัด | 3 ขาย | 0 | 11 | ar_customer, ic_trans, erp_province | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4021` | รายงานการขายสินค้าแบบแจกแจงเป็นรายสินค้า | 3 ขาย | 0 | 22 | ic_trans_detail, ic_inventory, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4021-1` | รายงานการขายสินค้าแบบแจกแจงเป็นรายสินค้า แสดงยอดคงเหลือตามคลัง | 3 ขาย | 0 | 22 | ic_trans_detail, ic_inventory, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4022` | รายงานวิเคราะห์ การขาย จัดเรียงตาม มิติแผนก กลุ่ม แสดงมูลค่า | 3 ขาย | 0 | 11 | ic_trans_detail, ic_inventory, ic_trans, erp_department_list, ic_group | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4023` | รายงานรวมขายประจำวัน | 3 ขาย | 0 | 4 | ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4024` | รายงานรวมขายประจำวัน-ตามลูกค้า | 3 ขาย | 0 | 5 | ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4025` | รายงานสรุปการสั่งอาหาร แจกแจงตามวันที่ พนักงาน | 3 ขาย | 0 | 5 | table_order, table_order_doc, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4026` | รายงานสรุปยอดขายตามวันที่-แจกแจงอาหารเครื่องดื่ม | 3 ขาย | 0 | 7 | ic_trans, ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4027` | รายงานการขายสินค้าแยกตามลูกค้า | 3 ขาย | 0 | 5 | ar_customer, ic_trans, ar_customer_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4028` | รายงานสรุปการสั่งอาหาร แจกแจงตามวันที่ พนักงาน แสดงหมายเหตุ | 3 ขาย | 0 | 7 | table_order_doc, table_order, erp_user, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4029` | รายงานยอดขายตามกะ | 3 ขาย | 0 | 9 | ic_trans, cb_trans, pos_period, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4030` | รายงานสรุปการสั่งอาหารและยอดขาย-ตามวันที่ | 3 ขาย | 0 | 6 | table_order, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4031` | สรุปยอดขายตามคลังสินค้า แสดงผู้จำหน่ายหลัก | 3 ขาย | 0 | 12 | ic_inventory, ic_warehouse, ic_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4032` | รายงานการขายสินค้า แสดงเฉพาะรายการที่มีส่วนลด | 3 ขาย | 0 | 6 | ic_trans_detail_promotion, ic_trans, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4033` | รายงานรายละเอียดการขายสินค้า แสดงเฉพาะยอดส่วนลด | 3 ขาย | 0 | 3 | ic_trans_detail, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4034` | รายงานใบสังขายสินค้าที่ค้างส่ง-ตามพนักงาน-ตามลูกค้า | 3 ขาย | 0 | 9 | ic_trans_detail, ar_customer, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4035` | รายงานการขายตามผู้จำหน่ายหลัก | 3 ขาย | 0 | 6 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4036` | รายงานการรับเงินประจำวันแยกตามรหัสเครื่องขาย POS | 3 ขาย | 0 | 31 | ic_trans, ar_customer, cb_trans, cb_trans_detail, ic_inventory, ic_trans_detail, ic_trans_serial_number | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4037` | รายงานการขาย/รับคืน ตามพนักงาน | 3 ขาย | 0 | 4 | ic_trans, erp_user, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4038` | รายงานสรุปยอดขายตามเดือน | 3 ขาย | 0 | 2 | ic_trans_detail, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4039` | รายงานการขายตามบาร์โค๊ด | 3 ขาย | 0 | 2 | ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4040` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า-ตามหน่วยนับ | 3 ขาย | 0 | 9 | ic_inventory, ic_trans, ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4041` | รายงานการขายสินค้าและบริการแยกตามหน่วยนับ/ตามคลัง/ที่เก็บ | 3 ขาย | 0 | 7 | ic_trans_detail, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4042` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มสินค้า ตามสาขา | 0 ทั่วไป | 0 | 10 | ic_inventory, ic_trans_detail, ic_trans |  |
| `4067` | รายงานยกเลิกการขายและบริการ แยกตามพนักงานขาย | 3 ขาย | 1 | 18 | ic_trans, ar_customer, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4067-1` | รายงานยกเลิกการขายและบริการ แยกตามพนักงานขาย | 3 ขาย | 0 | 18 | ic_trans, ar_customer, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4068` | รายงานสรุปมูลค่าการขาย 12 เดือน แยกตามลูกค้า | 3 ขาย | 0 | 12 | ar_customer, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4069` | รายงานการรับเงินประจำวัน แสดงรายการรับชำระ | 3 ขาย | 0 | 12 | ic_trans, ar_customer, cb_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4070` | รายงานแสดงการพักบิล | 3 ขาย | 0 | 6 | erp_user, pos_log | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4071` | รายงานการรับเงิน แสดง Wallet | 3 ขาย | 0 | 18 | ic_trans, ar_customer, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4072` | รายงานสรุปการขายสินค้าตามพนักงานขาย แสดงยอดมัดจำ | 3 ขาย | 0 | 10 | ic_trans_detail, erp_user, ar_customer, ic_trans, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4073` | รายงานการขาย/รับคืน ตามพนักงาน ตามรูปแบบเอกสาร | 3 ขาย | 0 | 4 | ic_trans, erp_user, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4074` | รายงานสรุปยอดขายสินค้าสุทธิ ตามพนักงานขาย | 3 ขาย | 0 | 6 | erp_user, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4075` | รายงานขายสินค้าและบริการ แยกแผนก | 3 ขาย | 0 | 18 | ic_trans, erp_department_list, ar_customer, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4076` | รายงานสรุปการขายสินค้า ตามกลุ่มพนักงานขาย | 3 ขาย | 0 | 25 | erp_user, erp_user_group_detail, ar_customer, ic_trans, erp_user_group, ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4078` | รายงานการรับเงิน Wallet | 3 ขาย | 0 | 5 | cb_trans_detail, ar_customer, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4079` | รายงานเปรียบเทียบยอดขายสินค้า 12 เดือน ตามลูกหนี้ | 3 ขาย | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4080` | รายงานสินค้าค้างส่ง ตามคลัง/ที่เก็บ | 3 ขาย | 0 | 18 | ic_trans_detail, ic_inventory, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4081` | รายงานใบเสนอราคาคงค้าง | 3 ขาย | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4082` | รายงานวิเคราะห์การขายสุทธิ-ตามโครงการ | 3 ขาย | 0 | 19 | ic_trans_detail, ic_trans, erp_project_list, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4083` | รายงานรับเงินมัดจำใช้ไปคงเหลือ | 3 ขาย | 0 | 10 | ic_trans, ar_customer, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4084` | รายงานออกใบกำกับภาษีออกแทน | 3 ขาย | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4085` | รายงานสรุปยอดขาย-ตามวันที่ | 3 ขาย | 0 | 3 | ic_trans, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4086` | รายงานการขายสินค้าและบริการ หักรับคืนและลดหนี้ | 3 ขาย | 0 | 22 | ic_trans, ar_customer, ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `4087` | รายงานการรับเงินประจำวัน ตามแคชเชียร์ | 3 ขาย | 0 | 18 | ic_trans, erp_user, ar_customer, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `5001` | รายงานการจ่ายชำระหนี้ (แสดงรายละเอียด) | 4 เจ้าหนี้ | 0 | 18 | cb_trans_detail, ap_ar_trans, ap_supplier, erp_bank, cb_trans, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `5002` | รายงานเจ้าหนี้ค้างจ่ายชำระจากการซื้อ - สรุป | 4 เจ้าหนี้ | 0 | 12 | ic_trans, ap_ar_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `5003` | รายงานการจ่ายชำระเจ้าหนี้ แสดงรายละเอียดบิล รายละเอียดการจ่ายเงิน | 4 เจ้าหนี้ | 0 | 34 | cb_trans, ic_trans, cb_trans_detail, ap_ar_trans, ap_supplier, erp_bank, ap_ar_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `5004` | รายงานรายละเอียดเจ้าหนี้ ตามกลุ่มเจ้าหนี้ | 4 เจ้าหนี้ | 0 | 34 | ap_supplier_detail, ap_group_sub, ap_group, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `5.7.4 รายงานยกเลิก` | รายงานสรุปใบกำกับภาษีอย่างย่อ(ยกเลิก) | 0 ทั่วไป | 0 | 4 | ar_customer, ic_trans |  |
| `5.8.11` | รายงานการรับเงิน เอวี | 0 ทั่วไป | 0 | 27 | ic_trans, ar_customer, cb_trans, cb_trans_detail |  |
| `6001` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียด) | 5 ลูกหนี้ | 0 | 21 | cb_trans_detail, ap_ar_trans, ar_customer, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6002` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า | 5 ลูกหนี้ | 0 | 14 | ic_trans, ar_customer, ic_inventory, ar_dealer, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6003` | รายงานลูกหนี้ค้างชำระ | 5 ลูกหนี้ | 0 | 9 | ic_trans, ap_ar_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6004` | รายงานลูกหนี้ค้างชำระ - แบบสรุป | 5 ลูกหนี้ | 0 | 10 | ic_trans, ap_ar_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6005` | รายงานสรุปการรับเงิน | 5 ลูกหนี้ | 0 | 28 | cb_trans, ar_customer, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6006` | รายงาน invoice ค้างชำระตามพนักงานขาย | 5 ลูกหนี้ | 0 | 7 | ic_trans, ap_ar_trans_detail, erp_user, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6007` | รายงานสมาชิกหมดอายุ | 5 ลูกหนี้ | 0 | 4 | ar_customer, ar_dealer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6008` | รายงานรายละเอียดลูกหนี้(สถานประกอบการ เลขประจำตัวผู้เสียภาษี) | 5 ลูกหนี้ | 0 | 5 | ar_customer, ar_customer_detail | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6009` | รายงานเอกสารค้างชำระตามพนักงานขาย | 5 ลูกหนี้ | 0 | 7 | ic_trans, ap_ar_trans_detail, erp_user, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6010` | รายงานยอดค้างชำระ ตามช่วงวันที่ | 5 ลูกหนี้ | 0 | 7 | ic_trans, ap_ar_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6011` | รายงานข้อมูลลูกหนี้ที่ไม่เป็นสมาชิก | 5 ลูกหนี้ | 0 | 4 | ar_customer, ar_dealer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6012` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน ตามพนักงานเก็บเงิน (แสดงรายละเอียด) | 5 ลูกหนี้ | 0 | 28 | ap_ar_trans, cb_trans_detail, erp_user, ar_customer, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6013` | รายงานรายละเอียดบัตรสมาชิก | 5 ลูกหนี้ | 0 | 16 | ar_customer, ar_customer_detail, ar_dealer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6014` | รายงานสมาชิกใหม่ | 5 ลูกหนี้ | 0 | 10 | ar_customer, ar_dealer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6015` | รายงานลูกค้าสินค้าหมายเหตุ | 5 ลูกหนี้ | 0 | 4 | ar_customer, ar_item_by_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6016` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียด) | 5 ลูกหนี้ | 0 | 33 | cb_trans_detail, ic_trans_detail, ap_ar_trans, erp_bank, ar_customer, cb_trans, erp_bank_branch | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6017` | รายงานกลุ่มลูกหนี้ผิดผลาด | 5 ลูกหนี้ | 0 | 7 | ar_customer_detail, ar_group_sub | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6018` | รายงานบันทึกตัดแต้มลูกหนี้ | 5 ลูกหนี้ | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6019` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียด) ตามรูปแบบเอกสาร | 5 ลูกหนี้ | 0 | 39 | ap_ar_trans, cb_trans_detail, ic_trans_detail, erp_bank, erp_bank_branch, ar_customer, cb_trans, erp_expenses_list | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6020` | รายงานเอกสารค้างชำระตามพนักงานขาย ตามรูปแบบเอกสาร | 5 ลูกหนี้ | 0 | 7 | ic_trans, ap_ar_trans_detail, erp_user, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6021` | รายงานแต้มคงเหลือยกมา | 5 ลูกหนี้ | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6022` | รายงานรายละเอียดลูกหนี้ (แสดงรายละเอียดเครดิต) | 5 ลูกหนี้ | 0 | 5 | ar_customer, ar_customer_detail | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6023` | รายงานแต้มคงเหลือลูกหนี้ แสดงเอกสารตามช่วงเวลา | 5 ลูกหนี้ | 0 | 31 | ic_trans, cb_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `6024` | รายงานข้อมูลลูกหนี้นำเข้า | 6 เงินสด/ธนาคาร | 0 | 2 | ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `69001` | รายงานรายละเอียดลูกค้า แสดงที่อยู่ และยอดขาย | 5 ลูกหนี้ | 0 | 7 | ic_trans, ar_customer, erp_tambon, erp_amper, erp_province | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `7001` | รายงานการจ่ายชำระค่าใช้จ่ายอื่น ๆ | 6 เงินสด/ธนาคาร | 0 | 18 | cb_trans_detail, ic_trans, ap_ar_trans, ap_supplier, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7002` | รายงานการรับชำระรายได้อื่น ๆ | 6 เงินสด/ธนาคาร | 0 | 18 | cb_trans_detail, ap_ar_trans, ic_trans, ar_customer, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7003` | รายงานค่าใช้จ่ายอื่นๆ ตามรหัสค่าใช้จ่าย | 6 เงินสด/ธนาคาร | 0 | 3 | ic_trans_detail, erp_expenses_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7004` | รายงานรายละเอียดเช็คจ่าย-ตามสถานะเช็ค | 6 เงินสด/ธนาคาร | 0 | 8 | ap_supplier, erp_bank, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7005` | รายงานรายละเอียดเช็ครับ-ตามสถานะเช็ค | 6 เงินสด/ธนาคาร | 0 | 9 | erp_bank, ar_customer, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7006` | รายงานสถานะบัตรเครดิต | 6 เงินสด/ธนาคาร | 0 | 8 | ap_supplier, erp_bank, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7007` | รายงานภาษีขายประจำเดือน | 6 เงินสด/ธนาคาร | 0 | 11 | ic_trans, gl_journal_vat_sale | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7008` | รายงานรายละเอียดเช็คจ่าย-ตามสถานะเช็คถึงวันที่ | 6 เงินสด/ธนาคาร | 0 | 8 | ap_supplier, erp_bank, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7009` | รายงานรายละเอียดเช็ครับ-ตามสถานะเช็คถึงวันที่ | 6 เงินสด/ธนาคาร | 0 | 9 | erp_bank, ar_customer, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7010` | รายงานยอดคงเหลือวงเงินสดย่อย | 6 เงินสด/ธนาคาร | 0 | 6 | cb_petty_cash, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7011` | รายการการจ่ายเงินสดย่อย | 6 เงินสด/ธนาคาร | 0 | 7 | cb_trans, cb_trans_detail, ap_supplier, cb_petty_cash | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7012` | รายงานการนำฝากเช็ครับตามสมุดเงินฝาก | 6 เงินสด/ธนาคาร | 0 | 21 | cb_chq_list, erp_bank, erp_bank_branch, ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7013` | รายงานเช็ครับผิดพลาด | 6 เงินสด/ธนาคาร | 0 | 8 | cb_chq_list, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7014` | รายงานนำฝากเช็ค เรียงตามวันที่นำฝาก | 6 เงินสด/ธนาคาร | 0 | 21 | cb_chq_list, erp_bank, erp_bank_branch, ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7015` | รายงานการชำระด้วยค่าใช้จ่ายอื่นๆ ตามรหัสค่าใช้จ่าย | 6 เงินสด/ธนาคาร | 0 | 10 | ap_supplier, ic_trans_detail, ar_customer, erp_expenses_list, cb_trans, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7017` | รายงานรายละเอียดลูกหนี้ | 5 ลูกหนี้ | 0 | 26 | ar_customer, erp_province, erp_amper, erp_tambon, ar_shoptype1, ar_shoptype2, ar_shoptype3, ar_shoptype4 | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `7018` | รายงานเคลื่อนไหวเงินสดย่อย | 6 เงินสด/ธนาคาร | 0 | 43 | ic_trans_detail, cb_trans_detail, cb_petty_cash, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `7019` | รายงานรายละเอียดธนาคาร | 6 เงินสด/ธนาคาร | 0 | 4 | erp_bank, erp_bank_branch | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `8001` | รายงานบัญชีแยกประเภทแบบสรุปเปรียบเทียบ 12 เดือน | 8 บัญชี (GL) | 0 | 7 | gl_chart_of_account, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8002` | รายงานรายการภาษีซื้อไม่ถึงกำหนดชำระ | 8 บัญชี (GL) | 0 | 11 | gl_journal_vat_buy | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8003` | รายงานภาษีขายไม่พบข้อมูลลูกหนี้ | 8 บัญชี (GL) | 0 | 4 | gl_journal_vat_sale, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8004` | รายงานตรวจสอบข้อมูลที่ยังไม่ได้บันทึกบัญชี | 8 บัญชี (GL) | 0 | 33 | gl_journal, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8005` | รายงานบัญชีแยกประเภท แสดงแผนก | 8 บัญชี (GL) | 0 | 24 | gl_chart_of_account, gl_journal_detail, gl_journal_depart_list, gl_journal, gl_journal_book | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8006` | รายงานข้อมูลรายวัน แสดงแผนก | 8 บัญชี (GL) | 0 | 8 | gl_journal_book, gl_journal, gl_journal_depart_list, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8007` | รายงานบัญชีแยกประเภท แยกสาขา | 8 บัญชี (GL) | 0 | 23 | gl_chart_of_account, gl_journal_detail, gl_journal_book, gl_journal, erp_branch_list, gl_journal_depart_list | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8008` | รายงานข้อมูลรายวัน แยกสาขา | 8 บัญชี (GL) | 0 | 9 | erp_branch_list, gl_journal_book, gl_journal, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8009` | รายงานภาษีขาย แยกสาขา | 8 บัญชี (GL) | 0 | 33 | ic_trans, ap_ar_trans, erp_branch_list, ar_customer, gl_journal_vat_sale, gl_journal | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8010` | รายงานภาษีซื้อ แยกสาขา | 8 บัญชี (GL) | 0 | 30 | ic_trans, ap_ar_trans, erp_branch_list, gl_journal, ap_supplier, gl_journal_vat_buy | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8011` | งบทดลอง แยกแผนก | 8 บัญชี (GL) | 0 | 26 | gl_journal_detail, gl_chart_of_account, gl_journal_depart_list, erp_department_list | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8012` | รายงานภาษีขาย แสดงใบกำกับภาษีอย่างเต็ม | 8 บัญชี (GL) | 0 | 38 | ic_trans, ar_customer, ap_ar_trans, gl_journal_vat_sale | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8013` | รายงานตรวจสอบการลงบัญชีที่ไม่ Balance | 8 บัญชี (GL) | 0 | 4 | gl_journal | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8014` | รายงานตรวจสอบข้อมูลรายวันทีไม่มีการลงบัญชี | 8 บัญชี (GL) | 0 | 6 | erp_doc_format, gl_journal, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8015` | รายงานภาษีซื้อ (รูปแบบใหม่แสดงมูลค่าอัตราภาษีศูนย์) | 8 บัญชี (GL) | 0 | 28 | ic_trans, ap_supplier_detail, ap_supplier, gl_journal_vat_buy | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8016` | รายงานภาษีถูกหัก ณ ที่จ่าย แสดงเลขที่เอกสาร | 8 บัญชี (GL) | 1 | 8 | ar_customer, ar_customer_detail, gl_wht_list_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8017` | งบทดลอง แยกสาขา | 8 บัญชี (GL) | 0 | 39 | erp_branch_list, gl_chart_of_account, gl_journal, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8018` | รายงานบัญชีแยกประเภท แยกสาขา แสดงรายละเอียดรายตัว | 8 บัญชี (GL) | 0 | 23 | gl_chart_of_account, gl_journal_detail, gl_journal_book, gl_journal, erp_branch_list, gl_journal_depart_list | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8019` | รายงานตรวจสอบการลงบัญชีและสินค้าคงเหลือ กรณีไม่แยกฝังบัญชี | 8 บัญชี (GL) | 0 | 16 | ic_trans, ic_trans_detail, ic_inventory, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8020` | รายงานภาษีขาย (รูปแบบใหม่) ตามวันที่ | 8 บัญชี (GL) | 0 | 34 | ap_ar_trans, ic_trans, ar_customer_detail, as_trans, ar_customer, gl_journal_vat_sale | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8021` | รายงานบัญชีแยกประเภท ตามโครงการ | 8 บัญชี (GL) | 0 | 30 | gl_journal_project_list, gl_journal_detail, gl_chart_of_account, gl_journal, gl_journal_book | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8022` | รายงานตรวจสอบการลงบัญชีและสินค้าคงเหลือ กรณีแยกฝังบัญชีรายสินค้า | 8 บัญชี (GL) | 0 | 15 | ic_inventory, ic_trans_detail, gl_journal_detail | รายงานอื่น ๆ (`menu_fastreport_other_gl`) |
| `8023` | รายงานการคืนเช็ค/ตั้งหนี้ใหม่ | 6 เงินสด/ธนาคาร | 0 | 4 | ar_customer, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `AP0001` | รายงานค้างจ่ายเจ้าหนี้ | 4 เจ้าหนี้ | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `AR0001` | รายงานค้างรับชำระ | 5 ลูกหนี้ | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B2007` | รายงานสินค้าและวัตถุดิบ คงเหลือยกมา แยกสาขา | 1 สินค้า | 0 | 19 | ic_trans, erp_branch_list, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B2016` | รายงานการเคลื่อนไหวตามปริมาณ แยกสาขา | 1 สินค้า | 0 | 47 | ic_trans_detail, ic_trans, ic_inventory, erp_branch_list, ic_unit, ic_unit_use | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B2025` | รายงานสินค้าที่ไม่มีการเคลื่อนไหว แยกสาขา | 1 สินค้า | 0 | 63 | ic_trans, ic_trans_detail, erp_branch_list, ic_unit, ic_unit_use, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B2029` | รายงานกำไรขั้นต้น (สินค้า) แยกสาขา | 1 สินค้า | 0 | 39 | ic_trans_detail, erp_branch_list, ic_unit, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B2037` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้า (แยกตามคลัง ที่เก็บ) แยกสาขา | 1 สินค้า | 0 | 33 | ic_inventory, erp_branch_list, ic_wh_shelf, ic_trans_detail, ic_group | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B2042` | รายงานสินค้าคงเหลือแสดงตามผู้จำหน่ายหลัก แยกสาขา | 1 สินค้า | 0 | 30 | ic_inventory, erp_branch_list, ic_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `B3017` | รายงานการซื้อสินค้าแยกตามสินค้า แยกสาขา | 2 ซื้อ | 0 | 10 | ic_trans_detail, erp_branch_list, ic_inventory, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `B4017` | รายงานยอดคงเหลือรับเงินล่วงหน้า แยกสาขา | 3 ขาย | 0 | 18 | ic_trans, erp_branch_list, ar_customer, cb_trans_detail, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4026` | รายงานการรับคืนสินค้า/ลดหนี้ แยกสาขา | 3 ขาย | 0 | 21 | erp_branch_list, ic_trans, ic_trans_detail, ar_customer, ic_inventory, ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4027` | รายงานขายบริการสินค้าและบริการ แยกสาขา | 3 ขาย | 0 | 20 | erp_branch_list, ic_trans, ar_customer, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4032` | รายงานประวัติการขายสินค้า แยกสาขา | 3 ขาย | 0 | 12 | ar_customer, erp_branch_list, ic_inventory, ic_unit, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4034` | รายงานสรุปยอดขายสินค้า-สรุปตามวันที่ แยกสาขา | 3 ขาย | 0 | 6 | erp_branch_list, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4052` | รายงานรวม INV_ ขายประจำวัน แยกสาขา | 3 ขาย | 0 | 10 | ic_trans, cb_trans, erp_branch_list | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4066` | รายงานการขายสินค้าแบบแจกแจงเป็นรายสินค้า ตามสาขา | 3 ขาย | 0 | 22 | ic_trans_detail, ic_inventory, ic_trans, erp_branch_list | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4066-1` | รายงานการขายสินค้าแบบแจกแจงเป็นรายสินค้า ตามสาขา แสดงยอดคงเหลือตามคลัง | 3 ขาย | 0 | 22 | ic_trans_detail, ic_inventory, ic_trans, erp_branch_list | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B4067` | รายงานจัดอันดับยอดขาย-ตามลูกค้า ตามสาขา | 3 ขาย | 0 | 5 | ic_trans_detail, erp_branch_list, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `B5012` | รายงานการจ่ายชำระหนี้ (แสดงรายละเอียด) แยกสาขา | 4 เจ้าหนี้ | 0 | 22 | ap_ar_trans, cb_trans_detail, erp_branch_list, ap_supplier, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `B6002` | รายงานใบส่งของค้างชำระ-ตามวันที่ แยกสาขา | 5 ลูกหนี้ | 0 | 12 | ap_ar_trans_detail, erp_branch_list, ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B6003` | รายงานสถานะลูกหนี้ แยกสาขา | 5 ลูกหนี้ | 0 | 104 | ic_trans, ap_ar_trans, erp_branch_list, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B6004` | รายงานอายุลูกหนี้-ตามเอกสาร(ว้นที่ครบกำหนด) แยกสาขา | 5 ลูกหนี้ | 0 | 20 | ap_ar_trans_detail, ic_trans, erp_branch_list, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B6005` | รายงานอายุลูกหนี้-ตามเอกสาร(ว้นที่เอกสาร) แยกสาขา | 5 ลูกหนี้ | 0 | 20 | ap_ar_trans_detail, ic_trans, erp_branch_list, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B6008` | รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน (แสดงรายละเอียด) แยกสาขา | 5 ลูกหนี้ | 0 | 23 | ap_ar_trans, cb_trans_detail, erp_branch_list, ar_customer, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B6013` | รายงานสรุปการรับเงิน | 5 ลูกหนี้ | 0 | 18 | cb_trans, ar_customer, ic_trans, ap_ar_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `B7002` | รายงานการจ่ายชำระค่าใช้จ่ายอื่น ๆ แยกสาขา | 6 เงินสด/ธนาคาร | 0 | 25 | ic_trans, cb_trans_detail, erp_branch_list, ap_supplier, erp_bank, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `B7005` | รายงานการฝากเงินสด แยกสาขา | 6 เงินสด/ธนาคาร | 0 | 8 | erp_branch_list, ic_trans, ic_trans_detail, erp_bank, erp_bank_branch | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `B7007` | รายงานการรับเงินทั้งหมดตามวันที่ แยกสาขา | 6 เงินสด/ธนาคาร | 0 | 15 | ic_trans, erp_branch_list, ap_ar_trans, ar_customer, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `B7010` | รายงานเคลื่อนไหวเงินสด แยกสาขา | 6 เงินสด/ธนาคาร | 0 | 13 | ic_trans, erp_branch_list, cb_trans, ap_ar_trans, ar_customer, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `BC2001` | รายงานเคลื่อนไหวสินค้า ตามคลัง | 1 สินค้า | 0 | 24 | ic_trans_detail, ic_inventory, ic_trans, ap_supplier, ar_customer, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `BC3001` | รายงานการสั่งซื้อสินค้าแบบแจกแจง-ตามสินค้า | 2 ซื้อ | 0 | 8 | ic_inventory, ap_supplier, ic_trans, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3002` | รายงานการซื้อสินค้าแบบสรุป-ตามโครงการ | 2 ซื้อ | 0 | 11 | ic_trans, erp_project_list, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3003` | รายงานการซื้อสินค้าแบบแจกแจง-ตามโครงการ | 2 ซื้อ | 0 | 13 | ic_trans, erp_project_list, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3004` | รายงานการอ้างอิงจากใบสั่งซื้อ | 2 ซื้อ | 0 | 7 | ic_trans, ap_supplier, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3005` | รายงานการอ้างอิงจากใบรับสินค้า | 2 ซื้อ | 0 | 7 | ic_trans, ap_supplier, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3006` | รายงานการซื้อสุทธิ-ตามยี่ห้อสินค้า | 2 ซื้อ | 0 | 8 | ic_brand, ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `BC3007` | รายงานวิเคราะห์การซื้อสุทธิ-ตามเจ้าหนี้ | 4 เจ้าหนี้ | 0 | 8 | ap_supplier, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `BC4001` | รายงานใบสั่งขาย/จองสินค้าที่ยังไม่ขาย | 3 ขาย | 0 | 6 | ic_trans_detail, erp_user, ic_trans, ic_inventory, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4002` | รายงานยอดสุทธิสรุปยอดขายตามลูกค้า - ตามพนักงานขาย | 3 ขาย | 0 | 10 | erp_user, ar_customer, ar_customer_detail, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4003` | รายงานสรุปยอดสินค้า-ตามเขตการขาย | 3 ขาย | 0 | 8 | ic_trans, ar_sale_area, ar_customer_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4004` | รายงานบันทึกขายสินค้า-บริการ | 3 ขาย | 0 | 6 | ar_customer, erp_user, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4005` | รายงานใบสั่งจองและใบสั่งขาย แสดงพนักงาน | 3 ขาย | 0 | 6 | ar_customer, erp_user, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4006` | รายงานจัดอันดับยอดขาย-ตามพนักงาน | 3 ขาย | 0 | 9 | ic_trans, ic_trans_detail, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4007` | รายงานจัดลำดับยอด ตามพนักงาน | 3 ขาย | 0 | 4 | erp_user, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4008` | รายงานใบส่งของค้างชำระ แยกตามแผนก | 3 ขาย | 0 | 12 | ap_ar_trans_detail, erp_department_list, ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4009` | รายงานการรับเงินประจำวัน แยกแผนก | 3 ขาย | 0 | 45 | ic_trans, ap_ar_trans, ar_customer, erp_department_list, ap_supplier, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4010` | รายงานการขายสุทธิ-ตามยี่ห้อสินค้า | 3 ขาย | 0 | 8 | ic_brand, ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `BC4011` | รายงานวิเคราะห์การขายสุทธิ-ตามแผนก | 3 ขาย | 0 | 10 | erp_department_list, ic_inventory, ic_unit, ic_trans_detail, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `CASH_IN` | รายงานการรับเงินทั้งหมดตามวันที่ | 6 เงินสด/ธนาคาร | 0 | 6 | ar_customer, cb_trans, ap_ar_trans, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `CASH_MOVEMENT` | รายงานเคลื่อนไหวเงินสด | 6 เงินสด/ธนาคาร | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `CASH_MOVEMENT01` | รายงานเคลื่อไหวเงินสด | 6 เงินสด/ธนาคาร | 0 | 3 | ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `CASH_OUT` | รายงานการจ่ายเงินทั้งหมดตามวันที่ | 6 เงินสด/ธนาคาร | 0 | 4 | cb_trans, ar_customer, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `IC_INVENTORY_NO_SALE` | รายงานสินค้าที่ไม่มีการขาย | 1 สินค้า | 0 | 3 | ic_inventory | สินค้า › วิเคราะห์ข้อมูล |
| `MANU_SINGHA_REPORT_AR_CUSTOMER` | รายงานรายละเอียดลูกหนี้ | 0 ทั่วไป | 0 | 26 | ar_customer, erp_province, erp_amper, erp_tambon, ar_shoptype1, ar_shoptype2, ar_shoptype3, ar_shoptype4 |  |
| `MENU_ADVANCE_MONEY_BALANCE_BRANCH` | รายงานยอดคงเหลือเงินมัดจำ ตามสาขา | 3 ขาย | 0 | 7 | ic_trans, ar_customer, cb_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ADVANCE_MONEY_CUT_BRANCH` | การงานการตัดเงินมัดจำ - แยกสาขา | 3 ขาย | 0 | 12 | ic_trans, cb_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ADVANCE_MONEY_RECRIVE_BRANCH` | รายงานการรับเงินมัดจำ - แยกสาขา | 3 ขาย | 0 | 7 | cb_trans, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ADVANCE_MONEY_RECRIVE_CANCEL_BRANCH` | รายงานยกเลิกรับเงินมัดจำ - แยกสาขา | 3 ขาย | 0 | 4 | ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ADVANCE_MONEY_RETURN_BRANCH` | รายงานคืนเงินมัดจำ - แยกสาขา | 3 ขาย | 0 | 7 | cb_trans, ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ADVANCE_MONEY_RETURN_CANCEL_BRANCH` | รายงานยกเลิกคืนเงินมัดจำ - แยกสาขา | 3 ขาย | 0 | 4 | ic_trans, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ANALYSIS_SELL_EX_BY_PRODUCT` | รายงานวิเคราะห์การขายแบบแจกแจง-ตามสินค้า | 3 ขาย | 0 | 4 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_ANALYSIS_SELL_SUM_BY_DOCNO` | รายงานวิเคราะห์การขายแบบสรุป-ตามเอกสาร | 3 ขาย | 0 | 4 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_AP_DETAIL_DEBT_BY_AP` | รายงานใบตั้งหนี้จากการซื้อแบบแจกแจงตามเจ้าหนี้ | 4 เจ้าหนี้ | 0 | 8 | ic_trans, ap_supplier, ic_trans_detail | เจ้าหนี้ › รายงานวิเคราะห์ |
| `MENU_AR_DEALER` | รายงานรายละเอียดสมาชิก | 5 ลูกหนี้ | 0 | 12 | ar_customer, ar_dealer | ลูกหนี้ › ข้อมูลลูกหนี้ |
| `MENU_AR_MAIN_REPORT` | รายงานข้อมูลลูกหนี้ | 5 ลูกหนี้ | 0 | 15 | ar_dealer, ar_customer, erp_tambon, erp_amper, erp_province | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `MENU_AR_MAIN_REPORT_BY_SALE` | รายงานข้อมูลลูกหนี้แสดงตามพนักงานขาย | 5 ลูกหนี้ | 0 | 13 | ar_customer_detail, ar_customer, erp_tambon, erp_amper, erp_province, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `MENU_AR_REPORT_INVOICE_REMAIN_PAY` | ใบส่งของค้างชำระ-ตามวันที่ | 0 ทั่วไป | 0 | 7 | ic_trans, ap_ar_trans_detail, ar_customer, ar_customer_detail | ลูกหนี้ › รายงานสรุป |
| `MENU_BILLING_OUTSTANDING` | รายงานใบรับวางบิลค่าสินค้าที่คงค้าง | 4 เจ้าหนี้ | 0 | 12 | ap_ar_trans, ap_ar_trans_detail, ap_supplier | เจ้าหนี้ › รายงาน/ยกเลิก |
| `MENU_BILLING_VALUE_BY_INVOICE` | รายงานใบรับวางบิลค่าสินค้า-ตามใบส่งของ | 0 ทั่วไป | 0 | 8 | ap_ar_trans, ap_supplier, ap_ar_trans_detail | เจ้าหนี้ › รายงาน/ยกเลิก |
| `MENU_BOOK_BANK_BALANCE` | รายงานยอดคงเหลือสมุดเงินฝาก | 6 เงินสด/ธนาคาร | 0 | 15 | erp_pass_book, cb_trans, ic_trans, ic_trans_detail, ar_customer, ap_supplier, cb_trans_detail, ap_ar_trans | เงินสด/ธนาคาร › ธนาคาร › รายงาน |
| `MENU_CB_REPORT_CHQ_IN_RECEIVE_BY_CHQ_GET_DATE` | รายงานรายละเอียดเช็ครับ-ตามวันที่รับ | 6 เงินสด/ธนาคาร | 0 | 9 | erp_bank, ar_customer, erp_bank_branch, cb_chq_list | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `MENU_CB_REPORT_CHQ_IN_RECEIVE_BY_DATE` | รายงานรายละเอียดเช็ครับ-ตามวันที่รับ-ตามสถานะเช็ค | 0 ทั่วไป | 0 | 9 | erp_bank, ar_customer, erp_bank_branch, cb_chq_list | เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก |
| `MENU_CB_REPORT_CHQ_OUT_PAYMENT_BY_DATE` | รายงานรายละเอียดเช็คจ่าย-ตามวันที่รับ-ตามสถานะเช็ค | 6 เงินสด/ธนาคาร | 0 | 8 | ap_supplier, erp_bank, erp_bank_branch, cb_chq_list | เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก |
| `MENU_CB_REPORT_PETTY_REQUEST` | รายงานการเบิกเงินสดย่อย | 6 เงินสด/ธนาคาร | 0 | 4 | ic_trans, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `MENU_CB_REPORT_PETTY_RETURN` | รายงานการรับคืนเงินสดย่อย | 6 เงินสด/ธนาคาร | 0 | 4 | ic_trans, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_cashbank`) |
| `MENU_COMPARE_SALE_WITH_PRICE` | รายงานการเทียบการขายกับราคาขาย | 0 ทั่วไป | 0 | 6 | ar_customer, ic_trans_detail, ic_inventory_price_formula | ขาย › รายงานวิเคราะห์ |
| `MENU_FAST_REPORT_ADDITIONAL_PRODUCT_PURCHASE_SUMMARY_BY_ITEM` | รายงานใบเพิ่มสินค้า(เจ้าหนี้)แบบสรุป-ตามสินค้า | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail |  |
| `MENU_FAST_REPORT_ANALYSIS_SELL_EX_BY_PRODUCT` | รายงานวิเคราเห์การขายแบบแจกแจง-ตามสินค้า | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ขาย › รายงานวิเคราะห์ |
| `MENU_FAST_REPORT_ANALYSIS_SELL_SUM_BY_DOCNO` | รายงานวิเคราะห์การขายแบบสรุป-ตามเลขที่เอกสาร | 0 ทั่วไป | 0 | 11 | ar_customer, gl_wht_list, ic_trans_detail, ic_trans, erp_option | ขาย › รายงานวิเคราะห์ |
| `MENU_FASTREPORT_AR_CUSTOMER` | รายงานข้อมูลลูกค้า | 5 ลูกหนี้ | 0 | 2 | ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `MENU_FAST_REPORT_COMPARE_PURCHASE_MONTHLY` | รายงานสรุปยอดซื้อ 12 เดือน ตามเจ้าหนี้ | 0 ทั่วไป | 0 | 0 |  |  |
| `MENU_FASTREPORT_CUSTOMER_MOVEMENT` | รายงานการเคลื่อนไหวลูกค้า | 0 ทั่วไป | 0 | 10 | ar_customer, ic_trans |  |
| `MENU_FASTREPORT_IC_INVENTORY` | รายงานข้อมูลสินค้า | 1 สินค้า | 0 | 2 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `menu_fastreport_invoice_cancel` | รายงานใบกำกับภาษีอย่างย่อยกเลิก | 0 ทั่วไป | 1 | 4 | ic_trans, ar_customer | ขาย POS › รายงาน/ยกเลิก |
| `MENU_FAST_REPORT_MARGIN_REACCEPTANCE` | รายงานกำไรขั้นต้นแสดงหักรับคืน | 0 ทั่วไป | 0 | 18 | ic_trans_detail, ic_inventory, ic_unit | ขาย › รายงานวิเคราะห์ |
| `MENU_FAST_REPORT_PRODUCT_RANK` | รายงานจัดอันดับยอดขาย-ตามสินค้า | 0 ทั่วไป | 0 | 5 | ic_inventory, ic_trans_detail | ขาย › รายงานวิเคราะห์ |
| `MENU_FAST_REPORT_PRODUCT_RANK_BY_CUST` | รายงานจัดอันดับยอดขาย-ตามลูกค้า | 3 ขาย | 0 | 4 | ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FAST_REPORT_PRODUCT_RANK_BY_SALE` | รายงานจัดอันดับยอดขาย-ตามพนักงาน | 3 ขาย | 0 | 12 | ic_trans, erp_user, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FAST_REPORT_PURCHASE_BY_TAX` | รายงานการซื้อสินค้าแจกแจงตามประเภทภาษี | 0 ทั่วไป | 0 | 6 | ic_trans, ic_inventory, ic_trans_detail |  |
| `MENU_FAST_REPORT_PURCHASE_DUE_DATE` | รายงานใบซื้อสินค้าที่ถึงกำหนดจ่ายเงิน | 0 ทั่วไป | 0 | 6 | ap_supplier, ic_unit, ic_trans |  |
| `MENU_FAST_REPORT_PURCHASE_SUMMARY_BY_DATE` | รายงานการซื้อสินค้าแบบสรุป-ตามวันที่ | 2 ซื้อ | 0 | 4 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_FAST_REPORT_PURCHASE_SUMMARY_BY_DATE_SHOW_PRICE` | รายงานการซื้อสินค้าแบบสรุป-ตามวันที่ แสดงราคาซื้อ | 2 ซื้อ | 0 | 4 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_FAST_REPORT_PURCHASE_SUMMARY_BY_DATE_SUPLIER` | รายงานการซื้อสินค้าแบบสรุป-ตามวันที่ เจ้าหนี้ | 2 ซื้อ | 0 | 6 | ap_supplier, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_FASTREPORT_RECEIVED_MONEY` | รายงานการรับเงิน | 0 ทั่วไป | 1 | 22 | ic_trans, ar_customer, cb_trans | ขาย POS › รายงาน/ยกเลิก |
| `MENU_FASTREPORT_RECEIVED_MONEY_SCG` | รายงานการรับเงิน | 0 ทั่วไป | 0 | 28 | ic_trans, ar_customer, cb_trans, cb_trans_detail, erp_option |  |
| `MENU_FAST_REPORT_SALE_BY_EMPLOYEE` | รายงานยอดขาย-ตามพนักงานขาย | 3 ขาย | 0 | 8 | erp_user, ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FAST_REPORT_SALE_HISTORY_PRODUCT` | รายงานประวัติการขายสินค้า | 3 ขาย | 0 | 6 | ic_inventory, ar_customer, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FASTREPORT_SERVICE_CHARGE_INCOME` | รายงานรายได้จาก Service Charge | 3 ขาย | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FASTREPORT_SERVICE_CHARGE_INCOME_CASH` | รายงานรายได้จาก Service Charge - ชำระเงินด้วยเงินสด | 3 ขาย | 0 | 10 | cb_trans, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FASTREPORT_SERVICE_CHARGE_INCOME_CREDIT` | รายงานรายได้จาก Service Charge - ชำระเงินด้วยบัตรเครคิต | 3 ขาย | 0 | 10 | cb_trans, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FAST_REPORT_SHIPMENTS_COMPARE_MONTH` | รายงานเปรียบเทียบยอดขายสินค้า 12 เดือน | 3 ขาย | 0 | 2 |  | ขาย › รายงานวิเคราะห์ |
| `MENU_FAST_REPORT_SHIPMENTS_QTY_COMPARE_MONTH` | รายงานเปรียบเทียบปริมาณขายสินค้า 12 เดือน | 3 ขาย | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_FAST_REPORT_SUMMARY_CREDIT_NOTE_BY_ITEM` | รายงานการส่งคืนสินค้า-ลดหนี้แบบสรุป-ตามสินค้า | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail |  |
| `MENU_FAST_REPORT_SUMMARY_SELL_BY_SALE` | รายงานสรุปยอดขายสินค้าสุทธิตามพนักงานขาย | 0 ทั่วไป | 0 | 10 | ic_trans, erp_user, ic_trans_detail, erp_option | ขาย › รายงานสรุป |
| `MENU_FAST_REPORT_SUMMARY_SELL_BY_SALE_BY_GROUP` | รายงานสรุปยอดขายสินค้าสุทธิตามพนักงานขาย แสดงตามหมวดสินค้า | 3 ขาย | 0 | 14 | ic_inventory, ic_trans, erp_user, ic_trans_detail, ic_category | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_GL_CHECK_NO_BRACNCH` | รายงานตรวจสอบรายการรายวัน ไม่พบรายละเอียดสาขา | 0 ทั่วไป | 0 | 3 | gl_journal_detail, erp_branch_list | รายงาน › ข้อมูลทั่วไป |
| `MENU_IC_BALANCE_WAREHOUSE_FOR_CENTER` | รายงานยอดคงเหลือสินค้าตามคลัง สำหรับระบบ Sync | 1 สินค้า | 0 | 20 | ic_trans, ic_inventory, ic_trans_detail, ic_warehouse, ic_unit, ic_unit_use, ic_inventory_barcode | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `MENU_IC_REPORT_POS_SALE_GROUP_BY_ITEM` | รายงานสรุปการขายสินค้าหน้าร้าน รวมรายการสินค้า | 0 ทั่วไป | 0 | 5 | ic_inventory, ic_trans_detail, ic_trans |  |
| `MENU_IC_REPORT_SALE_REMAIN` | รายงานสรุปยอดสินค้าค้างส่ง | 0 ทั่วไป | 0 | 16 | ic_trans_detail, erp_option, ic_trans, ic_inventory, ar_customer | สินค้า › รายงานวิเคราะห์ |
| `MENU_INVOICE_ARREARS_BY_DATE` | รายงานใบส่งของค้างจ่ายชำระ-ตามวันที่ | 0 ทั่วไป | 0 | 6 | ic_trans, ap_ar_trans_detail, ap_supplier | เจ้าหนี้ › รายงานสรุป |
| `MENU_INVOICE_ARREARS_DUE` | รายงานใบส่งของค้างชำระแสดงวันที่ถึงกำหนด | 4 เจ้าหนี้ | 0 | 6 | ic_trans, ap_ar_trans_detail, ap_supplier | เจ้าหนี้ › รายงานสรุป |
| `MENU_INVOICE_DUE_BY_DATE` | รายงานใบส่งของถึงกำหนดชำระ-ตามวันที่ | 4 เจ้าหนี้ | 0 | 6 | ic_trans, ap_ar_trans_detail, ap_supplier | เจ้าหนี้ › รายงานสรุป |
| `MENU_INVOICE_OVERDUE_BY_DATE` | รายงานใบส่งของเกินกำหนดชำระ-ตามวันที่ | 4 เจ้าหนี้ | 0 | 6 | ic_trans, ap_ar_trans_detail, ap_supplier | เจ้าหนี้ › รายงานสรุป |
| `MENU_PAYMENT_BY_DATE` | รายงานการจ่ายชำระประจำวัน-ตามวันที่ | 0 ทั่วไป | 0 | 5 | cb_trans, ap_supplier, ap_ar_trans, ic_trans | เจ้าหนี้ › รายงานสรุป |
| `MENU_PAYMENT_BY_DEPARTMENT` | รายงานการจ่ายเงินประจำวัน-ตามแผนก | 0 ทั่วไป | 0 | 16 | ic_trans, ap_ar_trans, erp_department_list, cb_trans, ap_supplier | เจ้าหนี้ › รายงานสรุป |
| `MENU_PAYMENT_BY_INVOICE` | รายงานจ่ายชำระสินค้า-ตามใบส่งของ | 0 ทั่วไป | 0 | 8 | ap_ar_trans, ap_supplier, ap_ar_trans_detail | เจ้าหนี้ › รายงานสรุป |
| `MENU_PO_REPORT_COMPARE_PURCHASE_MO` | รายงานการเปรียบเทียบยอดซื้อสินค้า 12 เดือน (ตามสินค้า-ราคา/ปริมาณ) | 0 ทั่วไป | 0 | 2 |  |  |
| `MENU_PO_REPORT_COMPARE_PURCHASE_MONTHLY` | รายงานการเปรียบเทียบยอดซื้อสินค้า 12 เดือน (ตามสินค้า-ราคา/ปริมาณ) | 0 ทั่วไป | 0 | 2 |  | ซื้อ › รายงานวิเคราะห์ |
| `MENU_PO_REPORT_COMPARE_PURCHASE_MONTHLY_QTY` | รายงานการเปรียบเทียบยอดซื้อสินค้า 12 เดือน ตามปริมาณ | 2 ซื้อ | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_PO_REPORT_COMPARE_PURCHASE_MONTHLY_QTY_SUPPLIER` | รายงานการเปรียบเทียบยอดซื้อสินค้า 12 เดือน ตามปริมาณ ตามผุ้จำหน่ายหลัก | 2 ซื้อ | 0 | 6 | ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_PO_REPORT_PURCHASE_ANALYZE` | รายงานวิเคราะห์การซื้อสุทธิ์-ตามสินค้า | 0 ทั่วไป | 0 | 8 | ic_inventory, ic_trans_detail | ซื้อ › รายงานวิเคราะห์ |
| `MENU_POS_PERIOD_STATUS` | รายงานแสดงสถานะการเปิด-ปิด กะ | 3 ขาย | 0 | 4 | pos_period, erp_user | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_POS_SALE_DETAIL_001` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามวันที่ | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_002` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามลูกค้า | 0 ทั่วไป | 0 | 7 | ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_003` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามรหัส | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_004` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามยี่ห้อสินค้า | 3 ขาย | 0 | 12 | ic_inventory, ar_customer, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_005` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามพนักงาน | 0 ทั่วไป | 0 | 11 | ic_trans, ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_006` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแผนก | 0 ทั่วไป | 0 | 11 | ic_trans, erp_department_list, ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_007` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามประเภทลูกค้า | 0 ทั่วไป | 0 | 14 | ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_008` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามแคชเชียร์ | 0 ทั่วไป | 0 | 12 | ic_trans, ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_009` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มสินค้า | 3 ขาย | 0 | 12 | ic_inventory, ar_customer, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_010` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามกลุ่มลูกค้า | 0 ทั่วไป | 0 | 12 | ar_customer_detail, ic_inventory, ar_customer, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์การขายแบบแจกแจง |
| `MENU_POS_SALE_DETAIL_011` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามหมวดสินค้า | 3 ขาย | 0 | 11 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_POS_SALE_DETAIL_012` | รายงานวิเคราะห์ยอดขายสินค้าแบบแจกแจง-เรียงตามรูปแบบสินค้า | 3 ขาย | 0 | 11 | ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_POS_SUMARY_001` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-เรียงตามแคชเชียร์ | 0 ทั่วไป | 0 | 10 | ic_trans, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_002` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามวันที่ | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_003` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามลูกค้า | 0 ทั่วไป | 0 | 8 | ar_customer, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_004` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามยี่ห้อสินค้า | 0 ทั่วไป | 0 | 10 | ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_005` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย | 0 ทั่วไป | 0 | 10 | ic_trans, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_006` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามแผนก | 0 ทั่วไป | 0 | 8 | erp_department_list, ic_inventory, ic_trans_detail |  |
| `MENU_POS_SUMARY_007` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามประเภทลูกค้า | 0 ทั่วไป | 0 | 10 | ar_customer, ic_inventory, ic_trans_detail |  |
| `MENU_POS_SUMARY_008` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มสินค้า | 0 ทั่วไป | 0 | 10 | ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_009` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามกลุ่มลูกค้า | 0 ทั่วไป | 0 | 8 | ar_customer_detail, ic_inventory, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก › รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป |
| `MENU_POS_SUMARY_010` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย (เทียบราคากลาง) | 3 ขาย | 0 | 15 | ic_trans, ic_inventory_price_formula, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_POS_SUMARY_011` | รายงานวิเคราะห์ยอดขายสินค้าแบบสรุป-ตามพนักงานขาย (เทียบราคากลาง) 2 | 3 ขาย | 0 | 15 | ic_trans, ic_inventory_price_formula, ic_inventory, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_POS_SUM_FRONT` | รายงานสรุปการขายหน้าร้าน | 0 ทั่วไป | 1 | 4 | ar_customer, ic_trans | ขาย POS › รายงาน/ยกเลิก |
| `MENU_POS_SUM_FRONT_SCG` | รายงานสรุปการขายหน้าร้าน | 0 ทั่วไป | 0 | 5 | ar_customer, ic_trans, erp_option |  |
| `MENU_POS_SUM_FULL_VAT` | รายงานสรุปใบกำกับภาษีอย่างเต็ม | 0 ทั่วไป | 0 | 4 | ar_customer, ic_trans | ขาย POS › รายงาน/ยกเลิก |
| `MENU_POS_SUM_SHORT_VAT` | รายงานสรุปใบกำกับภาษีอย่างย่อ | 3 ขาย | 1 | 6 | ar_customer, ic_trans, ic_trans_detail | ขาย POS › รายงาน/ยกเลิก |
| `MENU_POS_SUM_SHORT_VAT_SALE_SHIFT` | รายงานสรุปรายการใบกำกับภาษีอย่างย่อ ตามรอบการขาย | 3 ขาย | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_PRODUCT_SALE_LOSS` | รายงานสินค้าขายต่ำกว่าทุน | 0 ทั่วไป | 0 | 6 | ic_inventory, ar_customer, ic_trans_detail | ขาย › รายงานวิเคราะห์ |
| `MENU_REPORT_ACCRUED_IN_QTY` | รายงานสรุปยอดสินค้าค้างรับ | 0 ทั่วไป | 0 | 12 | ic_trans_detail, ap_supplier, ic_inventory, erp_option, ic_trans | สินค้า › รายงานวิเคราะห์ |
| `MENU_REPORT_AR_PAYMENT_PAY_DETAIL` | รายงานการรับชำระหนี้ / ออกใบเสร็จรับเงิน (แสดงรายละเอียดการรับเงิน) | 0 ทั่วไป | 0 | 4 | ap_ar_trans_detail, ap_ar_trans, cb_trans, ar_customer | ลูกหนี้ › รายงาน/ยกเลิก |
| `MENU_REPORT_CASH_PAYIN` | รายการการฝากเงินสด | 6 เงินสด/ธนาคาร | 0 | 7 | ic_trans_detail, ic_trans, erp_bank, erp_bank_branch | เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก |
| `MENU_REPORT_CASH_WITHDRAW` | รายงานการถอนเงินสด | 6 เงินสด/ธนาคาร | 0 | 6 | ic_trans, ic_trans_detail, erp_bank, erp_bank_branch | เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก |
| `MENU_REPORT_CB_PETTY_CASH_REQUEST` | รายงานการเบิกเงินสดย่อย | 0 ทั่วไป | 0 | 4 | ic_trans, ic_trans_detail | เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงาน/ยกเลิก |
| `MENU_REPORT_CB_PETTY_CASH_RETURN` | รายงานการรับคืนเงินสดย่อย | 0 ทั่วไป | 0 | 4 | ic_trans, ic_trans_detail | เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงาน/ยกเลิก |
| `MENU_REPORT_CHECK_VAT_BUY` | ตรวจสอบเลขที่ใบกำกับภาษีซื้อ | 2 ซื้อ | 0 | 3 | gl_journal_vat_buy, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `MENU_REPORT_CHQ_CARD_ENDDATE_CARD` | รายงานรายละเอียดบัตรครดิต-ตามวันที่รับ | 6 เงินสด/ธนาคาร | 0 | 8 | erp_bank, erp_bank_branch, cb_chq_list, ap_supplier, ar_customer | เงินสด/ธนาคาร › ธนาคาร › บัตรเครดิต |
| `MENU_REPORT_CHQ_PAY_DUE_DATE` | รายงานรายละเอียดเช็คจ่าย-ตามวันครบกำหนด | 6 เงินสด/ธนาคาร | 0 | 5 | cb_chq_list, ap_supplier, erp_bank, erp_bank_branch | เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก |
| `MENU_REPORT_CHQ_RECEIVE_DUE_DATE` | รายงานรายละเอียดเช็ครับ-ตามวันครบกำหนด | 0 ทั่วไป | 0 | 5 | cb_chq_list, ar_customer, erp_bank, erp_bank_branch | เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก |
| `MENU_REPORT_CUSTOMER_POINT_BALANCE` | รายงานแต้มคงเหลือสมาชิก | 0 ทั่วไป | 0 | 12 | ic_trans, cb_trans, ar_customer |  |
| `menu_report_employee_group` | รายงานพนักงานเรียงตามกลุ่ม | 0 ทั่วไป | 1 | 9 | erp_user, erp_user_group, erp_user_group_detail | เริ่มต้น › รายละเอียดข้อมูลทั่วไป |
| `MENU_REPORT_IC_STOCK_BALANCE_LOCATION_MAX` | รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง-จุดเก็บ | 0 ทั่วไป | 0 | 2 |  | สินค้า › รายงานวิเคราะห์ |
| `MENU_REPORT_IC_STOCK_BALANCE_LOCATION_MIN` | รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง-จุดเก็บ | 0 ทั่วไป | 0 | 2 |  | สินค้า › รายงานวิเคราะห์ |
| `MENU_REPORT_IC_STOCK_BALANCE_WAREHOUSE_MAX` | รายงานสินค้าถึงจุดสูงสุด แยกตามคลัง | 0 ทั่วไป | 0 | 2 |  | สินค้า › รายงานวิเคราะห์ |
| `MENU_REPORT_IC_STOCK_BALANCE_WAREHOUSE_MIN` | รายงานสินค้าถึงจุดต่ำสุด แยกตามคลัง | 0 ทั่วไป | 0 | 2 |  | สินค้า › รายงานวิเคราะห์ |
| `MENU_REPORT_INVENTORY_ADJUST` | รายงานการปรับปรุงยอดสินค้า | 1 สินค้า | 0 | 3 | ic_trans_detail, ic_inventory | สินค้า › รายงานสรุป |
| `MENU_REPORT_LOT_INVENTORY` | รายงาน Lot สินค้า | 1 สินค้า | 0 | 13 | ic_trans_detail_lot, ic_inventory, ic_unit, ic_unit_use | สินค้า › รายงานสรุป |
| `MENU_REPORT_PURCHASE_ADD_BY_DATE` | รายงานใบเพิ่มสินค้า(เจ้าหนี้)แบบสรุป-ตามวันที่ | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ซื้อ › รายงานสรุป |
| `MENU_REPORT_PURCHASE_BY_DATE` | รายงานยอดซื้อตามวันที่ | 0 ทั่วไป | 0 | 4 | ap_supplier, ic_trans | ซื้อ › รายงานสรุป |
| `MENU_REPORT_PURCHASE_CREDIT_BY_DATE` | รายงานใบตั้งหนี้จากการซื้อแบบสรุป-ตามวันที่ | 0 ทั่วไป | 0 | 3 | ic_trans, ap_supplier | ซื้อ › รายงานสรุป |
| `MENU_REPORT_PURCHASE_CREDIT_NOTE_BY_ITEM` | รายงานการส่งคืนสินค้า/ลดหนี้แบบสรุป-ตามสินค้า | 0 ทั่วไป | 0 | 4 | ic_inventory, ic_trans_detail | ซื้อ › รายงานสรุป |
| `menu_report_purchase_order_by_date` | รายงานการสั่งซื้อสินค้าแบบสรุป-ตามวันที่ | 0 ทั่วไป | 1 | 3 | ic_trans_detail, ic_inventory | ซื้อ › รายงานสรุป |
| `MENU_REPORT_PURCHASE_RANK_ITEM_GROUP` | รายงานการจัดอันดับยอดซื้อ(ตามสินค้า-กลุ่มสินค้า) | 0 ทั่วไป | 0 | 6 | ic_inventory, ic_trans_detail | ซื้อ › รายงานวิเคราะห์ |
| `MENU_REPORT_PURCHSE_ON_DUE` | รายงานใบซื้อสินค้าที่ถึงกำหนดจ่ายเงิน | 0 ทั่วไป | 0 | 8 | ic_trans, ap_supplier, ic_trans_detail, ic_inventory | ซื้อ › รายงานสรุป |
| `MENU_REPORT_RECEIVE_MONEY_CREDIT_BY_DATE` | รายงานการรับเงินบัตรเครดิต ตามวันที่ | 3 ขาย | 0 | 3 | cb_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_REPORT_RECEIVE_MONEY_SUMMARY` | รายงานสรุป การบันทึก รับเงินจากการขาย/รับชำระหนี้ | 0 ทั่วไป | 0 | 2 | cb_trans, ar_customer | ลูกหนี้ › รายงานสรุป |
| `MENU_REPORT_REGISTER_MEMBER_BY_DATE` | รายงานจำนวนสมาชิกตามวันที่ | 0 ทั่วไป | 0 | 2 | ar_dealer |  |
| `MENU_REPORT_SALE_VIEW_SERIAL_NUMBER` | รายการการขายสินค้าและบริการ แสดง Serial Number | 3 ขาย | 0 | 8 | ic_trans, ic_trans_detail, ic_trans_serial_number, ic_warehouse, ic_shelf | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_REPORT_SINGHA_LOGS_TRANS` | รายงานการตรวจสอบการแก้ไขข้อมูลย้อนหลัง | 0 ทั่วไป | 0 | 14 | ap_ar_trans, ic_trans, logs | รายงาน › ข้อมูลทั่วไป |
| `MENU_REPORT_SUMMARY_ORDER_KITCHEN` | รายงานสรุปการสั่งอาหาร ห้องครัว/บาร์น้ำ | 3 ขาย | 0 | 9 | table_order, ic_inventory, ic_unit_use, kitchen_master, ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_REPORT_SUM_PURCHASE_BY_VAT` | รายงานการซื้อสินค้าสรุปตามประเภทภาษี | 0 ทั่วไป | 0 | 2 | ic_trans_detail | ซื้อ › รายงานสรุป |
| `MENU_REPORT_SUPPLIER_UNCASH` | รายงานเจ้าหนี้ค้างจ่ายชำระ | 4 เจ้าหนี้ | 0 | 10 | ic_trans, ap_ar_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `MENU_REPORT_SUPPLIER_UNCASH_2` | รายงานเจ้าหนี้ค้างจ่ายชำระ | 4 เจ้าหนี้ | 0 | 10 | ic_trans, ap_ar_trans_detail, ap_supplier | รายงานอื่น ๆ (`menu_fastreport_other_supplier`) |
| `MENU_SALE_HISTORY_PRODUCT` | รายงานประวัติการขายสินค้า | 3 ขาย | 1 | 5 | ic_trans_detail, ic_inventory, ar_customer | ขาย › รายงานสรุป |
| `MENU_SCG_PRODUCT_SALE_LOSS` | รายงานสินค้าขายต่ำกว่าทุน | 0 ทั่วไป | 0 | 6 | ic_inventory, ar_customer, ic_trans_detail |  |
| `MENU_SCG_REPORT_SUMMARY_PAYMENT` | รายงานสรุปการจ่ายเงิน | 0 ทั่วไป | 0 | 2 | cb_trans |  |
| `MENU_SHIPMENTS_BY_DATE` | รายงานสรุปยอดขายสินค้า-สรุปตามวันที่ | 3 ขาย | 0 | 3 | ic_trans | ขาย › รายงานสรุป |
| `MENU_SINGHA_REPORT_AGING_DEPOSIT` | aging ของฝาก | 0 ทั่วไป | 0 | 30 | ic_unit_use, ic_wms_trans_detail, ic_inventory, ar_customer, ic_wms_trans |  |
| `MENU_SINGHA_REPORT_AMOUNT_SALE_CUSTOMER` | รายงานสรุปมูลค่าการขาย 12 เดือน แยกตามลูกค้า | 0 ทั่วไป | 0 | 7 | gl_journal_detail, ar_customer, ic_trans_detail, ar_customer_detail |  |
| `MENU_SINGHA_REPORT_ANALYST_SALE_AREA` | ยอดขายสินค้า ตามพื้นที่ | 0 ทั่วไป | 0 | 24 | ar_customer, ic_unit_use, ic_inventory, ic_trans_detail, ic_report_sort_item, ar_customer_detail | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_ANALYST_SALE_CUSTOMER` | ยอดขายสินค้า วิเคราะห์ตามลูกค้า | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_ANALYST_SALE_CUSTOMER_CUT_RETURN` | ยอดขายสินค้า วิเคราะห์ตามลูกค้า หักรับคืน | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_AP_PURCHASE_SUMMARY_PRODUCT` | สรุปยอดซื้อสินค้า วิเคราะห์ตามผู้ขาย | 0 ทั่วไป | 0 | 12 | ic_trans, ic_unit_use, ap_supplier, ic_trans_detail | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_AR_CUSTOMER` | รายงานรายละเอียดลูกหนี้ | 0 ทั่วไป | 0 | 78 | ar_customer_detail, erp_province, erp_amper, erp_tambon, ar_tier, ar_shoptype1, ar_shoptype2, ar_shoptype3 |  |
| `MENU_SINGHA_REPORT_AR_SALE_CARD` | การ์ดลูกค้า | 0 ทั่วไป | 0 | 9 | ic_unit_use, ar_customer, ic_trans_detail | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_BALANCE_QTY_WH_SHELF` | รายงานสินค้าคงเหลือแสดงตามพื้นที่เก็บ | 0 ทั่วไป | 0 | 33 | ic_unit_use, ic_inventory, ic_trans_detail, ic_unit |  |
| `MENU_SINGHA_REPORT_BANK_STATEMENT_SHOW_PAYMENT_DETAIL` | รายงาน Bank Statement แสดงช่องทางการจ่ายเงิน | 0 ทั่วไป | 0 | 40 | ic_trans, erp_pass_book, ap_supplier, ar_customer, ap_ar_trans, cb_trans, ic_trans_detail, ap_supplier_detail | รายงาน › เงินสด/ธนาคาร |
| `MENU_SINGHA_REPORT_CANCEL_DOC` | รายงานการยกเลิกเอกสาร | 0 ทั่วไป | 0 | 14 | erp_cancel_logs, ic_trans, ap_ar_trans | รายงาน › ข้อมูลทั่วไป |
| `MENU_SINGHA_REPORT_CHEQUEIN_BALANCE` | สรุปยอดรับเช็คคงเหลือ | 0 ทั่วไป | 0 | 6 | ar_customer, cb_chq_list, ic_trans, ap_ar_trans | รายงาน › เงินสด/ธนาคาร › เช็ครับ |
| `MENU_SINGHA_REPORT_CHEQUEIN_DEPOSIT` | สรุปยอดรับเช็ค  ส่งเข้าธนาคาร | 0 ทั่วไป | 0 | 13 | cb_chq_list, ar_customer, ic_trans_detail | รายงาน › เงินสด/ธนาคาร › เช็ครับ |
| `MENU_SINGHA_REPORT_CHEQUEIN_LIST` | ทะเบียนรับเช็ค | 0 ทั่วไป | 0 | 6 | ar_customer, cb_chq_list, ic_trans, ap_ar_trans | รายงาน › เงินสด/ธนาคาร › เช็ครับ |
| `MENU_SINGHA_REPORT_CHEQUEIN_PASS` | สรุปเช็ครับล่วงหน้า (ผ่าน) | 0 ทั่วไป | 0 | 13 | cb_chq_list, ar_customer, ic_trans_detail | รายงาน › เงินสด/ธนาคาร › เช็ครับ |
| `MENU_SINGHA_REPORT_CHQ_IN_RETURN` | รายงานรับคืน (เช็ครับ) | 0 ทั่วไป | 0 | 10 | cb_chq_list, ic_trans, ic_trans_detail, erp_bank, ar_customer | รายงาน › เงินสด/ธนาคาร › เช็ครับ |
| `MENU_SINGHA_REPORT_CREDIT_MONEY_CHECK` | รายงานตรวจสอบยอดวงเงิน | 0 ทั่วไป | 0 | 9 | ar_customer, ar_customer_detail, ic_trans | รายงาน › ลูกหนี้ |
| `MENU_SINGHA_REPORT_DEPART_RETURN` | รายงานการ์ดสินค้า เบิก-รับคืน (อ้างอิงลูกหนี้) | 0 ทั่วไป | 0 | 32 | ic_trans_detail, ar_customer, ic_inventory, ic_warehouse, ic_shelf |  |
| `MENU_SINGHA_REPORT_DEPART_SHOWNAME` | รายงานการเบิกสินค้า แสดงชื่อลูกค้า | 0 ทั่วไป | 0 | 12 | ic_trans, ar_customer, ic_trans_detail, ic_unit |  |
| `MENU_SINGHA_REPORT_DEPOSIT_CARD` | รายงานการ์ดสินค้าฝาก | 0 ทั่วไป | 0 | 40 | ic_unit_use, ic_wms_trans_detail, ic_unit, ar_customer, ic_warehouse, ic_shelf, ic_inventory |  |
| `MENU_SINGHA_REPORT_IC_DEPOSIT_SUMMARY` | สรุปสินค้าฝาก - ค้างส่ง | 0 ทั่วไป | 0 | 12 | ic_unit_use, ic_wms_trans_detail, ic_inventory, ar_customer |  |
| `MENU_SINGHA_REPORT_OTHER_EXPENSES` | รายงานค่าใช้จ่ายอื่น ๆ | 0 ทั่วไป | 0 | 9 | gl_journal_vat_buy, ic_trans, ic_trans_detail, ap_supplier | รายงาน › เงินสด/ธนาคาร |
| `MENU_SINGHA_REPORT_PRICE_LAST_BUY` | ราคาซื้อสินค้าล่าสุด | 0 ทั่วไป | 0 | 12 | ic_trans_detail, ap_supplier, ic_inventory | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_PRODUCT` | รายการรับสินค้ากรณีอื่นๆ โดยระเอียด | 0 ทั่วไป | 0 | 10 | ic_trans, ic_unit_use, ic_trans_detail |  |
| `MENU_SINGHA_REPORT_PRODUCT_MOVEMENT_STORE` | รายงานสโตร์ | 0 ทั่วไป | 0 | 33 | ic_unit_use, ic_inventory, ic_trans_detail, ic_unit, ic_report_sort_item, ic_trans | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_OUT_OTHER` | รายการจ่ายสินค้ากรณีอื่นๆ โดยระเอียด | 0 ทั่วไป | 0 | 17 | ic_trans, ic_unit_use, ic_trans_detail | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_RECEIVE` | รายการรับสินค้ากรณีอื่นๆโดยระเอียด | 0 ทั่วไป | 0 | 16 | ic_unit_use, ic_trans, ic_trans_detail | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_RECEIVE_BY_BRANCH` | รายงานรับสินค้า แยกสาขา | 0 ทั่วไป | 0 | 20 | erp_branch_list, ic_trans, ap_supplier, ic_inventory, ic_unit, ic_trans_detail | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_PRODUCT_SUM_OUT_BY_DAY` | สรุปยอดจ่ายสินค้าออกจากคลัง | 0 ทั่วไป | 0 | 26 | ic_unit_use, ic_unit, ic_inventory, ic_trans_detail, ic_report_sort_item | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_SUM_TRANSFER` | รับโอนสินค้าสรุปตามคลัง | 0 ทั่วไป | 0 | 29 | ic_unit_use, ic_trans, ic_trans_detail, ic_inventory, ic_unit | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_SUM_TRANSFEROUT` | จ่ายโอนสินค้าสรุปตามคลัง | 0 ทั่วไป | 0 | 29 | ic_unit_use, ic_trans, ic_trans_detail, ic_inventory, ic_unit | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PRODUCT_TRANSFER` | รายงานการโอนสินค้าและวัตถุดิบ | 0 ทั่วไป | 0 | 3 | ic_trans_detail, ic_trans, ic_report_sort_item | รายงาน › สินค้า |
| `MENU_SINGHA_REPORT_PU_BY_PRODUCT` | รายงานสรุปยอดซื้อจากผู้ขาย วิเคราะห์ตามสินค้า | 0 ทั่วไป | 0 | 19 | ic_unit_use, ic_inventory, ic_trans_detail, ar_customer, ap_supplier, ic_trans | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_SALE_BOX_LITRE` | รายงานยอดขาย (ลิตร) | 3 ขาย | 0 | 14 | ic_unit_use, ic_inventory, ic_unit, ic_trans_detail, ic_report_sort_item | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `MENU_SINGHA_REPORT_SALE_BY_BRANCH` | รายงานสรุปยอดขายสินค้าเรียงตามสาขา | 0 ทั่วไป | 0 | 22 | ic_unit_use, ic_trans, erp_branch_list, ic_inventory, ic_trans_detail, ar_customer | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_HISTORY_BRANCH` | รายงานประวัติการขายสินค้า แยกสาขา | 0 ทั่วไป | 0 | 16 | ic_trans, ar_customer, erp_branch_list, ic_inventory, ic_unit, ic_trans_detail | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_INVOICE` | สรุปรายละเอียดการขาย/เก็บเงิน รายบิล | 0 ทั่วไป | 0 | 9 | cb_trans, ar_customer, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_INVOICE_BY_CREDIT_DAY` | สรุปรายละเอียดการขาย/เก็บเงิน รายบิล ตามระยะเวลาเครดิต | 0 ทั่วไป | 0 | 10 | cb_trans, ar_customer, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_INVOICE_SHOWREMARK` | สรุปรายละเอียดการขาย/เก็บเงิน รายบิล | 0 ทั่วไป | 0 | 9 | cb_trans, ar_customer, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_PREMIUM_BY_DATE` | รายงานสรุปขาย/แถมรายวัน | 0 ทั่วไป | 0 | 17 | ic_unit_use, ic_inventory, ic_trans_detail, ar_customer | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_SUMMARY_BYPRODUCT` | สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_SUMMARY_BYPRODUCT_ADD_SALE_CODE` | สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (เพิ่มรหัสพนักงานขาย) | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans |  |
| `MENU_SINGHA_REPORT_SALE_SUMMARY_BYPRODUCT_ARM` | สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (ARM) | 0 ทั่วไป | 0 | 25 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans |  |
| `MENU_SINGHA_REPORT_SALE_SUMMARY_BYPRODUCT_ONELINE` | รายงานสรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า(หักรับคืน) แบบแถวเดียว | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SALE_SUMMARY_BYPRODUCT_SUMVAT` | สรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (รวม VAT) | 0 ทั่วไป | 0 | 21 | ic_unit_use, ar_customer, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans |  |
| `MENU_SINGHA_REPORT_SHIPMENT` | รายงานบันทึกการจัดส่ง | 0 ทั่วไป | 1 | 65 | ic_unit_use, pp_shipment, pp_shipment_detail, ic_wms_trans, ic_inventory, ar_customer, ic_trans, transport_type | คลังสินค้า › การส่งสินค้า |
| `MENU_SINGHA_REPORT_STOCK_BALANCE_COMPARE_DEPOSIT` | สรุปการ์ดสินค้า VS  สินค้าฝาก | 0 ทั่วไป | 0 | 30 | ic_unit_use, ic_inventory, ic_unit, ic_trans, ic_trans_detail, ic_wms_trans_detail, ic_report_sort_item | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SINGHA_REPORT_SUMARY_SALE_CUSTOMER_ANALYSIS_PRODUCT` | รายงานสรุปยอดขายลูกค้า วิเคราะห์ตามสินค้า (VAT) | 0 ทั่วไป | 0 | 8 | ar_customer, ic_inventory, ic_trans_detail |  |
| `MENU_SINGHA_REPORT_SUMMARY_DEPART_RETURN` | รายงานสรุปยอดค้างสินค้าจากการเบิก(ลูกค้า) | 0 ทั่วไป | 0 | 8 | ic_trans_detail, ar_customer |  |
| `MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPART_RETURN` | สรุปรับคืนฝาก | 0 ทั่วไป | 0 | 25 | ic_unit_use, ic_wms_trans, ar_customer, ic_inventory, ic_wms_trans_detail | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPOSIT` | สรุปฝาก | 0 ทั่วไป | 0 | 25 | ic_unit_use, ic_wms_trans, ar_customer, ic_inventory, ic_wms_trans_detail | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPOSIT_DEPART` | เบิกฝาก | 0 ทั่วไป | 0 | 25 | ic_unit_use, ic_wms_trans, ar_customer, ic_inventory, ic_wms_trans_detail | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SINGHA_REPORT_SUM_PAY_MONEY` | สรุปยอดเงินจ่าย | 0 ทั่วไป | 0 | 44 | cb_trans, ic_trans, ar_customer, ap_supplier, ap_ar_trans_detail, ap_ar_trans | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_SUM_RECEIVE_MONEY` | สรุปยอดเงินรับ | 0 ทั่วไป | 0 | 47 | cb_trans, ar_customer, ic_trans, ap_ar_trans_detail, ap_ar_trans | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SUM_SALE_QTY` | สรุปยอดขายสินค้า(QTY)ตามช่วงเวลา | 0 ทั่วไป | 0 | 29 | ic_unit_use, ic_unit, ic_inventory, ic_trans_detail, ic_report_sort_item, ic_trans, ar_customer | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SUM_TRANSPORT_TYPE` | สรุปยอดการส่งสินค้าตามประเภทการขนส่ง | 0 ทั่วไป | 0 | 17 | ic_unit_use, ic_inventory, ic_unit, ic_trans_shipment, ic_trans_detail, ar_customer | รายงาน › ขาย |
| `MENU_SINGHA_REPORT_SUPPLIER_DETAIL` | รายละเอียดเจ้าหนี้ | 0 ทั่วไป | 0 | 7 | ap_ar_trans_detail, ic_trans, ap_supplier | รายงาน › ซื้อ |
| `MENU_SINGHA_REPORT_TRANSPORT_ADDRESS` | รายงานที่อยู่จัดส่งลูกค้า | 0 ทั่วไป | 0 | 8 | ar_customer, erp_amper, erp_province, ap_ar_transport_label | รายงาน › ลูกหนี้ |
| `MENU_SINGHA_REPORT_VATBUY_GROUP` | รายงานตรวจสอบภาษีซื้อ | 0 ทั่วไป | 0 | 2 | gl_journal_vat_buy |  |
| `MENU_SINGHA_REPORT_VAT_FREE_BY_ISSUE` | รายงานภาษีขายสินค้าฟรี(ใบควบคุม) | 0 ทั่วไป | 0 | 8 | ar_customer, ic_trans, ic_inventory_price_formula, ic_trans_detail, erp_option | รายงาน › บัญชี |
| `MENU_SINGHA_REPORT_WH_ACCRUED_OUT` | สรุปสินค้าฝาก - ค้างส่ง | 0 ทั่วไป | 0 | 13 | ic_unit_use, ic_wms_trans_detail, ic_inventory, ar_customer, ic_wms_trans | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SINGHA_REPORT_WH_DEPOSITS_CUSTOMER` | สรุปฝากรายลูกค้า | 0 ทั่วไป | 0 | 23 | ic_unit_use, ic_unit, ar_customer, ic_inventory, ic_wms_trans_detail, ic_wms_trans | คลังสินค้า › ฝาก / เบิก / รับคืน สินค้า › รายงาน |
| `MENU_SING_REPORT_SALE_LESSTHAN_COST` | รายงานสินค้าต่ำกว่าทุน | 0 ทั่วไป | 0 | 8 | ar_customer, ic_inventory, ic_trans_detail | รายงาน › ขาย |
| `MENU_STATEMENT_ADVANCE` | รายงาน Statement ล่วงหน้า | 6 เงินสด/ธนาคาร | 0 | 2 | cb_chq_list | เงินสด/ธนาคาร › ธนาคาร › รายงาน |
| `MENU_STOCK_BALANCE_ALL_SHOW_CURRENT_VALUE` | รายงานยอดคงเหลือสินค้า (แสดงทุกสินค้า)  แสดงมูลค่าปัจจุบัน | 0 ทั่วไป | 0 | 4 | ic_inventory_barcode | สินค้า › วิเคราะห์ข้อมูล |
| `menu_summary_payment` | รายงานสรุปการจ่ายเงิน | 6 เงินสด/ธนาคาร | 1 | 2 | cb_trans | เงินสด/ธนาคาร › ธนาคาร › รายงาน |
| `MENU_SUMMARY_RECEIVED` | รายงานสรุปการรับเงิน | 0 ทั่วไป | 1 | 4 | cb_trans, ap_ar_trans, ic_trans | เงินสด/ธนาคาร › ธนาคาร › รายงาน |
| `MENU_SUMMARY_RECEIVED_SCG` | รายงานสรุปการรับเงิน | 0 ทั่วไป | 0 | 9 | ic_trans, cb_trans, ap_ar_trans, erp_option |  |
| `PANUT` | รายงานยอดคงเหลือสินค้าซีเรียวตามคลัง | 1 สินค้า | 0 | 40 | ic_trans, ic_inventory, ic_trans_detail, ic_unit_use, ic_serial | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `QC-RETEST-01` | รายงานสินค้า/วัตถุดิบ ที่ถึงกำหนด Retest | 0 ทั่วไป | 0 | 4 | ic_qc_lab, ic_inventory, ic_qc_lab_container |  |
| `REPORT_BUY_VAT_NO_DUE` | รายงานภาษีซื้อไม่ถึงกำหนดชำระ | 0 ทั่วไป | 0 | 5 | gl_journal_vat_buy |  |
| `REPORT_COUPON_LIST` | รายงานรายละเอียดคูปอง | 0 ทั่วไป | 0 | 8 | ic_trans, ar_customer, coupon_list |  |
| `REPORT_CUSTOM_2254367893_SALE_1` | รายงานยอดขายสินค้าแบบพิเศษ | 3 ขาย | 0 | 14 | ar_customer, ic_inventory_price_formula, ic_inventory, ic_trans_detail, ic_trans, ap_ar_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_ETAX_PENDING` | รายงานแสดงรายการค้างส่งข้อมูล e-Tax | 3 ขาย | 0 | 4 | ic_trans, ar_customer, erp_doc_format_etax, e_tax_transaction | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_IC_ALL_BALANCE` | รายงานสินค้าคงเหลือแบบรวม | 0 ทั่วไป | 0 | 2 | ic_unit_use, ic_inventory |  |
| `REPORT_IC_BALANCE_GROUP_BY_CATEGORY` | รายงานยอดคงเหลือสินค้า-ตามกลุ่มสินค้า | 3 ขาย | 0 | 11 | ic_inventory, ic_group | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_IC_DETAIL_WITH_ALL_BALANCE` | รายงานแสดงสินค้าแบบละเอียด | 0 ทั่วไป | 0 | 4 | ic_unit_use, ic_inventory |  |
| `REPORT_IMEX_QC_APPROVED_VENDOR` |  | 0 ทั่วไป | 0 | 2 | qc_approved_vendor_list, ic_inventory, ap_supplier, manufacturer_list | สินค้า › ตรวจสอบคุณภาพสินค้า |
| `REPORT_INVENTORY_EXPIRE_DATE` | รายงานสินค้าหมดอายุ | 1 สินค้า | 0 | 4 | ic_unit | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `REPORT_INVENTORY_EXPIRE_WAREHOUSE_DATE` | รายงานสินค้าหมดอายุตามคลัง | 1 สินค้า | 0 | 3 |  | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `REPORT_PACKING_FROM_INVOICE` | รายงานการจัดสินค้าจากใบขาย | 3 ขาย | 0 | 2 | ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_PACKING_FROM_INVOICE_CUSTOMER` | รายงานการจัดสินค้าจากใบขาย แสดงตามลูกค้า | 3 ขาย | 0 | 5 | ic_trans_detail, ar_customer | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_QC_LAB_RETEST` | รายงานกำหนด Retest วัตถุดิบ | 1 สินค้า | 0 | 4 | ic_qc_lab, ic_inventory, ic_qc_lab_container | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `REPORT_SALE_BY_EMPLOYEE` | รายงานการขายแยกตามพนักงานขาย (หักส่วนลด) | 3 ขาย | 0 | 10 | ic_trans_detail, erp_user, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_SALE_BY_SUPPLIER` | รายงานการขายสินค้า แยกตามผู้จัดจำหน่าย | 3 ขาย | 0 | 10 | ic_inventory, ap_supplier, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_SCG_SEND_MONEY_POS` | รายงานการนำส่งเงินประจำวัน | 0 ทั่วไป | 0 | 2 | poscashiersettle |  |
| `REPORT_SEND_MONEY_POS` | รายงานการนำส่งเงินประจำวัน | 0 ทั่วไป | 0 | 2 | poscashiersettle | ขาย POS › รายงาน/ยกเลิก |
| `REPORT_SUMMARY_PURCHASE_BY_SUPPLIER` | รายงานสรุปการซื้อสินค้า แยกตามผู้จัดจำหน่าย | 2 ซื้อ | 0 | 12 | ic_inventory, ap_supplier, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_purchase`) |
| `REPORT_SUMMARY_SALE_BY_SUPPLIER` | รายงานสรุปการขายสินค้า แยกตามผู้จัดจำหน่าย | 3 ขาย | 0 | 12 | ic_inventory, ap_supplier, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `REPORT_SYNC_SEND_SUCCESS_TRANS` | รายงานสถานะการส่งข้อมูล | 3 ขาย | 0 | 8 | ic_trans, ic_trans_detail, cb_trans, cb_trans_detail, ap_ar_trans, ap_ar_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `SALE_ANALYSIS_BY_CUSTOMER_GROUP_SALE_VALUE` | รายงานวิเคราะห์ การขาย จัดเรียงตาม กลุ่มลูกค้า แสดงมูลค่า | 3 ขาย | 0 | 15 | ar_customer_detail, ic_trans_detail, ar_group, ar_group_sub, erp_user, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `TESTSAVE` | รายงานลูกหนี้ค้างชำระ แสดงรายละเอียดบิลขาย | 5 ลูกหนี้ | 0 | 10 | ic_trans, ar_customer, erp_user, ic_trans_detail | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |
| `TEST SML` | test sml | 0 ทั่วไป | 0 | 2 |  |  |
| `TOC-001` | รายงานยอดคงเหลือสินค้า | 1 สินค้า | 0 | 23 | ic_trans_detail_lot, ic_inventory, ic_warehouse, ic_inventory_barcode, ic_unit_use, ic_lot_manage | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `TOC-SS-013` | รายงานยอดขายของผู้แทน หัก รับคืนสินค้า | 3 ขาย | 0 | 21 | ic_trans, erp_user, ic_trans_detail_commission | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `TOC-ST-004` | รายงานวัตถุดิบที่ใช้ในการผลิตสินค้าสำเร็จรูป | 1 สินค้า | 0 | 8 | ic_trans_detail, ic_inventory | รายงานอื่น ๆ (`menu_fastreport_other_ic`) |
| `TV_DIRECT_REPORT_INVOICE_SUMMARY` | รายงานการรวม INV_ ขายประจำวัน | 3 ขาย | 0 | 10 | ic_trans, cb_trans, erp_branch_list | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `TV_DIRECT_REPORT_INVOICE_SUMMARY_TRANSFER` | รายงานการ Tranfer ข้อมูลประจำวัน | 3 ขาย | 0 | 8 | ic_trans, erp_branch_list, pos_period, cb_trans | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `TV_DIRECT_REPORT_POS_OUTPUT_DATA` | รายงานข้อมูลออกจาก POS (Out put  Data) | 3 ขาย | 0 | 2 |  | รายงานอื่น ๆ (`menu_fastreport_other_sale`) |
| `V001` | รายงานขายสินค้าต่ำกว่าทุน | 0 ทั่วไป | 0 | 6 | ic_inventory, ar_customer, ic_trans_detail |  |
| `V002` | รายงานใบตั้งหนี้จากการซื้อแบบแจกแจงตามเจ้าหนี้ | 0 ทั่วไป | 0 | 8 | ic_trans, ap_supplier, ic_trans_detail |  |
| `รายงานตัดแต้มลูกหนี้` | 6018 | 5 ลูกหนี้ | 0 | 4 | ar_customer, ic_trans | รายงานอื่น ๆ (`menu_fastreport_other_customer`) |

## ตาราง → FastReport ที่อ่านตารางนั้น

| ตาราง | จำนวนรายงาน | ตัวอย่าง |
|---|---|---|
| `ic_trans` | 267 | 2001, 2035, 2043, 2044, 2046, 2055 |
| `ic_trans_detail` | 257 | 1006, 2001, 2002, 2005, 2008, 2015 |
| `ic_inventory` | 254 | 1001, 1004, 1005, 1006, 2001, 2002 |
| `ar_customer` | 205 | 2001, 2044, 2046, 2082, 2088, 2089 |
| `ap_supplier` | 107 | 2010, 2010-1, 2011, 2019, 2032, 2033 |
| `ic_unit` | 65 | 2002, 2035, 2054, 2063, 2064, 2068 |
| `ic_unit_use` | 58 | 1004, 2008, 2015, 2018, 2021, 2030 |
| `cb_trans` | 57 | 3022, 4002, 4007, 4029, 4036, 4069 |
| `ap_ar_trans` | 47 | 2061, 2087, 2090, 4069, 4078, 5001 |
| `erp_user` | 42 | 10002, 2001, 2046, 4015, 4016, 4019 |
| `erp_branch_list` | 39 | 2063, 8007, 8008, 8009, 8010, 8017 |
| `cb_trans_detail` | 31 | 2088, 2089, 2090, 4002, 4036, 4078 |
| `erp_bank` | 30 | 5001, 5003, 6001, 6012, 6016, 6019 |
| `ap_ar_trans_detail` | 29 | 4018, 5002, 5003, 6003, 6004, 6006 |
| `ic_inventory_barcode` | 23 | 1001, 1003, 1004, 1005, 2003, 2005 |
| `ic_warehouse` | 20 | 2005, 2012, 2015, 2017, 2032, 2033 |
| `ar_customer_detail` | 20 | 4027, 6008, 6013, 6017, 6022, 7017 |
| `cb_chq_list` | 20 | 7004, 7005, 7006, 7008, 7009, 7012 |
| `erp_bank_branch` | 19 | 6016, 6019, 7004, 7005, 7006, 7008 |
| `erp_department_list` | 15 | 10002, 2068, 2074, 3008, 3009, 3015 |
| `gl_journal_detail` | 14 | 4017, 8001, 8005, 8006, 8007, 8008 |
| `ic_report_sort_item` | 14 | MENU_SINGHA_REPORT_ANALYST_SALE_AREA, MENU_SINGHA_REPORT_ANALYST_SALE_CUSTOMER, MENU_SINGHA_REPORT_ANALYST_SALE_CUSTOMER_CUT_RETURN, MENU_SINGHA_REPORT_PRODUCT_MOVEMENT_STORE, MENU_SINGHA_REPORT_PRODUCT_SUM_OUT_BY_DAY, MENU_SINGHA_REPORT_PRODUCT_TRANSFER |
| `gl_journal` | 12 | 8004, 8005, 8006, 8007, 8008, 8009 |
| `ic_group` | 11 | 2006, 2007, 2008, 2056, 2067, 2080 |
| `ic_shelf` | 11 | 2012, 2017, 2033, 2037, 2050, 2060 |
| `ic_wms_trans_detail` | 11 | 2052, MENU_SINGHA_REPORT_AGING_DEPOSIT, MENU_SINGHA_REPORT_DEPOSIT_CARD, MENU_SINGHA_REPORT_IC_DEPOSIT_SUMMARY, MENU_SINGHA_REPORT_SHIPMENT, MENU_SINGHA_REPORT_STOCK_BALANCE_COMPARE_DEPOSIT |
| `erp_province` | 9 | 10002, 4020, 69001, 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_AR_MAIN_REPORT |
| `ic_inventory_price_formula` | 9 | 1004, 2022, 2042, 2905, MENU_COMPARE_SALE_WITH_PRICE, MENU_POS_SUMARY_010 |
| `ar_dealer` | 9 | 4001, 6002, 6007, 6011, 6013, 6014 |
| `ic_wms_trans` | 8 | 2052, MENU_SINGHA_REPORT_AGING_DEPOSIT, MENU_SINGHA_REPORT_SHIPMENT, MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPART_RETURN, MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPOSIT, MENU_SINGHA_REPORT_SUMMARY_WAREHOUSE_DEPOSIT_DEPART |
| `erp_project_list` | 8 | 2069, 2075, 3010, 3016, 3027, 4082 |
| `gl_chart_of_account` | 8 | 2085, 8001, 8005, 8007, 8011, 8017 |
| `erp_option` | 8 | MENU_FAST_REPORT_ANALYSIS_SELL_SUM_BY_DOCNO, MENU_FASTREPORT_RECEIVED_MONEY_SCG, MENU_FAST_REPORT_SUMMARY_SELL_BY_SALE, MENU_IC_REPORT_SALE_REMAIN, MENU_POS_SUM_FRONT_SCG, MENU_REPORT_ACCRUED_IN_QTY |
| `erp_amper` | 7 | 69001, 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_AR_MAIN_REPORT, MENU_AR_MAIN_REPORT_BY_SALE, MENU_SINGHA_REPORT_AR_CUSTOMER |
| `gl_journal_vat_buy` | 7 | 8002, 8010, 8015, MENU_REPORT_CHECK_VAT_BUY, MENU_SINGHA_REPORT_OTHER_EXPENSES, MENU_SINGHA_REPORT_VATBUY_GROUP |
| `ic_inventory_detail` | 6 | 2019, 2031, 2034, 2048, 2057, 2097 |
| `erp_tambon` | 6 | 69001, 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_AR_MAIN_REPORT, MENU_AR_MAIN_REPORT_BY_SALE, MENU_SINGHA_REPORT_AR_CUSTOMER |
| `gl_journal_book` | 6 | 8005, 8006, 8007, 8008, 8018, 8021 |
| `erp_side_list` | 5 | 10002, 2071, 2077, 3012, 3018 |
| `ic_wh_shelf` | 5 | 2012, 2029, 2037, 2066, B2037 |
| `gl_journal_vat_sale` | 5 | 7007, 8003, 8009, 8012, 8020 |
| `gl_journal_depart_list` | 5 | 8005, 8006, 8007, 8011, 8018 |
| `ic_trans_detail_lot` | 4 | 2036, 2054, MENU_REPORT_LOT_INVENTORY, TOC-001 |
| `erp_doc_group` | 4 | 2070, 2076, 3011, 3017 |
| `erp_allocate_list` | 4 | 2072, 2078, 3013, 3019 |
| `erp_job_list` | 4 | 2073, 2079, 3014, 3020 |
| `coupon_list` | 4 | 2088, 2089, 2090, REPORT_COUPON_LIST |
| `pos_period` | 4 | 4016, 4029, MENU_POS_PERIOD_STATUS, TV_DIRECT_REPORT_INVOICE_SUMMARY_TRANSFER |
| `table_order` | 4 | 4025, 4028, 4030, MENU_REPORT_SUMMARY_ORDER_KITCHEN |
| `ic_group_sub` | 3 | 2020, 2056, 2080 |
| `ic_brand` | 3 | 2045, BC3006, BC4010 |
| `ic_category` | 3 | 2056, 2067, MENU_FAST_REPORT_SUMMARY_SELL_BY_SALE_BY_GROUP |
| `ap_supplier_detail` | 3 | 5004, 8015, MENU_SINGHA_REPORT_BANK_STATEMENT_SHOW_PAYMENT_DETAIL |
| `erp_expenses_list` | 3 | 6019, 7003, 7015 |
| `erp_pass_book` | 3 | 6019, MENU_BOOK_BANK_BALANCE, MENU_SINGHA_REPORT_BANK_STATEMENT_SHOW_PAYMENT_DETAIL |
| `cb_petty_cash` | 3 | 7010, 7011, 7018 |
| `ar_shoptype1` | 3 | 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_SINGHA_REPORT_AR_CUSTOMER |
| `ar_shoptype2` | 3 | 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_SINGHA_REPORT_AR_CUSTOMER |
| `ar_shoptype3` | 3 | 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_SINGHA_REPORT_AR_CUSTOMER |
| `ar_shoptype4` | 3 | 7017, MANU_SINGHA_REPORT_AR_CUSTOMER, MENU_SINGHA_REPORT_AR_CUSTOMER |

## รายงานที่เขียนในโค้ด (335 เมนู)

| เมนู | menu name | คลาส | reportEnum / trans_flag |
|---|---|---|---|
| Data › Data ARM | `menu_sync_data_arm` | `SINGHAReport._singhaDataSyncControl` |  |
| Data › Data Saleout | `menu_sync_data_saleout` | `SINGHAReport._singhaDataSyncControl` |  |
| Data › Data Stock | `menu_sync_data_stock` | `SINGHAReport._singhaDataSyncControl` |  |
| Data › สร้างรายการขายจากสรุปการขาย POS | `menu_imort_sale_from_pos_sale_report` | `SMLERPTransferControl._saleImportFromPOSSaleReport` |  |
| Mobile Sales › Customer | `menu_saletools_customer` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › กำหนดค่าตัวแปร Mobile | `menu_saletools_14_9` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › Heat Map | `menu_saletools_hea_map` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › View Map | `menu_saletools_view_map` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › Fleet | `menu_saletools_fleet` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › Real Time | `menu_saletools_real_time` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › Customer GPS by salesman | `menu_saletools_customer_gps_by_salesman` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Map › Map Analysis | `menu_saletools_aap_analysis` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Administrator › Import/Export data | `menu_saletools_import_export_data` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Administrator › Update Mobile | `menu_saletools_update_mobile` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Administrator › Import Master SML | `menu_saletools_import_master_sml` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Distributor | `menu_saletools_distributor` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Company | `menu_saletools_company` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Warehouse | `menu_saletools_warehouse` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › DC State | `menu_saletools_dc_state` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › DC Section | `menu_saletools_dcsection` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Sales Area | `menu_saletools_sales_area` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Delivery Route | `menu_saletools_delivery_route` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Bank | `menu_saletools_bank` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Agent/DC › Bank Account | `menu_saletools_bank_account` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Product | `menu_saletools_product` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Store | `menu_saletools_store` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Region | `menu_saletools_region` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › State | `menu_saletools_state` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › City | `menu_saletools_city` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Town | `menu_saletools_town` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Customer Type | `menu_saletools_customer_type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Credit Days | `menu_saletools_credit_days` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Price Level | `menu_saletools_price_level` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Adjust Money | `menu_saletools_adjust_money` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › News Type | `menu_saletools_news_type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Payment Type | `menu_saletools_payment_type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Survey Type | `menu_saletools_survey_type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Delivery Days | `menu_saletools_delivery_days` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Material Type | `menu_saletools_material_Type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Common › Display Type | `menu_saletools_display_type` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Operation › News And Documents | `menu_saletools_news_and_documents` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Master Data › Operation › Mustlist Product | `menu_saletools_mustlist_product` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Photo › Photo Group | `menu_saletools_photo_group` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Photo › Photos | `menu_saletools_photos` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Promotion › Promotions | `menu_saletools_promotions` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Promotion › Import Promotion | `menu_saletools_import_promotion` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Promotion › Promotion Group | `menu_saletools_promotion_group` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Promotion › Advance Price | `menu_saletools_advance_price` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Route › Route Planning | `menu_saletools_route_planning` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Route › AdHoc Jobs | `menu_saletools_adhoc_jobs` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Route › Manage Route Plan | `menu_saletools_manage_route_plan` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Bill Collection › Approve Bill Collection | `menu_saletools_approve_bill_collection` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Generate Code › Approve Code | `menu_saletools_approve_code` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Generate Code › Document Running NO | `menu_saletools_document_running_no` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Interface SML › ods Transfer | `menu_saletools_ods_transfer` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › Approve Goods Transfer | `menu_saletools_approve_goods_transfer_request` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › Approve ods Transfer | `menu_saletools_approve_ods_transfer` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › Approve ods Recieved Customer (คืน/จ่ายมัดจำ) | `menu_saletools_approve_ods_recieved_customer` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › Approve ods Issued Customer (ยืม/รับมัดจำ) | `menu_saletools_approve_ods_issued_customer` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › ods Exchange (เปลี่ยนของเสีย) | `menu_saletools_ods_exchange` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Manage Stock › Approve Goods Return | `menu_saletools_approve_goods_return` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › Pre-Order › Approve Invoice | `menu_saletools_approve_sales_invoice` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Transaction › VAN › Approve Invoice | `menu_saletools_approve_invoice` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Users › Web Users | `menu_saletools_web_users` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Users › Change Password | `menu_saletools_change_password` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Users › Mobile Users | `menu_saletools_mobile_users` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Users › Sync Log | `menu_saletools_sync_log` | `SINGHAReport._saleToolsWebControl` |  |
| Mobile Sales › Users › User Roles | `menu_saletools_user_roles` | `SINGHAReport._saleToolsWebControl` |  |
| ขาย › รายงาน/ยกเลิก › รายงานบันทึกใบเสนอราคา | `menu_so_report_quotation` | `SMLERPReportTool._reportTrans` | ขาย_เสนอราคา, 30 |
| ขาย › รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอราคา | `menu_so_report_quotation_approve` | `SMLERPReportTool._reportTrans` | ขาย_เสนอราคา_อนุมัติ, 32 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกใบเสนอราคา | `menu_so_report_quotation_cancel` | `SMLERPReportTool._reportTrans` | ขาย_เสนอราคา_ยกเลิก, 31 |
| ขาย › รายงาน/ยกเลิก › รายงานสถานะใบเสนอราคา | `menu_so_report_quotation_stat` | `SMLERPReportTool._reportTrans` | ขาย_เสนอราคา_สถานะ, 30 |
| ขาย › รายงาน/ยกเลิก › รายงานใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry` | `SMLERPReportTool._reportTrans` | ขาย_สั่งจองและสั่งซื้อสินค้า, 34 |
| ขาย › รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_approve` | `SMLERPReportTool._reportTrans` | ขาย_สั่งจองและสั่งซื้อสินค้า_อนุมัติ, 38 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_cancel` | `SMLERPReportTool._reportTrans` | ขาย_สั่งจองและสั่งซื้อสินค้า_ยกเลิก, 39 |
| ขาย › รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ/สั่งจอง | `menu_so_report_inquiry_stat` | `SMLERPReportTool._reportTrans` | ขาย_สั่งจองและสั่งซื้อสินค้า_สถานะ, 34 |
| ขาย › รายงาน/ยกเลิก › รายงานใบสั่งขาย | `menu_so_report_sale_order` | `SMLERPReportTool._reportTrans` | ขาย_สั่งขาย, 36 |
| ขาย › รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งขาย | `menu_so_report_sale_order_approve` | `SMLERPReportTool._reportTrans` | ขาย_สั่งขาย_อนุมัติ, 52 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งขาย | `menu_so_report_sale_order_cancel` | `SMLERPReportTool._reportTrans` | ขาย_สั่งขาย_ยกเลิก, 37 |
| ขาย › รายงาน/ยกเลิก › รายงานสถานะใบสั่งขาย | `menu_so_report_sale_order_stat` | `SMLERPReportTool._reportTrans` | ขาย_สั่งขาย_สถานะ, 36 |
| ขาย › รายงาน/ยกเลิก › รายงานรับเงินล่วงหน้า | `menu_so_report_deposit_receive` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า, 40 |
| ขาย › รายงาน/ยกเลิก › รายงานคืนเงินรับล่วงหน้า | `menu_so_report_deposit_return` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า_คืน, 42 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกรับเงินล่วงหน้า | `menu_so_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า_ยกเลิก, 41 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินรับล่วงหน้า | `menu_so_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า_คืน_ยกเลิก, 43 |
| ขาย › รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินรับล่วงหน้า | `menu_so_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า_รายงานยอดคงเหลือ, 40 |
| ขาย › รายงาน/ยกเลิก › รายงานการตัดเงินรับล่วงหน้า | `menu_so_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินล่วงหน้า_รายงานตัดเงิน, 40 |
| ขาย › รายงาน/ยกเลิก › รายงานรับเงินมัดจำ | `menu_so_report_deposit_receive_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ, 110 |
| ขาย › รายงาน/ยกเลิก › รายงานคืนเงินมัดจำ | `menu_so_report_deposit_return_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ_คืน, 112 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกรับเงินมัดจำ | `menu_so_report_deposit_payment_cancel_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ_ยกเลิก, 111 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_so_report_deposit_payment_return_cancel_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ_คืน_ยกเลิก, 113 |
| ขาย › รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_so_report_deposit_payment_remain_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ_รายงานยอดคงเหลือ, 110 |
| ขาย › รายงาน/ยกเลิก › รายงานการตัดเงินมัดจำ | `menu_so_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` | ขาย_รับเงินมัดจำ_รายงานตัดเงิน, 110 |
| ขาย › รายงาน/ยกเลิก › รายงานการขายสินค้าและบริการ | `menu_so_report_invoice` | `SMLERPReportTool._reportTrans` | ขาย_ขายสินค้าและบริการ, 44 |
| ขาย › รายงาน/ยกเลิก › รายงานการขายและบริการเรียงตามสินค้า | `menu_so_sale_service_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` | ขาย_รายงานขายสินค้าแยกตามสินค้า |
| ขาย › รายงาน/ยกเลิก › รายงานการรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note` | `SMLERPReportTool._reportTrans` | ขาย_รับคืนสินค้า, 48 |
| ขาย › รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods` | `SMLERPReportTool._reportTrans` | ขาย_เพิ่มหนี้สินค้าราคาผิด, 46 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกขายสินค้าและบริการ | `menu_so_report_invoice_cancel` | `SMLERPReportTool._reportTrans` | ขาย_ขายสินค้าและบริการ_ยกเลิก, 45 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/ลดหนี้ | `menu_so_report_credit_note_cancel` | `SMLERPReportTool._reportTrans` | ขาย_รับคืนสินค้า_ยกเลิก, 49 |
| ขาย › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_so_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` | ขาย_เพิ่มหนี้สินค้าราคาผิด_ยกเลิก, 47 |
| ขาย › รายงานวิเคราะห์ › รายงานสินค้า ขายประจำเดือน | `menu_report_product_sale_monthly` | `IMEXControl.report.report_product_sale_monthly` |  |
| ขาย › รายงานสรุป › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_sell_by_sale` | `SMLERPSOReport._report_summary._report_sell_by_sale` | สินค้า_sell_by_sale |
| ขาย › รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.8) | `menu_so_report_sale_drug_by_lot` | `SMLERPSOReport._report_drug_sale_8` |  |
| ขาย › รายงานสรุป › รายงานการขายยาตามที่สำนักงานคณะกรรมการอาหารและยากำหนด (ขย.13) | `menu_so_report_sale_drug_13` | `SMLERPSOReport._report_sale_drug_13` |  |
| ขาย › รายงานสรุป › บัญชีการผลิตยาและขายยาที่ผลิต (แบบ ผ.ย. ๕) | `menu_so_report_sale_drug_by_lot_5` | `SMLERPSOReport._report_drug_sale_8` |  |
| ขาย › รายงานสรุป › รายงานเรียกเก็บยาคืน (Recall) | `menu_so_report_sale_recall` | `SMLERPSOReport._report_sale_drug_recall` |  |
| ขาย POS › รายงาน/ยกเลิก › รายงานใบกำกับภาษีอย่างเต็มออกแทน | `menu_so_report_pos_full_invoice` | `SMLERPReportTool._reportTrans` | ขาย_ขายสินค้าและบริการ_รายงานการออกใบกำกับภาษีอย่างเต็ม, 144 |
| คลัง › รายงาน (คลัง) › รายงานตรวจนับสินค้า (คลัง) | `menu_wh_report_item_count` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานสินค้าตรวจนับ, 502 |
| ค่าเสื่อม › รายงาน › รายงานรายละเอียดสินทรัพย์ | `menu_asset_report_list` | `SMLERPASSET._report._asset._report` |  |
| ค่าเสื่อม › รายงาน › รายงานค่าเสื่อมราคาสินทรัพย์ | `menu_asset_report_depreciate` | `SMLERPASSET._report._depreciate._report` |  |
| ค่าเสื่อม › รายงาน › รายงานการซ่อมบำรุงสินทรัพย์ | `menu_asset_report_maintain` | `SMLERPASSET._report._maintain._report` |  |
| ซื้อ › ซื้อสินค้าแบบทะยอยรับ › รายงานรับสินค้า | `menu_po_report_purchase_partial` | `SMLERPReportTool._reportTrans` | ซื้อ_พาเชียล_รับสินค้า, 310 |
| ซื้อ › ซื้อสินค้าแบบทะยอยรับ › รายงานส่งคืนสินค้า/ราคาผิด | `menu_po_report_purchase_partial_debit` | `SMLERPReportTool._reportTrans` | ซื้อ_พาเชียล_ส่งคืนสินค้าหรือราคาผิด, 311 |
| ซื้อ › ซื้อสินค้าแบบทะยอยรับ › รายงานตั้งหนี้จากการรับสินค้า | `menu_po_report_purchase_partial_1` | `SMLERPReportTool._reportTrans` | ซื้อ_พาเชียล_ตั้งหนี้, 315 |
| ซื้อ › ซื้อสินค้าแบบทะยอยรับ › รายงานเพิ่มหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_2` | `SMLERPReportTool._reportTrans` | ซื้อ_พาเชียล_เพิ่มหนี้, 316 |
| ซื้อ › ซื้อสินค้าแบบทะยอยรับ › รายงานลดหนี้จากใบตั้งหนี้ | `menu_po_report_purchase_partial_3` | `SMLERPReportTool._reportTrans` | ซื้อ_พาเชียล_ลดหนี้, 317 |
| ซื้อ › รายงาน/ยกเลิก › รายงานใบเสนอซื้อ | `menu_po_report_record_requisition_purchase` | `SMLERPReportTool._reportTrans` | ซื้อ_ใบเสนอซื้อ, 2 |
| ซื้อ › รายงาน/ยกเลิก › รายงานอนุมัติใบเสนอซื้อ | `menu_po_report_requisition_purchase1` | `SMLERPReportTool._reportTrans` | ซื้อ_ใบเสนอซื้อ_อนุมัติ, 4 |
| ซื้อ › รายงาน/ยกเลิก › รายงานสถานะใบเสนอซื้อ | `menu_po_report_requisition_purchase` | `SMLERPReportTool._reportTrans` | ซื้อ_ใบเสนอซื้อ_สถานะ, 2 |
| ซื้อ › รายงาน/ยกเลิก › รายงานบันทึกใบสั่งซื้อ | `menu_po_report_purchase_order` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานใบสั่งซื้อ, 6 |
| ซื้อ › รายงาน/ยกเลิก › รายงานอนุมัติใบสั่งซื้อ | `menu_po_report_purchase_order_approve` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานอนุมัติใบสั่งซื้อ, 8 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกใบสั่งซื้อ | `menu_po_report_purchase_order_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานยกเลิกใบสั่งซื้อ, 7 |
| ซื้อ › รายงาน/ยกเลิก › รายงานสถานะใบสั่งซื้อ | `menu_po_report_purchase_order_status` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานสถานะใบสั่งซื้อ, 6 |
| ซื้อ › รายงาน/ยกเลิก › รายงานค้างรับสินค้าตามใบสั่งซื้อ | `menu_po_hold_receive_by_doc` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานค้างรับตามใบสั่งซื้อ, 6 |
| ซื้อ › รายงาน/ยกเลิก › รายงานบันทึกการจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินล่วงหน้า, 10 |
| ซื้อ › รายงาน/ยกเลิก › รายงานบันทึกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินล่วงหน้า_รับคืน, 20 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินล่วงหน้า_ยกเลิก, 150 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกรับคืนเงินล่วงหน้า | `menu_po_report_deposit_payment_return_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินล่วงหน้า_รับคืน_ยกเลิก, 161 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยอดคงเหลือจ่ายเงินล่วงหน้า | `menu_po_report_deposit_payment_remain` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานยอดคงเหลือเงินจ่ายล่วงหน้า, 10 |
| ซื้อ › รายงาน/ยกเลิก › รายงานการตัดจ่ายเงินล่วงหน้า | `menu_po_report_cut_deposit_payment` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานตัดเงินจ่ายล่วงหน้า, 10 |
| ซื้อ › รายงาน/ยกเลิก › รายงานจ่ายเงินมัดจำ | `menu_po_report_advance_payment` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินมัดจำ, 11 |
| ซื้อ › รายงาน/ยกเลิก › รายงานรับคืนเงินมัดจำ | `menu_po_report_advance_payment_return` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินมัดจำ_รับคืน, 25 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกจ่ายเงินมัดจำ | `menu_po_report_advance_payment_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินมัดจำ_ยกเลิก, 151 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกคืนเงินมัดจำ | `menu_po_report_advance_payment_return_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_จ่ายเงินมัดจำ_รับคืน_ยกเลิก, 152 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยอดคงเหลือเงินมัดจำ | `menu_po_report_deposit_payment_2_remain` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานยอดคงเหลือเงินมัดจำจ่าย, 11 |
| ซื้อ › รายงาน/ยกเลิก › รายงานการตัดใบจ่ายเงินมัดจำ | `menu_po_report_cut_deposit_payment_2` | `SMLERPReportTool._reportTrans` | ซื้อ_รายงานตัดเงินมัดจำจ่าย, 11 |
| ซื้อ › รายงาน/ยกเลิก › รายงานการซื้อสินค้า/ตั้งหนี้ | `menu_po_report_purchase` | `SMLERPReportTool._reportTrans` | ซื้อ_ซื้อสินค้าและบริการ, 12 |
| ซื้อ › รายงาน/ยกเลิก › รายงานการส่งคืนสินค้า/ลดหนี้ | `menu_po_report_credit_note` | `SMLERPReportTool._reportTrans` | ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด, 16 |
| ซื้อ › รายงาน/ยกเลิก › รายงานการเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods` | `SMLERPReportTool._reportTrans` | ซื้อ_เพิ่มหนี้ราคาผิด, 14 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้า/ตั้งหนี้ | `menu_po_report_purchase_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_ซื้อสินค้าและบริการ_ยกเลิก, 13 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกส่งคืนสินค้า/ลดหนี้ | `menu_po_credit_note_cancel_report` | `SMLERPReportTool._reportTrans` | ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด_ยกเลิก, 17 |
| ซื้อ › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้/ราคาผิด/เพิ่มสินค้า | `menu_po_report_add_goods_cancel` | `SMLERPReportTool._reportTrans` | ซื้อ_เพิ่มหนี้ราคาผิด_ยกเลิก, 15 |
| ซื้อ › รายงานสรุป › รายงานซื้อสินค้าแยกตามสินค้า | `menu_po_recive_by_item` | `SMLERPSOReport._report._report_sale_service_by_item` | ซื้อ_รายงานซื้อสินค้าแยกตามสินค้า |
| บัญชี › รายงานอื่น ๆ | `menu_fastreport_other_gl` | `SMLFastReport._loadForm` |  |
| บัญชี › งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) | `menu_report_profit_and_lost_sum_year` | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year` |  |
| บัญชี › งบการเงิน › รายงานงบกำไร/ขาดทุน › งบกำไรขาดทุน (13 ช่อง) ตามแผนก | `menu_report_profit_and_lost_sum_year_by_department` | `SMLERPGL._report._profit_and_lost_sum_year._report_profit_and_lost_sum_year_by_department` |  |
| บัญชี › งบการเงิน › รายงานงบทดลอง › งบดุลหลังปรับปรุง | `menu_gl_report_balancesheet_asset_lao` | `SMLERPGL._report._report_balancesheet_asset_lao._report_balancesheet_asset_lao` |  |
| บัญชี › งบการเงิน › รายงานงบทดลอง › งบรายรับรายจ่าย | `menu_gl_report_profit_and_lost_lao` | `SMLERPGL._report._report_balancesheet_profit_and_lost_lao._report_balancesheet_profit_and_lost_lao` |  |
| บัญชี › บัญชีแยกประเภท › รายงานข้อมูลรายวัน | `menu_gl_report_journal` | `SMLERPGL._report._report_journal_daily_lao._report_daily_journal_lao` |  |
| บัญชี › บัญชีแยกประเภท › รายงานข้อมูลรายวันแบบสรุป | `menu_gl_report_journal_sum` | `SMLERPGL._report._journalSum._report` |  |
| บัญชี › บัญชีแยกประเภท › รายงานบัญชีแยกประเภท | `menu_gl_report_sheet` | `SMLERPGL._report._sheet._report` |  |
| บัญชี › บัญชีแยกประเภท › รายงานบัญชีแยกประเภท (แบบสรุป) | `menu_gl_report_sheet_sum` | `SMLERPGL._report._sheetSum._report` |  |
| บัญชี › ผังบัญชี › รายงานรายละเอียดผังบัญชี | `menu_report_chart_of_account` | `SMLERPGL._report._chartOfAccount._report` |  |
| บัญชี › ภาษีมูลค่าเพิ่ม › รายงานภาษีขาย (มาตรฐาน) | `menu_report_vat_sale_standard` | `SMLERPGL._report._tax._reportVatSale` |  |
| บัญชี › ภาษีมูลค่าเพิ่ม › รายงานภาษีซื้อ (มาตรฐาน) | `menu_report_vat_buy_standard` | `SMLERPGL._report._tax._reportVatBuy` |  |
| บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.53) | `menu_gl_wht_report_in_53` | `SMLERPGL._report._tax._wht` |  |
| บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.3) | `menu_gl_wht_report_in_3` | `SMLERPGL._report._tax._wht` |  |
| บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีถูกหัก ณ. ที่จ่าย | `menu_gl_wht_report_sum` | `SMLERPGL._report._tax._wht` |  |
| รายงาน › ขาย › รายงานสรุปการขายสินค้าตามพนักงานขาย | `menu_singha_report_sale_summary_by_saleman` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › ขาย › รายงานยอดขายรายเดือนตามกลุ่มผลิตภัณฑ์/เทียบปี | `menu_report_sale_category_year_compare` | `SINGHAReport.GL._glReport` |  |
| รายงาน › ข้อมูลทั่วไป › กำหนดการเรียงข้อมูลรายงาน | `menu_ic_report_sort` | `SMLERPICReport._icReportSort` |  |
| รายงาน › ซื้อ › การ์ดเจ้าหนี้ | `menu_singha_report_supplier_card` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › บัญชี › งบดุล | `menu_singha_report_balancesheet_asset` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |
| รายงาน › บัญชี › รายงานกระดาษทำการ | `menu_gl_report_balance_sheet` | `SMLERPGL._report._workSheet._report` |  |
| รายงาน › บัญชี › งบกำไรขาดทุน | `menu_singha_report_profit_and_lost` | `SMLERPGL._report._singhaReportProfitAndLost._report` |  |
| รายงาน › บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.3) | `menu_singha_report_product_wht_3` | `SINGHAReport.GL._glReport` |  |
| รายงาน › บัญชี › รายงานภาษีหัก ณ ที่จ่าย (ภ.ง.ด.53) | `menu_singha_report_product_wht_53` | `SINGHAReport.GL._glReport` |  |
| รายงาน › บัญชี › รายงานภาษีซื้อ | `menu_singha_report_vat_buy` | `SINGHAReport.GL._glReportGenerate` |  |
| รายงาน › บัญชี › รายงานภาษีขาย | `menu_singha_report_vat_sale` | `SINGHAReport.GL._glReportGenerate` |  |
| รายงาน › บัญชี › สมุดบัญชีแยกประเภทเงินสด | `menu_report_cash_gl_sheet` | `SINGHAReport.GL._glReport` |  |
| รายงาน › บัญชี › สมุดบัญชีแยกประเงินโอน | `menu_report_transfer_gl_sheet` | `SINGHAReport.GL._glReport` |  |
| รายงาน › บัญชี › รายงานข้อมูลรายวัน | `menu_singha_report_journal` | `SINGHAReport.GL._glReport` |  |
| รายงาน › บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (มาตรฐาน) | `menu_gl_report_trial_balance` | `SMLERPGL._report._report_lao_balance_sheet._report_lao_balance_sheet` |  |
| รายงาน › บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกแผนก) | `menu_gl_report_trial_balance_depart` | `SMLERPGL._report._trialBalanceDepart._reportTrialBalanceDepart` |  |
| รายงาน › บัญชี › รายงานงบทดลอง › รายงานงบทดลอง (แยกสาขา) | `menu_gl_report_trial_balance_branch` | `SMLERPGL._report._trialBalanceBranch._report` |  |
| รายงาน › บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา) | `menu_gl_report_profit_and_lost_branch_1` | `SMLERPGL._report._profitAndLostBranch._report` |  |
| รายงาน › บัญชี › รายงานอื่น ๆ › งบกำไรขาดทุน (แยกสาขา-แผนก) | `menu_gl_report_trial_balance_branch_depart` | `SMLERPGL._report._trialBalanceBranchDepart._report` |  |
| รายงาน › บัญชี › รายงานอื่น ๆ › งบกระแสเงินสด | `menu_gl_report_other_1` | `SMLERPGL._report._other_1._report` |  |
| รายงาน › ลูกหนี้ › ยอดลูกหนี้คงเหลือ | `menu_singha_report_customer_credit_balance` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › ลูกหนี้ › ลูกหนี้คงค้าง | `menu_singha_report_ar_outstanding` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › ลูกหนี้ › ยอดลูกหนี้คงเหลือ ตามระยะเวลาเครดิต | `menu_singha_report_customer_credit_balance_by_creditdate` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › สินค้า › สรุปการ์ดสินค้า | `menu_singha_report_stock_movement` | `SINGHAReport.GL._glReport` |  |
| รายงาน › สินค้า › สรุปโหลดสินค้า รายคลัง | `menu_singha_report_load_product_warehouse` | `SINGHAReport.GL._glReport` |  |
| รายงาน › เงินสด/ธนาคาร › รายงาน Bank Statement | `menu_singha_report_bank_statement` | `SINGHAReport._singhareportGenerate` |  |
| รายงาน › เงินสด/ธนาคาร › เช็ครับ › รายงานการตัดเช็ค | `report_singha_chq_receive_movement` | `SINGHAReport._singhareportGenerate` |  |
| ลูกหนี้ › ข้อมูลลูกหนี้ › รายงาน › รายงานรายละเอียดลูกค้า-ตามรหัสลูกค้า | `menu_ar_report_detail_ar` | `SMLERPReport.ar._report_ar_detail` |  |
| ลูกหนี้ › ข้อมูลลูกหนี้ › รายงาน › รายงานแต้มคงเหลือลูกหนี้ | `menu_report_point_balance` | `SMLERPARReport.report._ar_report` | ลูกหนี้_แต้มคงเหลือ |
| ลูกหนี้ › รายงาน › รายงานตั้งหนี้ยกมา | `menu_ar_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ตั้งหนี้ยกมา, 93 |
| ลูกหนี้ › รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ar_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` | ลูกหนี้_เพิ่มหนี้ยกมา, 95 |
| ลูกหนี้ › รายงาน › รายงานลดหนี้ยกมา | `menu_ar_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ลดหนี้ยกมา, 97 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_ar_cancel_increase_debt_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_เพิ่มหนี้อื่น_ยกเลิก, 102 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_ar_documents_early_year_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ตั้งหนี้อื่น, 99 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_report_ar_increase_debt_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_เพิ่มหนี้อื่น, 101 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_ar_reduction_dept_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ลดหนี้อื่น, 103 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_ar_cancel_documents_early_year_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ตั้งหนี้อื่น_ยกเลิก, 100 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_ar_cancel_reduction_dept_other` | `SMLERPReportTool._reportTrans` | ลูกหนี้_ลดหนี้อื่น_ยกเลิก, 104 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกใบวางบิล(ลูกหนี้) | `menu_ar_report_cancel_pay_billing` | `SMLERPReportTool._reportArApTrans` | ลูกหนี้_รับวางบิล_ยกเลิก, 236 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_cancel_invoice` | `SMLERPReportTool._reportArApTrans` | ลูกหนี้_รับชำระหนี้_ยกเลิก, 240 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานใบวางบิล (ลูกหนี้) | `menu_ar_report_billing` | `SMLERPReportTool._reportArApTrans` | ลูกหนี้_รับวางบิล, 235 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานการรับชำระหนี้ประจำวัน | `menu_ar_report_pay_debt_trans` | `SMLERPReportTool._reportArApTrans` | ลูกหนี้_รายงานการรับชำระหนี้ประจำวัน, 239 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานการรับชำระหนี้/ออกใบเสร็จรับเงิน | `menu_ar_report_receipt` | `SMLERPReportTool._reportArApTrans` | ลูกหนี้_รับชำระหนี้, 239 |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงายใบเสร็จรับเงินพร้อมรายการย่อย | `menu_ar_report_receipt_and_detail` | `SMLERPReport.ar._report_ar_receipt_and_detail` |  |
| ลูกหนี้ › รายงาน/ยกเลิก › รายงานใบวางบิลตามพนักงานเก็บเงิน | `menu_report_billing_note_by_customer_cashier` | `IMEXControl.report.report_billing_note_by_customer_cashier` |  |
| ลูกหนี้ › รายงานวิเคราะห์ › รายงานเคลื่อนไหวลูกหนี้ | `menu_ar_report_movement` | `SMLERPARAPReport.report._movement` |  |
| ลูกหนี้ › รายงานวิเคราะห์ › รายงานอายุลูกหนี้ | `menu_ar_report_period_ar_debt_remain` | `SMLERPARAPReport.report._ageing` |  |
| ลูกหนี้ › รายงานวิเคราะห์ › รายงานอายุลูกหนี้-ตามเอกสาร | `menu_ar_report_period_ar_debt_remain_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |
| ลูกหนี้ › รายงานวิเคราะห์ › รายงานสถานะลูกหนี้ | `menu_ar_report_status_ar` | `SMLERPARAPReport.report._absolute_status` |  |
| ลูกหนี้ › รายงานวิเคราะห์ › รายงาน Statement ลูกหนี้ | `menu_report_imex_ar_statement` | `IMEXControl.report._reportARStatement` |  |
| ลูกหนี้ › รายงานสรุป › รายงานตรวจสอบยอดวงเงิน | `menu_ar_report_check_balance` | `SMLERPReport.ar._report_ar_check_balance` |  |
| สินค้า › ข้อมูลสินค้า › รายงาน › รายงานรายละเอียดสินค้า | `menu_ic_detail` | `SMLERPICReport._report_ic_master` |  |
| สินค้า › ข้อมูลสินค้า › รายงาน › รายงานสินค้าชุด | `menu_ic_report_item_set_formula` | `SMLERPICReport._report_item_set_formula` |  |
| สินค้า › ข้อมูลสินค้า › รายงาน › รายงานบาร์โค้ดสินค้า | `menu_ic_report_item_barcode` | `SMLERPICReport._report_ic_barcode` |  |
| สินค้า › ข้อมูลสินค้า › รายงาน › รายงานสินค้าแบบมี Serial | `menu_ic_by_license` | `SMLERPICReport._report_ic_summary` | Item_by_serial |
| สินค้า › ระบบตรวจนับสินค้า › รายงานผลต่างจากการตรวจนับ | `menu_diff_from_count` | `SMLERPICReport._report_ic_summary` | รายงานผลต่างจากการตรวจนับ |
| สินค้า › ระบบตรวจนับสินค้า › รายงานสินค้าที่ไม่มีการตรวจนับแต่มียอดคงเหลือ | `menu_stock_no_balance_from_count` | `SMLERPICReport._report_ic_summary` | Stock_no_count_no_balance |
| สินค้า › ระบบตรวจนับสินค้า › รายงานการตรวจสอบสินค้า Serial | `menu_report_serial_check` | `SMLERPICReport._report_ic_summary` | สินค้า_รายงานการตรวจสอบสินค้า_serial |
| สินค้า › รายงาน › รายงานราคาซื้อสินค้า | `menu_ic_report_item_purchase_price` | `SMLERPICReport._report_ic_purchase_price` |  |
| สินค้า › รายงาน › รายงานของแถมซื้อ | `menu_ic_report_item_giveaway` | `SMLERPICReport._report_ic_summary` | Item_Giveaway |
| สินค้า › รายงาน › รายงานราคาขายสินค้ามาตรฐาน | `menu_ic_report_item_sale_price` | `SMLERPICReport._report_ic_sale_price` |  |
| สินค้า › รายงาน › รายงานราคาขายสินค้าทั่วไป | `menu_ic_report_item_sale_price_normal` | `SMLERPICReport._report_ic_sale_price` |  |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกรับสินค้าสำเร็จรูป | `menu_ic_report_cancel_goods_pack` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับสินค้าสำเร็จรูป_ยกเลิก, 61 |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกใบเบิกสินค้า/วัตถุดิบ | `menu_ic_report_cancel_raw_material` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานเบิกสินค้าวัตถุดิบ_ยกเลิก, 57 |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกรับคืนสินค้า/วัตถุดิบ จากการเบิก | `menu_ic_report_cancel_goods_raw_meterial` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับคืนเบิกสินค้าวัตถุดิบ_ยกเลิก, 59 |
| สินค้า › รายงาน/ยกเลิก › รายงานสินค้าและวัตถุดิบ คงเหลือยกมา | `menu_ic_report_goods_balance` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานสินค้าและวัตถุดิบคงเหลือยกมา, 54 |
| สินค้า › รายงาน/ยกเลิก › รายงานการรับสินค้าสำเร็จรูป | `menu_import_item_ready_by_date` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับสินค้าสำเร็จรูป, 60 |
| สินค้า › รายงาน/ยกเลิก › รายงานการเบิกสินค้าและวัตถุดิบ | `menu_ic_report_item_withdraw` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานเบิกสินค้าวัตถุดิบ, 56 |
| สินค้า › รายงาน/ยกเลิก › รายงานรับคืนสินค้าและวัตถุดิบ จากการเบิก | `menu_ic_report_item_return` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับคืนเบิกสินค้าวัตถุดิบ, 58 |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกโอนสินค้า/วัตถุดิบ | `menu_ic_report_stk_cancel` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานโอนสินค้าและวัตถุดิบ_ยกเลิก, 73 |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (เกิน) | `menu_ic_report_stk_cancel_over` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับสินค้าสำเร็จรูป_ยกเลิก, 67 |
| สินค้า › รายงาน/ยกเลิก › รายงานยกเลิกปรับปรุงสต๊อกสินค้า/วัตถุดิบ (ขาด) | `menu_ic_report_stk_cancel_lost` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานรับสินค้าสำเร็จรูป_ยกเลิก, 69 |
| สินค้า › รายงาน/ยกเลิก › รายงานการโอนสินค้าและวัตถุดิบ | `menu_ic_report_item_transfer` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานโอนสินค้าและวัตถุดิบ, 72 |
| สินค้า › รายงาน/ยกเลิก › รายงานตรวจนับสินค้า | `menu_ic_report_item_count` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานสินค้าตรวจนับ, 76 |
| สินค้า › รายงาน/ยกเลิก › รายงานการปรับปรุงสต็อกสินค้าและวัตถุดิบ (เกิน) | `menu_ic_report_item_adjust_increase` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_เกิน, 66 |
| สินค้า › รายงาน/ยกเลิก › รายงานการปรับปรุงสต๊อกสินค้าและวัตถุดิบ (ขาด) | `menu_ic_report_item_adjust_decrease` | `SMLERPReportTool._reportTrans` | สินค้า_รายงานปรับปรุงสินค้าและวัตถุดิบ_ขาด, 68 |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้นตามเอกสาร (แสดงส่วนลด) | `menu_ic_report_info_stk_profit_by_doc_and_discount` | `SMLERPICReport.ic_analysis._report_info_stk_profit_by_doc_and_discount` | สินค้า_รายงานกำไรขั้นต้นตามเอกสารแบบมีส่วนลด |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า) | `menu_ic_report_info_stk_profit` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า) | `menu_ic_report_info_stk_profit_ic_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (สินค้า-ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_ic_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร) | `menu_ic_report_info_stk_profit_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า) | `menu_ic_report_info_stk_profit_cust` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า) | `menu_ic_report_info_stk_profit_cust_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-สินค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_ic_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร) | `menu_ic_report_info_stk_profit_cust_doc` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานกำไรขั้นต้น › รายงานกำไรขั้นต้น (ลูกค้า-เอกสาร-สินค้า) | `menu_ic_report_info_stk_profit_cust_doc_ic` | `SMLERPICReport.ic_analysis._ic_report_info_stk_profit` |  |
| สินค้า › รายงานวิเคราะห์ › รายงานเคลื่อนไหว Serial Number | `menu_ic_serial_number` | `SMLERPICReport._report_ic_summary` | Serial_number |
| สินค้า › รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า | `menu_item_balance` | `SMLERPICReport._report_ic_balance` | สินค้า_รายงานยอดคงเหลือสินค้า |
| สินค้า › รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้าตาม LOT | `menu_item_balance_lot` | `SMLERPICReport._report_ic_balance` | สินค้า_รายงานยอดคงเหลือสินค้า_Lot |
| สินค้า › รายงานวิเคราะห์ › รายงานสินค้าที่ถึงจุดสั่งซื้อ | `menu_ic_report_info_stk_reorder` | `SMLERPICReport.ic_analysis._report_ic_stk_reorder` | สินค้า_ถึงจุดสั่งซื้อ_ตามสินค้า |
| สินค้า › รายงานวิเคราะห์ › รายงานยอดคงเหลือสินค้า ณ ปัจจุบัน(เฉพาะสินค้ามี Serial) | `menu_item_balance_now_only_serial` | `SMLERPICReport._report_ic_summary` | Item_Balance_now_Only_Serial |
| สินค้า › รายงานวิเคราะห์ › รายงานสินค้าที่ไม่มีการเคลื่อนไหว | `menu_item_non_transfer` | `SMLERPICReport._report_ic_none_movement` |  |
| สินค้า › รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้า | `menu_item_transfer` | `SMLERPICReport._report_ic_stk_movement` | สินค้า_รายงานเคลื่อนไหว |
| สินค้า › รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า | `menu_result_transfer_item` | `SMLERPICReport._report_ic_info_stk_movement_sum` |  |
| สินค้า › รายงานวิเคราะห์ › รายงานสรุปเคลื่อนไหวปริมาณสินค้า-แสดงมูลค่า | `menu_report_ic_info_stk_movement_sum_show_amount` | `SMLERPICReport._report_ic_info_stk_movement_sum_show_amount` |  |
| สินค้า › รายงานสรุป › รายงานสถานะสินค้า | `menu_item_status` | `SMLERPICReport._report_ic_summary` | Item_status |
| สินค้า › รายงานสรุป › รายงานบัญชีคุมพิเศษสินค้า | `menu_account_special_item` | `SMLERPICReport._report_ic_stk_movement` | สินค้า_รายงานบัญชีคุมพิเศษ |
| สินค้า › รายงานสรุป › รายงานสินค้าและวัตถุดิบ | `menu_report_ic_product_and_material` | `SMLERPICReport._report_ic_product_and_material` |  |
| เงินสด/ธนาคาร › ธนาคาร › บัตรเครดิต › รายงานขึ้นเงินบัตรเครดิต | `menu_cb_report_credit_card_pass` | `SMLERPReportTool._reportCashBankTrans` | บัตรเครดิต_ขึ้นเงิน, 461 |
| เงินสด/ธนาคาร › ธนาคาร › บัตรเครดิต › รายงานยกเลิกบัตรเครดิต | `menu_report_cb_credit_card_cancel` | `SMLERPReportTool._reportCashBankTrans` | บัตรเครดิต_ยกเลิก, 462 |
| เงินสด/ธนาคาร › ธนาคาร › บัตรเครดิต › รายงานรายการรับบัตรเครดิต | `menu_cb_report_credit_card_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` | บัตรเครดิต_รายงานบัตรเครดิต_ตามวันที่รับ |
| เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานการโอนเงินระหว่างธนาคาร | `menu_cb_report_transfer_bank` | `SMLERPReportTool._reportCashBankTrans` | ธนาคาร_โอนเงิน, 422 |
| เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกฝากเงิน | `menu_report_cancel_withdraw` | `SMLERPReportTool._reportCashBankTrans` | ธนาคาร_ฝากเงิน_ยกเลิก, 403 |
| เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกถอนเงิน | `menu_report_cancel_payin` | `SMLERPReportTool._reportCashBankTrans` | ธนาคาร_ถอนเงิน_ยกเลิก, 404 |
| เงินสด/ธนาคาร › ธนาคาร › ฝาก/ถอน › รายงาน/ยกเลิก › รายงานยกเลิกการโอนเงินระหว่างธนาคาร | `menu_report_transfer_bank_cancel` | `SMLERPReportTool._reportCashBankTrans` | ธนาคาร_โอนเงิน_ยกเลิก, 423 |
| เงินสด/ธนาคาร › ธนาคาร › รายงาน › รายงานเคลื่อนไหวเงินสด | `_menu_cash_movements` | `SMLERPCASHBANKReport._cashbank_report` | เคลื่อนไหวเงินสด |
| เงินสด/ธนาคาร › ธนาคาร › รายงาน › รายงานการรับเงินอื่นๆพร้อมรายการย่อย | `_menu_received_cash_sub_item` | `SMLERPReport.cash_bank.Received_Cash_sub_item` |  |
| เงินสด/ธนาคาร › ธนาคาร › รายงาน › รายงาน Bank Statement | `_menu_bank_statement` | `SMLERPReport.cash_bank._bankStatment` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คจ่ายยกมา | `menu_cb_report_chq_out_payment_balance` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_ยกมา, 406 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็คจ่าย) | `menu_bank_report_chq_out_pass` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_ผ่าน, 451 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คคืน (เช็คจ่าย) | `menu_bank_report_chq_out_return` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_คืน, 453 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็คจ่าย) | `menu_bank_report_chq_out_pass_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_ขาดสิทธิ์, 452 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็คจ่าย) | `menu_bank_report_chq_out_change` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_เปลี่ยนเช็ค, 456 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คจ่ายผ่าน | `menu_report_cb_chq_out_honor_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_ผ่าน_ยกเลิก, 471 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็คจ่าย | `menu_report_cb_chq_out_cancel_hornor_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_ขาดสิทธิ์_ยกเลิก, 472 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเช็คคืน | `menu_report_chq_out_return_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_คืน_ยกเลิก, 473 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็คจ่าย | `menu_report_cb_chq_out_change_cancle` | `SMLERPReportTool._reportCashBankTrans` | เช็คจ่าย_เปลี่ยน_ยกเลิก, 476 |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานทะเบียนเช็คจ่าย | `menu_cb_report_chq_out_payment` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` | เช็ค_รายงานเช็คจ่าย_ตามวันที่จ่ายเช็ค |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_pay_by_date_by_status` | `IMEXControl.report.report_chq_pay_by_status` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย - ตามวันที่ - ตามสถานะเช็ค | `imex_report_cheque_pay_status_by_date` | `IMEXControl.report._report_chq_pay_status_by_date` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็คจ่าย › รายงาน/ยกเลิก › รายงานรายละเอียดเช็คจ่าย ณ วันที่ | `menu_imex_report_chq_pay_at_date` | `IMEXControl.report._report_chq_pay_last_status_by_date` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็ครับยกมา | `menu_cb_report_chq_in_receive_balance` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ยกมา, 405 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานนำฝาก (เช็ครับ) | `menu_bank_report_chq_in_deposit` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ฝาก, 410 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คผ่าน (เช็ครับ) | `menu_bank_report_chq_in_pass` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ผ่าน, 411 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรับคืน (เช็ครับ) | `menu_bank_report_chq_in_return` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_รับคืน, 412 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานเช็คขาดสิทธิ์ (เช็ครับ) | `menu_bank_report_chq_in_pass_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ขาดสิทธิ์, 413 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานการเปลี่ยนเช็ค (เช็ครับ) | `menu_bank_report_chq_in_change` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_เปลี่ยนเช็ค, 416 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกนำฝากเช็ค | `menu_report_cb_chq_in_payin_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ฝาก_ยกเลิก, 430 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็คผ่าน | `menu_report_cb_chq_in_honor_cancle` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ผ่าน_ยกเลิก, 431 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเช็ครับคืน | `menu_report_cb_chq_in_return_cancle` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_รับคืน_ยกเลิก, 432 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิก ยกเลิกเช็ค | `menu_report_cb_chq_cancel` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_ขาดสิทธิ์_ยกเลิก, 433 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานยกเลิกเปลี่ยนเช็ค | `menu_report_cb_chq_in_change_cancle` | `SMLERPReportTool._reportCashBankTrans` | เช็ครับ_เปลี่ยน_ยกเลิก, 436 |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานทะเบียนเช็ครับ | `menu_cb_report_chq_in_receive` | `SMLERPCASHBANKReport._report_chq._chqCreditCardList` | เช็ค_รายงานเช็ครับ_ตามวันที่รับเช็ค |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานใบนำฝากเช็ครับพร้อมรายการย่อย | `menu_report_chq_card_disposit_cheque_detail` | `SMLERPReport.Cheque_Card._report_chq_card_Disposit_Cheque_Detail` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่รับ - ตามสถานะเช็ค แสดงยอดรวม | `imex_report_cheque_received_by_date_by_status` | `IMEXControl.report._report_chq_receive_by_status` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามวันที่ - ตามสถานะเช็ค แสดงยอดรวม | `menu_imex_report_chqreceive_status_by_date` | `IMEXControl.report._report_chq_receive_status_by_date` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ตามสถานะเช็ค แสดงยอดรวม(ไม่รวมเช็คคืน,เช็คคืนตั้งหนี้ใหม่) | `menu_imex_report_chqreceive_status_by_date_only_hand` | `IMEXControl.report._report_chq_receive_status_by_date_2` |  |
| เงินสด/ธนาคาร › ธนาคาร › เช็ครับ › รายงาน/ยกเลิก › รายงานรายละเอียดเช็ครับ - ณ วันที่ | `menu_imex_report_chq_receive_at_date` | `IMEXControl.report._report_chq_receive_last_status_by_date` |  |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานรายได้อื่นๆ | `menu_cash_income_other_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น, 250 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น_ลดหนี้, 252 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้, 254 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกรายได้อื่นๆ | `menu_cash_income_other_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น_ยกเลิก, 251 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้รายได้อื่นๆ | `menu_cash_income_other_credit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น_ลดหนี้_ยกเลิก, 253 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้รายได้อื่นๆ | `menu_cash_income_other_debit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายได้อื่น_เพิ่มหนี้_ยกเลิก, 255 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น, 260 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้, 262 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้, 264 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น_ยกเลิก, 261 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_credit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น_ลดหนี้_ยกเลิก, 263 |
| เงินสด/ธนาคาร › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้ค่าใช้จ่ายอื่นๆ | `menu_cash_expense_other_debit_cancel_report` | `SMLERPReportTool._reportCashBankTrans` | เงินสดธนาคาร_รายจ่ายอื่น_เพิ่มหนี้_ยกเลิก, 265 |
| เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกเบิกเงินสดย่อย | `menu_report_cb_cancel_pettycash_request` | `SMLERPReportTool._reportTrans` | เงินสดย่อย_เบิก_ยกเลิก, 302 |
| เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงาน/ยกเลิก › รายงานยกเลิกรับเงินสดย่อย | `menu_report_cb_cancel_pettycash_return` | `SMLERPReportTool._reportTrans` | เงินสดย่อย_รับคืน_ยกเลิก, 303 |
| เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงานสรุป › รายงานเคลื่อนไหวเงินสดย่อย | `menu_sub_cash_movements` | `SMLERPCASHBANKReport._report_petty_cash` | เงินสดย่อย_เคลื่อนไหว |
| เงินสด/ธนาคาร › เงินสด/เงินสดย่อย › รายงานสรุป › รายงานสถานะเงินสดย่อย | `menu_peety_cash_status` | `SMLERPCASHBANKReport._report_petty_cash` | เงินสดย่อย_สถานะ |
| เจ้าหนี้ › ข้อมูลเจ้าหนี้ › รายงานรายละเอียดเจ้าหนี้ | `menu_ap_report_detail_ap` | `SMLERPReportTool._reportCustMaster` | เจ้าหนี้_รายละเอียด |
| เจ้าหนี้ › รายงาน › รายงานตั้งหนี้ยกมา | `menu_ap_report_early_year_balance_setup` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ตั้งหนี้ยกมา, 81 |
| เจ้าหนี้ › รายงาน › รายงานลดหนี้ยกมา | `menu_ap_report_early_year_balance_decrease` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ลดหนี้ยกมา, 85 |
| เจ้าหนี้ › รายงาน › รายงานเพิ่มหนี้ยกมา | `menu_ap_report_early_year_balance_increase` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_เพิ่มหนี้ยกมา, 83 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานตั้งหนี้อื่นๆ | `menu_documents_early_year_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ตั้งหนี้อื่น, 87 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานเพิ่มหนี้อื่นๆ | `menu_increase_debt_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_เพิ่มหนี้อื่น, 89 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานลดหนี้อื่นๆ | `menu_reduction_dept_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ลดหนี้อื่น, 91 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกตั้งหนี้อื่นๆ | `menu_cancel_documents_early_year_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ตั้งหนี้อื่น_ยกเลิก, 88 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกเพิ่มหนี้อื่นๆ | `menu_cancel_increase_debt_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_เพิ่มหนี้อื่น_ยกเลิก, 90 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกลดหนี้อื่นๆ | `menu_cancel_reduction_dept_other` | `SMLERPReportTool._reportTrans` | เจ้าหนี้_ลดหนี้อื่น_ยกเลิก, 92 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกใบรับวางบิล ( เจ้าหนี้ ) | `menu_ap_report_cancel_pay_bill` | `SMLERPReportTool._reportArApTrans` | เจ้าหนี้_รับวางบิล_ยกเลิก, 214 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานยกเลิกจ่ายชำระ (เจ้าหนี้) | `menu_ap_report_cancel_debt_billing` | `SMLERPReportTool._reportArApTrans` | เจ้าหนี้_จ่ายชำระหนี้_ยกเลิก, 23 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานใบรับวางบิล (เจ้าหนี้) | `menu_ap_report_billing` | `SMLERPReportTool._reportArApTrans` | เจ้าหนี้_รับวางบิล, 213 |
| เจ้าหนี้ › รายงาน/ยกเลิก › รายงานการจ่ายชำระหนี้ (เจ้าหนี้) | `menu_ap_report_payment` | `SMLERPReportTool._reportArApTrans` | เจ้าหนี้_จ่ายชำระหนี้, 19 |
| เจ้าหนี้ › รายงานวิเคราะห์ › รายงานเคลื่อนไหวเจ้าหนี้ | `menu_ap_report_payable_movement` | `SMLERPARAPReport.report._movement` |  |
| เจ้าหนี้ › รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้ | `menu_ap_report_payable_aging` | `SMLERPARAPReport.report._ageing` |  |
| เจ้าหนี้ › รายงานวิเคราะห์ › รายงานอายุเจ้าหนี้-ตามเอกสาร | `menu_ap_report_payable_aging_by_doc` | `SMLERPARAPReport.report._ageingByCodeAndDoc` |  |
| เจ้าหนี้ › รายงานวิเคราะห์ › รายงานสถานะเจ้าหนี้ | `menu_ap_report_payable_status` | `SMLERPARAPReport.report._absolute_status` |  |
| เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม | `menu_form_edit` | `SMLReport._formReport._formDesigner` |  |
| เริ่มต้น › เครื่องมือ › นำเข้าแบบฟอร์ม | `menu_import_formdesign` | `SMLReport._ImportFormDesign` |  |
| เริ่มต้น › เครื่องมือ › นำเข้ารายงาน | `menu_import_report` | `SMLFastReport._importFastReport` |  |
| เริ่มต้น › เครื่องมือ › นำเข้ารายงานสาขา | `menu_import_report_branch` | `SMLFastReport._importFastReport` |  |
