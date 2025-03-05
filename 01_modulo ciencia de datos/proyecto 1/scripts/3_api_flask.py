# scripts/3_api_flask.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('./models/modelo_random_forest.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    prediction = model.predict(df)
    return jsonify({'prediccion': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)