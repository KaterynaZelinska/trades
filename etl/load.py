import sqlite3
import pandas as pd     
from config import Settings
import logging

settings = Settings()

def load_to_sqlite(df: pd.DataFrame) -> None:
    """
    Loads given DataFrame into the table
    """    
    with sqlite3.connect(settings.db_path) as conn:
        logging.info(f"Loading data to SQLite")
        df.to_sql(
            "agg_trades_weekly",
            conn,
            if_exists="replace",
            index=False
        )

    logging.info(f"Data loaded to SQLite successfully")