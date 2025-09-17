import pytest
from weather_application import get_weather

# test CI for get_weather function type

def test_get_weather_type():
    result = get_weather("New York")
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "temperature" in result, "The result should contain 'temperature' key"
    assert "humidity" in result, "The result should contain 'humidity' key"
    assert "description" in result, "The result should contain 'description' key"
    assert isinstance(result["temperature"], (int, float)), "'temperature' should be a number"
    assert isinstance(result["humidity"], (int, float)), "'humidity' should be a number"
    assert isinstance(result["description"], str), "'description' should be a string"
    assert result["description"], "'description' should not be empty"
    assert -50 <= result["temperature"] <= 60, "'temperature' should be within a realistic range"
    assert 0 <= result["humidity"] <= 100, "'humidity' should be between 0 and 100"
    assert result["description"].istitle(), "'description' should be capitalized"
    assert len(result["description"].split()) <= 5, "'description' should be concise"