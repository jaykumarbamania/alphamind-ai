from fastapi import APIRouter

from app.models.stock import StockRequest
from app.tools.yahoo_tool import get_stock_data

router = APIRouter()


@router.post("/analyze")
def analyze_stock(request: StockRequest):

    data = get_stock_data(request.ticker)

    return data