---
tags: [sml, webservice, api, generated]
status: from-code
---
# SMLJavaWebService — รายการ API

> สร้างอัตโนมัติด้วย `scripts/gen_webservice_api.py` จาก `~/dev/smljavaws2` (v3.9.14 ในเครื่อง; server จริงรัน 3.9.7 อาจต่างกัน) — กลับไป [[architecture]] · [[00-Index]]

คอลัมน์ "ตรวจ session" เป็นการเดาจากโค้ด (หาคำว่า guid/token/login ใน handler) — ต้องอ่านโค้ดยืนยันก่อนสรุปเรื่องความปลอดภัย

## REST (23 endpoint)

| path | method | handler | ไฟล์ | ตรวจ session | หมายเหตุ |
|---|---|---|---|---|---|
| `/?/processstockrequest` | POST | `SubmitRequestStockProcess` | `StockProcess/RequestStockProcess.java` | ไม่พบ |  |
| `/health` | GET | `GetHealty` | `Healty/Health.java` | ไม่พบ |  |
| `/health//configtest` | GET | `GetConfig` | `Healty/Health.java` | ไม่พบ |  |
| `/rest/v1` | GET | `RestResponseOK` | `Rest/v1/Rest.java` | ไม่พบ |  |
| `/rest/v1/clusterinfo` | GET | `getClusterInfo` | `Rest/v1/ClusterInfo.java` | ไม่พบ |  |
| `/rest/v1/logger` | GET | `log` | `Rest/v1/Logs.java` | ไม่พบ |  |
| `/rest/v1/structure` | GET | `GetTableIndexs` | `Rest/v1/SMLStructure.java` | ไม่พบ |  |
| `/webresources/rest` | GET | `getXml` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest` | PUT | `putXml` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/check` | GET | `checkConnect` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/device` | POST | `device` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/findbarcode` | POST | `findBarcode` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/findprice` | POST | `findPrice` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/lasttimescan` | POST | `lasTimeScan` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/login` | POST | `login` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/payprocess` | POST | `payProcess` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/posprocess` | POST | `posProcess` | `RestService/Rest.java` | มี |  |
| `/webresources/rest/query` | POST | `query` | `RestService/Rest.java` | ไม่พบ | รัน SQL จาก request |
| `/webresources/rest/querygroup` | POST | `querygroup` | `RestService/Rest.java` | ไม่พบ | รัน SQL จาก request |
| `/webresources/rest/select` | POST | `select` | `RestService/Rest.java` | ไม่พบ | รัน SQL จาก request |
| `/webresources/rest/selectgroup` | POST | `selectGroup` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/testlogs` | GET | `TestLogs` | `RestService/Rest.java` | ไม่พบ |  |
| `/webresources/rest/ulogin` | POST | `uLogin` | `RestService/Rest.java` | ไม่พบ |  |

## SOAP (178 web method)

endpoint `/DotNetFrameWork`, `/SMLFrameWork` (WSServlet) — โปรแกรม Windows เรียกผ่าน proxy `MyLib/Web References/SMLJAVAWS`

| คลาส | method | พารามิเตอร์ |
|---|---|---|
| AndroidFrameWork | `_getTempListFile` | provider, folder |
| AndroidFrameWork | `_getFileLastUpdate` | fileName |
| AndroidFrameWork | `_systemLogin` | password |
| AndroidFrameWork | `_systemChangePassword` | oldPassword, newPassword |
| AndroidFrameWork | `_changePassword` | configFileName, databaseName, userCode, oldPassword, newPassword |
| AndroidFrameWork | `_providerLoad` | password |
| AndroidFrameWork | `_providerSave` | password, Source |
| AndroidFrameWork | `_queryInsertOrUpdateNoGuid2` | configFileName, databaseName, query |
| AndroidFrameWork | `_query2` | configFileName, databaseName, query |
| AndroidFrameWork | `_loadXmlFile` | xmlName |
| AndroidFrameWork | `_saveXmlFile` | "XMLFileName" |
| AndroidFrameWork | `_insertLanguageToTable` | configFileName, databaseName, xmlName |
| AndroidFrameWork | `_getConnection` | databaseID, configFileName, databaseName, mainDatabaseFileName, databaseServer, databaseUser, databasePassword |
| AndroidFrameWork | `_connectDatabase` | configFileName, databaseName |
| AndroidFrameWork | `_getAdminConnection` | configFileName, adminUserCode, adminUserPassword |
| AndroidFrameWork | `_getUserList` | configFileName |
| AndroidFrameWork | `_getGroupList` | configFileName |
| AndroidFrameWork | `_getDatabaseList` | GUID, configFileName |
| AndroidFrameWork | `_saveUserList` | configFileName, databaseName, querySave |
| AndroidFrameWork | `_saveGroupList` | configFileName, databaseName, querySave |
| AndroidFrameWork | `_saveUserAndGroup` | configFileName, databaseName, querySave |
| AndroidFrameWork | `_saveDatabaseList` | configFileName, databaseName, querySave |
| AndroidFrameWork | `_deleteUserList` | configFileName, databaseName, queryDelete |
| AndroidFrameWork | `_deleteGroupList` | configFileName, databaseName, queryDelete |
| AndroidFrameWork | `_getAllTable` | configFileName, structFileName |
| AndroidFrameWork | `_getFieldFromDatabase` | configFileName, databaseName, tableName |
| AndroidFrameWork | `_getTableFromDatabase` | configFileName, databaseName |
| AndroidFrameWork | `_getUserListInGroup` | configFileName, whereString |
| AndroidFrameWork | `_createDatabaseAndTable` | configFileName, databaseGroup, databaseName, tableName, structFileName |
| AndroidFrameWork | `_verifyDatabase` | configFileName, databaseGroup, databaseName, tableName, structFileName |
| AndroidFrameWork | `_verifyDatabaseScript` | scriptName, configFileName, databaseGroup, databaseName, structFileName |
| AndroidFrameWork | `_findDatabase` | configFileName, databaseName |
| AndroidFrameWork | `_queryList` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryListCompress` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryListGetData` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryListGetDataCompress` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryGetStream` | GUID, configFileName, reportGuid, blockSize, skip |
| AndroidFrameWork | `_fileGetStream` | configFileName, provider, folder, fileName, blockSize, skip |
| AndroidFrameWork | `_queryStream` | GUID, configFileName, reportGuid, databaseName, query |
| AndroidFrameWork | `_queryCompressByteArray` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryCompressY` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryColumnName` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_query` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryByteData` | GUID, configFileName, database, query, byteValue |
| AndroidFrameWork | `_loadForm` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_SaveFormDesign` | GUID, configFileName, databaseName, InsertorUpdateType, formCode, formGuidCode, formName, fileCode, backgroundCode |
| AndroidFrameWork | `_query_Image` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_LoadImageList` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_SaveImageList` | GUID, configFileName, databaseName, query, InsertorUpdateType, feilds, TableName, swherefield, swhereData |
| AndroidFrameWork | `_DeleteImageList` | GUID, configFileName, databaseName, TableName, swherefield, swhereData |
| AndroidFrameWork | `_queryInsertOrUpdate` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryInsertOrUpdateCompress` | GUID, configFileName, databaseName, query |
| AndroidFrameWork | `_queryLimit` | GUID, configFileName, databaseName, queryForCount, query, startRecord, maxRecords, countTotalRecord |
| AndroidFrameWork | `_resourceInsertAll` | configFileName, databaseStructFile, dataGroup |
| AndroidFrameWork | `_systemStartup` | GUID, configFileName, databaseName, screenGroup, viewTableName, viewDetailTableName, dataViewFileName, dataViewTemplateFileName |
| AndroidFrameWork | `_resourceInsert` | databaseName, configFileName, dataGroup, code, defaultName, structFileName |
| AndroidFrameWork | `_readXmlFile` | configFileName, xmlFileName |
| AndroidFrameWork | `_getSchemaTable` | configFileName, databaseName, tableName |
| AndroidFrameWork | `_loginProcess` | configFileName, databaseName, userCode, userPassword, computerName, databaseCode |
| AndroidFrameWork | `_logoutProcess` | configFileName, guid, databaseName, userCode, computerName, databaseCode, tableList |
| AndroidFrameWork | `_sendGuid` | configFileName, guid, databaseName, tableList |
| AndroidFrameWork | `_checkConnect` |  |
| AndroidFrameWork | `_checkConnectSpeed` |  |
| AndroidFrameWork | `_queryfrontPosProduct` | GUID, configFileName, databaseName, Barcode, Qty, DocNo, DocDate, BillStatus, Posguid, Mode, freegoods |
| AndroidFrameWork | `_getDatabaseCode` | configFileName |
| DotNetFrameWork | `_getFileLastUpdate` | fileName |
| DotNetFrameWork | `_systemLogin` | password |
| DotNetFrameWork | `_systemChangePassword` | oldPassword, newPassword |
| DotNetFrameWork | `_changePassword` | configFileName, databaseName, userCode, oldPassword, newPassword |
| DotNetFrameWork | `_providerLoad` | password |
| DotNetFrameWork | `_providerSave` | password, Source |
| DotNetFrameWork | `_queryInsertOrUpdateNoGuid2` | configFileName, databaseName, query |
| DotNetFrameWork | `_query2` | configFileName, databaseName, query |
| DotNetFrameWork | `_loadXmlFile` | xmlName |
| DotNetFrameWork | `_saveXmlFile` | "XMLFileName" |
| DotNetFrameWork | `_insertLanguageToTable` | configFileName, databaseName, xmlName |
| DotNetFrameWork | `_getConnection` | databaseID, configFileName, databaseName, mainDatabaseFileName, databaseServer, databaseUser, databasePassword |
| DotNetFrameWork | `_connectDatabase` | configFileName, databaseName |
| DotNetFrameWork | `_getAdminConnection` | configFileName, adminUserCode, adminUserPassword |
| DotNetFrameWork | `_getUserList` | configFileName |
| DotNetFrameWork | `_getGroupList` | configFileName |
| DotNetFrameWork | `_getDatabaseList` | GUID, configFileName |
| DotNetFrameWork | `_saveUserList` | configFileName, databaseName, querySave |
| DotNetFrameWork | `_saveGroupList` | configFileName, databaseName, querySave |
| DotNetFrameWork | `_saveUserAndGroup` | configFileName, databaseName, querySave |
| DotNetFrameWork | `_saveDatabaseList` | configFileName, databaseName, querySave |
| DotNetFrameWork | `_deleteUserList` | configFileName, databaseName, queryDelete |
| DotNetFrameWork | `_deleteGroupList` | configFileName, databaseName, queryDelete |
| DotNetFrameWork | `_getAllTable` | configFileName, structFileName |
| DotNetFrameWork | `_getFieldFromDatabase` | configFileName, databaseName, tableName |
| DotNetFrameWork | `_getTableFromDatabase` | configFileName, databaseName |
| DotNetFrameWork | `_getUserListInGroup` | configFileName, whereString |
| DotNetFrameWork | `_createDatabaseAndTable` | configFileName, databaseGroup, databaseName, tableName, structFileName |
| DotNetFrameWork | `_verifyDatabase` | configFileName, databaseGroup, databaseName, tableName, structFileName |
| DotNetFrameWork | `_verifyDatabaseScript` | scriptName, configFileName, databaseGroup, databaseName, structFileName |
| DotNetFrameWork | `_findDatabase` | configFileName, databaseName |
| DotNetFrameWork | `_queryList` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryListCompress` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryListGetData` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryListGetDataCompress` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryGetStream` | GUID, configFileName, reportGuid, blockSize, skip |
| DotNetFrameWork | `_queryStream` | GUID, configFileName, reportGuid, databaseName, query |
| DotNetFrameWork | `_queryCompressByteArray` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryCompress` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryColumnName` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_query` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryByteData` | GUID, configFileName, database, query, byteValue |
| DotNetFrameWork | `_loadForm` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_SaveFormDesign` | GUID, configFileName, databaseName, InsertorUpdateType, formCode, formGuidCode, formName, fileCode, backgroundCode |
| DotNetFrameWork | `_query_Image` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_getQrCodeByte` | GUID, configFileName, Content |
| DotNetFrameWork | `_LoadImageList` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_SaveImageList` | GUID, configFileName, databaseName, query, InsertorUpdateType, feilds, TableName, swherefield, swhereData |
| DotNetFrameWork | `_DeleteImageList` | GUID, configFileName, databaseName, TableName, swherefield, swhereData |
| DotNetFrameWork | `_queryInsertOrUpdate` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryInsertOrUpdateCompress` | GUID, configFileName, databaseName, query |
| DotNetFrameWork | `_queryLimit` | GUID, configFileName, databaseName, queryForCount, query, startRecord, maxRecords, countTotalRecord |
| DotNetFrameWork | `_resourceInsertAll` | configFileName, databaseStructFile, dataGroup |
| DotNetFrameWork | `_systemStartup` | GUID, configFileName, databaseName, screenGroup, viewTableName, viewDetailTableName, dataViewFileName, dataViewTemplateFileName |
| DotNetFrameWork | `_resourceInsert` | databaseName, configFileName, dataGroup, code, defaultName, structFileName |
| DotNetFrameWork | `_readXmlFile` | configFileName, xmlFileName |
| DotNetFrameWork | `_getSchemaTable` | configFileName, databaseName, tableName |
| DotNetFrameWork | `_loginProcess` | configFileName, databaseName, userCode, userPassword, computerName, databaseCode |
| DotNetFrameWork | `_logoutProcess` | configFileName, guid, databaseName, userCode, computerName, databaseCode, tableList |
| DotNetFrameWork | `_sendGuid` | configFileName, guid, databaseName, tableList |
| DotNetFrameWork | `_checkConnect` |  |
| DotNetFrameWork | `_checkConnectSpeed` |  |
| DotNetFrameWork | `_queryfrontPosProduct` | GUID, configFileName, databaseName, Barcode, Qty, DocNo, DocDate, BillStatus, Posguid, Mode, freegoods |
| DotNetFrameWork | `_getDatabaseCode` | configFileName |
| SMLFrameWork | `_process_profit_and_lost_by_color_stream` | mode, GUID, configFileName, databaseName, itemCodeBegin, itemCodeEnd, custCodeBegin, custCodeEnd, dateBegin, dateEnd, itemCodeList, custCodeList, reportGuid |
| SMLFrameWork | `_process_profit_and_lost_by_product_stream` | mode, GUID, configFileName, databaseName, itemCodeBegin, itemCodeEnd, custCodeBegin, custCodeEnd, dateBegin, dateEnd, itemCodeList, custCodeList, reportGuid |
| SMLFrameWork | `_purchase_permium_process` | GUID, configFileName, databaseName, dateProcess, source |
| SMLFrameWork | `_purchase_permium_process_compress` | GUID, configFileName, databaseName, dateProcess, source |
| SMLFrameWork | `_glReFormatChartOfAccount` | GUID, configFileName, databaseName |
| SMLFrameWork | `_invoiceGetqueryCompress` | GUID, configFileName, databaseName, query |
| SMLFrameWork | `_processDashBoard` | GUID, configFileName, databaseName, query |
| SMLFrameWork | `_processDashBoardsCompress` | GUID, configFileName, databaseName, query |
| SMLFrameWork | `_processApTrans` | GUID, configFileName, databaseName, dateBegin, dateEnd, queryWhere, queryWhere2, orderby, reportType, trans_flag, startRecord, maxRecord |
| SMLFrameWork | `_processApTransCompress` | GUID, configFileName, databaseName, dateBegin, dateEnd, queryWhere, queryWhere2, orderby, reportType, trans_flag, startRecord, maxRecord |
| SMLFrameWork | `_trans_itemGetquery` | GUID, configFileName, databaseName, transection_flag, startRecord, maxRecords, countTotalRecord |
| SMLFrameWork | `_trans_itemGetqueryCompress` | GUID, configFileName, databaseName, query, startRecord, maxRecords, countTotalRecord |
| SMLFrameWork | `_process_ar_status` | GUID, configFileName, databaseName, dateBegin, dateEnd, where, orderby, reportType |
| SMLFrameWork | `_process_ar_status_compress` | GUID, configFileName, databaseName, dateBegin, dateEnd, where, orderby, reportType |
| SMLFrameWork | `_process_ar_ageing` | GUID, configFileName, databaseName, dateEnd, day1, day2, day3, day4, where1, orderby1 |
| SMLFrameWork | `_process_ar_ageing_compress` | GUID, configFileName, databaseName, dateEnd, day1, day2, day3, day4, where1, orderby1 |
| SMLFrameWork | `_process_ar_stream` | GUID, configFileName, databaseName, reportName, where, orderby, reportType |
| SMLFrameWork | `_processChqCreditCard` | GUID, configFileName, databaseName |
| SMLFrameWork | `_processChqWallet` | GUID, configFileName, databaseName |
| SMLFrameWork | `_process_cb_statement` | GUID, configFileName, databaseName, dateBegin, dateEnd, where, orderby, reporttype |
| SMLFrameWork | `_process_cb_statement_compress` | GUID, configFileName, databaseName, dateBegin, dateEnd, where, orderby, reporttype |
| SMLFrameWork | `_queryCBGetStream` | GUID, configFileName, reportGuid, blockSize, skip |
| SMLFrameWork | `_queryCBStream` | GUID, configFileName, reportGuid, databaseName, query |
| SMLFrameWork | `_process_stock_balance` | GUID, configFileName, databaseName, itemList, calcFlag |
| SMLFrameWork | `_process_stock_balance_compress` | GUID, configFileName, databaseName, itemList, calcFlag |
| SMLFrameWork | `_process_stock_cost_finish` | GUID, configFileName, databaseName |
| SMLFrameWork | `_process_stock_cost` | GUID, configFileName, databaseName, itemCode, processMode, dateBegin, dateEnd |
| SMLFrameWork | `_process_stock_cost_compress` | GUID, configFileName, databaseName, itemCode, processMode, dateBegin, dateEnd |
| SMLFrameWork | `_process_ic_balance` | GUID, configFileName, databaseName, startItem, endItem, where1, orderby1 |
| SMLFrameWork | `_process_ic_balance_compress` | GUID, configFileName, databaseName, startItem, endItem, where1, orderby1 |
| SMLFrameWork | `_process_ic_remain` | GUID, configFileName, databaseName, where1, orderby1 |
| SMLFrameWork | `_process_ic_remaimn_compress` | GUID, configFileName, databaseName, where1, orderby1 |
| SMLFrameWork | `_queryRemainGetStream` | GUID, configFileName, reportGuid, blockSize, skip |
| SMLFrameWork | `_queryRemainStream` | GUID, configFileName, reportGuid, databaseName, query |
| SMLFrameWork | `_process_request` | GUID, configFileName, databaseName, query |
| SMLFrameWork | `_process_request_cancel` | GUID, configFileName, databaseName |
| SMLFrameWork | `_process_ap_status` | GUID, configFileName, databaseName, dateEnd, where, where2, orderby, reportType, startRecord, maxRecord |
| SMLFrameWork | `_process_ap_status_compress` | GUID, configFileName, databaseName, dateEnd, where, where2, orderby, reportType, startRecord, maxRecord |
| SMLFrameWork | `_process_ap_ageing` | GUID, configFileName, databaseName, dateEnd, day1, day2, day3, day4, where1, orderby1 |
| SMLFrameWork | `_process_ap_ageing_compress` | GUID, configFileName, databaseName, dateEnd, day1, day2, day3, day4, where1, orderby1 |
| SMLFrameWork | `_process_gps_location` |  |
| SMLFrameWork | `_process_gps_data` | __name, __address, __latitude, __longitude, __flag, __roworder |
| SMLFrameWork | `_process_gps_load_condition` | __loadProvince, __loadAmper, __loadTambon |
| SMLFrameWork | `_process_gps_load_data` | __provinceCode, __amperCode, TambonCode, __keyword |
| SMLFrameWork | `_process_gps_update_data` | __customer_code, __latitude, __longitude, __remark |
| SMLFrameWork | `_process_gps_load_sale_data` | __databaseName, __fromDate, __toDate |
| SMLFrameWork | `_process_gps_load_sale_data_compress` | __databaseName, __fromDate, __toDate |
| SMLFrameWork | `_process` | GUID, configFileName, databaseName, processGuid |
| SMLFrameWork | `_processKiller` | GUID, configFileName, databaseName |
