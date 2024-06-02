from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    user = request.get_json()
    # Add user registration logic
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    # Add user login logic
    access_token = create_access_token(identity=user['username'])
    return jsonify(access_token=access_token), 200

@auth_bp.route('/2fa', methods=['POST'])
def two_factor_auth():
    # Add 2FA logic
    return jsonify({"message": "2FA success"}), 200
