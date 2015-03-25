# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory

from .models import db

__all__ = ()


class _ModelForm(model_form_factory(Form)):
    get_session = db.create_scoped_session
