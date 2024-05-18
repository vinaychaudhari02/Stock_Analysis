from scripts.pipeline import StockAnalysisPipeline

# Parameters
api_key = 'your_api_key'
target_stock = 'AAPL'

# Initialize and run the pipeline
pipeline = StockAnalysisPipeline(api_key, target_stock)
matching_stocks = pipeline.run()
print("Matching Stocks:", matching_stocks)
