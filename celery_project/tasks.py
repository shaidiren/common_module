# coding: utf-8

from __future__ import absolute_import

# from celery import Celery
# celery = Celery('tasks', broker='amqp://guest@localhost//', backend='redis://localhost')

from celery_project.app import celery


@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    # time.sleep(2.0)
    print('mail sent.')


@celery.task
def add(x, y):
    return x + y


import time
@celery.task
def log_test():
    with open('some.log', 'a+') as fh:
        fh.write('hello world%s\n' % (str(int(time.time()))))
