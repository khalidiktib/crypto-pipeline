import streamlit as st
import sqlite3
import pandas as pd


st.title('Crypto Data Pipeline')

#Load the data
conn = sqlite3.connect("crypto.db")

#historical data
df = pd.read_sql('SELECT * FROM coin_prices', conn)

#latest snapshot only
df_latest = pd.read_sql('''
    SELECT * FROM coin_prices 
    WHERE collected_at = (SELECT MAX(collected_at) FROM coin_prices)
''', conn)

#Display the dataframe as a table
st.dataframe(df)

#chart data preparation and display
df_chart = df_latest.set_index("id")["market_cap"]  
st.subheader("Market Cap Comparison")
st.bar_chart(df_chart)


shaped_df = df.pivot(index='collected_at', columns='id', values='current_price')
st.subheader("Price Over Time")
st.line_chart(shaped_df)

results_df = df_latest.set_index('id')['price_change_percentage_24h']
st.subheader("24h Price Change %")
st.bar_chart(results_df)


avg_change = df_latest["price_change_percentage_24h"].mean()
# Determine trend
if avg_change > 0:
    trend = "Bullish"
else:
    trend = "Bearish"
# Display
st.metric("Market Trend", trend, f"{avg_change:.2f}%")