# -*- coding: utf-8 -*-
from os.path import dirname, abspath
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
        print("===========================================")
        response = self.app.get('/company/autocomplete?input=W')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : W")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=원')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : 원")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?원')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        print("autocomplete : Input Error")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=株')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : 株")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=씨케')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : 씨케")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=스')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : 스")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=ket')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("autocomplete : ket")
        print(json.loads(response.get_data().decode()))