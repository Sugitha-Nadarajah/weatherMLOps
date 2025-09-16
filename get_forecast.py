import requests
from config import API_KEY
from datetime import datetime

BASE_URL = "http://api.weatherapi.com/v1"


def get_today_forecast_filtered():
    """
    Récupère les prévisions météo du jour à partir de l'heure actuelle uniquement.
    """
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q=auto:ip&days=1&aqi=no&alerts=no"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        today = data["forecast"]["forecastday"][0]

        # Heure actuelle locale
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Filtrer les heures >= maintenant
        hourly_forecast = [
            {
                "time": hour["time"],
                "temp_c": hour["temp_c"],
                "condition": hour["condition"]["text"],
                "wind_kph": hour["wind_kph"],
                "humidity": hour["humidity"],
                "chance_of_rain": hour.get("chance_of_rain", "N/A"),
            }
            for hour in today["hour"]
            if hour["time"] >= current_time  # filtre
        ]

        return {
            "location": f"{location}, {country}",
            "date": today["date"],
            "condition": today["day"]["condition"]["text"],
            "temp_min": today["day"]["mintemp_c"],
            "temp_max": today["day"]["maxtemp_c"],
            "rain_chance": today["day"].get("daily_chance_of_rain", "N/A"),
            "hourly": hourly_forecast,
        }

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la météo du jour : {e}")
        return None

