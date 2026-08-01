import yfinance as yf


def get_stock_data(symbol: str):

    stock = yf.Ticker(symbol)

    info = stock.info

    return {
        "company": info.get("longName"),
        "symbol": info.get("symbol"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "current_price": info.get("currentPrice"),
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "dividend_yield": info.get("dividendYield"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
        "website": info.get("website"),
        "business_summary": info.get("longBusinessSummary")
    }