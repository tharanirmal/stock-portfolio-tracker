"""Utility functions for the Stock Portfolio Tracker."""

import json

import yfinance as yf


def save_portfolio(portfolio, filepath):
    """Save the portfolio dictionary to a JSON file.

    Args:
        portfolio (dict): Portfolio data with ticker symbols as keys
            and share counts as values.
        filepath (str): Path to the JSON file.
    """
    with open(filepath, "w") as f:
        json.dump(portfolio, f, indent=4)


def load_portfolio(filepath):
    """Load the portfolio dictionary from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        dict: Portfolio data, or an empty dict if the file
        doesn't exist or is corrupted.
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: Portfolio file is corrupted. Starting fresh.")
        return {}


def fetch_stock_price(ticker):
    """Fetch the current stock price for a given ticker.

    Args:
        ticker (str): Stock ticker symbol (e.g., "AAPL", "RELIANCE.NS").

    Returns:
        float or None: Current stock price, or None if an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            return None
        price = data["Close"].iloc[-1]
        return float(price)
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None
