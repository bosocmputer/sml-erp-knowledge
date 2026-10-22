#!/usr/bin/env bash
# Regenerate every generated note from the current smlerp / smljavaws2 code (and DB when PG* env is set).
# Usage:
#   scripts/regenerate_all.sh                 # code-based notes only
#   PGHOST=... PGPORT=... PGUSER=... PGPASSWORD=... scripts/regenerate_all.sh --with-db
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/gen_menu.py
python3 scripts/gen_modules.py
python3 scripts/gen_dictionary.py
python3 scripts/gen_enums.py
python3 scripts/gen_options.py
python3 scripts/gen_menu_map.py
python3 scripts/gen_module_notes.py
python3 scripts/gen_docflow.py
python3 scripts/gen_gl_actions.py
python3 scripts/gen_code_reports.py
python3 scripts/gen_webservice_api.py
python3 scripts/gen_error_messages.py   # needs menu-map.json (gen_menu_map.py)

if [[ "${1:-}" == "--with-db" ]]; then
  scripts/gen_schema.sh kbyt
  python3 scripts/gen_reports.py aoy
fi

git status --short
