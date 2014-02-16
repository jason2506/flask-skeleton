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
    app.jinja_env.add_extension('jinja2.ext.do')
    app.jinja_env.globals['site_name'] = app.config.get('WEBSITE_NAME', '')
    app.jinja_env.globals['site_meta'] = app.config.get('WEBSITE_META', {})
    app.jinja_env.globals['inherit_site_meta'] = False


def _init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.user_loader(User.get)
    login_manager.login_view = '/login'


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
