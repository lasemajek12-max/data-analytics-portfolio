# 🔄 Retail Sales Data Cleaning & Automation Pipeline

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20Export-217346?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Tested%20%26%20Working-27ae60?style=for-the-badge)

> **Author:** Toluwalase Majekodunmi · [LinkedIn](https://www.linkedin.com/in/tolu-majek124/) · [Portfolio](https://lasemajek12-max.github.io/data-analytics-portfolio/)

---

## 📌 Project Overview

A production-ready 9-step Python automation pipeline that ingests raw retail CSV/Excel sales files, cleans and validates the data, engineers business features, and exports a clean dataset + flagged records + formatted Excel summary report.

**Replaces 12+ hours/week of manual Excel processing** — reflecting real automation work at Jumbo Supermarkten, Amsterdam.

---

## ⚙️ Pipeline Steps

```
RAW CSV / EXCEL
      │
      ▼
┌─────────────────────────────────────┐
│  Step 1 │ Load file (CSV or Excel)  │
│  Step 2 │ Schema validation         │
│  Step 3 │ Data type enforcement     │
│  Step 4 │ Null detection & imputing │
│  Step 5 │ Duplicate removal         │
│  Step 6 │ Business rule validation  │
│  Step 7 │ Feature engineering       │
│  Step 8 │ Summary report generation │
│  Step 9 │ Export (CSV + Excel)      │
└─────────────────────────────────────┘
      │
      ├── data/processed/  →  clean_data.csv
      ├── data/processed/  →  flagged_rows.csv
      └── data/reports/    →  monthly_summary.xlsx
```

---

## 🔑 Data Quality Checks Performed

| Check | What It Catches |
|---|---|
| Schema validation | Missing or misspelled column names |
| Type enforcement | Dates stored as strings, numbers as text |
| Null detection | Missing values in critical and non-critical fields |
| Duplicate removal | Exact duplicate rows + duplicate transaction IDs |
| Business rules | Negative prices, impossible discounts, future dates |

---

## 🛠️ Feature Engineering Output

The pipeline adds 12 derived columns including:

- `gross_revenue`, `discount_amount`, `net_revenue`
- `est_cost`, `gross_profit`, `margin_pct`
- `year`, `month`, `month_name`, `quarter`, `day_of_week`, `week_number`

---

## 🔑 Python Techniques Demonstrated

- **Pandas:** `read_csv`, `read_excel`, `to_datetime`, `dropna`, `fillna`, `groupby`, `agg`, `drop_duplicates`, `pd.ExcelWriter`
- **NumPy:** `where`, `random`, vectorised operations
- **openpyxl:** Excel export with column width formatting
- **Logging:** Structured timestamped logging across all pipeline steps
- **Pathlib:** Cross-platform file path handling
- **OOP patterns:** Modular functions with clear single responsibilities
- **Error handling:** Try/catch with informative failure logging

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas numpy openpyxl

# Run with demo data (generates sample CSV with quality issues automatically)
python retail_data_pipeline.py

# Run on your own file
python -c "from retail_data_pipeline import run_pipeline; run_pipeline('your_file.csv')"
```

**Expected output:**
```
2024-01-15 09:00:01  INFO      Pipeline START — demo_sales.csv
2024-01-15 09:00:01  WARNING   15 nulls detected in: category (15)
2024-01-15 09:00:01  WARNING   Removed 1 exact duplicates, 1 duplicate IDs
2024-01-15 09:00:01  WARNING   8 rows flagged with business rule violations
2024-01-15 09:00:01  INFO      Clean: 492 | Flagged: 8
2024-01-15 09:00:01  INFO      Pipeline COMPLETE in 0.4s ✅
```

---

## 📁 Files

```
project-5-python-automation-pipeline/
├── retail_data_pipeline.py    ← Full 9-step pipeline script
├── README.md                  ← This file
├── data/
│   ├── raw/                   ← Input files go here
│   ├── processed/             ← Clean + flagged CSVs exported here
│   └── reports/               ← Monthly Excel reports exported here
```

---

*Dataset is simulated. Pipeline logic reflects real retail data engineering work.*
