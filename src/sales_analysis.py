import pandas as pd
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# Load cleaned dataset
input_file = DATA_DIR / "clean_ecommerce_sales.csv"
df = pd.read_csv(input_file)

print("\nE-COMMERCE SALES ANALYSIS")
print("==========================")

# 1. Overall sales
total_sales = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()

print(f"\nTotal Sales: ₹{total_sales:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")

# 2. Sales by product
product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Product:")
print(product_sales)

# 3. Sales by region
region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Region:")
print(region_sales)

# 4. Sales by payment method
payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Payment Method:")
print(payment_sales)

# 5. Top-selling product
top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

print(f"\nTop-Selling Product: {top_product}")
print(f"Top Product Sales: ₹{top_product_sales:,.2f}")