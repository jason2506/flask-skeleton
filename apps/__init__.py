# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.login import LoginManager

from .models import db, User
from .views import module

__all__ = ('create_app',)


def _init_db(app):
    db.app = app
    db.init_app(app)


def _init_jinja(app):
    pass


def _init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.user_loader(User.get)
    login_manager.login_view = '/signin'


def create_app(name=None):
    if name is None:
        name = __name__

    app = Flask(name)
    app.config.from_object('config')

    _init_db(app)
    _init_jinja(app)
    _init_login(app)

    app.register_blueprint(module)
    return app
