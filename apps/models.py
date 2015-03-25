# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter

__all__ = ('db', 'User', 'user_manager')

db = SQLAlchemy()


class _CRUDMixin(object):

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    @classmethod
    def get(cls, id):
        if isinstance(id, (int, float)) or \
           (isinstance(id, basestring) and id.isdigit()):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


class User(_CRUDMixin, UserMixin, db.Model):
    __tablename__ = 'user'

    # User authentication information
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(55), nullable=False)
    reset_password_token = db.Column(db.String(100), nullable=False)

    confirmed_at = db.Column(db.DateTime())

    is_enabled = db.Column(
        db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(
        db.String(100), nullable=False, server_default='')
    last_name = db.Column(
        db.String(100), nullable=False, server_default='')

    def is_active(self):
        return self.is_enabled


_db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(_db_adapter)
