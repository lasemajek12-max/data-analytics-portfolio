# 📊 Data Analytics Portfolio — Toluwalase Majekodunmi

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![BigQuery](https://img.shields.io/badge/Google%20BigQuery-4285F4?style=for-the-badge&logo=googlebigquery&logoColor=white)

> **Data Analyst | Business Intelligence | Analytics Engineer**  
> Amsterdam, Netherlands · [LinkedIn](https://www.linkedin.com/in/tolu-majek124/) · lasemajek12@gmail.com

---

## 👋 About Me

Data Analyst with 6+ years delivering measurable business impact across retail (Jumbo Supermarkten), financial services (Tixee FX), and operations — engineering Power BI dashboards, automating ETL workflows with Python and SQL, and transforming raw data into decisions that drove 8–18% performance improvements across revenue, retention, and operational efficiency.

**Certifications:** IBM Data Science Professional Certificate · Microsoft Excel & Power BI (Macquarie University)  
**Cloud:** Google BigQuery · AWS (Free Tier)  
**Education:** MSc International Business Management · BSc Accounting

---

## 📁 Portfolio Projects

### 1. 📈 Sales & Revenue Analytics Dashboard
**Tools:** Power BI · DAX · SQL · Excel · Power Query  
**Industry:** Financial Services — Forex Brokerage  
**Dataset:** 1,200 simulated transactions · $8.47M revenue · 2022–2023

An end-to-end sales performance dashboard analyzing revenue, profit margin, deal volume, and client segment performance across 4 regions and 8 sales reps. Features 3 report pages, 7 DAX measures, dynamic slicers synced across pages, conditional formatting on target attainment, and a transaction detail table.

**Key DAX:** `Total Revenue`, `Profit Margin %`, `Target Attainment %`, `Revenue vs Target Variance`

| | |
|---|---|
| 🔗 **Live Preview** | [View Dashboard →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-1-sales-revenue/Dashboard1_Sales_Preview.html) |
| 📋 **Build Guide** | [Step-by-step Power BI instructions →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-1-sales-revenue/Dashboard1_Sales_BuildGuide.html) |
| 📂 **Dataset** | [Download Excel data →](https://github.com/lasemajek12-max/data-analytics-portfolio/raw/main/dashboard-1-sales-revenue/Dashboard1_Sales_Revenue_Data.xlsx) |

---

### 2. 👥 HR & Workforce Analytics Dashboard
**Tools:** Power BI · DAX · Power Query · Excel  
**Industry:** Human Resources — Multi-department Corporate  
**Dataset:** 214 simulated employees · 8 departments · 2022–2024

A 3-page interactive HR dashboard covering workforce headcount, attrition analysis (11.4% rate), performance distribution, diversity metrics, salary benchmarking, and a 5-stage recruitment funnel. Features bookmark-driven interactive storytelling for executive presentation mode and cross-page slicer syncing.

**Key DAX:** `Attrition Rate %`, `Active Employees`, `Promotion Eligible`, `Offer Acceptance Rate`

| | |
|---|---|
| 🔗 **Live Preview** | [View Dashboard →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-2-hr-workforce/Dashboard2_HR_Preview.html) |
| 📋 **Build Guide** | [Step-by-step Power BI instructions →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-2-hr-workforce/Dashboard2_HR_BuildGuide.html) |
| 📂 **Dataset** | [Download Excel data →](https://github.com/lasemajek12-max/data-analytics-portfolio/raw/main/dashboard-2-hr-workforce/Dashboard2_HR_Workforce_Data.xlsx) |

---

### 3. 🛒 Retail Sales & Customer Analysis — SQL
**Tools:** SQL (PostgreSQL / BigQuery compatible)  
**Industry:** Retail — Supermarket / FMCG  
**Dataset:** Simulated 5-table relational schema (customers, products, stores, transactions, items)

10 business insight queries across a normalized retail database demonstrating advanced SQL including multi-table JOINs, CTEs, window functions (LAG, RANK, SUM OVER), date arithmetic, CASE WHEN segmentation, and cohort retention analysis. Each query addresses a real business question faced in retail analytics.

**Techniques:** CTEs · `LAG()` · `RANK()` · `SUM() OVER()` · Cohort analysis · RFM segmentation · NULLIF · Subqueries

| Query | Business Question |
|---|---|
| Monthly Revenue & Margin | How is revenue trending month-on-month? |
| RFM Customer Segmentation | How do we classify customers by spend behaviour? |
| MoM Growth with LAG() | Is the business growing or declining each month? |
| Store Revenue per sq/m | Which stores are most space-efficient? |
| Cohort Retention Analysis | Do acquired customers return to buy? |

| | |
|---|---|
| 📄 **SQL Queries** | [retail_sales_analysis.sql →](./project-3-sql-retail-analysis/retail_sales_analysis.sql) |
| 📋 **Documentation** | [README →](./project-3-sql-retail-analysis/README.md) |

---

### 4. 🐍 Forex Trading Performance — Python EDA
**Tools:** Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook  
**Industry:** Financial Services — Forex Brokerage  
**Dataset:** 1,200 simulated trades · 8 sales reps · 4 regions · 2022–2023

End-to-end exploratory data analysis notebook covering data cleaning and validation, KPI summary dashboard, monthly revenue/profit trends, sales rep performance benchmarking, product and segment breakdown, deal size vs margin correlation analysis, and regional growth trajectory. Includes 6 multi-panel visualizations and a structured findings + recommendations section.

**Techniques:** `groupby/agg` · `pct_change` · IQR outlier detection · `np.polyfit` trend lines · `boxplot` distributions · Pearson correlation

| | |
|---|---|
| 📓 **Jupyter Notebook** | [forex_trading_eda.ipynb →](./project-4-python-eda-forex/forex_trading_eda.ipynb) |
| 📋 **Documentation** | [README →](./project-4-python-eda-forex/README.md) |

---

### 5. ⚙️ Retail Sales Data Cleaning & Automation Pipeline
**Tools:** Python · Pandas · NumPy · openpyxl  
**Industry:** Retail — Supermarket / FMCG  
**Context:** Reflects real automation work replacing 12+ hours/week of manual Excel processing at Jumbo Supermarkten

A production-ready 9-step Python automation pipeline that ingests raw retail CSV or Excel files, validates schema and data types, detects and handles nulls, removes duplicates, applies business rule validation, engineers 12 derived features, and exports clean data + flagged records + a formatted Excel monthly summary report. Fully tested — catches nulls, invalid prices, bad discounts, duplicate IDs, and future-dated rows.

**Techniques:** Modular pipeline architecture · structured `logging` · `Pathlib` · `pd.ExcelWriter` · IQR validation · feature engineering · error handling

| | |
|---|---|
| 🐍 **Pipeline Script** | [retail_data_pipeline.py →](./project-5-python-automation-pipeline/retail_data_pipeline.py) |
| 📋 **Documentation** | [README →](./project-5-python-automation-pipeline/README.md) |

---

## 🛠️ Technical Skills

| Category | Tools & Technologies |
|---|---|
| **BI & Visualisation** | Power BI · DAX · Tableau · Matplotlib · Seaborn · Data Storytelling |
| **Data & Cloud** | SQL (JOINs, CTEs, Window Functions) · Google BigQuery · AWS · ETL · Data Modeling |
| **Programming** | Python (Pandas, NumPy, automation & EDA) · Jupyter Notebooks · Statistical Analysis |
| **Business Systems** | SAP · QuickBooks · ERP · CRM · Advanced Excel (Power Query, PivotTables) |
| **Methodology** | Agile · A/B Testing · KPI Development · Stakeholder Management · Root-Cause Analysis |
| **Domain Expertise** | Retail Analytics · Financial Services · Sales Analytics · HR Analytics · Revenue Optimization |

---

## 📂 Repository Structure

```
📁 data-analytics-portfolio/
│
├── 📁 dashboard-1-sales-revenue/        Power BI — Sales & Revenue Analytics
├── 📁 dashboard-2-hr-workforce/         Power BI — HR & Workforce Analytics
├── 📁 project-3-sql-retail-analysis/    SQL — 10 retail business insight queries
├── 📁 project-4-python-eda-forex/       Python EDA — Forex trading analysis notebook
├── 📁 project-5-python-automation-pipeline/  Python — Retail data cleaning pipeline
└── README.md                            This file
```

---

## 📬 Get In Touch

Open to data analyst, BI developer, and analytics engineer roles in the Netherlands and across Europe.

- 📧 **Email:** lasemajek12@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/tolu-majek124](https://www.linkedin.com/in/tolu-majek124/)
- 🐙 **GitHub:** [github.com/lasemajek12-max](https://github.com/lasemajek12-max)
- 📍 **Location:** Amsterdam, Netherlands · Open to hybrid / remote

---

*All datasets in this repository are simulated and generated for portfolio demonstration purposes only.*
