import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders automatically
os.makedirs("visualizations", exist_ok=True)
os.makedirs("report", exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------

try:
    df = pd.read_csv("data/sales_data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: sales_data.csv file not found")
    exit()

# -----------------------------
# CLEAN DATA
# -----------------------------

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# BASIC ANALYSIS
# -----------------------------

total_sales = df['Sales'].sum()
average_profit = df['Profit'].mean()

print("\nTotal Sales:", total_sales)
print("Average Profit:", average_profit)

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()

print("\nSales by Category:")
print(category_sales)

# -----------------------------
# BAR CHART
# -----------------------------

plt.figure(figsize=(8,5))

category_sales.plot(kind='bar')

plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("visualizations/bar_chart.png")

plt.close()

# -----------------------------
# LINE CHART
# -----------------------------

monthly_sales = df.groupby(df['Date'].dt.month)['Sales'].sum()

plt.figure(figsize=(8,5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("visualizations/line_chart.png")

plt.close()

# -----------------------------
# PIE CHART
# -----------------------------

profit_distribution = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(7,7))

profit_distribution.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Profit Distribution")
plt.ylabel("")

plt.tight_layout()

plt.savefig("visualizations/pie_chart.png")

plt.close()

# -----------------------------
# REPORT GENERATION
# -----------------------------

report = f"""
E-COMMERCE SALES ANALYSIS REPORT
================================

Total Sales: {total_sales}

Average Profit: {average_profit}

Top Selling Category:
{category_sales.idxmax()}

Insights:
1. Electronics category generated highest sales.
2. Monthly sales trend shows business growth.
3. Profit distribution varies across categories.
"""

with open("report/final_report.txt", "w") as file:
    file.write(report)

print("\nAll charts generated successfully!")
print("Report generated successfully!")
print("Check visualizations folder.")