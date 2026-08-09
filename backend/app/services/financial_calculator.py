from typing import Optional


class FinancialCalculator:

    @staticmethod
    def gross_margin(
        revenue: Optional[float],
        gross_profit: Optional[float]
    ) -> Optional[float]:

        if not revenue or not gross_profit:
            return None

        return round((gross_profit / revenue) * 100, 2)

    @staticmethod
    def operating_margin(
        revenue: Optional[float],
        operating_income: Optional[float]
    ) -> Optional[float]:

        if not revenue or not operating_income:
            return None

        return round((operating_income / revenue) * 100, 2)

    @staticmethod
    def net_margin(
        revenue: Optional[float],
        net_income: Optional[float]
    ) -> Optional[float]:

        if not revenue or not net_income:
            return None

        return round((net_income / revenue) * 100, 2)

    @staticmethod
    def debt_ratio(
        total_assets: Optional[float],
        total_liabilities: Optional[float]
    ) -> Optional[float]:

        if not total_assets or not total_liabilities:
            return None

        return round((total_liabilities / total_assets) * 100, 2)

    @staticmethod
    def cash_to_debt_ratio(
        cash: Optional[float],
        debt: Optional[float]
    ) -> Optional[float]:

        if not cash or not debt:
            return None

        return round(cash / debt, 2)

    @staticmethod
    def free_cash_flow_margin(
        revenue: Optional[float],
        free_cash_flow: Optional[float]
    ) -> Optional[float]:

        if not revenue or not free_cash_flow:
            return None

        return round((free_cash_flow / revenue) * 100, 2)