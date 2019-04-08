# -*- coding: utf-8 -*-
from http import HTTPStatus


class InvalidParams(Exception):

    def __init__(self, reason, status_code=None):
        Exception.__init__(self)

        self.reason = reason
        self.status_code = HTTPStatus.BAD_REQUEST if not status_code else status_code

    def to_dict(self):
        return {'reason': self.reason}

    def __str__(self):
        return 'code: {}, reason: {}'.format(self.status_code, self.reason)