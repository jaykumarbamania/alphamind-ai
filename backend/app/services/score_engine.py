from app.models.investment import InvestmentScore


class ScoreEngine:

    def calculate(self, stock):

        score = InvestmentScore()

        pe = stock.get("trailing_pe")

        if pe:

            if pe < 20:
                score.valuation = 20

            elif pe < 30:
                score.valuation = 15

            elif pe < 40:
                score.valuation = 10

        if stock.get("free_cash_flow"):

            if stock["free_cash_flow"] > 0:
                score.cash_flow = 20

        if stock.get("net_income"):

            if stock["net_income"] > 0:
                score.profitability += 15

        if stock.get("market_cap"):

            if stock["market_cap"] > 100_000_000_000:
                score.financial_health += 15

        if stock.get("dividend_yield"):

            score.financial_health += 5

        score.total = (
            score.growth
            + score.profitability
            + score.valuation
            + score.cash_flow
            + score.financial_health
        )

        if score.total >= 90:
            score.recommendation = "STRONG BUY"

        elif score.total >= 80:
            score.recommendation = "BUY"

        elif score.total >= 70:
            score.recommendation = "HOLD"

        elif score.total >= 60:
            score.recommendation = "WATCH"

        else:
            score.recommendation = "AVOID"

        return score