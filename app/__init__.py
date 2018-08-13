from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()
api = Api()


def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file)
    initialize_extensions(app)
    register_api_resources(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    api.init_app(app)


def register_api_resources(app):
    from app.resources.host import Host
    api.add_resource(Host, "/hosts")
