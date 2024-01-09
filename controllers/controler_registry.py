from http.server import BaseHTTPRequestHandler


class ControlerRegistry(BaseHTTPRequestHandler):

    controllers = {}

    def register(self, path, controller):
        self.controllers[path] = controller        

    def do_GET(self):        
        for key, value in self.controllers.items():
            if key == self.path:
                print(value.path)
                value.GET(self)

    def do_POST(self):
        for key, value in self.controllers.items():
            if key == self.path:
                value.POST(self)