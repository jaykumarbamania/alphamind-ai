from fastapi import APIRouter

from app.models.stock import StockRequest
from app.tools.yahoo_tool import get_stock_data
from app.services.openai_service import analyze_stock

router = APIRouter()


@router.post("/analyze")
def analyze_stock_request(request: StockRequest):

    data = get_stock_data(request.ticker)

    analysis = analyze_stock(data)

    return {
        "stock": data,
        
        "analysis": analysis
    }