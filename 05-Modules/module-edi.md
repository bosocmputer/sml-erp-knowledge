---
tags: [sml, module, edi, generated]
menu_group: "EDI"
trans_flags: []
---
# โมดูล: EDI

กลับไป [[modules-index]] · [[00-Index]]

## ตัวเลข

- เมนูปลายทาง 2 รายการ, จับคู่คลาสได้ 2
- คลาสหน้าจอที่ใช้บ่อย: `SMLEDIControl._ediExternal` (1), `SMLEDIControl._ediExport` (1)
- control หลักที่ฝัง: -

## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)

`edi_product_list`, `edi_barcode_list`, `edi_external`, `edi_unit_list`, `edi_ar_list`, `ic_trans_detail`, `resource_report`, `ic_trans`

## เมนูทั้งหมด

| เมนู | menu name | คลาส | trans_flag | ตาราง |
|---|---|---|---|---|
| รายละเอียดลูกค้า EDI | `menu_edi_external` | `SMLEDIControl._ediExternal` |  | edi_product_list, edi_barcode_list, edi_unit_list, edi_ar_list |
| ส่งออกข้อมูล EDI | `menu_edi_export` | `SMLEDIControl._ediExport` |  | edi_external, edi_product_list, ic_trans_detail, resource_report |
