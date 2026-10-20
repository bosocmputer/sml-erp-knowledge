# sml_mcp_ai (`~/dev/smlmcpconnect`)

- Remote เดียว: `https://github.com/bosocmputer/sml_mcp_ai.git` (ตรวจ `git remote -v` ก่อน pull/push)
- TypeScript strict, Node 20, `@modelcontextprotocol/sdk`, `pg`, `zod`, `wordcut` (ตัดคำไทย), Docker
- Transport: stdio / sse / streamable-http; HTTP: `/health`, `/tools`, `/call`, `/reload`, `/mcp`, `/sse`, `/api/sale_reserve` (เขียน), `/media/products/:guid`
- ทุก query เป็น READ ONLY transaction, จำกัด 500 แถว; รูปสินค้าจาก `<db>_images` (ปิดเป็นค่าเริ่มต้น)
- RBAC 5 role: admin, sales, purchase, stock, general (`src/utils/permissions.ts`); sales/crm/ar tools = admin เท่านั้น
- Tool (~35): search (product, customer, supplier, smart), inventory (stock balance, price, incoming, outstanding, bookout), sales (summary, by customer/item/salesman/branch/dimension, top items/buyers, document summary, item detail), crm (RFM, activity, profitability, credit status, DSO, purchase frequency, conversion rate, segment, new customer trend, salesman KPI, by area), ar (outstanding, overdue, document detail), write (`create_sale_reserve` ผ่าน SML API)
- trans_flag ที่ใช้: 44 (ขาย), 46 (เพิ่มหนี้), 48 (ลดหนี้), 66, 93/95/97/99/101/103 (ลูกหนี้), 239 (รับชำระ)
- ใช้จริงกับ OpenClaw Gateway (LINE/Telegram, ผ่าน OpenRouter) เป็นบอท "น้องขาย" (`prompts/sales-agent-system-prompt.md`), MCP bind host-only `127.0.0.1:3515` บนเครื่อง production ตาม `CLAUDE_HANDOFF_2026-10-07.md`

## ช่องว่างความครอบคลุม (เทียบกับโมดูล SML)
ยังไม่มี: ซื้อ/เจ้าหนี้, เงินสด-ธนาคาร-เช็ค, GL/VAT, POS กะ/บิลยกเลิก, ล็อต/วันหมดอายุ, การเคลื่อนไหวสต็อก (โอน/ตรวจนับ), ติดตามสายเอกสาร (doc_ref), audit log ฝั่ง AI

## ความเสี่ยงที่พบ (2026-10-20, ยังไม่แก้)
- role มาจาก header `mcp-access-mode` ที่ผู้เรียกส่งเอง ไม่มี authentication → ขอ admin เองได้ (`src/index.ts` `resolveRole`), env ไม่ใช่เพดาน
- `/reload` ไม่ตรวจสิทธิ์, CORS `*`
- `docker-compose.yml` เปิดพอร์ตทุก interface และ default `MCP_ACCESS_MODE=admin`
- 1 instance = 1 DB (ยังไม่รองรับหลายร้าน), ข้อมูลลูกค้าส่งออกไป OpenRouter (PDPA)
