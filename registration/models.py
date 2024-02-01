from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
COUNTRY_LIST = [
    ('Not Applicable', 'Not Applicable'),
    ('United States', 'United States'),
    ('Georgia', 'Georgia'),
]

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
        


class UserManager(BaseUserManager):

    def create_user(self, email, password = None, country = None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")

        # ensures a default country is set if none is specified (i.e. superusers)
        if country is None:
            print("Country is none")
            country = Country.objects.get(name="Not Applicable")
            print(country)
        
        email = self.normalize_email(email)
        user = self.model(email=email, country=country, **extra_fields)
        print("Country ID before saving user:", user.country.country_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)



class UserProfile(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    preferred_name = models.CharField(max_length=200, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser
    # phonenumber = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email



# default customer with set fields
class Customer(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=50, blank=True)

    # billing address information
    billing_address_line1 = models.CharField(max_length=200)
    billing_address_line2 = models.CharField(max_length=200, blank=True)
    billing_city = models.CharField(max_length=100)
    billing_state_region = models.CharField(max_length=100)
    billing_zip_code = models.CharField(max_length=20)
    billing_country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Georgia_Customer(models.Model):
    # georgia specific fields
    tax_id = models.CharField(max_length=11, unique=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)