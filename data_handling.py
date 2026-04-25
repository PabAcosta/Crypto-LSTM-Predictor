import os
import pandas as pd
import numpy as np
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

def load_crypto_csv(path, asset_name):
  # Load the CSV file into a DataFrame
  df = pd.read_csv(path, skiprows=2, usecols=[0, 1])

  # Rename the columns to 'Date' and Close
  df.columns = ['Date', asset_name + "_Close"]
  
  return df

def merge_crypto_data(asset_files):
  # Initialize an empty list to hold the DataFrames
  dataframes = []

  # Loop through the asset files and load each one into a DataFrame
  for asset_name, path in asset_files.items():
    df = load_crypto_csv(path, asset_name)
    dataframes.append(df)

  # Merge all DataFrames on the 'Date' column
  merged_df = dataframes[0]
  for df in dataframes[1:]:
    merged_df = pd.merge(merged_df, df, on='Date')

  return merged_df

def make_sequences(data, feature_cols, target_col, lookback):
  # Initialize lists to hold the sequences of features and targets
  X = []
  y = []

  # Create sequences of features and corresponding targets
  for i in range(len(data) - lookback):
    X_window = data[feature_cols].iloc[i:i+lookback].values
    y_value = data[target_col].iloc[i+lookback]
    X.append(X_window)
    y.append(y_value)

  return np.array(X), np.array(y)

if __name__ == "__main__":
    # Define the cryptocurrency tickers to download
    tickers = ["ETH-USD", "BTC-USD", "XRP-USD", "SOL-USD", "DOGE-USD"]
    asset_files = {
    "BTC": "data/BTC_USD.csv",
    "ETH": "data/ETH_USD.csv",
    "XRP": "data/XRP_USD.csv",
    "SOL": "data/SOL_USD.csv",
    "DOGE": "data/DOGE_USD.csv"
    }

    fetch_crypto_data(tickers)
    merge_crypto_data(asset_files)
