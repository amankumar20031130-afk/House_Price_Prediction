# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

if not os.path.exists(MODEL_FILE) or not os.path.exists(PIPELINE_FILE):
    raise FileNotFoundError("Please run your training script to produce model.pkl and pipeline.pkl")

model = joblib.load(MODEL_FILE)
pipeline = joblib.load(PIPELINE_FILE)

EXPECTED_COLS = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "ocean_proximity"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error":"No JSON body sent"}), 400

    # Validate
    missing = [c for c in EXPECTED_COLS if c not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    try:
        numeric_fields = [
            "longitude", "latitude", "housing_median_age", "total_rooms",
            "total_bedrooms", "population", "households", "median_income"
        ]
        row = {}
        for k in EXPECTED_COLS:
            if k in numeric_fields:
                row[k] = float(data[k])
            else:
                row[k] = data[k]
        df = pd.DataFrame([row], columns=EXPECTED_COLS)
    except Exception as e:
        return jsonify({"error": f"Bad input data: {str(e)}"}), 400

    try:
        X_trans = pipeline.transform(df)
        pred = model.predict(X_trans)[0]
        return jsonify({"predicted_price": float(pred)})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    # Get port from environment variable for deployment (default to 5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

