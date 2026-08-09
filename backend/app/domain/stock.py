from dataclasses import dataclass
from typing import Optional


@dataclass
class Stock:

    company: Optional[str]

    symbol: Optional[str]

    sector: Optional[str]

    industry: Optional[str]

    current_price: Optional[float]

    market_cap: Optional[float]

    trailing_pe: Optional[float]

    forward_pe: Optional[float]

    dividend_yield: Optional[float]

    revenue: Optional[float]

    gross_profit: Optional[float]

    operating_income: Optional[float]

    net_income: Optional[float]

    total_assets: Optional[float]

    total_liabilities: Optional[float]

    cash: Optional[float]

    total_debt: Optional[float]

    operating_cash_flow: Optional[float]

    free_cash_flow: Optional[float]

    business_summary: Optional[str]