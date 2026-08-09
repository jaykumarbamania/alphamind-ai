from app.models.financial import CompanyFinancialData
from app.services.financial_calculator import FinancialCalculator


class FinancialProcessor:

    def process(
        self,
        data: CompanyFinancialData,
    ):

        stock = data.stock
        financial = data.financials

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

            "revenue": financial.revenue,
            "gross_profit": financial.gross_profit,
            "operating_income": financial.operating_income,
            "net_income": financial.net_income,

            "total_assets": financial.total_assets,
            "total_liabilities": financial.total_liabilities,

            "cash": financial.cash,
            "total_debt": financial.total_debt,

            "operating_cash_flow": financial.operating_cash_flow,
            "free_cash_flow": financial.free_cash_flow,

            # Calculated Metrics

            "gross_margin":

                FinancialCalculator.gross_margin(

                    financial.revenue,

                    financial.gross_profit

                ),

            "operating_margin":

                FinancialCalculator.operating_margin(

                    financial.revenue,

                    financial.operating_income

                ),

            "net_margin":

                FinancialCalculator.net_margin(

                    financial.revenue,

                    financial.net_income

                ),

            "debt_ratio":

                FinancialCalculator.debt_ratio(

                    financial.total_assets,

                    financial.total_liabilities

                ),

            "cash_to_debt_ratio":

                FinancialCalculator.cash_to_debt_ratio(

                    financial.cash,

                    financial.total_debt

                ),

            "free_cash_flow_margin":

                FinancialCalculator.free_cash_flow_margin(

                    financial.revenue,

                    financial.free_cash_flow

                ),

            "business_summary": stock.business_summary

        }