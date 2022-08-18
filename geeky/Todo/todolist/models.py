from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class  Todo(models.Model):

    choices_Status= [('C','Completed'),('P','Pending')]
    choices_Priority = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]

    title = models.CharField(max_length=70)
    status = models.CharField(max_length=2, choices= choices_Status)
    date= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    priority = models.CharField(max_length=2, choices=choices_Priority)