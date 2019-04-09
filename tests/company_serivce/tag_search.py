# -*- coding: utf-8 -*-
from os.path import dirname, abspath
import unittest
from app import create_app, create_mongo
import json
import yaml
from http import HTTPStatus


class TagSearchTest(unittest.TestCase):

    def setUp(self):
        path = dirname(dirname(dirname(abspath(__file__))))
        with open('{}/config.yaml'.format(path), 'r') as stream:
            try:
                config = yaml.load(stream, Loader=yaml.FullLoader)
                create_mongo(config)
                self.app = create_app(config).test_client()
            except Exception as e:
                print(e)

    def test_tag(self):
        print('\r\n==== Test Tag Search ====')
        response = self.app.get('/company/tag?input=태그_3')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/tag?input=태그_3')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

        response = self.app.get('/company/tag?input=タグ_3')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/tag?input=タグ_3')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

        response = self.app.get('/company/tag?input=tag_3')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('GET - /company/tag?input=tag_3')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

    def test_bad_request(self):
        print('\r\n==== Test Bad Request ====')
        response = self.app.get('/company/tag?=태그_3')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        print('GET - /company/tag?=태그_3')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

        response = self.app.get('/company/tag?intputt=태그_3')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        print('GET - /company/tag?intputt=태그_3')
        print('Response - {}'.format(json.loads(response.get_data().decode())))

