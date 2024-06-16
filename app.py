from flask import Flask
from routes import setup_routes

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        setup_routes(self.app)

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    flask_app = FlaskApp()
    flask_app.run()
