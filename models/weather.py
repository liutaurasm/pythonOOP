import urllib.request
import json
from urllib.error import URLError


class Weather:
    def __init__(self):
        pass

    def getWeatherData(city):
        baseUrl = 'https://api.openweathermap.org/data/2.5/weather'
        appId = '03fff98ce1bdd589a513152c4c3b4c61'
        lang = 'EN'
        q = 'Lithuania'
        units = 'metric'
        url = f'{baseUrl}?appid={appId}&units={units}?&lang={lang}&q={q}'
        print(url)
        try:
            with urllib.request.urlopen(url) as response:
                # Decode and parse JSON response
                data = json.loads(response.read().decode())
                return data
        except URLError as e:
            print(f"Error: {e.reason}")
