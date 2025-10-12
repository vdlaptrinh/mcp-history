# 🕰️ MCP-History for XiaoZhi AI

**MCP-History** là một **Model Context Protocol (MCP) skill** giúp XiaoZhi AI (hoặc ChatGPT có hỗ trợ MCP) tra cứu sự kiện lịch sử **“Ngày này năm xưa”**.  
Dự án được viết bằng **Python 3**, có thể chạy độc lập hoặc kết nối với **MCP endpoint** như `wss://api.xiaozhi.me/mcp...`.

---

## ⚡ Quick Start

Chạy 3 lệnh sau để bắt đầu ngay (Linux / Raspberry Pi):

```bash
git clone https://github.com/vdlaptrinh/mcp-history.git
cd mcp-history
bash quickstart.sh
💡 Nếu không có file quickstart.sh, bạn có thể làm thủ công theo hướng dẫn bên dưới.

✨ Tính năng
📅 Lấy sự kiện lịch sử nổi bật trong ngày (theo ngày & tháng hiện tại).

🌐 Kết nối tới máy chủ MCP qua WebSocket (MCP_ENDPOINT).

🤖 Tích hợp dễ dàng với XiaoZhi AI hoặc ChatGPT MCP Developer Mode.

🧩 Viết gọn gàng bằng Python, dễ mở rộng và tùy chỉnh.

💻 Hỗ trợ Linux, macOS, Windows và Raspberry Pi.

🧩 Cài đặt từng bước
1️⃣ Clone dự án
bash
Sao chép mã
git clone https://github.com/vdlaptrinh/mcp-history.git
cd mcp-history/
2️⃣ Tạo môi trường ảo Python
bash
Sao chép mã
python3 -m venv mcp_history_env
source mcp_history_env/bin/activate
💡 Trên Windows:

bash
Sao chép mã
mcp_history_env\Scripts\activate
3️⃣ Cài thư viện phụ thuộc
bash
Sao chép mã
pip install -r requirements.txt
4️⃣ Cấu hình endpoint MCP
Thiết lập URL endpoint để kết nối tới máy chủ MCP:

bash
Sao chép mã
export MCP_ENDPOINT=wss://api.xiaozhi.me/mcp...
⚠️ Nếu dùng Windows PowerShell:

powershell
Sao chép mã
setx MCP_ENDPOINT "wss://api.xiaozhi.me/mcp..."
🚀 Chạy MCP Skill
bash
Sao chép mã
python mcp_pipe.py /home/pi/mcp-history/server.py
✅ Thay /home/pi/mcp-history/server.py bằng đường dẫn thực tế trên máy bạn.

🧠 Ví dụ kết quả
Khi khởi chạy thành công, log sẽ hiện như sau:

csharp
Sao chép mã
[MCP] Connected to wss://api.xiaozhi.me/mcp...
[MCP] Registered skill: NgayNayNamXua
Khi được gọi qua XiaoZhi AI hoặc ChatGPT, tool history_today sẽ trả về:

diff
Sao chép mã
📜 Ngày này năm xưa:
- 1492: Christopher Columbus khám phá châu Mỹ
- 1968: NASA phóng Apollo 7
- 2006: Google mua lại YouTube
📂 Cấu trúc thư mục
css
Sao chép mã
mcp-history/
│
├── server.py           # MCP skill chính (Ngày này năm xưa)
├── mcp_pipe.py         # Trình kết nối tới MCP endpoint
├── requirements.txt    # Danh sách thư viện cần thiết
├── README.md           # Tài liệu hướng dẫn
└── index.json          # Metadata mô tả skill (tùy chọn)
🔁 Tự động khởi động trên Raspberry Pi
Nếu muốn MCP-History chạy tự động khi bật nguồn, tạo service như sau:

bash
Sao chép mã
sudo nano /etc/systemd/system/mcp-history.service
Thêm nội dung:

ini
Sao chép mã
[Unit]
Description=MCP-History Skill
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/mcp-history
ExecStart=/home/pi/mcp_history_env/bin/python3 /home/pi/mcp-history/mcp_pipe.py /home/pi/mcp-history/server.py
Restart=always

[Install]
WantedBy=multi-user.target
Lưu lại và kích hoạt:

bash
Sao chép mã
sudo systemctl daemon-reload
sudo systemctl enable mcp-history
sudo systemctl start mcp-history
Xem log hoạt động:

bash
Sao chép mã
journalctl -u mcp-history -f
🧾 index.json (tùy chọn)
File này giúp mô tả skill cho MCP client (như ChatGPT hoặc XiaoZhi):

json
Sao chép mã
{
  "name": "NgayNayNamXua",
  "description": "Trả về các sự kiện lịch sử nổi bật trong ngày hôm nay.",
  "tools": [
    {
      "name": "history_today",
      "description": "Lấy danh sách các sự kiện 'ngày này năm xưa'.",
      "input_schema": { "type": "object", "properties": {} }
    }
  ]
}
💡 Gợi ý mở rộng
Bạn có thể:

🔌 Thêm công cụ khác (VD: “Tin tức hôm nay”, “Thời tiết hiện tại”).

🧠 Kết hợp nhiều MCP skill thành cụm tiện ích thông minh.

🕹️ Tạo UI hiển thị sự kiện hoặc gửi qua Telegram / Discord.

📦 Đóng gói thành Docker container để chạy trên cloud.

🧑‍💻 Tác giả
VD Lập Trình
📘 GitHub: @vdlaptrinh
🌐 Website: https://vdlaptrinh.github.io
💬 Email: contact@vdlaptrinh.dev

🪪 Giấy phép
Phát hành theo MIT License.
Bạn được phép sử dụng, chỉnh sửa, phân phối tự do với điều kiện ghi rõ nguồn gốc.

🧩 MCP-History – Một phần mở rộng nhỏ nhưng mạnh mẽ cho hệ sinh thái XiaoZhi AI.