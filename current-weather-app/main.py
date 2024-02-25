# https://www.weatherapi.com/api-explorer.aspx
# Base URL: http://api.weatherapi.com/v1

# Example request
# http://api.weatherapi.com/v1/current.json?key=[YOUR_API_KEY]&q=new%20orleans

# Docs: https://www.weatherapi.com/docs/

from urllib.request import urlopen
from urllib.parse import urlencode
from json import loads


def get_current_weather(city):
    BASE_URL = "http://api.weatherapi.com/v1"
    endpoint = "/current.json"
    query_params = {
        "key": "c1f7ef615ae14c1b97544910222002",
        "q": city,
    }
    encoded_query_params = urlencode(query_params)

    request_url = f"{BASE_URL}{endpoint}?{encoded_query_params}"
    with urlopen(request_url) as response:
        weather_data = loads(response.read())

    return weather_data["current"]


def display_current_weather(current_weather, city):
    temp = current_weather["temp_f"]
    conditions = current_weather["condition"]["text"]
    wind_speed = current_weather["wind_mph"]

    print(f"***** Current weather for {city} *****")
    print(f"Temperature: {temp}F")
    print(f"Conditions: {conditions}")
    print(f"Wind Speed: {wind_speed} MPH")


options = """
    (1) Get current weather (2) Exit
"""

GET_CURRENT = 1
EXIT = 2

while True:
    user_choice = int(input(options))

    if user_choice == GET_CURRENT:
        city = input("What city would you like the weather for? ")
        current_weather = get_current_weather(city)
        display_current_weather(current_weather, city)
    elif user_choice == EXIT:
        break
