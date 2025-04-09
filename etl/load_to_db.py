import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df, table_name, db_url):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Données chargées dans la table '{table_name}' avec succès.")

if __name__ == "__main__":
    csv_file = Path(sys.argv[1])
    table_name = sys.argv[2]
    
    df = pd.read_csv(csv_file)
    
    # URL Render PostgreSQL
    db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    load_to_postgres(df, table_name, db_url)

# Pour excéuter : 
# python load_to_db.py ../data/supermarket_sales_cleaned.csv table_sales