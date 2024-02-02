from django.shortcuts import render, redirect
from .forms import FirstStepForm, SecondStepForm, ThirdStepForm
from .models import Country, UserProfile, Customer, Georgia_Customer
from formtools.wizard.views import SessionWizardView
from .validators import CustomPasswordValidator

FORMS = [
("0", FirstStepForm),
("1", SecondStepForm),
("2", ThirdStepForm),
]

TEMPLATES = {
"0": "signup_wizard1.html",
"1": "signup_wizard2.html",
"2": "signup_wizard3.html",
}

class SignUpWizard(SessionWizardView):
    #template_name = 'signup_wizard1.html'
    form_list = [FirstStepForm, SecondStepForm, ThirdStepForm]

    def done(self, form_list, **kwargs):

        for form in form_list:
            print(f"Form errors: {form.errors}")

        data1 = self.get_cleaned_data_for_step('0')
        data2 = self.get_cleaned_data_for_step('1')
        data3 = self.get_cleaned_data_for_step('2')

        all_data = {**data1, **data2, **data3}
        print("All Data: ", all_data)


        # First create a UserProfile
        userprofile = UserProfile.objects.create(
            email = all_data['email'],
            full_name = all_data['full_name'],
            preferred_name = all_data.get('preferred_name', ''),
            password = all_data['password'],
            country = all_data['country'],
            is_active = True
        )

        print("UserProfile created:", userprofile)

        customer = Customer.objects.create(
            user_profile = userprofile,
            phonenumber = all_data['phone_number'],
            billing_address_line1 = all_data['billing_address_line1'],
            billing_address_line2 = all_data.get('billing_address_line2', ''),
            billing_city = all_data['billing_city'],
            billing_state_region = all_data['billing_state_region'],
            billing_zip_code = all_data['billing_zip_code'],
            billing_country = all_data['billing_country']
        )
        print("Customer created:", customer)
        print("billing country", all_data['billing_country'])

        if all_data['country'] == Country.objects.get(name='Georgia'):
            print("Creating Georgian Customer...")
            georgia_customer = Georgia_Customer.objects.create(
                customer = customer,
                user_profile=userprofile,
                tax_id=all_data.get('tax_id', '')
                )
            print("Georgia Customer created: ", georgia_customer)

        return redirect('signup_success')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]



def signup_success(request):
    return render(request, 'signup_success.html')