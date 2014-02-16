# -*- coding: utf-8 -*-

from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt

__all__ = ('db', 'User')

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

    name = db.Column(
        db.String(32), nullable=False, index=True, unique=True,
        info={'label': 'Username'})
    pwd = db.Column(
        db.String(256), nullable=False,
        info={'label': 'Password'})

    @classmethod
    def login(cls, name, pwd):
        user = cls.query.filter_by(name=name).first()
        if user is None or not sha256_crypt.verify(pwd, user.pwd):
            return None

        return user

    def set_pwd(self, pwd):
        self.pwd = sha256_crypt.encrypt(pwd)
