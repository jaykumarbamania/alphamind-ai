from typing import Dict


class ScoreEngine:

    def calculate(self, stock: Dict) -> Dict:

        score = 0

        breakdown = {}

        # -----------------------------
        # Market Cap
        # -----------------------------
        market_cap = stock.get("market_cap")

        if market_cap:

            if market_cap > 200_000_000_000:
                score += 15
                breakdown["market_cap"] = 15

            elif market_cap > 50_000_000_000:
                score += 10
                breakdown["market_cap"] = 10

            else:
                breakdown["market_cap"] = 5

        # -----------------------------
        # PE Ratio
        # -----------------------------
        pe = stock.get("trailing_pe")

        if pe:

            if 10 <= pe <= 30:
                score += 20
                breakdown["valuation"] = 20

            elif pe < 40:
                score += 15
                breakdown["valuation"] = 15

            else:
                breakdown["valuation"] = 5

        # -----------------------------
        # Profitability
        # -----------------------------
        net_income = stock.get("net_income")

        if net_income:

            if net_income > 0:
                score += 20
                breakdown["profitability"] = 20

        # -----------------------------
        # Cash Flow
        # -----------------------------
        fcf = stock.get("free_cash_flow")

        if fcf:

            if fcf > 0:
                score += 20
                breakdown["cashflow"] = 20

        # -----------------------------
        # Debt
        # -----------------------------
        debt = stock.get("total_debt")

        if debt is None:

            score += 10
            breakdown["debt"] = 10

        elif debt < 100_000_000_000:

            score += 10
            breakdown["debt"] = 10

        else:

            score += 5
            breakdown["debt"] = 5

        # -----------------------------
        # Dividend
        # -----------------------------
        dividend = stock.get("dividend_yield")

        if dividend:

            score += 15
            breakdown["dividend"] = 15

        return {

            "overall_score": score,

            "breakdown": breakdown
        }