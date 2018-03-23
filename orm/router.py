# coding: utf-8


class AuthRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        # if model._meta.app_label == 'auth':
        #     return 'auth'

        return model._meta.app_label
        # return None

    def db_for_write(self, model, **hints):
        # if model._meta.app_label == 'auth':
        #     return 'auth'
        return model._meta.app_label
        # return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj2._meta.app_label and \
                obj1._meta.app_label == obj2._meta.app_label:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
