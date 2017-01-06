from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello wordl~'

@app.route('/name/<name>')
def user(name):
    return 'hello %s' %(name)

if __name__ == '__main__':
    app.run()
