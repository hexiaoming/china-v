from django.db import models

# Create your models here.

class costum_service(models.Model):
	problem_type = models.TextField()
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=30)
	describe = models.TextField()
