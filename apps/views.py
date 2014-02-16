# -*- coding: utf-8 -*-

from flask import Blueprint, request, url_for, redirect, render_template
from flask.ext.login import current_user, login_user, logout_user, login_required

from .models import User
from .forms import SigninForm, SignupForm

module = Blueprint('skeleton', __name__)


@module.route('/')
def index():
    return render_template('index.html')


@module.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('.index'))

    form = SigninForm(request.form)
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        return redirect(request.args.get('next') or url_for('.index'))

    return render_template('signin.html', form=form)


@module.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('.index'))

    user = User()
    form = SignupForm(request.form, obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        user.save()
        return redirect(url_for('.index'))

    return render_template('signup.html', form=form)


@module.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('.index'))
