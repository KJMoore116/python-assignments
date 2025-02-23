"""Module providing functions for printing python version."""
print('finalproject.py')

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import yfinance as yf

# Function to retrieve stock data
def get_stock_data(ticker, start_date, end_date):
    """Getting stock data"""
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to analyze historical trends
def analyze_trends(stock_data):
    """Analyzing trends"""
    # Plot historical trends
    plt.figure(figsize=(10, 6))
    stock_data['Adj Close'].plot()
    plt.title('Historical Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()

# Function to implement machine learning models
def predict_stock_prices(stock_data):
    """Predicting stock prices"""
    # Prepare data for machine learning
    features = stock_data[['Open', 'High', 'Low', 'Volume']]
    target = stock_data['Adj Close']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42
        )

    # Train a Random Forest regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print("Model Accuracy:", score)

    # Predict stock prices
    predictions = model.predict(X_test)

    # Plot actual vs. predicted prices
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.index, y_test.values, label='Actual Prices')
    plt.plot(y_test.index, predictions, label='Predicted Prices')
    plt.title('Actual vs. Predicted Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    """Function to execute the main functionality of the stock analysis program"""
    # Set parameters
    ticker = 'AAPL'  # Example: Apple Inc.
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    # Retrieve stock data
    stock_data = get_stock_data(ticker, start_date, end_date)

    # Analyze historical trends
    analyze_trends(stock_data)

    # Implement machine learning models
    predict_stock_prices(stock_data)

if __name__ == "__main__":
    main()
