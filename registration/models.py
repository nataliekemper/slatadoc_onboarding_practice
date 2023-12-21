from django.db import models

# Create your models here.

class UserProfile(models.Model):
    country = models.CharField(max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    #phonenumber = models.CharField(max_length=50, blank=True)