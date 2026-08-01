from pydantic import BaseModel


class StockAnalysisResponse(BaseModel):
    stock: dict
    score: int
    analysis: str