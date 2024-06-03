import pytest  # Import pytest for testing
from app import app  # Import the Flask app from the main application module

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:  # Create a test client for the app
        yield client  # Provide the test client to the test functions

def test_user_registration(client):
    """Test the user registration endpoint."""
    response = client.post('/register', json={"username": "testuser", "password": "testpass"})  # Send POST request to /register endpoint
    assert response.status_code == 201  # Assert that the response status code is 201 (Created)
    assert response.get_json()["message"] == "User registered successfully"  # Assert that the response contains the expected message

def test_user_login(client):
    """Test the user login endpoint."""
    client.post('/register', json={"username": "testuser", "password": "testpass"})  # Register a new user
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})  # Send POST request to /login endpoint
    assert response.status_code == 200  # Assert that the response status code is 200 (OK)
    assert "access_token" in response.get_json()  # Assert that the response contains an access token

def test_create_product(client):
    """Test creating a product via the API."""
    client.post('/register', json={"username": "testuser", "password": "testpass"})  # Register a new user
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})  # Log in the user
    token = response.get_json()["access_token"]  # Extract the access token from the login response
    headers = {'Authorization': f'Bearer {token}'}  # Set the authorization header with the token
    response = client.post('/product', json={"name": "testproduct", "price": 10.99}, headers=headers)  # Send POST request to /product endpoint
    assert response.status_code == 201  # Assert that the response status code is 201 (Created)

def test_create_order(client):
    """Test creating an order via the API."""
    client.post('/register', json={"username": "testuser", "password": "testpass"})  # Register a new user
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})  # Log in the user
    token = response.get_json()["access_token"]  # Extract the access token from the login response
    headers = {'Authorization': f'Bearer {token}'}  # Set the authorization header with the token
    client.post('/product', json={"name": "testproduct", "price": 10.99}, headers=headers)  # Create a new product
    response = client.post('/order', json={"product_id": 1, "quantity": 2}, headers=headers)  # Send POST request to /order endpoint
    assert response.status_code == 201  # Assert that the response status code is 201 (Created)
