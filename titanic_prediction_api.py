# -*- coding: utf-8 -*-
"""Titanic Prediction API.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LI8plf1ij77jYk8LUV0j-jw3ktr3DkCS
"""

!pip install fastapi uvicorn

"""Installer et configurer le token ngrok"""

!pip install pyngrok
!ngrok authtoken 2KEmulzOzABtZxb1pHULmIVC21k_5F4nAYQBQjgHvAz2FgcRx

"""Chargement des données

"""

import pandas as pd
import joblib
# Charger le dataset Titanic
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_data = pd.read_csv(url)

# Afficher les premières lignes du dataset
print(titanic_data.head())

"""Exploration et Préparation des données"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Charger le dataset Titanic
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_data = pd.read_csv(url)

# Analyse des données
print(titanic_data.info())
print(titanic_data.describe())

# Traitement des valeurs manquantes pour 'Age' (si elles existent)
if 'Age' in titanic_data.columns:
    titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Traitement des valeurs manquantes pour 'Embarked' (si elle existe)
if 'Embarked' in titanic_data.columns:
    titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

# Encodage des variables catégorielles (si elles existent)
if 'Sex' in titanic_data.columns:
    titanic_data = pd.get_dummies(titanic_data, columns=['Sex'], drop_first=True)
if 'Embarked' in titanic_data.columns:
    titanic_data = pd.get_dummies(titanic_data, columns=['Embarked'], drop_first=True)

# Suppression des colonnes inutiles (si elles existent)
columns_to_drop = ['Name', 'Ticket', 'Cabin']
for column in columns_to_drop:
    if column in titanic_data.columns:
        titanic_data.drop(column, axis=1, inplace=True)

# Afficher les premières lignes du DataFrame nettoyé
print(titanic_data.head())

"""Modélisation"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Séparation des caractéristiques et de la cible
X = titanic_data.drop('Survived', axis=1)
y = titanic_data['Survived']

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement de différents modèles
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name} Accuracy: {score:.2f}")

    # Enregistrer le modèle
joblib.dump(model, 'titanic_model.pkl')

"""Évaluation des modèles"""

from sklearn.metrics import classification_report, confusion_matrix

# Sélection du meilleur modèle (par exemple, Random Forest)
best_model = models['Random Forest']
y_pred = best_model.predict(X_test)

# Rapport de classification
print(classification_report(y_test, y_pred))

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédiction')
plt.ylabel('Réalité')
plt.show()

"""Déploiement"""

import joblib

# Enregistrer le modèle
joblib.dump(best_model, 'titanic_model.pkl')

"""Créer une API avec FastAPI"""

from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Charger le modèle
model = joblib.load('titanic_model.pkl')

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}

"""Utilisation de ngrok

Mise à jour du schéma de la requête
"""

from pydantic import BaseModel

class Passenger(BaseModel):
    Pclass: int
    Sex_male: int
    Age: float
    Siblings_Spouses_Aboard: int
    Parents_Children_Aboard: int
    Fare: float

@app.post("/predict")
def predict(data: Passenger):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}

!pip install fastapi uvicorn nest-asyncio pyngrok

# Importer les modules nécessaires
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Appliquer nest_asyncio pour éviter les erreurs liées aux boucles d'événements
nest_asyncio.apply()

# Créer une instance FastAPI
app = FastAPI()

# Charger le modèle
model = joblib.load('titanic_model.pkl')

# Classe Pydantic pour le schéma de la requête
class Passenger(BaseModel):
    Pclass: int
    Sex_male: int
    Age: float
    Siblings_Spouses_Aboard: int
    Parents_Children_Aboard: int
    Fare: float

# Route de base pour vérifier le bon fonctionnement
@app.get("/")
def read_root():
    return {"message": "Welcome to the Titanic prediction API!"}

# Route pour les prédictions
@app.post("/predict")
def predict(data: Passenger):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}

# Configurer et démarrer ngrok
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)

# Démarrer le serveur Uvicorn
uvicorn.run(app, host='0.0.0.0', port=8000)