# ML-M2RESI
Examen de fin d'année
Ce projet est une application web basée sur Gradio et FastAPI qui permet de prédire les chances de survie d'un passager lors du naufrage du Titanic en 1912. L'application utilise un modèle de machine learning entraîné sur les données des passagers du Titanic.

## Fonctionnalités

- Interface utilisateur intuitive créée avec Gradio
- Saisie des caractéristiques du passager (classe, âge, sexe, etc.)
- Prédiction de la survie (0 = Décédé, 1 = Survécu) à l'aide d'un modèle de machine learning
- API FastAPI pour effectuer les prédictions

## Démarrage

1. Clonez le référentiel : `[git clone https://github.com/votre-utilisateur/titanic-prediction.git](https://github.com/Nesby77/ML-M2RESI/blob/Nesby77-patch-1/Titanic_Prediction_API.ipynb)`
2. Installez les dépendances : `pip install -r requirements.txt`
3. Lancez l'application Gradio : `python app.py`
4. Accédez à l'interface web depuis votre navigateur à l'adresse `http://localhost:7860`

## Déploiement

L'application est déployée sur Hugging Face Spaces à l'adresse suivante : https://huggingface.co/spaces/Nestorthera/Titanic-App
