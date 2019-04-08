# -*- coding: utf-8 -*-
from flask import Flask
from service.version import version_service


app = Flask(__name__)
app.register_blueprint(version_service)


if __name__ == "__main__":
    app.run()