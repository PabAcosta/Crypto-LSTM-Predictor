import os
import yfinance

# Define the cryptocurrency tickers to download
tickers = ["ETH-USD", "BTC-USD"]

# Set the date range for historical data
from datetime import datetime
start = "2018-01-01"
end = datetime.now().strftime("%Y-%m-%d")

# Define folder where data will be saved
path = "data"
pathExist = os.path.exists(path)
if not pathExist:
  os.makedirs(path)

# Loop through each ticker and download its historical price data
for ticker in tickers:
  print("Loading " + ticker + "...")
  data = yfinance.download(ticker, start, end)
  if data.empty:
    print(ticker + " download failed")
    continue
  # Save the data to a CSV file with a clean filename
  data.to_csv("data/" + ticker.replace("-", "_") + ".csv")
  print(ticker + " downloaded")