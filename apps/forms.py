# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory

from .models import db, User

__all__ = ('SigninForm', 'SignupForm')


class _ModelForm(model_form_factory(Form)):
    get_session = db.create_scoped_session


class SigninForm(Form):
    name = TextField('Username', [DataRequired()])
    pwd = PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember me')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        isvalid = super(SigninForm, self).validate()
        if not isvalid:
            return False

        user = User.login(self.name.data, self.pwd.data)
        if user is None:
            self.name.errors.append('Invalid username or password.')
            return False

        self.user = user
        return True


class SignupForm(_ModelForm):
    class Meta:
        model = User
        exclude = ('pwd',)

    raw_pwd = PasswordField('Password', [DataRequired()])
    confirm_pwd = PasswordField('Confirm Password', [DataRequired()])

    def validate(self):
        isvalid = super(SignupForm, self).validate()
        if not isvalid:
            return False

        if self.raw_pwd.data != self.confirm_pwd.data:
            self.raw_pwd.errors.append('Password not matched.')
            return False

        return True

    def populate_obj(self, obj):
        super(SignupForm, self).populate_obj(obj)
        obj.set_pwd(self.raw_pwd.data)
