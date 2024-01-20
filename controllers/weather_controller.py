from controllers.base_controller import BaseController
from models.weather import Weather


class WeatherController(BaseController):

    def GET(self, http):

        weather = Weather()
        weatherData = weather.getWeatherData()

        f = open("views/weather.html", "r")
        html = f.read().format(city=weatherData["name"],
                               temp=weatherData["main"]["temp"])

        http.send_response(200)
        http.end_headers()
        http.wfile.write(html.encode('utf-8'))

    def POST(self, http):
        http.send_response(200)
        http.end_headers()
        http.wfile.write(b'Hello, World post!')
