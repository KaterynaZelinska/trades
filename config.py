from pydantic_settings import BaseSettings
from pathlib import Path
import logging

class Settings(BaseSettings): 
    input_csv: Path = Path("data/trades.csv")
    db_path: Path = Path("agg_result.db")
    output_dir: Path = Path("output")    
    weekly_volume_file: str = "weekly_trading_volume.png"
    top_volume_file: str = "top_clients_volume.csv"    
    top_pnl_file: str = "top_clients_pnl.csv"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )