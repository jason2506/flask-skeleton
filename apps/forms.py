# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired

from .models import User


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
