# -*- coding: utf-8 -*-
import re
import json
from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from db.company import Company
from flask import current_app as app

company_service = Blueprint('company', __name__, url_prefix='/company')


@company_service.route('/autocomplete', methods=['GET'])
def get_company_name():
    """  AutoComplete Function of company name
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


@company_service.route('/tag', methods=['POST'])
def put_company_tag():
    """
        put tag
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
        data = json.loads(request.data)
        company = data.get('company', None)
        tag = data.get('tag', None)
        if not company or not tag:
            return make_response(
                jsonify({'msg': 'The parameters field(company, tag) is required when calling the api'}),
                HTTPStatus.BAD_REQUEST)
        # find company
        find_company = Company.objects(name=company)
        if not find_company or len(find_company) is 0:
            return make_response(jsonify({'count': 0}), HTTPStatus.OK)
        # update tag
        count = Company.objects(name=company).update(add_to_set__tags=tag)
        if count is 0:
            raise Exception('Failed to Company(name={}).update(add_to_set_tag={})'.format(company, tag))
        return make_response(jsonify({'count': count}), HTTPStatus.OK)
    except Exception as e:
        print(e)
        return make_response('Internal Server Error', HTTPStatus.INTERNAL_SERVER_ERROR)


@company_service.route('/tag', methods=['DELETE'])
def delete_company_tag():
    """
        put tag
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
        data = json.loads(request.data)
        company = data.get('company', None)
        tag = data.get('tag', None)
        if not company or not tag:
            return make_response(
                jsonify({'msg': 'The parameters field(company, tag) is required when calling the api'}),
                HTTPStatus.BAD_REQUEST)
        # find company
        find_company = Company.objects(name=company)
        if not find_company or len(find_company) is 0:
            return make_response(jsonify({'count': 0}), HTTPStatus.OK)
        # update tag
        count = Company.objects(name=company).update(pull__tags=tag)
        if count is 0:
            raise Exception('Failed to Company(name={}).update(pull_tag={})'.format(company, tag))
        return make_response(jsonify({'count': count}), HTTPStatus.OK)
    except Exception as e:
        print(e)
        return make_response('Internal Server Error', HTTPStatus.INTERNAL_SERVER_ERROR)