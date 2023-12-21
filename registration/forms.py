from django import forms
from .models import UserProfile

COUNTRY_LIST = {
    ('GE', 'Georgia'),
    ('USA', 'United States of America'),
    ('OTH', 'Other'),
    }

class UserRegistrationForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['email', 'name']