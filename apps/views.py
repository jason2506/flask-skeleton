# -*- coding: utf-8 -*-

from flask import Blueprint, request, url_for, render_template
from flask.ext.user import login_required, current_user

module = Blueprint('skeleton', __name__)


@module.route('/')
def index():
    return render_template('index.html')
