# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.assets import Environment, Bundle

from .models import db, user_manager
from .views import module

__all__ = ('create_app',)


def _init_db(app):
    """Setup for Flask-SQLAlchemy."""
    db.app = app
    db.init_app(app)


def _init_assets(app):
    """Setup for Flask-Assets."""
    scripts = Bundle('js/script.js',
                     filters='closure_js',
                     output='js/scripts.%(version)s.js')
    styles = Bundle('css/style.css',
                    filters='yui_css',
                    output='css/styles.%(version)s.css')

    env = Environment(app)
    # env.url_expire = True
    env.register('scripts', scripts)
    env.register('styles', styles)


def _init_jinja(app):
    """Setup for Jinja2."""
    pass


def _init_user(app):
    """Setup for Flask-User."""
    user_manager.init_app(app)


def _init_modules(app):
    """Setup for blueprints"""
    app.register_blueprint(module)


def create_app(name=None):
    """Create and initialize app."""
    if name is None:
        name = __name__

    app = Flask(name)
    app.config.from_object('config')

    _init_db(app)
    _init_assets(app)
    _init_jinja(app)
    _init_user(app)
    _init_modules(app)

    return app
