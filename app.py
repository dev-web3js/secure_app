from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from utils.auth import auth_bp
from utils.security import encrypt_data, decrypt_data, validate_input

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a more secure key
api = Api(app)
jwt = JWTManager(app)

users = []

class UserResource(Resource):
    @jwt_required()
    def get(self, name):
        user = next((user for user in users if user["name"] == name), None)
        if user:
            return jsonify(user)
        return jsonify({"message": "User not found"}), 404

    def post(self):
        user = request.get_json()
        if any(u["name"] == user["name"] for u in users):
            return jsonify({"message": "User already exists"}), 400
        users.append(user)
        return jsonify(user), 201

api.add_resource(UserResource, "/user/<string:name>")

@app.route('/')
def index():
    return "Welcome to the Secure App API", 200

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
