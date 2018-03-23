# coding: utf-8


from django.db import models


class BaseModel(models.Model):
    def __init__(self, *args, **kws):
        super(BaseModel, self).__init__(self, *args, **kws)


    def to_json(self):
        pass


class User(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    nickname = models.CharField(db_column='name', max_length=30, default='unknown')
    age = models.IntegerField(db_column='age', default=20)

    class Meta:
        app_label = 'auth'
        db_table = 'admin'
