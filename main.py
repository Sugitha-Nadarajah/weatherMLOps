from get_weather import get_weather_by_ip, parse_weather

if __name__ == "__main__":
    raw_data = get_weather_by_ip()
    weather = parse_weather(raw_data)

    if weather:
        for key, value in weather.items():
            print(f"{key} : {value}")
    else:
        print("Impossible de récupérer la météo.")
