from dotenv import load_dotenv
import os
from get_weather import get_weather_by_ip, parse_weather
from get_forecast import get_forecast_seven_days
from config import API_KEY



if __name__ == "__main__":
    
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # --- météo actuelle ---

    raw_data = get_weather_by_ip()
    weather = parse_weather(raw_data)

    if weather:
        for key, value in weather.items():
            print(f"{key} : {value}")
    else:
        print("Impossible de récupérer la météo.")
        

    

    # --- prévisions météo ---
    forecast_data = get_forecast_seven_days()

    if forecast_data:
        print("=== Prévisions 7 jours ===")
        print(f"Localisation : {forecast_data['location']}")
        for day in forecast_data["forecast"]:
            print(
                f"{day['date']} → {day['condition']} "
                f"({day['temp_min']}°C - {day['temp_max']}°C), "
                f"Pluie : {day['rain_chance']}%"
            )
    else:
        print("Impossible de récupérer les prévisions.")