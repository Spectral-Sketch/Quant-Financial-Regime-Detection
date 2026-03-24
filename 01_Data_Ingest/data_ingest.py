import yfinance as yf
import sqlite3
import pandas as pd

def create_market_database():
    symbol = "SPY" # S&P 500 ETF als markt-benchmark
    db_name = 'market_data.db'

    print(f"Bezig met ophalen van {symbol} data...")
    df = yf.download(symbol, start="2020-01-01", end="2025-01-01")
    
    # Data Cleaning: Multi-index platmaken en kolommen SQL-vriendelijk maken
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.reset_index(inplace=True)
    df.columns = [c.replace(' ', '_') for c in df.columns]

    # Verbinding maken met SQLite
    conn = sqlite3.connect(db_name)
    try:
        df.to_sql('raw_market_data', conn, if_exists='replace', index=False)
        print(f"Succes! Tabel 'raw_market_data' aangemaakt met {len(df)} rijen.")
    finally:
        conn.close()

if __name__ == "__main__":
    create_market_database()
