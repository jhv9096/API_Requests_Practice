import requests
import json

def get_coordinates(city_name):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}

    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results")
        if results:
            lat = results[0]["latitude"]
            lon = results[0]["longitude"]
            return lat, lon
        else:
            print("❌ City not found.")
            return None, None
    else:
        print(f"❌ Geocoding failed. Status code: {response.status_code}")
        return None, None

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data.get("current_weather", {})
        print(f"\n🌍 Location: ({lat}, {lon})")
        print(f"🌡️ Temperature: {weather.get('temperature')}°C")
        print(f"💨 Wind Speed: {weather.get('windspeed')} km/h")
    else:
        print(f"❌ Failed to fetch weather. Status code: {response.status_code}")

if __name__ == "__main__":
    city = input("🏙️ Enter a city name: ")
    latitude, longitude = get_coordinates(city)
    if latitude and longitude:
        get_weather(latitude, longitude)