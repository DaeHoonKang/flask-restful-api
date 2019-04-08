# -*- coding: utf-8 -*-
import re
from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from db.company import Company


company_service = Blueprint('company', __name__, url_prefix='/company')


@company_service.route('/autocomplete', methods=['GET'])
def get_company_name():
    """
    AutoComplete Function of company name
    :return:
    status code
        200 :
            json format {'count': ?, 'data': ?}
            count is number
            data is list
        400 :
        500 :
            json format {'msg': ?}
    """
    try:
        input = request.args.get('input')
        if not input:
            return make_response(
                jsonify({'msg': 'The input parameter field is required when calling the api'}),
                HTTPStatus.BAD_REQUEST)
        regex = re.compile(".*{}.*".format(input))
        companies = Company.objects(name=regex).distinct(field='name')
        if not companies:
            return make_response(jsonify({'count': 0, 'data': {}}), HTTPStatus.OK)
        return make_response(jsonify({'count': len(companies), 'data': companies}), HTTPStatus.OK)
    except Exception:
        return make_response('Internal Server Error', HTTPStatus.INTERNAL_SERVER_ERROR)


@company_service.route('/tag', methods=['GET'])
def get_company_tag():
    """
        tag query of company name
        :return:
        status code
            200 :
                json format {'count': ?, 'data': ?}
                count is number
                data is list
            400 :
            500 :
                json format {'msg': ?}
        """
    try:
        input = request.args.get('input')
        if not input:
            return make_response(
                jsonify({'msg': 'The input parameter field is required when calling the api'}),
                HTTPStatus.BAD_REQUEST)
        companies = Company.objects(tags=input).distinct(field='name')
        if not companies:
            return make_response(jsonify({'count': 0, 'data': {}}), HTTPStatus.OK)
        return make_response(jsonify({'count': len(companies), 'data': companies}), HTTPStatus.OK)
    except Exception:
        return make_response('Internal Server Error', HTTPStatus.INTERNAL_SERVER_ERROR)