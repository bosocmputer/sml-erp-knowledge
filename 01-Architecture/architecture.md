# สถาปัตยกรรม SML ERP

## Client: smlerp (C# WinForms, .NET Framework 2.0)

- `SMLAccountPOSProfessional/Program.cs`: ตั้ง `MyLib._myGlobal._isVersionEnum = _versionType.SMLAccountPOS`, `_programName = "SML Account POS"` แล้วเรียก `SMLAccount.Program.Main()` — ทุก edition (POS, Professional, TomYumGoong, SeaAndHill, Lao ฯลฯ) เป็น launcher บางที่ตั้ง version flag ต่างกัน
- `SMLAccount` อ้างอิง 38 โปรเจกต์: SMLERPSO (ขาย), SMLERPPO (ซื้อ), SMLERPIC (สินค้า/คลัง), SMLERPAR (ลูกหนี้), SMLERPAP (เจ้าหนี้), SMLERPGL (บัญชีแยกประเภท), SMLERPCASHBANK (เงินสด/ธนาคาร/เช็ค), SMLERPASSET (สินทรัพย์), SMLPOSClient/SMLPOSControl (POS), SMLERPReport/SMLFastReport (รายงาน), SMLMIS, SMLERPAudit, SMLPPShipment, SMLTransportLabel, SMLDataCenterSync, SMLEDIControl, SMLERPConfig, SMLERPTemplate ฯลฯ
- เมนู: `SMLAccount/Menu.cs`, `SMLAccount/menu.json`, `_mainForm.cs`
- Data access: `MyLib/_myFrameWork.cs` → SOAP proxy `MyLib/Web References/SMLJAVAWS` (DotNetFrameWorkService.wsdl) operation หลัก `_query`, `_queryInsertOrUpdate`, `_queryList`, `_loginProcess`, `_getDatabaseList`, `_queryCompress*` ฯลฯ — **client สร้าง SQL string เอง** แล้วส่งไปให้ server รัน
- พจนานุกรมตาราง/ฟิลด์: `SMLERPGlobal/_data.cs` (~521 คลาสตาราง, ค่าคงที่ชื่อฟิลด์), โครงสร้าง DB: `SMLDBStructure/`
- Enum ประเภทเอกสาร: `SMLERPGlobal/_global.cs` `_transControlTypeEnum` (~บรรทัด 2749) และตัวแปลงเป็นเลข `_transFlag()` (~บรรทัด 1575)
- Edition เฉพาะกลุ่ม: SMLPOSMED/IMSPOSMED (ร้านยา), SMLTomYumGoong/IMSRestaurant (ร้านอาหาร), SMLColorStore (ร้านสี), SMLWMS, SMLServiceCenter, SMLETaxInvoice/INetEtaxService (e-Tax)
- `.github/copilot-instructions.md` ที่ CLAUDE.md อ้างถึง **ไม่มีอยู่จริง** — ไม่มีเอกสารสถาปัตยกรรม

## Server: SMLJavaWebService (`~/dev/smljavaws2`, Java WAR บน Tomcat, v3.9.14)

- SOAP: `/DotNetFrameWork`, `/SMLFrameWork` (WSServlet) — ตรวจ session ด้วย `_guidReady(GUID)` จาก login
- REST:
  - `/webresources/rest/...` (RestService/Rest.java): query, querygroup, select, selectgroup, findprice, findbarcode, posprocess, payprocess, login, device, lasttimescan, image
  - `/rest/v1/...`: processstockrequest, structure, logger, clusterinfo, try/{provider}
  - `/health`
- คำนวณต้นทุนสต็อก: `StockProcess/` (AverageCostStockCalculator, LotFIFOStockProcess, LotManualStockProcess), `SMLWebService/ICStockCostProcess.java`; ส่งงานผ่าน queue ได้ (RabbitMQ/Redis/Google Pub/Sub, STOMP) ตาม env `SML_NEXT_PROCESS_*`
- config ต่อ provider: ไฟล์ `SMLConfig<provider>.xml`
- ผู้ใช้ REST: Flutter POS (dedepos2, dedecashier, dedepos_new), smlcheckprice, smlaicloud-report เรียก `webresources/rest/select|query`

### ข้อสังเกตด้านความปลอดภัย (พบจากโค้ด 2026-10-20)
- `/webresources/rest/query`, `querygroup` (รัน SQL ใด ๆ), `select`, `selectgroup` **ไม่มีการตรวจสิทธิ์** มีแค่ XSS/X-Frame filter
- ผู้ใช้ยืนยันว่า web service ของลูกค้าเปิดผ่าน port forward ทั้งภายในและภายนอก
- ผู้ใช้บอกว่าไม่ต้องการแก้ smlerp — ให้ถือเป็นข้อจำกัดในการออกแบบ product (เชื่อมผ่าน MCP/agent ฝั่งร้าน ไม่ผ่าน web service นี้) และแจ้งเตือนเมื่อเกี่ยวข้องเท่านั้น

## โมเดลเอกสาร

- หัวเอกสาร `ic_trans` (trans_type, trans_flag, doc_no, doc_date, doc_ref, tax_doc_no, is_cancel, last_status ...) รายการ `ic_trans_detail`; ส่วนขยาย `ic_trans_detail_lot`, `_serial_number`, `_promotion`, `ic_trans_shipment`, `ic_trans_draft`
- สายขาย: เสนอราคา → สั่งจอง → สั่งขาย → สั่งจ่าย/ส่งของ (SoDeliveryOrder) → ขาย (44) → รับชำระ (239)
- สายซื้อ: เสนอซื้อ (2) → ใบสั่งซื้อ (6) → ซื้อ/รับสินค้า (12, partial 310) → ตั้งหนี้ → จ่ายชำระ
- คลัง: ยกมา (54), เบิก (56), รับคืนจากเบิก (58), รับสำเร็จรูป (60), ปรับปรุง (66), โอนเข้า/ออก (70/72), ตรวจนับ
- ผลกระทบของเอกสาร: สต็อก+ต้นทุน (web service), GL `gl_journal`/`gl_journal_detail`, VAT `gl_journal_vat_sale`/`_buy`, ลูกหนี้/เจ้าหนี้ `ap_ar_trans`(+`_detail`), เงินสด/ธนาคาร/เช็ค `cb_trans`
- POS: `sale_shift_id`, `cashier_code`, `pos_log`, `pos_settle_bill_cancel`, `temp_cash_movement`
- ล็อต/วันหมดอายุ: `ic_trans_detail_lot`, `ic_inventory_lot`, `lot_number`, `date_expire`
- Log: `erp_print_logs`, `erp_cancel_logs`, `erp_credit_approved_logs`, `master_logs`, `<db>_logs.erp_logs`
- ยังไม่พบ field จุดสั่งซื้อ/สต็อกขั้นต่ำ (ค้นด้วย minimum/min_qty/reorder/purchase_point) — ต้องยืนยัน
