import sys
import requests
import json


APP_ID = r"your_api_key"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python getOpenWeather.py <city_name, 2-letter_country_code>")
        exit()

    location = " ".join(sys.argv[1:])

    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APP_ID}"

    response = requests.get(url)
    response.raise_for_status()

    weather_data = json.loads(response.text)

    w = weather_data["list"]
    print(f"Current weather in {location}:")
    print(f"{w[0]['weather'][0]['main']} - {w[0]['weather'][0]['description']}\n")
    print("Tomorrow:")
    print(f"{w[1]['weather'][0]['main']} - {w[1]['weather'][0]['description']}\n")
    print("Day after tomorrow:")
    print(f"{w[2]['weather'][0]['main']} - {w[2]['weather'][0]['description']}\n")
