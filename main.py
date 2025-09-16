from get_weather import get_weather_by_ip, parse_weather
from get_forecast import get_today_forecast


if __name__ == "__main__":
    
    print("=== Application Météo ===\n")
    print("Affichage de la météo actuelle et des prévisions du jour.\n")
    print("Aujourd'hui :\n")
    
    # --- météo actuelle ---
    raw_data = get_weather_by_ip()
    weather = parse_weather(raw_data)

    if weather:
        print("=== Météo actuelle ===")
        for key, value in weather.items():
            print(f"{key} : {value}")
    else:
        print("Impossible de récupérer la météo actuelle.")

    print("\n")

    # --- prévisions météo du jour ---
    forecast_data = get_today_forecast()

    if forecast_data:
        print(f"=== Prévisions du jour ===\nLocalisation : {forecast_data['location']}\n")
        print(f"📅 {forecast_data['date']} → {forecast_data['condition']} "
              f"({forecast_data['temp_min']}°C - {forecast_data['temp_max']}°C), "
              f"Pluie : {forecast_data['rain_chance']}%\n")

        for hour in forecast_data["hourly"]:
            print(f"   ⏰ {hour['time']} | {hour['temp_c']}°C | "
                  f"{hour['condition']} | Vent: {hour['wind_kph']} km/h | "
                  f"Humidité: {hour['humidity']}% | Pluie: {hour['chance_of_rain']}%")
    else:
        print("Impossible de récupérer les prévisions du jour.")
