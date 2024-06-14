# ML-M2RESI
Examen de fin d'année
# Titanic Prediction API

Ce projet utilise FastAPI pour créer une API qui prédit la survie des passagers du Titanic.

## Instructions pour exécuter

1. Ouvrez le fichier `titanic_api.ipynb` dans Google Colab.
2. Exécutez chaque cellule dans l'ordre pour installer les dépendances et démarrer le serveur.
3. Une fois le serveur démarré, vous verrez une URL publique générée par ngrok.
4. Utilisez cette URL pour accéder à l'API et tester les prédictions.

## Exemples de requêtes

- URL de base : `http://<ngrok-url>/`
- Endpoint de prédiction : `http://<ngrok-url>/predict`

### Exemple de requête

```bash
curl -X POST "<ngrok-url>/predict" -H "accept: application/json" -H "Content-Type: application/json" -d '{
  "Pclass": 3,
  "Sex_male": 1,
  "Age": 22.0,
  "Siblings_Spouses_Aboard": 1,
  "Parents_Children_Aboard": 0,
  "Fare": 7.25
}'
