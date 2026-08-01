from fastapi import FastAPI
from app.services.stock_service import StockService

from app.api.stock import router as stock_router

app = FastAPI(
    title="AlphaMind AI",
    version="1.0.0"
)

stock_service = StockService()

@app.get("/")
def home():
    return {
        "message": "Welcome to AlphaMind AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/stock/{ticker}")
def analyze_stock(ticker: str):

    return stock_service.get_stock_info(ticker)


app.include_router(stock_router)