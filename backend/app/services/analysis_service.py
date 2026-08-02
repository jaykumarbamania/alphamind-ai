# from app.services.openai_service import OpenAIService
# from app.services.score_engine import ScoreEngine
# from app.services.stock_processor import StockProcessor
# from app.tools.yahoo_client import YahooFinanceClient


# class AnalysisService:

#     def __init__(self):

#         self.yahoo = YahooFinanceClient()
#         self.processor = StockProcessor()
#         self.score_engine = ScoreEngine()
#         self.openai = OpenAIService()

#     def analyze(self, ticker: str):

#         raw_data = self.yahoo.get_stock(ticker)

#         stock = self.processor.process(raw_data)

#         score = self.score_engine.calculate(stock)

#         analysis = self.openai.analyze(stock)

#         return {
#             "stock": stock,
#             "score": score,
#             "analysis": analysis,
#         }

# from app.services.openai_service import OpenAIService
# from app.services.score_engine import ScoreEngine
# from app.services.financial_processor import FinancialProcessor
# from app.tools.yahoo_client import YahooFinanceClient


# class AnalysisService:

#     def __init__(self):

#         self.yahoo = YahooFinanceClient()

#         self.processor = FinancialProcessor()

#         self.score_engine = ScoreEngine()

#         self.openai = OpenAIService()

#     def analyze(
#         self,
#         ticker: str,
#     ):

#         raw_data = self.yahoo.get_company_data(
#             ticker
#         )

#         processed = self.processor.process(
#             raw_data
#         )

#         score = self.score_engine.calculate(
#             processed
#         )

#         analysis = self.openai.analyze(
#             processed
#         )

#         return {

#             "stock": processed,

#             "score": score,

#             "analysis": analysis,
#         }

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

        processed = self.processor.process(raw)

        score = self.score_engine.calculate(processed)

        processed["investment_score"] = score

        analysis = self.openai.analyze(processed)

        return {

            "stock": processed,

            "analysis": analysis

        }