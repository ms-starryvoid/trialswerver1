from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with the URL of server 2
RECEIVER_URL = "http://localhost:5001/receive_message"

@app.route("/")
def home():
    return "Server 1"

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.json.get("message")
    if not message:
        return jsonify({"error": "Missing message in request body"}), 400

    # Send message to server 2
    response = requests.post(RECEIVER_URL, json={"message": message})
    if response.status_code != 200:
        return jsonify({"error": f"Error sending message: {response.text}"}), 500

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
