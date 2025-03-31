'''
import yfinance as yf

# Define the stock ticker symbol for Tesla
ticker_symbol = "TSLA"

# Create a Ticker object
tesla_data = yf.Ticker(ticker_symbol)

# Get historical stock data (maximum available)
tesla_data = tesla_data.history(period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first 5 rows
print(tesla_data.head())


import yfinance as yf

# Define the stock ticker symbol for Tesla
ticker_symbol = "TSLA"

# Create a Ticker object
tesla_data = yf.Ticker(ticker_symbol)

# Get the Tesla financials (Income Statement)
financials = tesla_data.financials

# Extract the revenue data
revenue_data = financials.loc['Total Revenue']

# Display the last 5 rows of the revenue data
print(revenue_data.tail())


import yfinance as yf
ticker_symbol = "GME"
gme_data = yf.Ticker(ticker_symbol)
gme_data = gme_data.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())

import yfinance as yf

ticker_symbol = "GME"
gme_data = yf.Ticker(ticker_symbol)
financials = gme_data.financials
gme_revenue = financials.loc['Total Revenue']
print(gme_revenue.tail())



import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    data['Close'].plot(figsize=(10, 6))
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.grid(True)
    plt.show()

ticker_symbol = "TSLA"
tesla_data = yf.Ticker(ticker_symbol)
tesla_stock_data = tesla_data.history(period="max")
make_graph(tesla_stock_data, "Tesla Stock Price")'
'''
import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    data['Close'].plot(figsize=(10, 6))
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.grid(True)
    plt.show()

ticker_symbol = "GME"
gme_data = yf.Ticker(ticker_symbol)
gme_stock_data = gme_data.history(period="max")
make_graph(gme_stock_data, "GameStop Stock Price")
