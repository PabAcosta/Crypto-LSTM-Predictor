import numpy as np
import data_handling as dh
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
