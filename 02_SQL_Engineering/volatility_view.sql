-- Create a processed view for the Quant model
CREATE VIEW IF NOT EXISTS processed_signals AS
WITH base_stats AS (
    SELECT 
        Date, 
        Close,
        -- Calculate Log Returns (standard for quantitative analysis)
        LN(Close / LAG(Close) OVER (ORDER BY Date)) as log_return,
        -- Manual Moving Volatility calculation (Standard Deviation)
        AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) as avg_price,
        AVG(Close * Close) OVER (ORDER BY Date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) as avg_sq_price
    FROM raw_market_data
)
SELECT 
    Date, 
    Close, 
    log_return,
    -- The Early Warning Indicator: Square root of Variance
    SQRT(ABS(avg_sq_price - (avg_price * avg_price))) as moving_volatility
FROM base_stats
WHERE log_return IS NOT NULL;
