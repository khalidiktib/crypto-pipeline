import sqlite3
from transform import transform

def load():
    #connect to database
    conn = sqlite3.connect("crypto.db") #create the actual database
    cursor = conn.cursor()

    #read schema.sql
    with open("schema.sql", "r") as file:
        sql_script = file.read()

    #execute SQL script
    cursor.executescript(sql_script)

    #save changes
    conn.commit()

    #load the DataFrame
    df_clean = transform()

    #insert df_clean into the database
    try:
        df_clean.to_sql('coin_prices', conn, if_exists='append', index=False)
        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)

    #close connection
    conn.close()

"""
# verify data in database
result = cursor.execute("SELECT * FROM coin_prices")
for row in result:
    print(row) """