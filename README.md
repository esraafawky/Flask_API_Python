# Iris Prediction API & Streamlit UI

This project uses a machine learning model to classify Iris flower species using a REST API built with Flask and a user interface built with Streamlit.

## 🚀 Features
- Predict Iris flower species (Setosa, Versicolor, Virginica)
- REST API using Flask
- Dockerized for portability
- Web interface with Streamlit

## 🐳 Run with Docker
```bash
docker build -t iris-api .
docker run -p 5000:5000 iris-api

