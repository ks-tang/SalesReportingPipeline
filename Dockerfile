# Utiliser une image Python
FROM python:3.13.2

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY ./etl ./etl
COPY ./data ./data
COPY requirements.txt .
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut (modifiable selon les besoins)
CMD ["python", "etl/run_pipeline.py"]

# docker build -t sales-reporting-image .
# docker run --env-file .env --name sales-reporting-container sales-reporting-image 