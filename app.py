from flask import Flask, jsonify, request  # Import Flask, jsonify, and request for creating the app, handling requests, and returning JSON responses
from flask_restful import Api, Resource, reqparse  # Import modules from Flask-RESTful for creating the API, resources, and request parsers
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity  # Import JWTManager and decorators for handling JWT authentication
from utils.auth import auth_bp  # Import the authentication blueprint from the utils.auth module
from utils.security import encrypt_data, decrypt_data  # Import utility functions for data encryption and decryption

# Initialize the Flask application
app = Flask(__name__)
# Set the secret key for JWT encryption
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a more secure key
# Initialize Flask-RESTful API and JWT manager
api = Api(app)
jwt = JWTManager(app)

# In-memory data stores for users, products, and orders
users = []
products = []
orders = []

# Set up argument parsers for user, product, and order requests
user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, required=True, help="Name of the user")
user_args.add_argument("password", type=str, required=True, help="Password of the user")

product_args = reqparse.RequestParser()
product_args.add_argument("name", type=str, required=True, help="Name of the product")
product_args.add_argument("price", type=float, required=True, help="Price of the product")

order_args = reqparse.RequestParser()
order_args.add_argument("product_id", type=int, required=True, help="ID of the product to purchase")
order_args.add_argument("quantity", type=int, required=True, help="Quantity to purchase")

# Define the UserResource class to handle user-related requests
class UserResource(Resource):
    @jwt_required()
    def get(self, name):
        """Retrieve user information."""
        # Find the user by name
        user = next((user for user in users if user["name"] == name), None)
        if user:
            return jsonify(decrypt_data(user))  # Return decrypted user data
        return {"message": "User not found"}, 404  # Return error if user not found

    def post(self):
        """Register a new user."""
        args = user_args.parse_args()  # Parse arguments from request
        user = {
            "name": args["name"],
            "password": encrypt_data(args["password"])  # Encrypt the user's password
        }
        # Check if user already exists
        if any(u["name"] == user["name"] for u in users):
            return {"message": "User already exists"}, 400  # Return error if user exists
        users.append(user)  # Add new user to the list
        return user, 201  # Return the newly created user

# Define the ProductResource class to handle product-related requests
class ProductResource(Resource):
    def get(self, product_id):
        """Retrieve product information."""
        # Find the product by ID
        product = next((product for product in products if product["id"] == product_id), None)
        if product:
            return product  # Return product data
        return {"message": "Product not found"}, 404  # Return error if product not found

    @jwt_required()
    def post(self):
        """Create a new product."""
        args = product_args.parse_args()  # Parse arguments from request
        product_id = len(products) + 1  # Generate new product ID
        product = {
            "id": product_id,
            "name": args["name"],
            "price": args["price"]
        }
        products.append(product)  # Add new product to the list
        return product, 201  # Return the newly created product

# Define the OrderResource class to handle order-related requests
class OrderResource(Resource):
    @jwt_required()
    def post(self):
        """Create a new order."""
        args = order_args.parse_args()  # Parse arguments from request
        # Find the product by ID
        product = next((product for product in products if product["id"] == args["product_id"]), None)
        if product is None:
            return {"message": "Product not found"}, 404  # Return error if product not found
        order = {
            "user": get_jwt_identity(),  # Get the current user's identity
            "product_id": args["product_id"],
            "quantity": args["quantity"],
            "total_price": args["quantity"] * product["price"]  # Calculate total price
        }
        orders.append(order)  # Add new order to the list
        return order, 201  # Return the newly created order

# Add the resource routes to the API
api.add_resource(UserResource, "/user")
api.add_resource(ProductResource, "/product")
api.add_resource(OrderResource, "/order")

# Define the index route for the root URL
@app.route('/')
def index():
    """Return a welcome message."""
    return "Welcome to the Secure App API", 200  # Return welcome message

# Register the authentication blueprint
app.register_blueprint(auth_bp)

# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
