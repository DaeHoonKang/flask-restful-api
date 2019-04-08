# -*- coding: utf-8 -*-
import unittest
from app import create_app
import json
from http import HTTPStatus
import itertools


class CompanyServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

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


if __name__ == '__main__':
    unittest.main()