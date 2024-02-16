from flask import Flask
from flask_cors import CORS

from src.web.routes import invoices_routes
from src.web.server import HttpServer

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(invoices_routes, url_prefix='/api/')

if __name__ == '__main__':
    http_server = HttpServer(app, '0.0.0.0', 8080)
    http_server.start()
