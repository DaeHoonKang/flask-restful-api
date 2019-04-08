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
        print("===========================================")
        response1 = self.app.get('/company/tag?input=태그_3')
        self.assertEqual(response1.status_code, HTTPStatus.OK)
        print("tag : 태그_3")
        print(json.loads(response1.get_data().decode()))

        response2 = self.app.get('/company/tag?input=タグ_3')
        self.assertEqual(response2.status_code, HTTPStatus.OK)
        print("tag : タグ_3")
        print(json.loads(response2.get_data().decode()))

        response3 = self.app.get('/company/tag?input=tag_3')
        self.assertEqual(response3.status_code, HTTPStatus.OK)
        print("tag : tag_3")
        print(json.loads(response3.get_data().decode()))