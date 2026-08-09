from dataclasses import asdict

from app.services.financial_processor import FinancialProcessor
from app.services.openai_service import OpenAIService
from app.services.score_engine import ScoreEngine
from app.tools.yahoo_client import YahooFinanceClient


class AnalysisService:

    def __init__(self):

        self.yahoo = YahooFinanceClient()
        self.processor = FinancialProcessor()
        self.score_engine = ScoreEngine()
        self.openai = OpenAIService()

    def analyze(self, ticker: str):

        raw = self.yahoo.get_company_data(ticker)

        stock = self.processor.process(raw)

        investment = self.score_engine.calculate(stock)

        ai_response = self.openai.analyze(
            {
                "stock": asdict(stock),
                "investment": asdict(investment)
            }
        )

        return {

            "stock": asdict(stock),

            "investment": asdict(investment),

            "analysis": ai_response

        }