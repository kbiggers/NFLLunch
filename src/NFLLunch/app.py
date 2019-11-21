from flask import Flask
from flask_rebar import errors, Rebar
from service import rebar
import sys
import logging


def create_app(name):
    app = Flask(name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    rebar.init_app(app)
    return app


if __name__ == '__main__':
    create_app("NFLLunch").run()
