# server.py — MCP skill: Ngày này năm xưa (nguồn: lichngaytot.com)
from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import sys
import logging
import re

logger = logging.getLogger("NgayNayNamXua")

# Sửa lỗi UTF-8 khi in ra terminal
if sys.platform == "win32":
    sys.stderr.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

# === Khởi tạo MCP Server ===
mcp = FastMCP("NgayNayNamXua")

# ====== HÀM PHỤ ======
URL = "https://lichngaytot.com/ngay-nay-nam-xua.html"
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}

def get_date(opt="TODAY"):
    today = datetime.now()
    if opt == "YESTERDAY":
        return today - timedelta(days=1)
    elif opt == "TOMORROW":
        return today + timedelta(days=1)
    return today

def clean_content(content):
    """Làm sạch HTML và gộp nội dung"""
    if not content:
        return "Không tìm thấy nội dung lịch sử hôm nay."
    combined_text = " ".join(" ".join(el.get_text().strip().split()) for el in content)

    # Loại bỏ ngày trùng lặp (vd: "12-10-2024" lặp nhiều lần)
    date_pattern = r"\b(\d{1,2}-\d{1,2}-\d{4})\b"
    seen_dates = set()

    def remove_duplicates(match):
        date = match.group(1)
        if date in seen_dates:
            return ""
        seen_dates.add(date)
        return date

    cleaned_text = re.sub(date_pattern, remove_duplicates, combined_text)
    return ' '.join(cleaned_text.split())

def fetch_history(opt="TODAY"):
    try:
        selected_date = get_date(opt)
        payload = {'ngayxem': f"{selected_date.day:02d}-{selected_date.month:02d}-{selected_date.year}"}
        response = requests.post(URL, headers=HEADERS, data=payload, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all(class_='table1')
        text = clean_content(content)
        return text
    except Exception as e:
        return f"Lỗi khi lấy dữ liệu: {e}"

# ====== MCP TOOL ======
@mcp.tool()
def ngay_nay_nam_xua(opt: str = "TODAY") -> dict:
    """
    📜 Trả về sự kiện 'Ngày này năm xưa' bằng tiếng Việt (nguồn: lichngaytot.com)

    - opt: "TODAY" | "YESTERDAY" | "TOMORROW"
    """
    opt = opt.upper().strip()
    if opt not in ["TODAY", "YESTERDAY", "TOMORROW"]:
        opt = "TODAY"

    text = fetch_history(opt)
    logger.info(f"Lấy sự kiện {opt}: {text[:60]}...")
    return {"success": True, "option": opt, "events": text}


# ====== CHẠY SERVER ======
if __name__ == "__main__":
    mcp.run(transport="stdio")
