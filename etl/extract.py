import pandas as pd
from config import Settings
from pathlib import Path
import logging

settings = Settings()

def extract_data(csv_path: Path = settings.input_csv) -> pd.DataFrame: 
    """
    Extracts data from CSV file.
    """ 
    logging.info(f"Extracting data")
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found")
    df = pd.read_csv(csv_path)
    logging.info(f"Data extracted successfully")
    return df
