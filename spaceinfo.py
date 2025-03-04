import requests
import json

#Сайт open-notify.org

def where_is_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    result = json.loads(response.text)
    
    return result['iss_position']

# print(where_is_iss())

def who_is_in_space():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    result = json.loads(response.text)

    for i in range(len(result['people'])):
        print(i + 1, result['people'][i])

who_is_in_space()