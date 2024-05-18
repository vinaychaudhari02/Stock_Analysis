import requests
import pandas as pd

import requests
from requests.exceptions import JSONDecodeError

def fetch_symbols(api_key, region):
    url = f"https://your-api-url.com?api_key={api_key}&region={region}"
    response = requests.get(url)

    try:
        data = response.json()
    except JSONDecodeError:
        print(f"Failed to decode JSON. Response was: {response.text}")
        raise

    return data

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
