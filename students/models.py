#coding: utf-8
from django.db import models

class Student(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=50)
    avatar = models.CharField(verbose_name=u'头像', max_length=255)
    playing = models.BooleanField(verbose_name=u'是否在表演', editable=False, default=False)
