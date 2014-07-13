#coding: utf-8
from django.db import models

class StudentManager(models.Manager):
    def getPlayingStudent(self):
        data = super(StudentManager, self).get_queryset().filter(playing=True)
        return data[0] if data.exists() else None


class Student(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=50)
    avatar = models.CharField(verbose_name=u'头像', max_length=255)
    playing = models.BooleanField(verbose_name=u'是否在表演', editable=False, default=False)
    objects = StudentManager()


class VoteRecord(models.Model):
    student = models.ForeignKey(Student)
    datetime = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20)
    audience = models.CharField(max_length=50)


LOTTERIES = (
    ('ticket', u'门票'),
    ('ipad-mini', 'iPad mini'),
    ('kindle', 'Kindle'),
    ('misc', u'京东券或话费')
)

class LotteryRecord(models.Model):
    phone = models.CharField(verbose_name=u'手机号码', max_length=255)
    lottery = models.CharField(verbose_name=u'奖品', choices=LOTTERIES, max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    audience = models.CharField(max_length=50)
