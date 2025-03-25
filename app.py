import pickle

import numpy as np
from flask import Flask, render_template, request

# Initializing the Flask name and Importing
app = Flask(__name__)

# Loading the trained model
with open("xgb_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Home Route - Input Form to index file
@app.route("/")
def home():
    return render_template("index.html")

# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        systolic_bp = float(request.form["systolic_bp"])
        diastolic_bp = float(request.form["diastolic_bp"])
        cholesterol = float(request.form["cholesterol"])

        input_data = np.array([[age, systolic_bp, diastolic_bp, cholesterol]]) 

        prediction = model.predict(input_data)[0] # passed to the model

        result = "Retinopathy Detected" if prediction == 1 else "No Retinopathy"
        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

# Running the Flask App
if __name__ == "__main__":
    app.run(debug=True)
