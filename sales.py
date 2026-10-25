import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# Show first 5 rows
print(data.head())

# Data cleaning
data.dropna(inplace=True)

# Total Sales
total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by Category
category_sales = data.groupby("Category")["Sales"].sum()
print(category_sales)

# Plot bar chart
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Monthly Sales Trend
data["Date"] = pd.to_datetime(data["Date"])
monthly_sales = data.groupby(data["Date"].dt.month)["Sales"].sum()

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
# import os
# print(os.listdir())
