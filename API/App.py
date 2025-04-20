import streamlit as st
import requests

st.title("🌸 Iris Flower Predictor")

# User inputs
sepal_length = st.number_input("Sepal Length", min_value=0.0)
sepal_width = st.number_input("Sepal Width", min_value=0.0)
petal_length = st.number_input("Petal Length", min_value=0.0)
petal_width = st.number_input("Petal Width", min_value=0.0)

if st.button("Predict"):
    # Pack the data to send to Flask
    data = {
        "features": [sepal_length, sepal_width, petal_length, petal_width]
    }

    try:
        # Call the Flask API (make sure it's running first!)
        response = requests.post("http://127.0.0.1:5000/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"🌟 Predicted Iris Class: {result['prediction']}")
        else:
            st.error("Prediction failed. Please try again.")
            st.text(response.text)
    except Exception as e:
        st.error(f"API Error: {e}")

