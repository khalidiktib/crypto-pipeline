CREATE TABLE IF NOT EXISTS coin_prices (
id TEXT,
symbol TEXT,
name TEXT,
current_price REAL,
market_cap REAL,
market_cap_rank INTEGER,
total_volume REAL,
price_change_percentage_24h REAL,
circulating_supply REAL,
high_24h REAL,
low_24h REAL,
ath REAL,
ath_change_percentage REAL,
last_updated TIMESTAMP,
collected_at TIMESTAMP,
CONSTRAINT pk_coin PRIMARY KEY (id, collected_at)
)