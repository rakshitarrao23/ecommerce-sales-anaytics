import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

# Create reports folder if needed
REPORT_DIR.mkdir(exist_ok=True)

# Load cleaned dataset
input_file = DATA_DIR / "clean_ecommerce_sales.csv"
df = pd.read_csv(input_file)

# -------------------------------
# 1. Sales by Product
# -------------------------------

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(REPORT_DIR / "sales_by_product.png")
plt.show()

# -------------------------------
# 2. Sales by Region
# -------------------------------

region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(REPORT_DIR / "sales_by_region.png")
plt.show()

# -------------------------------
# 3. Sales by Payment Method
# -------------------------------

payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
payment_sales.plot(kind="bar")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(REPORT_DIR / "sales_by_payment_method.png")
plt.show()

print("\nVISUALIZATION COMPLETED")
print("=======================")
print("Charts saved in the reports folder.")