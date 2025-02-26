from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Store user data in memory
data_store = []

# Fetch service B endpoint from environment variables
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://responder-service:5000")

@app.route("/data", methods=["POST"])
def store_data():
    """
    Stores JSON data sent via POST request.
    """
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    data_store.append(data)
    return jsonify({"message": "Data stored successfully in Service A", "stored_data": data}), 201

@app.route("/", methods=["GET"])
def get_combined_data():
    """
    Fetch stored data from both Service A and Service B.
    """
    try:
        response = requests.get(f"{SERVICE_B_URL}/data")
        service_b_data = response.json().get("stored_data", [])
    except Exception as e:
        service_b_data = {"error": f"Failed to reach Service B: {str(e)}"}

    return jsonify({
        "caller_service_data": data_store,
        "responder_service_data": service_b_data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
