# coding: utf-8

from __future__ import absolute_import

from celery import Celery

# celery = Celery('tasks', broker='amqp://guest@localhost//', backend='redis://localhost', include=['celery_project.tasks'])
celery = Celery('tasks', include=['celery_project.tasks'])
# 从配置文件中设置celery
celery.config_from_object('celery_project.celeryconfig')

if __name__ == '__main__':
    celery.start()
