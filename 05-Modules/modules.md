---
tags: [sml, modules, generated]
---
# โมดูลของ SMLAccount / SMLAccountPOSProfessional

> สร้างอัตโนมัติด้วย `scripts/gen_modules.py` — อย่าแก้ไฟล์นี้ด้วยมือ

`SMLAccountPOSProfessional` → อ้างอิง `MyLib`, `SMLAccount` แล้วเรียก `SMLAccount.Program.Main()` ดู [[architecture]]

`SMLAccount` อ้างอิงโดยตรง 39 โปรเจกต์ (จำนวนหน้าจอ = ไฟล์ *.Designer.cs โดยประมาณ)

| โปรเจกต์ | ไฟล์ .cs | หน้าจอ/ฟอร์ม | อ้างอิงต่อ |
|---|---|---|---|
| IMEXControl | 100 | 19 | MyDock, MyLib, SMLERPARAPInfo, SMLERPAudit, SMLERPControl, SMLERPGlobal, SMLERPIC, SMLReport |
| MyDock | 86 | 15 |  |
| MyLib | 215 | 65 | MyDock, PromptPayQRCode, SMLAutoUpdater, SMLDBStructure |
| SINGHAReport | 23 | 10 | MyLib, SMLERPARAPInfo, SMLERPControl, SMLERPGlobal, SMLProcess, SMLReport |
| SMLAutoUpdater | 9 | 4 |  |
| SMLDBStructure | 8 | 0 |  |
| SMLDataCenterSync | 9 | 2 | MyLib, SMLERPGlobal, SMLProcess |
| SMLEDIControl | 9 | 4 | MyLib, SMLERPGlobal |
| SMLERPAP | 53 | 25 | MyLib, SMLERPAPARControl, SMLERPControl, SMLERPGlobal, SMLERPReportTool, SMLInventoryControl |
| SMLERPAPReport | 32 | 15 | MyLib, SMLERPARAPInfo, SMLERPARAPReport, SMLERPGlobal, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPAR | 59 | 29 | MyLib, SMLERPAPARControl, SMLERPARAPInfo, SMLERPControl, SMLERPGlobal, SMLERPReportTool, SMLInventoryControl, SMLProcess |
| SMLERPARAPInfo | 12 | 4 | MyLib, SMLERPGlobal |
| SMLERPARAPReport | 41 | 18 | MyLib, SMLERPARAPInfo, SMLERPGlobal, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPASSET | 45 | 22 | MyLib, SMLERPConfig, SMLERPControl, SMLERPGLControl, SMLERPGlobal, SMLProcess, SMLReport |
| SMLERPAudit | 15 | 5 | MyLib, SMLERPGlobal |
| SMLERPCASHBANK | 116 | 57 | MyDock, MyLib, SMLERPControl, SMLERPGlobal, SMLInventoryControl |
| SMLERPCASHBANKReport | 130 | 63 | MyLib, SMLERPControl, SMLERPGLControl, SMLERPGlobal, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPConfig | 45 | 14 | MyDock, MyLib, PromptPayQRCode, SMLERPAudit, SMLERPGlobal |
| SMLERPControl | 208 | 78 | MyDock, MyLib, PromptPayQRCode, SMLERPARAPInfo, SMLERPAudit, SMLERPConfig, SMLERPGlobal, SMLProcess, SMLSmartCardConnector |
| SMLERPGL | 218 | 76 | Evaluant.Calculator, MyDock, MyLib, SMLERPConfig, SMLERPControl, SMLERPGLControl, SMLERPGlobal, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPGlobal | 73 | 18 | MyDock, MyLib |
| SMLERPIC | 135 | 58 | HTMLwysiwygLib, MyDock, MyLib, SINGHAReport, SMLBarcodeManage, SMLERPAPARControl, SMLERPAR, SMLERPControl, SMLERPGLControl, SMLERPGlobal, SMLERPICInfo, SMLInventoryControl, SMLProcess, SMLReport |
| SMLERPICInfo | 40 | 17 | MyLib, SMLERPControl, SMLERPGlobal, SMLERPPO, SMLInventoryControl, SMLProcess |
| SMLERPICReport | 83 | 35 | MyLib, SMLERPAPReport, SMLERPControl, SMLERPGlobal, SMLERPICInfo, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPPO | 21 | 10 | MyLib, SMLERPAPARControl, SMLERPControl, SMLERPGlobal, SMLInventoryControl |
| SMLERPPOReport | 37 | 18 | MyLib, SMLERPGlobal, SMLERPICReport, SMLERPReportTool, SMLERPSOReport, SMLProcess, SMLReport |
| SMLERPReport | 231 | 112 | MyDock, MyLib, SMLERPARAPInfo, SMLERPGlobal, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPSO | 83 | 37 | MobilystTMS, MyDock, MyLib, SMLERPAPARControl, SMLERPControl, SMLERPGlobal, SMLETaxInvoice, SMLInventoryControl, SMLProcess |
| SMLERPSOReport | 28 | 13 | MyDock, MyLib, SMLERPControl, SMLERPGlobal, SMLERPICReport, SMLERPReportTool, SMLProcess, SMLReport |
| SMLERPTemplate | 19 | 8 | MyDock, MyLib, SMLAutoUpdater, SMLDataCenterSync, SMLERPControl, SMLERPGlobal, SMLFastReport, SMLReport |
| SMLERPTransferControl | 21 | 8 | MyLib, SMLERPAPARControl, SMLERPGlobal, SMLInventoryControl, SMLProcess |
| SMLFastReport | 31 | 13 | MyDock, MyLib, SMLERPGlobal, SMLReport |
| SMLMIS | 3 | 1 | Calendar, MyDock, MyLib, SMLERPGlobal |
| SMLPOSClient | 137 | 47 | BarcoderLib, CreatusCashloop, MyDock, MyLib, PromptPayQRCode, SMLBarcodeManage, SMLComponentService, SMLERPAPARControl, SMLERPAR, SMLERPCASHBANKReport, SMLERPControl, SMLERPGlobal, SMLERPIC, SMLERPReportTool, SMLERPSO, SMLERPTemplate, SMLETaxInvoice, SMLInventoryControl, SMLPOSControl, SMLProcess, SMLReport |
| SMLPOSControl | 104 | 41 | BarcoderLib, MyDock, MyLib, SMLBarcodeManage, SMLERPControl, SMLERPGlobal, SMLERPIC, SMLERPReportTool, SMLInventoryControl, SMLReport |
| SMLPPShipment | 6 | 2 | SMLPPControl, SMLPPGlobal |
| SMLProcess | 207 | 3 | MyLib, SMLERPGlobal |
| SMLReport | 131 | 37 | MyLib, PromptPayQRCode, SMLERPControl, SMLERPGlobal |
| SMLTransportLabel | 13 | 5 | MyLib, SMLBarcodeManage, SMLERPGlobal, SMLReport |

## โปรเจกต์ทั้งหมดใน repo (287)

AKZOBIImport, AKZOBIReportCenter, AKZOPODownloadConfig, AKZOPODownloadConsole, AKZOUpdateAgencodeConsole, AccountPOSSingha, AkzoGenPo, AkzoGenPoConsole, AkzoGlobal, App1, AutoUpdateXMLGenerate, BCTOSML, BRAGENTPOS, BRAGENTPOSTest, BRInterface, BarcoderLib, BarcoderLibTests, Calendar, ChampaLaoAccountPOS, ClassLibrary1, CreatusCashloop, DTSClientDownload, EarthStockManage, EarthTransferDataPOS, Evaluant.Calculator, HTMLwysiwygLib, ICCManage, ICCManageTest, IMEXBillPaymentGenerate, IMEXControl, IMEXDataTransfer, IMSERPStandard, IMSERPStandardInstallBuilder, IMSInstallerBuilder, IMSORAN, IMSPOS, IMSPOSMED, IMSRestaurant, IMSSalesCommission, INetEtaxService, INetEtaxServiceTests, Java, JsonLib, MPAYPOS, MPAYPOSLiteOnline, MPAYPOSOnline, MobilystTMS, MobilystTMSTests, MyDock, MyLib, MyLibTests, ORANIMSInstallerBuilder, PDFExportTest, PackShipMoveParcelPrint, PdfSharp, PromptPayQRCode, PromptPayQRCodeTests, SABYPayRestaurant, SABYPayRestaurantDemo, SINGHAReport, SMLAPARControl, SMLAccount, SMLAccountDEMOLao, SMLAccountDemo, SMLAccountDemoEN, SMLAccountInstallerBuilder, SMLAccountOnline, SMLAccountPOS, SMLAccountPOSDEMOTEST, SMLAccountPOSDemo, SMLAccountPOSInstallBuilder, SMLAccountPOSPro, SMLAccountPOSProDEMO, SMLAccountPOSProTest, SMLAccountPOSProfessional, SMLAccountPOSTest, SMLAccountPosProInstallerBuilder, SMLAccountProDemoLao, SMLAccountProInstallBuilder, SMLAccountProPOSDEMO, SMLAccountProfessional, SMLAccountProfessionalDEMO, SMLAccountProfessionalTest, SMLAccountSuriwong, SMLAccountSuriwongTest, SMLAccountTest, SMLAccountTests, SMLAccountUAT, SMLActivesync, SMLAudit, SMLAutoUpdater, SMLBRAccountPOS, SMLBalanceTransfer, SMLBalanceTransfer, SMLBarcodeManage, SMLBarcodeManageTests, SMLBarcodeManageTests1, SMLBarcodePrint, SMLBillFree, SMLCM, SMLCMDEMO, SMLCMInstallBuilder, SMLCMPOSData, SMLCMPOSDataManage, SMLCMTest, SMLChangelogBuilder, SMLCloud, SMLColorStore, SMLColorStoreSync, SMLColorStoreSyncTest, SMLColorStoreTest1, SMLColorStoreTest2, SMLColorStoreTest3, SMLComponentService, SMLCustomerManage, SMLDBStructure, SMLDBStructureTests, SMLDataCenterSync, SMLDataQuery, SMLDataTransfer, SMLDataTransferPro, SMLDatabaseCutOff, SMLDatabaseDesign, SMLDiagnostic, SMLDocs, SMLEDIControl, SMLERP22, SMLERPAP, SMLERPAPReport, SMLERPAR, SMLERPARInfo, SMLERPARReport, SMLERPASSET, SMLERPAudit, SMLERPAuditTests, SMLERPCASHBANK, SMLERPCASHBANKReport, SMLERPConfig, SMLERPControl, SMLERPControlTests, SMLERPDashBoard, SMLERPDatabaseDesign, SMLERPGL, SMLERPGLControl, SMLERPGLTests1, SMLERPGlobal, SMLERPGlobalTests, SMLERPIC, SMLERPICInfo, SMLERPICReport, SMLERPLogger, SMLERPMenuManage, SMLERPPO, SMLERPPOReport, SMLERPReport, SMLERPReportTool, SMLERPSERVICECENTER, SMLERPSO, SMLERPSOReport, SMLERPSOTests, SMLERPTemplate, SMLERPTemplateTests, SMLERPTransferControl, SMLETaxInvoice, SMLETaxInvoiceTests, SMLExecuteQueryTools, SMLFastReport, SMLFastReportDesign, SMLFastReportUpdate, SMLFinancialStatementDesigner, SMLFormDesign, SMLFormDesignGenerate, SMLGLJournalProcess, SMLGeneralLedger, SMLGetPrice, SMLGetPriceCommand, SMLHTMLEditorTest, SMLHealthy, SMLHealthyConfig, SMLHealthyControl, SMLICIAdmin, SMLIMS, SMLIMSTest, SMLInstallerGen, SMLInventoryControl, SMLInventoryControlTests, SMLKAPIConnect, SMLKAPIConnectTests, SMLLanguage, SMLLogQueryGen, SMLLogQueryGenTests, SMLMDBImport, SMLMDBImportConfig, SMLMDBImportTests, SMLMIS, SMLMerchant, SMLMerchantDemo, SMLOffTakeSalesAdmin, SMLPOS, SMLPOSAIS, SMLPOSCashier, SMLPOSChecker, SMLPOSClientDesign, SMLPOSClientTests, SMLPOSCoffee, SMLPOSCoffeeTest, SMLPOSConnect, SMLPOSConnectTests, SMLPOSControl, SMLPOSControlTests, SMLPOSCustomerService, SMLPOSDTAC, SMLPOSDemo, SMLPOSDesign, SMLPOSENDemo, SMLPOSFinalTest, SMLPOSInstallerBuilder, SMLPOSLAODEMO, SMLPOSLite, SMLPOSLiteDemo, SMLPOSLiteDemoEN, SMLPOSLiteDemoENTEST, SMLPOSLiteInstallBuilder, SMLPOSLiteTest, SMLPOSMED, SMLPOSMEDTest, SMLPOSMEDdemo, SMLPOSManage, SMLPOSManageSuriwong, SMLPOSStarter, SMLPOSSuriwong, SMLPOSSuriwongTest, SMLPOSTest, SMLPPControl, SMLPPGlobal, SMLPPShipment, SMLPickAndPack, SMLPosClient, SMLPosCoffeeDemo, SMLPostgreSQLPartitionTable, SMLProcess, SMLProcessService, SMLProcessTests, SMLQRPayment, SMLReport, SMLReportControl, SMLReportTests, SMLReportToolsTest, SMLServiceCenter, SMLSmartCardConnector, SMLStockCostProcess, SMLStockImport, SMLStockMovementTransfer, SMLSyncCheckingTools, SMLSyncClient, SMLTOBC, SMLTemplate, SMLTomYumGoong, SMLTomYumGoongDemo, SMLTomYumGoongENDemo, SMLTomYumGoongInstallBuilder2, SMLTomYumGoongPro, SMLTomYumGoongProDemo, SMLTomYumGoongProInstallBuilder, SMLTomYumGoongProTest, SMLTomYumGoongTest, SMLTransfer, SMLTransferDataPOS, SMLTransportLabel, SMLWMS, SMLWixInstallerBuilder, SeaAndHillAccount, SeaAndHillAccountInstallBuilder, SeaAndHillAccountPOS, SeaAndHillAccountPOSInstallBuilder, SeaAndHillAccountPOSTest, SeaAndHillAccountTest, SeaAndHillPOS, SeaAndHillPOSInstallBuilder, SeaAndHillPOSTest, SeaAndHillRestaurant, SeaAndHillRestaurantTest, TEST, TESTDBSMLPOS, TestPrinter, ZetaHtmlEditControl, _icTransControlTest
