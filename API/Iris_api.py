from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your model
model = joblib.load('iris_model.pkl')

@app.route("/")
def home():
    return "Iris Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    features = data["features"]  
    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)


