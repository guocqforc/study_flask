from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/name/<name>')
def user(name):
    import datetime
    print datetime.datetime.utcnow()
    return render_template('user.html', name=name, current_now=datetime.datetime.utcnow())


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