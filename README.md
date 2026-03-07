[README_portfolio_final.md](https://github.com/user-attachments/files/25813081/README_portfolio_final.md)
# 📊 Data Analytics Portfolio — Toluwalase Majekodunmi

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL%2FBigQuery-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Advanced-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![BigQuery](https://img.shields.io/badge/Google%20BigQuery-4285F4?style=for-the-badge&logo=googlebigquery&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

> **Data Analyst · Business Intelligence · Analytics Engineer**
> Amsterdam, Netherlands &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/tolu-majek124/) &nbsp;·&nbsp; [Live Portfolio](https://lasemajek12-max.github.io/data-analytics-portfolio/) &nbsp;·&nbsp; lasemajek12@gmail.com

---

## 👋 About Me

Data Analyst with **6+ years** delivering measurable business impact across retail, financial services, and operations — engineering Power BI dashboards, automating ETL workflows with Python and SQL, and transforming raw data into decisions that drove **8–18% performance improvements** across revenue, retention, and operational efficiency.

Currently working as **Sales & Marketing Data Analyst at Jumbo Supermarkten**, Amsterdam — Netherlands' second-largest supermarket chain with 700+ stores.

| | |
|---|---|
| 🏢 **Current Role** | Sales & Marketing Data Analyst · Jumbo Supermarkten · Amsterdam |
| 🎓 **Education** | MSc International Business Management · BSc Accounting |
| 📜 **Certifications** | IBM Data Science · Microsoft Excel & Power BI · Google BigQuery · AWS · PL-300 (in progress) |
| ☁️ **Cloud** | Google BigQuery · AWS (Free Tier) |
| 🌍 **Experience** | Nigeria · Ukraine · Netherlands |

---

## 📁 Projects — Quick Navigation

| # | Project | Tools | Type | Link |
|---|---|---|---|---|
| 1 | Sales & Revenue Analytics Dashboard | Power BI · DAX · SQL | Interactive Dashboard | [View →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-1-sales-revenue/Dashboard1_Sales_Preview.html) |
| 2 | HR & Workforce Analytics Dashboard | Power BI · DAX · Power Query | Interactive Dashboard | [View →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-2-hr-workforce/Dashboard2_HR_Preview.html) |
| 3 | Retail Sales & Customer Analysis | SQL · PostgreSQL · BigQuery | 10 Advanced Queries | [View →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-3-sql-retail-analysis/) |
| 4 | Forex Trading Performance EDA | Python · Pandas · Matplotlib | Jupyter Notebook | [View →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-4-python-eda-forex/) |
| 5 | Retail Data Cleaning & Pipeline | Python · Pandas · openpyxl | Automation Script | [View →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-5-python-automation-pipeline/) |

---

## 🗂️ Project Details

---

### 1. 📈 Sales & Revenue Analytics Dashboard

**Tools:** Power BI · DAX · SQL · Excel · Power Query
**Industry:** Financial Services — Forex Brokerage
**Dataset:** 1,200 transactions · $8.47M revenue · 4 regions · 8 sales reps · 2022–2023

An end-to-end sales performance dashboard tracking revenue, profit margin, deal volume, and client segment performance. Features 3 report pages, 7 DAX measures, dynamic slicers synced across pages, and conditional formatting on target attainment.

**Key DAX measures:** `Total Revenue` · `Profit Margin %` · `Target Attainment %` · `Revenue vs Target Variance`

**Business questions answered:**
- Which regions and reps are hitting their revenue targets?
- What is the month-on-month revenue and margin trend?
- How does performance break down by client segment (VIP, Corporate, Institutional, Retail)?

| | |
|---|---|
| 🔗 **Live Dashboard** | [lasemajek12-max.github.io · Dashboard 1 →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-1-sales-revenue/Dashboard1_Sales_Preview.html) |
| 🛠️ **Build Guide** | [Step-by-step Power BI instructions →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-1-sales-revenue/Dashboard1_Sales_BuildGuide.html) |
| 📂 **Dataset** | [Download Excel data →](https://github.com/lasemajek12-max/data-analytics-portfolio/raw/main/dashboard-1-sales-revenue/Dashboard1_Sales_Revenue_Data.xlsx) |

---

### 2. 👥 HR & Workforce Analytics Dashboard

**Tools:** Power BI · DAX · Power Query · Excel
**Industry:** Human Resources — Multi-department Corporate
**Dataset:** 214 employees · 8 departments · 1,842 applications · 2022–2024

A 3-page interactive HR dashboard covering headcount, attrition analysis (11.4% rate), performance distribution, diversity metrics, salary benchmarking, and a 5-stage recruitment funnel. Features bookmark-driven executive presentation mode — same data, two layouts, one click.

**Key DAX measures:** `Attrition Rate %` · `Active Employees` · `Promotion Eligible` · `Offer Acceptance Rate`

**Business questions answered:**
- Which departments have the highest attrition risk?
- What does the recruitment funnel look like from application to hire?
- How do salaries compare across levels and departments?

| | |
|---|---|
| 🔗 **Live Dashboard** | [lasemajek12-max.github.io · Dashboard 2 →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-2-hr-workforce/Dashboard2_HR_Preview.html) |
| 🛠️ **Build Guide** | [Step-by-step Power BI instructions →](https://lasemajek12-max.github.io/data-analytics-portfolio/dashboard-2-hr-workforce/Dashboard2_HR_BuildGuide.html) |
| 📂 **Dataset** | [Download Excel data →](https://github.com/lasemajek12-max/data-analytics-portfolio/raw/main/dashboard-2-hr-workforce/Dashboard2_HR_Workforce_Data.xlsx) |

---

### 3. 🛒 Retail Sales & Customer Analysis — SQL

**Tools:** SQL · PostgreSQL · Google BigQuery
**Industry:** Retail — Supermarket / FMCG
**Schema:** 5 joined tables (customers · products · stores · transactions · transaction_items)

10 advanced SQL business insight queries demonstrating CTEs, window functions, RFM segmentation, cohort retention analysis, and business rule logic. Directly reflects analytical work at Jumbo Supermarkten.

**SQL techniques used:**
`INNER JOIN` across 4 tables · Multiple CTEs · `LAG()` · `RANK()` · `SUM() OVER()` · `DATE_TRUNC` · `CASE WHEN` segmentation · `NULLIF` zero-division safety · Subqueries

| Query | Technique | Business Question |
|---|---|---|
| Monthly Revenue & Margin | `DATE_TRUNC` · aggregation | How is revenue trending month-on-month? |
| RFM Customer Segmentation | CTE · `CASE WHEN` | How do we classify customers by spend behaviour? |
| Month-over-Month Growth | CTE · `LAG()` | Is the business growing or shrinking? |
| Churn Risk Detection | CTE · date arithmetic · subquery | Which loyal customers haven't bought in 60+ days? |
| Cohort Retention Analysis | Multi-CTE · self-join · `AGE()` | Do acquired customers return to buy? |

| | |
|---|---|
| 🌐 **Project Page** | [lasemajek12-max.github.io · Project 3 →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-3-sql-retail-analysis/) |
| 📄 **SQL File** | [retail_sales_analysis.sql →](./project-3-sql-retail-analysis/retail_sales_analysis.sql) |
| 📋 **Documentation** | [README →](./project-3-sql-retail-analysis/README.md) |

---

### 4. 🐍 Forex Trading Performance — Python EDA

**Tools:** Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook
**Industry:** Financial Services — Forex Brokerage
**Dataset:** 1,200 trades · 8 sales reps · 4 regions · 5 products · 2022–2023

End-to-end exploratory data analysis notebook covering data cleaning, KPI dashboard, monthly revenue/profit trends, rep performance benchmarking, product/segment breakdown, deal size vs margin correlation, and regional growth analysis. Reflects real analytical work at Tixee Forex Brokerage, Kyiv.

**Python techniques:** `groupby/agg` · `pct_change` · IQR outlier detection · `np.polyfit` trend lines · `fill_between` shading · `boxplot` distributions · Pearson correlation (r = −0.12)

**Key findings:**
- Revenue dips are seasonal, not driven by rep performance
- Top rep outperforms bottom by 2.3× — gap is in volume, not deal size
- Larger deals compress margins (r = −0.12): chasing big tickets was counterproductive
- MENA: smallest region, fastest growth trajectory

| | |
|---|---|
| 🌐 **Project Page** | [lasemajek12-max.github.io · Project 4 →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-4-python-eda-forex/) |
| 📓 **Jupyter Notebook** | [forex_trading_eda.ipynb →](./project-4-python-eda-forex/forex_trading_eda.ipynb) |
| 📋 **Documentation** | [README →](./project-4-python-eda-forex/README.md) |

---

### 5. ⚙️ Retail Data Cleaning & Automation Pipeline

**Tools:** Python · Pandas · NumPy · openpyxl · logging · Pathlib
**Industry:** Retail — Supermarket / FMCG
**Context:** Replaces 12+ hours/week of manual Excel processing — reflects real automation work at Jumbo Supermarkten

A production-ready 9-step automation pipeline that ingests raw retail CSV or Excel files and returns a clean dataset, a flagged records file (with reason column), and a formatted Excel monthly summary report. Run time: 0.4 seconds.

**Pipeline steps:**
`Ingest` → `Schema Validation` → `Type Enforcement` → `Null Handling` → `Deduplication` → `Business Rules` → `Feature Engineering` → `Summary Report` → `Export`

**Data quality checks:**
- Schema validation — missing or misspelled column names
- Type enforcement — dates as strings, prices as text
- Null handling — critical fields dropped, non-critical fields imputed
- Duplicate removal — exact row duplicates AND duplicate transaction IDs (two separate checks)
- Business rules — negative prices, discounts >100%, zero quantity, future-dated records

**12 engineered features:** `gross_revenue` · `discount_amount` · `net_revenue` · `est_cost` · `gross_profit` · `margin_pct` · `year` · `month` · `month_name` · `quarter` · `day_of_week` · `week_number`

**Test result on demo file:** 500 rows in → 492 clean, 8 flagged, 2 duplicates removed, completed in 0.4s ✅

| | |
|---|---|
| 🌐 **Project Page** | [lasemajek12-max.github.io · Project 5 →](https://lasemajek12-max.github.io/data-analytics-portfolio/project-5-python-automation-pipeline/) |
| 🐍 **Pipeline Script** | [retail_data_pipeline.py →](./project-5-python-automation-pipeline/retail_data_pipeline.py) |
| 📋 **Documentation** | [README →](./project-5-python-automation-pipeline/README.md) |

---

## 🛠️ Technical Skills

| Category | Tools & Technologies |
|---|---|
| **BI & Visualisation** | Power BI · DAX (CALCULATE, SUMX, DIVIDE) · Tableau · Matplotlib · Seaborn · Data Storytelling |
| **Data & Cloud** | SQL (JOINs, CTEs, Window Functions) · Google BigQuery · AWS · Git · GitHub · ETL · Data Modelling |
| **Programming** | Python (Pandas, NumPy · EDA & automation) · Jupyter Notebooks · Statistical Analysis |
| **Business Systems** | SAP · QuickBooks · ERP · CRM · Advanced Excel (Power Query, PivotTables, macros) |
| **Methodology** | Agile · A/B Testing · KPI Development · Stakeholder Management · Root-Cause Analysis |
| **Domain Expertise** | Retail Analytics · Financial Services · Sales Analytics · HR Analytics · Revenue Optimisation |

---

## 📂 Repository Structure

```
📁 lasemajek12-max/data-analytics-portfolio/
│
├── 📁 dashboard-1-sales-revenue/
│   ├── Dashboard1_Sales_Preview.html         ← Live interactive dashboard
│   ├── Dashboard1_Sales_BuildGuide.html      ← Step-by-step build instructions
│   └── Dashboard1_Sales_Revenue_Data.xlsx    ← Source dataset (1,200 rows)
│
├── 📁 dashboard-2-hr-workforce/
│   ├── Dashboard2_HR_Preview.html            ← Live interactive dashboard
│   ├── Dashboard2_HR_BuildGuide.html         ← Step-by-step build instructions
│   └── Dashboard2_HR_Workforce_Data.xlsx     ← Source dataset (214 employees)
│
├── 📁 project-3-sql-retail-analysis/
│   ├── index.html                            ← Project landing page
│   ├── retail_sales_analysis.sql             ← 10 advanced SQL queries
│   └── README.md
│
├── 📁 project-4-python-eda-forex/
│   ├── index.html                            ← Project landing page
│   ├── forex_trading_eda.ipynb               ← Full EDA notebook
│   └── README.md
│
├── 📁 project-5-python-automation-pipeline/
│   ├── index.html                            ← Project landing page
│   ├── retail_data_pipeline.py               ← 9-step automation pipeline
│   └── README.md
│
└── README.md                                 ← This file
```

---

## 📬 Get In Touch

Open to **Data Analyst**, **BI Developer**, and **Analytics Engineer** roles in the Netherlands and across Europe.

| | |
|---|---|
| 📧 **Email** | lasemajek12@gmail.com |
| 💼 **LinkedIn** | [linkedin.com/in/tolu-majek124](https://www.linkedin.com/in/tolu-majek124/) |
| 🌐 **Portfolio** | [lasemajek12-max.github.io/data-analytics-portfolio](https://lasemajek12-max.github.io/data-analytics-portfolio/) |
| 📍 **Location** | Amsterdam, Netherlands · Open to hybrid / remote |

---

*All datasets in this repository are simulated and generated for portfolio demonstration purposes. Analysis reflects real business contexts from professional experience.*
