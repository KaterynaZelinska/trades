import pandas as pd
import logging

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms data:
    - converts timestamp to week_start_date
    - aggregates by: 
        week_start_date
        client_type (gold, silver, bronze)
        user_id
        symbol
    - calculates:  
        total_volume
        trade_count 
        total_pnl 
    """
    logging.info(f"Transforming data")  
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    invalid_rows_count = df['timestamp'].isna().sum()
    if invalid_rows_count > 0:
        logging.warning(f" {invalid_rows_count} rows with invalid timestamps dropped")
    df = df.dropna(subset=['timestamp'])

    df['week_start_date'] = (df['timestamp'].dt.to_period('W').dt.start_time.dt.date)
 
    # Based on a given data, using simplified formule and calculating total_pnl as signed cash flow based on trade side
    df["signed_pnl"] = (df["quantity"] * df["price"]).where(df["side"].str.lower() == "sell", -df["quantity"] * df["price"])

    aggregated_df = df.groupby(
        ['week_start_date', 'client_type', 'user_id', 'symbol'],
        as_index=False
    ).agg(
        total_volume=('quantity', 'sum'),
        trade_count=('quantity', 'count'),
        total_pnl=('signed_pnl', 'sum')
    )

    logging.info(f"Data transformed successfully")
    return aggregated_df
