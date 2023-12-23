from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    username = None
    country = models.CharField(max_length=50, default="Default")
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    # phonenumber = models.CharField(max_length=50, blank=True)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# class Country(model.Model):
    # name = models.Charfield(max_length=100)

# create a few country specific customer models that will be linked to user profile model

    class georgia_customer(AbstractUser):
        tax_id = models.IntegerField(max_length=9, unique=True)

    