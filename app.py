from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True
manager = Manager(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/name/<name>')
def user(name):
    return render_template('user.html',name=name)


@app.route('/ab')
def get_user():
    abort(404)

if __name__ == '__main__':
    manager.run()
