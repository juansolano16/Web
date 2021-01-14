# app_mail/tasks.py
from config.celery import app


@app.task
def prueba_suma(x, y):
    return x + y


@app.task
def prueba_resta(x, y):
    return x - y