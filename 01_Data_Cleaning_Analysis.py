"""
Global Superstore Sales Analysis - Python Data Cleaning & Analysis
Project: Sales Performance Dashboard
Author: Your Name
Date: February 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Resolve paths relative to this script so it works from any directory
SCRIPT_DIR = Path(__file__).parent

print("=" * 80)
print("GLOBAL SUPERSTORE SALES ANALYSIS")
print("=" * 80)
print()

# ==============================================================================
# 1. DATA LOADING
# ==============================================================================
print("1. LOADING DATA...")
print("-" * 80)

CSV_FILE = SCRIPT_DIR / 'global_superstore_cleaned.csv'
if not CSV_FILE.exists():
    raise FileNotFoundError(
        f"\n  File not found: {CSV_FILE}"
        f"\n  Make sure 'global_superstore_cleaned.csv' is in the same folder as this script."
    )

df = pd.read_csv(CSV_FILE)
# Date columns are already parsed in the cleaned CSV; ensure correct dtype
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

print(f"Dataset loaded: {CSV_FILE.name}")
print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print()

# ==============================================================================
# 2. DATA EXPLORATION
# ==============================================================================
print("2. DATA EXPLORATION")
print("-" * 80)

print("\nFirst 5 rows:")
print(df.head())
print()

print("\nData Types:")
print(df.dtypes)
print()

print("\nBasic Statistics:")
print(df.describe())
print()

# ==============================================================================
# 3. DATA QUALITY CHECKS
# ==============================================================================
print("3. DATA QUALITY CHECKS")
print("-" * 80)

print("\nMissing Values:")
missing_values = df.isnull().sum()
if missing_values.sum() > 0:
    print(missing_values[missing_values > 0])
else:
    print("✓ No missing values found!")
print()

print("\nDuplicate Rows:")
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"⚠ Found {duplicates} duplicate rows")
else:
    print("✓ No duplicate rows found!")
print()

# ==============================================================================
# 4. DATA CLEANING & TRANSFORMATION
# ==============================================================================
print("4. DATA CLEANING & TRANSFORMATION")
print("-" * 80)

# Date columns already converted above
print("✓ Date columns confirmed as datetime format")

# Calculated columns already exist in the cleaned CSV; recreate to be safe
df['Order Year']    = df['Order Date'].dt.year
df['Order Month']   = df['Order Date'].dt.month
df['Order Quarter'] = df['Order Date'].dt.quarter
df['Ship Days']     = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Margin'] = (df['Profit'] / df['Sales'] * 100).round(2)
df['Revenue']       = df['Sales']
print("✓ Confirmed calculated columns: Year, Month, Quarter, Ship Days, Profit Margin")
print()

# ==============================================================================
# 5. KEY METRICS CALCULATION
# ==============================================================================
print("5. KEY BUSINESS METRICS")
print("-" * 80)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()
avg_order_value = df.groupby('Order ID')['Sales'].sum().mean()
overall_profit_margin = (total_profit / total_sales * 100)

print(f"\n📊 OVERALL PERFORMANCE:")
print(f"  Total Sales:              ${total_sales:,.2f}")
print(f"  Total Profit:             ${total_profit:,.2f}")
print(f"  Overall Profit Margin:    {overall_profit_margin:.2f}%")
print(f"  Total Orders:             {total_orders:,}")
print(f"  Total Customers:          {total_customers:,}")
print(f"  Average Order Value:      ${avg_order_value:,.2f}")
print()

# ==============================================================================
# 6. SALES BY CATEGORY
# ==============================================================================
print("6. SALES ANALYSIS BY CATEGORY")
print("-" * 80)

category_analysis = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum',
    'Order ID': 'nunique'
}).round(2)

category_analysis.columns = ['Total Sales', 'Total Profit', 'Total Quantity', 'Number of Orders']
category_analysis['Profit Margin %'] = (category_analysis['Total Profit'] / category_analysis['Total Sales'] * 100).round(2)
category_analysis = category_analysis.sort_values('Total Sales', ascending=False)

print("\nCategory Performance:")
print(category_analysis)
print()

# ==============================================================================
# 7. SALES BY REGION
# ==============================================================================
print("7. SALES ANALYSIS BY REGION")
print("-" * 80)

region_analysis = df.groupby('Region').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Order ID': 'nunique',
    'Customer ID': 'nunique'
}).round(2)

region_analysis.columns = ['Total Sales', 'Total Profit', 'Orders', 'Customers']
region_analysis['Profit Margin %'] = (region_analysis['Total Profit'] / region_analysis['Total Sales'] * 100).round(2)
region_analysis = region_analysis.sort_values('Total Sales', ascending=False)

print("\nRegion Performance:")
print(region_analysis)
print()

# ==============================================================================
# 8. SALES BY SEGMENT
# ==============================================================================
print("8. SALES ANALYSIS BY CUSTOMER SEGMENT")
print("-" * 80)

segment_analysis = df.groupby('Segment').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Customer ID': 'nunique'
}).round(2)

segment_analysis.columns = ['Total Sales', 'Total Profit', 'Unique Customers']
segment_analysis['Profit Margin %'] = (segment_analysis['Total Profit'] / segment_analysis['Total Sales'] * 100).round(2)
segment_analysis = segment_analysis.sort_values('Total Sales', ascending=False)

print("\nCustomer Segment Performance:")
print(segment_analysis)
print()

# ==============================================================================
# 9. TOP PERFORMING PRODUCTS
# ==============================================================================
print("9. TOP PERFORMING PRODUCTS")
print("-" * 80)

# Top 10 products by sales
top_products_sales = df.groupby('Product Name').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
}).round(2)
top_products_sales = top_products_sales.sort_values('Sales', ascending=False).head(10)

print("\nTop 10 Products by Sales:")
print(top_products_sales)
print()

# ==============================================================================
# 10. UNPROFITABLE PRODUCTS
# ==============================================================================
print("10. UNPROFITABLE PRODUCTS ANALYSIS")
print("-" * 80)

unprofitable_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(10)
print("\nTop 10 Loss-Making Products:")
print(unprofitable_products)
print()

# ==============================================================================
# 11. SHIPPING ANALYSIS
# ==============================================================================
print("11. SHIPPING MODE ANALYSIS")
print("-" * 80)

shipping_analysis = df.groupby('Ship Mode').agg({
    'Order ID': 'count',
    'Ship Days': 'mean',
    'Sales': 'sum',
    'Profit': 'sum'
}).round(2)

shipping_analysis.columns = ['Order Count', 'Avg Ship Days', 'Total Sales', 'Total Profit']
shipping_analysis = shipping_analysis.sort_values('Order Count', ascending=False)

print("\nShipping Mode Performance:")
print(shipping_analysis)
print()

# ==============================================================================
# 12. MONTHLY SALES TREND
# ==============================================================================
print("12. MONTHLY SALES TREND")
print("-" * 80)

monthly_sales = df.groupby(['Order Year', 'Order Month']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Order ID': 'nunique'
}).round(2)

print("\nMonthly Performance (Sample):")
print(monthly_sales.tail(12))
print()

# ==============================================================================
# 13. CUSTOMER ANALYSIS
# ==============================================================================
print("13. CUSTOMER ANALYSIS")
print("-" * 80)

# Customer Lifetime Value
customer_value = df.groupby('Customer Name').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Order ID': 'nunique'
}).round(2)

customer_value.columns = ['Total Sales', 'Total Profit', 'Number of Orders']
customer_value['Avg Order Value'] = (customer_value['Total Sales'] / customer_value['Number of Orders']).round(2)
customer_value = customer_value.sort_values('Total Sales', ascending=False).head(10)

print("\nTop 10 Customers by Sales:")
print(customer_value)
print()

# ==============================================================================
# 14. SAVE CLEANED DATA
# ==============================================================================
print("14. SAVING CLEANED DATA")
print("-" * 80)

# Save cleaned dataset
df.to_csv(SCRIPT_DIR / 'global_superstore_cleaned.csv', index=False)
print("✓ Cleaned data saved to: global_superstore_cleaned.csv")

# Save summary statistics
with open(SCRIPT_DIR / 'analysis_summary.txt', 'w') as f:
    f.write("GLOBAL SUPERSTORE SALES ANALYSIS SUMMARY\n")
    f.write("=" * 80 + "\n\n")
    f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write(f"Total Sales: ${total_sales:,.2f}\n")
    f.write(f"Total Profit: ${total_profit:,.2f}\n")
    f.write(f"Profit Margin: {overall_profit_margin:.2f}%\n")
    f.write(f"Total Orders: {total_orders:,}\n")
    f.write(f"Total Customers: {total_customers:,}\n")
    f.write(f"\n\nTop Category: {category_analysis.index[0]}\n")
    f.write(f"Top Region: {region_analysis.index[0]}\n")
    f.write(f"Top Segment: {segment_analysis.index[0]}\n")

print("✓ Analysis summary saved to: analysis_summary.txt")
print()

# ==============================================================================
# 15. EXPORT DATA FOR EXCEL & POWER BI
# ==============================================================================
print("15. EXPORTING DATA FOR EXCEL & POWER BI")
print("-" * 80)

# Export summary tables
category_analysis.to_csv(SCRIPT_DIR / 'summary_category.csv')
region_analysis.to_csv(SCRIPT_DIR / 'summary_region.csv')
segment_analysis.to_csv(SCRIPT_DIR / 'summary_segment.csv')
top_products_sales.to_csv(SCRIPT_DIR / 'summary_top_products.csv')

print("✓ Summary tables exported:")
print("  - summary_category.csv")
print("  - summary_region.csv")
print("  - summary_segment.csv")
print("  - summary_top_products.csv")
print()

print("=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)
print("\n✓ All files ready for Excel and Power BI analysis")
print("\nNext Steps:")
print("1. Open 'global_superstore_cleaned.csv' in Excel for pivot table analysis")
print("2. Import 'global_superstore_cleaned.csv' into Power BI for dashboard creation")
print("3. Use the summary CSV files for quick reference tables")
