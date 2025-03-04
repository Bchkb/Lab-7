import requests

def weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    key = "e4f06a140d5c997e5bcd60df238b175d"

    response = requests.post(f"{url}q={city_name}&appid={key}")
    return response.text

city_name = input("Введите город ")
print(weather(city_name))




