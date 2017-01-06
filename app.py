from flask import Flask
from flask import request
from flask import make_response
from flask import abort
from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True
manager = Manager(app)


@app.route('/')
def hello_world():
    return 'hello wordl~'


@app.route('/name/<name>')
def user(name):
    # user_agent = request.headers.get('User-Agent')
    request = make_response('xxx')
    request.set_cookie('answer', '24')
    return 'hello %s usr-agent ;request_headers %s' % (name,request.headers)


@app.route('/ab')
def get_user():
    abort(404)

if __name__ == '__main__':
    manager.run()
