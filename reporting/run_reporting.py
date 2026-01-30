from reporting import aggregate_bronze_clients, get_top_clients_by_volume, get_top_clients_by_pnl, save_top_clients, plot_volume_by_client_type
from config import Settings, setup_logging
import logging

settings = Settings()
settings.output_dir.mkdir(exist_ok=True)

setup_logging()

def run() -> None:
    """
    - Runs get_top_clients_by_volume, get_top_clients_by_pnl functions, generates 2 reports into a csv files  
    - Runs plot_volume_by_client_type function, that create a plot of aggregated weekly total_volume by client types
    """     
    logging.info(f"Starting reporting")
    aggregated_df = aggregate_bronze_clients()

    top_volume = get_top_clients_by_volume(aggregated_df)
    save_top_clients(top_volume, settings.output_dir/settings.top_volume_file)
    logging.info(f"csv with top 3 clients by volume generated successfully")
    
    top_pnl = get_top_clients_by_pnl(aggregated_df)
    save_top_clients(top_pnl, settings.output_dir/settings.top_pnl_file)
    logging.info(f"csv with top 3 clients by pnl generated successfully")
    
    plot_volume_by_client_type()
    logging.info(f"plot of aggregated weekly total_volume by client types generated successfully")
    logging.info(f"Reporting finished successfully")    

if __name__ == "__main__":
    run()