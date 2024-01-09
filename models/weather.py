import urllib.request
import json
from urllib.error import URLError

class Weather: 
    def __init__(self):
        pass

    def getWeatherData(city):
        url = 'https://api.openweathermap.org/data/2.5/weather?appid=03fff98ce1bdd589a513152c4c3b4c61&units=metric?&lang=EN&q=Lithuania'
        try:
            with urllib.request.urlopen(url) as response:
                # Decode and parse JSON response
                data = json.loads(response.read().decode())
                return data
        except URLError as e:
            print(f"Error: {e.reason}")