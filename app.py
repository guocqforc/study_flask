from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/name/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/ab')
def get_user():
    abort(404)

@app.route('/li')
def render_li():
    return render_template('macro_tmp.html',list=['abc','def','gkl'])

@app.route('/base')
def base():
    return render_template('super_base.html')

if __name__ == '__main__':
    manager.run()
