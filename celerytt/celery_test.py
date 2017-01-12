# coding:utf-8

from celeryadd import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/5')


@app.task
def add(x, y):
    return x + y
