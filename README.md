# FastAPI + Docker Compose 快速部署指南

本指南將帶領您從零開始，在本機端建立一個基於 FastAPI 的 API Server，並透過 Docker Compose 實現容器化自動部署。所有步驟與代碼均經過驗證。

---

## 📋 環境需求
* 已安裝 **Docker Desktop** (並確保正在運行)
* 終端機工具 (PowerShell, Command Prompt, 或 Terminal)

---

## 🚀 部署步驟

### 步驟一：建立專案資料夾
建立一個獨立的空間來存放專案檔案。

```bash
mkdir my-local-api
cd my-local-api
```

### 步驟二：建立應用程式主程式 (`main.py`)
這是 API 的核心邏輯。

```python
from fastapi import FastAPI

app = FastAPI(title="Local API Server")

@app.get("/")
def read_root():
    return {
        "status": "success", 
        "message": "API Server is successfully running via Docker Compose."
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "service": "Local API"
    }
```

### 步驟三：建立相依套件清單 (`requirements.txt`)
明確指定套件版本以確保環境一致性。

```text
fastapi==0.110.0
uvicorn==0.29.0
```

### 步驟四：撰寫 Docker 配置檔案 (`Dockerfile`)
定義映像檔 (Image) 的建置流程。

```dockerfile
# 使用官方輕量級 Python 3.11 映像檔
FROM python:3.11-slim

# 設定容器內的工作目錄
WORKDIR /app

# 複製相依套件清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製當前目錄下所有檔案至容器
COPY . .

# 宣告容器監聽之 Port (文件性質)
EXPOSE 8000

# 啟動指令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 步驟五：設定 Docker Compose (`docker-compose.yml`)
定義服務運作參數。

```yaml
version: '3.8'

services:
  api_server:
    build: .
    container_name: local_fastapi_server
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - TZ=Asia/Taipei
```

---

## 🛠️ 服務管理指令

### 1. 啟動服務
執行以下指令建置並於背景執行容器：
```bash
docker compose up -d --build
```

### 2. 驗證服務
* **首頁測試：** 瀏覽 [http://localhost:8000/](http://localhost:8000/)
* **互動式 API 文件 (Swagger UI)：** 瀏覽 [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. 停止服務
若需停止並移除容器設定，請執行：
```bash
docker compose down
```

---

## 📝 注意事項
* 若修改了 `main.py` 或 `requirements.txt`，重啟時請務必加上 `--build` 參數以更新映像檔。
* 確保本機 8000 Port 未被其他應用程式佔用。
