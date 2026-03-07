# 📈 Forex Trading Performance — Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Seaborn-11557c?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

> **Author:** Toluwalase Majekodunmi · [LinkedIn](https://www.linkedin.com/in/tolu-majek124/) · [Portfolio](https://lasemajek12-max.github.io/data-analytics-portfolio/)

---

## 📌 Project Overview

End-to-end exploratory data analysis of 1,200 simulated forex brokerage transactions across 8 sales reps, 4 regions, 5 products, and 2 years (2022–2023). Reflects real analytical work performed at **Tixee Forex Brokerage, Kyiv**.

---

## 🎯 Business Questions Answered

1. What is the overall revenue and profit margin trend month-on-month?
2. Which products and client segments drive the most profit?
3. Are there seasonal patterns in trading volume and revenue?
4. Which sales reps are over/underperforming against targets?
5. What is the relationship between deal size and profit margin?
6. Which regions show the strongest growth trajectory?

---

## 📊 Analysis Sections

| Section | What It Covers |
|---|---|
| 1. Data Generation | Simulating realistic trading data with Pandas + NumPy |
| 2. Data Cleaning | Null checks, duplicate detection, outlier analysis |
| 3. KPI Dashboard | Revenue, profit, margin, deal count, completion rate |
| 4. Monthly Trend | Revenue vs profit trend, MoM growth, margin % |
| 5. Rep Performance | Revenue, avg deal size, target attainment by rep |
| 6. Product & Segment | Donut chart + bar breakdown by product/segment |
| 7. Correlation | Deal size vs margin scatter, box plots by product |
| 8. Regional Analysis | Monthly trend lines + total revenue by region |
| 9. Key Findings | Summary of insights + business recommendations |

---

## 🔑 Python Techniques Demonstrated

- **Pandas:** `groupby`, `agg`, `merge`, `pct_change`, `dt` accessor, `to_period`
- **NumPy:** `random`, `polyfit`, `linspace`, `clip`, `sort`
- **Matplotlib:** Multi-panel subplots, `fill_between`, `barh`, `scatter`, `boxplot`
- **Seaborn:** Color palettes, distribution styling
- **Data Cleaning:** IQR outlier detection, null checks, type validation
- **Derived Metrics:** Margin %, MoM growth, target attainment, running totals

---

## 🚀 How to Run

**Option 1 — Jupyter Notebook (recommended):**
```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook forex_trading_eda.ipynb
```

**Option 2 — Google Colab (no install needed):**
Upload `forex_trading_eda.ipynb` to [colab.research.google.com](https://colab.research.google.com) and run all cells.

---

## 📁 Files

```
project-4-python-eda-forex/
├── forex_trading_eda.ipynb    ← Full EDA notebook
└── README.md                  ← This file
```

---

*Dataset is simulated for portfolio purposes. Analysis reflects the business context of a real forex brokerage environment.*
