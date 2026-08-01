from fastapi import APIRouter

from app.models.stock import StockRequest
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/api/v1/stocks",
    tags=["Stocks"]
)

analysis_service = AnalysisService()


@router.post("/analyze")
def analyze_stock(request: StockRequest):

    return analysis_service.analyze(request.ticker)