---
tags: [sml, database, dictionary, generated]
---
# พจนานุกรมข้อมูล SML (Data Dictionary)

> สร้างอัตโนมัติด้วย `scripts/gen_dictionary.py` จากไฟล์ออกแบบทางการของ SML (`SMLERPTemplate/smldatabase.xml` + `SMLDatabaseDesign_New.xml`) — คำอธิบายภาษาไทย/อังกฤษทุกคอลัมน์ ข้อมูลดิบสำหรับ agent: `02-Database/dictionary.json`

ทั้งหมด 520 ตาราง 9,988 คอลัมน์ · โครงสร้างจริงใน DB ดู [[schema-index]] · ที่เก็บเอกสาร [[data-model]] · กลับไป [[00-Index]]

หมายเหตุ: `resource_only=true` = คอลัมน์ที่มีไว้เป็นป้ายบนหน้าจอ/รายงาน ไม่ได้สร้างใน DB

| โมดูล | ความหมาย | ตาราง | โน้ต |
|---|---|---|---|
| Master | ข้อมูลหลัก | 74 | [[dict-master]] |
| Setup | ตั้งค่าระบบ | 69 | [[dict-setup]] |
| IC | สินค้า | 51 | [[dict-ic]] |
| POS | POS | 47 | [[dict-pos]] |
| WMS | คลังสินค้า WMS | 39 | [[dict-wms]] |
| GL | บัญชีแยกประเภท | 36 | [[dict-gl]] |
| IC_Trans | เอกสารสินค้า (ic_trans) | 33 | [[dict-ic-trans]] |
| AP_AR | ลูกหนี้/เจ้าหนี้ | 30 | [[dict-ap-ar]] |
| IMEX | IMEX (OEM) | 26 | [[dict-imex]] |
| Healthy | สุขภาพ/ร้านยา | 19 | [[dict-healthy]] |
| AP_AR_Trans | เอกสารลูกหนี้/เจ้าหนี้ | 13 | [[dict-ap-ar-trans]] |
| Cash_Bank | เงินสด/ธนาคาร | 11 | [[dict-cash-bank]] |
| Temp | ตารางชั่วคราว | 11 | [[dict-temp]] |
| Asset | สินทรัพย์ | 10 | [[dict-asset]] |
| Report | รายงาน | 9 | [[dict-report]] |
| EDI | EDI | 8 | [[dict-edi]] |
| Pick_and_Pack | Pick and Pack | 7 | [[dict-pick-and-pack]] |
| Thai7 | Thai7 | 7 | [[dict-thai7]] |
| Draft | ร่างเอกสาร | 5 | [[dict-draft]] |
| Form | ฟอร์มพิมพ์ | 4 | [[dict-form]] |
| Sync | Sync | 4 | [[dict-sync]] |
| Mobillyst_TMS | Mobillyst TMS | 3 | [[dict-mobillyst-tms]] |
| Utility | Utility | 2 | [[dict-utility]] |
| Cloud | Cloud | 1 | [[dict-cloud]] |
| E-Tax | e-Tax | 1 | [[dict-e-tax]] |
