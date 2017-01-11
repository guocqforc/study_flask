# coding:utf-8
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired
from flask import session, redirect, url_for
from flask import flash
from flask.ext.migrate import Migrate, MigrateCommand

from flask.ext.mail import Mail,Message

import os

from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 这个是可选这的 如果你要用到 sqlalchemy的系统事件 可以选着打开
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess string'

#配置邮箱信息
app.config['MAIL_SERVER'] = 'smtp.139.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('mail_name')
app.config['MAIL_PASSWORD'] = os.environ.get('mail_pswd')

# 定义邮件发送的前缀
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasy_amin'
mail = Mail(app)


app.debug = True
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


def send_mail(to, subject, template, **kwargs):
    """
    指定模板时候 不要指定拓展名
    :param to:
    :param subject:
    :param template:
    :param kwargs:
    :return:
    """
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


def make_shell_context():
    """
    为shell命令添加环境的上下文
    :return:
    """
    from model import User, Role
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))


class NameForm(Form):
    name = StringField('what is you name?', validators=[Required()])
    submit = SubmitField('Submit', validators=[])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/name/<name>')
def user(name):
    import datetime
    print datetime.datetime.utcnow()
    return render_template('user.html', name=name, current_now=datetime.datetime.utcnow(), form=NameForm())


@app.route('/post', methods=['GET', 'POST'])
def index():
    import datetime
    from model import User
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
                flash('yo~~')
                flash('new user %s'%name)
            else:
                flash('old friend!')
            session['name'] = name
        return redirect(url_for('index'))

    return render_template('user.html', name=session.get('name'),
                           current_now=datetime.datetime.utcnow(), form=form)


@app.route('/ab')
def get_user():
    abort(404)


@app.route('/li')
def render_li():
    return render_template('macro_tmp.html', list=['abc', 'def', 'gkl'])


@app.route('/base')
def base():
    return render_template('super_base.html')


@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
