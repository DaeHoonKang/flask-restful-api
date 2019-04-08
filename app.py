# -*- coding: utf-8 -*-
from mongoengine import *
from flask import Flask
from service.version import version_service
from service.company import company_service



# global flask app
app = Flask(__name__)
# register version service
app.register_blueprint(version_service)
# register company service
app.register_blueprint(company_service)


if __name__ == "__main__":
    app.run()