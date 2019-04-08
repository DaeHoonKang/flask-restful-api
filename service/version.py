# -*- coding: utf-8 -*-
from http import HTTPStatus
from flask import Blueprint, make_response, jsonify


version_service = Blueprint('version', __name__, url_prefix='/v')


@version_service.route('/', methods=['GET'])
def version():
    return make_response(jsonify({'version': '1.0'}), HTTPStatus.OK)