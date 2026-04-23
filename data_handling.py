import os
from datetime import datetime
import yfinance

def fetch_crypto_data(tickers, start_date="2018-01-01", end_date=None, save_dir="data"):

  # Set the date range for historical data
  if end_date is None:
    end_date = datetime.now().strftime("%Y-%m-%d")

  # Define folder where data will be saved
  os.makedirs(save_dir, exist_ok=True)

  # Loop through each ticker and download its historical price data
  for ticker in tickers:
    print("Loading " + ticker + "...")
    data = yfinance.download(ticker, start_date, end_date)
    if data.empty:
      print(ticker + " download failed")
      continue
    # Save the data to a CSV file with a clean filename
    file_path = os.path.join(save_dir, ticker.replace("-", "_") + ".csv")
    data.to_csv(file_path)
    print(ticker + " downloaded")


if __name__ == "__main__":
    # Define the cryptocurrency tickers to download
    tickers = ["ETH-USD", "BTC-USD", "XRP-USD", "SOL-USD"]
    fetch_crypto_data(tickers)
