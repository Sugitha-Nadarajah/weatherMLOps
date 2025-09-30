# 1. Choisir une image Python légère
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier les fichiers de dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le reste du projet dans le conteneur
COPY . .

# 5. Définir la commande par défaut
CMD ["python", "main.py"]


# # Construire l'image Docker
# docker build -t weather-app .

# Lancer le conteneur
# docker run -it weather-app