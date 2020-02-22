from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.conf import settings

class User(AbstractUser):
    is_authenticatedbyp=models.BooleanField(default=True)
    contact = models.CharField(max_length=12)
    Date_of_Birth=models.DateField(null=True)



class missing_obj(models.Model):

    complainant=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    missdate=models.DateField()
    reported_on=models.DateTimeField(auto_now_add=True)
    objectdescription=models.TextField()
    object_name=models.TextField()
    location=models.CharField(max_length=100)


class murder(models.Model):

    complainant=models.ForeignKey(User,on_delete=models.CASCADE)
    reported_on=models.DateTimeField(auto_now_add=True)
    dead_name=models.CharField(max_length=100)
    suspects=models.TextField()
    location=models.CharField(max_length=100)

class miss_person(models.Model):
    complainant=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    missdate=models.DateField()
    reported_on=models.DateTimeField(auto_now_add=True)
    miss_name=models.CharField(max_length=100)
    pdescription=models.TextField()
    last_seen_loc=models.TextField()

class Assault(models.Model):
    complainant=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    reported_on=models.DateTimeField(auto_now_add=True)
    victim_name=models.CharField(max_length=60)
    s_description=models.TextField()
    suspects=models.TextField()
    date_time=models.DateTimeField()
    








