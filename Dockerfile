# --------------------------------------------------
# Étape 1 : Utiliser une image de base avec Python
# --------------------------------------------------
    FROM python:3.10-slim

    # --------------------------------------------------
    # Étape 2 : Définir le répertoire de travail dans le conteneur
    # --------------------------------------------------
    WORKDIR /app
    
    # --------------------------------------------------
    # Étape 3 : Copier les fichiers nécessaires dans le conteneur
    # --------------------------------------------------
    # On copie uniquement les fichiers essentiels d'abord
    COPY requirements.txt .
    
    # --------------------------------------------------
    # Étape 4 : Installer les dépendances du projet
    # --------------------------------------------------
    RUN pip install --no-cache-dir -r requirements.txt
    
    # --------------------------------------------------
    # Étape 5 : Copier le reste des fichiers de l'application
    # --------------------------------------------------
    COPY . .
    
    # --------------------------------------------------
    # Étape 6 : Exposer le port utilisé par Flask
    # --------------------------------------------------
    EXPOSE 5000
    
    # --------------------------------------------------
    # Étape 7 : Définir la commande à exécuter au démarrage du conteneur
    # --------------------------------------------------
    CMD ["python", "app.py"]
    