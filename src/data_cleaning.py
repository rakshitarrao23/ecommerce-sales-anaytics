import pandas as pd
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# Input and output files
input_file = DATA_DIR / "raw_ecommerce_sales.csv"
output_file = DATA_DIR / "clean_ecommerce_sales.csv"

# Load raw data
df = pd.read_csv(input_file)

print("RAW DATA")
print("--------")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Convert numeric columns to appropriate data types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# Recalculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned data
df.to_csv(output_file, index=False)

print("\nDATA CLEANING COMPLETED")
print("-----------------------")
print(f"Clean rows: {len(df)}")
print(f"Clean file: {output_file}")

print("\nCleaned data:")
print(df.head())