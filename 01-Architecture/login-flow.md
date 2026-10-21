---
tags: [sml, login, flow]
---
# โฟลว์เปิดโปรแกรมและ Login (SMLAccountPOSProfessional)

ไล่จากโค้ด 2026-10-20 (static trace ยังไม่ได้รันจริง) — กลับไป [[00-Index]] · ดูภาพรวม [[architecture]]

## ลำดับการทำงาน

1. **`SMLAccountPOSProfessional/Program.cs`** ตั้ง `_isVersionEnum = SMLAccountPOS`, `_programName = "SML Account POS"` → เรียก `SMLAccount.Program.Main()`
2. **`SMLAccount/Program.cs` `Main()`**
   - เปิด TLS 1.2, ยอมรับ SSL certificate ทุกใบ (`ServerCertificateValidationCallback` คืน `true`)
   - (Release) เช็กอัปเดตจาก `https://www.smlaccount.com/smlaccount/update.xml` ผ่าน `SMLAutoUpdater`
   - ตั้งค่า global: ภาษาไทย, ปี พ.ศ. (`_year_add = 543`), culture `en-US`, ชื่อไฟล์ config ต่าง ๆ:
     `SMLERPLogin.xml` (profile login), `SMLConfig.xml`, main database `smlerpmain`, `SMLDatabase.xml` / `SMLMainDatabase.xml` / `smllogsdatabase.xml` / `smlimagesdatabase.xml` (โครงสร้าง DB), `smllanguage.xml`, `smlposclientdesign.xml`, web service ชื่อ `SMLJavaWebService`
   - `SMLERPTemplate._main._startProgram()`
   - เครื่องที่ชื่อขึ้นต้นตามรายชื่อเครื่องของทีม SML (toe-pc, jead, sml-dev-pc …) ได้ `_isUserTest = true`; `smlsupport-pc` ได้ `_isUserSupport`
   - ถ้าเป็น demo (`_isDemo`) จะ auto-login เข้า `ws.smlaccount.com` / `ws.smlsoft.com:8080` ด้วย provider `DEMO1`
3. **หน้า Login = `MyLib/_databaseManage/_selectDatabase..cs`** (`Application.Run(__selectDatabase)`)
   - อ่าน/บันทึก profile ที่ `<_smlConfigFile>smlerplogin.xml` (+ ไฟล์ประวัติ `H...`) เก็บ provider, data group, user ล่าสุด, รายชื่อ web service server
   - ผู้ใช้กรอก **provider code, data group, user, password** → เลือก web service server ที่ต่อได้ (`_findWebserviceServer`)
   - Login ผู้ดูแล (admin panel) → `_loginProcess(..., mainDatabase)` แล้วเรียก `afterLoginAdminPanel` เพื่อสร้างเมนูสำหรับกำหนดสิทธิ์
   - ดึงรายชื่อ database ที่ผู้ใช้มีสิทธิ์จาก `smlerpmain<provider>`:
     `sml_database_list` (กรอง `data_group`) ∩ (`sml_database_list_user_and_group` ระดับ user `status=0` หรือระดับกลุ่ม `status=1` ผ่าน `sml_user_and_group`)
   - เลือก database → `_loginProcess(config, mainDatabase, user, password, computerName, databaseName)` → ได้ **GUID** เก็บใน `_myGlobal._guid`
4. **ฝั่ง server `SMLWebService/Routine.java` `_loginProcess`**
   - ตรวจ `sml_user_list` ด้วย `user_code` (ตัวพิมพ์ใหญ่) และ `user_password` เทียบตรง ๆ
   - สร้าง GUID ใหม่ → `insert into sml_guid (guid_code, login_time, last_access_time, user_code, computer_name, database_code)`
   - บันทึก `sml_access_list` (access_type 1 = login)
   - ทุกการเรียก SOAP หลังจากนี้ส่ง GUID มาด้วย และ server ตรวจด้วย `_guidReady(GUID)`
5. **หลังเลือก database สำเร็จ** (`SMLAccount/Program.cs` ต่อ)
   - `_g.g._companyProfileLoad()` โหลดข้อมูลบริษัท/ตัวเลือกระบบ, `_loadProgramClientConfig()` (font ฯลฯ), `_checkFirst()`
   - `_g.g._logMenu(0, "", "Login")` บันทึก log การเข้าใช้
   - สร้าง resource table: เมนูจาก `menu.json` (embedded resource) → โครงสร้าง DB (`SMLDBStructure`) → ภาษา XML → `sml_language` → `sml_resource` (ใน main DB ตาม data group)
   - สร้าง `_mainForm` ใหม่, เตือน backup (`_checkBackup`) ถ้าไม่ได้ปิด
   - ถ้า company profile ตั้ง `select_branch_first` + `change_branch_code` → ฟอร์มเลือกสาขา `MyLib._selectBranchForm` (ยกเลิก = logout)
   - `Application.Run(_mainForm)` → หน้าหลัก: สร้างเมนูจาก `menu.json`, ซ่อนเมนูตามสิทธิ์ `_hideNode()` (สิทธิ์กลุ่ม/ผู้ใช้), กดเมนูแล้วส่งตาม tag (`so`, `po`, `ar`, `gl`, `pos`, `config`, `fastreport` …) ใน `_mainForm.cs` ~บรรทัด 1080–1240
   - ปิดโปรแกรม → `_logMenu(2, guid, "")`

## ตารางที่เกี่ยวข้อง (ใน `smlerpmain<provider>`)
`sml_user_list`, `sml_group_list`, `sml_user_and_group`, `sml_database_list`, `sml_database_list_user_and_group`, `sml_guid`, `sml_access_list`, `sml_permissions_user`, `sml_permissions_group`, `sml_language`, `sml_resource` — ดูโครงสร้างที่ [[database-layout]]

## ข้อสังเกต (ข้อเท็จจริงจากโค้ด ไม่ใช่งานแก้)
- รหัสผ่านเทียบเป็นข้อความตรง ๆ ใน `sml_user_list.user_password` และ SQL ต่อ string
- client ยอมรับ SSL certificate ทุกใบ

## ยืนยันจากการรันจริง (2026-10-21)
- หลังเลือก database โปรแกรมโหลดตั้งค่าจาก `aoy`: `erp_user`, `erp_user_group*`, `erp_branch_list`, `erp_company_profile`, `erp_option`, `erp_thai_qr_config`, `erp_option_etax_inet`, `erp_option_mobillyst` และตรวจ `pg_indexes`
- **main database ที่ใช้ตอน login AOY = `smlerpmainnext`** (provider ที่ผู้ใช้กรอกคือ `NEXT`, data group `SML`, data code `AOY`) — ยืนยัน 2 ทาง:
  1. capture aoy-run1 (parse ใหม่แบบไม่กรอง database, 2026-10-21) เห็นลำดับ SQL บน `smlerpmainnext` ตามตารางด้านล่าง
  2. `smlerpmainnext.sml_access_list` มีแถว `database_code='AOY'` เวลา 08:47/08:48 (type 2→1), 09:05 (2), 09:43 (2,1), 10:15 (2), 10:39 (2,1), 10:44 (2) ตรงกับเวลาที่ผู้ใช้ login/ปิดโปรแกรมทั้ง 3 รอบ
- `smlerpmainaoy` ก็ลงทะเบียน AOY ไว้ (`sml_database_list`: AOY|AOY|SML) แต่ไม่ได้ถูกใช้ในการทดสอบนี้ — **database ก้อนเดียวกันลงทะเบียนได้หลาย provider** ([[tenants-overview]])
- บันทึกเดิมที่ว่า "ไม่พบ query ไป main database" ผิด เกิดจากตอน parse ใส่ `--db aoy --db smlerpmainaoy` จึงกรอง `smlerpmainnext` ทิ้ง (ไม่ใช่พฤติกรรมของ SML)

### ลำดับ SQL ที่เห็นจริงบน main database (capture aoy-run1, 08:47–08:48, ค่าใน '' ถูกปิด)
| เวลา | SQL | มาจาก |
|---|---|---|
| ทุก ~60 วิ | `update sml_guid set last_access_time=? where guid_code=?` → `select * from sml_guid where now()-last_access_time > '00:05:00'` (ถ้าพบ → `delete ... > '00:05:00'`) | `Routine.java` `_sendGuid` (heartbeat จาก client `SMLERPTemplate/_templateMainForm.cs` `_processStatusBarWork`) |
| ทุก ~30 วิ | `select roworder from sml_screen_realtime where computer_name=? and ... now()-request_time<'00:00:30'` / `select roworder,request from sml_screen_capture where guid_code=?` | ระบบดูหน้าจอระยะไกล (`SMLERPGlobal/_viewCaptureScreen.cs`) |
| 08:47:39 | `delete from sml_guid where guid_code=?` → `insert into sml_access_list (...) values (...,2,...)` | `_logoutProcess` (ปิด session เก่าก่อน login ใหม่) |
| 08:48:04 | `select data_group from sml_database_list where upper(data_group)=?` | ตรวจ data group |
| 08:48:05 | `select user_password / user_name,user_level / device_id from sml_user_list where upper(user_code)=?` | ตรวจผู้ใช้ |
| 08:48:09 | `select data_code,data_database_name,data_name from sml_database_list where upper(data_group)=? and upper(data_code) in (...)` | รายชื่อ database ที่มีสิทธิ์ |
| 08:48:11 | `select * from sml_user_list where upper(user_code)=? and user_password=?` → `insert into sml_guid (...)` | `_loginProcess` |
| 08:48:18–36 | `sml_language`, `sml_resource where data_group=?`, `sml_custom_language` | โหลดภาษา/resource |

- session หมดอายุเมื่อไม่มี heartbeat เกิน **5 นาที** (`'00:05:00'` ใน `_sendGuid`) — ตอนนี้ `sml_guid` ของ smlerpmainnext ว่าง (0 แถว, 2026-10-21) เพราะ logout ลบแถวทิ้ง
- ผลต่อ sml_mcp_ai: ถ้าจะเขียนผ่าน SOAP ต้องมี GUID ที่ยังไม่หมดอายุ และต้องส่ง heartbeat หรือ login ใหม่ทุกครั้ง; ถ้าเขียน DB ตรง ไม่ผ่านกลไกนี้ (ไม่มีแถวใน `sml_access_list`)

## ยังต้องไล่ต่อ
- `SMLERPTemplate._main._startProgram()` และ `_g.g._companyProfileLoad()` ทำอะไรบ้าง
- dispatcher เมนู → ฟอร์มใน `_mainForm.cs`
