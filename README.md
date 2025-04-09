# 🛒 Sales Reporting Pipeline

Ce projet met en place une pipeline de données complète pour l’analyse des ventes d’un supermarché à partir d’un dataset public (disponible ici : https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales).

Il combine des outils de data engineering (ETL, PostgreSQL, Docker, CI/CD) et de visualisation (Power BI).

---

## 📦 Contenu du projet

### 🔁 ETL (Extract, Transform, Load)
- Nettoyage et transformation des données avec Python
- Chargement dans une base de données PostgreSQL hébergée sur Render
- Script principal : `etl/run_pipeline.py`

### 🐘 Base de données
- PostgreSQL déployée sur le cloud via Render
- Accès sécurisé via variables d’environnement

### 📊 Visualisation
- Dashboard interactif Power BI
- Deux pages principales :
  - Vue générale (chiffre d’affaires, panier moyen, etc.)
  - Analyse client (par genre, segment, ville, etc.)
  - Analyse produits (type de produits etc.)

### ⚙️ CI/CD
- GitHub Actions exécute automatiquement le pipeline à chaque `push` ou `pull request`
- Pipeline Dockerisé et testé dans un environnement PostgreSQL temporaire

---

## Galerie

Voici un aperçu des visualisations Power BI :

<p align="center">
  <img src="images/powerbi_main.png" alt="Image Main" width="500">
</p>

<p align="center">
  <img src="images/powerbi_client.png" alt="Image Client" width="500">
</p>
