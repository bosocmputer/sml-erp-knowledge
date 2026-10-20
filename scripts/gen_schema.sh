#!/usr/bin/env bash
# Generate 02-Database/schema/<prefix>.md (tables + columns) from a SML data database.
# Reads only information_schema / pg_stat (no business rows).
#
# Usage:
#   export PGHOST=... PGPORT=... PGUSER=... PGPASSWORD=...   # never commit credentials
#   scripts/gen_schema.sh kbyt
set -euo pipefail

DB="${1:?usage: gen_schema.sh <database>}"
VAULT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$VAULT/02-Database/schema"
mkdir -p "$OUT"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

psql -d "$DB" -At -F $'\t' -c "
  select c.table_name, c.column_name, c.data_type,
         coalesce(c.character_maximum_length::text, ''),
         coalesce(s.n_live_tup, 0)
  from information_schema.columns c
  join information_schema.tables t
    on t.table_schema = c.table_schema and t.table_name = c.table_name and t.table_type = 'BASE TABLE'
  left join pg_stat_user_tables s on s.schemaname = c.table_schema and s.relname = c.table_name
  where c.table_schema = 'public'
  order by c.table_name, c.ordinal_position;" > "$TMP"

python3 - "$TMP" "$OUT" "$DB" <<'PY'
import collections, pathlib, re, sys
rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
out, db = pathlib.Path(sys.argv[2]), sys.argv[3]
tables = collections.OrderedDict()
for table, col, typ, length, est in rows:
    tables.setdefault(table, {"est": int(est), "cols": []})["cols"].append((col, typ + (f"({length})" if length else "")))

def prefix(name):
    if re.search(r"_\d{8}_\d{6}$", name):
        return "backup"
    return name.split("_")[0]

groups = collections.defaultdict(list)
for name in tables:
    groups[prefix(name)].append(name)

for old in out.glob("*.md"):
    old.unlink()
index = ["---", "tags: [sml, database, schema, generated]", "---",
         f"# Schema ของ database `{db}`", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_schema.sh` จาก information_schema — ไม่มีข้อมูลธุรกิจ, จำนวนแถวเป็นค่าประมาณจาก pg_stat", "",
         f"ทั้งหมด {len(tables)} ตาราง ดูภาพรวมที่ [[database-layout]] และความหมายประเภทเอกสารที่ [[trans_flag]]", "",
         "| กลุ่ม (prefix) | จำนวนตาราง | ไฟล์ |", "|---|---|---|"]
for g in sorted(groups, key=lambda k: -len(groups[k])):
    names = groups[g]
    index.append(f"| `{g}` | {len(names)} | [[schema-{g}]] |")
    lines = ["---", f"tags: [sml, schema, {g}, generated]", "---", f"# ตารางกลุ่ม `{g}` ({db})", "", "กลับไป [[schema-index]]", ""]
    for name in sorted(names):
        t = tables[name]
        lines += [f"## {name}", "", f"แถวโดยประมาณ: {t['est']:,}", "", "| คอลัมน์ | ชนิด |", "|---|---|"]
        lines += [f"| {c} | {ty} |" for c, ty in t["cols"]]
        lines.append("")
    (out / f"schema-{g}.md").write_text("\n".join(lines), encoding="utf-8")
(out / "schema-index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
print(f"wrote {len(groups)} group files, {len(tables)} tables")
PY
