from flask import Flask
from flask_rebar import errors, Rebar
from service import rebar


def create_app(name):
    app = Flask(name)
    rebar.init_app(app)
    return app


if __name__ == '__main__':
    create_app(__name__).run()
