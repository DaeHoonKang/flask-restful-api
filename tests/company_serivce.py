# -*- coding: utf-8 -*-
import unittest
from app import create_app
import json
from http import HTTPStatus
from db.company import Company


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

    def test_put_tag(self):
        print("===========================================")
        response = self.app.post('/company/tag', data=json.dumps({"company": "원티드랩", "tag": "태그6"}), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("put : 태그_6")
        res_data = json.loads(response.get_data().decode())
        count = Company.objects(name="원티드랩").count()
        self.assertEqual(res_data['count'], count)

    def test_delete_tag(self):
        print("===========================================")
        response = self.app.delete('/company/tag', data=json.dumps({"company": "원티드랩", "tag": "태그6"}), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("delete : 태그_6")
        res_data = json.loads(response.get_data().decode())
        companies = Company.objects(name="원티드랩")
        self.assertEqual(res_data['count'], companies.count())
        for company in companies:
            print("name: {}, tags: {}".format(company.name, company.tags))


if __name__ == '__main__':
    unittest.main()