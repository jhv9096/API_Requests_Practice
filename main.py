import json

import requests

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 40.7128,  # New York City
        "longitude": -74.0060,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Full JSON Response")
        print(json.dumps(data, indent=4))
        # weather = data.get("current_weather", {})
        # print(f"🌤️ Temperature: {weather.get('temperature')}°C")
        # print(f"💨 Wind Speed: {weather.get('windspeed')} km/h")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_weather()