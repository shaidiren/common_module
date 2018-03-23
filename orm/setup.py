# coding: utf-8

import sys, os
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'base', 'site-packages')))

import django
from django.conf import settings as django_settings

from django_setting import settings


def setup_django_orm(*app_name):
    """启用django ORM
    :param app_name: 需要安装到django中的app列表
    :return:
    """
    if not django_settings.configured:
        if app_name:
            settings.setdefault('INSTALLED_APPS', []).extend(app_name)
        django_settings.configure(**settings)
        django.setup()

