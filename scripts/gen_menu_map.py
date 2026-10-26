#!/usr/bin/env python3
"""Generate the menu -> screen map for SMLAccount and SMLPOS.

Reads (per product, SMLAccount and SMLPOS):
  smlerp/<product>/menu.json             menu tree (name, text, tag)
  smlerp/<product>/_mainForm.cs          dispatcher: tag -> _selectMenuXxx -> <Module>._selectMenu
  smlerp/*/_selectMenu.cs                per-module switch: menu name -> new ScreenClass(args)
  smlerp/**/*.cs                         class index: class -> file, base class
  smlerp/SMLERPGlobal/_global.cs         _transFlag() enum -> trans_flag number

Writes:
  04-Menu/menu-map.md / .json          SMLAccount (editions Acc, Pro, AccPOS, AccPOSPro)
  04-Menu/menu-map-pos.md / .json      SMLPOS family (POS, Lite, TYG, TYGPro, Coffee)
  04-Menu/screen-classes.md            SMLAccount screen classes grouped by base class (screen templates)

Menu numbers (X.Y.Z) follow the program: SMLERPTemplate/_templateMainForm.cs _menuRemoveByVersion drops nodes whose
tag is not empty, lacks &<edition>&, and is not exactly &hide&; then mainMenuChangeResource numbers the remaining
siblings (hidden nodes keep their position); _createMenuBar skips children whose tag contains &hide&.
Not modelled: OEM tags (&imex&/&singha&), menu features enabled from the web service, per-user permission hiding.

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
def dispatcher(main_rel):
    src = strip_comments(read(ERP / main_rel))
    fn_to_module = {}
    for m in re.finditer(r"void\s+(_selectMenu\w+)\s*\([^)]*\)\s*\{(.*?)\n        \}", src, flags=re.S):
        mod = re.search(r"([\w.]+)\._selectMenu\._getObject", m.group(2))
        if mod:
            fn_to_module[m.group(1)] = mod.group(1)
    start = re.search(r"void\s+_activeMenu\s*\(", src)
    start = start.start() if start else 0
    # position of each check inside _activeMenu = check order (the first check that matches wins)
    tag_to_module, tag_pos = {}, {}
    for m in re.finditer(r'tag\.IndexOf\("&(\w+)&"\)\s*!=\s*-1', src[start:]):
        tag = m.group(1)
        if tag in tag_pos:
            continue
        tag_pos[tag] = m.start()
        body = src[start + m.end():start + m.end() + 600]
        call = re.match(r"\s*\)\s*\{\s*(\w+)\(", body)
        if call:
            tag_to_module[tag] = fn_to_module.get(call.group(1), call.group(1))
    special, special_pos = {}, {}
    for m in re.finditer(r'menuName\.Equals\("(\w+)"\)\s*\)\s*\{(.*?)\}', src, flags=re.S):
        new = re.search(r"new\s+([\w.]+)\s*\(", m.group(2))
        if new and m.group(1).lower() not in special:
            special[m.group(1).lower()] = new.group(1)
            special_pos[m.group(1).lower()] = m.start() - start
    # explicit fastreport handling
    tag_to_module.setdefault("fastreport", "SMLFastReport._designer._load(menuName)")
    tag_to_module.setdefault("fastreportother", "SMLFastReport")
    return tag_to_module, tag_pos, special, special_pos


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
PRODUCTS = [
    {"product": "SMLAccount", "menu": "SMLAccount/menu.json", "main": "SMLAccount/_mainForm.cs", "out": "menu-map",
     "editions": [("Acc", "2"), ("Pro", "3"), ("AccPOS", "12"), ("AccPOSPro", "13")]},
    {"product": "SMLPOS", "menu": "SMLPOS/menu.json", "main": "SMLPOS/_mainForm.cs", "out": "menu-map-pos",
     "editions": [("POS", "6"), ("Lite", "7"), ("TYG", "8"), ("TYGPro", "11"), ("Coffee", "16")]},
]


def walk(nodes, path, out, editions, prefix, shown, top=True):
    """prefix[label] = number prefix of the parent ("" at top, None if removed for that edition)."""
    count = {lbl: 0 for lbl, _ in editions}
    for n in nodes:
        kids = n.get("Children") or []
        raw = n.get("Tag") or ""
        tags = re.findall(r"&([^&]+)&", raw)
        words = [t for t in tags if not t.isdigit() and t not in ("line", "hide")]
        num, vis = {}, {}
        for lbl, ed in editions:
            if prefix[lbl] is None or (raw and f"&{ed}&" not in raw and raw != "&hide&"):
                num[lbl] = None
                continue
            count[lbl] += 1
            num[lbl] = f"{prefix[lbl]}{count[lbl]}"
            vis[lbl] = shown[lbl] and (top or "&hide&" not in raw)
        row = {"name": n.get("Name", ""), "text": " ".join((n.get("Text") or "").split()), "path": path,
               "tags": words, "editions": [t for t in tags if t.isdigit()], "leaf": not kids,
               "numbers": {lbl: num[lbl] for lbl, _ in editions if num[lbl] and vis[lbl]},
               "numbers_hidden": {lbl: num[lbl] for lbl, _ in editions if num[lbl] and not vis[lbl]}}
        out.append(row)
        walk(kids, path + [row["text"]], out, editions,
             {lbl: (num[lbl] + ".") if num[lbl] else None for lbl, _ in editions},
             {lbl: vis.get(lbl, False) for lbl, _ in editions}, top=False)


def fmt_numbers(numbers, editions):
    """'4.1.2' when every edition that shows it agrees, else '4.1.2 Acc/Pro · 5.1.2 AccPOS/AccPOSPro'."""
    groups = collections.OrderedDict()
    for lbl, _ in editions:
        if lbl in numbers:
            groups.setdefault(numbers[lbl], []).append(lbl)
    if len(groups) == 1 and len(next(iter(groups.values()))) == len(editions):
        return next(iter(groups))
    return " · ".join(f"{k} {'/'.join(v)}" for k, v in groups.items())


def build_rows(prod, flags, idx):
    eds = prod["editions"]
    menus = []
    walk(json.loads(read(ERP / prod["menu"])), [], menus, eds, {l: "" for l, _ in eds}, {l: True for l, _ in eds})
    tag_to_module, tag_pos, special, special_pos = dispatcher(prod["main"])
    cache = {}
    rows = []
    for m in menus:
        if not m["leaf"]:
            continue
        name = m["name"].lower()
        r = dict(m, **{"product": prod["product"], "module": "", "selector_file": "", "class": "", "file": "", "base": "",
                       "args": "", "trans_enum": [], "trans_flag": [], "report_enum": [], "route": ""})
        checks = sorted((tag_pos[t], t) for t in m["tags"] if t in tag_pos)
        tag = checks[0][1] if checks else next((t for t in m["tags"] if t in tag_to_module), "")
        if name in special and (not checks or special_pos[name] < checks[0][0]):
            r["route"] = "special(_mainForm)"
            r["class"] = special[name]
        else:
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
                    r["route"] += " (ไม่พบตัวจัดการ: เมนูค้าง/ไม่เปิดอะไร)"
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
        if prod["product"] == "SMLAccount":
            # SMLAccountPOSPro (the maintained launcher) sets _versionType.SMLAccountPOSProfessional -> tag &13&
            r["pos_pro"] = "AccPOSPro" in r["numbers"]
        rows.append(r)
    return rows


EDITION_NOTE = ("**เลข edition ใน tag ของเมนู** (`SMLERPTemplate/_templateMainForm.cs` `_menuRemoveByVersion`): 2 = SMLAccount, "
                "3 = SMLAccountProfessional, 6 = SMLPOS/IMSPOS, 7 = POSLite, 8 = TomYumGoong, 9 = POSMED, 10 = POSStarter, "
                "11 = TomYumGoongPro, 12 = SMLAccountPOS, **13 = SMLAccountPOSProfessional / SMLCM**, 15 = Merchant, 16 = POSCoffee · "
                "ตัวเปิดที่ยังพัฒนาอยู่ `SMLAccountPOSPro/Program.cs` ตั้ง `SMLAccountPOSProfessional` (13) — ✅ ยืนยันจากเครื่องร้าน AOY (แถบเมนูมี 11.คลังสินค้า 12.Data ซึ่งมีเฉพาะ edition 3/13) "
                "(โปรเจกต์เก่า `SMLAccountPOSProfessional/` แก้ล่าสุด 2015 ตั้ง `SMLAccountPOS` = 12) — "
                "เมนูแสดงเมื่อ tag ว่าง, มีเลขของ edition, หรือเป็น `&hide&` ตรงๆ (หรือ tag OEM `&imex&`/`&singha&`, หรือเปิดใน enableMenuFeatures) แล้วจึงกรองตามสิทธิ์ผู้ใช้")

NUMBER_NOTE = ("**เลขเมนู** = เลข X.Y.Z ที่โปรแกรมใส่หน้าชื่อเมนู (`mainMenuChangeResource`) หลังตัดเมนูตามรุ่น — นับรวมเมนูที่ซ่อน (`&hide&`) "
               "ด้วย จึงอาจมีเลขข้าม (✅ ยืนยันจากภาพหน้าจอ AOY 2026-10-26: เมนู ระบบขาย เริ่มที่ 1.3.2 เพราะ 1.3.1 ถูกซ่อน) · เลขที่ต่างกันตามรุ่นแสดงแยก เช่น `5.1 Acc/Pro · 6.1 AccPOS/AccPOSPro` · ไม่มีเลข = รุ่นเหล่านั้นไม่เห็นเมนูนี้ · "
               "ไม่รวมผลของสิทธิ์ผู้ใช้ (ตัวเลือก `show_menu_by_permission` ซ่อนเมนูแต่ไม่เปลี่ยนเลข), OEM และเมนูที่เปิดจาก service")


def write_md(prod, rows, title, links):
    eds = prod["editions"]
    mapped = sum(1 for r in rows if r["class"])
    per_ed = " · ".join(f"{lbl} (&{ed}&) {sum(1 for r in rows if lbl in r['numbers'])}" for lbl, ed in eds)
    lines = ["---", "tags: [sml, menu, generated]", "---", f"# {title}", "",
             f"> สร้างอัตโนมัติด้วย `scripts/gen_menu_map.py` (static analysis) — อย่าแก้ด้วยมือ ข้อมูลดิบสำหรับ agent อยู่ที่ `04-Menu/{prod['out']}.json`", "",
             f"เมนูปลายทาง {len(rows)} รายการ จับคู่คลาสได้ {mapped} รายการ ({mapped * 100 // max(len(rows), 1)}%) · เห็นตามรุ่น: {per_ed}", "",
             EDITION_NOTE, "", NUMBER_NOTE, "",
             f"การ route: `{prod['main']}` `_activeMenu` ตรวจสิทธิ์ → ดู tag ของเมนูตามลำดับการเช็คในโค้ด (ตัวแรกที่ตรงชนะ) → `_selectMenuXxx` → "
             "`<Module>._selectMenu._getObject(menuName)` (switch) → `new ScreenClass(...)` เปิดเป็นแท็บ " + links,
             "", "คอลัมน์ trans_flag แปลงจาก `_transControlTypeEnum` ที่ส่งเข้า constructor (ถ้ามี) ดู [[trans_flag]]", ""]
    by_top = collections.defaultdict(list)
    for r in rows:
        by_top[r["path"][0] if r["path"] else "(root)"].append(r)
    for top, items in by_top.items():
        lines += [f"## {top} ({len(items)})", "", "| เลขเมนู (ตามรุ่น) | เมนู | menu name | คลาส | ใช้ control | trans_flag |", "|---|---|---|---|---|---|"]
        for r in items:
            sub = " › ".join(r["path"][1:] + [r["text"]])
            cls = f"`{r['class']}`" if r["class"] else ""
            flag = ", ".join(str(x) for x in r["trans_flag"]) or ", ".join(r["report_enum"][:1])
            emb = ", ".join(e.split(".")[-1] for e in r.get("embedded", [])[:3])
            num = fmt_numbers(r["numbers"], eds) or ("ซ่อน" if r["numbers_hidden"] else "—")
            lines.append(f"| {num} | {sub} | `{r['name'].strip()}` | {cls or r['route']} | {emb} | {flag} |")
        lines.append("")
    (OUT_DIR / f"{prod['out']}.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    flags = trans_flag_map()
    idx = class_index()
    OUT_DIR.mkdir(exist_ok=True)
    all_rows = {}
    for prod in PRODUCTS:
        rows = build_rows(prod, flags, idx)
        all_rows[prod["product"]] = rows
        (OUT_DIR / f"{prod['out']}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    write_md(PRODUCTS[0], all_rows["SMLAccount"], "แผนที่เมนู → หน้าจอ (SMLAccount / Pro / AccountPOS / AccountPOSPro)",
             "ดู [[login-flow]], [[screen-classes]] · ตระกูล SMLPOS ดู [[menu-map-pos]]")
    write_md(PRODUCTS[1], all_rows["SMLPOS"], "แผนที่เมนู → หน้าจอ (SMLPOS / Lite / TomYumGoong / TomYumGoongPro / Coffee)",
             "· ลำดับการเช็ค tag ต่างจาก SMLAccount (เช่น `&pos&` ถูกเช็คหลัง `&so&`/`&ar&`/`&ic&`) · ตระกูล SMLAccount ดู [[menu-map]]")
    rows = all_rows["SMLAccount"]

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
    for prod in PRODUCTS:
        rs = all_rows[prod["product"]]
        unrouted = collections.Counter(r["route"] for r in rs if not r["class"])
        print(f"{prod['product']}: leaf menus={len(rs)} mapped={sum(1 for r in rs if r['class'])} "
              + " ".join(f"{l}={sum(1 for r in rs if l in r['numbers'])}" for l, _ in prod["editions"]))
        print("  unmapped by route:", unrouted.most_common(8))


if __name__ == "__main__":
    main()
