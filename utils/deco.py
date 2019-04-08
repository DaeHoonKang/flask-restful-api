# -*- coding: utf-8 -*-
from functools import wraps


def request_log(func):
    @wraps(func)
    def log(*args, **kwargs):
        app.logger.info('{} : {}'.format(request.url, request.remote_addr))
        return func(*args, **kwargs)
    return log
