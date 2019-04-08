# -*- coding: utf-8 -*-
from os.path import dirname, abspath
import unittest
from app import create_app, create_mongo
import json
import yaml
from http import HTTPStatus
from db.company import Company


class PutTagTest(unittest.TestCase):

    def setUp(self):
        path = dirname(dirname(dirname(abspath(__file__))))
        with open('{}/config.yaml'.format(path), 'r') as stream:
            try:
                config = yaml.load(stream, Loader=yaml.FullLoader)
                create_mongo(config)
                self.app = create_app(config).test_client()
            except Exception as e:
                print(e)

    def test_put_tag(self):
        print("===========================================")
        response = self.app.post('/company/tag', data=json.dumps({"company": "원티드랩", "tag": "태그6"}), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("put : 태그_6")
        res_data = json.loads(response.get_data().decode())
        companies = Company.objects(name="원티드랩")
        for company in companies:
            print("name: {}, tags: {}".format(company.name, company.tags))