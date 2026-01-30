from etl import extract_data, transform_data, load_to_sqlite
from config import Settings, setup_logging
import logging
    
setup_logging()

settings = Settings()
def main() -> None:
    """
    Executes extract, transform and load modules
    """
    logging.info(f"Starting ETL pipeline")
    df = extract_data(settings.input_csv)
    df_transformed = transform_data(df)    
    load_to_sqlite(df_transformed)
    logging.info(f"ETL pipeline finished successfully")

if __name__ == "__main__":
    main()