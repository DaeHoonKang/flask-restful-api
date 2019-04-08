# -*- coding: utf-8 -*-
from mongoengine import *


class Company(Document):
    """
    collection of company
    """
    name = StringField(required=True, max_length=128)
    tags = ListField(StringField(max_length=20))
    lang = StringField(required=True, max_length=5)
