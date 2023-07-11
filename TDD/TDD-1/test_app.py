import json
import pytest
from app import app, weather_data


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['city'] == 'San Francisco'
    assert 'temperature' in data
    assert 'weather' in data
    assert data['temperature'] == weather_data['San Francisco']['temperature']
    assert data['weather'] == weather_data['San Francisco']['weather']

    response = client.get('/weather/Seattle')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['city'] == 'Seattle'
    assert 'temperature' in data
    assert 'weather' in data
    assert data['temperature'] == weather_data['Seattle']['temperature']
    assert data['weather'] == weather_data['Seattle']['weather']

    # Add more test cases for other cities


def test_get_weather_invalid_city(client):
    response = client.get('/weather/InvalidCity')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'City not found'
