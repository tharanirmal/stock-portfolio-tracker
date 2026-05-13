"""Portfolio management functions for the Stock Portfolio Tracker."""


def add_stock(portfolio, ticker, shares):
    """Add shares of a stock to the portfolio.

    If the ticker already exists, adds to the existing share count.
    If it's new, creates a new entry.

    Args:
        portfolio (dict): Current portfolio data.
        ticker (str): Stock ticker symbol (e.g., "AAPL").
        shares (int): Number of shares to add.

    Returns:
        dict: Updated portfolio.
    """
    ticker = ticker.upper()
    portfolio[ticker] = portfolio.get(ticker, 0) + shares
    return portfolio


def remove_stock(portfolio, ticker):
    """Remove a stock entirely from the portfolio.

    Args:
        portfolio (dict): Current portfolio data.
        ticker (str): Stock ticker symbol to remove.

    Returns:
        dict: Updated portfolio.
    """
    ticker = ticker.upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found in portfolio.")
    return portfolio


def view_portfolio(portfolio):
    """Display all stocks and share counts in the portfolio.

    Args:
        portfolio (dict): Current portfolio data.
    """
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\n--- Your Portfolio ---")
    for ticker, shares in portfolio.items():
        print(f"  {ticker}: {shares} shares")
    print("---------------------\n")
