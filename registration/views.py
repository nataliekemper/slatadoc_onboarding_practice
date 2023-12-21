from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def get_country_fields(request):
    country = request.GET.get('country', 'Default')
    form_fields = render_to_string('registration_form_field.html', {'country': country})
    return HttpResponse(form_fields)