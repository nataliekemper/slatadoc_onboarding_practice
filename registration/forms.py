from django import forms
from .models import UserProfile, Customer, Georgia_Customer, COUNTRY_LIST

class BaseUserRegistrationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['full_name', 'preferred_name', 'email', 'country', 'password']
        widgets = {
            'country': forms.Select(choices=COUNTRY_LIST),
        }

    def clean_country(self):
        country = self.cleaned_data['country']

        valid_choices = dict(COUNTRY_LIST).keys()
        print(f"Valid country choices: {valid_choices}")

        return country


class BaseCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['billing_address_line1', 'billing_address_line2', 'billing_city', 
                  'billing_state_region', 'billing_zip_code', 'billing_country']


class Georgia_CustomerRegistrationForm(BaseUserRegistrationForm, BaseCustomerForm):
    class Meta(BaseUserRegistrationForm.Meta, BaseCustomerForm.Meta):
        model = Georgia_Customer
        fields = BaseUserRegistrationForm.Meta.fields + ['tax_id']
