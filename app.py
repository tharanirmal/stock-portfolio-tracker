"""FastAPI application for the Stock Portfolio Tracker.

Now uses SQLAlchemy + SQLite for persistent storage.
Full CRUD: Create, Read, Update, Delete.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.models import Stock
from src.database import SessionLocal

app = FastAPI()


# -----------------------------
# Pydantic models
# -----------------------------
class StockRequest(BaseModel):
    ticker: str
    shares: int


class UpdateStockRequest(BaseModel):
    shares: int


# -----------------------------
# POST -> Add stock
# -----------------------------
@app.post("/stocks")
def add_stock_endpoint(stock: StockRequest):
    """Add shares of a stock to the portfolio."""
    db = SessionLocal()
    new_stock = Stock(
        ticker=stock.ticker.upper(),
        shares=stock.shares
    )
    db.add(new_stock)
    db.commit()
    db.close()
    return {
        "message": f"Added {stock.shares} shares of {stock.ticker.upper()}"
    }


# -----------------------------
# GET -> View portfolio
# -----------------------------
@app.get("/stocks")
def get_stocks():
    """Return the current portfolio."""
    db = SessionLocal()
    stocks = db.query(Stock).all()
    result = [
        {"ticker": s.ticker, "shares": s.shares}
        for s in stocks
    ]
    db.close()
    return {"portfolio": result}


# -----------------------------
# PUT -> Update shares
# -----------------------------
@app.put("/stocks/{ticker}")
def update_stock(ticker: str, data: UpdateStockRequest):
    """Update the share count for an existing stock."""
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.ticker == ticker.upper()).first()
    if not stock:
        db.close()
        return {"error": f"{ticker.upper()} not found in portfolio"}
    stock.shares = data.shares
    db.commit()
    db.close()
    return {
        "message": f"Updated {ticker.upper()} to {data.shares} shares"
    }


# -----------------------------
# DELETE -> Remove stock
# -----------------------------
@app.delete("/stocks/{ticker}")
def delete_stock(ticker: str):
    """Remove a stock from the portfolio."""
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.ticker == ticker.upper()).first()
    if stock:
        db.delete(stock)
        db.commit()
    db.close()
    return {
        "message": f"Removed {ticker.upper()} from portfolio"
    }
