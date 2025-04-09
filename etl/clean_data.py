import pandas as pd
import sys
from pathlib import Path


def load_data(file_path):
    """Charger les données à partir d'un fichier CSV."""
    print(file_path)
    return pd.read_csv(file_path)

def save_data(df, output_file_path):
    """Sauvegarder les données nettoyées dans un nouveau fichier CSV."""
    df.to_csv(output_file_path, index=False)
    print(f"Les données nettoyées ont été sauvegardées dans {output_file_path}")

def clean_data(df):

    # Supprime la colonne "gross margin percentage"
    df.drop(columns=['gross margin percentage'], inplace=True)

    # Modifie le format de Date en yyyy_mm-dd
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Supprimer les espaces au début et à la fin
    df.columns = df.columns.str.strip()  
    # Convertir tout en minuscules
    df.columns = df.columns.str.lower()  
    # Remplacer les espaces par des underscores
    df.columns = df.columns.str.replace(' ', '_')  
    # Supprimer les caractères spéciaux
    df.columns = df.columns.str.replace(r'[^\w\s]', '', regex=True)

    return df  

if __name__ == "__main__":

    list_files = sys.argv[1:]

    print(list_files)

    for file in list_files:

        path = Path(file)

        # Charger les données
        input_file = path
        # input_file = '../data/supermarket_sales.csv'
        df = load_data(input_file)
        
        # Nettoyer les données
        cleaned_df = clean_data(df)
        
        # Sauvegarder les données nettoyées
        file = file.removesuffix('.csv')
        output_file = file + '_cleaned.csv' 
        save_data(cleaned_df, output_file)

# Pour executer : 
# Se positionner dans le dossier etl  (là où se trouve ce ficher)
# Exécuter : python ../data/clean_data.py (+ autant de fichier.csv que vous voulez)
# (autant de fichier csv que vous voulez dans le dossier data)
# (pas besoin de mettre ../data/ avant les fichiers csv)