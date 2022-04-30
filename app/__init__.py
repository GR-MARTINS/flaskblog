from flask import Flask
from app.ext import dynaconf


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)
    return app
