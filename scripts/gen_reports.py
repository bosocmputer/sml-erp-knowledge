#!/usr/bin/env python3
"""Generate 08-Reports/reports.md: catalogue of SML reports.

Sources:
  1. FastReport definitions in <db>.sml_fastreport (reportdata = zip with report template + SQL)
     -> report name, type, and the tables its SQL reads (only table names are written, no data)
  2. Code-based report screens from 04-Menu/menu-map.json (SMLERPReportTool, *Report modules)

Usage:
  export PGHOST=... PGPORT=... PGUSER=... PGPASSWORD=...
  python3 scripts/gen_reports.py aoy
"""
import base64
import collections
import io
import json
import pathlib
import re
import subprocess
import sys
import zipfile

VAULT = pathlib.Path(__file__).resolve().parent.parent
DB = sys.argv[1] if len(sys.argv) > 1 else "aoy"
OUT = VAULT / "08-Reports"
SQL_FROM = re.compile(r"\b(?:from|join)\s+([a-z_][a-z0-9_]*)", re.I)


def psql(sql):
    res = subprocess.run(["psql", "-d", DB, "-At", "-F", "\t", "-c", sql], capture_output=True, text=True, check=True)
    return [line.split("\t") for line in res.stdout.splitlines() if line]


def known_tables():
    return {r[0] for r in psql("select table_name from information_schema.tables where table_schema='public'")}


def tables_in_report(blob, tables):
    found, n_sql = collections.Counter(), 0
    try:
        z = zipfile.ZipFile(io.BytesIO(blob))
    except zipfile.BadZipFile:
        return found, -1
    for name in z.namelist():
        text = z.read(name).decode("utf-8", errors="ignore")
        text = text.replace("&#13;", " ").replace("&#10;", " ").replace("&quot;", '"').replace("&gt;", ">").replace("&lt;", "<")
        n_sql += len(re.findall(r"\bselect\b", text, re.I))
        for t in SQL_FROM.findall(text):
            if t.lower() in tables:
                found[t.lower()] += 1
    return found, n_sql


def main():
    OUT.mkdir(exist_ok=True)
    tables = known_tables()
    menu = {r["name"].lower(): r for r in json.loads((VAULT / "04-Menu/menu-map.json").read_text(encoding="utf-8"))}
    rows = psql("select menuid, menuname, report_type, is_system_report, translate(encode(reportdata,'base64'), E'\\n', '') from sml_fastreport order by menuid")
    fr, by_table = [], collections.defaultdict(list)
    for menuid, menuname, rtype, system, b64 in rows:
        blob = base64.b64decode(b64.replace("\\n", "")) if b64 else b""
        found, n_sql = tables_in_report(blob, tables)
        m = menu.get(menuid.lower())
        fr.append((menuid, menuname, rtype, system, n_sql, [t for t, _ in found.most_common()], " › ".join(m["path"]) if m else ""))
        for t in found:
            by_table[t].append(menuid)
    code_reports = [r for r in menu.values() if r["class"] and r["class"] != "SMLFastReport._designer"
                    and re.search(r"report|Report|_reportTrans|_viewReport", r["class"] + r.get("base", ""))]

    L = ["---", "tags: [sml, reports, generated]", "---", "# รายงานทั้งหมด", "",
         f"> สร้างอัตโนมัติด้วย `scripts/gen_reports.py {DB}` — เก็บเฉพาะชื่อรายงานและชื่อตาราง ไม่มีข้อมูลธุรกิจ กลับไป [[00-Index]] · [[module-reports]]", "",
         "## เครื่องมือรายงาน 3 แบบ", "",
         "1. **FastReport** — เมนู tag `fastreport` → `SMLFastReport._designer._load(menuName)` โหลดแบบรายงานจากตาราง `sml_fastreport` (คอลัมน์ `reportdata` เป็น zip ที่มี template + SQL) ซึ่ง sync มาจาก master server `ws.smlaccount.com` / DB `SMLMASTER` ตาม `timeupdate`",
         "2. **รายงานเอกสารตาม trans_flag** — `SMLERPReportTool._reportTrans(reportEnum, transType, screenName)` และตระกูล `_reportCashBankTrans`, `_reportArApTrans` (เขียนในโค้ด)",
         "3. **รายงานเฉพาะ** — คลาสใน `SMLERP*Report`, `SINGHAReport` ที่สืบจาก `SMLReport._report._viewReport` หรือ UserControl", "",
         f"## FastReport ใน `{DB}` ({len(fr)} รายงาน)", "",
         "`report_type` / `is_system_report` ยังไม่ได้ยืนยันความหมาย", "",
         "| menuid | ชื่อ | type | system | จำนวน SELECT | ตารางที่อ่าน | อยู่ในเมนู |", "|---|---|---|---|---|---|---|"]
    for menuid, name, rtype, system, n_sql, tbls, path in fr:
        L.append(f"| `{menuid}` | {name} | {rtype} | {system} | {n_sql if n_sql >= 0 else 'ไม่ใช่ zip'} | {', '.join(tbls[:8])} | {path} |")
    L += ["", "## ตาราง → FastReport ที่อ่านตารางนั้น", "", "| ตาราง | จำนวนรายงาน | ตัวอย่าง |", "|---|---|---|"]
    for t, ids in sorted(by_table.items(), key=lambda kv: -len(kv[1]))[:60]:
        L.append(f"| `{t}` | {len(ids)} | {', '.join(ids[:6])} |")
    L += ["", f"## รายงานที่เขียนในโค้ด ({len(code_reports)} เมนู)", "", "| เมนู | menu name | คลาส | reportEnum / trans_flag |", "|---|---|---|---|"]
    for r in sorted(code_reports, key=lambda r: r["path"]):
        L.append(f"| {' › '.join(r['path'] + [r['text']])} | `{r['name']}` | `{r['class']}` | {', '.join(r['report_enum'][:1] + [str(x) for x in r['trans_flag']])} |")
    (OUT / "reports.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    bad = sum(1 for x in fr if x[4] < 0)
    print(f"fastreport={len(fr)} (not zip: {bad}), with tables={sum(1 for x in fr if x[5])}, code reports={len(code_reports)}")


if __name__ == "__main__":
    main()
