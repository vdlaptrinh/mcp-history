# 🕰️ MCP-History for XiaoZhi AI

**MCP-History** là một **Model Context Protocol (MCP) skill** giúp **XiaoZhi AI** (hoặc **ChatGPT có hỗ trợ MCP**) tra cứu sự kiện lịch sử **“Ngày này năm xưa”**.  
Dự án được viết bằng **Python 3**, có thể chạy độc lập hoặc kết nối với **MCP endpoint** như `wss://api.xiaozhi.me/mcp...`.

---

## ⚡ Quick Start

Chạy 3 lệnh sau để bắt đầu ngay (Linux / Raspberry Pi):

```bash
git clone https://github.com/vdlaptrinh/mcp-history.git
cd mcp-history
./quickstart.sh
```bash
💡 Nếu không có file quickstart.sh, bạn có thể làm thủ công theo hướng dẫn bên dưới.

✨ Tính năng

📅 Lấy sự kiện lịch sử nổi bật trong ngày (theo ngày & tháng hiện tại).

🌐 Kết nối tới máy chủ MCP qua WebSocket (MCP_ENDPOINT).

🤖 Tích hợp dễ dàng với XiaoZhi AI hoặc ChatGPT MCP Developer Mode.

🧩 Viết gọn gàng bằng Python, dễ mở rộng và tùy chỉnh.

💻 Hỗ trợ Linux, macOS, Windows và Raspberry Pi.

🧩 Cài đặt từng bước
1️⃣ Clone dự án
git clone https://github.com/vdlaptrinh/mcp-history.git
cd mcp-history/