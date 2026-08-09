from app.domain.investment_result import InvestmentResult


class ScoreEngine:

    def calculate(self, stock):

        score = 0

        breakdown = {}

        # ------------------------

        if stock.market_cap:

            if stock.market_cap > 200_000_000_000:

                score += 15

                breakdown["Market Cap"] = 15

        # ------------------------

        if stock.trailing_pe:

            if stock.trailing_pe < 20:

                score += 20

                breakdown["Valuation"] = 20

            elif stock.trailing_pe < 30:

                score += 15

                breakdown["Valuation"] = 15

        # ------------------------

        if stock.net_income:

            if stock.net_income > 0:

                score += 20

                breakdown["Profitability"] = 20

        # ------------------------

        if stock.free_cash_flow:

            if stock.free_cash_flow > 0:

                score += 20

                breakdown["Cash Flow"] = 20

        # ------------------------

        if stock.dividend_yield:

            score += 5

            breakdown["Dividend"] = 5

        # ------------------------

        recommendation = "WATCH"

        if score >= 90:

            recommendation = "STRONG BUY"

        elif score >= 80:

            recommendation = "BUY"

        elif score >= 70:

            recommendation = "HOLD"

        elif score >= 60:

            recommendation = "WATCH"

        else:

            recommendation = "AVOID"

        return InvestmentResult(

            overall_score=score,

            recommendation=recommendation,

            breakdown=breakdown

        )