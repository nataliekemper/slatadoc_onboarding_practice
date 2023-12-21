from django.db import models

# Create your models here.

class UserProfile(models.Model):
    country = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    #phonenumber = models.CharField(max_length=50, blank=True)