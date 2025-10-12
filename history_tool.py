# server.py
from mcp.server.fastmcp import FastMCP
import sys
import logging
from history_tool import fetch_history

logger = logging.getLogger("NgayNayNamXua")

# Fix UTF-8 encoding (đặc biệt cần thiết trên Windows hoặc Raspberry Pi)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# === MCP SERVER KHỞI TẠO ===
mcp = FastMCP("ngay_nay_nam_xua")

# === TOOL: Lịch sử hôm nay / hôm qua / ngày mai ===
@mcp.tool()
def ngay_nay_nam_xua(opt: str = "TODAY") -> str:
    """
    📜 Trả về sự kiện lịch sử 'Ngày này năm xưa'.
    Tham số:
      opt: "TODAY" | "YESTERDAY" | "TOMORROW"
    """
    return fetch_history(opt)

# === CHẠY SERVER ===
if __name__ == "__main__":
    mcp.run()
