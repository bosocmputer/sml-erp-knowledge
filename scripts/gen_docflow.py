#!/usr/bin/env python3
"""Generate 03-Reference/doc-flow-rules.md from SMLProcess/_docFlowThread.cs `_docFlowProcess()`.

For each source document type the code defines SQL fragments that decide its status:
  cancel     : which trans_flag cancels it (queryGetDocCancel(src, cancel) or literal SQL)
  consumed by: which downstream trans_flags reference it through ic_trans_detail.ref_doc_no (reduce qty / ref count)
These drive ic_trans.used_status (มีการอ้างอิงแล้ว), doc_success (สิ้นสุด), last_status (ยกเลิก).

Usage: python3 scripts/gen_docflow.py [path/to/smlerp]
"""
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
ERP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "dev/smlerp"
FLAGS = dict(re.findall(r"^\| (\d+) \| (.+?) \|$", (VAULT / "03-Reference/trans_flag.md").read_text(encoding="utf-8"), flags=re.M))
NAME_TO_FLAG = {v: k for k, v in FLAGS.items()}


def strip(src):
    return re.sub(r"(?m)^\s*//.*$", "", src)


def flags_in(expr):
    out = []
    for m in re.finditer(r"trans_flag\s*(?:=|in)\s*\(?\s*([\d,\s]+)\)?", expr):
        out += [x.strip() for x in m.group(1).split(",") if x.strip()]
    return out


def main():
    src = (ERP / "SMLProcess/_docFlowThread.cs").read_text(encoding="utf-8-sig", errors="ignore")
    start = src.find("public void _docFlowProcess()")
    end = src.find("\n        public ", start + 10)
    body = strip(src[start:end])
    # split switch into case groups: labels followed by statements until 'break;'
    rules = []
    for block in re.split(r"\bbreak;", body):
        labels = re.findall(r"case _g\.g\._transControlTypeEnum\.([^\s:]+)\s*:", block)
        if not labels:
            continue
        stmts = block[block.rfind(":") + 1:] if False else block
        cancel = re.findall(r"queryGetDocCancel\((\d+),\s*(\d+)\)", stmts)
        cancel_flags = sorted({c[1] for c in cancel})
        if not cancel_flags:
            m = re.search(r"__queryDocCancelCount\s*=\s*\"(.*?)\";", stmts, re.S)
            if m:
                cancel_flags = sorted(set(flags_in(m.group(1))) - {NAME_TO_FLAG.get(labels[-1], "")})
        reduce = []
        for var in ("__queryReduceItemQty", "__queryDocRefCount", "__queryDocRefCount2", "__queryUseAmount"):
            for m in re.finditer(var + r"\s*=\s*\"(.*?)\";", stmts, re.S):
                reduce += flags_in(m.group(1))
        src_flag = NAME_TO_FLAG.get(labels[-1], "")
        consumed = sorted(set(reduce) - {src_flag} - set(cancel_flags), key=lambda x: int(x))
        moved = [x for x in consumed if FLAGS.get(x, "").endswith("_ยกเลิก")]
        cancel_flags = sorted(set(cancel_flags) | set(moved), key=lambda x: int(x))
        consumed = [x for x in consumed if x not in moved]
        if not (cancel_flags or consumed):
            continue
        rules.append((labels, src_flag, cancel_flags, consumed))

    L = ["---", "tags: [sml, reference, doc-flow, generated]", "status: from-code", "---",
         "# กฎสายเอกสาร (Document Flow) — สถานะ อ้างอิง ยกเลิก", "",
         "> สร้างอัตโนมัติด้วย `scripts/gen_docflow.py` จาก `SMLProcess/_docFlowThread.cs` `_docFlowProcess()` — รันหลังบันทึกทุกเอกสาร ดู [[document-engine]] · กลับไป [[00-Index]]", "",
         "## หลักการ", "",
         "- **ยกเลิก** = มีเอกสารประเภทยกเลิก (ส่วนใหญ่ trans_flag ถัดไป +1) ที่ `doc_ref = doc_no` ของต้นทาง **หรือ** ต้นทางเองมี `is_cancel = 1` → ตั้ง `ic_trans.last_status`",
         "- **ถูกอ้างอิง** = มีรายการ `ic_trans_detail.ref_doc_no = doc_no` ต้นทาง ในเอกสารปลายทางที่กำหนด → `used_status = 1` (มีการอ้างอิงแล้ว)",
         "- **สิ้นสุด** = จำนวนที่ถูกใช้ (`sum(qty * stand_value/divide_value)` ของปลายทาง) ≥ จำนวนต้นทาง → `doc_success = 1` (สิ้นสุด)",
         "- ฟิลด์ที่ถูกอัปเดต: `ic_trans.used_status`, `used_status_2`, `doc_success`, `last_status`, `approve_status`, `expire_status`, `on_hold`; `ic_trans_detail.last_status`; `ap_ar_trans_detail.last_status`; `cb_chq_list.status`",
         "- เอกสารที่ค้นได้: `ic_trans`, `ap_ar_trans`, `ic_wms_trans`, `pp_shipment`", "",
         "**ใช้ทำ product \"ตามงานค้าง\":** เอกสารที่ `used_status = 0` และไม่ได้ยกเลิก = ยังไม่มีใครนำไปใช้ต่อ; `used_status = 1` แต่ `doc_success = 0` = ใช้ไปบางส่วน", "",
         "## กฎรายประเภท", "", "| ต้นทาง | trans_flag | ยกเลิกด้วย | ถูกใช้ต่อโดย (ref_doc_no) |", "|---|---|---|---|"]
    for labels, src_flag, cancel_flags, consumed in rules:
        name = " / ".join(labels)
        fmt = lambda xs: ", ".join(f"{x} {FLAGS.get(x, '')}" for x in xs)
        L.append(f"| {name} | {src_flag} | {fmt(cancel_flags)} | {fmt(consumed)} |")
    out = VAULT / "03-Reference/doc-flow-rules.md"
    if out.exists():  # keep manually verified section between "## ยืนยันกับ AOY" and "## กฎรายประเภท"
        old = out.read_text(encoding="utf-8")
        a, b = old.find("## ยืนยันกับ AOY"), old.find("## กฎรายประเภท")
        if a != -1 and b > a:
            i = L.index("## กฎรายประเภท")
            L[i:i] = old[a:b].rstrip("\n").split("\n") + [""]
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"rules={len(rules)}")


if __name__ == "__main__":
    main()
