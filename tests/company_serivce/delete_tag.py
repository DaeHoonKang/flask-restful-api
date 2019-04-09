# -*- coding: utf-8 -*-
from os.path import dirname, abspath
import unittest
from app import create_app, create_mongo
import json
import yaml
from http import HTTPStatus
from db.company import Company


class DeleteTagTest(unittest.TestCase):

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
        print('\r\n==== Test Delete Tag ====')
        new_tag = '태그_999'
        data = json.dumps({'company': '원티드랩', 'tag': new_tag})
        response = self.app.delete('/company/tag', data=data, content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print('DELETE - /company/tag data={}'.format(data))
        companies = Company.objects(name='원티드랩')
        for company in companies:
            print('{}, {}'.format(company.name, company.tags))
            self.assertEqual(new_tag not in company.tags, True)

    def test_bad_request(self):
        print('\r\n==== Test Put Tag ====')
        new_tag = '태그_999'
        data = {'company': '원티드랩', 'tagggggg': '태그_999'}
        response = self.app.delete('/company/tag', data=data, content_type='application/json')
        print('DELETE - /company/tag data={}'.format(data))
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

        data = {'company': '원티드랩'}
        response = self.app.delete('/company/tag', data=data, content_type='application/json')
        print('DELETE - /company/tag data={}'.format(data))
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
