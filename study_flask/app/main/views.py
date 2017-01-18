#coding:utf-8
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from flask import session, redirect, url_for
from flask import flash
from flask.ext.migrate import Migrate, MigrateCommand
from . import main

# 这个种写法还不是很适应
from .. import db
from flask.ext.mail import Mail,Message
from threading import Thread

@main.route('/post', methods=['GET', 'POST'])
def index():
    import datetime
    from ..models import User
    from .forms import NameForm
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if name:
            user = User.query.filter_by(username=name).first()
            if user is None:
                db.session.add(User(username=name))
                db.session.commit()
                flash('yo~~send email')
                flash('new user %s'%name)
                # send_mail(os.environ.get('to_mail_name'), 'index_function new user', 'mail/new_user', name=name,
                #           date_time=datetime.datetime.now())
            else:
                flash('old friend!')
            session['name'] = name
        return redirect(url_for('.index'))

    return render_template('user.html', name=session.get('name'),
                           current_now=datetime.datetime.utcnow(), form=form)
