# -*- coding: utf-8 -*-
import os


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "app.log",
            "dir": "/log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": { # here you can add specific configuration for other libraries
        "werkzeug": {
            "level": "INFO", # change to "ERROR" if you want to see less logs from flask
            "handlers": ["console", "info_file_handler"],
            "propagate": False # required to avoid double logging
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler"]
    }
}


def validation_check(logging_config):
    handlers = logging_config.get('handlers', None)
    result = [True, '']

    if not handlers:
        return False
    # make directories
    for name, handler in handlers.items():
        dir = handler.get('dir', None)
        if not dir:
            continue
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except Exception as e:
            result[0] = False
            result[1] = str(e)
            break

    return result


