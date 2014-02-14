# -*- coding: utf-8 -*-

DEBUG = True
SECRET_KEY = 'SECRET_KEY'

WTF_CSRF_SECRET_KEY = 'WTF_CSRF_SECRET_KEY'

SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp.db'
SQLALCHEMY_ECHO = True

WEBSITE_NAME = 'Skeleton'
WEBSITE_META = {
    'author': 'Chi-En Wu',
    'description': 'Basic skeleton for flask applications.',
    'keywords': 'flask, skeleton'
}
