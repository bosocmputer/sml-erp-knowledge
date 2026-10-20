#!/usr/bin/env python3
"""Generate the menu -> screen map for SMLAccount.

Reads:
  smlerp/SMLAccount/menu.json            menu tree (name, text, tag)
  smlerp/SMLAccount/_mainForm.cs         dispatcher: tag -> _selectMenuXxx -> <Module>._selectMenu
  smlerp/*/_selectMenu.cs                per-module switch: menu name -> new ScreenClass(args)
  smlerp/**/*.cs                         class index: class -> file, base class
  smlerp/SMLERPGlobal/_global.cs         _transFlag() enum -> trans_flag number

Writes:
  04-Menu/menu-map.md        human/Obsidian view grouped by top menu
  04-Menu/menu-map.json      machine-readable rows for AI agents
  04-Menu/screen-classes.md  screen classes grouped by base class (screen templates)

Usage: python3 scripts/gen_menu_map.py [path/to/smlerp]
"""
import collections
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
OUT_DIR = VAULT / "04-Menu"


def read(p):
    return p.read_text(encoding="utf-8-sig", errors="ignore")


def strip_comments(src):
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"//[^\n]*", "", src)


# --- trans_flag numbers -----------------------------------------------------
def trans_flag_map():
    g = read(ERP / "SMLERPGlobal/_global.cs")
    start = g.find("public static int _transFlag(")
    body = g[start:start + 60000]
    return {m.group(1): int(m.group(2)) for m in re.finditer(r"case _transControlTypeEnum\.([^:\s]+)\s*:\s*return\s+(\d+)", body)}


# --- class index ------------------------------------------------------------
CLASS_RE = re.compile(r"\bclass\s+(\w+)\s*(?::\s*([\w.]+))?")
NS_RE = re.compile(r"\bnamespace\s+([\w.]+)")


def class_index():
    idx = collections.defaultdict(list)  # simple name -> [(namespace, file, base)]
    for p in ERP.rglob("*.cs"):
        if "/obj/" in p.as_posix() or "/bin/" in p.as_posix():
            continue
        src = strip_comments(read(p))
        ns = NS_RE.search(src)
        ns = ns.group(1) if ns else ""
        for m in CLASS_RE.finditer(src):
            base = m.group(2) or ""
            idx[m.group(1)].append((ns, p.relative_to(ERP).as_posix(), base))
    return idx


def resolve(cls, module_ns, idx):
    """Return (qualified name, file, base) for a 'new X' expression."""
    simple = cls.split(".")[-1]
    ns_hint = ".".join(cls.split(".")[:-1]) or module_ns
    cands = idx.get(simple, [])
    best = [c for c in cands if c[0] == ns_hint] or [c for c in cands if c[0].startswith(module_ns)] or cands
    with_base = [c for c in best if c[2]] or best
    if not with_base:
        return cls, "", ""
    ns, f, base = with_base[0]
    return (f"{ns}.{simple}" if ns else simple), f, base


# --- controls embedded by a screen (designer) -------------------------------
CORE_RE = re.compile(r"new\s+((?:SMLInventoryControl|SMLERPAPARControl|SMLERPCASHBANK|SMLERPGLControl|SMLERPControl|SMLPOSControl|MyLib)\.\w+)\s*\(")
_emb_cache = {}
_tbl_cache = {}


def embedded(rel):
    if rel in _emb_cache:
        return _emb_cache[rel]
    p = ERP / rel
    files = [p] + [q for q in p.parent.glob(p.stem + ".*esigner.cs")]
    src = "".join(strip_comments(read(f)) for f in files if f.exists())
    keep_mylib = {"MyLib._myManageData", "MyLib._managerMasterScreenClass", "MyLib._ManageTransData", "MyLib._searchDataFull"}
    tables = collections.Counter(re.findall(r"_g\.d\.(\w+)\._table", src))
    _tbl_cache[rel] = [t for t, _ in tables.most_common(25)]
    emb = sorted({m.group(1) for m in CORE_RE.finditer(src)
                  if not m.group(1).startswith("MyLib.") or m.group(1) in keep_mylib} - {"MyLib._myGrid", "MyLib._myScreen", "MyLib._myTextBox", "MyLib._myLabel", "MyLib._myButton", "MyLib._myPanel", "MyLib._myToolStripButton", "MyLib._myShadowLabel", "MyLib._myTabControl", "MyLib._myCheckBox", "MyLib._myGroupBox", "MyLib._myComboBox", "MyLib._myFlowLayoutPanel", "MyLib._myTabPage"})
    enums = sorted(set(re.findall(r"_transControlType\s*=\s*_g\.g\._transControlTypeEnum\.([^\s;,)]+)", src)))
    _emb_cache[rel] = (emb, enums)
    return emb, enums


# --- dispatcher -------------------------------------------------------------
def dispatcher():
    src = strip_comments(read(ERP / "SMLAccount/_mainForm.cs"))
    fn_to_module = {}
    for m in re.finditer(r"void\s+(_selectMenu\w+)\s*\([^)]*\)\s*\{(.*?)\n        \}", src, flags=re.S):
        mod = re.search(r"([\w.]+)\._selectMenu\._getObject", m.group(2))
        if mod:
            fn_to_module[m.group(1)] = mod.group(1)
    tag_to_module, tag_order = {}, []
    for m in re.finditer(r'tag\.IndexOf\("&(\w+)&"\)\s*!=\s*-1\s*\)\s*\{\s*(\w+)\(', src):
        tag, fn = m.group(1), m.group(2)
        if tag not in tag_to_module:
            tag_to_module[tag] = fn_to_module.get(fn, fn)
            tag_order.append(tag)
    special = {}
    for m in re.finditer(r'menuName\.Equals\("(\w+)"\)\s*\)\s*\{(.*?)\}', src, flags=re.S):
        new = re.search(r"new\s+([\w.]+)\s*\(", m.group(2))
        if new:
            special[m.group(1).lower()] = new.group(1)
    # explicit fastreport handling
    tag_to_module.setdefault("fastreport", "SMLFastReport._designer._load(menuName)")
    tag_to_module.setdefault("fastreportother", "SMLFastReport")
    return tag_to_module, tag_order, special


# --- per-module switch ------------------------------------------------------
def module_cases(module):
    folder = module.split(".")[0]
    if folder == "flow":
        f = ERP / "SMLERPControl/_flow/_selectMenu.cs"
    elif folder == "_g":
        f = ERP / "SMLERPGlobal/_selectMenu.cs"
    else:
        f = ERP / folder / "_selectMenu.cs"
    if not f.exists():
        return {}, None
    src = strip_comments(read(f))
    cases, pending = {}, []
    parts = re.split(r'case\s+"([^"]+)"\s*:', src)
    # parts = [prefix, label1, seg1, label2, seg2, ...]
    for i in range(1, len(parts), 2):
        label, seg = parts[i].lower(), parts[i + 1]
        pending.append(label)
        seg_core = re.split(r"\bdefault\s*:", seg)[0]
        new = re.search(r"new\s+([\w.]+)\s*\(([^;]*)", seg_core)
        if new or re.search(r"\b(return|break)\b", seg_core):
            args = new.group(2) if new else ""
            row = {
                "class": new.group(1) if new else "",
                "trans_enum": re.findall(r"_transControlTypeEnum\.([^\s;,)]+)", seg_core),
                "report_enum": re.findall(r"_reportEnum\.([^\s;,)]+)", seg_core),
                "args": re.sub(r"\s+", " ", args)[:160],
                "tables": sorted(set(re.findall(r"_g\.d\.(\w+)\._table", seg_core))),
            }
            for lbl in pending:
                cases[lbl] = row
            pending = []
    return cases, f.relative_to(ERP).as_posix()


# --- menu tree --------------------------------------------------------------
def walk(nodes, path, out):
    for n in nodes:
        kids = n.get("Children") or []
        tags = re.findall(r"&([^&]+)&", n.get("Tag") or "")
        words = [t for t in tags if not t.isdigit() and t not in ("line", "hide")]
        row = {"name": n.get("Name", ""), "text": (n.get("Text") or "").strip(), "path": path,
               "tags": words, "editions": [t for t in tags if t.isdigit()], "leaf": not kids}
        out.append(row)
        walk(kids, path + [row["text"]], out)


def main():
    menus = []
    walk(json.loads(read(ERP / "SMLAccount/menu.json")), [], menus)
    tag_to_module, tag_order, special = dispatcher()
    flags = trans_flag_map()
    idx = class_index()
    cache = {}
    rows = []
    for m in menus:
        if not m["leaf"]:
            continue
        name = m["name"].lower()
        r = dict(m, **{"module": "", "selector_file": "", "class": "", "file": "", "base": "", "args": "",
                       "trans_enum": [], "trans_flag": [], "report_enum": [], "route": ""})
        if name in special:
            r["route"] = "special(_mainForm)"
            r["class"] = special[name]
        else:
            tag = next((t for t in tag_order if t in m["tags"]), next((t for t in m["tags"] if t in tag_to_module), ""))
            module = tag_to_module.get(tag, "")
            if not module:
                module = "_g"  # fallback: (new _g._selectMenu())._getObject(menuName, screenName, programName)
            r["route"] = f"tag:{tag}" if tag else "fallback:_g._selectMenu"
            r["module"] = module
            if tag == "fastreport":
                r["class"] = "SMLFastReport._designer"
                r["route"] = "fastreport(load by menu name)"
            elif module:
                if module not in cache:
                    cache[module] = module_cases(module)
                cases, sel_file = cache[module]
                r["selector_file"] = sel_file or ""
                c = cases.get(name)
                if c:
                    r["class"], r["trans_enum"], r["report_enum"], r["args"] = c["class"], c["trans_enum"], c["report_enum"], c["args"]
                    r["selector_tables"] = c["tables"]
                else:
                    r["route"] += " (no case found)"
        if r["class"]:
            q, f, base = resolve(r["class"], (r["module"] or "").split(".")[0], idx)
            r["class"], r["file"], r["base"] = q, f, base
            chain, cur = [], base
            while cur and cur.split(".")[-1] not in ("UserControl", "Form", "Control") and len(chain) < 6:
                chain.append(cur)
                _, _, cur = resolve(cur, q.split(".")[0], idx)
            r["base_chain"] = chain + ([cur] if cur else [])
        if r["file"]:
            emb, enums = embedded(r["file"])
            r["embedded"] = emb
            core = any(e.endswith("_icTransControl") for e in emb) or r["class"].endswith("_clone_icTrans")
            r["tables"] = r.get("selector_tables") or ([] if core else _tbl_cache.get(r["file"], []))
            if not r["trans_enum"]:
                r["trans_enum"] = enums
        r["trans_flag"] = [flags[e] for e in r["trans_enum"] if e in flags]
        rows.append(r)

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "menu-map.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

    mapped = sum(1 for r in rows if r["class"])
    lines = ["---", "tags: [sml, menu, generated]", "---", "# แผนที่เมนู → หน้าจอ (SMLAccount)", "",
             "> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` (static analysis) — อย่าแก้ด้วยมือ ข้อมูลดิบสำหรับ agent อยู่ที่ `04-Menu/menu-map.json`", "",
             f"เมนูปลายทาง {len(rows)} รายการ จับคู่คลาสได้ {mapped} รายการ ({mapped * 100 // max(len(rows), 1)}%)", "",
             "การ route: `_mainForm._activeMenu` ตรวจสิทธิ์ → ดู tag ของเมนู → `_selectMenuXxx` → `<Module>._selectMenu._getObject(menuName)` (switch) → `new ScreenClass(...)` เปิดเป็นแท็บ ดู [[login-flow]] และ [[screen-classes]]",
             "", "คอลัมน์ trans_flag แปลงจาก `_transControlTypeEnum` ที่ส่งเข้า constructor (ถ้ามี) ดู [[trans_flag]]", ""]
    by_top = collections.defaultdict(list)
    for r in rows:
        by_top[r["path"][0] if r["path"] else "(root)"].append(r)
    for top, items in by_top.items():
        lines += [f"## {top} ({len(items)})", "", "| เมนู | menu name | คลาส | ใช้ control | trans_flag |", "|---|---|---|---|---|"]
        for r in items:
            sub = " › ".join(r["path"][1:] + [r["text"]])
            cls = f"`{r['class']}`" if r["class"] else ""
            flag = ", ".join(str(x) for x in r["trans_flag"]) or ", ".join(r["report_enum"][:1])
            emb = ", ".join(e.split(".")[-1] for e in r.get("embedded", [])[:3])
            lines.append(f"| {sub} | `{r['name']}` | {cls} | {emb} | {flag} |")
        lines.append("")
    (OUT_DIR / "menu-map.md").write_text("\n".join(lines), encoding="utf-8")

    # screen templates
    by_base = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        if r["class"]:
            by_base[r["base"] or "(ไม่พบ base)"][r["class"]].append(r)
    tl = ["---", "tags: [sml, screen, generated]", "---", "# คลาสหน้าจอ จัดกลุ่มตาม base class (หน้าจอต้นแบบ)", "",
          "> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` — base class บอกว่าหน้าจอใช้ต้นแบบอะไร (เช่นหน้าจอเอกสาร, รายงาน, master data) กลับไป [[menu-map]]", "",
          "| base class | จำนวนคลาส | จำนวนเมนู |", "|---|---|---|"]
    order = sorted(by_base, key=lambda b: -sum(len(v) for v in by_base[b].values()))
    for b in order:
        tl.append(f"| `{b}` | {len(by_base[b])} | {sum(len(v) for v in by_base[b].values())} |")
    tl.append("")
    for b in order:
        tl += [f"## {b}", "", "| คลาส | ไฟล์ | เมนู |", "|---|---|---|"]
        for cls, rs in sorted(by_base[b].items(), key=lambda kv: -len(kv[1])):
            f = rs[0]["file"]
            names = ", ".join(f"{x['text']} (`{x['name']}`)" for x in rs[:6]) + (f" … +{len(rs) - 6}" if len(rs) > 6 else "")
            tl.append(f"| `{cls}` | `{f}` | {names} |")
        tl.append("")
    (OUT_DIR / "screen-classes.md").write_text("\n".join(tl), encoding="utf-8")
    unrouted = collections.Counter(r["route"] for r in rows if not r["class"])
    print(f"leaf menus={len(rows)} mapped={mapped} base-groups={len(by_base)}")
    print("unmapped by route:", unrouted.most_common(12))


if __name__ == "__main__":
    main()
