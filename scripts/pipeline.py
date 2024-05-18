from scripts.data_collection import fetch_symbols, fetch_stock_data, fetch_all_stocks_data
from scripts.feature_engineering import calculate_technical_indicators, prepare_features
from scripts.model_training import find_matching_stocks

class StockAnalysisPipeline:
    def __init__(self, api_key, target_stock, region='US', threshold=0.95):
        self.api_key = api_key
        self.target_stock = target_stock
        self.region = region
        self.threshold = threshold

    def run(self):
        # Fetch stock symbols
        symbols = fetch_symbols(self.api_key, self.region)
        
        # Fetch data for target stock and all other stocks
        target_data = fetch_stock_data(self.target_stock, self.api_key)
        all_data = fetch_all_stocks_data(symbols, self.api_key)
        
        # Calculate technical indicators
        target_features = calculate_technical_indicators(target_data)
        all_features = prepare_features(all_data)
        
        # Find matching stocks
        matching_stocks = find_matching_stocks(target_features, all_features, self.threshold)
        
        return matching_stocks
