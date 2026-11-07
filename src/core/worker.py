import yfinance as yf

tickers = ["JOBY", "AMZN"]
for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    def stock_curr_price(info):
        history = stock.history(period="1d", interval="1m")
        if history.empty:
            print(f"No data found for {ticker}")
            return None
        price = history['Close'].iloc[-1]
        return price

    print(f"Symbol: {ticker}")
    print(f"Name: {info.get('shortName', 'N/A')}")
    price = stock_curr_price(info)
    print(f"Current Price: {price}")
    print("--------------------------------------")
