from flask import Flask, request, jsonify
import pickle

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Charger le pipeline complet
with open('pipeline.pickle', 'rb') as f:
    pipeline = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    # Vérifiez que la requête contient l'email
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "Le champ 'email' est requis"}), 400

    try:
        # Utiliser le pipeline pour prédire
        prediction = pipeline.predict([email])
        result = "spam" if prediction[0] == 1 else "non-spam"
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la prédiction : {str(e)}"}), 500

    #return jsonify({"email": email, "prediction": result})
    return result


if __name__ == '__main__':
    app.run()
