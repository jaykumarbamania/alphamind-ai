class ScoreEngine:
    
    def calculate(self, stock):

        score = 0

        breakdown = {}

        # -----------------------
        # Valuation
        # -----------------------

        pe = stock.get("trailing_pe")

        if pe:

            if pe < 20:

                score += 20

                breakdown["PE"] = 20

            elif pe < 30:

                score += 15

                breakdown["PE"] = 15

        # -----------------------
        # Net Margin
        # -----------------------

        margin = stock.get("net_margin")

        if margin:

            if margin > 20:

                score += 20

                breakdown["Net Margin"] = 20

            elif margin > 10:

                score += 15

                breakdown["Net Margin"] = 15

        # -----------------------
        # Gross Margin
        # -----------------------

        gross = stock.get("gross_margin")

        if gross:

            if gross > 50:

                score += 15

                breakdown["Gross Margin"] = 15

        # -----------------------
        # Cash Flow
        # -----------------------

        if stock.get("free_cash_flow", 0) > 0:

            score += 20

            breakdown["Free Cash Flow"] = 20

        # -----------------------
        # Debt
        # -----------------------

        debt = stock.get("debt_ratio")

        if debt:

            if debt < 50:

                score += 15

                breakdown["Debt"] = 15

            elif debt < 70:

                score += 10

                breakdown["Debt"] = 10

        # -----------------------

        recommendation = "AVOID"

        if score >= 85:

            recommendation = "STRONG BUY"

        elif score >= 70:

            recommendation = "BUY"

        elif score >= 55:

            recommendation = "HOLD"

        elif score >= 40:

            recommendation = "WATCH"

        return {

            "overall_score": score,

            "recommendation": recommendation,

            "breakdown": breakdown

        }