#!/usr/bin/env python3
"""Generate 05-Modules/modules.md: project references of SMLAccount and per-project file counts.

Usage: python3 scripts/gen_modules.py [path/to/smlerp]
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
OUT = VAULT / "05-Modules/modules.md"
REF = re.compile(r'<ProjectReference Include="([^"]+)"')


def refs(csproj):
    text = csproj.read_text(encoding="utf-8-sig", errors="ignore")
    return [pathlib.PureWindowsPath(r).stem for r in REF.findall(text)]


CSPROJ = {p.stem: p for p in ERP.glob("*/*.csproj")}  # project name may differ from its folder


def info(name):
    d = CSPROJ[name].parent if name in CSPROJ else ERP / name
    cs = list(d.rglob("*.cs")) if d.is_dir() else []
    forms = [p for p in cs if p.name.endswith(".Designer.cs") or p.name.endswith(".designer.cs")]
    return len(cs), len(forms)


def main():
    root = ERP / "SMLAccount/SMLAccount.csproj"
    direct = refs(root)
    lines = [
        "---",
        "tags: [sml, modules, generated]",
        "---",
        "# โมดูลของ SMLAccount / SMLAccountPOSProfessional",
        "",
        "> สร้างอัตโนมัติด้วย `scripts/gen_modules.py` — อย่าแก้ไฟล์นี้ด้วยมือ",
        "",
        "`SMLAccountPOSProfessional` → อ้างอิง `MyLib`, `SMLAccount` แล้วเรียก `SMLAccount.Program.Main()` ดู [[architecture]]",
        "",
        f"`SMLAccount` อ้างอิงโดยตรง {len(direct)} โปรเจกต์ (จำนวนหน้าจอ = ไฟล์ *.Designer.cs โดยประมาณ)",
        "",
        "| โปรเจกต์ | ไฟล์ .cs | หน้าจอ/ฟอร์ม | อ้างอิงต่อ |",
        "|---|---|---|---|",
    ]
    for name in sorted(direct):
        n_cs, n_forms = info(name)
        sub = CSPROJ.get(name)
        deps = ", ".join(sorted(set(refs(sub)))) if sub else "(ไม่พบ csproj)"
        lines.append(f"| {name} | {n_cs} | {n_forms} | {deps} |")
    all_proj = sorted(p.parent.name for p in ERP.glob("*/*.csproj"))
    lines += ["", f"## โปรเจกต์ทั้งหมดใน repo ({len(all_proj)})", "", ", ".join(all_proj), ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(direct)} direct refs, {len(all_proj)} projects)")


if __name__ == "__main__":
    main()
