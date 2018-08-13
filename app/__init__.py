from flask import Flask
from flask_restful import Api
from app.resources.home import HomeResource
from app.resources.host import HostResource


def create_app(config_file=None, testing=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file)
    app.testing = testing

    # TODO: This api stuff needs to be refactored somewhere else without
    # breaking tests
    # https://github.com/flask-restful/flask-restful/issues/357
    api = Api()
    api.add_resource(HomeResource, '/', '/home', '/index')
    api.add_resource(HostResource, '/hosts')

    from app.database import db
    db.init_app(app)

    api.init_app(app)
    return app
