# POWER BI DASHBOARD CREATION GUIDE
## Global Superstore Sales Analysis

---

## TABLE OF CONTENTS
1. Data Import & Setup
2. Data Model Configuration
3. DAX Measures to Create
4. Visualizations to Build
5. Dashboard Layout
6. Interactive Features

---

## 1. DATA IMPORT & SETUP

### Step 1: Import Data
1. Open Power BI Desktop
2. Click "Get Data" > "Excel"
3. Select "Global_Superstore_Analysis.xlsx"
4. Check the "Raw Data" sheet
5. Click "Transform Data" to open Power Query Editor

### Step 2: Data Type Verification
In Power Query Editor, verify these data types:
- Order Date: Date
- Ship Date: Date
- Sales: Decimal Number
- Profit: Decimal Number
- Quantity: Whole Number
- Discount: Decimal Number

### Step 3: Create Date Table (IMPORTANT!)
```DAX
DateTable = 
ADDCOLUMNS(
    CALENDAR(DATE(2014,1,1), DATE(2017,12,31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", FORMAT([Date], "MMMM"),
    "MonthNum", MONTH([Date]),
    "YearMonth", FORMAT([Date], "YYYY-MM")
)
```

### Step 4: Create Relationships
- DateTable[Date] → Raw Data[Order Date] (Many to One)
- Mark DateTable as Date Table: Right-click DateTable > Mark as Date Table

---

## 2. DATA MODEL CONFIGURATION

### Suggested Table Structure
Your model should have:
- **Raw Data** (Fact Table)
- **DateTable** (Date Dimension)

Optional: Create additional dimension tables:
- **Products** (Product ID, Product Name, Category, Sub-Category)
- **Customers** (Customer ID, Customer Name, Segment)
- **Geography** (Country, City, State, Region)

---

## 3. DAX MEASURES TO CREATE

Create a new table called "Measures" to organize all calculations:

### Core Metrics
```DAX
Total Sales = SUM('Raw Data'[Sales])

Total Profit = SUM('Raw Data'[Profit])

Total Orders = DISTINCTCOUNT('Raw Data'[Order ID])

Total Customers = DISTINCTCOUNT('Raw Data'[Customer ID])

Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

Total Quantity = SUM('Raw Data'[Quantity])
```

### Time Intelligence Measures
```DAX
Sales LY = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DateTable[Date])
)

Sales Growth % = 
DIVIDE(
    [Total Sales] - [Sales LY],
    [Sales LY],
    0
)

Profit LY = 
CALCULATE(
    [Total Profit],
    SAMEPERIODLASTYEAR(DateTable[Date])
)

YTD Sales = 
TOTALYTD([Total Sales], DateTable[Date])

MTD Sales = 
TOTALMTD([Total Sales], DateTable[Date])
```

### Advanced Measures
```DAX
Avg Discount = AVERAGE('Raw Data'[Discount])

Avg Ship Days = AVERAGE('Raw Data'[Ship Days])

Profitable Orders = 
CALCULATE(
    [Total Orders],
    'Raw Data'[Profit] > 0
)

Profitable Orders % = 
DIVIDE([Profitable Orders], [Total Orders], 0)

Sales per Customer = 
DIVIDE([Total Sales], [Total Customers], 0)
```

### Conditional Formatting Measures
```DAX
Profit Color = 
IF([Total Profit] >= 0, "Green", "Red")

Sales vs Target = 
VAR Target = 20000
RETURN
IF([Total Sales] >= Target, "Above", "Below")
```

---

## 4. VISUALIZATIONS TO BUILD

### PAGE 1: EXECUTIVE OVERVIEW

#### KPI Cards (Top Row)
1. **Total Sales Card**
   - Visual: Card
   - Field: [Total Sales]
   - Format: Currency, $#,##0

2. **Total Profit Card**
   - Visual: Card
   - Field: [Total Profit]
   - Format: Currency

3. **Profit Margin Card**
   - Visual: Card
   - Field: [Profit Margin %]
   - Format: Percentage

4. **Total Orders Card**
   - Visual: Card
   - Field: [Total Orders]
   - Format: Number

#### Sales Trend Line Chart
- Visual: Line Chart
- Axis: DateTable[YearMonth]
- Values: [Total Sales], [Total Profit]
- Legend: Metric names
- Add trend line
- Enable data labels

#### Sales by Category (Pie/Donut Chart)
- Visual: Donut Chart
- Legend: Raw Data[Category]
- Values: [Total Sales]
- Show data labels with percentages

#### Sales by Region (Map)
- Visual: Map
- Location: Raw Data[Country] or [State]
- Bubble size: [Total Sales]
- Bubble color: [Profit Margin %]

#### Top 10 Products (Bar Chart)
- Visual: Clustered Bar Chart
- Axis: Raw Data[Product Name]
- Values: [Total Sales]
- Sort by: [Total Sales] descending
- Add data labels
- Top N filter: 10

---

### PAGE 2: CATEGORY & PRODUCT ANALYSIS

#### Matrix: Category Performance
- Visual: Matrix
- Rows: Raw Data[Category], Raw Data[Sub-Category]
- Values: [Total Sales], [Total Profit], [Profit Margin %]
- Conditional formatting on Profit (red for negative, green for positive)

#### Sales by Sub-Category (Stacked Bar)
- Visual: Stacked Bar Chart
- Axis: Raw Data[Sub-Category]
- Values: [Total Sales]
- Legend: Raw Data[Category]

#### Profitability Scatter Plot
- Visual: Scatter Chart
- X-axis: [Total Sales]
- Y-axis: [Total Profit]
- Details: Raw Data[Product Name]
- Size: [Total Quantity]

#### Product Performance Table
- Visual: Table
- Columns: Product Name, Category, [Total Sales], [Total Profit], [Profit Margin %]
- Conditional formatting on metrics

---

### PAGE 3: CUSTOMER & REGIONAL ANALYSIS

#### Sales by Segment (Column Chart)
- Visual: Clustered Column Chart
- Axis: Raw Data[Segment]
- Values: [Total Sales], [Total Profit]

#### Regional Performance Matrix
- Visual: Matrix
- Rows: Raw Data[Region], Raw Data[Country]
- Values: [Total Sales], [Total Profit], [Total Orders], [Total Customers]

#### Customer Segmentation (Treemap)
- Visual: Treemap
- Group: Raw Data[Segment]
- Values: [Total Sales]

#### Shipping Analysis
- Visual: Stacked Column Chart
- Axis: Raw Data[Ship Mode]
- Values: [Total Orders]
- Add [Avg Ship Days] as line chart on secondary axis

---

### PAGE 4: TIME ANALYSIS

#### Year-over-Year Comparison
- Visual: Clustered Column Chart
- Axis: DateTable[Year]
- Values: [Total Sales], [Sales LY]

#### Monthly Sales Waterfall
- Visual: Waterfall Chart
- Category: DateTable[Month]
- Y-axis: [Total Sales]

#### Sales Calendar Heatmap (Optional)
- Visual: Matrix
- Rows: DateTable[Month]
- Columns: DateTable[Year]
- Values: [Total Sales]
- Conditional formatting: Color scale

#### Quarterly Performance
- Visual: Line and Clustered Column Chart
- Axis: DateTable[Quarter], DateTable[Year]
- Column values: [Total Sales]
- Line values: [Profit Margin %]

---

## 5. DASHBOARD LAYOUT

### Recommended Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  GLOBAL SUPERSTORE SALES DASHBOARD           Last Updated   │
├─────────────────────────────────────────────────────────────┤
│  [  Sales  ] [  Profit  ] [ Margin % ] [  Orders  ]         │
│    $16.9K      $260.82      1.54%         30               │
├──────────────────────────────┬──────────────────────────────┤
│                              │                              │
│   Sales Trend Over Time      │   Sales by Category         │
│   (Line Chart)               │   (Donut Chart)             │
│                              │                              │
├──────────────────────────────┼──────────────────────────────┤
│                              │                              │
│   Sales by Region            │   Top 10 Products           │
│   (Map)                      │   (Bar Chart)               │
│                              │                              │
└──────────────────────────────┴──────────────────────────────┘
```

### Design Best Practices
- Use consistent color scheme (Blue for Sales, Green for Profit)
- White background with subtle grid lines
- Company logo in top-left
- Filter pane on left side
- Page navigation buttons at top

---

## 6. INTERACTIVE FEATURES

### Slicers to Add
1. **Date Range Slicer**
   - Field: DateTable[Date]
   - Style: Between
   - Position: Top or left panel

2. **Category Slicer**
   - Field: Raw Data[Category]
   - Style: Dropdown or Tile
   - Multi-select enabled

3. **Region Slicer**
   - Field: Raw Data[Region]
   - Style: Dropdown
   - Multi-select enabled

4. **Segment Slicer**
   - Field: Raw Data[Segment]
   - Style: Tile
   - Multi-select enabled

### Drill-Through Configuration
1. Create drill-through page for Product Details
   - Drag Product Name to drill-through filters
   - Add detailed product metrics
   - Add back button

### Sync Slicers
- Sync slicers across all pages for consistent filtering
- Edit interactions: Turn off filtering where needed

### Bookmarks
1. **Reset Filters** - Clear all filters
2. **High Performers** - Show only profitable products
3. **Regional Focus** - Pre-filtered views by region

### Buttons
- Reset filters button
- Navigation buttons between pages
- Export to PDF button

---

## 7. FORMATTING TIPS

### Theme
Use built-in theme or customize:
- Primary color: #4472C4 (Blue)
- Secondary color: #70AD47 (Green)
- Background: White or #F2F2F2
- Font: Segoe UI or similar

### Number Formatting
- Sales: $#,##0
- Profit: $#,##0 (red if negative)
- Percentages: 0.00%
- Quantities: #,##0

### Conditional Formatting
- Profit: Red for negative, Green for positive
- Profit Margin: Color scale (red < 0% < green)
- Sales Growth: Icons (up/down arrows)

---

## 8. PUBLISHING & SHARING

### Publish to Power BI Service
1. Click "Publish" in Power BI Desktop
2. Select workspace
3. Set up data refresh schedule

### Create Dashboard
1. Pin key visuals from report
2. Arrange tiles
3. Add text boxes for context

### Share Options
- Share link with specific users
- Embed in SharePoint/website
- Export to PowerPoint
- Create mobile layout

---

## 9. PERFORMANCE OPTIMIZATION

### Best Practices
- Use DAX measures instead of calculated columns where possible
- Avoid relationships on calculated columns
- Use SELECTEDVALUE instead of VALUES when expecting single value
- Remove unnecessary columns from model
- Use aggregations for large datasets

---

## 10. TROUBLESHOOTING

### Common Issues

**Issue**: Relationships not working
**Solution**: Check data types match, remove blanks, ensure one-to-many cardinality

**Issue**: Measures showing wrong totals
**Solution**: Use CALCULATE or iterators (SUMX, AVERAGEX)

**Issue**: Slow performance
**Solution**: Optimize DAX, reduce visual count, use aggregations

**Issue**: Date table not recognized
**Solution**: Mark table as Date Table, ensure continuous date range

---

## ADDITIONAL RESOURCES

- Power BI Documentation: https://docs.microsoft.com/power-bi
- DAX Guide: https://dax.guide
- SQLBI (Advanced DAX): https://www.sqlbi.com
- Power BI Community: https://community.powerbi.com

---

## PROJECT COMPLETION CHECKLIST

- [ ] Data imported correctly
- [ ] Date table created and marked
- [ ] All DAX measures created
- [ ] 4 dashboard pages built
- [ ] Slicers added and synced
- [ ] Conditional formatting applied
- [ ] Drill-through configured
- [ ] Bookmarks created
- [ ] Theme applied consistently
- [ ] Report published to service
- [ ] Documentation created

---

**Created by:** [Your Name]
**Date:** February 2026
**Version:** 1.0
