from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Agent is Online and Listening...</h1>"

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    print("Incoming Webhook Signal...")
    # validate data
    if not request.is_json:
        return jsonify({"error": "Payload must be JSON"}), 400

    data = request.get_json()
    # extract info
    sender = data.get("sender", "Unknown")
    action = data.get("action", "ping")

    print(f"Event: {action.upper()}")
    print(f"From: {sender}")
    # agent decision logic
    response_msg = ""
    if action == "alert":
        print("AGENT ACTION: Triggering Red Alert Protocol")
        response_msg = "Red Alert Activated"
    elif action == "greet":
        print("AGENT ACTION: Waving back.")
        response_msg = "Hello there!"
    else:
        print("AGENT ACTION: Logging event.")
        response_msg = "Event Logged"

    return jsonify({"status": "success", "agent_reply": response_msg}), 200

if __name__ == "__main__":

    app.run(port=5000)
