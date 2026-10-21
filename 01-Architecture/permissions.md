---
tags: [sml, permissions, security, verified-on-data]
status: from-code + ข้อมูลจริงใน main database 6 provider (2026-10-21, นับ/โครงสร้างเท่านั้น)
source: smlerp MyLib/_global.cs (`_isAccessMenuPermision`, `_loadmenuPermissions_user/_group`, `_getUserAccessMenuPermissionAll`, `_checkChangeMaster`), MyLib/_databaseManage/_selectDatabase..cs, _userAndGroup(.Designer).cs, SMLAccount/_mainForm.cs, SMLERPGlobal/_global.cs + DB smlerpmain{aoy,cus,cusms,demo,kbyt,next}, aoy
---
# สิทธิ์ผู้ใช้ของ SML

กลับไป [[00-Index]] · login [[login-flow]] · โครงสร้าง database [[database-layout]] · เมนู [[menu-map]]

SML มีสิทธิ์ 3 ชั้น: **(1) เข้า database ไหนได้** และ **(2) เมนูไหน อ่าน/เพิ่ม/แก้/ลบ ได้** อยู่ใน main database ของ provider; **(3) สิทธิ์ทางธุรกิจ** (เปลี่ยนสาขา, เห็นต้นทุน, อนุมัติ, แก้ข้อมูลหลัก …) อยู่ใน data database ของร้าน

## 1. ผู้ใช้และกลุ่ม (main database `smlerpmain<provider>`)
| ตาราง | คอลัมน์ |
|---|---|
| `sml_user_list` | `user_code, user_name, user_password, user_level, active_status, device_id` |
| `sml_group_list` | `group_code, group_name, active_status` |
| `sml_user_and_group` | `user_code, group_code` |
| `sml_database_list_user_and_group` | `data_group, data_code, user_or_group_code, user_or_group_status` — ใครเข้า database ไหนได้ (`status` 0 = ผู้ใช้, 1 = กลุ่ม ดู [[login-flow]]) |
| `sml_permissions_user` / `sml_permissions_group` | `usercode, image_file (bytea), system_id, guid_code` — **สิทธิ์เมนูเก็บเป็นไฟล์ XML ทั้งก้อน 1 แถวต่อผู้ใช้/กลุ่ม** (`usercode` ของตารางกลุ่มคือรหัสกลุ่ม) |
| `sml_permission_links` | โปรแกรม insert เมนูที่ไม่พบในรายการเมนูหลักเข้าไปเอง (`_isAccessMenuPermision`) |

**`user_level`** (ลำดับใน `_userAndGroup.Designer.cs` ~299): **0 = User, 1 = Super User, 2 = Admin, 3 = Super Admin**
- แผงผู้ดูแล (จัดการผู้ใช้/กลุ่ม/สิทธิ์) เข้าได้เฉพาะ level 2–3 (`_selectDatabase..cs` ~662, ~1054); level 0–1 login โหมดผู้ดูแลจะถูกปฏิเสธ (`warning92`)
- ข้อมูลจริง: ค่า level ที่ใช้ 0, 2, 3 (ไม่มีร้านไหนใช้ 1)

**จำนวนจริง** (2026-10-21):
| main database | สิทธิ์ผู้ใช้ | สิทธิ์กลุ่ม | กลุ่ม | ผู้ใช้↔กลุ่ม | สิทธิ์เข้า database |
|---|---|---|---|---|---|
| smlerpmaindemo | 5 | 0 | 1 | 7 | 34 |
| smlerpmainkbyt | 16 | 4 | 5 | 5 | 21 |
| smlerpmaincusms | 4 | 1 | 2 | 6 | 11 |
| smlerpmaincus | 5 | 0 | 1 | 0 | 6 |
| smlerpmainaoy | 1 | 0 | 1 | 0 | 3 |
| smlerpmainnext | 0 | 0 | — | — | — |

## 2. สิทธิ์เมนู (XML ใน `image_file`)
โครงสร้าง (ถอดจากแถวจริงใน smlerpmainkbyt — เก็บแค่ชื่อแท็ก/ค่าสิทธิ์):
```xml
<_mainMenuClass>
  <_MainMenuList>
    <_MainMenuList _menuMainname="menu_setup">
      <_munsubList>
        <_MenusubList _submeid="menu_company_profile" _submenuname1="1.1.1.กำหนดรายละเอียดบริษัท"
                      _isRead="true" _isAdd="true" _isEdit="true" _isDelete="false" />
        …
```
- 1 ไฟล์ ≈ 280 KB, 823 เมนูย่อยใน 11 เมนูหลัก (`menu_setup, menu_ic, menu_po, menu_so, menu_so_pos, menu_ap, menu_ar, menu_cash_and_bank, menu_asset, menu_general_ledger_main, menu_other_link`)
- `_submeid` = รหัสเมนูเดียวกับ [[menu-map]] (`menu_so_sale_order` ฯลฯ)
- แถวตัวอย่างนั้น: ทุกเมนู อ่าน/เพิ่ม/แก้ = true, ลบ = false

**กฎรวมสิทธิ์** (`MyLib/_global.cs` `_isAccessMenuPermision` ~2203):
1. อ่านสิทธิ์กลุ่มของทุกกลุ่มที่ผู้ใช้อยู่ (`sml_permissions_group where usercode in (select group_code from sml_user_and_group where user_code=?)`)
2. อ่านสิทธิ์ผู้ใช้ (`sml_permissions_user where upper(usercode)=?`)
3. **ผลลัพธ์ = กลุ่ม OR ผู้ใช้** แยกทีละสิทธิ์ (อ่าน/เพิ่ม/แก้/ลบ)
4. ถ้าไม่พบเมนูในไฟล์สิทธิ์ใดเลย: ผู้ใช้ `superadmin` ได้ทุกสิทธิ์; คนอื่นไม่ได้ (`false` ทั้งหมด)
5. `_nonPermission = true` (ตั้งในโปรแกรมย่อยบางตัว เช่น `SMLPOSChecker`, `ICCManage`) + `superadmin` ได้ทุกสิทธิ์สำหรับ `sml_soft_home_screen_menu_fast_report`
- ตอนเปิดหน้าหลัก `SMLAccount/_mainForm.cs` ~332 โหลด `_getUserAccessMenuPermissionAll()` + `_getGroupAccessMenuPermissionAll()` แล้วซ่อนเมนูที่ไม่มีสิทธิ์อ่าน (`_hideNode`)
- หน้าจอใช้ผลเป็นปุ่ม: เช่น `_icMain._saveData` — mode เพิ่มแต่ `_isAdd == false` → `warning19` (ไม่ให้บันทึก)

## 3. สิทธิ์ทางธุรกิจ (data database ของร้าน)
| ตาราง | คอลัมน์ที่เกี่ยวกับสิทธิ์ |
|---|---|
| `erp_user` | `branch_code`, `change_branch_code` (เปลี่ยนสาขาได้), `lock_bill`, `show_item_cost`, `disable_edit_doc_no_doc_date_user`, `reset_print_log`, `ic_wht`/`ic_shelf` (คลังเริ่มต้น), `price_level_1/2`, `discount_level_1`, `discount_bill_pos`, `cancel_pos_bill_level`, `delete_item_pos`, `open_cash_drawer`, `pos_cashier`, `approve_ar_credit`, `po_approve_from/to`, `sr_approve_from/to`, `ss_approve_from/to`, `cr_approve_from/to`, `max_cr_approve`, `sr/load_approve_percent`, `is_copy_doc`, `mobile_user`, `sale_hub_user`, `is_login_user` |
| `erp_user_group` | `is_po, is_so, is_wh, is_sale_group, is_pr_approve, is_po_approve, is_price_list_approve, is_so_approve, **is_change_masterdata**` |
| `erp_user_group_detail` | `group_code, user_code` |
| `erp_user_group_approve` | กลุ่มอนุมัติตาม `approve_flag` (0 = ใบสั่งซื้อ, 1 = ใบจอง SR, 2 = ใบสั่งขาย SS — จากชื่อ alias `po_/sr_/ss_approve_group` ใน query จริง) |

- โปรแกรมอ่านชุดนี้**ก่อนบันทึกเอกสารทุกครั้ง** (capture: `select coalesce(is_change_masterdata,1) … from erp_user_group …` และ `select change_branch_code, branch_code, lock_bill, … show_item_cost, disable_edit_doc_no_doc_date_user, reset_print_log, <กลุ่มอนุมัติ 0/1/2>, ic_wht, ic_shelf from erp_user where upper(code)=?`)
- **แก้ข้อมูลหลัก** = `erp_user_group.is_change_masterdata` (ค่าว่างถือเป็น 1) → `_allowChangeMaster` (`SMLERPGlobal/_global.cs` ~3728) → `_checkChangeMaster()` ([[write-spec-master-product]])
- ⚠️ ชื่อผู้ใช้ใน main database (`sml_user_list.user_code`) และใน data database (`erp_user.code`) เป็นคนละตาราง — โปรแกรมจับคู่ด้วยรหัสเดียวกัน

## 4. สำหรับ sml_mcp_ai
- ปัจจุบัน sml_mcp_ai ใช้ role ของตัวเอง 5 แบบจาก header/env ([[mcp-project]]) **ไม่ได้อิงสิทธิ์ SML** — ADR-001 ข้อ 5 กำหนดให้แก้ก่อนเปิดเขียน
- แนวทางที่ทำได้จากข้อมูลจริง: ผูก API key/ผู้ใช้ของ sml_mcp_ai กับ `user_code` ของ SML แล้ว
  1. ตรวจสิทธิ์เข้า database จาก `sml_database_list_user_and_group`
  2. ตรวจสิทธิ์เมนูของเอกสารที่จะเขียน ด้วยกฎ "กลุ่ม OR ผู้ใช้" ข้อ 2 (เช่น สร้างใบสั่งขาย = `menu_so_sale_order._isAdd`)
  3. ตรวจสิทธิ์ทางธุรกิจข้อ 3 (เปลี่ยนสาขา, เห็นต้นทุน, แก้ข้อมูลหลัก, ขีดอนุมัติ)
- ต้อง parse XML ~280 KB ต่อผู้ใช้ → cache ต่อ user + invalidate เมื่อ `guid_code` ของแถวเปลี่ยน (ยังไม่ได้ยืนยันว่าโปรแกรมเปลี่ยน `guid_code` ทุกครั้งที่แก้สิทธิ์)

## 5. ยังไม่ทราบ
- `system_id` ใน `sml_permissions_*` (ว่างทุกแถวที่ตรวจ)
- `active_status` ของผู้ใช้/กลุ่ม ถูกตรวจตอน login อย่างไร
- ความหมายตัวเลขของ `cancel_pos_bill_level`, `discount_level_1`, `price_level_*`
- โปรแกรมแก้ `guid_code` ของแถวสิทธิ์เมื่อบันทึกสิทธิ์ใหม่หรือไม่
