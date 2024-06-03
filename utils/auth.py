
from flask import Blueprint, request, jsonify  # Import necessary modules from Flask for creating blueprints, handling requests, and returning JSON responses
from flask_bcrypt import Bcrypt  # Import Bcrypt for hashing passwords
from flask_jwt_extended import create_access_token  # Import function to create JWT access tokens

bcrypt = Bcrypt()  # Initialize Bcrypt for password hashing

auth_bp = Blueprint('auth', __name__)  # Create a new blueprint for authentication routes

users = []  # In-memory list to store user data

@auth_bp.route('/register', methods=['POST'])  # Define a route for user registration
def register():
    data = request.get_json()  # Get the JSON data from the request
    username = data.get('username')  # Extract the username from the data
    password = data.get('password')  # Extract the password from the data

    # Check if the username already exists in the users list
    if any(u['username'] == username for u in users):
        return jsonify({"message": "User already exists"}), 400  # Return an error message if the user exists

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  # Hash the password
    users.append({"username": username, "password": hashed_password})  # Add the new user to the users list
    return jsonify({"message": "User registered successfully"}), 201  # Return a success message

@auth_bp.route('/login', methods=['POST'])  # Define a route for user login
def login():
    data = request.get_json()  # Get the JSON data from the request
    username = data.get('username')  # Extract the username from the data
    password = data.get('password')  # Extract the password from the data

    user = next((u for u in users if u['username'] == username), None)  # Find the user in the users list
    # Check if the user exists and the password is correct
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)  # Create a JWT access token
        return jsonify(access_token=access_token), 200  # Return the access token

    return jsonify({"message": "Invalid credentials"}), 401  # Return an error message if the credentials are invalid
