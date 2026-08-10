from app.services.financial_processor import FinancialProcessor
from app.services.historical_processor import HistoricalProcessor
from app.services.openai_service import OpenAIService
from app.services.score_engine import ScoreEngine
from app.tools.yahoo_client import YahooFinanceClient


class AnalysisService:

    def __init__(self):

        self.yahoo = YahooFinanceClient()
        self.processor = FinancialProcessor()
        self.history_processor = HistoricalProcessor()
        self.score_engine = ScoreEngine()
        self.openai = OpenAIService()

    def analyze(self, ticker: str):

        # ---------------------------------
        # Fetch Data
        # ---------------------------------

        company_data = self.yahoo.get_company_data(ticker)

        historical_data = self.yahoo.get_historical_financials(ticker)

        # ---------------------------------
        # Process Current Financials
        # ---------------------------------

        stock = self.processor.process(company_data)

        # ---------------------------------
        # Process Historical Metrics
        # ---------------------------------

        historical_metrics = self.history_processor.process(
            historical_data
        )

        # Merge both dictionaries
        stock.update(historical_metrics)

        # ---------------------------------
        # Calculate Investment Score
        # ---------------------------------

        investment = self.score_engine.calculate(stock)

        # ---------------------------------
        # AI Analysis
        # ---------------------------------

        ai_response = self.openai.analyze(
            {
                "stock": stock,
                "investment": investment
            }
        )

        # ---------------------------------
        # Final Response
        # ---------------------------------

        return {

            "stock": stock,

            "investment": investment,

            "analysis": ai_response

        }