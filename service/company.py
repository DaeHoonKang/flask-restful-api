# -*- coding: utf-8 -*-
from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from db.company import Company
from exceptions.exception import InvalidParams
from utils.functions import json_loads


company_service = Blueprint('company', __name__, url_prefix='/company')


@company_service.route('/autocomplete', methods=['GET'])
def get_company_name():
    """ 회사명 자동완성 검색 """
    input = request.args.get('input')
    if not input:
        raise InvalidParams(reason='The input parameter field is required when calling the api')
    companies = Company.objects(name__contains=input).distinct(field='name')
    return make_response(jsonify({'count': len(companies), 'data': companies}), HTTPStatus.OK)


@company_service.route('/tag', methods=['GET'])
def get_company_tag():
    """ 태그로 회사명 검색 """
    input = request.args.get('input')
    if not input:
        raise InvalidParams(reason='The input parameter field is required when calling the api')
    companies = Company.objects(tags=input).distinct(field='name')
    return make_response(jsonify({'count': len(companies), 'data': companies}), HTTPStatus.OK)


@company_service.route('/tag', methods=['POST'])
def put_company_tag():
    """ 입력한 회사명 정보에 태그 추가 """
    data = json_loads(request.data)
    company = data.get('company', None)
    tag = data.get('tag', None)
    if not company or not tag:
        raise InvalidParams(reason='One or more fields - company or tag - not found in the json data')
    # update tag
    count = Company.objects(name=company).update(add_to_set__tags=tag)
    return make_response(jsonify({'count': count}), HTTPStatus.OK)


@company_service.route('/tag', methods=['DELETE'])
def delete_company_tag():
    """ 입력한 회사명 정보에 태그 삭제 """
    data = json_loads(request.data)
    company = data.get('company', None)
    tag = data.get('tag', None)
    if not company or not tag:
        raise InvalidParams(reason='One or more fields - company or tag - not found in the json data')
    # update tag
    count = Company.objects(name=company).update(pull__tags=tag)
    return make_response(jsonify({'count': count}), HTTPStatus.OK)
