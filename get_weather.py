import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
#print("Ma clé API est :", API_KEY)


BASE_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=auto:ip&aqi=n"


def get_weather_by_ip():
    """
    Récupère la météo actuelle automatiquement en fonction de l'adresse IP.
    Retourne un dictionnaire si succès, None sinon.
    """
    url = f"{BASE_URL}/current.json?key={API_KEY}&q=auto:ip&aqi=no"
    
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Erreur {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Erreur de connexion : {e}")
        return None



def parse_weather(data: dict) -> dict:
    """
    Transforme la réponse JSON en dictionnaire structuré.
    """
    if not data:
        return {}

    weather_info = {
        "localisation": data["location"]["name"],
        "region": data["location"]["region"],
        "pays": data["location"]["country"],

        "temperature_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],

        "vent_mph": data["current"]["wind_mph"],
        "vent_kph": data["current"]["wind_kph"],
        "vent_degree": data["current"]["wind_degree"],
        "vent_dir": data["current"]["wind_dir"],

        "pression_mb": data["current"]["pressure_mb"],
        "pression_in": data["current"]["pressure_in"]
    }

    return weather_info