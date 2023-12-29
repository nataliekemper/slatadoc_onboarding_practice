from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # phonenumber = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

# create a few country specific customer models that will be linked to user profile model
class US_Customer(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Georgia_Customer(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # georgia specific fields
    tax_id = models.CharField(max_length=9, unique=True)


class UserModel(BaseUserManager):
    def create_customer(self, email, password = None, country = None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            return ValueError("You must provide a valid E-mail.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_Georgia_customer(self, email, password = None, **tax_id):
        """
        Uses create_customer() to create and save a Georgia User 
        with the given email, password, and tax_id.
        """
        georgia_country = Country.objects.get(name="Georgia")
        georgia_user = self.create_customer(self, email, password = password, country = georgia_country)

        Georgia_Customer.objects.create(user_profile = georgia_user, tax_id = tax_id)
        return georgia_user
        


    