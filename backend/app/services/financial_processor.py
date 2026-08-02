from app.models.financial import CompanyFinancialData


class FinancialProcessor:

    def process(
        self,
        data: CompanyFinancialData,
    ):

        stock = data.stock
        financials = data.financials

        return {

            "company": stock.company,

            "symbol": stock.symbol,

            "sector": stock.sector,

            "industry": stock.industry,

            "market_cap": stock.market_cap,

            "current_price": stock.current_price,

            "trailing_pe": stock.trailing_pe,

            "forward_pe": stock.forward_pe,

            "dividend_yield": stock.dividend_yield,

            "revenue": financials.revenue,

            "gross_profit": financials.gross_profit,

            "operating_income": financials.operating_income,

            "net_income": financials.net_income,

            "total_assets": financials.total_assets,

            "total_liabilities": financials.total_liabilities,

            "cash": financials.cash,

            "total_debt": financials.total_debt,

            "operating_cash_flow": financials.operating_cash_flow,

            "free_cash_flow": financials.free_cash_flow,

            "business_summary": stock.business_summary,
        }