import yfinance as yf


class StockService:

    def get_stock_info(self, ticker: str):

        stock = yf.Ticker(ticker)

        return stock.info