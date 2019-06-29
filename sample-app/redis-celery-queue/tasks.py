from celery import Celery
from time import sleep
from random import randint

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def hello(m):
    sleep(randint(0, 2))
    return m
