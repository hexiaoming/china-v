from django.db import models

# Create your models here.

class Provet(models.Model):
	circle_num = models.CharField(max_length = 3)
	top_num = models.CharField(max_length = 8)
	mobile = models.CharField(max_length = 13)
	timestamp = models.CharField(max_length = 20)

class Mobvet(models.Model):
	mobile = models.CharField(max_length = 13)
	timestamp = models.CharField(max_length = 20)