import requests
import json

response = requests.get('http://ip-api.com/json')
location = json.loads(response.content)

def return_current_timezone():
    return location['timezone']

print(return_current_timezone())