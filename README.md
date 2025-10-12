# mcp-history
mcp-history for xiaozhi AI

git clone https://github.com/vdlaptrinh/mcp-history.git

python3 -m venv mcp_history_env
source mcp_history_env/bin/activate    


cd mcp-history/

pip install -r requirements.txt

export MCP_ENDPOINT=wss://api.xiaozhi.me/mcp...
python mcp_pipe.py /home/pi/mcp-history/server.py
