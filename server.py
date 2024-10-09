#!/usr/bin/env python3

from flask import Flask, request, jsonify
import requests
import os

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

@app.route('/api/upload', methods=['POST'])
@require_api_key
def upload_file():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    # Read the content of the uploaded file
    content = file.read().decode('utf-8')  # Decode the file content to string

    # Define the local file path where the content will be saved
    local_file_path = file.filename  # Save to the current directory with the original filename

    # Write the content to a local file
    with open(local_file_path, 'w', encoding='utf-8') as local_file:
        local_file.write(content)

    return jsonify({"status": "success", "message": "File received and saved", "content": content}), 200

if __name__ == "__main__":
    external_ip = get_external_ip()
    print("External IP Address:", external_ip)
    app.run(host="0.0.0.0", port=8000)
