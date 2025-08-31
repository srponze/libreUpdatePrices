from typing import List

import yfinance as yf


class YFinance:

    def getListPrices(self, listTicker: List[str]) -> List[float]:
        listPrices = []
        for ticker in listTicker:
            yfTicker = yf.Ticker(ticker)
            price = yfTicker.get_fast_info().last_price
            if price is not None:
                price = float(price)
            else:
                price = 0.0
            listPrices.append(
                round(price, 4),
            )
        return listPrices

    def getPrice(self, ticker: str) -> float:
        yfTicker = yf.Ticker(ticker)
        price = yfTicker.get_fast_info().last_price
        if price is not None:
            return round(float(price), 4)
        else:
            return 0.0
