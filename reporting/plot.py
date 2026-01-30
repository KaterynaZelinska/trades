import matplotlib.pyplot as plt
import mplcyberpunk
import pandas as pd
import sqlite3      
from config import Settings

settings = Settings()

def plot_volume_by_client_type() -> None:
    """
    Builds plot of aggregated weekly total_volume by client types 
    """    
    # gets data from the table
    conn = sqlite3.connect(settings.db_path)
    df = pd.read_sql("SELECT week_start_date, client_type, total_volume FROM agg_trades_weekly", conn)
    conn.close()

    # aggregates by weeks and client types
    pivot = df.pivot_table(
        index='week_start_date',
        columns='client_type',
        values='total_volume',
        aggfunc='sum',
        fill_value=0
    )

    plt.style.use("cyberpunk")
    mplcyberpunk.add_glow_effects()

    pivot.plot(figsize=(6,4), title="weekly trading volume", xlabel="week", ylabel="total volume")   
    plt.xticks(rotation=60)    
    plt.tight_layout()
 
    file_path = settings.output_dir / settings.weekly_volume_file
    plt.savefig(file_path)
    plt.close()