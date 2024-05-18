import requests
import pandas as pd

def fetch_symbols(api_key, region='US'):
    url = f'https://cloud.iexapis.com/stable/ref-data/region/{region}/symbols?token={api_key}'
    response = requests.get(url)
    data = response.json()
    symbols = [item['symbol'] for item in data]
    return symbols

def fetch_stock_data(symbol, api_key):
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/chart/max?token={api_key}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def fetch_all_stocks_data(symbols, api_key):
    all_data = {}
    for symbol in symbols:
        data = fetch_stock_data(symbol, api_key)
        all_data[symbol] = data
    return all_data
