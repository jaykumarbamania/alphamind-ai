class ScoreEngine:
    
    def calculate(self, stock: dict) -> int:

        score = 0

        pe = stock.get("trailing_pe")
        market_cap = stock.get("market_cap")
        dividend = stock.get("dividend_yield")

        if market_cap and market_cap > 10_000_000_000:
            score += 30

        if pe and pe < 30:
            score += 40

        if dividend:
            score += 30

        return score