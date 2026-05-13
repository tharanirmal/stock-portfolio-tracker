"""Database setup for the Stock Portfolio Tracker.

Creates SQLite engine, initializes tables, and provides session factory.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

# Create engine — SQLite database stored in stocks.db file
engine = create_engine("sqlite:///stocks.db")

# Create all tables defined by Base (Stock model)
Base.metadata.create_all(bind=engine)

# Session factory — use this to interact with the database
SessionLocal = sessionmaker(bind=engine)
