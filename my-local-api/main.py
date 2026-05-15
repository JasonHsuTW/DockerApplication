from fastapi import FastAPI

app = FastAPI(title="Local API Server")

@app.get("/")
def read_root():
    return {"status": "success", "message": "API Server is successfully running via Docker Compose."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Local API"}