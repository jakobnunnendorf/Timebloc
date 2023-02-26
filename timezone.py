import requests
import json

response = requests.get('http://ip-api.com/json')
location = json.loads(response.content)

def return_current_timezone():
    return location['timezone']

import datetime, pytz

def return_current_timezone_utc():
    return datetime.datetime.now(pytz.timezone(return_current_timezone())).strftime('%z')

# print(return_current_timezone())
# print(return_current_timezone_utc())
# print(location)

from geopy.geocoders import Nominatim

coordinates = str(location['lat'])+","+str(location['lon'])
geolocator = Nominatim(user_agent="test")
position = geolocator.reverse(coordinates)
# print(position.address)