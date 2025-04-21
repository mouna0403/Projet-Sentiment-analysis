# Importation des modules nécessaires
from flask import Flask, request, jsonify  # Flask pour l'API web, request pour récupérer les données entrantes, jsonify pour formater les réponses
import joblib  # Pour charger les fichiers de modèle et de vectorizer sauvegardés

# Chargement du modèle entraîné (logistic regression) et du vectorizer (Tfidf)
model = joblib.load("logistic_model.pkl")  # Chargement du modèle de classification
vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Chargement du vectorizer entraîné sur les textes

# Création de l'application Flask
app = Flask(__name__)

# Définition d'une route pour prédire le sentiment à partir d'un texte
@app.route("/predict", methods=["POST"])



def predict():
    # Récupère les données envoyées sous forme de JSON
    data = request.get_json()

    # Vérifie que la clé "text" est bien présente dans les données reçues
    if "text" not in data:
        return jsonify({"error": "Aucune donnée 'text' reçue"}), 400  # Retourne une erreur 400 si le texte n'est pas fourni

    # Applique le vectorizer (TF-IDF) sur le texte envoyé par l'utilisateur
    vect_text = vectorizer.transform([data["text"]])  # On transforme le texte en vecteur compatible avec le modèle

    # Fait la prédiction avec le modèle chargé
    prediction = model.predict(vect_text)[0]  # On récupère la première (et unique) prédiction

    # Convertit le résultat numérique en un label lisible
    label = "Feedback positive" if prediction == 1 else "Feedback negative"

    # Retourne la prédiction au format JSON
    return jsonify({
        "prediction": int(prediction),  # 0 ou 1
        "label": label  # "positive" ou "negative"
    })

# Démarre le serveur Flask en mode debug
if __name__ == "__main__":
    app.run(debug=True)  # Debug=True => permet le rechargement automatique et l'affichage des erreurs
