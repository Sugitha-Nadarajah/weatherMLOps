import requests

API_KEY="2ed45e3e3ed4443a95f82100250909"
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=auto:ip&aqi=n"

response = requests.get(url)
data = response.json()

#print(data)
print(f"Localisation : {data['location']['name']}")
print(f"Région : {data['location']['region']}")
print(f"Pays : {data['location']['country']}")
print("\n")

print(f"Température : {data['current']['temp_c']}")
print("\n")

print(f"Condition : {data['current']['condition']['text']}")
print("\n")

print(f"Vent 1 : {data['current']['wind_mph']}")
print(f"Vent 2 : {data['current']['wind_kph']}")
print(f"Vent 3 : {data['current']['wind_degree']}")
print(f"Vent 4 : {data['current']['wind_dir']}")
print("\n")

print(f"Pression 1 : {data['current']['pressure_mb']}")
print(f"Pression 2 : {data['current']['pressure_in']}")


#, pressure_mb, pressure_in, precip_mm, precip_in, humidity, cloud, feelslike_c, feelslike_f, windchill_c, windchill_f, heatindex_c, heatindex_f, dewpoint_c, dewpoint_f, vis_km, vis_miles,uv