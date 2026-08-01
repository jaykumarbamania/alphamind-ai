class StockProcessor:
    
    def process(self, data: dict) -> dict:

        return {
            "company": data.get("company"),
            "sector": data.get("sector"),
            "industry": data.get("industry"),
            "market_cap": data.get("market_cap"),
            "current_price": data.get("current_price"),
            "trailing_pe": data.get("trailing_pe"),
            "forward_pe": data.get("forward_pe"),
            "dividend_yield": data.get("dividend_yield"),
            "business_summary": data.get("business_summary")
        }