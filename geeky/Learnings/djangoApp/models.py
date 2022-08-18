from django.db import models

# Create your models here.

class Student(models.Model):

    stuID = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    marks = models.CharField(max_length=25, default='not available')
