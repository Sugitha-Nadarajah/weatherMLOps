import pytest
from weather_application.get_weather import parse_weather

def test_parse_weather_types():
    # Simulation de données comme l'API WeatherAPI
    
    fake_data = {
        "location": {"name": "Paris", "region": "Ile-de-France", "country": "France"},
        "current": {
            "temp_c": 22.5,
            "condition": {"text": "Partly cloudy"}
        }
    }

    result = parse_weather(fake_data)

    # Vérification -> types
    assert isinstance(result["localisation"], str)
    assert isinstance(result["region"], str)
    assert isinstance(result["pays"], str)
    assert isinstance(result["temperature_c"], (int, float))
    assert isinstance(result["condition"], str)



