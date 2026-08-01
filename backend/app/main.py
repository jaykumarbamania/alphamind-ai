from fastapi import FastAPI

from app.api.stock import router as stock_router

app = FastAPI(
    title="AlphaMind AI",
    version="1.0.0",
)

app.include_router(stock_router)


@app.get("/")
def home():
    return {"message": "Welcome to AlphaMind AI 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}