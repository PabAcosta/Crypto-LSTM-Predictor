import numpy as np
import data_handling as dh
import pandas as pd
from tensorflow import Sequential, LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

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

def split_data(X, y, train_ratio):
  # Calculate the index at which to split the data
  split_index = int(len(X) * train_ratio)

  # Split the data into training and testing sets
  X_train = X[:split_index]
  X_test = X[split_index:]
  y_train = y[:split_index]
  y_test = y[split_index:]

  return X_train, X_test, y_train, y_test

def scale_data(data, feature_cols, target_col):
  # Initialize scalers for features and target
  feature_scaler = MinMaxScaler()
  target_scaler = MinMaxScaler()

  # Fit the scalers to the data and transform the features and target
  scaled_features = feature_scaler.fit_transform(data[feature_cols])
  scaled_target = target_scaler.fit_transform(data[[target_col]])

  return scaled_features, scaled_target, feature_scaler, target_scaler

def prepare_training_data(merged_df, feature_cols, target_col, lookback, train_ratio):
  # Scale the features and target
  scaled_features, scaled_target, feature_scaler, target_scaler = scale_data(merged_df,feature_cols,target_col)
  scaled_df = merged_df.copy()
  scaled_df[feature_cols] = scaled_features
  scaled_df[target_col] = scaled_target

  # Create sequences of features and corresponding targets
  X,y = make_sequences(scaled_df,feature_cols,target_col,lookback)
  X_train, X_test, y_train, y_test = split_data(X,y,train_ratio)

  return X_train, X_test, y_train, y_test, feature_scaler, target_scaler 

def build_lstm_model(input_shape):
  model = Sequential()
  model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
  model.add(LSTM(50))
  model.add(Dense(25))
  model.add(Dense(1))

  model.compile(optimizer="adam", loss="mean_squared_error")
  return model

def train_model_for_target():
  # prepare the data
  # build the model
  # fit the model
  # return the model and scalers
  return

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

  dh.fetch_crypto_data(tickers)
  merged_df = dh.merge_crypto_data(asset_files)

  feature_cols = ["BTC_Close", "ETH_Close"]
  target_col = "XRP_Close"

  prepare_training_data(merged_df,feature_cols,target_col,60,0.8)
  model = build_lstm_model((60, 2))
  print(type(merged_df))