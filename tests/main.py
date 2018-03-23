# coding: utf-8

from orm.setup import setup_django_orm
setup_django_orm('tests')

import json
import tornado.ioloop
import tornado.web

from tests.models import User
from django.core.management import call_command

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        user_list = User.objects.filter(age__gte=20)
        # print [vars(v) for v in user_list]
        results = []
        if user_list:
            results = [{'name': v.nickname, 'age': v.age} for v in user_list]
        self.write(json.dumps({'user_list': results}))


tornado_settings = {}


def make_app():
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler)],
        **tornado_settings)
    return app

def init_db(db_name):
    call_command('makemigrations')
    call_command('migrate')
    print 'finish init db.'


if __name__ == '__main__':
    # init_db('auth')
    app = make_app()
    app.listen(8888)
    print 'app run on port:8888.'
    tornado.ioloop.IOLoop.current().start()
