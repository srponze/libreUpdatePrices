from libre_update_prices.libreOffice import LibreOffice
from libre_update_prices.yfinance import YFinance

libreOffice = LibreOffice("/path/to/file/.ods")
yFinance = YFinance()

row = 1  # 1 is the first row, not 0
column = "A"  # Column AA onwards doesn't work
ticker = libreOffice.getDatum(row, column)
# ticker simbol may be a exchange rate, USDEUR=X, for example, search in yahoo finance
price = yFinance.getPrice(ticker)
libreOffice.setDatum(price, row, column)

start = 1
end = 2
column = "B"
tickers = libreOffice.getData(start, end, column)
listPrices = yFinance.getListPrices(tickers)
libreOffice.setData(listPrices, start, column)
