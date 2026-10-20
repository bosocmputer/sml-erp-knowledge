#!/usr/bin/env python3
"""Generate 01-Architecture/webservice-api.md: SOAP web methods and REST endpoints of SMLJavaWebService.

Static scan of smljavaws2: @WebMethod in SOAP classes, @Path/@GET/@POST in JAX-RS classes, and whether each
REST handler body contains a session/GUID check (heuristic).

Usage: python3 scripts/gen_webservice_api.py [path/to/smljavaws2]
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
WS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smljavaws2"
JAVA = WS / "src/main/java"


def main():
    soap, rest = [], []
    app_paths = {}
    for p in JAVA.rglob("*.java"):
        src = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'@javax\.ws\.rs\.ApplicationPath\("([^"]+)"\)|@ApplicationPath\("([^"]+)"\)', src)
        if m:
            app_paths[p.parent.name] = m.group(1) or m.group(2)
    for p in sorted(JAVA.rglob("*.java")):
        src = p.read_text(encoding="utf-8", errors="ignore")
        rel = p.relative_to(JAVA).as_posix()
        for m in re.finditer(r"@WebMethod[^\n]*\n\s*public\s+[\w<>\[\]]+\s+(\w+)\s*\(([^)]*)\)", src):
            params = ", ".join(x.strip().split()[-1] for x in m.group(2).split(",") if x.strip())
            soap.append((p.stem, m.group(1), params))
        cls = re.search(r'^@Path\("([^"]*)"\)', src, re.M)
        base = cls.group(1) if cls else ""
        for m in re.finditer(r'((?:@\w+(?:\([^)]*\))?\s*)+)public\s+[\w<>\[\]]+\s+(\w+)\s*\(([^)]*)\)\s*(?:throws[^{]*)?\{', src):
            ann = m.group(1)
            if "@Path" not in ann and not re.search(r"@(GET|POST|PUT|DELETE)\b", ann):
                continue
            verb = ",".join(re.findall(r"@(GET|POST|PUT|DELETE)\b", ann)) or "-"
            sub = re.search(r'@Path\("([^"]*)"\)', ann)
            body_start = m.end()
            depth, i = 1, body_start
            while i < len(src) and depth:
                depth += {"{": 1, "}": -1}.get(src[i], 0)
                i += 1
            body = src[body_start:i]
            auth = "มี" if re.search(r"_guidReady|GUID|guid|token|Authorization|login", body) else "ไม่พบ"
            sql = "รัน SQL จาก request" if re.search(r'getString\("query"\)|getString\("sql"\)', body) else ""
            root = app_paths.get(p.parent.name) or app_paths.get(p.parent.parent.name, "?")
            rest.append((f"/{root}/{base}/{sub.group(1) if sub else ''}".replace("//", "/").rstrip("/"), verb, m.group(2), rel, auth, sql))
    L = ["---", "tags: [sml, webservice, api, generated]", "status: from-code", "---", "# SMLJavaWebService — รายการ API", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_webservice_api.py` จาก `~/dev/smljavaws2` (v3.9.14 ในเครื่อง; server จริงรัน 3.9.7 อาจต่างกัน) — กลับไป [[architecture]] · [[00-Index]]", "",
         "คอลัมน์ \"ตรวจ session\" เป็นการเดาจากโค้ด (หาคำว่า guid/token/login ใน handler) — ต้องอ่านโค้ดยืนยันก่อนสรุปเรื่องความปลอดภัย", "",
         f"## REST ({len(rest)} endpoint)", "", "| path | method | handler | ไฟล์ | ตรวจ session | หมายเหตุ |", "|---|---|---|---|---|---|"]
    L += [f"| `{a}` | {b} | `{c}` | `{d}` | {e} | {f} |" for a, b, c, d, e, f in sorted(rest)]
    L += ["", f"## SOAP ({len(soap)} web method)", "", "endpoint `/DotNetFrameWork`, `/SMLFrameWork` (WSServlet) — โปรแกรม Windows เรียกผ่าน proxy `MyLib/Web References/SMLJAVAWS`", "",
          "| คลาส | method | พารามิเตอร์ |", "|---|---|---|"]
    L += [f"| {c} | `{m}` | {p} |" for c, m, p in soap]
    (VAULT / "01-Architecture/webservice-api.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"rest={len(rest)} soap={len(soap)}")


if __name__ == "__main__":
    main()
