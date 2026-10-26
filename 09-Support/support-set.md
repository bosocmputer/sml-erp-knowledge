---
tags: [sml, support, policy]
date: 2026-10-22
---
# ชุดความรู้สำหรับพนักงาน support (support set)

กลับไป [[00-Index]] · มติที่มา [[team-review-2026-10-22-support-use]] (S1–S3)

## หลักการ
- support ใช้ความรู้นี้**ผ่าน AI** (skill `sml-support`) หรืออ่านเองใน Obsidian จาก**ชุดที่ export แล้วเท่านั้น** — ห้ามแจก vault ทั้งก้อน (มติ S2)
- ชุด support สร้างด้วย `scripts/export_support.py` ทุกครั้ง (ห้าม copy มือ) — script กรอง/แทนที่ข้อมูลภายใน และ**ล้มทันที**ถ้าเจอข้อมูลต้องห้ามที่กรองไม่ได้
- ทุกคำตอบต้องบอกระดับความเชื่อมั่น ✅ / 🔶 (มติ S3) และเรื่องใน [[00-Unverified]] ต้องส่งต่อ dev

## โน้ตที่ให้ (allow-list)
| กลุ่ม | โน้ต | เหตุผล |
|---|---|---|
| Support | `09-Support/faq.md`, `09-Support/error-messages.md` | สร้างมาเพื่อ support โดยตรง |
| เมนู | `04-Menu/menu-map.md`, `04-Menu/menu-map-pos.md`, `04-Menu/menu-tree.md`, `05-Modules/*.md` | หาเมนู/หน้าจอ และเลขเมนูที่ร้านเห็นตามรุ่น |
| กฎของโปรแกรม | `03-Reference/trans_flag.md`, `doc-flow-rules.md`, `company-options.md`, `enums.md`, `gl-action-codes.md` | อธิบาย "ทำไมโปรแกรมทำแบบนี้" |
| การทำงาน | `01-Architecture/stock-cost.md`, `pricing-vat-gl.md`, `tax-period.md`, `permissions.md`, `cash-bank.md`, `document-engine.md`, `pos-client.md`, `print-forms.md`, `data-model.md` | support ระดับ 2 |
| รายงาน | `08-Reports/report-formulas.md`, `08-Reports/reports.md` | ตรวจตัวเลขรายงาน |
| ความหมายข้อมูล | `02-Database/dictionary/*.md` | ความหมายคอลัมน์ภาษาไทย (จากไฟล์ออกแบบของโปรแกรม) |
| คำเตือน | `00-Unverified.md` | รู้ว่าเรื่องไหนต้องส่งต่อ dev |

## โน้ตที่ไม่ให้ (deny) และเหตุผล
| โน้ต | เหตุผล |
|---|---|
| `01-Architecture/server-layout.md`, `runtime-verified.md`, `login-flow.md`, `architecture.md`, `webservice-api.md` | โครงสร้าง server, IP, port, main database ของ provider, รายการ API (พื้นผิวโจมตี) |
| `02-Database/` ยกเว้น `dictionary/` (schema dump, `tenants-overview`, `database-layout`, `aoy-settings`, `sql-capture-*`, `phase2-tcpdump`) | ข้อมูลของร้าน/tenant, วิธีดักจับ, การเชื่อมต่อ database |
| `06-sml_mcp_ai/*` | การออกแบบผลิตภัณฑ์ภายใน, ช่องโหว่ที่ยังไม่แก้, สเปกการเขียนข้อมูล |
| `07-Product/*` | ไอเดียผลิตภัณฑ์ภายใน |
| `00-Index`, `00-Completeness`, `00-Gap-Review`, `CLAUDE.md`, `README.md`, `scripts/` | สถานะ/วิธีทำงานของทีม dev (ชุด support มี README ของตัวเอง) |
| `08-Reports/code-reports.md`, `04-Menu/screen-classes.md`, `04-Menu/menu-map.json`, `04-Menu/menu-map-pos.json` | ระดับโค้ด ไม่จำเป็นสำหรับ support |

## การแปลงตอน export (ทำอัตโนมัติ)
| สิ่งที่เจอในโน้ตที่ให้ | ทำอย่างไร |
|---|---|
| ชื่อ database ของร้าน/tenant (เช่น aoy, kbgtest, samai, wawacrm, kbyt, `smlerpmain…`) | แทนด้วย "ร้านทดสอบ" |
| IP (เช่น `172.18.0.3`) | แทนด้วย "<ip ภายใน>" |
| บรรทัดที่พูดถึง sml_mcp_ai / Nexflow / sml-api-bybos / openclaw / loyalty | ตัดทั้งบรรทัด |
| ชื่อไฟล์ capture (`aoy-runN`) | แทนด้วย "การทดสอบภายใน" |
| ลิงก์ `[[…]]` ไปโน้ตที่ไม่ได้อยู่ในชุด | เปลี่ยนเป็นข้อความ "…(เอกสารภายในทีม dev)" |
| host/path ภายใน (`nextstep`, `iszai`, `/home/`, `sshpass`) | **หยุด export** — ต้องแก้ต้นทางก่อน |

## วิธีสร้างและแจกชุด
```bash
python3 scripts/export_support.py ~/dev/sml-knowledge-support
```
- ผลลัพธ์: โฟลเดอร์ Obsidian ที่เปิดได้ทันที + `README.md` + `skill/sml-support/SKILL.md`
- สร้างใหม่ทุกครั้งที่ vault เปลี่ยน (โฟลเดอร์ปลายทางถูกล้างแล้วเขียนใหม่)
- แจกผ่านช่องทางที่ควบคุมสิทธิ์ได้ (ห้ามเปิดสาธารณะ)
- ใช้กับ AI: คัดลอก `skill/sml-support` ในชุดที่ export ไปที่ `~/.claude/skills/` ของเครื่อง support (skill อ่านชุดจาก `~/dev/sml-knowledge-support` เป็นค่าเริ่มต้น ถ้าวางที่อื่นให้บอก AI ตำแหน่ง)
- export ครั้งแรก 2026-10-22: 68 ไฟล์, แทนชื่อร้าน 68 จุด, IP 1, ตัดบรรทัดภายใน 13, เปลี่ยนลิงก์ภายใน 133 — ตรวจซ้ำด้วย grep ไม่พบ host/IP/รหัสร้านเหลือ
