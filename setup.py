

from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.manifold import TSNE
import joblib

# Charge le dataset IMDB complet
dataset = load_dataset("imdb")

# Séparez le dataset en train et test
train_dataset = dataset['train']
test_dataset = dataset['test']


labels_train = pd.Series(train_dataset['label'])


labels_test = pd.Series(test_dataset['label'])



#Appliquer TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)  # Limit to 3000 features
train_tfidf = vectorizer.fit_transform(train_dataset["text"])

test_tfidf = vectorizer.transform(test_dataset["text"])


from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(train_tfidf, labels_train)

train_score = model.score(train_tfidf,labels_train )
print("Train_score: ", train_score)



# Prédictions sur les données de test
y_pred = model.predict(test_tfidf)

# Calcul de l'accuracy
accuracy = accuracy_score(labels_test, y_pred)
print("Test_Accuracy: ", accuracy)

# Rapport de classification
print("Classification Report:")
print(classification_report(labels_test, y_pred))





# Sauvegarde du modèle
joblib.dump(model, "logistic_model.pkl")

# Sauvegarde du vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")