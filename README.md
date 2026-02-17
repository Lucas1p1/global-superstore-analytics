# Global Superstore Sales Analysis
## Complete Data Analytics Portfolio Project

![Project Status](https://img.shields.io/badge/Status-Complete-success)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Excel%20%7C%20Power%20BI-blue)
![Skills](https://img.shields.io/badge/Skills-Data%20Analysis%20%7C%20Visualization%20%7C%20Dashboard-orange)

---

## 📋 Project Overview

This is a comprehensive data analytics project analyzing sales performance for Global Superstore, a fictional global retail company. The project demonstrates end-to-end data analysis skills including data cleaning, statistical analysis, Excel modeling, and dashboard creation.

**Business Context:** Global Superstore operates globally across multiple regions, selling products in three main categories: Furniture, Office Supplies, and Technology. This analysis helps identify sales trends, profitable products, regional performance, and areas for improvement.

---

## 🎯 Business Questions Answered

1. **What is our overall sales and profit performance?**
2. **Which product categories and sub-categories are most profitable?**
3. **Which regions generate the most revenue?**
4. **What products should we discontinue due to losses?**
5. **Which customer segments are most valuable?**
6. **How do shipping methods impact profitability?**
7. **What are our monthly and yearly sales trends?**
8. **Who are our top customers?**

---

## 🛠️ Tools & Technologies

### Python (Pandas, NumPy, Matplotlib, Seaborn)
- Data cleaning and transformation
- Exploratory data analysis
- Statistical calculations
- Data export preparation

### Microsoft Excel
- Advanced formulas (SUMIF, COUNTIF, INDEX-MATCH)
- Pivot tables
- Conditional formatting
- Data validation
- Dashboard creation

### Power BI
- Interactive dashboards
- DAX measures
- Data modeling
- Visual analytics
- Time intelligence

---

## 📁 Project Structure

```
Global-Superstore-Analysis/
│
├── data/
│   ├── global_superstore_sample.csv          # Raw dataset
│   ├── global_superstore_cleaned.csv         # Cleaned data
│   ├── summary_category.csv                  # Category analysis
│   ├── summary_region.csv                    # Regional analysis
│   ├── summary_segment.csv                   # Segment analysis
│   └── summary_top_products.csv              # Product performance
│
├── python/
│   └── 01_Data_Cleaning_Analysis.py          # Python analysis script
│
├── excel/
│   ├── 02_Create_Excel_Workbook.py           # Excel creation script
│   └── Global_Superstore_Analysis.xlsx       # Excel workbook
│
├── powerbi/
│   └── PowerBI_Dashboard_Guide.md            # Power BI instructions
│
├── outputs/
│   └── analysis_summary.txt                  # Analysis summary
│
└── README.md                                 # This file
```

---

## 📊 Key Findings

### Overall Performance
- **Total Sales:** $16,882.89
- **Total Profit:** $260.82
- **Profit Margin:** 1.54%
- **Total Orders:** 30
- **Average Order Value:** $562.76

### Category Performance
| Category | Sales | Profit | Margin |
|----------|-------|--------|---------|
| Technology | $9,249.32 | $2,123.76 | 22.96% |
| Office Supplies | $1,426.06 | $409.20 | 28.69% |
| Furniture | $6,207.51 | -$2,272.13 | -36.60% |

**Key Insight:** Furniture category is highly unprofitable despite significant sales volume.

### Regional Performance
| Region | Sales | Profit | Margin |
|--------|-------|--------|---------|
| South | $5,606.82 | $182.28 | 3.25% |
| Asia | $4,167.73 | -$1,418.31 | -34.03% |
| LATAM | $2,323.47 | $649.47 | 27.95% |

**Key Insight:** Asia region requires immediate attention - negative profitability.

### Customer Segments
| Segment | Sales | Profit | Margin |
|---------|-------|--------|---------|
| Consumer | $12,157.52 | -$989.09 | -8.14% |
| Corporate | $2,491.79 | $617.94 | 24.80% |
| Home Office | $2,233.59 | $631.98 | 28.29% |

**Key Insight:** Focus on Corporate and Home Office segments for profitability.

---

## 🔍 Methodology

### 1. Data Collection
- Dataset: Global Superstore (sample of 50 transactions)
- Source: Realistic sample based on common retail data structure
- Time Period: 2014-2016
- Geographic Scope: Global (9 regions)

### 2. Data Cleaning (Python)
```python
# Key cleaning steps:
✓ Converted date columns to datetime format
✓ Checked for missing values (none found)
✓ Checked for duplicates (none found)
✓ Created calculated columns:
  - Order Year, Month, Quarter
  - Ship Days
  - Profit Margin
```

### 3. Exploratory Data Analysis
- Calculated key business metrics
- Analyzed sales by category, region, and segment
- Identified top and bottom performing products
- Examined shipping method impact
- Studied temporal trends

### 4. Excel Analysis
Created 6-sheet workbook with:
- Raw data with filters and formatting
- Executive summary with dynamic formulas
- Sales analysis with conditional formatting
- Profitability analysis
- Advanced formula examples
- User instructions

### 5. Power BI Dashboard (Design)
Comprehensive guide for creating:
- 4-page interactive dashboard
- 15+ DAX measures
- Time intelligence calculations
- Geographic visualizations
- Drill-through capabilities

---

## 💡 Key Insights & Recommendations

### 1. Product Strategy
**Finding:** Furniture category showing -36.60% profit margin
**Recommendation:** 
- Discontinue unprofitable furniture items (tables especially)
- Renegotiate supplier contracts
- Increase prices or reduce discounts on furniture

### 2. Geographic Expansion
**Finding:** Asia region has -34.03% profit margin
**Recommendation:**
- Investigate root causes (shipping costs, pricing, competition)
- Consider restructuring operations in Asia
- Focus expansion on LATAM (27.95% margin)

### 3. Customer Focus
**Finding:** Corporate and Home Office segments most profitable
**Recommendation:**
- Increase marketing to B2B customers
- Create specialized offerings for business customers
- Review consumer segment pricing strategy

### 4. Shipping Optimization
**Finding:** Standard Class most used but Second Class more profitable
**Recommendation:**
- Incentivize Second Class shipping
- Review Standard Class cost structure
- Negotiate better rates with carriers

---

## 📈 Visualizations

### Excel Dashboard Features
- Executive KPI cards with formulas
- Category performance tables with conditional formatting
- Regional sales breakdown
- Automated calculations using SUMIF, COUNTIF, INDEX-MATCH
- Professional formatting with color coding

### Power BI Dashboard (Proposed)
**Page 1: Executive Overview**
- KPI cards (Sales, Profit, Margin, Orders)
- Sales trend line chart
- Category donut chart
- Geographic map
- Top 10 products bar chart

**Page 2: Category Analysis**
- Category/sub-category matrix
- Profitability scatter plot
- Product performance table

**Page 3: Regional Analysis**
- Regional performance matrix
- Customer segmentation treemap
- Shipping analysis

**Page 4: Time Analysis**
- Year-over-year comparison
- Monthly waterfall chart
- Quarterly trends

---

## 🚀 How to Use This Project

### For Recruiters & Hiring Managers
1. Review the README for project overview
2. Check `analysis_summary.txt` for quick insights
3. Open `Global_Superstore_Analysis.xlsx` to see Excel skills
4. Review `PowerBI_Dashboard_Guide.md` for BI capabilities
5. Examine Python code in `01_Data_Cleaning_Analysis.py`

### For Reproducing the Analysis
1. **Python Analysis:**
   ```bash
   python 01_Data_Cleaning_Analysis.py
   ```
   
2. **Excel Workbook:**
   ```bash
   python 02_Create_Excel_Workbook.py
   ```
   Then open `Global_Superstore_Analysis.xlsx`

3. **Power BI Dashboard:**
   - Open Power BI Desktop
   - Import `global_superstore_cleaned.csv`
   - Follow instructions in `PowerBI_Dashboard_Guide.md`

---

## 🎓 Skills Demonstrated

### Technical Skills
- ✅ Python programming (Pandas, NumPy)
- ✅ Data cleaning and transformation
- ✅ Statistical analysis
- ✅ Excel advanced formulas
- ✅ Excel pivot tables
- ✅ Conditional formatting
- ✅ Data visualization
- ✅ DAX (Power BI)
- ✅ Dashboard design
- ✅ SQL concepts (GROUP BY, aggregations)

### Analytical Skills
- ✅ Business problem identification
- ✅ Root cause analysis
- ✅ Trend analysis
- ✅ Profitability analysis
- ✅ Customer segmentation
- ✅ Product performance analysis
- ✅ Geographic analysis

### Communication Skills
- ✅ Data storytelling
- ✅ Executive reporting
- ✅ Documentation
- ✅ Insight generation
- ✅ Recommendation development

---

## 📝 Future Enhancements

- [ ] Add predictive modeling (sales forecasting)
- [ ] Implement customer lifetime value analysis
- [ ] Create RFM segmentation
- [ ] Add market basket analysis
- [ ] Build automated reporting pipeline
- [ ] Integrate with SQL database
- [ ] Add real-time dashboard refresh
- [ ] Implement A/B testing framework

---

## 📚 Additional Resources

### Data Sources
- This project uses sample data representative of retail operations
- For real-world analysis, similar data can be obtained from:
  - Company ERP systems
  - E-commerce platforms
  - Point-of-sale systems
  - Public datasets (Kaggle, data.gov)

### Learning Resources
- **Python:** Python for Data Analysis by Wes McKinney
- **Excel:** Excel Bible by John Walkenbach
- **Power BI:** Microsoft Power BI Documentation
- **DAX:** The Definitive Guide to DAX by SQLBI

---

## 🤝 Connect With Me

- **LinkedIn:** [Your LinkedIn]
- **GitHub:** [Your GitHub]
- **Portfolio:** [Your Portfolio Website]
- **Email:** [Your Email]

---

## 📄 License

This project is for educational and portfolio purposes. Feel free to use it as a template for your own projects.

---

## 🙏 Acknowledgments

- Dataset structure inspired by common retail analytics datasets
- Dashboard design follows industry best practices
- Analysis methodology based on standard business intelligence frameworks

---

**Project Completed:** February 2026
**Author:** [Your Name]
**Version:** 1.0

---

## ⭐ Project Highlights

This project showcases a complete data analytics workflow that would be valuable in roles such as:
- Data Analyst
- Business Analyst
- Business Intelligence Analyst
- Data Scientist (entry-level)
- Analytics Consultant

The end-to-end nature of this project demonstrates the ability to:
1. Collect and clean real-world messy data
2. Perform meaningful statistical analysis
3. Create professional Excel reports
4. Design interactive dashboards
5. Communicate insights to stakeholders
6. Make data-driven recommendations

Perfect for demonstrating practical skills to potential employers! 🚀
