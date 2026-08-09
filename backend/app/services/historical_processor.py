from app.services.growth_calculator import GrowthCalculator


class HistoricalProcessor:

    def process(self, history):

        return {

            "revenue_cagr":

                GrowthCalculator.cagr(

                    history.revenue

                ),

            "net_income_cagr":

                GrowthCalculator.cagr(

                    history.net_income

                ),

            "free_cash_flow_cagr":

                GrowthCalculator.cagr(

                    history.free_cash_flow

                ),

            "average_revenue_growth":

                GrowthCalculator.average_growth(

                    history.revenue

                ),

            "average_profit_growth":

                GrowthCalculator.average_growth(

                    history.net_income

                )

        }