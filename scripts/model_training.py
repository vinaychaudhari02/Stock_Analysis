import numpy as np

def calculate_matching_percentage(target_features, other_features):
    indicators = ['SMA', 'RSI', 'Bollinger_Mid', 'Bollinger_Upper', 'Bollinger_Lower']
    match_count = 0

    for indicator in indicators:
        target_indicator = target_features[indicator].values
        other_indicator = other_features[indicator].values

        min_length = min(len(target_indicator), len(other_indicator))
        target_indicator = target_indicator[:min_length]
        other_indicator = other_indicator[:min_length]

        # Calculate percentage match for each indicator
        match_count += np.sum(np.isclose(target_indicator, other_indicator, rtol=0.01))

    total_points = min_length * len(indicators)
    match_percentage = match_count / total_points
    return match_percentage

def find_matching_stocks(target_features, all_features, threshold=0.95):
    matching_stocks = {}
    for symbol, features in all_features.items():
        match_percentage = calculate_matching_percentage(target_features, features)
        if match_percentage >= threshold:
            matching_stocks[symbol] = match_percentage
    return matching_stocks
