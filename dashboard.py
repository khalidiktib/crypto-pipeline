import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd


st.title('Crypto Data Pipeline')

#Load environment variables
load_dotenv()

#create engine (Postgres / Supabase)
database_url = os.getenv('DATABASE_URL') or st.secrets['DATABASE_URL']
st.write("DB URL found:", database_url is not None)
engine = create_engine(
    database_url,
    connect_args={
        'sslmode': 'require',
        'connect_timeout': 10
        }
)

#historical data
df = pd.read_sql('SELECT * FROM coin_prices', engine)

#latest snapshot only
df_latest = pd.read_sql('''
    SELECT * FROM coin_prices 
    WHERE collected_at = (SELECT MAX(collected_at) FROM coin_prices)
''', engine)


#Display the dataframe as a table
st.dataframe(df)


#Market cap chart
df_chart = df_latest.set_index("id")["market_cap"]  
st.subheader("Market Cap Comparison")
st.bar_chart(df_chart)


#Price overtime
shaped_df = df.pivot(index='collected_at', columns='id', values='current_price')
st.subheader("Price Over Time")
st.line_chart(shaped_df)

#24h change
results_df = df_latest.set_index('id')['price_change_percentage_24h']
st.subheader("24h Price Change %")
st.bar_chart(results_df)


#Market trend
avg_change = df_latest["price_change_percentage_24h"].mean()

# Determine trend
if avg_change > 0:
    trend = "Bullish"
else:
    trend = "Bearish"
# Display
st.metric("Market Trend", trend, f"{avg_change:.2f}%")