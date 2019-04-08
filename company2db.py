# -*- coding: utf-8 -*-
import sys
import csv
from mongoengine import *
from absl import flags
from db.company import Company


flags.DEFINE_string("file", "sample_data/wanted_temp_data.csv",
                    "The file is company data save to mongodb, it have field name and tags")


"""
The connect function must be called first.
Otherwise, the Company object will not work
"""
connect('company', host='127.0.0.1', port=27017)


def write_company(lang, name, tags):
    if not isinstance(tags, tuple):
        raise TypeError('The tags must be a tuple')

    ex_tag = []
    for tag in tags:
        if tag:
            ex_tag.extend(tag.split('|'))

    try:
        company = Company(name=name)
        company.tags = ex_tag
        company.lang = lang
        company.save()
    except Exception as ex:
        print('WRITE TO COMPANY: {}'.format(ex))


if __name__ == "__main__":
    # argument string parsing
    args = flags.FLAGS
    args(sys.argv)

    # try:
    #     # Connect to mongodb
    #     connect('test', host=args.host, port=args.port)
    # except MongoEngineConnectionError as e:
    #     print('CONNECTION ERROR: {}'.format(e))

    try:
        # Read csv file
        with open(args.file, 'r', encoding='UTF-8') as stream:
            csv_stream = csv.DictReader(stream)
            for text in csv_stream:
                company_ko = text.get("company_ko", None)
                if company_ko and len(company_ko) > 0:
                    write_company(lang='KOR',
                                  name=company_ko,
                                  tags=(text.get("tag_ko", None),
                                        text.get("tag_en", None),
                                        text.get("tag_ja", None))
                                  )
                company_en = text.get("company_en", None)
                if company_en and len(company_en) > 0:
                    write_company(lang='ENG',
                                  name=company_en,
                                  tags=(text.get("tag_ko", None),
                                        text.get("tag_en", None),
                                        text.get("tag_ja", None))
                                  )
                company_ja = text.get("company_ja", None)
                if company_ja and len(company_ja) > 0:
                    write_company(lang='JPN',
                                  name=company_ja,
                                  tags=(text.get("tag_ko", None),
                                        text.get("tag_en", None),
                                        text.get("tag_ja", None))
                                  )
            print('Company rows: {}'.format(Company.objects().count()))
    except TypeError as e:
        print('WRITE COMPANY ERROR: {}'.format(e))
    except Exception as e:
        print('CSV READ ERROR: {}'.format(e))




