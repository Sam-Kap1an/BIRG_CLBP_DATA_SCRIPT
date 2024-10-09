#!/usr/bin/env python3

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the API key (you can store this in environment variables in production)
API_KEY = "440dc1aa436f397a6f07439e21f40b25"


def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return f"Error fetching IP: {e}"

# A simple decorator to check for API key
def require_api_key(f):
    def decorated_function(*args, **kwargs):
        key = request.headers.get('x-api-key')  # Look for the API key in the request headers
        if key and key == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized access"}), 401
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/api/result', methods=['POST'])
@require_api_key
def receive_result():
    data = request.get_json()
    if 'result' in data:
        # Process result here
        return jsonify({"status": "success", "message": "Result received"}), 200
    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == "__main__":
    external_ip = get_external_ip()
    print("External IP Address:", external_ip)
    app.run(host="0.0.0.0", port=8000)
