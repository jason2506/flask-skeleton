# -*- coding: utf-8 -*-

# Basic Settings
DEBUG = True
SECRET_KEY = 'SECRET_KEY'  # TODO

# Flask-Assets Settings
ASSETS_DEBUG = DEBUG

# Flask-WTF Settings
WTF_CSRF_SECRET_KEY = 'WTF_CSRF_SECRET_KEY'  # TODO

# Flask-SQLAlchemy Settings
SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp.db'  # TODO

# Flask-User Settings
USER_ENABLE_USERNAME = False  # use email as username
USER_ENABLE_CHANGE_USERNAME = False
USER_ENABLE_CONFIRM_EMAIL = False
USER_ENABLE_LOGIN_WITHOUT_CONFIRM = False
