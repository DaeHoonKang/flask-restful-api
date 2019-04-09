# -*- coding: utf-8 -*-
from os.path import dirname, abspath
import urllib.parse
import unittest
from app import create_app, create_mongo
import json
import yaml
from http import HTTPStatus


class AutoCompleteTest(unittest.TestCase):

    def setUp(self):
        path = dirname(dirname(dirname(abspath(__file__))))
        with open('{}/config.yaml'.format(path), 'r') as stream:
            try:
                config = yaml.load(stream, Loader=yaml.FullLoader)
                create_mongo(config)
                self.app = create_app(config).test_client()
            except Exception as e:
                print(e)

    def test_autocomplete(self):
        print('\r\n==== Test AutoComplete ====')
        # 대문자
        response = self.app.get('/company/autocomplete?input=W')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=W')
        print('Response - {}'.format(json.loads(response.get_data().decode())))
        # 일본어+영어
        response = self.app.get('/company/autocomplete?input=社Z')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=社Z')
        print('Response - {}'.format(json.loads(response.get_data().decode())))
        # 없는 영어문자
        response = self.app.get('/company/autocomplete?input=abc')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=abc')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

    def test_bad_request(self):
        print('\r\n==== Test BadRequest ====')
        response = self.app.get('/company/autocomplete?원')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        print('GET - /company/autocomplete?원')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

        response = self.app.get('/company/autocomplete?inputtt=원')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        print('GET - /company/autocomplete?inputtt=원')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

    def test_special_char(self):
        print('\r\n==== Test Special Characters ====')
        # 특수문자-1
        query = urllib.parse.urlencode({'input': '#'})
        response = self.app.get('/company/autocomplete?{}'.format(query))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=#')
        print('Response - {}'.format(json.loads(response.get_data().decode())))
        # 특수문자-2
        query = urllib.parse.urlencode({'input': '.'})
        response = self.app.get('/company/autocomplete?{}'.format(query))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=.')
        print('Response - {}'.format(json.loads(response.get_data().decode())))
        # 특수문자-3
        query = urllib.parse.urlencode({'input': '$'})
        response = self.app.get('/company/autocomplete?{}'.format(query))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/autocomplete?input=$')
        print('Response - {}'.format(json.loads(response.get_data().decode())))