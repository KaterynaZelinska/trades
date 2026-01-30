import pandas as pd
import sqlite3
from pathlib import Path
from config import Settings 

settings = Settings()

def aggregate_bronze_clients() -> pd.DataFrame:
    """
    Gets data from the agg_trades_weekly table  
    Filters to get bronze clients only and aggregates by user_id 
    """ 
    conn = sqlite3.connect(settings.db_path)
    df = pd.read_sql("SELECT client_type, user_id, total_volume, trade_count, total_pnl FROM agg_trades_weekly", conn)
    conn.close()

    bronze = df[df['client_type'] == 'bronze']

    agg = (
        bronze.groupby('user_id', as_index=False)
              .agg(
                  total_volume=('total_volume', 'sum'),
                  total_pnl=('total_pnl', 'sum'),
                  trade_count=('trade_count', 'sum')
              )
    )
    return agg

def get_top_clients_by_volume(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Sorts by total_volume 
    Returns n number of top clients
    """ 
    return df.sort_values('total_volume', ascending=False).head(top_n)

def get_top_clients_by_pnl(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Sorts by total_pnl 
    Returns n number of top clients
    """ 
    return df.sort_values('total_pnl', ascending=False).head(top_n)
    
def save_top_clients(df: pd.DataFrame, file_path: Path) -> None:
    """
    Takes DataFrame and saves output to csv file
    """
    df.to_csv(file_path, index=False)