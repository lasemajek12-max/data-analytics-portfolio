"""
========================================================
  Retail Sales Data Cleaning & Automation Pipeline
  Author  : Toluwalase Majekodunmi
  Tools   : Python · Pandas · NumPy · openpyxl
  Purpose : Automated ingestion, cleaning, validation,
            and export of raw retail CSV/Excel sales data
  Context : Reflects automation work at Jumbo Supermarkten
            replacing 12+ hrs/week of manual processing
========================================================
"""

import pandas as pd
import numpy as np
import os
import logging
from datetime import datetime
from pathlib import Path


# ── Logging setup ──────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)-8s  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
log = logging.getLogger(__name__)


# ── Config ─────────────────────────────────────────────────────────────────
INPUT_DIR      = Path('data/raw')
OUTPUT_DIR     = Path('data/processed')
REPORT_DIR     = Path('data/reports')
REQUIRED_COLS  = ['transaction_id', 'date', 'store_id', 'product_id',
                  'product_name', 'category', 'quantity', 'unit_price',
                  'discount_pct', 'sales_rep', 'region']
DATE_FORMAT    = '%Y-%m-%d'
MAX_PRICE      = 50_000
MAX_DISCOUNT   = 100
MIN_QUANTITY   = 1


# ──────────────────────────────────────────────────────────────────────────
# STEP 1 — Data Ingestion: Load CSV or Excel automatically
# ──────────────────────────────────────────────────────────────────────────
def load_file(filepath: Path) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a DataFrame.
    Automatically detects file type by extension.
    """
    suffix = filepath.suffix.lower()
    log.info(f'Loading file: {filepath.name}')

    if suffix == '.csv':
        df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)
    elif suffix in ('.xlsx', '.xls'):
        df = pd.read_excel(filepath, engine='openpyxl')
    else:
        raise ValueError(f'Unsupported file type: {suffix}')

    log.info(f'Loaded {len(df):,} rows × {len(df.columns)} columns')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 2 — Schema Validation: Check required columns exist
# ──────────────────────────────────────────────────────────────────────────
def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verify all required columns are present.
    Normalise column names to lowercase with underscores.
    """
    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace(' ', '_', regex=False)
                  .str.replace(r'[^a-z0-9_]', '', regex=True))

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f'Missing required columns: {missing}')

    log.info('Schema validation passed ✅')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 3 — Data Type Enforcement
# ──────────────────────────────────────────────────────────────────────────
def enforce_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cast columns to correct data types.
    Coerce invalid values to NaN for later handling.
    """
    original_len = len(df)

    # Date parsing
    df['date'] = pd.to_datetime(df['date'], format=DATE_FORMAT, errors='coerce')

    # Numeric columns
    for col in ['quantity', 'unit_price', 'discount_pct']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # String columns — strip whitespace
    for col in ['transaction_id', 'store_id', 'product_id',
                'product_name', 'category', 'sales_rep', 'region']:
        df[col] = df[col].astype(str).str.strip()

    invalid_dates = df['date'].isna().sum()
    if invalid_dates:
        log.warning(f'{invalid_dates} rows with unparseable dates — will be removed')

    log.info(f'Type enforcement complete. Rows: {original_len:,}')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 4 — Null Handling
# ──────────────────────────────────────────────────────────────────────────
def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Report nulls, drop rows with critical nulls,
    and impute non-critical nulls where appropriate.
    """
    null_summary = df.isnull().sum()
    null_cols    = null_summary[null_summary > 0]

    if len(null_cols):
        log.warning(f'Null values detected:\n{null_cols.to_string()}')

    # Critical columns — drop rows where these are null
    critical = ['transaction_id', 'date', 'product_id', 'unit_price', 'quantity']
    before   = len(df)
    df = df.dropna(subset=critical)
    dropped = before - len(df)
    if dropped:
        log.warning(f'Dropped {dropped:,} rows with nulls in critical columns')

    # Non-critical — impute
    df['discount_pct'] = df['discount_pct'].fillna(0.0)
    df['category']     = df['category'].fillna('Unknown')
    df['region']       = df['region'].fillna('Unknown')

    log.info(f'Null handling complete. Remaining rows: {len(df):,}')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 5 — Duplicate Removal
# ──────────────────────────────────────────────────────────────────────────
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows and duplicate transaction IDs,
    keeping the first occurrence.
    """
    before = len(df)
    df = df.drop_duplicates()
    exact_dupes = before - len(df)

    df = df.drop_duplicates(subset='transaction_id', keep='first')
    id_dupes = (before - exact_dupes) - len(df)

    if exact_dupes or id_dupes:
        log.warning(f'Removed {exact_dupes} exact duplicates, '
                    f'{id_dupes} duplicate transaction IDs')

    log.info(f'Duplicate removal complete. Rows: {len(df):,}')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 6 — Business Rule Validation
# ──────────────────────────────────────────────────────────────────────────
def validate_business_rules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply domain-specific business rules:
    - quantity must be >= 1
    - unit_price must be > 0 and <= MAX_PRICE
    - discount_pct must be between 0 and MAX_DISCOUNT
    - date must not be in the future
    Flag violations in a new column rather than silently dropping.
    """
    df = df.copy()
    df['validation_flag'] = ''

    # Quantity check
    mask_qty = df['quantity'] < MIN_QUANTITY
    df.loc[mask_qty, 'validation_flag'] += 'INVALID_QUANTITY;'

    # Price check
    mask_price = (df['unit_price'] <= 0) | (df['unit_price'] > MAX_PRICE)
    df.loc[mask_price, 'validation_flag'] += 'INVALID_PRICE;'

    # Discount check
    mask_disc = (df['discount_pct'] < 0) | (df['discount_pct'] > MAX_DISCOUNT)
    df.loc[mask_disc, 'validation_flag'] += 'INVALID_DISCOUNT;'

    # Future date check
    today     = pd.Timestamp.today().normalize()
    mask_fut  = df['date'] > today
    df.loc[mask_fut, 'validation_flag'] += 'FUTURE_DATE;'

    flagged = (df['validation_flag'] != '').sum()
    if flagged:
        log.warning(f'{flagged} rows flagged with business rule violations')

    # Separate clean vs flagged
    clean   = df[df['validation_flag'] == ''].drop(columns='validation_flag')
    flagged_df = df[df['validation_flag'] != '']

    log.info(f'Business validation complete. '
             f'Clean: {len(clean):,} | Flagged: {len(flagged_df):,}')
    return clean, flagged_df


# ──────────────────────────────────────────────────────────────────────────
# STEP 7 — Feature Engineering: Add derived columns
# ──────────────────────────────────────────────────────────────────────────
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add calculated columns used in downstream reporting:
    - net_revenue  : revenue after discount
    - gross_profit : estimated profit (40% margin assumption)
    - year, month, quarter, day_of_week
    - basket_value : total value per transaction
    """
    df = df.copy()

    df['gross_revenue']   = (df['quantity'] * df['unit_price']).round(2)
    df['discount_amount'] = (df['gross_revenue'] * df['discount_pct'] / 100).round(2)
    df['net_revenue']     = (df['gross_revenue'] - df['discount_amount']).round(2)
    df['est_cost']        = (df['net_revenue'] * 0.55).round(2)
    df['gross_profit']    = (df['net_revenue'] - df['est_cost']).round(2)
    df['margin_pct']      = np.where(
        df['net_revenue'] > 0,
        (df['gross_profit'] / df['net_revenue'] * 100).round(2),
        0
    )

    df['year']         = df['date'].dt.year
    df['month']        = df['date'].dt.month
    df['month_name']   = df['date'].dt.strftime('%b %Y')
    df['quarter']      = df['date'].dt.quarter.map(
                             {1:'Q1',2:'Q2',3:'Q3',4:'Q4'})
    df['day_of_week']  = df['date'].dt.strftime('%A')
    df['week_number']  = df['date'].dt.isocalendar().week.astype(int)

    log.info(f'Feature engineering complete. '
             f'Columns: {len(df.columns)} (+{len(df.columns)-len(REQUIRED_COLS)})')
    return df


# ──────────────────────────────────────────────────────────────────────────
# STEP 8 — Summary Report Generation
# ──────────────────────────────────────────────────────────────────────────
def generate_summary_report(df: pd.DataFrame,
                             flagged_df: pd.DataFrame,
                             source_file: str) -> dict:
    """
    Generate a processing summary dictionary logged and
    optionally written to a text report file.
    """
    report = {
        'source_file'       : source_file,
        'processed_at'      : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_rows_clean'  : len(df),
        'total_rows_flagged': len(flagged_df),
        'date_range_start'  : str(df['date'].min().date()),
        'date_range_end'    : str(df['date'].max().date()),
        'total_net_revenue' : f"${df['net_revenue'].sum():,.2f}",
        'total_gross_profit': f"${df['gross_profit'].sum():,.2f}",
        'avg_margin_pct'    : f"{df['margin_pct'].mean():.1f}%",
        'unique_stores'     : df['store_id'].nunique(),
        'unique_products'   : df['product_id'].nunique(),
        'unique_reps'       : df['sales_rep'].nunique(),
        'categories'        : sorted(df['category'].unique().tolist()),
        'regions'           : sorted(df['region'].unique().tolist()),
    }

    log.info('── PIPELINE SUMMARY ──────────────────────────────────────')
    for k, v in report.items():
        log.info(f'   {k:<25}: {v}')
    log.info('─' * 60)
    return report


# ──────────────────────────────────────────────────────────────────────────
# STEP 9 — Export: Save clean data + flagged rows + pivot summary
# ──────────────────────────────────────────────────────────────────────────
def export_outputs(df: pd.DataFrame,
                   flagged_df: pd.DataFrame,
                   source_stem: str) -> None:
    """
    Export three outputs:
    1. Clean processed dataset as CSV
    2. Flagged/invalid rows as separate CSV for review
    3. Monthly pivot summary as Excel with formatting
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M')

    # Clean data
    clean_path = OUTPUT_DIR / f'{source_stem}_clean_{ts}.csv'
    df.to_csv(clean_path, index=False)
    log.info(f'Clean data exported → {clean_path}')

    # Flagged rows
    if len(flagged_df):
        flag_path = OUTPUT_DIR / f'{source_stem}_flagged_{ts}.csv'
        flagged_df.to_csv(flag_path, index=False)
        log.info(f'Flagged rows exported → {flag_path}')

    # Monthly pivot summary to Excel
    pivot = (df.groupby(['year','month_name','region'])
             .agg(
                 transactions = ('transaction_id', 'count'),
                 net_revenue  = ('net_revenue',    'sum'),
                 gross_profit = ('gross_profit',   'sum'),
                 avg_margin   = ('margin_pct',     'mean'),
             )
             .round(2)
             .reset_index())
    pivot.columns = ['Year','Month','Region','Transactions',
                     'Net Revenue ($)','Gross Profit ($)','Avg Margin (%)']

    report_path = REPORT_DIR / f'{source_stem}_monthly_report_{ts}.xlsx'
    with pd.ExcelWriter(report_path, engine='openpyxl') as writer:
        pivot.to_excel(writer, sheet_name='Monthly Summary', index=False)

        # Basic column width formatting
        ws = writer.sheets['Monthly Summary']
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col) + 4
            ws.column_dimensions[col[0].column_letter].width = min(max_len, 30)

    log.info(f'Monthly summary exported → {report_path}')


# ──────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE ORCHESTRATOR
# ──────────────────────────────────────────────────────────────────────────
def run_pipeline(filepath: str) -> pd.DataFrame:
    """
    Execute the full 9-step data cleaning and automation pipeline.
    Returns the clean, processed DataFrame.

    Steps:
        1. Load file (CSV or Excel)
        2. Validate schema
        3. Enforce data types
        4. Handle nulls
        5. Remove duplicates
        6. Validate business rules
        7. Engineer features
        8. Generate summary report
        9. Export outputs
    """
    fp = Path(filepath)
    log.info('=' * 60)
    log.info(f'  PIPELINE START — {fp.name}')
    log.info('=' * 60)
    start_time = datetime.now()

    try:
        df          = load_file(fp)
        df          = validate_schema(df)
        df          = enforce_types(df)
        df          = handle_nulls(df)
        df          = remove_duplicates(df)
        df, flagged = validate_business_rules(df)
        df          = engineer_features(df)
        report      = generate_summary_report(df, flagged, fp.name)
        export_outputs(df, flagged, fp.stem)

    except Exception as e:
        log.error(f'Pipeline failed: {e}')
        raise

    elapsed = (datetime.now() - start_time).total_seconds()
    log.info(f'  PIPELINE COMPLETE in {elapsed:.1f}s ✅')
    log.info('=' * 60)
    return df


# ──────────────────────────────────────────────────────────────────────────
# DEMO — Generate sample data and run pipeline
# ──────────────────────────────────────────────────────────────────────────
def generate_demo_data(output_path: str = 'data/raw/demo_sales.csv',
                       n: int = 500) -> None:
    """
    Generate a realistic sample CSV with intentional data quality issues:
    - Some nulls in non-critical columns
    - A few invalid prices and discount values
    - Duplicate transaction IDs
    - A future-dated row
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    np.random.seed(99)

    categories = ['Dairy','Bakery','Produce','Beverages','Snacks','Frozen','Household']
    regions    = ['Noord-Holland','Zuid-Holland','Utrecht','Gelderland']
    reps       = ['Emma V.','Lars B.','Sophie K.','Pieter D.','Aisha M.']
    products   = [f'PROD-{str(i).zfill(4)}' for i in range(1, 51)]

    df = pd.DataFrame({
        'transaction_id': [f'TXN-{str(i).zfill(5)}' for i in range(1, n+1)],
        'date'          : pd.to_datetime(
                              np.random.choice(
                                  pd.date_range('2024-01-01','2024-12-31'), n)
                          ).strftime(DATE_FORMAT),
        'store_id'      : [f'STR-{np.random.randint(1,16):02d}' for _ in range(n)],
        'product_id'    : np.random.choice(products, n),
        'product_name'  : [f'Product {np.random.randint(1,51)}' for _ in range(n)],
        'category'      : np.random.choice(categories, n),
        'quantity'      : np.random.randint(1, 25, n),
        'unit_price'    : np.random.uniform(0.5, 120, n).round(2),
        'discount_pct'  : np.random.choice(
                              [0, 5, 10, 15, 20], n,
                              p=[0.5, 0.2, 0.15, 0.1, 0.05]),
        'sales_rep'     : np.random.choice(reps, n),
        'region'        : np.random.choice(regions, n),
    })

    # Introduce intentional data quality issues for demo purposes
    df.loc[np.random.choice(n, 15, replace=False), 'category']    = np.nan
    df.loc[np.random.choice(n, 8, replace=False),  'discount_pct']= np.nan
    df.loc[np.random.choice(n, 5, replace=False),  'unit_price']  = -99
    df.loc[np.random.choice(n, 3, replace=False),  'discount_pct']= 150
    # Add duplicate
    df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)
    # Add future date
    df.loc[df.index[-1], 'date'] = '2099-01-01'

    df.to_csv(output_path, index=False)
    log.info(f'Demo data generated → {output_path} ({len(df)} rows, '
             f'includes intentional quality issues)')


# ──────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    # Generate demo data with quality issues, then run the full pipeline
    generate_demo_data()
    clean_df = run_pipeline('data/raw/demo_sales.csv')
    print(f'\n✅ Final clean dataset: {clean_df.shape[0]:,} rows × '
          f'{clean_df.shape[1]} columns')
    print(clean_df[['transaction_id','date','product_name',
                    'net_revenue','gross_profit','margin_pct']].head(10))
