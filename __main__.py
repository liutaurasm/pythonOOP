from http.server import HTTPServer
from controllers.controler_registry import ControlerRegistry
from controllers.weather_controller import WeatherController


ControlerRegistry.register(ControlerRegistry, "/", WeatherController())

# Set the port
port = 8000
# Create an HTTP server instance
httpd = HTTPServer(('localhost', port), ControlerRegistry)

print(f"Server started on localhost:{port}")
httpd.serve_forever()


