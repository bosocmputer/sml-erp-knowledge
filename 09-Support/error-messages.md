---
tags: [sml, support, generated, error-messages]
status: from-code
---
# ข้อความที่โปรแกรม SML แสดง (MessageBox)

> สร้างอัตโนมัติด้วย `scripts/gen_error_messages.py` จากโค้ด smlerp — ห้ามแก้มือ (แก้ที่ script แล้วรันใหม่)
> กลับไป [[00-Index]] · คำถามที่พบบ่อย [[faq]] · ใช้ร่วมกับ [[menu-map]]

**วิธีใช้:** ค้นด้วยข้อความที่ร้านเห็นบนหน้าจอ (Ctrl+F หรือถาม AI) — คอลัมน์ "ที่โค้ด" บอกหน้าจอ/ฟังก์ชันที่แสดงข้อความ, "เมนู" คือเมนูที่หน้าจอนั้นเป็นของเมนูโดยตรง; ถ้าขึ้นว่า "ส่วนกลาง" = ข้อความมาจาก control ที่ใช้ร่วมหลายหน้าจอ (เช่น `_icTransControl` ของเอกสารขาย/ซื้อ/สต็อก) ให้ดูชื่อ control และฟังก์ชันในคอลัมน์ "ที่โค้ด"

⚠️ **ระดับ from-code:** ได้มาจากการอ่านโค้ด ยังไม่ได้ยืนยันว่าทุกข้อความขึ้นจริงในทุก edition; `{…}` = ค่าที่โปรแกรมแทรกตอนแสดง (เลขที่, ชื่อ, ข้อความจาก server); ข้อความผ่าน `_resource()` บางตัวอาจถูกแปลใหม่จากตาราง `sml_resource` ของร้าน

รวม 851 ข้อความ (ครอบคลุม 2,062 จาก 3,153 จุดในโค้ด) · คำแปลรหัส (`warningNN` ฯลฯ) จาก `MyLib/_smlResourceManager.cs` 175 รายการ

จุดที่ไม่อยู่ในรายการ = ข้อความที่สร้างตอนรันทั้งก้อน (เช่น `MessageBox.Show(__result)` ที่แสดงข้อความ error จาก web service/PostgreSQL หรือ `ex.Message`) — ดูส่วน "ข้อความจาก server" ด้านล่าง

## ข้อความจาก server / database ที่โปรแกรมแปลให้ (`MyLib/_global.cs` `_errorText`)

| ข้อความที่ร้านเห็น | สาเหตุ (ข้อความ PostgreSQL ที่ตรวจพบ) |
|---|---|
| เลขที่เอกสารซ้ำ | `duplicate key value violates unique constraint` + `ic_trans_ic_trans_pk_primary` (unique `doc_no, trans_flag` ดู [[write-spec-sale-order]] §1) |
| เลขที่ เอกสารหัก ณ ที่จ่าย ซ้ำ | duplicate key + `gl_wht_list_gl_wht_list_doc_no` |
| รหัสซ้ำ | duplicate key อื่น ๆ (เช่น บาร์โค้ดซ้ำ — unique `ic_inventory_barcode.barcode` ดู [[write-spec-master-product]]) |

## สารบัญตามโปรเจกต์ (โมดูลในโค้ด)

- [[#SMLInventoryControl]] (165)
- [[#MyLib]] (98)
- [[#SMLPosClient]] (88)
- [[#SMLAPARControl]] (83)
- [[#SMLPOSControl]] (46)
- [[#SMLERPIC]] (29)
- [[#SMLERPGlobal]] (26)
- [[#SMLERPGL]] (24)
- [[#SMLERPControl]] (21)
- [[#SMLReport]] (18)
- [[#DTSClientDownload]] (17)
- [[#SMLBalanceTransfer]] (17)
- [[#SMLERPConfig]] (16)
- [[#SMLERPGLControl]] (13)
- [[#IMEXControl]] (12)
- [[#SMLActivesync]] (11)
- [[#SMLERPASSET]] (10)
- [[#SMLTransferDataPOS]] (9)
- [[#AkzoGenPo]] (8)
- [[#SMLERPTransferControl]] (8)
- [[#SMLSyncCheckingTools]] (8)
- [[#SMLERPAP]] (6)
- [[#SMLFastReport]] (6)
- [[#SMLProcess]] (6)
- [[#BRInterface]] (4)
- [[#SMLBarcodeManage]] (4)
- [[#SMLDatabaseDesign]] (4)
- [[#SMLERPICInfo]] (4)
- [[#SMLERPSO]] (4)
- [[#SMLETaxInvoice]] (4)
- [[#SMLMDBImportConfig]] (4)
- [[#SMLOffTakeSalesAdmin]] (4)
- [[#SMLTransfer]] (4)
- [[#SMLAccount]] (3)
- [[#SMLERPICReport]] (3)
- [[#SMLGetPrice]] (3)
- [[#SMLICIAdmin]] (3)
- [[#SMLQRPayment]] (3)
- [[#SMLStockMovementTransfer]] (3)
- [[#SMLTransportLabel]] (3)
- [[#AKZOPODownloadConfig]] (2)
- [[#BCTOSML]] (2)
- [[#EarthStockManage]] (2)
- [[#PackShipMoveParcelPrint]] (2)
- [[#PromptPayQRCode]] (2)
- [[#SMLDataQuery]] (2)
- [[#SMLEDIControl]] (2)
- [[#SMLERPAR]] (2)
- [[#SMLERPCASHBANKReport]] (2)
- [[#SMLERPReport]] (2)
- [[#SMLERPTemplate]] (2)
- [[#SMLLanguage]] (2)
- [[#SMLPOS]] (2)
- [[#SMLPOSChecker]] (2)
- [[#TEST]] (2)
- [[#HTMLwysiwygLib]] (1)
- [[#ICCManage]] (1)
- [[#IMEXDataTransfer]] (1)
- [[#IMSSalesCommission]] (1)
- [[#SMLBillFree]] (1)
- [[#SMLDataCenterSync]] (1)
- [[#SMLDataTransfer]] (1)
- [[#SMLERPARReport]] (1)
- [[#SMLERPPOReport]] (1)
- [[#SMLERPReportTool]] (1)
- [[#SMLERPSOReport]] (1)
- [[#SMLFastReportUpdate]] (1)
- [[#SMLFormDesignGenerate]] (1)
- [[#SMLHealthy]] (1)
- [[#SMLLogQueryGen]] (1)
- [[#SMLPickAndPack]] (1)
- [[#SMLSyncClient]] (1)
- [[#SMLTOBC]] (1)
- [[#SMLTemplate]] (1)

## SMLInventoryControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่พบ : {…} | แจ้ง | 62 | SMLAPARControl/_ar_ap_trans_screen_top.cs:2086 `_search`<br>SMLAPARControl/_ar_cut_point.cs:276 `_search` | หน้าจอกลาง — ขึ้นได้ใน 6 เมนู |
| กรุณาป้อนเลขที่เอกสาร และลูกค้า |  | 15 | SMLInventoryControl/_icTransControl.cs:17762 `_printDataWork`<br>SMLInventoryControl/_icTransControl.cs:17774 `_printDataWork` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารนี้มีการยกเลิกไปแล้ว ไม่สามารถนำมายกเลิกได้ |  | 14 | SMLInventoryControl/_icTransScreenTopControl.cs:5185<br>SMLInventoryControl/_icTransScreenTopControl.cs:5282 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารนี้มีปิดรายการไปแล้ว ไม่สามารถนำมายกเลิกได้ |  | 11 | SMLInventoryControl/_icTransScreenTopControl.cs:5190<br>SMLInventoryControl/_icTransScreenTopControl.cs:5287 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| {…} : สินค้านี้มีหน่วยนับเดียว |  | 10 | SMLERPControl/_ic/_icPriceFormulaDetail.cs:265 `_selectUnitCode`<br>SMLERPIC/_icPromotion/_gridItemClass.cs:125 `_selectUnitCode` | ส่วนกลาง `_gridItemClass`, `_gridPriceAndDiscountClass`, `_icPriceDetail` — ใช้ร่วมหลายหน้าจอ |
| เอกสารนี้มีการอ้างอิงรายการไปแล้ว ไม่สามารถนำมายกเลิกได้ |  | 6 | SMLInventoryControl/_icTransScreenTopControl.cs:5292<br>SMLInventoryControl/_icTransScreenTopControl.cs:5327 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเอกสารเลขที่ : {…} |  | 6 | SMLInventoryControl/_icTransControl.cs:6684 `_shipmentControl__afterSelectAddress`<br>SMLInventoryControl/_icTransControl.cs:6713 `_shipmentControl__afterSelectAddress` | ส่วนกลาง `_cancelBillForm`, `_icTransControl`, `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูล : {…} |  | 5 | SMLInventoryControl/_icTransScreenMoreControl.cs:463<br>SMLInventoryControl/_icTransScreenTopControl.cs:5809 | ส่วนกลาง `_icTransScreenMoreControl`, `_icTransScreenTopControl`, `_shipmentControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบสินค้าในเอกสารอ้างอิง |  | 5 | SMLInventoryControl/_icTransItemGridControl.cs:13963<br>SMLInventoryControl/_icTransItemGridControl.cs:14006 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนเลขที่เอกสาร |  | 4 | SMLInventoryControl/_icTransControl.cs:17941 `_printDataWork`<br>SMLInventoryControl/_icTransControl.cs:17952 `_printDataWork` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ตัวเลขผิดพลาด |  | 4 | SMLInventoryControl/_icTransItemGridControl.cs:6758 `_icTransItemGridChangeCost__submit`<br>SMLInventoryControl/_icTransItemGridControl.cs:6788 `_icTransItemGridChangeAmount__submit` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเลขที่เช็ค |  | 4 | SMLInventoryControl/_icTransItemGridControl.cs:14386 `findChequeDetail`<br>SMLInventoryControl/_icTransItemGridControl.cs:14507 `_ictransItemGridControl__alterCellUpdate` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน {…} | ผิดพลาด | 3 | SMLInventoryControl/_icTransControl.cs:13192 `_saveData`<br>SMLInventoryControl/_icTransControl.cs:13214 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกเอกสารก่อน |  | 3 | SMLInventoryControl/_icTransControl.cs:7719 `_importItemFromHandheld`<br>SMLInventoryControl/_icTransControl.cs:8379 `ProcessCmdKey` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเกินเอกสารอ้างอิง |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12976 `_checkReferenceQty`<br>SMLInventoryControl/_icTransItemGridControl.cs:13054 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| มีการอ้างอิงเอกสาร ไม่อนุญาติให้เปลี่ยน คลัง,ที่เก็บ |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:8447 `_checkEditWarehouseLocation`<br>SMLInventoryControl/_icTransItemGridControl.cs:8457 `_checkEditWarehouseLocation` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้ใส่รหัสเจ้าหนี้ |  | 3 | SMLAPARControl/_depositControl/_po_so_deposit_screen_top_control.cs:860 `_deleteSearchList`<br>SMLInventoryControl/_icTransControl.cs:6502 `_shipmentControl__afterSelectAddress` | ส่วนกลาง `_icTransControl`, `_po_so_deposit_screen_top_control` — ใช้ร่วมหลายหน้าจอ |
| ลูกค้า {…} : {…} ถูกปิดสถานะเครดิต | แจ้ง | 3 | SMLInventoryControl/_icTransControl.cs:11701 `_creditMoneyCheck`<br>SMLInventoryControl/_icTransControl.cs:11775 `_creditMoneyCheck` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า : {…},คลัง : {…} ห้ามติดลบ |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12320 `_checkBalance`<br>SMLInventoryControl/_icTransItemGridControl.cs:12428 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า : {…},คลัง : {…},ที่เก็บ : {…} ห้ามติดลบ |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12360 `_checkBalance`<br>SMLInventoryControl/_icTransItemGridControl.cs:12468 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า [{…}] ห้ามขายเกินยอดคงเหลือลบด้วยค้างส่ง |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12610<br>SMLInventoryControl/_icTransItemGridControl.cs:12649 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า [{…}] ห้ามติดลบ |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12282 `_checkBalance`<br>SMLInventoryControl/_icTransItemGridControl.cs:12390 `_checkBalance` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ส่งคืนเกินจำนวน |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:12884 `_checkReferenceQty`<br>SMLInventoryControl/_icTransItemGridControl.cs:12918 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสาร {…}ยังไม่ได้รับการอนุมัติ |  | 3 | SMLInventoryControl/_icTransControl.cs:3714 `_clearLogPrintButton_Click`<br>SMLInventoryControl/_icTransControl.cs:7645 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ{…} | แจ้ง | 3 | SMLERPControl/_bank/_bankControl.cs:1021<br>SMLInventoryControl/_icTransExtraControl.cs:222 `_search` | ส่วนกลาง `_bankControl`, `_icTransExtraControl`, `_icmainScreenControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัส {…} |  | 3 | SMLInventoryControl/_icTransItemGridControl.cs:15185<br>SMLInventoryControl/_icTransItemGridControl.cs:15340 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรูปแบบเลขที่เอกสาร กรุณาเลือก รูปแบบเลขที่เอกสาร |  | 3 | SMLInventoryControl/_stockAutoAdjustControl.cs:328 `_processButton_Click`<br>SMLInventoryControl/_stockAutoAdjustControl.cs:760 `_productNotFoundButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ |
| ไม่พบเอกสารอ้างอิง |  | 3 | SMLInventoryControl/_icTransControl.cs:450 `_vatTypeNumber`<br>SMLInventoryControl/_icTransControl.cs:502 `_vatTypeNumber` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาระบุวันหมดอายุ : {…} | เตือน | 2 | SMLInventoryControl/_icTransControl.cs:13954<br>SMLInventoryControl/_icTransControl.cs:13983 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการแก้ไขคลังและที่เก็บทั้งหมด หรือไม่ | แจ้ง | 2 | SMLInventoryControl/_icTransControl.cs:8545 `ProcessCmdKey`<br>SMLInventoryControl/_icTransControl.cs:8589 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ประมวลผลสำเร็จ |  | 2 | SMLInventoryControl/_stockAutoAdjustControl.cs:678 `_processNow`<br>SMLInventoryControl/_stockAutoAdjustLotControl.cs:512 | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ<br>สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ (สินค้า Lot) |
| พบการมัดจำเลขที่ {…}ในเอกสารที่เลือก |  | 2 | SMLInventoryControl/_icTransRefControl.cs:1167<br>SMLInventoryControl/_icTransRefControl.cs:1173 | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดวงเงินเครดิตของลุกค้า เกินที่กำหนดไว้ ต้องการขออนุมัติวงเงินเครดิตหรือไม่ | แจ้ง | 2 | SMLInventoryControl/_icTransControl.cs:12053 `_creditMoneySaleCheck`<br>SMLInventoryControl/_icTransControl.cs:12389 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสสินค้า {…} ยังไม่บันทึกหมายเลข LOT แบบกำหนดเอง | ผิดพลาด | 2 | SMLInventoryControl/_icTransControl.cs:13777<br>SMLInventoryControl/_icTransControl.cs:13784 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสสินค้า {…} ยังไม่บันทึกหมายเลข LOT แบบกำหนดเอง คุณต้องการที่จะบันทึกหรือไม่ | เตือน | 2 | SMLInventoryControl/_icTransControl.cs:13423 `_saveData`<br>SMLInventoryControl/_icTransControl.cs:13643 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสสินค้า {…} ยังไม่ได้กำหนดหมายเลข LOT แบบกำหนดเอง | เตือน | 2 | SMLInventoryControl/_icTransControl.cs:13417 `_saveData`<br>SMLInventoryControl/_icTransControl.cs:13636 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสอนุมัติวงเงินไม่ถูกต้อง | ผิดพลาด | 2 | SMLInventoryControl/_icTransControl.cs:917 `_getSaleOrderForApprove`<br>SMLInventoryControl/_icTransControl.cs:12034 `_creditMoneySaleCheck` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ราคาขายต่ำกว่าต้นทุน | เตือน | 2 | SMLInventoryControl/_icTransItemGridControl.cs:15643 `_checkPriceLowCost`<br>SMLInventoryControl/_icTransItemGridControl.cs:15654 `_checkPriceLowCost` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ลูกค้า {…} : {…} ยังไม่อนุมัติเปิดสถานะเครดิต | แจ้ง | 2 | SMLInventoryControl/_icTransControl.cs:12443<br>SMLInventoryControl/_icTransControl.cs:12449 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า [{…}] ห้ามขายเกินยอดคงเหลือลบด้วยค้างจอง |  | 2 | SMLInventoryControl/_icTransItemGridControl.cs:12727<br>SMLInventoryControl/_icTransItemGridControl.cs:12742 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้านี้ไม่สามารถแก้ไขราคาได้ |  | 2 | SMLInventoryControl/_icTransItemGridControl.cs:8719 `_changeProductPrice`<br>SMLInventoryControl/_icTransItemGridControl.cs:8774 `_changeProductAmount` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ส่งคืนเกินมูลค่า |  | 2 | SMLInventoryControl/_icTransItemGridControl.cs:12789 `_checkReferenceAmount`<br>SMLInventoryControl/_icTransItemGridControl.cs:12814 `_checkReferenceAmount` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่องมีอยู่ในระบบแล้ว : {…} |  | 2 | SMLInventoryControl/_icTransSerialNumberForm.cs:322 `_loadData`<br>SMLInventoryControl/_icTransSerialNumberForm.cs:527 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| ห้ามขายต่ำกว่าราคากลาง |  | 2 | SMLInventoryControl/_icTransItemGridControl.cs:15602 `_checkPriceLowStandPrice`<br>SMLPosClient/_posClientForm.cs:12175 | ส่วนกลาง `_icTransItemGridControl`, `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| เอกสารยกเลิกไม่สามารถอ้างอิงได้ |  | 2 | SMLInventoryControl/_icTransRefControl.cs:1024 `_getDocRefList`<br>SMLInventoryControl/_icTransRefControl.cs:1078 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารไม่สามารถอ้างอิงได้ |  | 2 | SMLInventoryControl/_icTransRefControl.cs:1034 `_getDocRefList`<br>SMLInventoryControl/_icTransRefControl.cs:1089 | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้พิมพ์ซ้ำ | เตือน | 2 | SMLInventoryControl/_icTransControl.cs:7624<br>SMLInventoryControl/_icTransControl.cs:17654 `_printFormData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| Auto Warehouse and location all (WareHouse : {…},Shelf : {…}) | แจ้ง | 1 | SMLInventoryControl/_icTransItemGridControl.cs:7711 `ProcessCmdKey` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| Cancel YES/NO | แจ้ง | 1 | SMLInventoryControl/_icTransSerialNumberDockForm.cs:98 `_saveButton_Click` | ส่วนกลาง `_icTransSerialNumberDockForm` — ใช้ร่วมหลายหน้าจอ |
| Cannot Load Pos Config |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:3086 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| Clear All | แจ้ง | 1 | SMLInventoryControl/_basket/_productOriginalStyleForm.cs:141 `toolStripButton2_Click` | ส่วนกลาง `_productOriginalStyleForm` — ใช้ร่วมหลายหน้าจอ |
| Eror Query : {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:15960 `_searchUnitNameWareHouseNameShelfNameAll` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| Error Query{…} |  | 1 | SMLInventoryControl/_stockAutoAdjustControl.cs:647 `_process` | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ |
| Move and Clear | แจ้ง | 1 | SMLInventoryControl/_basket/_productOriginalStyleForm.cs:150 `toolStripButton1_Click` | ส่วนกลาง `_productOriginalStyleForm` — ใช้ร่วมหลายหน้าจอ |
| Password fail. |  | 1 | SMLInventoryControl/_pricePasswordForm.cs:147 `ProcessCmdKey` | ส่วนกลาง `_pricePasswordForm` — ใช้ร่วมหลายหน้าจอ |
| Search Unit, Warehouse, Shelf Failed <br>{…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:15955 `_searchUnitNameWareHouseNameShelfNameAll` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| Send e-Tax Success. |  | 1 | SMLInventoryControl/_icTransControl.cs:18516 `LoadReqeustStockCountDoc` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| Trans Grid : Build Duplicate |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:968 `_build` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| TransControl : มีการสร้างจอสองครั้ง |  | 1 | SMLInventoryControl/_icTransControl.cs:4081 `_clearCopiedDocumentReferenceData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| TransScreenTop : มีการสร้างจอสองครั้ง |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:398 `ProcessCmdKey` | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| _saveData case not found : {…} |  | 1 | SMLInventoryControl/_icTransControl.cs:15243 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| _vatTypeNumber Error |  | 1 | SMLInventoryControl/_icTransControl.cs:310 `_vatTypeNumber` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| case not found : {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:17326 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| screentop Case not found : {…} |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:2377 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| {…} : ไม่มีสิทธิอนุมัติ |  | 1 | SMLInventoryControl/_pricePasswordForm.cs:133 `ProcessCmdKey` | ส่วนกลาง `_pricePasswordForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน <br>{…} | ผิดพลาด | 1 | SMLInventoryControl/_icTransImportDataControl.cs:190 `_importButton_Click` | ส่วนกลาง `_icTransImportDataControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน จำนวนวันหมดอายุ | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:13255 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน วันที่รับ/ส่งสินค้า | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:13205 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนวันที่ใบกำกับภาษี | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:13318 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนสาเหตุการออกใบกำกับภาษีฉบับใหม่ทดแทนฉบับเดิม | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:721 `_buttonCopy_Click` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนหมายเลข Order |  | 1 | SMLInventoryControl/_icTransControl.cs:8325 `ProcessCmdKey` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนเลขที่ใบกำกับภาษี | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:13311 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณายืนยันการออกใบกำกับภาษีฉบับใหม่แทนฉบับเดิม |  | 1 | SMLInventoryControl/_icTransControl.cs:830 `_buttonCopy_Click` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาระบุสินค้า | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:13277 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเฉลี่ยรายการ {…} [{…}] ให้ครบ | เตือน | 1 | SMLInventoryControl/_icTransControl.cs:14071 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือก{…} |  | 1 | SMLInventoryControl/_icTransControl.cs:13160 `_saveData` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกสินค้าก่อนทำรายการ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13301 `_aferCellUpdateItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกเขตขนส่ง | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:14340 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกเอกสาร |  | 1 | SMLInventoryControl/_icTransControl.cs:18166 `_sendETaxInetButton_Click` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| การตรวจสอบข้อมูลผู้ขายผิดพลาด |  | 1 | SMLInventoryControl/_icTransControl.cs:13028 `CheckCanPurchaseThisVendor` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| การตรวจสอบข้อมูลผู้ขายผิดพลาด : {…} |  | 1 | SMLInventoryControl/_icTransControl.cs:13023 `CheckCanPurchaseThisVendor` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| คลังและที่เก็บสินค้า Serial : {…} ไม่ตรงกับเอกสารต้นทาง |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:417 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| คำสั่งผิดพลาด {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:12253 `_checkBalance` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวน {…} ผิดพลาด |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13515 `_aferCellUpdateItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเกินรายการขอเบิก |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13177 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเกินรายการสั่งซื้อ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13146 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการทำการประมวลผล ปรับปรุงสต๊อคสินค้า/วัตถุดิบ หรือไม่ | ถาม | 1 | SMLInventoryControl/_stockAutoAdjustControl.cs:318 `_processButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ |
| ต้องการปรับปรุงมูลค่าคงเหลือ ของสินค้าหรือไม่ | ถาม | 1 | SMLInventoryControl/StockLotAdjustmentForm.cs:61 `_saveButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงมูลค่าสินค้า Lot คงค้าง |
| ต้องการล้างประวัติการพิมพ์ หรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:3609 `_clearLogPrintButton_Click` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเปลี่ยนราคาสินค้าเป็น {…} หรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransItemGridControl.cs:7481 `ProcessCmdKey` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกข้อมูลสำเร็จ หมายเลขขออนุมัติเอกสารของคุณคือ : {…} `save_success` | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:12324 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกรายการบัญชีสำเร็จและผ่านรายการไปสมุดบัญชีแยกประเภทเรียบร้อยแล้ว | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:17171 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกหมายเลขเครื่องซ้ำ |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:250 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| บันทึกหมายเลขเครื่องซ้ำกับรายการอื่นในเอกสาร |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:8381 `_serialNumberForm__checkSerialNumber` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| บาร์โค้ดลดราคา {…} {…} | ผิดพลาด | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13382 `_aferCellUpdateItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| บาร์โค๊ดซ้ำ |  | 1 | SMLInventoryControl/_icmainGridBarCodeControl.cs:195 `ProcessCmdKey` | ส่วนกลาง `_icmainGridBarCodeControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนข้อมูลคลังสินค้าไม่ครบ | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:14105 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนข้อมูลที่เก็บสินค้าไม่ครบ | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:14119 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ผู้ซื้อรายนี้ ไม่ได้รับอนุญาติ/ได้มีการทำการสั่งซื้อไว้เกินยอดขั้นต่ำ |  | 1 | SMLInventoryControl/_icTransControl.cs:13012 `CheckCanPurchaseThisVendor` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| มีการอ้างอิงเอกสารไปแล้ว ไม่สามารถดำเนินการยกเลิกได้ |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:5741 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| มีการเลือก {…}:{…} ไปแล้ว |  | 1 | SMLInventoryControl/_icTransWeightControl.cs:205 `_loadData` | ส่วนกลาง `_icTransWeightControl` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขรหัสลูกค้า อาจจะทำให้ราคาสินค้าผิดพลาด |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:4704 `_custCheckChange` | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขวันที่ อาจจะทำให้ราคาสินค้าผิดพลาด |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:2872 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขวันเครดิต อาจจะทำให้ราคาสินค้าผิดพลาด |  | 1 | SMLInventoryControl/_icTransScreenBottomControl.cs:122 `_icTransScreenBottomControl__textBoxSaved` | ส่วนกลาง `_icTransScreenBottomControl` — ใช้ร่วมหลายหน้าจอ |
| ยกเลิกการแก้ไข ? |  | 1 | SMLInventoryControl/_icUpdateForm.cs:73 `ProcessCmdKey` | ส่วนกลาง `_icUpdateForm` — ใช้ร่วมหลายหน้าจอ |
| ยอดมัดจำมากกว่ามูลค่าสุทธิ |  | 1 | SMLInventoryControl/_icTransControl.cs:6767 `_checAdvanceAmount` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดวงเงินเครดิตของลุกค้า เกินที่กำหนดไว้ | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:12345 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดวงเงินเครดิตของลุกค้า เกินที่กำหนดไว้ ต้องการดำเนินการต่อหรือไม่ | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:12374 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดเฉลี่ยไม่สมบูรณ์ |  | 1 | SMLInventoryControl/_icTransWeightControl.cs:244 `_saveButton_Click` | ส่วนกลาง `_icTransWeightControl` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่มีการอนุมัติรายการเอกสาร : {…} |  | 1 | SMLInventoryControl/_icTransControl.cs:11979 `_creditMoneySaleCheck` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัส : ' ไม่พบจำนวนสินค้า | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:14317 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสที่เลือกมีอยู่แล้ว `warning125` |  | 1 | SMLInventoryControl/_icmainGridControl.cs:389 `_searchShelfCode` | ส่วนกลาง `_icmainGridControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสผ่านหมดอายุ คุณต้องการส่งคำขออนุมัติใหม่ หรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:926 `_getSaleOrderForApprove` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| รายการนี้มีการอ้างอิงไปแล้ว ต้องการแก้ไขหรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:3277 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ลูกค้าถูกปิดสถานะชั่วคราว ต้องการบันทึกเพื่อขออนุมัติหรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:14258 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ลูกหนี้เกินกำหนดชำระ | เตือน | 1 | SMLInventoryControl/_icTransControl.cs:12746 `checkOverDueBeforeSave` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ล้างประวัติการพิมพ์ สำเร็จ |  | 1 | SMLInventoryControl/_icTransControl.cs:3616 `_clearLogPrintButton_Click` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| สร้างข้อมูลซื้อขาย AUTO | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:8879 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า : {…} สามารถรับคืนได้: {…} {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:11216 `_checkReduce` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า Serial : {…} ขายไปแล้ว |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:401 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| สินค้า Serial : {…} ไม่ตรงกับเอกสารต้นทาง |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:409 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| สินค้า {…} : {…} ห้ามขาย |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:5990 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า {…} หยุดซื้อ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:9579 `_gridFindItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า {…} เลิกขาย |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:9562 `_gridFindItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้านี้ไม่มีการบันทึกหมายเลขเครื่อง |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:7399 `_isSerial` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้านี้ไม่สามารถแก้ไขส่วนลดได้ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:8818 `_changeProductDiscount` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้าเคยตรวจนับไปแล้ว : เอกสารเลขที่ : {…} เอกสารวันที่ : {…} จำนวน : {…} {…} : {…}/{…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13414 `_aferCellUpdateItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ส่งคำขออนุมัติเปิดวงเงินสำเร็จ `save_success` | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:12412 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ส่งคำขออนุมัติใหม่สำเร็จ `save_success` | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:936 `_getSaleOrderForApprove` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่อง {…} มีอยู่ในระบบแล้ว ต้องการใช้หมายเลขเครื่องนี้ดำเนินการต่อหรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:518 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่องมีอยู่ในระบบแล้ว ต้องการใช้หมายเลขเครื่องนี้ดำเนินการต่อหรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:314 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่องไม่ตรงกับเอกสารการขาย : {…} |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:363 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่องไม่สัมพันธ์กับจำนวน : {…} |  | 1 | SMLInventoryControl/_icTransControl.cs:13924 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามขายเมื่อเกินกำหนดชำระ | เตือน | 1 | SMLInventoryControl/_icTransControl.cs:12741 `checkOverDueBeforeSave` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามรับคืนเกินยอดเบิกสินค้า |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:15446 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามเบิกเกินยอดฝากสินค้า |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:15448 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| เกินวงเงินเครดิต ไม่สามารถบันทึกเอกสารได้ | แจ้ง | 1 | SMLInventoryControl/_icTransControl.cs:11754 `_creditMoneyCheck` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เกินวงเงินเครดิตลูกค้า |  | 1 | SMLInventoryControl/_icTransControl.cs:14243 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เกินวงเงินเครดิตลูกค้า ต้องการบันทึกเพื่อขออนุมัติหรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:14250 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เลขที่ใบกำกับภาษีซ้ำ |  | 1 | SMLInventoryControl/_icTransScreenTopControl.cs:2594 | ส่วนกลาง `_icTransScreenTopControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสาร {…} มีการอ้างอิงเอกสาร ระบบจะคัดลอกเฉพาะข้อมูลหัวเอกสาร และล้างรายการสินค้า/ข้อมูลอ้างอิง เพื่อป้องกันการอ้างอิงจำนวนเกิน | เตือน | 1 | SMLInventoryControl/_icTransControl.cs:3886 `_checkApproveDocNo` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารยังไม่ผ่านการอนุมัติ<br>ไม่อนุญาติให้สั่งพิมพ์ค่ะ | เตือน | 1 | SMLInventoryControl/_icTransControl.cs:17716 `_checkPrintStatusSR` | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารสั่งซื้อไม่อนุมัติ |  | 1 | SMLInventoryControl/_icTransRefControl.cs:954 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารเสนอซื้อไม่อนุมัติ |  | 1 | SMLInventoryControl/_icTransRefControl.cs:964 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| ใบกำกับภาษีซื้อ เกิน 6 เดือน จะนำมาบันทึกบัญชีใช่หรือไม่ | ถาม | 1 | SMLInventoryControl/_icTransControl.cs:2341 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ใบเสนอซื้อไม่อนุมัตื |  | 1 | SMLInventoryControl/_icTransRefControl.cs:993 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| ใบเสนอราคาหมดอายุ |  | 1 | SMLInventoryControl/_icTransRefControl.cs:978 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ : รหัส หรือ รหัสคลังไม่สัมพันธ์กับที่เก็บสินค้า : {…} `warning124` | แจ้ง | 1 | SMLInventoryControl/_icmainGridControl.cs:377 `_searchShelfCode` | ส่วนกลาง `_icmainGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ Serial : {…} |  | 1 | SMLInventoryControl/_icTransSerialNumberForm.cs:435 `_loadData` | ส่วนกลาง `_icTransSerialNumberForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลเอกสาร {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:14473 `_ictransItemGridControl__alterCellUpdate` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบประเภทเอกสารปรับปรุงสินค้า |  | 1 | SMLInventoryControl/_stockAutoAdjustControl.cs:124 `_stockAutoAdjustControl` | สินค้า › ระบบตรวจนับสินค้า › ปรับปรุงสต็อกสินค้า/วัตถุดิบอัตโนมัติ |
| ไม่พบรหัสลูกค้า |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:13321 `_aferCellUpdateItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสสินค้า : {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:9865 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสสินค้า ทำการเพิ่มรายละเอียดสินค้าหรือไม่ : {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:9837 | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบราคารวมใน พบแต่ราคาแยกนอก คือ : {…} ต้องการใช้ราคานี้หรือไม่ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:10521 `_findPrice` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบราคาสินค้า |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:10504 `_findPrice` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบราคาแยกนอก พบแต่ราคารวมใน คือ : {…} ต้องการใช้ราคานี้หรือไม่ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:10513 `_findPrice` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการอ้างอิง |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:12891 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบสินค้า หรือ Query ผิดพลาด {…} |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:9367 `_gridFindItem` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบหมายเลขบรรทัดที่อ้างอิง |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:12845 `_checkReferenceQty` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเลขที่บัตรเครดิต |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:14681 `_ictransItemGridControl__alterCellUpdate` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติลูกค้าต่างสาขา |  | 1 | SMLInventoryControl/_icTransControl.cs:2639 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้บันทึกรายการล่วงหน้าได้ | ผิดพลาด | 1 | SMLInventoryControl/_icTransControl.cs:2335 | ส่วนกลาง `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้เปลี่ยนหน่วยนับ |  | 1 | SMLInventoryControl/_icTransItemGridControl.cs:8616 `_selectUnitCode` | ส่วนกลาง `_icTransItemGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้เลือกเอกสารเสนอราคา |  | 1 | SMLInventoryControl/_icTransRefControl.cs:751 `_getDocRefList` | ส่วนกลาง `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |

## MyLib

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ท่านไม่มีสิทธิในการเพิ่มข้อมูลใหม่ `warning19,warning44` | เตือน | 15 | MyLib/_myManageData.cs:419 `_newData`<br>MyLib/_myManageData.cs:473 `_newData` | หน้าจอกลาง — ขึ้นได้ใน 7 เมนู |
| บันทึกข้อมูลเสร็จเรียบร้อย โปรแกรมจะปิดหน้าจอนี้ให้ | แจ้ง | 14 | MyLib/_databaseManage/_databaseAccess.cs:440 `_buttonSave_Click`<br>MyLib/_databaseManage/_groupDatabase.cs:456 `_buttonSave_Click` | หน้าจอกลาง — ขึ้นได้ใน 6 เมนู |
| {…} : {…} |  | 13 | MyLib/_databaseManage/_selectDatabase..cs:1116 `_selectDatabase_Load`<br>MyLib/_databaseManage/_selectDatabase..cs:1129 `_selectDatabase_Load` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) |
| Error : {…} |  | 7 | MyLib/_databaseManage/_importExport/_import.cs:297 `_processButton_Click`<br>MyLib/_databaseManage/_providerConfig.cs:173 `_buttonLoginAdmin_Click` | หน้าจอกลาง — ขึ้นได้ใน 134 เมนู |
| Query ใช้ได้เฉพาะคำสั่ง select เท่านั้น<br>{…} `warning20` | ผิดพลาด | 4 | MyLib/_databaseManage/_queryDataView.cs:47 `_buttonProcess_Click`<br>SMLDataQuery/Form1.cs:62 `_processButton_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ใช้คำสั่ง Query<br>เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ตรวจสอบและปรับปรุงข้อมูล |
| กรุณาเลือกบริษัทที่ต้องการใช้งาน | ผิดพลาด | 4 | MyLib/_databaseManage/_selectDatabase..cs:1002 `_selectDatabase_Load`<br>MyLib/_databaseManage/_selectDatabase..cs:1006 `_selectDatabase_Load` | ส่วนกลาง `_selectDatabase.`, `_userLogin` — ใช้ร่วมหลายหน้าจอ |
| Device not found. |  | 3 | MPAYPOSOnline/_loginForm.cs:141 `_loginButton_Click`<br>MyLib/_databaseManage/_selectDatabase..cs:704 `_checkInput` | ส่วนกลาง `_loginForm`, `_selectDatabase.`, `_userLogin` — ใช้ร่วมหลายหน้าจอ |
| Login fail. |  | 3 | MyLib/_erpUserLoginForm.cs:56 `_loginButton_Click`<br>MyLib/_erpUserLoginForm.cs:61 `_loginButton_Click` | ส่วนกลาง `_erpUserLoginForm`, `_posLoginForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกกลุ่มที่ต้องการก่อน `warning15,warning34,warning40` | ผิดพลาด | 3 | MyLib/_databaseManage/_databaseAccess.cs:214 `_databaseAccess`<br>MyLib/_databaseManage/_groupDatabase.cs:148 `_groupDatabase` | ส่วนกลาง `_databaseAccess`, `_groupDatabase`, `_groupManage` — ใช้ร่วมหลายหน้าจอ |
| ระบบตรวจสอบข้อมูลไม่สมบูรณ์<br>อาจทำให้โปรแกรมมีปัญหา<br>กรุณาจบโปรแกรม และเรียกโปรแกรมใหม่ |  | 3 | MyLib/_global.cs:827 `_autoVerifyDatabase`<br>SMLBillFree/Program.cs:275 `_autoVerifyDatabase` | ส่วนกลาง `Program`, `_global` — ใช้ร่วมหลายหน้าจอ |
| ห้ามแก้ไข หรือลบข้อมูล `delete2,warning53` |  | 3 | MyLib/_myManageData.cs:561 `_unlockRecord`<br>MyLib/_myManageData.cs:619 `_unlockRecord` | ส่วนกลาง `_myManageData` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบประเภทเอกสาร `doc_type_not_found` |  | 3 | MyLib/_global.cs:2840 `_getAutoRun`<br>MyLib/_global.cs:2879 `_getAutoRun` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| Fail : [{…}] | ผิดพลาด | 2 | MyLib/_databaseManage/_serverSetup.cs:360 `buttonTest_Click`<br>MyLib/_databaseManage/_serverSetup.cs:371 `buttonTest_Click` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| Fail.<br>{…} | ผิดพลาด | 2 | MyLib/_databaseManage/_viewManage.cs:559 `ButtonTest_Click`<br>SMLERPGlobal/_viewManageCustom.cs:656 | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › กำหนดรูปแบบการค้นหาข้อมูล |
| Login Fail. |  | 2 | MyLib/_databaseManage/_providerConfig.cs:168 `_buttonLoginAdmin_Click`<br>MyLib/_registerForm.cs:84 `_buttonLoginAdmin_Click` | ส่วนกลาง `_providerConfig`, `_registerForm` — ใช้ร่วมหลายหน้าจอ |
| Login Success. |  | 2 | MyLib/_databaseManage/_providerConfig.cs:86 `_buttonLoginAdmin_Click`<br>MyLib/_registerForm.cs:78 `_buttonLoginAdmin_Click` | ส่วนกลาง `_providerConfig`, `_registerForm` — ใช้ร่วมหลายหน้าจอ |
| Query ใช้ได้เฉพาะคำสั่ง select เท่านั้น `warning20` | ผิดพลาด | 2 | MyLib/_databaseManage/_queryDataView.cs:30 `_buttonProcess_Click`<br>SMLDataQuery/Form1.cs:42 `_processButton_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ใช้คำสั่ง Query |
| Save Fail. |  | 2 | MyLib/_databaseManage/_providerConfig.cs:146 `_buttonLoginAdmin_Click`<br>MyLib/_databaseManage/_providerConfig.cs:205 `_saveButton_Click` | ส่วนกลาง `_providerConfig` — ใช้ร่วมหลายหน้าจอ |
| Send File Error : {…} : {…} |  | 2 | MyLib/_myFrameWork.cs:282 `_saveXmlFile`<br>MyLib/_myFrameWork.cs:300 `_sendXmlFile` | บัญชี › ผังบัญชี › ปรับปรุงผังบัญชีแบบเร็ว |
| [{…}]<br>{…} | เตือน | 2 | MyLib/_databaseManage/_serverSetup.cs:271 `buttonTest_Click`<br>MyLib/_databaseManage/_serverSetup.cs:318 `buttonTest_Click` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกรายการที่ต้องการลบ `warning38,warning42` | เตือน | 2 | MyLib/_databaseManage/_groupDatabase.cs:430 `_buttonGroup_Click`<br>MyLib/_databaseManage/_userAndGroup.cs:474 `_buttonDelete_Click` | ส่วนกลาง `_groupDatabase`, `_userAndGroup` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขรายการ<br>ต้องการทำรายการต่อไปหรือไม่ `warning22,warning33` | เตือน | 2 | MyLib/_databaseManage/_resourceEdit.cs:50 `_buttonLoad_Click`<br>MyLib/_databaseManage/_viewManage.cs:279 `_viewManage` | ส่วนกลาง `_resourceEdit`, `_viewManage` — ใช้ร่วมหลายหน้าจอ |
| มีข้อผิดพลาดในการตรวจสอบระบบ<br>{…} | ผิดพลาด | 2 | MyLib/_databaseManage/_viewManage.cs:586 `_resetButton_Click`<br>SMLERPTemplate/_templateMainForm.cs:2891 `_templateMainForm_Load` | ส่วนกลาง `_templateMainForm`, `_viewManage` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่บันทึก : Webservice Name กรุณากลับไปบันทึกก่อน `warning56` | ผิดพลาด | 2 | MyLib/_databaseManage/_selectDatabase..cs:601 `_checkInput`<br>MyLib/_databaseManage/_userLogin.cs:199 `_checkInput` | ส่วนกลาง `_selectDatabase.`, `_userLogin` — ใช้ร่วมหลายหน้าจอ |
| รายละเอียดไม่ครบ กรุณาตรวจสอบใหม่ `warning29,warning36` | ผิดพลาด | 2 | MyLib/_databaseManage/_groupDatabase.cs:282 `_detailUpdateButton_Click`<br>MyLib/_databaseManage/_userAndGroup.cs:235 `button1_Click` | ส่วนกลาง `_groupDatabase`, `_userAndGroup` — ใช้ร่วมหลายหน้าจอ |
| หน้าจอนี้ไม่อนุญาติให้แก้ไขข้อมูล `warning54` |  | 2 | MyLib/_myManageData.cs:666 `_unlockRecord`<br>MyLib/_myManageData.cs:731 `_unlockRecord` | ส่วนกลาง `_myManageData` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลในระบบ ต้องการดึงข้อมูลจาก Server www.smlsoft.com มาเป็นข้อมูลเบื้องต้นหรือไม่ |  | 2 | MyLib/_manageMasterCodeFull.cs:211 `_finish`<br>SMLERPGlobal/_docFormat.cs:32 `_docFormat` | หน้าจอกลาง — ขึ้นได้ใน 75 เมนู |
| 0 |  | 1 | MyLib/_global.cs:822 `_autoVerifyDatabase` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| Add column Duplicate : {…} |  | 1 | MyLib/_myGrid.cs:2775 `_addColumn` | ส่วนกลาง `_myGrid` — ใช้ร่วมหลายหน้าจอ |
| Auto verify | ถาม | 1 | MyLib/_global.cs:845 `_checkFirst` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| CONFIRM_CLOSE | ถาม | 1 | MyLib/_dialogConfigForm.cs:25 `_dialogConfigForm_FormClosing` | ส่วนกลาง `_dialogConfigForm` — ใช้ร่วมหลายหน้าจอ |
| Can't use same database name. : {…} |  | 1 | MyLib/_databaseManage/_transferDatabase.cs:1063 `_startButton_Click` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| Close windows |  | 1 | MyLib/_databaseManage/_providerConfig.cs:53 `OnClosing` | ส่วนกลาง `_providerConfig` — ใช้ร่วมหลายหน้าจอ |
| Connect Fail : {…} |  | 1 | MyLib/_databaseManage/_importExport/_import.cs:148 `_connectButton_Click` | ส่วนกลาง `_import` — ใช้ร่วมหลายหน้าจอ |
| Connect Success |  | 1 | MyLib/_databaseManage/_importExport/_import.cs:142 `_connectButton_Click` | ส่วนกลาง `_import` — ใช้ร่วมหลายหน้าจอ |
| Demo Only |  | 1 | MyLib/_global.cs:3619 `_demoVersion` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| Format error : {…} |  | 1 | MyLib/_myGrid.cs:2322 `_cellUpdate` | ส่วนกลาง `_myGrid` — ใช้ร่วมหลายหน้าจอ |
| Input Database Name |  | 1 | MyLib/_databaseManage/_transferDatabase.cs:1090 `_startButton_Click` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| Insert fail : {…} |  | 1 | MyLib/_databaseManage/_importExport/_import.cs:216 `_closeButton_Click` | ส่วนกลาง `_import` — ใช้ร่วมหลายหน้าจอ |
| Load fail. : {…} |  | 1 | MyLib/_myScreen.cs:791 `_loadData` | ส่วนกลาง `_myScreen` — ใช้ร่วมหลายหน้าจอ |
| Lock เด็ดขาด : ห้ามแก้ไข หรือลบข้อมูล `delete3` |  | 1 | MyLib/_myManageData.cs:570 `_unlockRecord` | ส่วนกลาง `_myManageData` — ใช้ร่วมหลายหน้าจอ |
| Reset All Resource | แจ้ง | 1 | MyLib/_databaseManage/_serverSetup.cs:330 `buttonTest_Click` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| Reset Language Success. Please Restart Program. |  | 1 | MyLib/_databaseManage/_verifyDatabase.cs:484 `_resetLanguageButton_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ตรวจสอบโครงสร้างฐานข้อมูล |
| Reset Success and will close this screen. |  | 1 | MyLib/_databaseManage/_viewManage.cs:590 `_resetButton_Click` | ส่วนกลาง `_viewManage` — ใช้ร่วมหลายหน้าจอ |
| Reset superadmin password | แจ้ง | 1 | MyLib/_databaseManage/_serverSetup.cs:377 `buttonTest_Click` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| Reset to Default ? | แจ้ง | 1 | MyLib/_databaseManage/_viewManage.cs:575 `_resetButton_Click` | ส่วนกลาง `_viewManage` — ใช้ร่วมหลายหน้าจอ |
| Resource load fail. |  | 1 | MyLib/_myFrameWork.cs:1903 `_resourceLoadAll` | บัญชี › ผังบัญชี › ปรับปรุงผังบัญชีแบบเร็ว |
| Save Success. |  | 1 | MyLib/_databaseManage/_providerConfig.cs:199 `_saveButton_Click` | ส่วนกลาง `_providerConfig` — ใช้ร่วมหลายหน้าจอ |
| Selecte : {…} |  | 1 | MyLib/_databaseManage/_providerConfig.cs:213 `_saveButton_Click` | ส่วนกลาง `_providerConfig` — ใช้ร่วมหลายหน้าจอ |
| Source Field Duplicate : {…}.{…} |  | 1 | MyLib/_databaseManage/_transferDatabase.cs:1253 `_scriptTargetFieldNameDuplicate` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| Success Total : {…} |  | 1 | MyLib/_databaseManage/_importExport/_import.cs:293 `_processButton_Click` | ส่วนกลาง `_import` — ใช้ร่วมหลายหน้าจอ |
| Target Field Duplicate : {…}.{…} |  | 1 | MyLib/_databaseManage/_transferDatabase.cs:1270 `_scriptTargetFieldNameDuplicate` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| Truncate all table success. |  | 1 | MyLib/_databaseManage/_transferDatabase.cs:1055 `_truncateAllTable` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| Webservice can't connect : [{…}] | ผิดพลาด | 1 | MyLib/_databaseManage/_serverSetup.cs:398 `buttonTest_Click` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| {…} : Again. Truncate All Table ? | ถาม | 1 | MyLib/_databaseManage/_transferDatabase.cs:1329 `_truncateAllTableButton_Click` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| {…} : Truncate All Table ? | ถาม | 1 | MyLib/_databaseManage/_transferDatabase.cs:1326 `_truncateAllTableButton_Click` | ส่วนกลาง `_transferDatabase` — ใช้ร่วมหลายหน้าจอ |
| กรุณากรอกรายละเอียดให้ครบถ้วนก่อน `select_data_group_3` | ผิดพลาด | 1 | MyLib/_databaseManage/_createDatabase.cs:382 `_createButton_Click` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| กรุณากำหนด Webservice Server ก่อน (กำหนด Tab แรก) `warning100` |  | 1 | MyLib/_databaseManage/_selectDatabase..cs:1191 `buttonLoginAdmin_Click_1` | ส่วนกลาง `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| กรุณาดำเนินการลงทะเบียนการใช้งาน Server |  | 1 | MyLib/_serverRegister/_smlServerRegister.cs:66 `GetRegisterFromSMLCloud` | ส่วนกลาง `_smlServerRegister` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกข้อมูล | เตือน | 1 | MyLib/_myDataList/_myDataList.cs:1788 `_printRangeButton_Click` | ส่วนกลาง `_myDataList` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกรายการที่ต้องการลบก่อน `warning86` | เตือน | 1 | MyLib/_myDataList/_myDataList.cs:1642 `_deleteDataBegin` | ส่วนกลาง `_myDataList` — ใช้ร่วมหลายหน้าจอ |
| การลงทะเบียนสมบูรณ์ |  | 1 | MyLib/_registerForm.cs:54 `button1_Click` | ส่วนกลาง `_registerForm` — ใช้ร่วมหลายหน้าจอ |
| กำหนดรหัสผ่านใหม่สำเร็จ `warning11` | แจ้ง | 1 | MyLib/_databaseManage/_serverChangePassword.cs:28 `_buttonOK_Click` | ส่วนกลาง `_serverChangePassword` — ใช้ร่วมหลายหน้าจอ |
| ฐานข้อมูลปัจจุบันมีข้อมูลอยู่แล้ว |  | 1 | MyLib/_databaseManage/_dataRestoreForm.cs:75 `_buttonStart_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › นำข้อมูลสำรองกลับมาใช้ |
| ตรวจพบการเปลี่ยนแปลงโครงสร้างข้อมูล กรุณาทำการตรวจสอบโครงสร้างฐานข้อมูลใหม่ | เตือน | 1 | MyLib/_global.cs:1001 `_checkFirst` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| ตรวจพบการเปลี่ยนแปลงโครงสร้างข้อมูล ต้องการดำเนินการปรับปรุงหรือไม่ | ถาม | 1 | MyLib/_global.cs:893 `_checkFirst` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเลือกหรือไม่ `warning91` | แจ้ง | 1 | MyLib/_myDataList/_myDataList.cs:1687 `_buttonSelectAll_Click` | ส่วนกลาง `_myDataList` — ใช้ร่วมหลายหน้าจอ |
| ต้องบันทึกรหัส{…} `input_first` | เตือน | 1 | MyLib/_databaseManage/_menupermissions_user.cs:491 `__gridInit_user` | ส่วนกลาง `_menupermissions_user` — ใช้ร่วมหลายหน้าจอ |
| ทำงานไม่สำเร็จ<br>{…} `warning101` | ผิดพลาด | 1 | MyLib/_databaseManage/_viewManage.cs:481 `ButtonLoadTemplate_Click` | ส่วนกลาง `_viewManage` — ใช้ร่วมหลายหน้าจอ |
| ท่านกำลังทำการเพิ่มหรือแก้ไขข้อมูลไม่อนุญาติให้ลบ `warning85` | เตือน | 1 | MyLib/_myDataList/_myDataList.cs:1614 `_deleteDataBegin` | ส่วนกลาง `_myDataList` — ใช้ร่วมหลายหน้าจอ |
| ท่านยังไม่ได้ทำการ Login ไม่สามารถทำรายการได้ `warning98` | ผิดพลาด | 1 | MyLib/_databaseManage/_selectDatabase..cs:1050 `_selectDatabase_Load` | ส่วนกลาง `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| ท่านเลือกวันที่ : {…} `warning24` | แจ้ง | 1 | MyLib/_setDate.cs:16 `_setDate` | ส่วนกลาง `_setDate` — ใช้ร่วมหลายหน้าจอ |
| ท่านไม่ใช่กลุ่ม Admin ไม่อนุญาติให้ Login ในหน้าจอ Admin `warning92` | ผิดพลาด | 1 | MyLib/_databaseManage/_selectDatabase..cs:664 `_checkInput` | ส่วนกลาง `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| ท่านไม่ใช่กลุ่ม Admin ไม่อนุญาติให้ กระทำการได ๆ ๆ ในหน้าจอ Admin `warning99` | ผิดพลาด | 1 | MyLib/_databaseManage/_selectDatabase..cs:1157 `_selectDatabase_Load` | ส่วนกลาง `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| บันทึกการตั้งค่าสำเร็ต โปรแกรมจะปิดหน้าจอนี้ให้ | แจ้ง | 1 | MyLib/_preferenceForm.cs:71 `_saveButton_Click` | ส่วนกลาง `_preferenceForm` — ใช้ร่วมหลายหน้าจอ |
| ป้อนวันที่ผิดพลาด `format_date_error` | ผิดพลาด | 1 | MyLib/_myRoutine.cs:671 `_checkDate` | ส่วนกลาง `_myRoutine` — ใช้ร่วมหลายหน้าจอ |
| มีชื่อข้อมูลอยู่แล้วไม่สามารถสร้างใหม่ได้ [{…}] `create_database_3` | ผิดพลาด | 1 | MyLib/_databaseManage/_createDatabase.cs:395 `_createButton_Click` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| มีรหัสข้อมูลอยู่แล้วไม่สามารถสร้างใหม่ได้ [{…}] `create_database_6` | ผิดพลาด | 1 | MyLib/_databaseManage/_createDatabase.cs:390 `_createButton_Click` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้เลือกกลุ่มข้อมูล `select_data_group_1` | ผิดพลาด | 1 | MyLib/_databaseManage/_createDatabase.cs:361 `_createButton_Click` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้เลือกข้อมูลที่ต้องการ Shrink กรุณาเลือกก่อน `warning25` | ผิดพลาด | 1 | MyLib/_databaseManage/_shrinkDatabase.cs:70 `_buttonStart_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ลดขนาดข้อมูล |
| ยังไม่ได้เลือกข้อมูลที่ต้องการ Verify กรุณาเลือกก่อน `warning30` | ผิดพลาด | 1 | MyLib/_databaseManage/_verifyDatabase.cs:385 `_buttonStart_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ตรวจสอบโครงสร้างฐานข้อมูล |
| ยังไม่ได้เลือกผู้มีสิทธิ์ใช้งาน `select_data_group_2` | ผิดพลาด | 1 | MyLib/_databaseManage/_createDatabase.cs:375 `_createButton_Click` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการนำข้อมูลที่สำรองไว้ กลับมาใช้งาน | แจ้ง | 1 | MyLib/_databaseManage/_dataRestoreForm.cs:57 `_buttonStart_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › นำข้อมูลสำรองกลับมาใช้ |
| รหัสไม่ผ่าน `warning14` | แจ้ง | 1 | MyLib/_databaseManage/_serverChangePassword.cs:43 `_buttonOK_Click` | ส่วนกลาง `_serverChangePassword` — ใช้ร่วมหลายหน้าจอ |
| รายการนี้มีผู้ใช้อยู่ `warning52` | ผิดพลาด | 1 | MyLib/_myManageData.cs:585 `_unlockRecord` | ส่วนกลาง `_myManageData` — ใช้ร่วมหลายหน้าจอ |
| หน้าจอนี้ไม่อนุญาติให้ลบข้อมูล `delete1` |  | 1 | MyLib/_myDataList/_myDataList.cs:1672 `_buttonDelete_Click` | ส่วนกลาง `_myDataList` — ใช้ร่วมหลายหน้าจอ |
| เนื่องจากท่านเป็นผู้ใช้คนแรก ระบบจะเพิ่มชื่อ และรหัสผ่านให้โดยอัตโนมัติ<br>โดยท่านจะมีสิทธิ์ในการทำงานสูงสุด กรุณาจดรหัสผู้ใช้ และรหัสผ่านไว้ด้วย<br><br>รหัสผู้ใช้คือ : {0}<br>รหัสผ่านคือ : {1}superadminsuperadmin `warning51` | แจ้ง | 1 | MyLib/_databaseManage/_serverSetup.cs:415 `_insertFirstUser` | ส่วนกลาง `_serverSetup` — ใช้ร่วมหลายหน้าจอ |
| เปลี่ยนรหัสผ่านใหม่สำเร็จ `warning8` | แจ้ง | 1 | MyLib/_databaseManage/_smlChangePassword.cs:28 `_buttonOK_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › เปลี่ยนรหัสผ่าน |
| เปลี่ยนรหัสผ่านใหม่ไม่สำเร็จ `warning9` | แจ้ง | 1 | MyLib/_databaseManage/_smlChangePassword.cs:33 `_buttonOK_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › เปลี่ยนรหัสผ่าน |
| เพิ่มรายละเอียดที่เกี่ยวข้องเรียบร้อยแล้ว `create_database_1` | แจ้ง | 1 | MyLib/_databaseManage/_createDatabase.cs:455 `AfterCreateDatabaseSuccess` | ส่วนกลาง `_createDatabase` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ user และ password ดังกล่าว | ผิดพลาด | 1 | MyLib/_databaseManage/_emergencyForm.cs:64 `ProcessCmdKey` | ส่วนกลาง `_emergencyForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบกลุ่มข้อมูลที่ต้องการ กรุณาเลือกกลุ่มใหม่<br>โปรแกรมไม่สามารถแสดงกลุ่มได้ ด้วยเหตุผลด้านความปลอดภัย<br>โปรแกรมจะไม่ทำงานในขั้นตอนต่อไปจนกว่าจะระบุกลุ่มข้อมูลถูกต้อง `warning89` | ผิดพลาด | 1 | MyLib/_databaseManage/_selectDatabase..cs:641 `_checkInput` | ส่วนกลาง `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบกลุ่มข้อมูลที่ต้องการ กรุณาเลือกใหม่ `warning17` | ผิดพลาด | 1 | MyLib/_databaseManage/Link Database/_linkDatabase.cs:175 `_linkDatabase_Load` | ส่วนกลาง `_linkDatabase` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบกลุ่มผู้ใช้ กรุณากลับไปทำการสร้างกลุ่มผู้ใช้ก่อน `warning16` | ผิดพลาด | 1 | MyLib/_databaseManage/_groupManage.cs:48 `_groupManage` | ส่วนกลาง `_groupManage` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบฐานข้อมูล กรุณากลับไปทำการสร้างก่อน `warning10` | ผิดพลาด | 1 | MyLib/_databaseManage/_databaseAccess.cs:47 `_databaseAccess` | ส่วนกลาง `_databaseAccess` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบฐานข้อมูลที่ต้องการ กรุณาเลือกใหม่ `warning18` | ผิดพลาด | 1 | MyLib/_databaseManage/Link Database/_linkDatabase.cs:193 `_linkDatabase_Load` | ส่วนกลาง `_linkDatabase` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถกำหนดรหัสใหม่ได้ `warning13` | แจ้ง | 1 | MyLib/_databaseManage/_serverChangePassword.cs:38 `_buttonOK_Click` | ส่วนกลาง `_serverChangePassword` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถกำหนดรหัสใหม่ได้ Server ไม่ยอมรับ `warning12` | แจ้ง | 1 | MyLib/_databaseManage/_serverChangePassword.cs:33 `_buttonOK_Click` | ส่วนกลาง `_serverChangePassword` — ใช้ร่วมหลายหน้าจอ |

## SMLPosClient

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่พบรายการสินค้า |  | 11 | BCTOSML/Form1.cs:513 `_importSMLICtoolStrip_Click`<br>BCTOSML/Form1.cs:1005 `_selectTableButton_Click` | ส่วนกลาง `Form1`, `_posClientForm`, `_posSaleControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกสำเร็จ |  | 6 | IMEXControl/QualityControl/ICQCProductReceive.cs:137 `_saveData`<br>SMLERPConfig/_dashboardConfigScreen.cs:363 `_saveEditPassword_Click` | สินค้า › ตรวจสอบคุณภาพสินค้า › บันทึกรับสินค้า<br>สินค้า › จัดการ LOT สินค้า<br>MIS › หน้าจอสำหรับผู้บริหาร |
| รหัสผ่านไม่ถูกต้อง |  | 6 | SMLFastReport/_importFastReport.cs:178 `_buttonProcess_Click`<br>SMLPosClient/_summaryDayUserControl.cs:86 `_processSaleDaily` | เริ่มต้น › เครื่องมือ › นำเข้ารายงาน<br>เริ่มต้น › เครื่องมือ › นำเข้ารายงานสาขา |
| ไม่พบ username และ password ดังกล่าว |  | 6 | SMLPosClient/_posClientForm.cs:9280 `_allowShowTotalBalance`<br>SMLPosClient/_posClientForm.cs:9349 `_allowCancelBill` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| รหัสผู้ใช้หรือรหัสผ่านไม่ถูกต้อง |  | 4 | SMLPosClient/screen/_cancelBillForm.cs:217 `_buttonProcess_Click`<br>SMLPosClient/screen/_posPrintSlipPeriod.cs:72 `_buttonProcess_Click` | ส่วนกลาง `_cancelBillForm`, `_posPrintSlipPeriod`, `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| เอกสาร [{…}] ยกเลิกไปแล้ว |  | 4 | SMLPosClient/screen/_cancelBillForm.cs:86 `_buttonProcess_Click`<br>SMLPosClient/screen/_printVatFull.cs:166 `ProcessCmdKey` | ส่วนกลาง `_cancelBillForm`, `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเอกสาร [{…}] |  | 4 | SMLPosClient/screen/_printVatFull.cs:197 `ProcessCmdKey`<br>SMLPosClient/screen/_printVatFull.cs:204 `ProcessCmdKey` | ส่วนกลาง `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| Please select a credit card type |  | 3 | SMLERPControl/_payment/_edcPaymentForm.cs:119 `_payPromptPayButton_Click`<br>SMLPosClient/screen/_posPayForm.cs:2448 `_buttonKTBQRCode_Click` | ส่วนกลาง `_edcPaymentForm`, `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้ทำการเปิดกะ กรุณาเปิดกะ ก่อนทำรายการ | ผิดพลาด | 3 | SMLPosClient/_posClientForm.cs:7669<br>SMLPosClient/_posClientForm.cs:7675 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| รหัสหรือรหัสผ่านผู้จัดการไม่ถูกต้อง |  | 3 | SMLPosClient/_summaryDayUserControl.cs:81 `_processSaleDaily`<br>SMLPosClient/screen/_moneyReceive.cs:101 `_saveButton_Click` | ส่วนกลาง `_moneyReceive`, `_posPrintSlipPeriod`, `_summaryDayUserControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการพิมพ์เอกสาร [{…}] จริงหรือไม่ | แจ้ง | 2 | SMLPosClient/screen/_printVatFull.cs:572 `_buttonProcess_Click`<br>SMLPosClient/screen/_reprintBillForm.cs:64 `_buttonProcess_Click` | ส่วนกลาง `_printVatFull`, `_reprintBillForm` — ใช้ร่วมหลายหน้าจอ |
| มีการขายไปแล้ว ไม่สามารถเลือกสมาชิกได้ |  | 2 | SMLPosClient/_posClientForm.cs:9139<br>SMLPosClient/_posClientForm.cs:9232 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| มีการใช้สิทธิ์ ดังกล่าวไปแล้ว บิลเลขที่ : {…} เมื่อวันที่ : {…} |  | 2 | SMLPosClient/_posClientForm.cs:13160<br>SMLPosClient/_posClientForm.cs:13194 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่มีการเปิดกะ |  | 2 | SMLPosClient/screen/_periodCloseForm.cs:66 `_periodCloseForm`<br>SMLPosClient/screen/_periodCloseForm.cs:244 `_periodCloseForm` | ส่วนกลาง `_periodCloseForm` — ใช้ร่วมหลายหน้าจอ |
| เอกสาร [{…}] อ้างอิงไปแล้ว |  | 2 | SMLPosClient/screen/_printVatFull.cs:176 `ProcessCmdKey`<br>SMLPosClient/screen/_printVatFull.cs:226 `ProcessCmdKey` | ส่วนกลาง `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเลขที่เอกสาร | ผิดพลาด | 2 | SMLPosClient/_posClientForm.cs:7828<br>SMLPosClient/_posClientForm.cs:7970 `__pay__genQrCode` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| Cancel ? | แจ้ง | 1 | SMLPosClient/screen/_posPayForm.cs:1346 `OnShown` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| Connected. |  | 1 | SMLPosClient/_configCustomerDisplayControl.cs:152 `_testConnect_Click` | ส่วนกลาง `_configCustomerDisplayControl` — ใช้ร่วมหลายหน้าจอ |
| Error :{…}///{…} |  | 1 | SMLPosClient/screen/_posPayForm.cs:2439 `_buttonKTBQRCode_Click` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| Error Promotion : {…}<br>{…} |  | 1 | SMLPosClient/_posClientForm.cs:10021 `_addItemToGrid` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| POS Design Object Not Set !!! | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:7088 `_setXMLDesign` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| Test Print Doc {…} | เตือน | 1 | SMLPosClient/_posClientForm.cs:13064 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| {…} มีปฏิกริยากับ {…} คุณต้องการดำเนินการต่อหรือไม่ |  | 1 | SMLPosClient/_posClientForm.cs:14669 `_checkDrugInteractive` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณา Login เข้าสู่ระบบก่อน ถึงจะสามารถทำรายการต่อไปได้ | ผิดพลาด | 1 | SMLPosClient/_posLoginConfigScreen.cs:45 `_posLoginConfigScreen` | ส่วนกลาง `_posLoginConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| กรุณากำหนดเครื่องพิมพ์ฉลากยา | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:5227 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาตรวจสอบจำนวนเงิน! |  | 1 | SMLPosClient/screen/_posPayForm.cs:727 `_payOtherScreen__qrGenRespone` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาบันทึกรายละเอียดลูกค้า |  | 1 | SMLPosClient/screen/_printVatFull.cs:274 `_buttonProcess_Click` | ส่วนกลาง `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| กรุณาปิดลิ้นชักก่อนทำรายการ | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:11352 `_checkCashDrawerStatusOpen` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน เลขที่ใบกำกับภาษีเต็มรูปแบบ ก่อน | ผิดพลาด | 1 | SMLPosClient/screen/_printVatFull.cs:79 `_printVatFull` | ส่วนกลาง `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| การชำระเงินไม่สัมพันธ์กับยอดขาย |  | 1 | SMLPosClient/screen/_posPayForm.cs:922 `_payOtherCurrencyGrid__afterCalcTotal` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| คลังและที่เก็บไม่ตรงกับ หมายเลขเครื่อง : {…} |  | 1 | SMLPosClient/process/_posSearchProduct.cs:1192 `_findWithSerialNumber` | ส่วนกลาง `_posSearchProduct` — ใช้ร่วมหลายหน้าจอ |
| คุณต้องการบันทีกรายการเป็นขายเงินเชื่อ | ถาม | 1 | SMLPosClient/screen/_posPayForm.cs:1595 `_buttonCreditSave_Click` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเงินในลิ้นชักเกินกว่าที่กำหนดไว้ | เตือน | 1 | SMLPosClient/_posClientForm.cs:9685 `_checkMoneyLimit` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| จำนวนแต้มผิดพลาด |  | 1 | SMLPosClient/screen/_posPayForm.cs:917 `_payOtherCurrencyGrid__afterCalcTotal` | ส่วนกลาง `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการปิดหน้าจอ | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:14218 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการพักบิลและเริ่มหน้าจอขายใหม่ | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:13520 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการพิมพ์เอกสาร <br>ตั้งแต่เลขที่ [{…}] ถึงเลขที่ [{…}] <br>จริงหรือไม่ | แจ้ง | 1 | SMLPosClient/screen/_posPrintSlipPeriod.cs:54 `_buttonProcess_Click` | ส่วนกลาง `_posPrintSlipPeriod` — ใช้ร่วมหลายหน้าจอ |
| ต้องการยกเลิกรายการพักบิลทั้งหมด | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:13600 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการยกเลิกเอกสาร [{…}] จริงหรือไม่ | แจ้ง | 1 | SMLPosClient/screen/_cancelBillForm.cs:123 `_buttonProcess_Click` | ส่วนกลาง `_cancelBillForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการสั่งอาหารเพิ่มก่อนปิดโต๊ะหรือไม่ |  | 1 | SMLPosClient/_posClientForm.cs:12941 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ต้องการออกใบกำกับภาษีแบบเต็ม [{…}] จริงหรือไม่ | แจ้ง | 1 | SMLPosClient/screen/_printVatFull.cs:299 `_buttonProcess_Click` | ส่วนกลาง `_printVatFull` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเริ่มรายการใหม่ | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:13941 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| บันทึกการตั้งค่า เรียบร้อยแล้ว ระบบจะทำการปิดจอให้ |  | 1 | SMLPosClient/screen/_counSellingConfigForm.cs:137 `_buttonSave_Click` | ส่วนกลาง `_counSellingConfigForm` — ใช้ร่วมหลายหน้าจอ |
| ปิดกะสำเร็จ |  | 1 | SMLPosClient/screen/_periodCloseForm.cs:267 `_saveButton_Click` | ส่วนกลาง `_periodCloseForm` — ใช้ร่วมหลายหน้าจอ |
| ป้อนชื่อสินค้าผิดพลาด |  | 1 | SMLPosClient/_posClientForm.cs:12712 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ป้อนราคาผิดพลาด |  | 1 | SMLPosClient/_posClientForm.cs:12333 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ผิดพลาดการเชื่อมต่อ กรุณาลองใหม่ |  | 1 | SMLPosClient/_posClientForm.cs:13170 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| พบการตั้งค่า cashloop use ระบบจะ login creatus | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:751 `_doPosCloseCleanup` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| มีการเปิดกะค้างไว้แล้ว กรุณาปิดกะก่อน |  | 1 | SMLPosClient/screen/_periodOpenForm.cs:75 `_periodOpenForm` | ส่วนกลาง `_periodOpenForm` — ใช้ร่วมหลายหน้าจอ |
| ยกเลิกเอกสาร [{…}] สำเร็จ |  | 1 | SMLPosClient/screen/_cancelBillForm.cs:199 `_buttonProcess_Click` | ส่วนกลาง `_cancelBillForm` — ใช้ร่วมหลายหน้าจอ |
| ยอดการส่งเงิน ไม่สัมพันธ์ กับยอดขาย <br>กรุณาส่งเงิน ให้ตรงกับยอดขาย ก่อนจะทำการปิดกะ | ผิดพลาด | 1 | SMLPosClient/screen/_periodCloseForm.cs:225 `_periodCloseForm` | ส่วนกลาง `_periodCloseForm` — ใช้ร่วมหลายหน้าจอ |
| ยอดการส่งเงิน ไม่สัมพันธ์ กับยอดขาย <br>ต้องการทีจะดำเนินการต่อหรือไม่ | เตือน | 1 | SMLPosClient/screen/_periodCloseForm.cs:217 `_periodCloseForm` | ส่วนกลาง `_periodCloseForm` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่มียอดเงิน | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:7833 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้กำหนดค่าฉลากยา | ผิดพลาด | 1 | SMLPosClient/_selectMenu.cs:148 `_getObject` | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้รับเงินทอน กรุณารับเงินทอน ก่อนทำรายการ | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:7732 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ยิงหมายเลขเครื่องไปแล้ว : {…} |  | 1 | SMLPosClient/process/_posSearchProduct.cs:1211 `_findWithSerialNumber` | ส่วนกลาง `_posSearchProduct` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการพิมพ์ใบเสร็จรับเงิน | ถาม | 1 | SMLPosClient/_posClientForm.cs:8766 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการเปลี่ยนแปลงจำนวนสินค้า | ถาม | 1 | SMLPosClient/_posClientForm.cs:7261 `_getPOSObject` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| รหัสพนักงาน หรือ รหัสผ่านไม่ตรง |  | 1 | SMLPosClient/screen/_cnBillForm.cs:46 `_buttonProcess_Click` | ส่วนกลาง `_cnBillForm` — ใช้ร่วมหลายหน้าจอ |
| สมาชิกหมดอายุไปแล้ว ต้องการดำเนินการต่อไปหรือไม่ | แจ้ง | 1 | SMLPosClient/_posClientForm.cs:9047 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| สินค้าหน่วยนับเดียว |  | 1 | SMLPosClient/_posClientForm.cs:12575 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| หมายเลขเครื่อง : {…} ขายไปแล้ว |  | 1 | SMLPosClient/process/_posSearchProduct.cs:1183 `_findWithSerialNumber` | ส่วนกลาง `_posSearchProduct` — ใช้ร่วมหลายหน้าจอ |
| ห้ามทอนเงินมากกว่า {…} | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:7957 `__pay__genQrCode` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ห้ามยกเลิกใบเสร็จข้ามกะ |  | 1 | SMLPosClient/screen/_cancelBillForm.cs:111 `_buttonProcess_Click` | ส่วนกลาง `_cancelBillForm` — ใช้ร่วมหลายหน้าจอ |
| ห้ามยกเลิกใบเสร็จข้ามวัน |  | 1 | SMLPosClient/screen/_cancelBillForm.cs:119 `_buttonProcess_Click` | ส่วนกลาง `_cancelBillForm` — ใช้ร่วมหลายหน้าจอ |
| เปิดกะสำเร็จ |  | 1 | SMLPosClient/screen/_periodOpenForm.cs:128 `_saveButton_Click` | ส่วนกลาง `_periodOpenForm` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะนี้ทำการปิดโต๊ะไปแล้ว |  | 1 | SMLPosClient/_posClientForm.cs:12993 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะนี้ยังไม่มีการปิดโต๊ะ |  | 1 | SMLPosClient/_posClientForm.cs:12814 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลการเปิดกะ |  | 1 | SMLPosClient/_posClientForm.cs:9311 `_allowCancelBill` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลสมาชิก |  | 1 | SMLPosClient/_posClientForm.cs:13228 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสสาขาที่เครื่อง POS กรุณากำหนดสาขา เครื่อง POS | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:5854 `_newKey` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสเครื่อง POS | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:5764 `_newKey` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการขาย |  | 1 | SMLPosClient/_posClientForm.cs:9743 `_findSaleOrder` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการคิดเงิน กรุณาเลือกโต๊ะก่อน | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:1960 `_drawSummaryItemSaleDaily` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายละเอียดบริษัท |  | 1 | SMLPosClient/slip/_printSlip.cs:264 `_printSlipDraw` | ส่วนกลาง `_printSlip` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเลขที่เอกสารส่งเงิน |  | 1 | SMLPosClient/_summaryUserControl.cs:717 `_saveData` | ส่วนกลาง `_summaryUserControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเอกสาร ตั้งแต่เลขที่ {…} ถึงเอกสารเลขที่ {…} |  | 1 | SMLPosClient/screen/_posPrintSlipPeriod.cs:62 `_buttonProcess_Click` | ส่วนกลาง `_posPrintSlipPeriod` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีรายการขาย |  | 1 | SMLPosClient/_posClientForm.cs:13516 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีรายการพักบิล |  | 1 | SMLPosClient/_posClientForm.cs:13556 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถขายเครื่องดื่มแอลกอฮอล์ได้ในเวลานี้ |  | 1 | SMLPosClient/_posClientForm.cs:14307 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถยกเลิกใบเสร็จได้ |  | 1 | SMLPosClient/_posClientForm.cs:9343 `_allowCancelBill` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถรับคืนสินค้าได้ เนื่องจากเกินกำหนดรับคืนสินค้าไปแล้ว {…} วัน |  | 1 | SMLPosClient/screen/_cnBillForm.cs:115 `_buttonProcess_Click` | ส่วนกลาง `_cnBillForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถแก้ไขราคาสินค้าได้ |  | 1 | SMLPosClient/_posClientForm.cs:9387 `_allowChangePrice` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถแก้ไขส่วนลดได้ |  | 1 | SMLPosClient/_posClientForm.cs:9433 `_allowChangeDiscount` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถแสดงยอดขาย |  | 1 | SMLPosClient/_posClientForm.cs:9273 `_allowShowTotalBalance` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้เปิดลิ้นชัก | ผิดพลาด | 1 | SMLPosClient/_posClientForm.cs:9540 `_allowOpenCashDrawer` | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่อยู่ในช่วงเดือนเกิดของสมาชิก |  | 1 | SMLPosClient/_posClientForm.cs:13223 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่ได้รับอนุญาติใหัแก้ไขส่วนลด |  | 1 | SMLPosClient/_posClientForm.cs:12397 | ส่วนกลาง `_posClientForm` — ใช้ร่วมหลายหน้าจอ |

## SMLAPARControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ยังไม่มีการบันทึกเอกสาร | ผิดพลาด | 8 | SMLAPARControl/_ar_ap_trans.cs:658 `_printSelectRecordButton_Click`<br>SMLAPARControl/_ar_ap_trans.cs:717 `_withHoldingTax__getDueDateEventArgs` | บัญชี › บัญชีแยกประเภท › ข้อมูลรายวัน |
| ประเภทเอกสารไม่สัมพันธ์กับเลขที่เอกสาร ต้องการเปลี่ยนตามเลขที่เอกสารเลยหรือไม่ | แจ้ง | 6 | SMLAPARControl/_ar_cut_point.cs:216 `_closeButton_Click`<br>SMLAPARControl/_ar_point_balance.cs:215 `_closeButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| ยังไม่ได้ใส่รหัสลูกค้า |  | 6 | SMLAPARControl/_ar_ap_trans.cs:730 `_withHoldingTax__getDueDateEventArgs`<br>SMLAPARControl/_ar_ap_trans.cs:1114 `_convertToNumber` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| สถานะ ลูกค้าปิดการใช้งาน |  | 6 | SMLAPARControl/_ar_ap_trans.cs:2219 `_saveData`<br>SMLAPARControl/_ar_ap_trans_screen_top.cs:1480 | ส่วนกลาง `_ar_ap_trans`, `_ar_ap_trans_screen_top`, `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเอกสาร |  | 5 | SMLAPARControl/_ar_ap_trans.cs:1311 `_dataList__flowEvent`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:393 `_dataList__flowEvent` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_icTransRefControl` — ใช้ร่วมหลายหน้าจอ |
| {…} : Recheck Doc Flow Success |  | 4 | SMLAPARControl/_ar_ap_trans.cs:1692 `_docNoAdd`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2508 `_docNoAdd` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเรียกเอกสารกลับมาใชังานได้ปรกติ หรือไม่ |  | 4 | SMLAPARControl/_ar_ap_trans.cs:1830 `ProcessCmdKey`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2628 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ยกเลิกเอกสารสำเร็จ |  | 4 | SMLAPARControl/_ar_ap_trans.cs:1787 `ProcessCmdKey`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2593 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| เรียกคืนเอกสารสำเร็จ |  | 4 | SMLAPARControl/_ar_ap_trans.cs:1869 `ProcessCmdKey`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2663 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน สาขา | ผิดพลาด | 3 | SMLAPARControl/_ar_ap_trans.cs:2167 `_saveData`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:1592 `_saveData` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อน แผนก | ผิดพลาด | 3 | SMLAPARControl/_ar_ap_trans.cs:2232 `_saveData`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:1658 `_saveData` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกลูกค้า |  | 3 | SMLAPARControl/_payControl.cs:2111 `_findChqButton_Click`<br>SMLAPARControl/_payDepositAdvanceGridControl.cs:322 `SearchDepositAdvance` | ส่วนกลาง `_payControl`, `_payDepositAdvanceGridControl`, `_posPayForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณเลือกประเภทเอกสารก่อน |  | 3 | SMLAPARControl/_refDocControl.cs:234 `_displayAPARTransSearch`<br>SMLERPIC/_icHiddenCost/_icHiddenCostScreenDetailControl.cs:614 `_displayIcTransSearch` | ส่วนกลาง `_icHiddenCostScreenDetailControl`, `_icTransRefControl`, `_refDocControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการส่งข้อมูล e-Tax หรือไม่ |  | 3 | SMLAPARControl/_ar_ap_trans.cs:2976<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2190 | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ทำงานสำเร็จ `save_success` | แจ้ง | 3 | MyLib/_manageMasterCodeFull.cs:328 `_finish`<br>SMLAPARControl/_ap_ar_deposit_control.cs:138 `_ap_ar_deposit_control` | หน้าจอกลาง — ขึ้นได้ใน 74 เมนู |
| เอกสาร {…} ได้ส่ง e-Tax ไปแล้ว |  | 3 | SMLAPARControl/_ar_ap_trans.cs:2990<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2204 | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| เอกสารซ้ำ |  | 3 | SMLAPARControl/_refDocControl.cs:147 `_build`<br>SMLERPIC/_icHiddenCost/_icHiddenCostScreenDetailControl.cs:709 `_displayIcTransSearch` | ส่วนกลาง `_icHiddenCostScreenDetailControl`, `_icTransRefControl`, `_refDocControl` — ใช้ร่วมหลายหน้าจอ |
| เอกสารนี้ไม่ได้ตั้งค่าให้ส่งข้อมูล e-Tax |  | 3 | SMLAPARControl/_ar_ap_trans.cs:2966<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2180 | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| เอกสารอ้างอิงไปแล้ว |  | 3 | SMLAPARControl/_ar_ap_trans.cs:1799 `ProcessCmdKey`<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2605 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| The data was imported successfully. |  | 2 | SMLAPARControl/_importDebtBilling.cs:138 `_clipboardbutton_Click`<br>SMLAPARControl/_importDebtBilling.cs:155 `_clipboardbutton_Click` | Data › Import File Cash Received Account Receivable |
| TransScreenMore : มีการสร้างจอสองครั้ง |  | 2 | SMLAPARControl/ap_ar_trans_screen_more.cs:55 `_newData`<br>SMLInventoryControl/_icTransScreenMoreControl.cs:62 `_newData` | ส่วนกลาง `_icTransScreenMoreControl`, `ap_ar_trans_screen_more` — ใช้ร่วมหลายหน้าจอ |
| _vatType Error |  | 2 | SMLAPARControl/_depositControl/_po_so_deposit_control.cs:79<br>SMLInventoryControl/_icTransControl.cs:294 `AddReferDoc` | ส่วนกลาง `_icTransControl`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| กรุณากรอกข้อมูล สมุดธนาคาร | แจ้ง | 2 | SMLAPARControl/_payControl.cs:1730 `_payChqAmount`<br>SMLAPARControl/_payControl.cs:1735 `_payChqAmount` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาตรวจสอบ จำนวนเงินชำระเงินไม่ครบตามจำนวน <br>\r ต้องการทำขั้นตอนต่อไป กด YES <br>\r ต้องการกลับไปตรวจสอบใหม่ กด NO | ถาม | 2 | SMLAPARControl/_payControl.cs:1748 `_payChqAmount`<br>SMLAPARControl/_payControl.cs:1770 `_payChqAmount` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนข้อมูล <br>{…} | ผิดพลาด | 2 | SMLAPARControl/_ar_cut_point.cs:129 `_ar_cut_point`<br>SMLAPARControl/_ar_point_balance.cs:128 `_ar_point_balance` | ส่วนกลาง `_ar_cut_point`, `_ar_point_balance` — ใช้ร่วมหลายหน้าจอ |
| คูปอง {…} ใช้ังานไปแล้ว |  | 2 | SMLAPARControl/_payCouponGridControl.cs:155 `_payCouponGridControl__afterRemoveRow`<br>SMLAPARControl/_payCouponGridControl.cs:282 `_checker` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| ดำเนินการส่งข้อมูล e-Tax สำเร็จ |  | 2 | SMLAPARControl/_ar_ap_trans.cs:2984<br>SMLAPARControl/_depositControl/_po_so_deposit_control.cs:2198 | ส่วนกลาง `_ar_ap_trans`, `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ยอด Debit, Credit ไม่เท่ากัน<br>ไม่สามารถบันทึกรายการได้ | เตือน | 2 | SMLAPARControl/_ap_ar_gl.cs:109 `_save_data`<br>SMLERPGL/_journalEntryAccount.cs:404 `_saveLog` | บัญชี › บัญชีแยกประเภท › ข้อมูลรายวัน |
| ลบประวัติการส่งข้อมูล e-Tax เรียบร้อยแล้ว |  | 2 | SMLAPARControl/_ar_ap_trans.cs:621 `_buttonDeleteEtaxTransaction_Click`<br>SMLInventoryControl/_icTransControl.cs:5972 `_buttonDeleteEtaxTransaction_Click` | ส่วนกลาง `_ar_ap_trans`, `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| วันที่เอกสารห้ามว่าง | แจ้ง | 2 | SMLAPARControl/_ar_ap_trans.cs:3911 `_glButton_Click`<br>SMLAPARControl/_ar_ap_trans.cs:3970 `_print_Click` | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเปิดลิ้นชักได้ กรุณาตรวจสอบการตั้งค่าและอุปกรณ์ที่เชื่อมต่อ<br>{…} | ผิดพลาด | 2 | SMLAPARControl/_ar_ap_trans.cs:2933<br>SMLInventoryControl/_icTransControl.cs:17456 | ส่วนกลาง `_ar_ap_trans`, `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| Cancel failed! | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:2091 `_cancalPayTigerButton_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Cancel success! | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:2084 `_cancalPayTigerButton_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Canceled before polling started. | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:1901 `_TigerCash_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Case not found : {…} |  | 1 | SMLAPARControl/_payChequeGridControl.cs:501 `_build` | ส่วนกลาง `_payChequeGridControl` — ใช้ร่วมหลายหน้าจอ |
| ERROR: {…} |  | 1 | SMLAPARControl/_payControl.cs:2003 `PollingPaymentStatus` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Error : _icTransControlType |  | 1 | SMLAPARControl/_advanceControl.cs:67 `_queryDelete` | ส่วนกลาง `_advanceControl` — ใช้ร่วมหลายหน้าจอ |
| Order ID not found. | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:1922 `_TigerCash_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Payment Canceled! | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:2073 `_cancalPayTigerButton_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Please enter Doc_date Doc_type Income_code Expense_Code |  | 1 | SMLAPARControl/_importDebtBilling.cs:165 `_clipboardbutton_Click` | Data › Import File Cash Received Account Receivable |
| Screen Bottom Duplicate |  | 1 | SMLAPARControl/_ar_ap_trans_screen_bottom.cs:47 `_ar_ap_trans_screen_bottom` | ส่วนกลาง `_ar_ap_trans_screen_bottom` — ใช้ร่วมหลายหน้าจอ |
| Send K Merchant API Error:{…} | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:2467 `_payWithKbankQRApi_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| Unexpected Error: {…} | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:1942 `_TigerCash_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| _PoSoDepositScreenBottomControl สร้างมากกว่า 1 ครั้ง |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_screen_bottom_control.cs:48 | ส่วนกลาง `_po_so_deposit_screen_bottom_control` — ใช้ร่วมหลายหน้าจอ |
| _PoSoDepositScreenTopControl สร้างมากกว่า 1 ครั้ง |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_screen_top_control.cs:79 `_newData` | ส่วนกลาง `_po_so_deposit_screen_top_control` — ใช้ร่วมหลายหน้าจอ |
| _ar_ap_trans_grid : มีการสร้างจอสองครั้ง |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:75 `_ar_ap_trans_grid` | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| _ar_ap_trans_screen_top : มีการสร้างจอสองครั้ง |  | 1 | SMLAPARControl/_ar_ap_trans_screen_top.cs:101 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans_screen_top` — ใช้ร่วมหลายหน้าจอ |
| _payDetailScreen สร้างมากกว่า 1 ครั้ง |  | 1 | SMLAPARControl/_payDetailScreen.cs:49 `_payDetailScreen` | ส่วนกลาง `_payDetailScreen` — ใช้ร่วมหลายหน้าจอ |
| _po_so_deposit_screen_more_control : มีการสร้างจอสองครั้ง |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_screen_more_control.cs:64 `_newData` | ส่วนกลาง `_po_so_deposit_screen_more_control` — ใช้ร่วมหลายหน้าจอ |
| error{…} |  | 1 | SMLAPARControl/_ar_ap_trans.cs:2789 | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| grid สร้างมากกว่า 1 ครั้ง |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_control.cs:667 `_po_so_deposit_control` | ส่วนกลาง `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ok |  | 1 | SMLAPARControl/_ar_ap_trans_screen_top.cs:1156 | ส่วนกลาง `_ar_ap_trans_screen_top` — ใช้ร่วมหลายหน้าจอ |
| pay detail Case not found : {…} |  | 1 | SMLAPARControl/_payDetailScreen.cs:1382 | ส่วนกลาง `_payDetailScreen` — ใช้ร่วมหลายหน้าจอ |
| save documents? |  | 1 | SMLAPARControl/_importDebtBilling.cs:124 `_clipboardbutton_Click` | Data › Import File Cash Received Account Receivable |
| กรุณาเลือกลูกค้าเดียวกันเท่านั้น |  | 1 | SMLAPARControl/_arBillOverDueForm.cs:44 `vistaButton1_Click` | ส่วนกลาง `_arBillOverDueForm` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกเงือนไขก่อน | แจ้ง | 1 | SMLAPARControl/_search_bill_auto.cs:68 `_OkButton_Click` | ส่วนกลาง `_search_bill_auto` — ใช้ร่วมหลายหน้าจอ |
| คูปอง {…} ถูกยกเลิกใช้งาน |  | 1 | SMLAPARControl/_payCouponGridControl.cs:150 `_payCouponGridControl__afterRemoveRow` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| คูปองหมดอายุ ไปตั้งแต่ วันที่ {…}dd/MM/yyyy{…} |  | 1 | SMLAPARControl/_payCouponGridControl.cs:143 `_payCouponGridControl__afterRemoveRow` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเงินชำระต้องมากกว่า 0 | ผิดพลาด | 1 | SMLAPARControl/_payControl.cs:2419 `_payWithKbankQRApi_Click` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเงินมัดจำเกินจำนวนเอกสารอ้างอิง |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_control.cs:1645 `_saveData` | ส่วนกลาง `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเงินไม่สัมพันธ์กับมูลค่าคงเหลือเช็ค |  | 1 | SMLAPARControl/_payChequeGridControl.cs:651 | ส่วนกลาง `_payChequeGridControl` — ใช้ร่วมหลายหน้าจอ |
| จำนวนเงินไม่สัมพันธ์กับมูลค่าเช็ค |  | 1 | SMLAPARControl/_payChequeGridControl.cs:641 | ส่วนกลาง `_payChequeGridControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนจำนวนเงินไม่สมบูรณ์ |  | 1 | SMLAPARControl/_payCouponGridControl.cs:203 `_payCouponGridControl__afterRemoveRow` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนยอดชำระเกิน |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:443 `_ar_ap_trans_grid` | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| ผิดพลาด : {…}<br>กรุณาติดต่อเจ้าหน้าที่ |  | 1 | SMLAPARControl/_eWalletPaymentControl.cs:569 `_buttonKBankPromptPay_Click` | ส่วนกลาง `_eWalletPaymentControl` — ใช้ร่วมหลายหน้าจอ |
| มีรายการซ้ำ : {…} |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:485 | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| ยอดการจ่ายเงินไม่สมบูรณ์ |  | 1 | SMLAPARControl/_payControl.cs:400 `_checker` | ส่วนกลาง `_payControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดคืน ไม่สัมพันธ์กับยอดคงเหลือ |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_control.cs:1717 `_saveData` | ส่วนกลาง `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |
| ยอดตัดจ่ายมากกว่ายอดคงเหลือ |  | 1 | SMLAPARControl/_payDepositAdvanceGridControl.cs:231 `_payDepositAdvanceGridControl__afterRemoveRow` | ส่วนกลาง `_payDepositAdvanceGridControl` — ใช้ร่วมหลายหน้าจอ |
| ยอดเดบิต เครดิต ไม่ลงตัว | ผิดพลาด | 1 | SMLAPARControl/_ar_ap_trans.cs:2785 | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการรับชำระเงิน | ถาม | 1 | SMLAPARControl/_waitPaymentConfirmForm.cs:313 `_confirmButton_Click` | ส่วนกลาง `_waitPaymentConfirmForm` — ใช้ร่วมหลายหน้าจอ |
| รหัสลูกหนี้ ห้ามว่าง | แจ้ง | 1 | SMLAPARControl/_ar_ap_trans.cs:1592 `_extraWhere` | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| รหัสเจ้าหนี้ ห้ามว่าง | แจ้ง | 1 | SMLAPARControl/_ar_ap_trans.cs:1588 `_extraWhere` | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| ลูกค้าไม่ตรงกับคูปอง |  | 1 | SMLAPARControl/_payCouponGridControl.cs:135 `_payCouponGridControl__afterRemoveRow` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| ลูกหนี้ไม่สัมพันธ์กัน |  | 1 | SMLAPARControl/_ar_ap_trans.cs:1950 `ProcessCmdKey` | ส่วนกลาง `_ar_ap_trans` — ใช้ร่วมหลายหน้าจอ |
| ห้ามรับวางบิลซ้ำ : {…} |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:499 | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| ห้ามวางบิลซ้ำ : {…} |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:501 | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| เอกสาร {…} ไม่มียอดคงเหลือแล้ว |  | 1 | SMLAPARControl/_depositControl/_po_so_deposit_screen_top_control.cs:1209 `_search` | ส่วนกลาง `_po_so_deposit_screen_top_control` — ใช้ร่วมหลายหน้าจอ |
| เอกสารไม่สามารถนำมายกเลิกได้อีก |  | 1 | SMLAPARControl/_ar_ap_trans_screen_top.cs:2005 `_search` | ส่วนกลาง `_ar_ap_trans_screen_top` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบคูปอง : {…} |  | 1 | SMLAPARControl/_payCouponGridControl.cs:189 `_payCouponGridControl__afterRemoveRow` | ส่วนกลาง `_payCouponGridControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการ ดังต่อไปนี้ กรุณาตรวจสอบใหม่<br>{…} |  | 1 | SMLAPARControl/_ar_ap_trans_grid.cs:895 `_searchBillList` | ส่วนกลาง `_ar_ap_trans_grid` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายระเอียดการชำระ |  | 1 | SMLAPARControl/_waitPaymentConfirmForm.cs:272 `_waitPaymentConfirmForm_Load` | ส่วนกลาง `_waitPaymentConfirmForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่มียอดเงินมัดจำ | ผิดพลาด | 1 | SMLAPARControl/_depositControl/_po_so_deposit_control.cs:1579 `_saveData` | ส่วนกลาง `_po_so_deposit_control` — ใช้ร่วมหลายหน้าจอ |

## SMLPOSControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| โต๊ะนี้ยังไม่เปิด |  | 8 | SMLPOSControl/_food/_orderControl.cs:306 `_orderScreen`<br>SMLPOSControl/_food/_orderControl.cs:463 `_tableCloseButton_Click` | ส่วนกลาง `_orderControl`, `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| ปิดโต๊ะหมายเลข : {…}/{…} สำเร็จ |  | 6 | SMLPOSControl/_food/_foodOrderControl.cs:936 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:971 `_checkInputKey` | ส่วนกลาง `_foodOrderControl`, `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้เลือกโต๊ะ ต้นทางและปลายทาง | ผิดพลาด | 4 | SMLPOSControl/_food/_tableMoveControl.cs:205 `_moveOutAllButton_Click`<br>SMLPOSControl/_food/_tableMoveControl.cs:405 `_moveOutButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีรายการอาหารในโต๊ะ {…}/{…} คุณต้องการที่จะปิดโต๊ะ หรือไม่ | แจ้ง | 3 | SMLPOSControl/_food/_foodOrderControl.cs:953 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:1197 `_inputCodeTextbox_KeyUp` | ส่วนกลาง `_foodOrderControl`, `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกโต๊ะก่อนทำรายการบันทึกรายการ/ปิดโต๊ะ |  | 2 | SMLPOSControl/_food/_foodOrderControl.cs:990 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:1234 `_inputCodeTextbox_KeyUp` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการย้ายจำนวนทั้งหมดหรือไม่ | ถาม | 2 | SMLPOSControl/_food/_tableMoveControl.cs:219 `_moveOutAllButton_Click`<br>SMLPOSControl/_food/_tableMoveControl.cs:307 `_moveOutAllButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกรายการสั่งอาหาร เรียบร้อยแล้ว | แจ้ง | 2 | SMLPOSControl/_food/_foodOrderControl.cs:592 `_saveData`<br>SMLPOSControl/_food/_foodOrderControl.cs:608 `_saveData` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนจำนวนผิด |  | 2 | SMLPOSControl/_food/_tableMoveControl.cs:233 `_moveOutAllButton_Click`<br>SMLPOSControl/_food/_tableMoveControl.cs:320 `_moveOutAllButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ผิดพลาด |  | 2 | SMLPOSControl/_food/_tableMoveControl.cs:76 `_tableMoveControl`<br>SMLPOSControl/_food/_tableMoveControl.cs:110 `_tableMoveControl` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการบันทึกรายการ/ปิดโต๊ะ โต๊ะ : {…}/{…} | ถาม | 2 | SMLPOSControl/_food/_foodOrderControl.cs:901 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:1145 `_inputCodeTextbox_KeyUp` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ส่งพิมพ์รายการสั่งอาหาร เรียบร้อยแล้ว | แจ้ง | 2 | SMLPOSControl/_food/_tableInfoControl.cs:161 `_reprintOrderButton_Click`<br>SMLPOSControl/_food/_tableInfoControl.cs:174 `_reprintOrderButton_Click` | ส่วนกลาง `_tableInfoControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามแก้ไขรายการอาหาร | เตือน | 2 | SMLPOSControl/_food/_orderControl.cs:900 `_editOrderButton_Click`<br>SMLPosClient/_posClientForm.cs:11688 `_command` | ส่วนกลาง `_orderControl`, `_posClientForm` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะ {…} ไม่สามารถปิดโต๊ะได้ |  | 2 | SMLPOSControl/_food/_foodOrderControl.cs:982 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:1226 `_inputCodeTextbox_KeyUp` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะ {…} ไม่สามารถสั่งอาหารได้ |  | 2 | SMLPOSControl/_food/_foodOrderControl.cs:1068 `_checkInputKey`<br>SMLPOSControl/_food/_foodOrderControl.cs:1312 `_inputCodeTextbox_KeyUp` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะยังไม่ได้เปิด |  | 2 | SMLPOSControl/_food/_tableMoveControl.cs:55 `_tableMoveControl`<br>SMLPOSControl/_food/_tableMoveControl.cs:93 `_tableMoveControl` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเลือกโต๊ะนี้ได้ กำลังอยู่ในสถานะ รอคิดเงิน |  | 2 | SMLPOSControl/_food/_tableMoveControl.cs:73 `_tableMoveControl`<br>SMLPOSControl/_food/_tableMoveControl.cs:107 `_tableMoveControl` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| Install POS Sound Success !! |  | 1 | SMLPOSControl/_posDownloadSound.cs:85 `_startButton_Click` | เริ่มต้น › ระบบขาย › Download ระบบเสียงพูด |
| กรุณายิง Barcode ก่อน |  | 1 | SMLPOSControl/_checkPriceUserControl.cs:105 `label3_Click` | สินค้า › ข้อมูลสินค้า › ตรวจสอบราคาสินค้า |
| กรุณาเลือกโต๊ะก่อน |  | 1 | SMLPOSControl/_food/_foodOrderControl.cs:459 `_saveData` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| กำลังดาวน์โหลด เสียงจาก Server คุณต้องการที่ะยกเลิกแล้วจบการทำงานหรือไม่ | ถาม | 1 | SMLPOSControl/_posDownloadSound.cs:31 `OnClosing` | เริ่มต้น › ระบบขาย › Download ระบบเสียงพูด |
| ต้องการบันทึกรายการหรือไม่ | ถาม | 1 | SMLPOSControl/_food/_tableMoveControl.cs:463 `_saveButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการยกเลิกรายการทั้งหมดหรือไม่ | ถาม | 1 | SMLPOSControl/_food/_orderCancelControl.cs:553 `_cancelAllOrder_Click` | ส่วนกลาง `_orderCancelControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการย้ายกลับทั้งหมดหรือไม่ | ถาม | 1 | SMLPOSControl/_food/_tableMoveControl.cs:411 `_moveInAllButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการย้ายไปทั้งหมดหรือไม่ | ถาม | 1 | SMLPOSControl/_food/_tableMoveControl.cs:185 `_moveOutAllButton_Click` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเปลี่ยนราคาเป็น : {…} บาท | แจ้ง | 1 | SMLPOSControl/_checkPriceUserControl.cs:87 `label3_Click` | สินค้า › ข้อมูลสินค้า › ตรวจสอบราคาสินค้า |
| ต้องการเริ่มใหม่หรือไม่ | แจ้ง | 1 | SMLPOSControl/_food/_foodOrderControl.cs:319 `_loadControl` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ป้อนจำนวนยกเลิกผิด | ผิดพลาด | 1 | SMLPOSControl/_food/_orderCancelControl.cs:101 `_orderCancelControl` | ส่วนกลาง `_orderCancelControl` — ใช้ร่วมหลายหน้าจอ |
| ยกเลิกปิดโต๊ะหมายเลข : {…}/{…} สำเร็จ |  | 1 | SMLPOSControl/_food/_orderControl.cs:771 `_tableReOpenButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการปิดโต๊ะ | ถาม | 1 | SMLPOSControl/_food/_orderControl.cs:467 `_tableCloseButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการยกเลิกปิดโต๊ะ | ถาม | 1 | SMLPOSControl/_food/_orderControl.cs:742 `_tableReOpenButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการลบรายการ | ถาม | 1 | SMLPOSControl/_food/_foodOrderControl.cs:291 `_loadControl` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการแก้ไขรายละเอียดการสั่งอาหาร | แจ้ง | 1 | SMLPOSControl/_food/_tableOrderEditControl.cs:78 `_tableOrderEditControl` | ส่วนกลาง `_tableOrderEditControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสผ่านผิด กรุณาตรวจสอบ | ผิดพลาด | 1 | SMLPOSControl/_food/_selectSaleUserControl.cs:130 `_saleSelect` | ส่วนกลาง `_selectSaleUserControl` — ใช้ร่วมหลายหน้าจอ |
| รายการอาหารนี้ถูกยกเลิกไปหมดแล้ว | ผิดพลาด | 1 | SMLPOSControl/_food/_orderCancelControl.cs:84 `_orderCancelControl` | ส่วนกลาง `_orderCancelControl` — ใช้ร่วมหลายหน้าจอ |
| สินค้า {…} หยุดขาย |  | 1 | SMLPOSControl/_food/_foodOrderControl.cs:707 `_buttonSearchItem_Click` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามยกเลิกรายการอาหาร | เตือน | 1 | SMLPOSControl/_food/_orderControl.cs:704 `_cancelOrderButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ห้ามเลือกโต๊ะเดียวกัน |  | 1 | SMLPOSControl/_food/_tableMoveControl.cs:86 `_tableMoveControl` | ส่วนกลาง `_tableMoveControl` — ใช้ร่วมหลายหน้าจอ |
| เปลี่ยนราคาสำเร็จ |  | 1 | SMLPOSControl/_checkPriceUserControl.cs:94 `label3_Click` | สินค้า › ข้อมูลสินค้า › ตรวจสอบราคาสินค้า |
| เปิดโต๊ะหมายเลข : {…}/{…}สำเร็จ |  | 1 | SMLPOSControl/_food/_orderControl.cs:230 `_openTableButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะ {…} มีการใช้งานอยู่ |  | 1 | SMLPOSControl/_table.cs:118 `_table` | ส่วนกลาง `_table` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะนี้ยังไม่ปิด |  | 1 | SMLPOSControl/_food/_orderControl.cs:738 `_tableReOpenButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| โต๊ะนี้เปิดไปแล้ว |  | 1 | SMLPOSControl/_food/_orderControl.cs:275 `_openTableButton_Click` | ส่วนกลาง `_orderControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบเลขที่เอกสารการสั่งอาหาร | แจ้ง | 1 | SMLPOSControl/_food/_foodOrderControl.cs:635 `_saveData` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีรายการอาหาร | แจ้ง | 1 | SMLPOSControl/_food/_foodOrderControl.cs:644 `_saveData` | ส่วนกลาง `_foodOrderControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถแก้ัไขได้ โต๊ะ ดังกล่าวมีการใช้งานอยู่ |  | 1 | SMLPOSControl/_table.cs:199 `_saveData` | ส่วนกลาง `_table` — ใช้ร่วมหลายหน้าจอ |
| ไม่อนุญาติให้จำนวนที่สั่งเป็น 0 |  | 1 | SMLPOSControl/_food/_foodDetailForm.cs:34 `_saveButton_Click` | ส่วนกลาง `_foodDetailForm` — ใช้ร่วมหลายหน้าจอ |

## SMLERPIC

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| บันทึกข้อมูลสำเร็จ | แจ้ง | 110 | IMEXControl/QualityControl/LabBeginningBalance/QCLabBalance.cs:178 `saveData`<br>IMEXControl/QualityControl/ProductContainerAdjustment/_productContainerAdjustmentControl.cs:245 `saveData` | หน้าจอกลาง — ขึ้นได้ใน 138 เมนู |
| ลบข้อมูลสำเสร็จ `delete_success` | แจ้ง | 33 | IMEXControl/QualityControl/ICQCPassControl.cs:235 `deleteData`<br>IMEXControl/QualityControl/ICQCQuarantineConrol.cs:101 `deleteData` | หน้าจอกลาง — ขึ้นได้ใน 24 เมนู |
| ต้องการดึงข้อมูลใหม่มาแทนของเดิมหรือไม่ |  | 4 | SMLERPIC/_icMainControl.cs:674 `_loadWarehouseAndLocationAuto`<br>SMLERPIC/_icWarehouseLocation.cs:97 `_getWareHouseAndLocationButton_Click` | สินค้า › ข้อมูลสินค้า › คลังที่เก็บสินค้า |
| ต้องการล้างข้อมูลหรือไม่ |  | 2 | SMLERPIC/_icMainControl.cs:719 `_clearButton_Click`<br>SMLERPIC/_icWarehouseLocation.cs:86 `_clearButton_Click` | สินค้า › ข้อมูลสินค้า › คลังที่เก็บสินค้า |
| ไม่พบหน่วยต้นทุนในตารางหน่วยนับ |  | 2 | SMLERPIC/_icMain.cs:598 `_saveData`<br>SMLInventoryControl/_icUpdateControl.cs:603 `_saveData` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| ไม่พบหน่วยมาตรฐานในตารางหน่วยนับ |  | 2 | SMLERPIC/_icMain.cs:626 `_saveData`<br>SMLInventoryControl/_icUpdateControl.cs:625 `_saveData` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| ไม่อนุญาติให้เพิ่มสูตรสี |  | 2 | SMLERPIC/_icMain.cs:670 `_saveData`<br>SMLERPIC/_icMainColorSet.cs:196 `_saveData` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| Barcode ซ้ำ : {…} |  | 1 | SMLERPIC/_utility.cs:29 `_barcodeDuplicate` | ส่วนกลาง `_utility` — ใช้ร่วมหลายหน้าจอ |
| Process End |  | 1 | SMLERPIC/_icStockColorAdj.cs:253 `_process` | ส่วนกลาง `_icStockColorAdj` — ใช้ร่วมหลายหน้าจอ |
| Save : {…} | แจ้ง | 1 | SMLERPIC/_icStockColorAdj.cs:232 `_process` | ส่วนกลาง `_icStockColorAdj` — ใช้ร่วมหลายหน้าจอ |
| Success and open file : {…} |  | 1 | SMLERPIC/_icBuildPriceList.cs:144 `_processButton_Click` | ส่วนกลาง `_icBuildPriceList` — ใช้ร่วมหลายหน้าจอ |
| Success. |  | 1 | SMLERPIC/_icStockColorRecalc.cs:82 `_processButton_Click` | ส่วนกลาง `_icStockColorRecalc` — ใช้ร่วมหลายหน้าจอ |
| Update | แจ้ง | 1 | SMLERPIC/_icPointUpdateControl.cs:55 `ToolStripButton_Click` | ส่วนกลาง `_icPointUpdateControl` — ใช้ร่วมหลายหน้าจอ |
| Update Success !! |  | 1 | SMLERPIC/_icEditDetailFast.cs:112 `_icEditDetailFast` | สินค้า › ข้อมูลสินค้า › แก้ไขรายละเอียด(เร็ว) |
| {…} ซ้ำ |  | 1 | SMLERPIC/_gridICSpecialSearchWord.cs:41 `_gridICSpecialSearchWord__alterCellUpdate` | ส่วนกลาง `_gridICSpecialSearchWord` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนช่องดังต่อไปนี้ <br>{…} | ผิดพลาด | 1 | SMLERPIC/_icSerialStockCheck.cs:371 `_saveButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| กรุณาป้อนรหัสสินค้า {…} |  | 1 | SMLERPIC/_icSerialStockCheck.cs:381 `_saveButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| กรุณาป้อนหน่วยนับ {…} |  | 1 | SMLERPIC/_icSerialStockCheck.cs:389 `_saveButton_Click` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| กรุณาเลือกสินค้า |  | 1 | SMLERPIC/_icSerialStockCheck.cs:616 `ProcessCmdKey` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| ข้อมูลไม่สมบูรณ์ |  | 1 | SMLERPIC/_icAddBarcodeFastControl.cs:391 `ProcessCmdKey` | สินค้า › ข้อมูลสินค้า › เพิ่มบาร์โค๊ดสินค้าแบบเร็ว |
| คุณต้องการล้างการกำหนดลำดับการค้นหาหรือไม่ | ถาม | 1 | SMLERPIC/_icSearchLevelMultiItem.cs:60 `_icSearchLevelMultiItem` | สินค้า › ข้อมูลสินค้า › กำหนดลำดับการค้นหา (เร็ว) |
| ดำเนินการ Reset Flow สำเร็จ |  | 1 | SMLERPIC/_icRecalc.cs:345 `_recheckFlowButton_Click` | สินค้า › คำนวณยอดสต๊อกใหม่ |
| ดำเนินการเสร็จสิ้นแล้ว | เตือน | 1 | SMLERPIC/_icModifyPrice.cs:1321 | สินค้า › ข้อมูลสินค้า › ปรับราคาสินค้า |
| มีการป้อน Serial Number {…} ไปแล้ว | แจ้ง | 1 | SMLERPIC/_icSerialStockCheck.cs:286 `_icSerialStockCheck` | สินค้า › ระบบตรวจนับสินค้า › ตรวจสอบสินค้า Serial Number |
| ยังไม่บันทึกคลังที่เก็บ |  | 1 | SMLERPIC/_icMain.cs:654 `_saveData` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| ล้างการกำหนดลำดับการค้นหาสำเร็จ |  | 1 | SMLERPIC/_icSearchLevelMultiItem.cs:67 `_icSearchLevelMultiItem` | สินค้า › ข้อมูลสินค้า › กำหนดลำดับการค้นหา (เร็ว) |
| สินค้ามีการใช้ไปแล้ว ห้ามลบ : {…} |  | 1 | SMLERPIC/_icMain.cs:293 `ProcessCmdKey` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| หน้าจอนี้ห้ามลบข้อมูล |  | 1 | SMLERPIC/_icMain.cs:361 `ProcessCmdKey` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า |
| ไม่มีข้อมูล |  | 1 | SMLERPIC/_icStockColorAdj.cs:414 `_save` | ส่วนกลาง `_icStockColorAdj` — ใช้ร่วมหลายหน้าจอ |

## SMLERPGlobal

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Fail : {…} |  | 9 | MyLib/_manageMasterCodeFull.cs:238 `_finish`<br>MyLib/_manageMasterCodeFull.cs:243 `_finish` | หน้าจอกลาง — ขึ้นได้ใน 79 เมนู |
| Error | ผิดพลาด | 3 | SMLERPGlobal/_ic_add_warehouse_shelf_form.cs:61 `_processButton_Click2`<br>SMLERPGlobal/_ic_add_warehouse_shelf_form.cs:93 `_processButton_Click2` | เริ่มต้น › ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ |
| มีการใช้งานรหัสดังกล่าวไปแล้ว กรุณาตรวจสอบ | ผิดพลาด | 2 | SMLERPGlobal/_selectMenu.cs:643<br>SMLERPGlobal/_selectMenu.cs:724 | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| _apArTransCalcType case not found : {…} |  | 1 | SMLERPGlobal/_global.cs:2741 `_apArTransCalcType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _icTransFlagGlobal by number case not found {…} |  | 1 | SMLERPGlobal/_global.cs:1563 `_transFlagByNumber` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _icTransFlagGlobal case not found {…} |  | 1 | SMLERPGlobal/_global.cs:1849 `_transFlag` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _ictransGlobalTemplate case not found {…} |  | 1 | SMLERPGlobal/_global.cs:2070 `_transTemplate` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _payType case not found {…} |  | 1 | SMLERPGlobal/_global.cs:2209 `_payType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _transFlagByScreenCode case not found {…} |  | 1 | SMLERPGlobal/_global.cs:1315 `_transFlagByScreenCode` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _transName case not found {…} |  | 1 | SMLERPGlobal/_global.cs:1145 `_transName` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _transStockCalcType case not found : {…} |  | 1 | SMLERPGlobal/_global.cs:2597 `_transStockCalcType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _transType case not found {…} |  | 1 | SMLERPGlobal/_global.cs:2399 `_transType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _vatBuyType case not found {…} |  | 1 | SMLERPGlobal/_global.cs:2110 `_vatBuyType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| _vatSaleType case not found {…} |  | 1 | SMLERPGlobal/_global.cs:2144 `_vatSaleType` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| กรุณากรอกข้อมูล มูลค่า เป็น ตัวเลข |  | 1 | SMLERPGlobal/_selectMenu.cs:1293 | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| กรุณาสำรองข้อมูลประจำวัน ต้องการดูคู่มือการสำรองข้อมูลหรือไม่ |  | 1 | SMLERPGlobal/_global.cs:4196 `_checkBackup` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกกลุ่ม | ผิดพลาด | 1 | SMLERPGlobal/_userGroupWarehouseShelf.cs:234 `_userGroupNewData` | เริ่มต้น › รายละเอียดข้อมูลทั่วไป › กำหนดการใช้คลังและที่เก็บ |
| คำเตือน!<br>วันที่ปัจจุบัน หรือที่เอกสารที่กำหนด ได้ถูกปิดงวดไปแล้ว หรือยังไม่ได้กำหนดงวดบัญชี<br>กรุณาตรวจสอบ | เตือน | 1 | SMLERPGlobal/_global.cs:4003 `_checkOpenPeriod` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| ค่าเริ่มต้นไม่สมบูรณ์ให้ไปกำหนดค่าเริ่มต้นก่อนเริ่มใช้งาน : {…} |  | 1 | SMLERPGlobal/_smlOption.cs:403 `LoadErpOption` | ส่วนกลาง `_smlOption` — ใช้ร่วมหลายหน้าจอ |
| ต้องการล้างของเก่าหรือไม่ | แจ้ง | 1 | SMLERPGlobal/_docFormatGeneralLedgerControl.cs:119 `_loadFormatButton_Click` | ส่วนกลาง `_docFormatGeneralLedgerControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสผังบัญชีใหม่ซ้ำ |  | 1 | SMLERPGlobal/_changeCode/changeChartOfAccountUserControl.cs:89 `_grid__alterCellUpdate` | เริ่มต้น › เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสผังบัญชี |
| รหัสสินค้าใหม่ซ้ำ |  | 1 | SMLERPGlobal/_changeCode/_itemCodeUserControl.cs:74 `screenBuild` | เริ่มต้น › เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสสินค้า |
| ไม่พบ กลุ่มภาษี | แจ้ง | 1 | SMLERPGlobal/_global.cs:3920 `_searchTaxGroup` | ส่วนกลาง `_global` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลชื่อมิติ |  | 1 | SMLERPGlobal/_selectMenu.cs:538 | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลผังบัญชี : {…} |  | 1 | SMLERPGlobal/_docFormatGeneralLedgerControl.cs:165 `_loadFormatButton_Click` | ส่วนกลาง `_docFormatGeneralLedgerControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูลสินค้า |  | 1 | SMLERPGlobal/_ic_add_warehouse_shelf_form.cs:124 `_processButton_Click` | เริ่มต้น › ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ |

## SMLERPGL

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่สามารถทำรายการได้ |  | 9 | SMLERPGL/_report/_other_1/_report.cs:172 `_report`<br>SMLERPGL/_report/_profitAndLostBranch/_report.cs:200 `_report` | หน้าจอกลาง — ขึ้นได้ใน 17 เมนู |
| {…}กรุณาบันทึกรายละเอียดให้ครบก่อนPlease enter ref field |  | 8 | SMLERPASSET/_display/_depreciateByDay.cs:108 `_process`<br>SMLERPASSET/_display/_depreciateByMonth.cs:108 `_process` | หน้าจอกลาง — ขึ้นได้ใน 8 เมนู |
| ต้องการเปลี่ยนรหัสจริงหรือไม่ |  | 4 | SMLERPGL/_chart/_changeAccountCode.cs:35 `_buttonStart_Click`<br>SMLERPGL/_chart/_changeAccountCode.cs:44 `_buttonStart_Click` | ส่วนกลาง `_changeAccountCode` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการ {…} |  | 4 | SMLERPGL/JournalProductSaleCost/_journalSaleCostProductAccountGrid.cs:60 `_journalSaleCostProductAccountGrid__alterCellUpdate`<br>SMLERPGL/JournalProductSaleCost/_journalSaleCostPurchaseAccountGrid.cs:138 `_journalSaleCostProductAccountGrid__alterCellUpdate` | ส่วนกลาง `JournalSummaryDetailGrid`, `_journalSaleCostProductAccountGrid`, `_journalSaleCostPurchaseAccountGrid` — ใช้ร่วมหลายหน้าจอ |
| Data not found |  | 2 | SMLERPGL/_journalPass.cs:207 `_processButton_Click`<br>SMLERPGL/_journalPassUndo.cs:84 `_processButton_Click` | บัญชี › บัญชีแยกประเภท › ผ่านรายการ<br>บัญชี › บัญชีแยกประเภท › ยกเลิกผ่านรายการ |
| กรุณาเลือก เลขที่เอกสาร | ผิดพลาด | 2 | SMLERPGL/_journalEntryAccount.cs:396 `_saveLog`<br>SMLInventoryControl/_icTransControl.cs:13173 `_saveData` | บัญชี › บัญชีแยกประเภท › ข้อมูลรายวัน |
| ผิดพลาด : {…} | ผิดพลาด | 2 | SMLERPGL/AccountCloseWizard/JournalCloseAccountControl.cs:712 `_saveButton_Click`<br>SMLPOSControl/_checkPriceUserControl.cs:98 `label3_Click` | บัญชี › ประมวลผลกำไร/ขาดทุน และต้นทุนขาย<br>สินค้า › ข้อมูลสินค้า › ตรวจสอบราคาสินค้า |
| ดำเนินการสำเร็จ |  | 1 | SMLERPGL/StatementDesign/_statementDesigner.cs:202 `_saveButton_Click` | เริ่มต้น › ระบบบัญชี › ออกแบบงบการเงิน |
| ต้องการผ่านรายการจริงหรือไม่ | แจ้ง | 1 | SMLERPGL/_journalPass.cs:267 `_passButton_Click` | บัญชี › บัญชีแยกประเภท › ผ่านรายการ |
| ต้องการยกเลิกผ่านรายการจริงหรือไม่ | แจ้ง | 1 | SMLERPGL/_journalPassUndo.cs:117 `_passButton_Click` | บัญชี › บัญชีแยกประเภท › ยกเลิกผ่านรายการ |
| ต้องการสร้างงบใหม่ |  | 1 | SMLERPGL/_report/_reportDesign/_glDesign.cs:711 `_newButton_Click` | ส่วนกลาง `_glDesign` — ใช้ร่วมหลายหน้าจอ |
| ต้องการสร้างเป็นข้อมูลรายวันจริงหรือไม่ | แจ้ง | 1 | SMLERPGL/_journalEntryFast.cs:272 `_processButton_Click` | บัญชี › บัญชีแยกประเภท › บันทึกข้อมูลรายวันแบบเร็ว |
| ต้องกำหนดวันที่ก่อน |  | 1 | SMLERPGL/_report/_sheet/_report.cs:399 `_report` | บัญชี › บัญชีแยกประเภท › รายงานบัญชีแยกประเภท |
| ปรับปรุงข้อมูลสำเร็จ |  | 1 | SMLERPGL/_chart/_chartOfAccountFast.cs:211 `_buttonClose_Click` | ส่วนกลาง `_chartOfAccountFast` — ใช้ร่วมหลายหน้าจอ |
| ปรับปรุงข้อมูลไม่สำเร็จ : {…} |  | 1 | SMLERPGL/_chart/_chartOfAccountFast.cs:216 `_buttonClose_Click` | ส่วนกลาง `_chartOfAccountFast` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขข้อมูลบางส่วนแล้ว ท่านต้องการปิดหน้าจอจริงหรือไม่ | แจ้ง | 1 | SMLERPGL/_chart/_chartOfAccountFast.cs:181 `ProcessCmdKey` | ส่วนกลาง `_chartOfAccountFast` — ใช้ร่วมหลายหน้าจอ |
| มีรายการที่ยอดไม่ตรง (ดูที่บรรทัดสีแดง) |  | 1 | SMLERPGL/_journalEntryFast.cs:265 `_processButton_Click` | บัญชี › บัญชีแยกประเภท › บันทึกข้อมูลรายวันแบบเร็ว |
| รหัสซ้ำ |  | 1 | SMLERPGL/_report/_reportDesign/_saveAsControl.cs:51 `_buttonSave_Click` | ส่วนกลาง `_saveAsControl` — ใช้ร่วมหลายหน้าจอ |
| เปลี่ยนรหัสสมบูรณ์ |  | 1 | SMLERPGL/_chart/_changeAccountCode.cs:81 `_buttonStart_Click` | ส่วนกลาง `_changeAccountCode` — ใช้ร่วมหลายหน้าจอ |
| โปรแกรมจะทำการ Lock ข้อมูลผังบัญชีทั้งหมด ต้องการทำรายการต่อหรือไม่ | แจ้ง | 1 | SMLERPGL/_selectMenu.cs:47 `_getObject` | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรูปแบบเอกสาร |  | 1 | SMLERPGL/_transProcessUserControl.cs:2432 `processWithData` | บัญชี › บัญชีแยกประเภท › ประมวลผลจากข้อมูลรายวัน |
| ไม่พบเงื่อนไขข้อมูล |  | 1 | SMLERPGL/StatementDesign/_glFinanceReport.cs:792 `Build` | ส่วนกลาง `_glFinanceReport` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีรายการแก้ไข |  | 1 | SMLERPGL/_chart/_chartOfAccountFast.cs:221 `_buttonClose_Click` | ส่วนกลาง `_chartOfAccountFast` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถ Lock รายการผังบัญชีได้ เนื่องจากมีผู้อื่นใช้งานอยู่บางส่วน |  | 1 | SMLERPGL/_selectMenu.cs:58 `_getObject` | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |

## SMLERPControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ข้อมูลไม่สมบูรณ์ {…} `data_not_complete` | ผิดพลาด | 68 | MyLib/_manageMasterCodeFull.cs:370 `_finish`<br>SMLAPARControl/_ap_ar_deposit_control.cs:192 `_saveData` | หน้าจอกลาง — ขึ้นได้ใน 112 เมนู |
| สำเร็จ `save_success` | แจ้ง | 45 | SMLAPARControl/_ar_cut_point.cs:71 `_ar_cut_point`<br>SMLAPARControl/_ar_point_balance.cs:70 `_ar_point_balance` | หน้าจอกลาง — ขึ้นได้ใน 20 เมนู |
| มีการแก้ไขข้อมูลบางส่วน<br>ต้องการยกเลิกการแก้ไขหรือไม่ `warning1` | แจ้ง | 42 | MyLib/_databaseManage/_resourceEdit.cs:88 `OnClosing`<br>MyLib/_manageMasterCodeFull.cs:434 `_finish` | หน้าจอกลาง — ขึ้นได้ใน 90 เมนู |
| ไม่สามารถบันทึกข้อมูลได้ | ผิดพลาด | 8 | SMLERPControl/_customer/_ar.cs:389 `_save_data`<br>SMLERPControl/_customer/_ar_dealer.cs:178 `_save_data` | สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า<br>สินค้า › ข้อมูลสินค้า › ข้อมูลสินค้า (แสดงตามบาร์โค๊ด)<br>สินค้า › ข้อมูลสินค้า › กำหนดสินค้า<br>(+1 เมนู) |
| ท่านไม่มีสิทธิ์ แก้ไขข้อมูล `warning55` | เตือน | 3 | MyLib/_myManageData.cs:737 `_unlockRecord`<br>SMLERPControl/_customer/_ar_detail.cs:271 `_save_data` | ส่วนกลาง `_ap_detail`, `_ar_detail`, `_myManageData` — ใช้ร่วมหลายหน้าจอ |
| Finish |  | 2 | SMLERPControl/_imageTransfer.cs:42 `_imageTransfer`<br>SMLERPControl/_imageTransfer.cs:54 `_imageTransfer` | เริ่มต้น › เครื่องมือ › ย้ายรูปภาพสินค้า |
| Invalid time format. Please enter time in HH:mm format. |  | 2 | SMLERPControl/pos_slip_campaign/pos_slip_campaign_screentop.cs:38 `pos_slip_campaign_screentop`<br>SMLERPControl/pos_slip_campaign/pos_slip_campaign_screentop.cs:47 `pos_slip_campaign_screentop` | ส่วนกลาง `pos_slip_campaign_screentop` — ใช้ร่วมหลายหน้าจอ |
| invalided fomat |  | 2 | SMLERPControl/_getPicture.cs:1399 `pathToolStripMenuItem_Click`<br>SMLERPControl/_getPicture.cs:1684 `pasteToolStripMenuItem_Click` | ส่วนกลาง `_getPicture` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการทำการโอนย้ายรูปภาพ | เตือน | 2 | SMLERPControl/_imageTransfer.cs:103 `_transferProcessButton_Click`<br>SMLERPControl/_imageTransfer.cs:218 `_startTransferDocImageButton_Click` | เริ่มต้น › เครื่องมือ › ย้ายรูปภาพสินค้า |
| Cannot Reader Data:{…} |  | 1 | SMLERPControl/_customer/_ar.cs:665 `_readIDCardButton_Click` | ส่วนกลาง `_ar` — ใช้ร่วมหลายหน้าจอ |
| Doc not found |  | 1 | SMLERPControl/_importFromImageForm.cs:74 `_importFromImageForm` | เริ่มต้น › เครื่องมือ › นำเข้าข้อมูลจากรูปภาพ |
| Screen Dup |  | 1 | SMLERPControl/_bank/_chqListControl.cs:276 `_chqListScreenTopControl` | ส่วนกลาง `_chqListControl` — ใช้ร่วมหลายหน้าจอ |
| ชื่อลูกค้า : {…} ซ้ำ |  | 1 | SMLERPControl/_customer/_ar.cs:248 `_save_data` | ส่วนกลาง `_ar` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการทำการลดขนาดรูปภาพ | เตือน | 1 | SMLERPControl/_imageTransfer.cs:170 `_resizeImage_Click` | เริ่มต้น › เครื่องมือ › ย้ายรูปภาพสินค้า |
| รูปแแบบไม่ถูกต้อง<br> -รูปแบบต้องเป็น (9x9x99x99)<br>*** 9 แทนตัวเลขของ ความกว้าง ความยาว ความสูง หน่วย<br>ต้องอยู่ในรูปแบบ กว้างxยาวxสูงxหน่วย | แจ้ง | 1 | SMLERPControl/_ic/_icmainGridUnitControl.cs:113 `_createQueryForLoad` | ส่วนกลาง `_icmainGridUnitControl` — ใช้ร่วมหลายหน้าจอ |
| ลูกหนี้มีการใช้ไปแล้ว ห้ามลบ : {…} |  | 1 | SMLERPControl/_customer/_ar.cs:417 `_save_data` | ส่วนกลาง `_ar` — ใช้ร่วมหลายหน้าจอ |
| เจ้าหนี้มีการใช้ไปแล้ว ห้ามลบ : {…} |  | 1 | SMLERPControl/supplier/_ap.cs:239 `_save_data` | ส่วนกลาง `_ap` — ใช้ร่วมหลายหน้าจอ |
| โอนย้ายรูปภาพสำเร็จ |  | 1 | SMLERPControl/_imageTransfer.cs:234 `_transferDocImageButton_Click` | เริ่มต้น › เครื่องมือ › ย้ายรูปภาพสินค้า |
| โอนย้ายรูปภาพไม่สำเร็จ |  | 1 | SMLERPControl/_imageTransfer.cs:238 `_transferDocImageButton_Click` | เริ่มต้น › เครื่องมือ › ย้ายรูปภาพสินค้า |
| ไม่พบ {…} | แจ้ง | 1 | SMLERPControl/_ChqReceive/_chqReceiveScreen.cs:77 `_chqReceiveScreen` | ส่วนกลาง `_chqReceiveScreen` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสลูกหนี้ :{…} |  | 1 | SMLERPControl/_customer/_ar_dealer.cs:81 `_screen_ar_main2__textBoxChanged` | ส่วนกลาง `_ar_dealer` — ใช้ร่วมหลายหน้าจอ |

## SMLReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ผิดพลาด โปรดแจ้งกลับเจ้าหน้าที่ |  | 3 | SMLReport/_formReport/_formDesigner.cs:1284 `_loadStandradForm_Click`<br>SMLReport/_formReport/_formDesigner.cs:1291 `_loadStandradForm_Click` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| Save FormDesign Success |  | 2 | SMLReport/_formReport/_formDesigner.cs:1661 `_saveXMLSerialize`<br>SMLReport/_formReport/_formDesigner.cs:3011 `_saveFromToServerButton_Click` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| จำนวน บรรทัดในตาราง ไม่พอสำหรับการพิพม์ กรุณาแก้ไขแบบฟอร์มใหม่ | ผิดพลาด | 2 | SMLReport/_formReport/_formPrint.cs:4606 `_buildDocGroup`<br>SMLReport/_formReport/_formPrint.cs:4750 `_build` | ส่วนกลาง `_formPrint` — ใช้ร่วมหลายหน้าจอ |
| Current Page Background is Largest |  | 1 | SMLReport/_formReport/_formDesigner.cs:2829 `_loadForm` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| Data Read fail. |  | 1 | SMLReport/_report/_view.cs:1044 `_buildReport` | ส่วนกลาง `_view` — ใช้ร่วมหลายหน้าจอ |
| Delete this page. |  | 1 | SMLReport/_formReport/_formDesigner.cs:1070 `_buttonPageRemove_Click` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| Duplicate |  | 1 | SMLReport/_queryDesigner/_linkList.cs:439 `_getAllFieldFormPanel` | ส่วนกลาง `_linkList` — ใช้ร่วมหลายหน้าจอ |
| Failed Print Data on row:{…}<br>{…} |  | 1 | SMLReport/_generate.cs:310 `_getDataObjectLevel` | ส่วนกลาง `_generate` — ใช้ร่วมหลายหน้าจอ |
| Failed Print Total<br>{…} |  | 1 | SMLReport/_generate.cs:345 `_getDataObjectLevel` | ส่วนกลาง `_generate` — ใช้ร่วมหลายหน้าจอ |
| Page not found. |  | 1 | SMLReport/_report/_view.cs:300 `ProcessCmdKey` | ส่วนกลาง `_view` — ใช้ร่วมหลายหน้าจอ |
| Please set Default Printer | แจ้ง | 1 | SMLReport/_report/_view.cs:119 `_view` | ส่วนกลาง `_view` — ใช้ร่วมหลายหน้าจอ |
| Save File to local Drive Success |  | 1 | SMLReport/_formReport/_formDesigner.cs:1705 `_saveToLocalFile` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| have one page |  | 1 | SMLReport/_formReport/_formDesigner.cs:1062 `_buttonPageSort_Click` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| {…}มีรายการนี้อยู่แล้วDuplicate |  | 1 | SMLReport/_queryDesigner/_linkList.cs:288 `_getAllFieldFormPanel` | ส่วนกลาง `_linkList` — ใช้ร่วมหลายหน้าจอ |
| คำสั่งผิดพลาด : {…} |  | 1 | SMLReport/_formReport/_formPrint.cs:4485 `_query` | ส่วนกลาง `_formPrint` — ใช้ร่วมหลายหน้าจอ |
| คุณยังไม่ได้ทำการบันทึกการเปลี่ยนแปลง คุณต้องการที่จะบันทึก หรือไม่ | เตือน | 1 | SMLReport/_formReport/_formDesigner.cs:1091 `_toolStripClose_Click` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| มีการใช้ Form Code ดังกล่าวไปแล้ว |  | 1 | SMLReport/_formReport/_formDesigner.cs:1616 `_saveXMLSerialize` | เริ่มต้น › สร้าง/แก้ไขแบบฟอร์ม |
| แบบฟอร์ม : {…},{…} <br>ได้มีการนำเข้าสู่ระบบไปแล้ว<br>คุณต้องการที่จะเขียนทับเลยหรือไม่ | ถาม | 1 | SMLReport/_ImportFormDesign.cs:116 `_buttonProcess_Click` | เริ่มต้น › เครื่องมือ › นำเข้าแบบฟอร์ม |

## DTSClientDownload

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Date format Error Please select d/M/yyyy or dd/MM/yyyy : Control Panel -> Regional |  | 10 | DTSClientDownload/Program.cs:136 `HookCallback`<br>IMEXBillPaymentGenerate/Program.cs:52 | ส่วนกลาง `Program`, `_main` — ใช้ร่วมหลายหน้าจอ |
| รหัสผู้ใช้ไม่ถูกต้อง หรือรหัสผ่านไม่ถูกต้อง กรุณาลองอีกครั้ง `warning90` | ผิดพลาด | 8 | DTSClientDownload/_dtsLogin.cs:680 `button1_Click`<br>DTSClientDownload/_dtsLogin.cs:728 `button1_Click` | ส่วนกลาง `_dtsLogin`, `_loginForm`, `_selectDatabase.` — ใช้ร่วมหลายหน้าจอ |
| Local Connect | แจ้ง | 7 | DTSClientDownload/Program.cs:200 `HookCallback`<br>SMLActivesync/Program.cs:232 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| Fail Open Excel : {…} |  | 5 | DTSClientDownload/_download_log.cs:467 `_exportButton_Click`<br>DTSClientDownload/_download_log.cs:754 `_exportButton_Click` | ส่วนกลาง `TestOpenTempPathForm`, `_download_log`, `_glFinanceReport` — ใช้ร่วมหลายหน้าจอ |
| คุณต้องการบันทึกข้อมูลหรือไม่ | เตือน | 2 | DTSClientDownload/_dts_item_download.cs:153 `_dts_item_download`<br>DTSClientDownload/_dts_item_download.cs:690 `_saveButton_Click` | ส่วนกลาง `_dts_item_download` — ใช้ร่วมหลายหน้าจอ |
| ดาวน์โหลดข้อมูลสมบูรณ์ !! | แจ้ง | 2 | DTSClientDownload/_dts_item_download.cs:844 `_saveButton_Click`<br>DTSClientDownload/_transDownloadControl.cs:921 `_saveButton_Click` | ส่วนกลาง `_dts_item_download`, `_transDownloadControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบฐานข้อมูลที่ใช้งาน คุณต้องการสร้างฐานข้อมูลใหม่หรือไม่ | เตือน | 2 | DTSClientDownload/_dtsLogin.cs:601<br>MyLib/_databaseManage/_userLogin.cs:166 `_packWebserviceName` | ส่วนกลาง `_dtsLogin`, `_userLogin` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถ เชื่อมต่อกับเครื่องแม่ข่ายได้ | ผิดพลาด | 2 | DTSClientDownload/_serverConfig.cs:193 `_closeButton_Click`<br>DTSClientDownload/_serverConfig.cs:288 `_connectButton_Click` | ส่วนกลาง `_serverConfig` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเชื่อมต่อกับแม่ข่าย CHAMP ได้ | ผิดพลาด | 2 | DTSClientDownload/_dtsLogin.cs:639 `button1_Click`<br>DTSClientDownload/_dtsLogin.cs:723 `button1_Click` | ส่วนกลาง `_dtsLogin` — ใช้ร่วมหลายหน้าจอ |
| Agent Code และ Agent Password ไม่ถูกต้อง | ผิดพลาด | 1 | DTSClientDownload/_serverConfig.cs:118 `_closeButton_Click` | ส่วนกลาง `_serverConfig` — ใช้ร่วมหลายหน้าจอ |
| Exception Occured while releasing object {…} |  | 1 | DTSClientDownload/_download_log.cs:282 `releaseObject` | ส่วนกลาง `_download_log` — ใช้ร่วมหลายหน้าจอ |
| Reset Password | ถาม | 1 | DTSClientDownload/_serverConfig.cs:156 `_closeButton_Click` | ส่วนกลาง `_serverConfig` — ใช้ร่วมหลายหน้าจอ |
| {…}มีอยู่แล้วในระบบ <br>{…} | ผิดพลาด | 1 | DTSClientDownload/_transDownloadControl.cs:762 `_saveButton_Click` | ส่วนกลาง `_transDownloadControl` — ใช้ร่วมหลายหน้าจอ |
| ต้องการจบโปรแกรมจริงหรือไม่ | เตือน | 1 | DTSClientDownload/_dtsMain.cs:57 `OnClosing` | ส่วนกลาง `_dtsMain` — ใช้ร่วมหลายหน้าจอ |
| ต้องการบันทึกข้อมูลหรือไม่ | เตือน | 1 | DTSClientDownload/_transDownloadControl.cs:727 `_saveButton_Click` | ส่วนกลาง `_transDownloadControl` — ใช้ร่วมหลายหน้าจอ |
| บันทึกสำเร็จ ระบบจะปิดจอนี้ให้โดยอัตโนมัติ | แจ้ง | 1 | DTSClientDownload/_serverConfig.cs:199 `_closeButton_Click` | ส่วนกลาง `_serverConfig` — ใช้ร่วมหลายหน้าจอ |
| รหัสสินค้ามีอยู่แล้วในระบบ <br>{…} | ผิดพลาด | 1 | DTSClientDownload/_dts_item_download.cs:717 `_saveButton_Click` | ส่วนกลาง `_dts_item_download` — ใช้ร่วมหลายหน้าจอ |

## SMLBalanceTransfer

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| success |  | 7 | SMLBalanceTransfer/_mainForm.cs:2114 `_checkAkzoItemButton_Click`<br>SMLBalanceTransfer/_mainForm.cs:2162 `_priceExport_Click_1` | ส่วนกลาง `Form1`, `_checkReceiveGUIDControl`, `_icTransControl` — ใช้ร่วมหลายหน้าจอ |
| Connect Success !! |  | 1 | SMLBalanceTransfer/_mainForm.cs:450 `_connectButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Customer Balance ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:1547 `_arBalanceExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Customer Balance Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:1578 `_arBalanceExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Customer Data ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:1591 `_arMasterExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Customer Data Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:1600 `_arMasterExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Inventory Balance ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:1439 `_saveIcBalance_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Inventory Balance Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:1492 `_saveIcBalance_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Inventory Data ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:854 `_exportICButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Inventory Data Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:930 `_exportICButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Inventory Price ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:2130 `_priceExport_Click_1` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Supplier Balance ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:1503 `_apBalanceExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Supplier Balance Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:1535 `_apBalanceExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Supplier Data ?? | ถาม | 1 | SMLBalanceTransfer/_mainForm.cs:1606 `_apMasterExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Export Supplier Data Success |  | 1 | SMLBalanceTransfer/_mainForm.cs:1614 `_apMasterExportButton_Click` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Local Login |  | 1 | SMLBalanceTransfer/Program.cs:22 | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| กำหนดค่าเริ่มต้นไม่สมบูรณ์ |  | 1 | SMLBalanceTransfer/_mainForm.cs:183 `_mainForm` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |

## SMLERPConfig

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่อนุญาติให้แก้ไขข้อมูล |  | 3 | SMLERPConfig/_companyProfile.cs:135 `_saveData`<br>SMLERPConfig/_option.cs:506 `save_data` | เริ่มต้น › รายละเอียดข้อมูลทั่วไป › กำหนดรายละเอียดบริษัท<br>เริ่มต้น › รายละเอียดข้อมูลทั่วไป › กำหนดข้อเลือกพิเศษต่างๆ<br>สินค้า › ข้อมูลสินค้า › ตรวจสอบราคาสินค้า |
| Failed:{…} |  | 2 | SMLERPConfig/_edcConfigForm.cs:73 `OnClickSaveButton`<br>SMLERPConfig/_usbQRDisplayConfigForm.cs:76 `OnClickSaveButton` | เริ่มต้น › รายละเอียดข้อมูลทั่วไป › กำหนดค่าเครื่องรูดบัตรเครดิต<br>เริ่มต้น › รายละเอียดข้อมูลทั่วไป › กำหนดค่าจอแสดงผล QR Code |
| มีการลงทะเบียนไปแล้ว |  | 2 | SMLERPConfig/_dashboardConfigScreen.cs:148 `_registerNewShopButton_Click`<br>SMLERPConfig/_dashboardConfigScreen.cs:252 `_registerOldShowButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| รหัสผ่านไม่สัมพันธ์กัน |  | 2 | SMLERPConfig/_dashboardConfigScreen.cs:105 `_registerButton_Click`<br>SMLERPConfig/_dashboardConfigScreen.cs:347 `_saveEditPassword_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเชื่อมต่อไปยัง www.smlsoft.com ได้ กรุณาตรวจสอบการเชื่อมต่ออินเตอร์เน็ต | ผิดพลาด | 2 | SMLERPConfig/_dashboardConfigScreen.cs:286 `_checkConnectSMLServer`<br>SMLERPConfig/_dashboardConfigScreen.cs:295 `_checkConnectSMLServer` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| {…} ส่งข้อมูลไม่ครบ กรุณาตรวจสอบรายการส่งข้อมูล | ผิดพลาด | 1 | SMLERPConfig/_optionSaleShiftScreen.cs:112 `_createShiftButton_Click` | ส่วนกลาง `_optionSaleShiftScreen` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนรหัสร้านค้า |  | 1 | SMLERPConfig/_dashboardConfigScreen.cs:169 `_checkShopIDButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| กรุณาลงทะเบียนผลิตภัณฑ์ก่อน จึงจะสามารถลงทะเบียนได้ |  | 1 | SMLERPConfig/_dashboardConfigScreen.cs:79 `_registerButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| คุณสามารถใช้งาน รหัสร้านค้า : {…} ได้ | แจ้ง | 1 | SMLERPConfig/_dashboardConfigScreen.cs:180 `_checkShopIDButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| บันทึกการลงทะเบียนสำเร็จ |  | 1 | SMLERPConfig/_dashboardConfigScreen.cs:131 `_registerButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการสร้างรอบการขายใหม่ | เตือน | 1 | SMLERPConfig/_optionSaleShiftScreen.cs:27 `_createShiftButton_Click` | ส่วนกลาง `_optionSaleShiftScreen` — ใช้ร่วมหลายหน้าจอ |
| ระบบสาขาไม่ได้เปิดใช้งาน |  | 1 | SMLERPConfig/_selectMenu.cs:149 `_getObject` | ส่วนกลาง `_selectMenu` — ใช้ร่วมหลายหน้าจอ |
| สร้างรอบการขายสำเร็จ |  | 1 | SMLERPConfig/_optionSaleShiftScreen.cs:211 `_createShiftButton_Click` | ส่วนกลาง `_optionSaleShiftScreen` — ใช้ร่วมหลายหน้าจอ |
| เข้าสู่ระบบสำเร็จ | แจ้ง | 1 | SMLERPConfig/_dashboardConfigScreen.cs:241 `_loginShopButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| เข้าสู่ระบบสำเร็จ กรุณาป้อนรหัสผ่านใหม่ ในช่องรหัสผ่านและยืนยันรหัสผ่านอีกครั้ง | แจ้ง | 1 | SMLERPConfig/_dashboardConfigScreen.cs:229 `_loginShopButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ รหัสร้านค้าและรหัสผ่านดังกล่าว กรุณาลองใหม่อีกครั้ง | ผิดพลาด | 1 | SMLERPConfig/_dashboardConfigScreen.cs:217 `_loginShopButton_Click` | ส่วนกลาง `_dashboardConfigScreen` — ใช้ร่วมหลายหน้าจอ |

## SMLERPGLControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่พบรายการที่ต้องการ |  | 2 | SMLERPGLControl/_glDetailExtra.cs:168 `_createGrid`<br>SMLERPGLControl/_glDetailExtra.cs:174 `_createGrid` | ส่วนกลาง `_glDetailExtra` — ใช้ร่วมหลายหน้าจอ |
| Fail .{…} |  | 1 | SMLERPGLControl/_withHoldingTax.cs:922 `_buttonDelete_Click` | ส่วนกลาง `_withHoldingTax` — ใช้ร่วมหลายหน้าจอ |
| {…}กรุณาบันทึกเลขที่ใบกำกับภาษีก่อนPlease enter tax number |  | 1 | SMLERPGLControl/_vatSale.cs:335 `_updateFirstRow` | ส่วนกลาง `_vatSale` — ใช้ร่วมหลายหน้าจอ |
| {…}ยอดไม่เหมาะสมtax Rate error |  | 1 | SMLERPGLControl/_vatBuy.cs:591 `_updateFirstRow` | ส่วนกลาง `_vatBuy` — ใช้ร่วมหลายหน้าจอ |
| {…}อัตราภาษีไม่เหมาะสมtax Rate error |  | 1 | SMLERPGLControl/_vatBuy.cs:561 `_updateFirstRow` | ส่วนกลาง `_vatBuy` — ใช้ร่วมหลายหน้าจอ |
| ต้องการลบ [{0}] จริงหรือไม่{…} | แจ้ง | 1 | SMLERPGLControl/_recurring.cs:156 `_deleteData` | ส่วนกลาง `_recurring` — ใช้ร่วมหลายหน้าจอ |
| บัญชีนี้ไม่สามารถบันทึกรายการได้ | แจ้ง | 1 | SMLERPGLControl/_glDetail.cs:713 `_searchAccount` | ส่วนกลาง `_glDetail` — ใช้ร่วมหลายหน้าจอ |
| มีการแก้ไขข้อมูลบางส่วน ต้องการยกเลิกจริงหรือไม่ |  | 1 | SMLERPGLControl/_glDetailExtra.cs:44 `OnClosing` | ส่วนกลาง `_glDetailExtra` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้เลือกรายการ |  | 1 | SMLERPGLControl/_recurring.cs:152 `_deleteData` | ส่วนกลาง `_recurring` — ใช้ร่วมหลายหน้าจอ |
| รายการนี้ใช้ไปแล้ว |  | 1 | SMLERPGLControl/_glDetailExtra.cs:137 `_createGrid` | ส่วนกลาง `_glDetailExtra` — ใช้ร่วมหลายหน้าจอ |
| สร้างเรียบร้อย |  | 1 | SMLERPGLControl/_recurring.cs:124 `_recurringActive` | ส่วนกลาง `_recurring` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบ ผังบัญชี : {…} | แจ้ง | 1 | SMLERPGLControl/_glDetail.cs:722 `_searchAccount` | ส่วนกลาง `_glDetail` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรายการ : {…} | แจ้ง | 1 | SMLERPGLControl/_glDetail.cs:682 `_clearAmount` | ส่วนกลาง `_glDetail` — ใช้ร่วมหลายหน้าจอ |

## IMEXControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Success |  | 82 | AkzoGenPo/_podesign.cs:42 `_onClickSaveFromDesign`<br>BCTOSML/Form1.cs:182 `_checkButton_Click` | หน้าจอกลาง — ขึ้นได้ใน 30 เมนู |
| Error: {…} | ผิดพลาด | 5 | IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:84 `LabBalanceLabGrid1__mouseClick`<br>IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:118 `LabBalanceProductGrid1__mouseClick` | เริ่มต้น › ระบบสินค้าคงคลัง › เพิ่มคลังและพื้นที่เก็บอัตโนมัติ |
| กรุณาเลือก Lab ก่อน | เตือน | 2 | IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:95 `LabBalanceLabContainerGrid1__beforeInputCell`<br>IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:279 `_addContainerButton_Click` | ส่วนกลาง `LabBalanceDetailScreenControl` — ใช้ร่วมหลายหน้าจอ |
| {…} ไม่สามารถทำการลบได้ เนื่องจากมีการนำไปใช้งานแล้ว |  | 1 | IMEXControl/QualityControl/ICQCLabList.cs:256 `_dataList__deleteData` | สินค้า › ตรวจสอบคุณภาพสินค้า › ทะเบียนการตรวจสอบคุณภาพ |
| กรุณาเลือกคอลัมน์ให้ครบถ้วน | เตือน | 1 | IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:372 `_importButton_Click` | ส่วนกลาง `LabBalanceDetailScreenControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกสินค้าก่อน | เตือน | 1 | IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:208 `_addLabButton_Click` | ส่วนกลาง `LabBalanceDetailScreenControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกเอกสารที่ต้องการยกเลิก | เตือน | 1 | IMEXControl/QualityControl/_approvedVendorControl.cs:101 `_cancelButton_Click` | สินค้า › ตรวจสอบคุณภาพสินค้า › อนุมัติผู้จำหน่ายและสินค้า |
| ผิดพลาดในการตรวจสอบข้อมูล<br>{…} |  | 1 | IMEXControl/QualityControl/ICQCLabList.cs:261 `_dataList__deleteData` | สินค้า › ตรวจสอบคุณภาพสินค้า › ทะเบียนการตรวจสอบคุณภาพ |
| มีหมายเลข Lab No: {…} ในระบบแล้ว กรุณาเปลี่ยนใหม่ |  | 1 | IMEXControl/QualityControl/ICQCProductReceive.cs:145 `_saveData` | สินค้า › ตรวจสอบคุณภาพสินค้า › บันทึกรับสินค้า |
| แบ่งภาชนะไม่สมบูรณ์ กรุณาตรวจสอบการแบ่งภาชนะบรรจุ |  | 1 | IMEXControl/QualityControl/PackingSize/ICQCPurchaesPackingSizeSplit.cs:284 `saveData` | สินค้า › ตรวจสอบคุณภาพสินค้า › กำหนดจำนวนภาชนะ(Container) |
| ไม่พบเอกสาร: {…} | เตือน | 1 | IMEXControl/QualityControl/LabBeginningBalance/LabBalanceDetailScreenControl.cs:188 `LabBalanceScreenTop1__docNoSelected` | ส่วนกลาง `LabBalanceDetailScreenControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถยกเลิกเอกสารที่ยกเลิกแล้ว | เตือน | 1 | IMEXControl/QualityControl/_approvedVendorControl.cs:70 `_cancelButton_Click` | สินค้า › ตรวจสอบคุณภาพสินค้า › อนุมัติผู้จำหน่ายและสินค้า |

## SMLActivesync

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| {…}:{…} |  | 6 | MyLib/_databaseManage/_genQueryControl.cs:85 `toolStripButton1_Click`<br>MyLib/_myGrid.cs:2429 `_cellUpdate` | เริ่มต้น › เครื่องมือ › สร้างคำสั่ง Query |
| Select Branch Code to Resync |  | 2 | SMLActivesync/_reSyncReciveControl.cs:85 `_processButton_Click`<br>SMLActivesync/_reSyncSendControl.cs:89 `_processButton_Click` | ส่วนกลาง `_reSyncReciveControl`, `_reSyncSendControl` — ใช้ร่วมหลายหน้าจอ |
| error : {…} |  | 2 | SMLActivesync/_branchSyncControl.cs:78 `_branchSyncControl`<br>SMLActivesync/_tableSyncControl.cs:346 `_tableSyncControl` | ส่วนกลาง `_branchSyncControl`, `_tableSyncControl` — ใช้ร่วมหลายหน้าจอ |
| รหัสใหม่ซ้ำ |  | 2 | SMLActivesync/_changeMasterCode.cs:95 `_changeMasterCode`<br>SMLERPGlobal/_changeCode/_changeApArCodeUserControl.cs:423 | เริ่มต้น › เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสเจ้าหนี้<br>เริ่มต้น › เครื่องมือ › เปลี่ยนรหัส › เปลี่ยนรหัสลูกหนี้ |
| Confirm To Clear Log : {…}({…}) | ถาม | 1 | SMLActivesync/_syncStatusControl.cs:169 `_clearLogButton_Click` | ส่วนกลาง `_syncStatusControl` — ใช้ร่วมหลายหน้าจอ |
| Delete Log {…}({…}) Success | แจ้ง | 1 | SMLActivesync/_syncStatusControl.cs:181 `_clearLogButton_Click` | ส่วนกลาง `_syncStatusControl` — ใช้ร่วมหลายหน้าจอ |
| Resend to {…}({…}) |  | 1 | SMLActivesync/_reSyncSendControl.cs:93 `_processButton_Click` | ส่วนกลาง `_reSyncSendControl` — ใช้ร่วมหลายหน้าจอ |
| Resend {…}({…}) Success | แจ้ง | 1 | SMLActivesync/_reSyncSendControl.cs:132 `_processButton_Click` | ส่วนกลาง `_reSyncSendControl` — ใช้ร่วมหลายหน้าจอ |
| Reset Receive From {…}({…}) |  | 1 | SMLActivesync/_reSyncReciveControl.cs:89 `_processButton_Click` | ส่วนกลาง `_reSyncReciveControl` — ใช้ร่วมหลายหน้าจอ |
| Reset Receive From {…}({…}) Success | แจ้ง | 1 | SMLActivesync/_reSyncReciveControl.cs:128 `_processButton_Click` | ส่วนกลาง `_reSyncReciveControl` — ใช้ร่วมหลายหน้าจอ |
| ยกเลิกการส่งข้อมูล : {…}({…}) | ถาม | 1 | SMLActivesync/_syncStatusControl.cs:190 `_clearSendDataButton_Click` | ส่วนกลาง `_syncStatusControl` — ใช้ร่วมหลายหน้าจอ |

## SMLERPASSET

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ท่านอยู่ในหัวข้อตรวจสอบข้อมูล<br>ถ้าต้องการแก้ไขให้กด Double Click ที่ข้อมูล `warning2` | แจ้ง | 22 | MyLib/_manageMasterCodeFull.cs:280 `_finish`<br>SMLERPASSET/_as_list.cs:749 `ProcessCmdKey` | หน้าจอกลาง — ขึ้นได้ใน 83 เมนู |
| ไม่พบ | แจ้ง | 8 | SMLERPASSET/_as_maintain.cs:524 `_search`<br>SMLERPASSET/_as_sale.cs:628 `_search` | ค่าเสื่อม › บันทึกการซ่อมบำรุงสินทรัพย์<br>บัญชี › ผังบัญชี › รายละเอียดผังบัญชี |
| {…}วันที่สิ้นสุดต้องมากกว่าหรือเท่ากับวันที่เริ่มต้นเท่านั้นEnddate much more than or equal to Begindate |  | 5 | SMLERPASSET/_display/_depreciateByDay.cs:118 `_process`<br>SMLERPASSET/_display/_depreciateByMonth.cs:118 `_process` | ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายวัน<br>ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายเดือน<br>ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายปี<br>(+1 เมนู) |
| {…}ไม่พบข้อมูลที่ต้องการNot Found Data |  | 3 | SMLERPASSET/_display/_depreciateByDay.cs:203 `_process`<br>SMLERPASSET/_display/_depreciateByMonth.cs:202 `_process` | ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายวัน<br>ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายเดือน<br>ค่าเสื่อม › แสดงค่าเสื่อมราคาสินทรัพย์รายปี |
| {…}กรุณาบันทึก วันที่เริ่มต้น และ วันที่สิ้นสุด ก่อนPlease enter startdate and enddate |  | 2 | SMLERPASSET/_report/_depreciate/_condition.cs:75 `_buttonOk_Click`<br>SMLERPASSET/_report/_depreciate/_report.cs:540 `_getDepreciateForProcess` | ค่าเสื่อม › รายงาน › รายงานค่าเสื่อมราคาสินทรัพย์ |
| {…}กรุณาบันทึกรหัสสินทรัพย์ก่อนPlease input asset code |  | 2 | SMLERPASSET/_controls/_maintenanceGrid.cs:125 `_maintenanceGrid`<br>SMLERPASSET/_controls/_saleGrid.cs:123 `_saleGrid` | ส่วนกลาง `_maintenanceGrid`, `_saleGrid` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนข้อมูล <br>{…}<br>{…} | ผิดพลาด | 2 | SMLERPASSET/_as_transfer.cs:133 `_glDeleteQuery`<br>SMLERPGL/_glTransControl.cs:341 `_saveData` | ค่าเสื่อม › โอนข้อมูลเข้าระบบบัญชี<br>บัญชี › ประมวลผลสิ้นงวด<br>บัญชี › ประมวลผลสิ้นปี |
| {…}กรุณาบันทึก มูลค่าที่คิดค่าเสื่อม ราคาซาก และ อายุการใช้งาน ก่อน แล้วโปรแกรมจะทำการคำนวณอัตราค่าเสื่อมให้โดยอัตโนมัติPlease enter calcvalue deadvalue and age, Program will automatic calculate ratevalue |  | 1 | SMLERPASSET/_as_list.cs:389 `_screenDepreciation__textBoxChanged` | ค่าเสื่อม › รายละเอียดสินทรัพย์ › ข้อมูลสินทรัพย์ |
| {…}กรุณาบันทึก อายุการใช้งาน ก่อน แล้วโปรแกรมจะทำการคำนวณอัตราค่าเสื่อมให้โดยอัตโนมัติPlease enter age, Program will automatic calculate ratevalue |  | 1 | SMLERPASSET/_as_list.cs:381 `_screenDepreciation__textBoxChanged` | ค่าเสื่อม › รายละเอียดสินทรัพย์ › ข้อมูลสินทรัพย์ |
| {…}วันที่สิ้นสุดคิดค่าเสื่อมต้องมากกว่าหรือเท่ากับวันที่เริ่มคิดค่าเสื่อมเท่านั้นStopCalcDate much more than or equal to StartCaclDate |  | 1 | SMLERPASSET/_as_list.cs:1322 `_search` | ค่าเสื่อม › รายละเอียดสินทรัพย์ › ข้อมูลสินทรัพย์ |

## SMLTransferDataPOS

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ยืนยันการโอนข้อมูลการขาย | ถาม | 3 | SMLTransferDataPOS/_earthSaleTransferUserControl.cs:1346 `_saveButton_Click`<br>SMLTransferDataPOS/_posDataTransfer.cs:567 `_checkDuplicate` | ส่วนกลาง `_earthSaleTransferUserControl`, `_posDataTransfer`, `_siriPosDataTransfer` — ใช้ร่วมหลายหน้าจอ |
| Process Success !! | แจ้ง | 1 | SMLTransferDataPOS/_icTransfer.cs:141 `_icTransfer` | ส่วนกลาง `_icTransfer` — ใช้ร่วมหลายหน้าจอ |
| Process Success !!<br> Error : {…} Record | แจ้ง | 1 | SMLTransferDataPOS/_icTransfer.cs:145 `_icTransfer` | ส่วนกลาง `_icTransfer` — ใช้ร่วมหลายหน้าจอ |
| Process is Running... |  | 1 | SMLTransferDataPOS/_icTransfer.cs:1426 `_processToolStripButton_Click` | ส่วนกลาง `_icTransfer` — ใช้ร่วมหลายหน้าจอ |
| error query{…} |  | 1 | SMLTransferDataPOS/_earthTransferTransectionControl.cs:290 `_earthTransferTransectionControl` | ส่วนกลาง `_earthTransferTransectionControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาป้อนข้อมูล {…} | ผิดพลาด | 1 | SMLTransferDataPOS/_posSaleControl.cs:898 | ส่วนกลาง `_posSaleControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณาเลือกรูปแบบเอกสารและลูกหนี้ก่อนทำรายการ |  | 1 | SMLTransferDataPOS/_posDataTransfer.cs:563 `_checkDuplicate` | ส่วนกลาง `_posDataTransfer` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการถ่ายโอนข้อมูล | เตือน | 1 | SMLTransferDataPOS/_icTransfer.cs:1411 `_processToolStripButton_Click` | ส่วนกลาง `_icTransfer` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการโอนข้อมูล | ถาม | 1 | SMLTransferDataPOS/_earthTransferTransectionControl.cs:296 `_earthTransferTransectionControl` | ส่วนกลาง `_earthTransferTransectionControl` — ใช้ร่วมหลายหน้าจอ |

## AkzoGenPo

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Connect Fail | ผิดพลาด | 1 | AkzoGenPo/_poConfigForm.cs:52 `_poConfigForm` | ส่วนกลาง `_poConfigForm` — ใช้ร่วมหลายหน้าจอ |
| Print Fail |  | 1 | AkzoGenPo/_mainScreen.cs:87 `_mainScreen` | ส่วนกลาง `_mainScreen` — ใช้ร่วมหลายหน้าจอ |
| Query Button |  | 1 | AkzoGenPo/_podesign.cs:104 `_onClickQueryButton` | ส่วนกลาง `_podesign` — ใช้ร่วมหลายหน้าจอ |
| Save PO Config Success. <br>this Screen will be close. | แจ้ง | 1 | AkzoGenPo/_poConfigForm.cs:74 `_poConfigForm` | ส่วนกลาง `_poConfigForm` — ใช้ร่วมหลายหน้าจอ |
| การพิมพ์ {…} เสร็จสมบุรณ์ | แจ้ง | 1 | AkzoGenPo/_mainScreen.cs:55 `_mainScreen` | ส่วนกลาง `_mainScreen` — ใช้ร่วมหลายหน้าจอ |
| คุณต้องการ พิมพ์รายการ {…}หรือไม่ | ถาม | 1 | AkzoGenPo/_mainScreen.cs:49 `_mainScreen` | ส่วนกลาง `_mainScreen` — ใช้ร่วมหลายหน้าจอ |
| คุณต้องการที่จะส่ง Order Email ไปยัง Agent หรือไม่ <br> {…} | แจ้ง | 1 | AkzoGenPo/_mainScreen.cs:69 `_mainScreen` | ส่วนกลาง `_mainScreen` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถติดต่อกับฐานข้อมูลได้ กรุณาตรวจสอบใหม่ |  | 1 | AkzoGenPo/_loginForm.cs:49 `_loginButton_Click` | ส่วนกลาง `_loginForm` — ใช้ร่วมหลายหน้าจอ |

## SMLERPTransferControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบรายการต่อไปนี้<br>{…} |  | 2 | SMLERPTransferControl/_saleImportFromPOSSaleReport.cs:94 `_saveSaleInvoiceButton_Click`<br>SMLERPTransferControl/_saleImportFromStockCountDiff.cs:65 `_saveSaleButton_Click` | Data › สร้างรายการขายจากสรุปการขาย POS<br>Data › สร้างการขายจากผลต่างจากการตรวจนับ |
| ไม่พบข้อมูลลูกค้า |  | 2 | SMLERPTransferControl/_saleImportFromPOSSaleReport.cs:77 `_processButton_Click`<br>SMLPosClient/screen/_posPayForm.cs:1615 `_buttonCreditSave_Click` | Data › สร้างรายการขายจากสรุปการขาย POS |
| กรุณากรอกข้อมูลให้ครบถ้วน |  | 1 | SMLERPTransferControl/_salesItemsFromPurchaseBill.cs:139 `_importButton_Click` | Data › สร้างรายการขายจาก บิลซื้อ |
| ยืนยันการนำผลต่างการตรวจนับ ไปสร้างเป็นรายการขายสินค้า | ถาม | 1 | SMLERPTransferControl/_saleImportFromStockCountDiff.cs:70 `_saveSaleButton_Click` | Data › สร้างการขายจากผลต่างจากการตรวจนับ |
| ยืนยันการสร้างรายการขายสินค้า | ถาม | 1 | SMLERPTransferControl/_saleImportFromPOSSaleReport.cs:99 `_saveSaleInvoiceButton_Click` | Data › สร้างรายการขายจากสรุปการขาย POS |
| ไม่พบรายกายผลต่างจาการตรวจนับ |  | 1 | SMLERPTransferControl/_saleImportFromStockCountDiff.cs:58 `_saveSaleButton_Click` | Data › สร้างการขายจากผลต่างจากการตรวจนับ |
| ไม่พบรายการ |  | 1 | SMLERPTransferControl/_saleImportFromPOSSaleReport.cs:87 `_saveSaleInvoiceButton_Click` | Data › สร้างรายการขายจากสรุปการขาย POS |
| ไม่สามารถเชื่อมต่อไปยัง {…} ได้ |  | 1 | SMLERPTransferControl/_saleImportFromPOSSaleReport.cs:71 `_processButton_Click` | Data › สร้างรายการขายจากสรุปการขาย POS |

## SMLSyncCheckingTools

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Login Failed |  | 5 | SMLExecuteQueryTools/Form1.cs:75 `_desConnectButton_Click`<br>SMLSyncCheckingTools/Form1.cs:184 `_sourceConnectButton_Click` | ส่วนกลาง `Form1`, `_mainForm1` — ใช้ร่วมหลายหน้าจอ |
| Pleage Connect Data Center & Data Client |  | 1 | SMLSyncCheckingTools/_checkReceiveGUIDControl.cs:200 `startCheckButton_Click` | ส่วนกลาง `_checkReceiveGUIDControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณกรอกข้อมูลการเชื่อมต่อต้นทางและปลายทางให้ครบถ้วน |  | 1 | SMLSyncCheckingTools/Form1.cs:808 `_saveProfilebutton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| กรุณา Disconnect server ปลายทางก่อน! |  | 1 | SMLSyncCheckingTools/Form1.cs:124 `_sourceConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| บันทึก profile เรียบร้อยแล้ว |  | 1 | SMLSyncCheckingTools/Form1.cs:1026 `_saveProfilebutton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่มีการบันทึก profile กรุณากรอกชื่อ profile และกรอกข้อมูลการเชื่อมต่อแล้วกดปุ่ม save เพื่อบันทึกข้อมูล |  | 1 | SMLSyncCheckingTools/Form1.cs:1124 `_selectprofile_MouseClick` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสสาขาที่ server ต้นทาง |  | 1 | SMLSyncCheckingTools/Form1.cs:326 `_desConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบรหัสสาขาที่ server ปลายทาง |  | 1 | SMLSyncCheckingTools/Form1.cs:337 `_desConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLERPAP

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ต้องการนำเข้าข้อมูลที่ได้เลือกไว้หรือไม่ |  | 6 | BRInterface/saletools/_import_so_invoice.cs:466 `_importButton_Click`<br>BRInterface/saletools/import_request_transfer.cs:293 `_importButton_Click` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า)<br>(+1 เมนู) |
| กรุณาเลือกรูปแบบเอกสาร คลัง และ ที่เก็บ ก่อน Import ข้อมูล | ผิดพลาด | 3 | SMLERPAP/_apPartnerBillImport.cs:232 `_importButton_Click`<br>SMLERPAP/_apPartnerBillImportAddDebt.cs:220 `_importButton_Click` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) |
| นำเข้าข้อมูลสำเร็จแล้ว |  | 3 | SMLERPAP/_apPartnerBillImport.cs:457 `_importButton_Click`<br>SMLERPAP/_apPartnerBillImportAddDebt.cs:388 `_importButton_Click` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) |
| ไม่พบเอกสารที่สามารถ import ได้จากคู่ค้านี้ | ผิดพลาด | 3 | SMLERPAP/_apPartnerBillImport.cs:192 `_apPartnerBillImport`<br>SMLERPAP/_apPartnerBillImportAddDebt.cs:180 `_apPartnerBillImportAddDebt` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) |
| ไม่สามารถเชื่อมต่อกับคู่ค้าได้ กรุณาตรวจสอบข้อมูล config ในเมนู คู่ค้า 6.17 | ผิดพลาด | 3 | SMLERPAP/_apPartnerBillImport.cs:197 `_apPartnerBillImport`<br>SMLERPAP/_apPartnerBillImportAddDebt.cs:185 `_apPartnerBillImportAddDebt` | เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(เพิ่มหนี้)<br>เจ้าหนี้ › คู่ค้า › นำเข้าข้อมูลจากคู่ค้า(ส่งคืนสินค้า) |
| กรุณาป้อนเลขที่เอกสาร และเจ้าหนี้ |  | 2 | SMLERPAP/_ap_debt_billing.cs:81 `_printData`<br>SMLERPAP/_ap_pay_bill.cs:86 `_printData` | เจ้าหนี้ › จ่ายชำระหนี้ (เจ้าหนี้)<br>เจ้าหนี้ › ใบรับวางบิล (เจ้าหนี้) |

## SMLFastReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| บันทึกข้อมูลเรียบร้อย |  | 5 | SMLBarcodeManage/_itemBarcodePrint.cs:1797 `_formatSaveButton_Click`<br>SMLERPGlobal/_userGroupWarehouseShelf.cs:264 `_userGroupNewData` | หน้าจอกลาง — ขึ้นได้ใน 136 เมนู |
| Save XML Success | แจ้ง | 2 | SMLFastReport/_designer.cs:641 `_saveXMLButton_Click`<br>SMLPOSControl/_designer/_clientDesign.cs:1381 `_saveXMLButton_Click` | หน้าจอกลาง — ขึ้นได้ใน 134 เมนู |
| กรุณากรอกข้อมูล <br>{…} | ผิดพลาด | 1 | SMLFastReport/_saveForm.cs:67 `_buttonSave_Click_1` | ส่วนกลาง `_saveForm` — ใช้ร่วมหลายหน้าจอ |
| รายงานนี้อยู่ในโหมดเปิดอ่านได้อย่างเดียว | ผิดพลาด | 1 | SMLFastReport/_designer.cs:563 `_checkReportReadOnly` | หน้าจอกลาง — ขึ้นได้ใน 133 เมนู |
| รายงานนี้ไม่อนุญาติให้แก้ไข | ผิดพลาด | 1 | SMLFastReport/_designer.cs:523 `_buttonSaveReport_Click` | หน้าจอกลาง — ขึ้นได้ใน 133 เมนู |
| ไม่พบข้อมูล หรือคำสั่งผิดพลาด : {…} |  | 1 | SMLFastReport/_genReport.cs:223 `_init` | ส่วนกลาง `_genReport` — ใช้ร่วมหลายหน้าจอ |

## SMLProcess

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ข้อมูลผิดพลาด ไม่มีข้อมูล ค่าจ้าง ในวันที่ {…}<br>Message : {…} |  | 3 | SMLProcess/_payrollProcess.cs:108 `_processTranShortOfWork`<br>SMLProcess/_payrollProcess.cs:310 `_processArriveLate` | ส่วนกลาง `_payrollProcess` — ใช้ร่วมหลายหน้าจอ |
| Field To Process Chq {…} on Doc No {…}<br>{…} |  | 2 | SMLProcess/_docFlowThread.cs:4279 `__processChqWallet`<br>SMLProcess/_docFlowThread.cs:4289 `__processChqWallet` | ส่วนกลาง `_docFlowThread` — ใช้ร่วมหลายหน้าจอ |
| ISNULL ไม่สามารถใช้ได้กับ PostgreSQL |  | 2 | SMLProcess/_cbProcess.cs:71 `_queryCBStream`<br>SMLProcess/_icProcess.cs:420 `_queryRemainStream` | ส่วนกลาง `_cbProcess`, `_icProcess` — ใช้ร่วมหลายหน้าจอ |
| Process Chq Exception: {…} |  | 1 | SMLProcess/_docFlowThread.cs:4310 `__processChqWallet` | ส่วนกลาง `_docFlowThread` — ใช้ร่วมหลายหน้าจอ |
| xxxxx |  | 1 | SMLProcess/_asProcess.cs:2386 | ส่วนกลาง `_asProcess` — ใช้ร่วมหลายหน้าจอ |
| ข้อมูลผิดพลาด ไม่มีข้อมูล ค่าจ้าง ในวันที่ {…}<br>Message: {…} |  | 1 | SMLProcess/_payrollProcess.cs:209 `_processLeave` | ส่วนกลาง `_payrollProcess` — ใช้ร่วมหลายหน้าจอ |

## BRInterface

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| This program need FrameWork 2.0 up, if your computer have frame work 1.1 please remove first. |  | 23 | BRInterface/Program.cs:32<br>DTSClientDownload/Program.cs:96 `HookCallback` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| Limit user please wait. |  | 18 | BRInterface/_mainForm.cs:38 `_activeMenu`<br>EarthStockManage/_mainForm.cs:47 `_activeMenu` | ส่วนกลาง `_mainForm`, `_menuForm` — ใช้ร่วมหลายหน้าจอ |
| GUID Error |  | 17 | BRInterface/Program.cs:136<br>ICCManage/Program.cs:277 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| ต้องการเข้าทดสอบระบบ (ไม่ถามรหัสผ่าน) | แจ้ง | 12 | BRInterface/Program.cs:91<br>DTSClientDownload/Program.cs:166 `HookCallback` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |

## SMLBarcodeManage

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| กรุณากรอกข้อมูลต่อไปนี้ <br>{…} | ผิดพลาด | 1 | SMLBarcodeManage/_itemBarcodePrint.cs:1775 `_formatSaveButton_Click` | สินค้า › ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป |
| ขนาด Label ไม่สัมพันธ์กับขนาดกระดาษ |  | 1 | SMLBarcodeManage/_itemBarcodePrint.cs:1021 `_printForm` | สินค้า › ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป |
| คุณต้องการลบรูปแบบนี้หรือไม่ | ถาม | 1 | SMLBarcodeManage/_itemBarcodePrint.cs:1809 `_formatDeleteButton_Click` | สินค้า › ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป |
| ลบข้อมูลสำเร็จ |  | 1 | SMLBarcodeManage/_itemBarcodePrint.cs:1816 `_formatDeleteButton_Click` | สินค้า › ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป |

## SMLDatabaseDesign

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Can't open this file |  | 2 | SMLDatabaseDesign/Form1.cs:260 `_open_Click`<br>SMLDatabaseDesign/Form1.cs:282 `_open_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| Connect success... |  | 1 | SMLDatabaseDesign/reverseEnginnerDatabase.cs:125 `_connectButton_Click` | ส่วนกลาง `reverseEnginnerDatabase` — ใช้ร่วมหลายหน้าจอ |
| File name error |  | 1 | SMLDatabaseDesign/Form1.cs:577 `_createScript_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| ͧźԧ | เตือน | 1 | SMLDatabaseDesign/tableEdit.cs:516 `_removeIndexButton_Click` | ส่วนกลาง `tableEdit` — ใช้ร่วมหลายหน้าจอ |

## SMLERPICInfo

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Image Error : {…} |  | 1 | SMLERPICInfo/_ic_inventory_information_2.cs:1442 `_saveButton_Click` | MIS › หน้าจอสำหรับผู้บริหาร |
| กรุณาเลือกคลังสินค้า |  | 1 | SMLERPICInfo/_stkMovement.cs:191 `_process` | สินค้า › วิเคราะห์ข้อมูล › เคลื่อนไหวสินค้า<br>สินค้า › วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ<br>สินค้า › วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ (รวมต้นทุนแฝง) |
| กรุณาเลือกที่เก็บสินค้า |  | 1 | SMLERPICInfo/_stkMovement.cs:200 `_process` | สินค้า › วิเคราะห์ข้อมูล › เคลื่อนไหวสินค้า<br>สินค้า › วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ<br>สินค้า › วิเคราะห์ข้อมูล › บัญชีคุมพิเศษ (รวมต้นทุนแฝง) |
| ยืนยันการปรับปรุงข้อมูล | ถาม | 1 | SMLERPICInfo/_icTransectionCheck.cs:392 `_updateButton_Click` | เริ่มต้น › เครื่องมือ › ระบบข้อมูล › ตรวจสอบและปรับปรุงข้อมูล |

## SMLERPSO

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่พบรายละเอียดากรจัดส่งสินค้า คุณต้องการให้ระบบดึงข้อมูลจากที่อยู่ลูกค้าหรือไม่ |  | 4 | SMLERPSO/mobillyst_tms/_create_cn_delivery_order.cs:110 `LoadInvoice`<br>SMLERPSO/mobillyst_tms/_create_delivery_order.cs:171 `LoadInvoice` | Mobillyst TMS › สร้างคำสั่งส่ง-จากการรับคืนสินค้า<br>Mobillyst TMS › สร้างคำสั่งส่งสินค้า<br>Mobillyst TMS › สร้างคำสั่งส่ง-จากการสั่งซื้อสินค้า<br>(+1 เมนู) |
| Send Api Failed : {…} |  | 3 | SMLERPSO/mobillyst_tms/_create_delivery_order.cs:244 `CreateDeliveryOrder`<br>SMLERPSO/mobillyst_tms/_delivery_order_list.cs:217 `saveData` | Mobillyst TMS › รายการสั่งส่งสินค้า<br>Mobillyst TMS › สร้างคำสั่งส่งสินค้า |
| ยืนยันการบันทึกข้อมูล |  | 3 | IMEXControl/QualityControl/ICQCProductReceive.cs:279 `_saveButton_Click`<br>SMLERPSO/mobillyst_tms/_create_delivery_order.cs:214 `CreateDeliveryOrder` | สินค้า › ตรวจสอบคุณภาพสินค้า › บันทึกรับสินค้า<br>Mobillyst TMS › สร้างคำสั่งส่งสินค้า<br>Mobillyst TMS › รายการสั่งส่งสินค้า |
| ยกเลิกเอกสารเรียบร้อยแล้ว | แจ้ง | 1 | SMLERPSO/mobillyst_tms/_delivery_order_list.cs:115 `_cancelButton_Click` | Mobillyst TMS › รายการสั่งส่งสินค้า |

## SMLETaxInvoice

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Error Get Data |  | 1 | SMLETaxInvoice/_sendETaxControl.cs:272 `_processButton_Click` | ขาย › ส่งข้อมูล e-Tax |
| Error out of Memory. Please Close program and try again or wait 5 minute |  | 1 | SMLETaxInvoice/_sendETaxControl.cs:211 `_sendETaxButton_Click` | ขาย › ส่งข้อมูล e-Tax |
| ดำเนินการส่ง e-Tax สำเร็จ |  | 1 | SMLETaxInvoice/_sendETaxControl.cs:231 `_sendETaxButton_Click` | ขาย › ส่งข้อมูล e-Tax |
| ยืนยันการส่งข้อมูล e-Tax |  | 1 | SMLETaxInvoice/_sendETaxControl.cs:119 `_sendETaxButton_Click` | ขาย › ส่งข้อมูล e-Tax |

## SMLMDBImportConfig

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| เชื่อมต่อสำเร็จ |  | 4 | DTSClientDownload/_serverConfig.cs:284 `_connectButton_Click`<br>SMLDataTransfer/_serverConnectionControl.cs:190 `connectButton_Click` | ส่วนกลาง `_configForm`, `_serverConfig`, `_serverConnectionControl` — ใช้ร่วมหลายหน้าจอ |
| กรุณากรอกข้อมูลให้ครบถ้วน{…} |  | 1 | SMLMDBImportConfig/_configForm.cs:331 `_btnSave_Click` | ส่วนกลาง `_configForm` — ใช้ร่วมหลายหน้าจอ |
| บันทึกเรียบร้อยแล้ว |  | 1 | SMLMDBImportConfig/_configForm.cs:326 `_btnSave_Click` | ส่วนกลาง `_configForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเชื่อมต่อได้กรุณาตรวจสอบข้อมูลอีกครั้ง |  | 1 | SMLMDBImportConfig/_configForm.cs:189 `_btnTestconfig2_Click` | ส่วนกลาง `_configForm` — ใช้ร่วมหลายหน้าจอ |

## SMLOffTakeSalesAdmin

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Error 1 {…} |  | 4 | SMLOffTakeSalesAdmin/_importDataChannelMasterControl.cs:186 `_saveToDatabase`<br>SMLOffTakeSalesAdmin/_importDataProductMasterControl.cs:163 `_saveToDatabase` | ส่วนกลาง `_importDataChannelMasterControl`, `_importDataProductMasterControl`, `_importDataRDM_Master` — ใช้ร่วมหลายหน้าจอ |
| Error >> {…} |  | 3 | SMLOffTakeSalesAdmin/_importDataChannelMasterControl.cs:158 `_saveToDatabase`<br>SMLOffTakeSalesAdmin/_importDataProductMasterControl.cs:135 `_saveToDatabase` | ส่วนกลาง `_importDataChannelMasterControl`, `_importDataProductMasterControl`, `_importDataRDM_Master` — ใช้ร่วมหลายหน้าจอ |
| เลือก File ก่อน |  | 3 | SMLOffTakeSalesAdmin/_importDataChannelMasterControl.cs:163 `_saveToDatabase`<br>SMLOffTakeSalesAdmin/_importDataProductMasterControl.cs:140 `_saveToDatabase` | ส่วนกลาง `_importDataChannelMasterControl`, `_importDataProductMasterControl`, `_importDataRDM_Master` — ใช้ร่วมหลายหน้าจอ |
| warning126{…} `warning126` | แจ้ง | 1 | SMLOffTakeSalesAdmin/_mainScreen.cs:341 `_activeMenu` | ส่วนกลาง `_mainScreen` — ใช้ร่วมหลายหน้าจอ |

## SMLTransfer

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Debug | ถาม | 1 | SMLTransfer/_mainForm1.cs:41 `_mainForm1` | ส่วนกลาง `_mainForm1` — ใช้ร่วมหลายหน้าจอ |
| Failed {…}<br>{…} |  | 1 | SMLTransfer/_mainForm1.cs:1818 | ส่วนกลาง `_mainForm1` — ใช้ร่วมหลายหน้าจอ |
| Process Success |  | 1 | SMLTransfer/_mainForm1.cs:1403 `_startTransferMasterButton_Click` | ส่วนกลาง `_mainForm1` — ใช้ร่วมหลายหน้าจอ |
| ยังไม่ได้เชื่อมต่อฐานข้อมูล |  | 1 | SMLTransfer/_mainForm1.cs:1894 `tabControl1_SelectedIndexChanged` | ส่วนกลาง `_mainForm1` — ใช้ร่วมหลายหน้าจอ |

## SMLAccount

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Proxy Setting | แจ้ง | 1 | SMLAccount/Program.cs:302 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| Select Branch : {…}({…}) |  | 1 | SMLAccount/Program.cs:474 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| คุณต้องการลบทางลัด {…} หรือไม่ | เตือน | 1 | SMLAccount/_mainShortcut.cs:146 `_panelLabelName_Paint` | เริ่มต้น › เครื่องมือ › หน้าจอเริ่มต้น |

## SMLERPICReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| error : {…}<br>Length: {…}:{…} |  | 1 | SMLERPICReport/_report_ic_stk_movement.cs:88 `_report_ic_stk_movement` | สินค้า › รายงานสรุป › รายงานบัญชีคุมพิเศษสินค้า<br>สินค้า › รายงานวิเคราะห์ › รายงานเคลื่อนไหวสินค้า |
| error : {…}<br>{…} |  | 1 | SMLERPICReport/_report_ic_product_and_material.cs:110 `_getDataObject` | สินค้า › รายงานสรุป › รายงานสินค้าและวัตถุดิบ |
| ผิดพลาด คำสั่ง Query |  | 1 | SMLERPICReport/_report_ic_summary.cs:839 `_whPack` | หน้าจอกลาง — ขึ้นได้ใน 8 เมนู |

## SMLGetPrice

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| รหัสไม่ตรงกัน |  | 2 | SMLGetPrice/_validForm.cs:32 `_okButton_Click`<br>SMLTOBC/_validForm.cs:32 `_okButton_Click` | ส่วนกลาง `_validForm` — ใช้ร่วมหลายหน้าจอ |
| มีราคาเปลี่ยนแปลง กรุณาตรวจสอบ และกดปุ่มเปลี่ยนให้เป็นราคาใหม่ |  | 1 | SMLGetPrice/Form1.cs:326 `timer1_Tick` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| ไม่มีราคาเปลี่ยนแปลง |  | 1 | SMLGetPrice/Form1.cs:322 `timer1_Tick` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLICIAdmin

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Auto Login | แจ้ง | 1 | SMLICIAdmin/Program.cs:71 | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| Check ok |  | 1 | SMLICIAdmin/_importFcolorDataControlScreenfile.cs:745 | ส่วนกลาง `_importFcolorDataControlScreenfile` — ใช้ร่วมหลายหน้าจอ |
| Error {…} |  | 1 | SMLICIAdmin/_importFcolorDataControlScreenfile.cs:751 | ส่วนกลาง `_importFcolorDataControlScreenfile` — ใช้ร่วมหลายหน้าจอ |

## SMLQRPayment

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Failed :{…} |  | 1 | SMLQRPayment/_edcPaymentControl.cs:91 `_edcPaymentControl` | ส่วนกลาง `_edcPaymentControl` — ใช้ร่วมหลายหน้าจอ |
| Not Found Payment |  | 1 | SMLQRPayment/BCELQRPay.cs:56 `_checkPaymentButton_Click` | ส่วนกลาง `BCELQRPay` — ใช้ร่วมหลายหน้าจอ |
| Payment Success Ref: {…} |  | 1 | SMLQRPayment/BCELQRPay.cs:52 `_checkPaymentButton_Click` | ส่วนกลาง `BCELQRPay` — ใช้ร่วมหลายหน้าจอ |

## SMLStockMovementTransfer

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Connect Failed |  | 1 | SMLStockMovementTransfer/Form1.cs:349 `_sourceConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| Connect Failed : {…} |  | 1 | SMLStockMovementTransfer/Form1.cs:432 `_desConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| Please Connection Server |  | 1 | SMLStockMovementTransfer/Form1.cs:93 `_importAllButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLTransportLabel

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Printer is invalid. |  | 10 | SMLBarcodeManage/_itemBarcodePrint.cs:634 `_print`<br>SMLBarcodeManage/_itemBarcodePrint.cs:1164 | สินค้า › ข้อมูลสินค้า › พิมพ์บาร์โค๊ดด้วยเครื่องพิมพ์ทั่วไป<br>เจ้าหนี้ › ข้อมูลเจ้าหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า<br>ลูกหนี้ › ข้อมูลลูกหนี้ › พิมพ์ที่อยู่จัดส่งสินค้า |
| นำเข้าข้อมูลเรียบร้อย | แจ้ง | 1 | SMLTransportLabel/_importTransportLabel.cs:42 `_importButton_Click` | เจ้าหนี้ › ข้อมูลเจ้าหนี้ › นำเข้าที่อยู่จัดส่งเจ้าหนี้<br>ลูกหนี้ › ข้อมูลลูกหนี้ › นำเข้าที่อยู่จัดส่งลูกหนี้ |
| ผิดพลาด {…} | ผิดพลาด | 1 | SMLTransportLabel/_importTransportLabel.cs:46 `_importButton_Click` | เจ้าหนี้ › ข้อมูลเจ้าหนี้ › นำเข้าที่อยู่จัดส่งเจ้าหนี้<br>ลูกหนี้ › ข้อมูลลูกหนี้ › นำเข้าที่อยู่จัดส่งลูกหนี้ |

## AKZOPODownloadConfig

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Connected Success !! |  | 1 | AKZOPODownloadConfig/Form1.cs:141 `_testConnectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| Save Config Success !!! |  | 1 | AKZOPODownloadConfig/Form1.cs:110 `_saveButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## BCTOSML

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Import Success |  | 2 | BCTOSML/Form1.cs:982 `_selectTableButton_Click`<br>BCTOSML/Form1.cs:1184 `_selectTableButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| import Success |  | 1 | BCTOSML/Form1.cs:701 `_importSMLICtoolStrip_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## EarthStockManage

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| บันทึกข้อมูลสำเร็จ ระบบจะปิดจอนี้ให้โดยอัตโนมัติ `save_success` | แจ้ง | 2 | EarthStockManage/_serverConfig.cs:61 `_saveButton_Click`<br>SMLTransferDataPOS/_mainServerSetup.cs:62 `_saveButton_Click` | ส่วนกลาง `_mainServerSetup`, `_serverConfig` — ใช้ร่วมหลายหน้าจอ |
| Start Import Data | ถาม | 1 | EarthStockManage/_stockImportControl.cs:307 `_importButton_Click` | ส่วนกลาง `_stockImportControl` — ใช้ร่วมหลายหน้าจอ |

## PackShipMoveParcelPrint

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Errror Response:{…} |  | 1 | PackShipMoveParcelPrint/_packShipAPI.cs:137 `phaseResponseParcelSend` | ส่วนกลาง `_packShipAPI` — ใช้ร่วมหลายหน้าจอ |
| Login Failed :{…} |  | 1 | PackShipMoveParcelPrint/_packShipAPI.cs:132 `phaseResponseParcelSend` | ส่วนกลาง `_packShipAPI` — ใช้ร่วมหลายหน้าจอ |

## PromptPayQRCode

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ต้องการยกเลิกการเชื่อมต่อหรือไม่ | เตือน | 2 | PromptPayQRCode/EDC/EDCConnectForm.cs:249 `_cancelButton_Click`<br>PromptPayQRCode/KbankEDC/KBankEDCConnectForm.cs:175 `_cancelButton_Click` | ส่วนกลาง `EDCConnectForm`, `KBankEDCConnectForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเชื่อมต่อได้ |  | 2 | PromptPayQRCode/EDC/EDCConnectForm.cs:167 `EDCConnectForm_Load`<br>PromptPayQRCode/KbankEDC/KBankEDCConnectForm.cs:139 `_payKBankEDCForm_Load` | ส่วนกลาง `EDCConnectForm`, `KBankEDCConnectForm` — ใช้ร่วมหลายหน้าจอ |

## SMLDataQuery

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Are You Sure ?? | ถาม | 1 | SMLDataQuery/Form1.cs:70 `_executeButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |
| Query Selec Only |  | 1 | SMLDataQuery/Form1.cs:83 `_executeButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLEDIControl

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| {…} : ใช้ไปแล้ว |  | 5 | SMLEDIControl/_ediExternalScreenControl.cs:109 `_gridCustomer__alterCellUpdate`<br>SMLEDIControl/_ediExternalScreenControl.cs:126 `_gridBarcode__alterCellUpdate` | ส่วนกลาง `_ediExternalScreenControl` — ใช้ร่วมหลายหน้าจอ |
| ไม่พบข้อมูล : รหัสลูกค้า |  | 1 | SMLEDIControl/_ediExternalScreenControl.cs:497 `_search` | ส่วนกลาง `_ediExternalScreenControl` — ใช้ร่วมหลายหน้าจอ |

## SMLERPAR

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| กรุณาป้อนเลขที่เอกสาร และลูกหนี้ |  | 7 | SMLERPAR/_ar_debt_billing.cs:73 `_printData`<br>SMLERPAR/_ar_pay_bill.cs:75 `_printData` | หน้าจอกลาง — ขึ้นได้ใน 6 เมนู |
| ไม่พบรายการ กรุณาตรวจสอบใหม่ : {…} |  | 3 | SMLAPARControl/_ar_ap_trans_grid.cs:973 `_searchBillList`<br>SMLERPAR/_ar_bill_collector.cs:736 | ลูกหนี้ › Bill Collector |

## SMLERPCASHBANKReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ยังไม่ได้กำหนดเงื่อนไข | แจ้ง | 54 | SMLERPCASHBANKReport/_report_cash/_cb_subcashopen.cs:262 `_getCompanyValue`<br>SMLERPCASHBANKReport/_report_cash/_cb_subcashreceive.cs:259 `_getCompanyValue` | หน้าจอกลาง — ขึ้นได้ใน 6 เมนู |
| :: ERR :: <br>{…} |  | 42 | SMLERPCASHBANKReport/_report_cash/_cb_deposit.cs:83 `_cb_deposit`<br>SMLERPCASHBANKReport/_report_cash/_cb_subcashopen.cs:188 `_showCondition` | บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.53)<br>บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีหัก ณ. ที่จ่าย  (ภงด.3)<br>บัญชี › หัก ณ. ที่จ่าย › รายงานภาษีถูกหัก ณ. ที่จ่าย |

## SMLERPReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| เอกสารเลขที่ หรือ ยอดตัดจ่าย ห้ามว่าง | แจ้ง | 9 | SMLERPControl/supplier/_screen_ap_main.cs:686 `_search`<br>SMLERPReport/ap/_condition_type_1.cs:728 `_searchAndWarning` | ส่วนกลาง `_condition`, `_condition_type_1`, `_icTransScreenBottomControl` — ใช้ร่วมหลายหน้าจอ |
| >> {…} |  | 1 | SMLERPReport/ap/_report_ap.cs:1814 | ส่วนกลาง `_report_ap` — ใช้ร่วมหลายหน้าจอ |

## SMLERPTemplate

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| คุณต้องการ เพิ่ม เมนู {…} เข้าไป หรือไม่ | ถาม | 1 | SMLERPTemplate/_selectMenuShortcutForm.cs:26 `_selectMenuShortcutForm` | ส่วนกลาง `_selectMenuShortcutForm` — ใช้ร่วมหลายหน้าจอ |
| ไม่สามารถเข้าเมนูนี้ได้ | แจ้ง | 1 | SMLERPTemplate/_templateMainForm.cs:586 `_doImportMasterFormDesign` | ส่วนกลาง `_templateMainForm` — ใช้ร่วมหลายหน้าจอ |

## SMLLanguage

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Can't save {…} ({…}) |  | 6 | SMLDatabaseDesign/Form1.cs:592 `writeScriptIntoFile`<br>SMLFastReportDesign/_formCreateScrip.cs:182 `_buttonSave_Click` | ส่วนกลาง `Form1`, `_formCreateScrip` — ใช้ร่วมหลายหน้าจอ |
| Found Duplicate |  | 1 | SMLLanguage/Form1.cs:351 `_duplicateCheckButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLPOS

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Failed Create C:\smlsoft{…} |  | 1 | SMLPOS/_mainForm.cs:131 `_mainForm` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |
| Failed Create Folder C:\smlsoft{…} |  | 1 | SMLPOS/_mainForm.cs:127 `_mainForm` | ส่วนกลาง `_mainForm` — ใช้ร่วมหลายหน้าจอ |

## SMLPOSChecker

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Auto Connect | แจ้ง | 1 | SMLPOSChecker/Program.cs:75 | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |
| ยืนยันการ เปลี่ยนแปลงข้อมูล | แจ้ง | 1 | SMLPOSChecker/_checkVatControl.cs:194 `_updateVatButton_Click` | ส่วนกลาง `_checkVatControl` — ใช้ร่วมหลายหน้าจอ |

## TEST

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Error loading image: {…} |  | 1 | TEST/DisplayImageFromURL.cs:47 `_previewButton_Click` | ส่วนกลาง `DisplayImageFromURL` — ใช้ร่วมหลายหน้าจอ |
| Open : {…} |  | 1 | TEST/TestOpenTempPathForm.cs:25 `button1_Click` | ส่วนกลาง `TestOpenTempPathForm` — ใช้ร่วมหลายหน้าจอ |

## HTMLwysiwygLib

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Error Couldn't Cut<br>\r{…} | ผิดพลาด | 1 | HTMLwysiwygLib/htmlwysiwyg.cs:169 `cutToolStripButton_Click` | ส่วนกลาง `htmlwysiwyg` — ใช้ร่วมหลายหน้าจอ |

## ICCManage

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Renew Resource | แจ้ง | 5 | ICCManage/Program.cs:287 `Main`<br>SMLColorStore/Program.cs:311 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |

## IMEXDataTransfer

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| กรุณาทำการเชื่อมต่อ |  | 2 | IMEXDataTransfer/MainForm.cs:72 `_transferDataControl1_GetDataTransferConnectionEventArgs`<br>SMLDataTransfer/MainForm.cs:60 `_transferDataControl1_GetDataTransferConnectionEventArgs` | ส่วนกลาง `MainForm` — ใช้ร่วมหลายหน้าจอ |

## IMSSalesCommission

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่สามารถเข้าเมนูนี้ได้{…} | แจ้ง | 10 | IMSSalesCommission/_mainForm.cs:79 `_activeMenu`<br>SMLAccount/_mainForm.cs:1346 `_activeMenu` | ส่วนกลาง `_mainForm`, `_mainScreen`, `_menuForm` — ใช้ร่วมหลายหน้าจอ |

## SMLBillFree

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ยืนดีต้อนรับเข้าสู่ระบบ | แจ้ง | 2 | SMLBillFree/_loginForm.cs:299 `_loginButton_Click`<br>SMLCloud/_loginForm.cs:299 `_loginButton_Click` | ส่วนกลาง `_loginForm` — ใช้ร่วมหลายหน้าจอ |

## SMLDataCenterSync

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Active SyncDatabase มีข้อผิดพลาด :{…} |  | 1 | SMLDataCenterSync/_run.cs:280 `_start` | ส่วนกลาง `_run` — ใช้ร่วมหลายหน้าจอ |

## SMLDataTransfer

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่สามารถเชื่อมต่อได้ กรุณาตรวจสอบ |  | 2 | SMLDataTransfer/_serverConnectionControl.cs:178 `connectButton_Click`<br>SMLDataTransfer/_serverConnectionControl.cs:186 `connectButton_Click` | ส่วนกลาง `_serverConnectionControl` — ใช้ร่วมหลายหน้าจอ |

## SMLERPARReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ไม่พบข้อมูล | ผิดพลาด | 3 | SMLERPARReport/report/_movement.cs:191 `_reportInitColumnValue`<br>SMLInventoryControl/_icTransControl.cs:18204 `_getDoHomeAPIButton_Click` | เจ้าหนี้ › รายงานวิเคราะห์ › รายงานเคลื่อนไหวเจ้าหนี้<br>ลูกหนี้ › รายงานวิเคราะห์ › รายงานเคลื่อนไหวลูกหนี้ |

## SMLERPPOReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| ยังไม่ได้เลือกเงื่อนไข |  | 8 | SMLERPCASHBANKReport/_report_bank/_report_cash_bank.cs:352 `_cash_bank_config`<br>SMLERPICReport/ic_analysis/_ic_report_info_stk_profit.cs:796 | หน้าจอกลาง — ขึ้นได้ใน 11 เมนู |

## SMLERPReportTool

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| กรุณาเลือกเอกสารตรวจนับ |  | 2 | SMLERPReportTool/_conditionScreen.cs:362 `_conditionScreen`<br>SMLERPReportTool/_conditionScreen.cs:379 `_conditionScreen` | ส่วนกลาง `_conditionScreen` — ใช้ร่วมหลายหน้าจอ |

## SMLERPSOReport

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| คำสั่งผิดพลาด <br> {…} |  | 1 | SMLERPSOReport/_report/_report_sale_service_by_item.cs:205 `_reportInitDocColumn` | ซื้อ › รายงานสรุป › รายงานซื้อสินค้าแยกตามสินค้า<br>ขาย › รายงาน/ยกเลิก › รายงานการขายและบริการเรียงตามสินค้า |

## SMLFastReportUpdate

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Connected !!! |  | 1 | SMLFastReportUpdate/Form1.cs:58 `_connectButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLFormDesignGenerate

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Save Success !! |  | 1 | SMLFormDesignGenerate/Form1.cs:158 `_saveButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLHealthy

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| UAT1=Yes,UAT7=No | แจ้ง | 3 | SMLHealthy/Program.cs:229 `Main`<br>SMLPOSCashier/Program.cs:217 `Main` | ส่วนกลาง `Program` — ใช้ร่วมหลายหน้าจอ |

## SMLLogQueryGen

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| sucess {…} |  | 1 | SMLLogQueryGen/Form1.cs:93 `ProcessDate` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLPickAndPack

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Save Success |  | 1 | SMLPickAndPack/_setupMachineUserControl.cs:54 `_buttonSave_Click` | ส่วนกลาง `_setupMachineUserControl` — ใช้ร่วมหลายหน้าจอ |

## SMLSyncClient

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| Success Please Restart Program |  | 1 | SMLSyncClient/main.cs:258 `_saveConfigButton_Click` | ส่วนกลาง `main` — ใช้ร่วมหลายหน้าจอ |

## SMLTOBC

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| สำเร็จ (จะเริ่มทำงานเมื่อกดปุ่มเริ่มโอนข้อมูล) |  | 1 | SMLTOBC/Form1.cs:1044 `_autoButton_Click` | ส่วนกลาง `Form1` — ใช้ร่วมหลายหน้าจอ |

## SMLTemplate

| ข้อความ | ชนิด | จุดในโค้ด | ที่โค้ด (ตัวอย่าง) | เมนู (ตัวอย่าง) |
|---|---|---|---|---|
| {…}Success{…} |  | 1 | SMLTemplate/_glUserControl.cs:255 `_saveButton_Click` | ส่วนกลาง `_glUserControl` — ใช้ร่วมหลายหน้าจอ |

