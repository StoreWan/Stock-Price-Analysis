import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and time range
stock_symbol = "MSFT" 
start_date = "2020-01-01"
end_date = "2025-01-01"

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)


# Moving average columns (MA)
stock_data['10-day MA'] = stock_data['Close'].rolling(window=10).mean()
stock_data['50-day MA'] = stock_data['Close'].rolling(window=50).mean()

# Delete comment for error handling
# print(stock_data.head())
# print(stock_data.isnull().sum())
# print(stock_data.describe())


# Plot for stock prices with MA's
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label=f'{stock_symbol} Close Price', linewidth=1)
plt.plot(stock_data['10-day MA'], label='10-Day Moving Average', linestyle='--')
plt.plot(stock_data['50-day MA'], label='50-Day Moving Average', linestyle='--')

plt.title(f'{stock_symbol} Stock Price Analysis')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

stock_data['Daily Return'] = stock_data['Close'].pct_change()

stock_data['Daily Return'].plot(kind='hist', bins=50, figsize=(10, 6), title='Daily Return Distribution')
plt.show()

# save to csv
stock_data.to_csv('stock_data.csv')
