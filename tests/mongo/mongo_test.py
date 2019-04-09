# -*- coding: utf-8 -*-
import yaml
from os.path import dirname, abspath
from db.company import Company
from app import create_mongo
import unittest


class MongoTest(unittest.TestCase):

    def setUp(self):
        path = dirname(dirname(dirname(abspath(__file__))))
        with open('{}/config.yaml'.format(path), 'r') as stream:
            try:
                config = yaml.load(stream, Loader=yaml.FullLoader)
                create_mongo(config)
            except Exception as e:
                print(e)

    def test_company_find(self):
        try:
            companies = Company.objects(name__contains='태').distinct(field='name')
            self.assertFalse(companies, None)
            for company in companies:
                print('{}, {}'.format(company.name, company.tags))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()