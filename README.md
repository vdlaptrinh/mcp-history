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
```
💡 Nếu không có file quickstart.sh, bạn có thể làm thủ công theo hướng dẫn bên dưới.

## ✨ Tính năng
📅 Lấy sự kiện lịch sử nổi bật trong ngày (theo ngày & tháng hiện tại).

🌐 Kết nối tới máy chủ MCP qua WebSocket (MCP_ENDPOINT).

🤖 Tích hợp dễ dàng với XiaoZhi AI hoặc ChatGPT MCP Developer Mode.

## 🧩 Viết gọn gàng bằng Python, dễ mở rộng và tùy chỉnh.

💻 Hỗ trợ Linux, macOS, Windows và Raspberry Pi.

## 🧩 Cài đặt từng bước
1️⃣ Clone dự án
```
git clone https://github.com/vdlaptrinh/mcp-history.git
cd mcp-history/
```
2️⃣ Tạo môi trường ảo Python
```
python3 -m venv mcp_history_env
source mcp_history_env/bin/activate
```
💡 Trên Windows:

```
mcp_history_env\Scripts\activate
```
3️⃣ Cài thư viện phụ thuộc
```
pip install -r requirements.txt
```
4️⃣ Cấu hình endpoint MCP
Thiết lập URL endpoint để kết nối tới máy chủ MCP:

```
export MCP_ENDPOINT=wss://api.xiaozhi.me/mcp...
```
⚠️ Nếu dùng Windows PowerShell:

powershell
```
setx MCP_ENDPOINT "wss://api.xiaozhi.me/mcp..."
```
🚀 Chạy MCP Skill
```
python mcp_pipe.py /home/pi/mcp-history/server.py
```
✅ Thay /home/pi/mcp-history/server.py bằng đường dẫn thực tế trên máy bạn.

## 🧠 Ví dụ kết quả
Khi khởi chạy thành công, log sẽ hiển thị:

```
[MCP] Connected to wss://api.xiaozhi.me/mcp...
[MCP] Registered skill: NgayNayNamXua
```
Khi được gọi qua XiaoZhi AI hoặc ChatGPT, tool history_today sẽ trả về:

📜 Ngày này năm xưa:
- 1492: Christopher Columbus khám phá châu Mỹ
- 1968: NASA phóng Apollo 7
- 2006: Google mua lại YouTube
## 📂 Cấu trúc thư mục
```
mcp-history/
│
├── server.py           # MCP skill chính (Ngày này năm xưa)
├── mcp_pipe.py         # Trình kết nối tới MCP endpoint
├── requirements.txt    # Danh sách thư viện cần thiết
├── README.md           # Tài liệu hướng dẫn
└── index.json          # Metadata mô tả skill (tùy chọn)
```

🧾 index.json (tùy chọn)
File này giúp mô tả skill cho MCP client (như ChatGPT hoặc XiaoZhi):

```
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
```
## 💡 Gợi ý mở rộng
Bạn có thể:

🔌 Thêm công cụ khác (VD: “Tin tức hôm nay”, “Thời tiết hiện tại”).

🧠 Kết hợp nhiều MCP skill thành cụm tiện ích thông minh.

🕹️ Tạo UI hiển thị sự kiện hoặc gửi qua Telegram / Discord.

📦 Đóng gói thành Docker container để chạy trên cloud.

## 🧑‍💻 Tác giả
VD Lập Trình
📘 GitHub: @vdlaptrinh
🌐 Website: https://vdlaptrinh.github.io
💬 Email: contact@vdlaptrinh.com

##  Giấy phép
Phát hành theo MIT License.
Bạn được phép sử dụng, chỉnh sửa, phân phối tự do với điều kiện ghi rõ nguồn gốc.

## 🧩 MCP-History – Một phần mở rộng nhỏ nhưng mạnh mẽ cho hệ sinh thái XiaoZhi AI.

## Tự động thực hiện:

Kích hoạt môi trường ảo mcp_history_env

Thiết lập endpoint MCP_ENDPOINT

Chạy mcp_pipe.py kết nối với server.py

Khởi động cùng hệ thống bằng systemd

## 1️⃣ Viết script khởi động
Tạo file:
```
sudo nano /home/pi/start_mcp_history.sh
```

Thêm nội dung sau:
```
#!/bin/bash
# === Script khởi động MCP-History ===

# Chờ hệ thống ổn định mạng (quan trọng để kết nối wss)
sleep 10

# Kích hoạt môi trường ảo
source /home/pi/mcp-history/mcp_history_env/bin/activate

# Thiết lập endpoint MCP
export MCP_ENDPOINT=wss://api.xiaozhi.me/...

# Chuyển đến thư mục dự án
cd /home/pi/mcp-history

# Ghi log để dễ kiểm tra
echo "=== MCP-History started at $(date) ===" >> /home/pi/mcp-history/mcp_history.log

# Chạy chương trình (server + pipe)
python3 mcp_pipe.py server.py >> /home/pi/mcp-history/mcp_history.log 2>&1
```

Lưu lại (Ctrl + O, Enter, Ctrl + X), rồi cấp quyền thực thi:
```
sudo chmod +x /home/pi/start_mcp_history.sh
```
## ⚙️ 2️⃣ Tạo file dịch vụ systemd

Tạo service:
```
sudo nano /etc/systemd/system/mcp_history.service
```


Thêm nội dung sau:
```
[Unit]
Description=MCP-History Skill for XiaoZhi AI
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/mcp-history
ExecStart=/home/pi/start_mcp_history.sh
Restart=always
RestartSec=5
StandardOutput=append:/home/pi/mcp-history/mcp_history.log
StandardError=append:/home/pi/mcp-history/mcp_history.log
Environment="MCP_ENDPOINT=wss://api.xiaozhi.me/..."

[Install]
WantedBy=multi-user.target
```

Lưu lại và thoát.

## 🚀 3️⃣ Kích hoạt và khởi động dịch vụ

Chạy các lệnh sau:
```
sudo systemctl daemon-reload
sudo systemctl enable mcp_history.service
sudo systemctl start mcp_history.service
```


Kiểm tra trạng thái:

sudo systemctl status mcp_history.service

## 🧩 4️⃣ Kiểm tra log hoạt động

Xem log MCP-History:
```
tail -f /home/pi/mcp-history/mcp_history.log
```
## ✅ 5️⃣ Tự khởi động sau reboot

Từ giờ, mỗi lần Raspberry Pi khởi động, nó sẽ tự động:

kích hoạt môi trường mcp_history_env

kết nối tới wss://api.xiaozhi.me/mcp-history

chạy mcp_pipe.py + server.py

ghi log ra /home/pi/mcp-history/mcp_history.log