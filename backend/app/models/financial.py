from pydantic import BaseModel
from typing import Optional


class StockInfo(BaseModel):
    company: Optional[str] = None
    symbol: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None

    market_cap: Optional[int] = None
    current_price: Optional[float] = None

    trailing_pe: Optional[float] = None
    forward_pe: Optional[float] = None

    dividend_yield: Optional[float] = None

    fifty_two_week_high: Optional[float] = None
    fifty_two_week_low: Optional[float] = None

    business_summary: Optional[str] = None


class FinancialMetrics(BaseModel):
    revenue: Optional[float] = None
    gross_profit: Optional[float] = None
    operating_income: Optional[float] = None
    net_income: Optional[float] = None

    total_assets: Optional[float] = None
    total_liabilities: Optional[float] = None

    cash: Optional[float] = None
    total_debt: Optional[float] = None

    operating_cash_flow: Optional[float] = None
    free_cash_flow: Optional[float] = None


class CompanyFinancialData(BaseModel):
    stock: StockInfo
    financials: FinancialMetrics