class HttpServer:
    def __init__(self, app, ip_address, http_port):
        self.app = app
        self.ip_address = ip_address
        self.http_port = http_port

    def start(self):
        self.app.run(host=self.ip_address, port=self.http_port)
