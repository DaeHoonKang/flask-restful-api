# -*- coding: utf-8 -*-
import yaml
import sys
from absl import flags
from mongoengine import *
from flask import Flask
from service.version import version_service
from service.company import company_service


flags.DEFINE_string("config", "config.yaml", "config file")
flags.DEFINE_boolean("debug", False, "if debug is true, flask debug mode on")


def create_app(config):
    # connect to mongodb
    connect(config['mongo']['db'],
            host=config['mongo']['host'],
            port=config['mongo']['port'])
    # global flask app
    app = Flask(__name__)
    # register version service
    app.register_blueprint(version_service)
    # register company service
    app.register_blueprint(company_service)
    return app


if __name__ == "__main__":
    args = flags.FLAGS
    args(sys.argv)

    with open(args.config, 'r') as stream:
        try:
            config = yaml.load(stream)
            app = create_app(config)
            app.run(debug=args.debug,
                    host=config['run']['host'],
                    port=config['run']['port'])
        except yaml.YAMLError as e:
            print(e)
