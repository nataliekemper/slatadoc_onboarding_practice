from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import BaseUserRegistrationForm
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        print(country)

        if country == 'Georgia':
            form = BaseUserRegistrationForm(request.POST)
        else:
            form = BaseUserRegistrationForm(request.POST)

        print("Received data:", request.POST)
        print("Form is valid:", form.is_valid())
        print("Form errors:", form.errors)

        if form.is_valid():
            print('The form is valid')
            user = form.save()
            login(request, user)
            return redirect('success_view')
        else:
            print('The form is not valid. Errors:', form.errors)
    else:
        form = BaseUserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def get_country_fields(request):
    country = request.GET.get('country', 'Default')
    form_fields = render_to_string('registration_form_field.html', {'country': country})
    return HttpResponse(form_fields)