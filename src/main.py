"""Main entry point for the Stock Portfolio Tracker."""

from src.portfolio import add_stock, remove_stock, view_portfolio
from utils.helpers import save_portfolio, load_portfolio
from config.settings import PORTFOLIO_FILE


def show_menu():
    """Display the main menu options."""
    print("\n=== Stock Portfolio Tracker ===")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio")
    print("4. Exit")


def main():
    """Run the Stock Portfolio Tracker application."""
    portfolio = load_portfolio(PORTFOLIO_FILE)
    print("Portfolio loaded successfully.")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            ticker = input("Enter ticker symbol: ").upper()
            try:
                shares = int(input("Enter number of shares: "))
                if shares <= 0:
                    print("Shares must be a positive number.")
                    continue
                portfolio = add_stock(portfolio, ticker, shares)
                save_portfolio(portfolio, PORTFOLIO_FILE)
                print(f"Added {shares} shares of {ticker}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        elif choice == "2":
            ticker = input("Enter ticker symbol to remove: ").upper()
            portfolio = remove_stock(portfolio, ticker)
            save_portfolio(portfolio, PORTFOLIO_FILE)

        elif choice == "3":
            view_portfolio(portfolio)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
