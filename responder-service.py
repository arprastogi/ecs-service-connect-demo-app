from flask import Flask, jsonify, request

app = Flask(__name__)

# Store user data in memory
data_store = []

@app.route("/data", methods=["POST"])
def store_data():
    """
    Stores JSON data sent via POST request.
    """
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    data_store.append(data)
    return jsonify({"message": "Data stored successfully in Service B", "stored_data": data}), 201

@app.route("/data", methods=["GET"])
def get_data():
    """
    Returns stored data from Service B.
    """
    return jsonify({"stored_data": data_store})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
