from pydantic import BaseModel


class HistoricalFinancials(BaseModel):

    revenue: list[float] = []

    operating_income: list[float] = []

    net_income: list[float] = []

    free_cash_flow: list[float] = []