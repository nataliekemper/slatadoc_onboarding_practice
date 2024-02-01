from django import forms
from .models import UserProfile, Customer, Georgia_Customer, Country
from formtools.wizard.views import SessionWizardView
from .validators import CustomPasswordValidator

class FirstStepForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country", to_field_name="country_id")
    tax_id = forms.CharField(required=False, label='Tax ID')
    phone_number = forms.CharField(max_length=20, label="Phone Number")
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[CustomPasswordValidator()]
    )

    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'country', 'tax_id', 'phone_number']



class SecondStepForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200)
    preferred_name = forms.CharField(max_length=200, required=False)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'preferred_name']



class ThirdStepForm(forms.ModelForm):
    billing_address_line1 = forms.CharField(max_length=200, label='Address Line 1')
    billing_address_line2 = forms.CharField(max_length=200, required=False, label='Address Line 2')
    billing_city = forms.CharField(max_length=100, label='City')
    billing_state_region = forms.CharField(max_length=100, label='State/Province')
    billing_zip_code = forms.CharField(max_length=20, label='Zip Code')
    billing_country = forms.ModelChoiceField(queryset=Country.objects.all(), label='Country')

    class Meta:
        model = UserProfile
        fields = ['billing_address_line1', 'billing_address_line2', 'billing_city', 
                  'billing_state_region', 'billing_zip_code', 'billing_country']











    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

            # Create customer linked to the user
            customer = Customer.objects.create(
                user_profile=user,
                billing_address_line1=self.cleaned_data["billing_address_line1"],
                billing_address_line2=self.cleaned_data["billing_address_line2"],
                billing_city=self.cleaned_data["billing_city"],
                billing_state_region=self.cleaned_data["billing_state_region"],
                billing_zip_code=self.cleaned_data["billing_zip_code"],
                billing_country=self.cleaned_data["billing_country"]
            )

            # If the user selected Georgia, create a Georgia customer
            if self.cleaned_data["country"] == Country.objects.get(name="Georgia"):
                Georgia_Customer.objects.create(
                    user_profile=user,
                    tax_id=self.cleaned_data["tax_id"],
                )

        return user










#class BaseUserRegistrationForm(forms.ModelForm):
    #country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country", to_field_name="country_id")
    #tax_id = forms.CharField(required=False, label='Tax ID')
    #billing_address_line1 = forms.CharField(max_length=200)
    #billing_address_line2 = forms.CharField(max_length=200, required=False)
    #billing_city = forms.CharField(max_length=100)
    #billing_state_region = forms.CharField(max_length=100)
    #billing_zip_code = forms.CharField(max_length=20)
    #billing_country = forms.ModelChoiceField(queryset=Country.objects.all())


    #class Meta:
        #model = UserProfile
        #fields = ['country', 'full_name', 'email', 'password', 'tax_id']

   #def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

            # Create customer linked to the user
            customer = Customer.objects.create(
                user_profile=user,
                billing_address_line1=self.cleaned_data["billing_address_line1"],
                billing_address_line2=self.cleaned_data["billing_address_line2"],
                billing_city=self.cleaned_data["billing_city"],
                billing_state_region=self.cleaned_data["billing_state_region"],
                billing_zip_code=self.cleaned_data["billing_zip_code"],
                billing_country=self.cleaned_data["billing_country"]
            )

            # If the user selected Georgia, create a Georgia customer
            if self.cleaned_data["country"] == Country.objects.get(name="Georgia"):
                Georgia_Customer.objects.create(
                    user_profile=user,
                    tax_id=self.cleaned_data["tax_id"],
                )

        return user