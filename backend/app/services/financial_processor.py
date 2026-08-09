from app.domain.stock import Stock


class FinancialProcessor:

    def process(self, data):

        stock = data.stock

        financial = data.financials

        return Stock(

            company=stock.company,

            symbol=stock.symbol,

            sector=stock.sector,

            industry=stock.industry,

            current_price=stock.current_price,

            market_cap=stock.market_cap,

            trailing_pe=stock.trailing_pe,

            forward_pe=stock.forward_pe,

            dividend_yield=stock.dividend_yield,

            revenue=financial.revenue,

            gross_profit=financial.gross_profit,

            operating_income=financial.operating_income,

            net_income=financial.net_income,

            total_assets=financial.total_assets,

            total_liabilities=financial.total_liabilities,

            cash=financial.cash,

            total_debt=financial.total_debt,

            operating_cash_flow=financial.operating_cash_flow,

            free_cash_flow=financial.free_cash_flow,

            business_summary=stock.business_summary,

        )