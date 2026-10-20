#!/usr/bin/env python3
"""Generate the SML data dictionary (table/column meanings in Thai/English).

Sources (official SML design files in smlerp/SMLERPTemplate):
  smldatabase.xml             table + field: thai/eng label, type, length, null, indexes, xversion
  SMLDatabaseDesign_New.xml   module grouping of each table (Setup, Master, GL, IC, IC_Trans, AP_AR, POS ...)

Writes:
  02-Database/dictionary/dictionary-index.md
  02-Database/dictionary/dict-<module>.md
  02-Database/dictionary.json   [{table, module, thai, eng, fields:[{name, thai, eng, type, length, null}], indexes}]

Usage: python3 scripts/gen_dictionary.py [path/to/smlerp]
"""
import collections
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
SRC = ERP / "SMLERPTemplate"
OUT = VAULT / "02-Database/dictionary"

MODULE_TH = {
    "Setup": "ตั้งค่าระบบ", "Master": "ข้อมูลหลัก", "GL": "บัญชีแยกประเภท", "Asset": "สินทรัพย์", "Cash_Bank": "เงินสด/ธนาคาร",
    "IC": "สินค้า", "IC_Trans": "เอกสารสินค้า (ic_trans)", "AP_AR": "ลูกหนี้/เจ้าหนี้", "AP_AR_Trans": "เอกสารลูกหนี้/เจ้าหนี้",
    "POS": "POS", "WMS": "คลังสินค้า WMS", "IMEX": "IMEX (OEM)", "Healthy": "สุขภาพ/ร้านยา", "Temp": "ตารางชั่วคราว",
    "Report": "รายงาน", "EDI": "EDI", "Pick_and_Pack": "Pick and Pack", "Thai7": "Thai7", "Draft": "ร่างเอกสาร",
    "Form": "ฟอร์มพิมพ์", "Sync": "Sync", "Mobillyst_TMS": "Mobillyst TMS", "Utility": "Utility", "Cloud": "Cloud", "E-Tax": "e-Tax",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    module_of = {}
    design = ET.parse(SRC / "SMLDatabaseDesign_New.xml").getroot()
    for t in design.iter("_tableList"):
        module_of[t.get("_name")] = t.get("_moduleName") or "Other"

    root = ET.parse(SRC / "smldatabase.xml").getroot()
    tables = []
    for t in root.findall("table"):
        name = t.get("name")
        fields = [{"name": f.get("name"), "thai": (f.get("thai") or "").strip(), "eng": (f.get("eng") or "").strip(),
                   "type": f.get("type"), "length": f.get("length"), "null": f.get("allow_null"),
                   "resource_only": f.get("resource_only") == "true"} for f in t.findall("field")]
        indexes = [{"name": i.get("index_name"), "field": i.get("field")} for i in t.findall("index")]
        tables.append({"table": name, "module": module_of.get(name, "Other"), "thai": (t.get("thai") or "").strip(),
                       "eng": (t.get("eng") or "").strip(), "xversion": t.get("xversion") or "", "fields": fields, "indexes": indexes})

    (VAULT / "02-Database/dictionary.json").write_text(json.dumps(tables, ensure_ascii=False, indent=1), encoding="utf-8")

    by_mod = collections.defaultdict(list)
    for t in tables:
        by_mod[t["module"]].append(t)
    for old in OUT.glob("dict-*.md"):
        old.unlink()
    idx = ["---", "tags: [sml, database, dictionary, generated]", "---", "# พจนานุกรมข้อมูล SML (Data Dictionary)", "",
           "> สร้างอัตโนมัติด้วย `scripts/gen_dictionary.py` จากไฟล์ออกแบบทางการของ SML (`SMLERPTemplate/smldatabase.xml` + `SMLDatabaseDesign_New.xml`) — คำอธิบายภาษาไทย/อังกฤษทุกคอลัมน์ ข้อมูลดิบสำหรับ agent: `02-Database/dictionary.json`", "",
           f"ทั้งหมด {len(tables)} ตาราง {sum(len(t['fields']) for t in tables):,} คอลัมน์ · โครงสร้างจริงใน DB ดู [[schema-index]] · ที่เก็บเอกสาร [[data-model]] · กลับไป [[00-Index]]", "",
           "หมายเหตุ: `resource_only=true` = คอลัมน์ที่มีไว้เป็นป้ายบนหน้าจอ/รายงาน ไม่ได้สร้างใน DB", "",
           "| โมดูล | ความหมาย | ตาราง | โน้ต |", "|---|---|---|---|"]
    for mod in sorted(by_mod, key=lambda m: -len(by_mod[m])):
        ts = sorted(by_mod[mod], key=lambda t: t["table"])
        slug = re.sub(r"[^a-z0-9]+", "-", mod.lower()).strip("-")
        idx.append(f"| {mod} | {MODULE_TH.get(mod, '')} | {len(ts)} | [[dict-{slug}]] |")
        L = ["---", f"tags: [sml, dictionary, {slug}, generated]", f"module: {mod}", "---",
             f"# พจนานุกรม: {mod} — {MODULE_TH.get(mod, '')}", "", "กลับไป [[dictionary-index]]", "",
             "| ตาราง | ความหมาย | คอลัมน์ |", "|---|---|---|"]
        L += [f"| [[#{t['table']}]] | {t['thai']} {('/ ' + t['eng']) if t['eng'] else ''} | {len(t['fields'])} |" for t in ts]
        L.append("")
        for t in ts:
            L += [f"## {t['table']}", "", f"**{t['thai']}**" + (f" — {t['eng']}" if t["eng"] else "") + (f" · edition: `{t['xversion']}`" if t["xversion"] else ""), "",
                  "| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |", "|---|---|---|---|---|"]
            for f in t["fields"]:
                typ = f["type"] + (f"({f['length']})" if f["length"] not in (None, "0", "") else "")
                ro = " *(resource only)*" if f["resource_only"] else ""
                L.append(f"| `{f['name']}` | {f['thai']}{ro} | {f['eng']} | {typ} | {'✓' if f['null'] == 'true' else ''} |")
            if t["indexes"]:
                L += ["", "index: " + ", ".join(f"`{i['name']}`({i['field']})" for i in t["indexes"])]
            L.append("")
        (OUT / f"dict-{slug}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (OUT / "dictionary-index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"tables={len(tables)} modules={len(by_mod)}")


if __name__ == "__main__":
    main()
