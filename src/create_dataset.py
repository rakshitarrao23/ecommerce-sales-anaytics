import pandas as pd
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# Create sample e-commerce sales data
data = {
    "Order_ID": [
        "ORD001", "ORD002", "ORD003", "ORD004", "ORD005",
        "ORD006", "ORD007", "ORD008", "ORD009", "ORD010"
    ],
    "Customer_ID": [
        "C001", "C002", "C003", "C004", "C005",
        "C006", "C007", "C008", "C009", "C010"
    ],
    "Product": [
        "Laptop", "Mobile Phone", "Headphones", "Keyboard", "Mouse",
        "Smart Watch", "Tablet", "Laptop", "Mobile Phone", "Headphones"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories", "Accessories",
        "Accessories", "Wearables", "Electronics", "Electronics",
        "Electronics", "Accessories"
    ],
    "Quantity": [1, 2, 3, 2, 4, 1, 2, 1, 1, 2],
    "Unit_Price": [55000, 25000, 2000, 1500, 800, 5000, 30000, 55000, 25000, 2000],
    "Region": [
        "South", "South", "West", "North", "South",
        "East", "West", "South", "North", "East"
    ],
    "Payment_Method": [
        "UPI", "Credit Card", "UPI", "Debit Card", "Cash",
        "UPI", "Credit Card", "UPI", "Debit Card", "Cash"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save dataset
output_file = DATA_DIR / "raw_ecommerce_sales.csv"
df.to_csv(output_file, index=False)

print("E-Commerce dataset created successfully!")
print(f"Dataset saved at: {output_file}")
print(f"Number of records: {len(df)}")
print("\nFirst 5 records:")
print(df.head())