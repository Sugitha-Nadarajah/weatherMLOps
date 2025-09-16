from get_weather import get_weather_by_ip, parse_weather
from get_forecast import get_forecast_seven_days, print_today_forecast


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
    forecast_data = get_forecast_seven_days()

    if forecast_data:
        print_today_forecast(forecast_data)
    else:
        print("Impossible de récupérer les prévisions.")
