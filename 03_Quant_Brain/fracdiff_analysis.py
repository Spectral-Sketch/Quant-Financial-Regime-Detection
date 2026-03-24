import sqlite3
import pandas as pd
import numpy as np

def apply_frac_diff(series, d, window=100):
    """Custom implementation of Fractional Differentiation using binomial expansion."""
    # Generate weights
    w = [1.0]
    for k in range(1, window):
        w.append(-w[-1] * ((d - k + 1) / k))
    weights = np.array(w[::-1])
    
    series_values = series.values
    res = np.full(len(series_values), np.nan)
    
    for i in range(window, len(series_values)):
        res[i] = np.dot(weights, series_values[i-window+1:i+1])
    return res

# Execution
conn = sqlite3.connect('../01_Data_Ingest/market_data.db')
df = pd.read_sql_query("SELECT * FROM processed_signals", conn)
conn.close()

# Apply d=0.35 for optimal Stationarity vs Memory balance
df['frac_diff_signal'] = apply_frac_diff(df['log_return'], d=0.35)

# Calculate Information Retention Score
mask = ~np.isnan(df['frac_diff_signal'])
retention = np.corrcoef(df['log_return'][mask], df['frac_diff_signal'][mask]) * 100
print(f"Information Retention Score: {round(retention, 2)}%")

# Export for Power BI Dashboard
df.to_csv('powerbi_input_final.csv', index=False)
