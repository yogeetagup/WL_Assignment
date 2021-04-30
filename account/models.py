from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True,blank=True)
    login_time= models.DateTimeField(default=timezone.now)




   




   
