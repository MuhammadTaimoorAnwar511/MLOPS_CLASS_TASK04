from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to MongoDB Atlas
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Replace with a valid database name without spaces
db = client['MLOPS_CLASS_ACTIVITY_4']  # Updated database name
collection = db['STUDENT']  # Replace with your collection name

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    collection.insert_one(data)  # Insert data into MongoDB
    return jsonify({"message": "Data stored successfully!"}), 201

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find())
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

