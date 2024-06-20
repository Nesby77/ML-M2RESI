# ML-M2RESI
Examen de fin d'année
# Prédiction de survie du Titanic

Ce projet est une application web basée sur Gradio et FastAPI qui permet de prédire les chances de survie d'un passager lors du naufrage du Titanic en 1912. L'application utilise un modèle de machine learning entraîné sur les données des passagers du Titanic.

## Fonctionnalités

- Interface utilisateur intuitive créée avec Gradio
- Saisie des caractéristiques du passager (classe, âge, sexe, etc.)
- Prédiction de la survie (0 = Décédé, 1 = Survécu) à l'aide d'un modèle de machine learning
- API FastAPI pour effectuer les prédictions

## Démarrage

1. Clonez le référentiel : `git clone https://github.com/votre-utilisateur/titanic-prediction.git`
2. Installez les dépendances : `pip install -r requirements.txt`
3. Lancez l'application Gradio : `python app.py`
4. Accédez à l'interface web depuis votre navigateur à l'adresse `http://localhost:7860`

## Déploiement

L'application est déployée sur Hugging Face Spaces à l'adresse suivante : https://huggingface.co/spaces/votre-espace/titanic-prediction

## Données

Le modèle a été entraîné sur le célèbre jeu de données du Titanic, disponible sur Kaggle : https://www.kaggle.com/c/titanic

## Licence

Ce projet est sous licence MIT.
