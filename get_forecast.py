import requests
from config import API_KEY

BASE_URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=auto:ip&days=7&aqi=no&alerts=no"

def get_forecast_seven_days():
    """
    Prédiction de la météo des 7 prochains jours
    """
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q=auto:ip&days=7&aqi=no&alerts=no"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lève une erreur si code != 200
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        forecast_days = data["forecast"]["forecastday"]

        forecast = []
        for day in forecast_days:
            forecast.append({
                "date": day["date"],
                "condition": day["day"]["condition"]["text"],
                "temp_min": day["day"]["mintemp_c"],
                "temp_max": day["day"]["maxtemp_c"],
                "rain_chance": day["day"].get("daily_chance_of_rain", "N/A")
            })

        return {
            "location": f"{location}, {country}",
            "forecast": forecast
        }

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données météo : {e}")
        return None