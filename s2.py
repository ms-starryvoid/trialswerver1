from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server 2"

@app.route("/receive_message", methods=["POST"])
def receive_message():
    message = request.json.get("message")
    if not message:
        return jsonify({"error": "Missing message in request body"}), 400

    # Process or store the received message here
    print(f"Received message: {message}")

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="localhost", port=5001)
