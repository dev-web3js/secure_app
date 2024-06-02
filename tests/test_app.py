import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Secure App API" in response.data

def test_user_post(client):
    response = client.post('/user/johndoe', json={"name": "johndoe"})
    assert response.status_code == 201

def test_user_get(client):
    client.post('/user/johndoe', json={"name": "johndoe"})
    response = client.get('/user/johndoe')
    assert response.status_code == 200
    assert b"johndoe" in response.data

def test_user_not_found(client):
    response = client.get('/user/janedoe')
    assert response.status_code == 404
