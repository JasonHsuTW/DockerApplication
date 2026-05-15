# 使用官方輕量級的 Python 3.11 映像檔作為基底
FROM python:3.11-slim

# 設定容器內的工作目錄
WORKDIR /app

# 將本機的 requirements.txt 複製到容器內
COPY requirements.txt .

# 安裝相依套件 (不使用快取以減小映像檔體積)
RUN pip install --no-cache-dir -r requirements.txt

# 將本機當前目錄的所有檔案複製到容器內的工作目錄
COPY . .

# 宣告容器在運行時會監聽 8000 port (僅作為文件說明，實際曝露由 docker-compose 決定)
EXPOSE 8000

# 啟動 FastAPI 伺服器的指令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]