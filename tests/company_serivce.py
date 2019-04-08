# -*- coding: utf-8 -*-
import unittest
from app import app
import json


class CompanyServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_autocomplete(self):
        response = self.app.get('/company/autocomplete?input=W')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : W")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=원')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : 원")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?원')
        self.assertEqual(response.status_code, 400)
        print("autocomplete : Input Error")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=株')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : 株")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=씨케')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : 씨케")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=스')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : 스")
        print(json.loads(response.get_data().decode()))

        response = self.app.get('/company/autocomplete?input=ket')
        self.assertEqual(response.status_code, 200)
        print("autocomplete : ket")
        print(json.loads(response.get_data().decode()))


if __name__ == '__main__':
    unittest.main()