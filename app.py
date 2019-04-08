# -*- coding: utf-8 -*-
from mongoengine import *
from flask import Flask
from service.version import version_service
from service.company import company_service
from initialize.log import initialize_logger


def create_app():
    # connect to mongodb
    connect('company', host='127.0.0.1', port=27017)
    # global flask app
    app = Flask(__name__)
    # register version service
    app.register_blueprint(version_service)
    # register company service
    app.register_blueprint(company_service)
    # create file log
    initialize_logger(app, {'debug': True})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)