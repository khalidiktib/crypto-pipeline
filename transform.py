import glob
import pandas as pd
import json
import datetime

def transform():
    #get the latest file
    latest_file = sorted(glob.glob("raw_data/*.json"))[-1]

    #read JSON
    with open(latest_file, 'r') as file:
        file_list = json.load(file) 

    #convert to DataFrame
    df = pd.DataFrame(file_list)

    #select needed columns
    df_clean = df[
        ['id', 'symbol', 'name', 'current_price',
        'market_cap', 'market_cap_rank', 'total_volume',
        'price_change_percentage_24h', 'circulating_supply',
        'high_24h', 'low_24h', 'ath', 'ath_change_percentage',
        'last_updated']
    ]

    #add collected_at
    df_clean["collected_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    #return cleaned DataFrame
    return df_clean


#test
""" if __name__ == "__main__":
    df_result = transform()
    print(df_result.head())
    print(df_result.dtypes) """