import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather(client):
    # Test the GET route for retrieving weather data of a city
    response = client.get('/weather/San Francisco')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['city'] == 'San Francisco'
    assert 'temperature' in data
    assert 'weather' in data

def test_get_weather_invalid_city(client):
    # Test the GET route for an invalid city
    response = client.get('/weather/InvalidCity')
    assert response.status_code == 404

def test_add_weather(client):
    # Test the POST route for adding weather data
    data = {
        'city': 'London',
        'temperature': 18,
        'weather': 'Cloudy'
    }
    response = client.post('/weather', json=data)
    assert response.status_code == 201

def test_update_weather(client):
    # Test the PUT route for updating weather data
    data = {
        'temperature': 22,
        'weather': 'Sunny'
    }
    response = client.put('/weather/London', json=data)
    assert response.status_code == 200

def test_update_weather_invalid_city(client):
    # Test the PUT route for an invalid city
    data = {
        'temperature': 25,
        'weather': 'Hot'
    }
    response = client.put('/weather/InvalidCity', json=data)
    assert response.status_code == 404

def test_delete_weather(client):
    # Test the DELETE route for deleting weather data
    response = client.delete('/weather/London')
    assert response.status_code == 204

def test_delete_weather_invalid_city(client):
    # Test the DELETE route for an invalid city
    response = client.delete('/weather/InvalidCity')
    assert response.status_code == 404
