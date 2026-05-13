# Stock Portfolio Tracker

A CLI tool that tracks your stock portfolio — add stocks, remove them, view your holdings, and fetch real-time prices.

## Tech Stack
- Python 3
- yfinance (Yahoo Finance API)
- pandas
- JSON file storage

## Project Structure
```
stock-portfolio-tracker/
├── src/
│   ├── main.py          # Entry point — menu loop
│   └── portfolio.py     # Portfolio management functions
├── config/
│   └── settings.py      # Configuration constants
├── utils/
│   └── helpers.py       # File I/O and API utilities
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python -m src.main
```

## Features
- Add stocks with share count
- Remove stocks from portfolio
- View all holdings
- Portfolio saved to JSON (persists between sessions)
- Real-time stock price fetching via Yahoo Finance

## Example Output
```
=== Stock Portfolio Tracker ===
1. Add stock
2. Remove stock
3. View portfolio
4. Exit
Choose an option (1-4): 3

--- Your Portfolio ---
  AAPL: 10 shares
  RELIANCE.NS: 5 shares
---------------------
```

## Status
🚧 In progress — Phase 1 project for interview prep.
