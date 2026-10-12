import sqlite3
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# Database file
DB_FILE = BASE_DIR / "ecommerce_sales.db"

# Connect to SQLite database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    Order_ID TEXT,
    Customer_ID TEXT,
    Product TEXT,
    Category TEXT,
    Quantity INTEGER,
    Unit_Price REAL,
    Region TEXT,
    Payment_Method TEXT,
    Total_Sales REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
print(f"Database location: {DB_FILE}")