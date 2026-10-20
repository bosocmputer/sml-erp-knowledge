---
tags: [sml, form, print]
source: smlerp/SMLReport/_formReport/*, SMLERPGlobal dictionary (formdesign, erp_doc_format)
status: from-code
date: 2026-10-20
---
# ฟอร์มพิมพ์เอกสาร (ใบกำกับ ใบเสร็จ ใบสั่งซื้อ ฯลฯ)

กลับไป [[00-Index]] · รายงาน [[reports]] · รูปแบบเอกสาร [[pricing-vat-gl]]

- **เก็บที่** ตาราง `formdesign` ใน DB ของร้าน: `formcode`, `formname`, `formdesigntext` (แบบฟอร์มทั้งหมดเป็นข้อความ/XML), `formbackground`, `form_type` (`form_print` ฟอร์มเอกสาร, `form_barcode` ฟอร์มบาร์โค้ด, `form_transportlabel` ฟอร์มจัดส่ง), `timeupdate`
- **ผูกกับเอกสาร** ผ่านรูปแบบเอกสาร `erp_doc_format.form_code` และ `form_code_1..5` (หนึ่งรูปแบบเอกสารเลือกพิมพ์ได้หลายฟอร์ม) และ `tax_format` (รูปแบบใบกำกับภาษี)
- **ออกแบบ** เมนู `menu_form_edit` → `SMLReport._formReport._formDesigner` (วาดกระดาษ `_drawPaper`, `_drawPaperXml`); นำเข้า `menu_import_formdesign` → `SMLReport._ImportFormDesign` (ดึงแบบจาก server กลาง)
- **พิมพ์** `SMLReport._formReport._formPrint` (+ `_formPrintOption`, `_formDesignLabelPrint` สำหรับฉลาก) — ใช้ query ของฟอร์มดึงข้อมูลเอกสารตาม doc_no แล้ววางตามตำแหน่งในแบบ
- **บันทึกการพิมพ์** `erp_print_logs` (นับครั้งการพิมพ์ ใช้ตรวจการพิมพ์ซ้ำ), ตารางช่วย `form_print_detail_temp`
- ตารางแม่แบบฟอร์มเฉพาะ: `resource_form_quotation`, `resource_form_purchase_order`, `resource_form_sale_order` ดู [[dict-form]]
- สลิป POS ไม่ใช้ formdesign — วาดในโค้ด `_posClientForm._printSlip` ดู [[pos-client]]

## ยังไม่ได้ไล่
- โครงสร้างภายใน `formdesigntext` และภาษา expression ของฟิลด์ในฟอร์ม
