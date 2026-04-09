from transform import transform
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

#load connection string
load_dotenv()
database_url = os.getenv("DATABASE_URL").replace("postgresql://", "postgresql+psycopg://")

#create SQLAlchemy engine
engine = create_engine(database_url)


def load():
    #read schema.sql
    with open("schema.sql", "r") as file:
        sql_script = file.read()

    #create table in Postgres
    try:
        with engine.connect() as conn:
            conn.execute(text(sql_script))
        print("Table created or already exists.")
    except Exception as e:
        print("Schema error:", e)
        return

    #get transformed data
    df_clean = transform()

    #insert into Postgres
    try: 
        df_clean.to_sql('coin_prices', engine, if_exists='append', index=False, method='multi')
        print('Data inserted successfully!')
    except Exception as e :
        print('Insert error', e)

if __name__ == '__main__':
    load()