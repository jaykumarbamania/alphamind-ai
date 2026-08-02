# import yfinance as yf


# class YahooFinanceClient:

#     def get_stock(self, ticker: str) -> dict:

#         stock = yf.Ticker(ticker)

#         info = stock.info

#         return {
#             "company": info.get("longName"),
#             "symbol": info.get("symbol"),
#             "sector": info.get("sector"),
#             "industry": info.get("industry"),
#             "market_cap": info.get("marketCap"),
#             "current_price": info.get("currentPrice"),
#             "trailing_pe": info.get("trailingPE"),
#             "forward_pe": info.get("forwardPE"),
#             "dividend_yield": info.get("dividendYield"),
#             "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
#             "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
#             "business_summary": info.get("longBusinessSummary"),
#         }

import yfinance as yf

from app.models.financial import (
    StockInfo,
    FinancialMetrics,
    CompanyFinancialData,
)


class YahooFinanceClient:

    def get_company_data(
        self,
        ticker: str,
    ) -> CompanyFinancialData:

        stock = yf.Ticker(ticker)

        info = stock.info

        income_stmt = stock.income_stmt

        balance_sheet = stock.balance_sheet

        cash_flow = stock.cash_flow

        stock_info = StockInfo(
            company=info.get("longName"),
            symbol=info.get("symbol"),
            sector=info.get("sector"),
            industry=info.get("industry"),
            market_cap=info.get("marketCap"),
            current_price=info.get("currentPrice"),
            trailing_pe=info.get("trailingPE"),
            forward_pe=info.get("forwardPE"),
            dividend_yield=info.get("dividendYield"),
            fifty_two_week_high=info.get("fiftyTwoWeekHigh"),
            fifty_two_week_low=info.get("fiftyTwoWeekLow"),
            business_summary=info.get("longBusinessSummary"),
        )

        financials = FinancialMetrics(
            revenue=self._safe_lookup(
                income_stmt,
                "Total Revenue",
            ),
            gross_profit=self._safe_lookup(
                income_stmt,
                "Gross Profit",
            ),
            operating_income=self._safe_lookup(
                income_stmt,
                "Operating Income",
            ),
            net_income=self._safe_lookup(
                income_stmt,
                "Net Income",
            ),
            total_assets=self._safe_lookup(
                balance_sheet,
                "Total Assets",
            ),
            total_liabilities=self._safe_lookup(
                balance_sheet,
                "Total Liabilities Net Minority Interest",
            ),
            cash=self._safe_lookup(
                balance_sheet,
                "Cash And Cash Equivalents",
            ),
            total_debt=self._safe_lookup(
                balance_sheet,
                "Total Debt",
            ),
            operating_cash_flow=self._safe_lookup(
                cash_flow,
                "Operating Cash Flow",
            ),
            free_cash_flow=self._safe_lookup(
                cash_flow,
                "Free Cash Flow",
            ),
        )

        return CompanyFinancialData(
            stock=stock_info,
            financials=financials,
        )

    @staticmethod
    def _safe_lookup(frame, row_name):

        try:
            return float(frame.loc[row_name].iloc[0])
        except Exception:
            return None