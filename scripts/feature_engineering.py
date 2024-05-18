import pandas as pd
import ta

def calculate_technical_indicators(data):
    data['SMA'] = ta.trend.sma_indicator(data['Close'], window=20)
    data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
    data['Bollinger_Mid'] = ta.volatility.bollinger_mavg(data['Close'])
    data['Bollinger_Upper'] = ta.volatility.bollinger_hband(data['Close'])
    data['Bollinger_Lower'] = ta.volatility.bollinger_lband(data['Close'])
    data.dropna(inplace=True)
    return data

def prepare_features(data_dict):
    features_dict = {}
    for symbol, data in data_dict.items():
        features = calculate_technical_indicators(data)
        features_dict[symbol] = features
    return features_dict
