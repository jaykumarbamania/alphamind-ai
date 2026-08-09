from pydantic import BaseModel


class InvestmentScore(BaseModel):
    growth: int = 0
    profitability: int = 0
    valuation: int = 0
    cash_flow: int = 0
    financial_health: int = 0

    total: int = 0
    recommendation: str = "WATCH"