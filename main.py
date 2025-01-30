# Import Flask for creating the web application and jsonify for returning JSON responses
from flask import Flask, jsonify
# Import Flask-CORS to handle Cross-Origin Resource Sharing (CORS)
from flask_cors import CORS
import os  # Import os to access environment variables
# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

# Configure CORS to allow requests to the "/products" route from any origin
CORS(app, resources={r"/products": {"origins": "*"}})

# Retrieve the PORT value from environment variables, default to 3030 if not set
PORT = int(os.getenv("PORT", 3030))

# Define a route for "/products" that responds to GET requests


@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},  # Product 1: Dog Food
        {"id": 2, "name": "Cat Food", "price": 34.99},  # Product 2: Cat Food
        {"id": 3, "name": "Bird Seeds", "price": 10.99},  # Product 3: Bird Seeds
        {"id": 4, "name": "Tiger Seeds", "price": 50.99}  # Product 4: Tiger Seeds
    ]
    return jsonify(products)  # Return the list of products as a JSON response


# Start the Flask server
if __name__ == '__main__':
    # Run the server on the specified port and listen on all network interfaces
    app.run(host='0.0.0.0', port=PORT)
