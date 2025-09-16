import requests
from config import API_KEY

BASE_URL = "http://api.weatherapi.com/v1"


def get_forecast_seven_days():
    """
    Prédiction de la météo des 7 prochains jours, avec détails horaires
    """
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q=auto:ip&days=7&aqi=no&alerts=no"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        forecast_days = data["forecast"]["forecastday"]

        forecast = []
        for day in forecast_days:
            # Prévisions par heure
            hourly_forecast = []
            for hour in day["hour"]:
                hourly_forecast.append({
                    "time": hour["time"],                # ex: "2025-09-09 14:00"
                    "temp_c": hour["temp_c"],            # température
                    "condition": hour["condition"]["text"],
                    "wind_kph": hour["wind_kph"],
                    "humidity": hour["humidity"],
                    "chance_of_rain": hour.get("chance_of_rain", "N/A")
                })

            # Résumé du jour + détails horaires
            forecast.append({
                "date": day["date"],
                "condition": day["day"]["condition"]["text"],
                "temp_min": day["day"]["mintemp_c"],
                "temp_max": day["day"]["maxtemp_c"],
                "rain_chance": day["day"].get("daily_chance_of_rain", "N/A"),
                "hourly": hourly_forecast
            })

        return {
            "location": f"{location}, {country}",
            "forecast": forecast
        }

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données météo : {e}")
        return None


def print_today_forecast(forecast_data: dict):
    """
    Affiche uniquement les prévisions météo pour le jour actuel (heure par heure).
    """
    print("=== Prévisions du jour ===")
    print(f"Localisation : {forecast_data['location']}\n")

    # On prend uniquement le premier jour (jour actuel)
    today = forecast_data["forecast"][0]

    print(f"📅 {today['date']} → {today['condition']} "
          f"({today['temp_min']}°C - {today['temp_max']}°C), "
          f"Pluie : {today['rain_chance']}%\n")

    # Affichage horaire
    for hour in today["hourly"]:
        print(f"   ⏰ {hour['time']} | {hour['temp_c']}°C | "
              f"{hour['condition']} | Vent: {hour['wind_kph']} km/h | "
              f"Humidité: {hour['humidity']}% | Pluie: {hour['chance_of_rain']}%")


def print_today_forecast(forecast_data: dict):
    """
    Affiche uniquement les prévisions météo pour le jour actuel (heure par heure).
    """
    print("=== Prévisions du jour ===")
    print(f"Localisation : {forecast_data['location']}\n")

    # On prend uniquement le premier jour (jour actuel)
    today = forecast_data["forecast"][0]

    print(f"📅 {today['date']} → {today['condition']} "
          f"({today['temp_min']}°C - {today['temp_max']}°C), "
          f"Pluie : {today['rain_chance']}%\n")

    # Affichage horaire
    for hour in today["hourly"]:
        print(f"   ⏰ {hour['time']} | {hour['temp_c']}°C | "
              f"{hour['condition']} | Vent: {hour['wind_kph']} km/h | "
              f"Humidité: {hour['humidity']}% | Pluie: {hour['chance_of_rain']}%")
