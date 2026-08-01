import yfinance as yf


class YahooFinanceClient:

    def get_stock(self, ticker: str) -> dict:

        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "company": info.get("longName"),
            "symbol": info.get("symbol"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice"),
            "trailing_pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "dividend_yield": info.get("dividendYield"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            "business_summary": info.get("longBusinessSummary"),
        }