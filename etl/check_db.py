import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")  
table_name = "table_sales"  

engine = create_engine(db_url)
df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 10", engine)
print(df)


count = pd.read_sql(f"SELECT COUNT(*) FROM {table_name}", engine)
print("Nombre total de lignes :", count.iloc[0,0])