#!/usr/bin/env python3
"""Generate one note per top-level menu (module) from 04-Menu/menu-map.json.

Each note: curated summary (CURATED below, edit here), stats, core controls, trans_flags,
tables, and the full screen list. Run gen_menu_map.py first.

Usage: python3 scripts/gen_module_notes.py
"""
import collections
import json
import pathlib
import re

VAULT = pathlib.Path(__file__).resolve().parent.parent
ROWS = json.loads((VAULT / "04-Menu/menu-map.json").read_text(encoding="utf-8"))
OUT = VAULT / "05-Modules"
FLAG_NAMES = dict(re.findall(r"^\| (\d+) \| (.+?) \|$", (VAULT / "03-Reference/trans_flag.md").read_text(encoding="utf-8"), flags=re.M))

SLUG = {
    "เริ่มต้น": "setup", "สินค้า": "inventory", "ซื้อ": "purchase", "ขาย": "sales", "ขาย POS": "pos",
    "ลูกหนี้": "ar", "เจ้าหนี้": "ap", "เงินสด/ธนาคาร": "cashbank", "บัญชี": "gl", "คลัง": "warehouse",
    "คลังสินค้า": "wms", "ค่าเสื่อม": "asset", "รายงาน": "reports", "MIS": "mis", "Mobile Sales": "mobile-sales",
    "Data": "data", "Mobillyst TMS": "tms", "EDI": "edi",
}

# Curated knowledge per module (keep short, factual, cite verification status)
CURATED = {
    "ขาย": [
        "เอกสารขายทุกประเภทเปิดด้วย `_icTransControl` ต่างกันที่ `_transControlType` ดู [[document-engine]]",
        "สายเอกสาร: เสนอราคา (30) → สั่งจอง (34) → สั่งขาย (36) → ขาย (44) → ลดหนี้ (48) / เพิ่มหนี้ (46); ยกเลิกเป็นเอกสารแยก (เช่น 45)",
        "ขายหน้าจอปกติ `is_pos=0`; บิล POS ดูได้จากเมนูเดียวกันแต่ `is_pos=1` แบบอ่านอย่างเดียว (ยืนยันกับ AOY: 132/649 ใบเป็น POS)",
        "ขายเงินสดสร้าง `cb_trans`, ขายเชื่อไปตั้งหนี้และรับชำระด้วยเอกสารลูกหนี้ 239 ดู [[data-model]]",
    ],
    "ขาย POS": [
        "หน้าจอขายหน้าร้านจริงอยู่ในโปรเจกต์ `SMLPOSClient` (ยังไม่ได้ไล่ละเอียด) ส่วนเมนูนี้เป็นการตั้งค่า/ดูข้อมูล POS",
        "บิล POS บันทึกเป็น `ic_trans` flag 44 `is_pos=1` (ยืนยันกับ AOY)",
        "ตั้งค่า POS อยู่ในเมนูเริ่มต้น: ค่าเริ่มต้น POS, รหัสเครื่อง POS, เงื่อนไขสะสมแต้ม",
    ],
    "ซื้อ": [
        "รายละเอียดเชิงลึก: [[write-spec-purchase]]",
        "สายเอกสาร: เสนอซื้อ (2) → อนุมัติ (4) → ใบสั่งซื้อ (6) → อนุมัติ (8) → ซื้อ/รับสินค้า (12) → ส่งคืน/ลดหนี้ (16); มีแบบรับบางส่วน (partial, 310+)",
        "ใช้ `_icTransControl` เหมือนฝั่งขาย ดู [[document-engine]]",
        "เอกสารที่เหมาะให้ AI สร้างเป็นร่าง: ใบเสนอซื้อ (2) เพราะยังต้องอนุมัติและไม่กระทบสต็อก",
    ],
    "สินค้า": [
        "ข้อมูลหลักสินค้า `ic_inventory` (+ barcode, หน่วย, ราคา) และเอกสารสต็อก: ยกมา 54, เบิก 56, รับคืนจากเบิก 58, รับสำเร็จรูป 60, ปรับปรุง 66/68, โอน 70/72, ตรวจนับ",
        "เอกสารสต็อกส่วนใหญ่เปิดด้วย `SMLInventoryControl._clone_icTrans(transType, menuName)`",
        "ต้นทุนคำนวณหลังบันทึกผ่าน web service (Average/FIFO/Lot) ดู [[document-engine]]",
    ],
    "ลูกหนี้": [
        "รายละเอียดเชิงลึก: [[write-spec-receipt]], ใบวางบิล [[write-spec-billing-note]]",
        "เอกสารลูกหนี้เก็บใน `ap_ar_trans` / `ap_ar_trans_detail` (ไม่ใช่ ic_trans): ตั้งหนี้ยกมา 93, ใบวางบิล 235, รับชำระ 239 (ยืนยันกับ AOY)",
        "หน้าจอกลาง `SMLAPARControl._ar_ap_trans`; หลังบันทึกเรียก `_process_ap_ar_flow` อัปเดตยอดค้างของบิลขาย",
        "ข้อมูลลูกค้า `ar_customer` / `ar_customer_detail`; วงเงินเครดิตตรวจตอนบันทึกเอกสารขาย",
    ],
    "เจ้าหนี้": [
        "รายละเอียดเชิงลึก: [[write-spec-ap-payment]]",
        "เอกสารเจ้าหนี้เก็บใน `ap_ar_trans`: ตั้งหนี้ยกมา 81, รับวางบิล 213, จ่ายชำระ 19 (ยืนยันกับ AOY)",
        "หน้าจอกลาง `SMLAPARControl._ar_ap_trans` (เดียวกับลูกหนี้)",
    ],
    "เงินสด/ธนาคาร": [
        "รายละเอียดเชิงลึก: [[cash-bank]]",
        "การรับ/จ่ายเงินเก็บใน `cb_trans` / `cb_trans_detail` โดยใช้ trans_flag ของเอกสารต้นทาง; ทะเบียนเช็ค `cb_chq_list`",
        "รายได้อื่น 250 / รายจ่ายอื่น 260 มีหัวเอกสารใน `ic_trans` ด้วย (ยืนยันกับ AOY)",
        "วงจรเช็ค: รับ/จ่าย, ฝาก (410), ผ่าน (411/451), คืน, เปลี่ยนเช็ค — มีสถานะละเอียด เหมาะกับพยากรณ์กระแสเงินสด",
        "control ส่วนกลาง `SMLERPControl._bank._bankControl`",
    ],
    "บัญชี": [
        "รายละเอียดเชิงลึก: ภาษีและงวดบัญชี [[tax-period]]",
        "สมุดรายวัน `gl_journal` / `gl_journal_detail`, ผังบัญชี `gl_chart_of_account`, ภาษี `gl_journal_vat_buy` / `_sale`",
        "GL ส่วนใหญ่สร้างอัตโนมัติจากเอกสาร (`_processGLByTrans`) เมื่อเปิด `gl_process_realtime`; หน้าจอบันทึกมือ `SMLERPGLControl._journalScreen`",
        "AOY: 176 จาก 188 รายการ GL ผูก doc_no กับ ic_trans",
    ],
    "เริ่มต้น": [
        "รายละเอียดเชิงลึก: สิทธิ์ผู้ใช้ [[permissions]], งวดบัญชี/ล็อกวันที่ [[tax-period]]",
        "ตั้งค่าบริษัท สาขา แผนก พนักงาน กลุ่มเอกสาร รูปแบบเลขที่เอกสาร และข้อมูลหลักต่าง ๆ",
        "หน้าจอข้อมูลหลักส่วนใหญ่ใช้ `MyLib._manageMasterCodeFull` ผูก 1 เมนู = 1 ตาราง (ดูคอลัมน์ตารางด้านล่าง)",
    ],
    "รายงาน": [
        "รายละเอียดเชิงลึก: สูตรรายงานหลัก [[report-formulas]]",
        "รายงานใช้เครื่องมือ 3 แบบ: `SMLFastReport._designer` (รายงานที่โหลดตามชื่อเมนู), `SMLERPReportTool._reportTrans` (รายงานเอกสารตาม trans_flag), `SMLReport._report._viewReport`",
        "ดูรายการรายงานทั้งหมดที่ [[reports]]",
    ],
}


def main():
    by_top = collections.defaultdict(list)
    for r in ROWS:
        by_top[r["path"][0] if r["path"] else "(root)"].append(r)
    index = ["---", "tags: [sml, modules, generated]", "---", "# โมดูลตามเมนูหลัก", "",
             "> สร้างอัตโนมัติด้วย `scripts/gen_module_notes.py` จาก [[menu-map]] — ส่วนสรุปแก้ได้ที่ `CURATED` ในสคริปต์", "",
             "| เมนูหลัก | โน้ต | เมนู | จับคู่คลาส |", "|---|---|---|---|"]
    for top, rows in by_top.items():
        slug = SLUG.get(top, re.sub(r"\W+", "-", top).strip("-").lower() or "other")
        mapped = [r for r in rows if r["class"]]
        flags = collections.Counter(f for r in rows for f in r["trans_flag"])
        tables = collections.Counter(t for r in rows for t in r.get("tables", []))
        cores = collections.Counter(e for r in rows for e in r.get("embedded", []) if not e.startswith("MyLib."))
        classes = collections.Counter(r["class"] for r in mapped)
        L = ["---", f"tags: [sml, module, {slug}, generated]", f"menu_group: \"{top}\"",
             f"trans_flags: [{', '.join(str(f) for f in sorted(flags))}]", "---",
             f"# โมดูล: {top}", "", "กลับไป [[modules-index]] · [[00-Index]]", ""]
        if top in CURATED:
            L += ["## สรุปการทำงาน", ""] + [f"- {x}" for x in CURATED[top]] + [""]
        L += ["## ตัวเลข", "", f"- เมนูปลายทาง {len(rows)} รายการ, จับคู่คลาสได้ {len(mapped)}, เห็นใน SMLAccountPOSProfessional (edition 13) {sum(1 for r in rows if r.get('pos_pro'))}",
              f"- คลาสหน้าจอที่ใช้บ่อย: " + ", ".join(f"`{c}` ({n})" for c, n in classes.most_common(6)),
              f"- control หลักที่ฝัง: " + (", ".join(f"`{c}` ({n})" for c, n in cores.most_common(6)) or "-"), ""]
        if flags:
            L += ["## ประเภทเอกสาร (trans_flag) ที่เมนูในโมดูลนี้ใช้", "", "| trans_flag | ชื่อ | จำนวนเมนู |", "|---|---|---|"]
            L += [f"| {f} | {FLAG_NAMES.get(str(f), '')} | {n} |" for f, n in sorted(flags.items())] + [""]
        if tables:
            L += ["## ตารางที่หน้าจออ้างถึง (static, ไม่นับ control กลาง)", "", ", ".join(f"`{t}`" for t, _ in tables.most_common(40)), ""]
        L += ["## เมนูทั้งหมด", "", "| เมนู | menu name | เลข POS Pro | คลาส | trans_flag | ตาราง |", "|---|---|---|---|---|---|"]
        for r in rows:
            sub = " › ".join(r["path"][1:] + [r["text"]])
            L.append(f"| {sub} | `{r['name'].strip()}` | {r.get('numbers', {}).get('AccPOSPro', '')} | {('`' + r['class'] + '`') if r['class'] else r['route']} | "
                     f"{', '.join(map(str, r['trans_flag']))} | {', '.join(r.get('tables', [])[:4])} |")
        (OUT / f"module-{slug}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        index.append(f"| {top} | [[module-{slug}]] | {len(rows)} | {len(mapped)} |")
    (OUT / "modules-index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"wrote {len(by_top)} module notes")


if __name__ == "__main__":
    main()
