# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.gemini_service import generate_json_from_image
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Endpoint to process the uploaded image
@app.route("/process-receipt", methods=["POST"])
def process_receipt():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    try:
        # Process the image file to extract data and generate JSON output
        json_output = generate_json_from_image(file)
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

    return jsonify(json_output)
@app.route("/welcome", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Receipt Reader API!"})
if __name__ == "__main__":
    app.run(debug=True)
