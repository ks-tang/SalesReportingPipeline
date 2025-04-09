import subprocess
from pathlib import Path

# Configuration
raw_csv_path = Path("data/supermarket_sales.csv")
cleaned_csv_path = Path("data/supermarket_sales_cleaned.csv")
table_name = "table_sales"

# Étape 1 : Nettoyage des données
print("\n[1/2] Nettoyage des données...")
subprocess.run(["python", "etl/clean_data.py", str(raw_csv_path)], check=True)

# Étape 2 : Chargement dans PostgreSQL
print("\n[2/2] Chargement des données dans PostgreSQL...")
subprocess.run(["python", "etl/load_to_db.py", str(cleaned_csv_path), table_name], check=True)

print("\n✅ Pipeline ETL terminé avec succès.")

# Pour executer :
# python run_pipeline.py