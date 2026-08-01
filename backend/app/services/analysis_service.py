from app.services.openai_service import OpenAIService
from app.services.score_engine import ScoreEngine
from app.services.stock_processor import StockProcessor
from app.tools.yahoo_client import YahooFinanceClient


class AnalysisService:

    def __init__(self):

        self.yahoo = YahooFinanceClient()
        self.processor = StockProcessor()
        self.score_engine = ScoreEngine()
        self.openai = OpenAIService()

    def analyze(self, ticker: str):

        raw_data = self.yahoo.get_stock(ticker)

        stock = self.processor.process(raw_data)

        score = self.score_engine.calculate(stock)

        analysis = self.openai.analyze(stock)

        return {
            "stock": stock,
            "score": score,
            "analysis": analysis,
        }