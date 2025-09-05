import requests
import json

def get_coordinates(city_name):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 10, "language": "en"}

    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        if not results:
            print("❌ No matching cities found.")
            return None, None

        print("\n🔍 Multiple matches found:")
        for i, result in enumerate(results):
            name = result.get("name", "Unknown")
            state = result.get("admin1", "Unknown")
            country = result.get("country", "Unknown")
            print(f"{i + 1}. {name}, {state}, {country}")

        try:
            choice = int(input("\n👉 Enter the number of the correct location: "))
            selected = results[choice - 1]
            lat = selected["latitude"]
            lon = selected["longitude"]
            print(f"\n✅ You selected: {selected['name']}, {selected['admin1']}, {selected['country']}")
            return lat, lon
        except (ValueError, IndexError):
            print("❌ Invalid selection.")
            return None, None
    else:
        print(f"❌ Geocoding failed. Status code: {response.status_code}")
        return None, None

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "temperature_unit": "fahrenheit",
        "windspeed_unit": "mph"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data.get("current_weather", {})
        print(f"\n🌍 Location: ({lat}, {lon})")
        print(f"🌡️ Temperature: {weather.get('temperature')}°F")
        print(f"💨 Wind Speed: {weather.get('windspeed')} mph")
    else:
        print(f"❌ Failed to fetch weather. Status code: {response.status_code}")

if __name__ == "__main__":
    city = input("🏙️ Enter a city name: ")
    latitude, longitude = get_coordinates(city)
    if latitude and longitude:
        get_weather(latitude, longitude)