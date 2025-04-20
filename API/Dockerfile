# Use official Python image
FROM python:3.11

# Set working directory in container
WORKDIR /app

# Copy contents into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask API
CMD ["python", "Iris_api.py"]

