import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def fetch_call_details(call_id):
    url = f"https://api.vapi.ai/call/{call_id}"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route("/call-details", methods=["GET"])
def get_call_details():
    call_id = request.args.get("call_id")
    if not call_id:
        return jsonify({"error": "Call ID is required"}), 400
    
    try:
        response = fetch_call_details(call_id)
        print(response)
        summary = response.get("summary")
        analysis = response.get("analysis")
        return jsonify({"analysis": analysis, "summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)