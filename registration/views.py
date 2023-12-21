from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def register_user(request):
    form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def get_country_fields(request):
    country = request.GET.get('country', 'Default')
    form_fields = render_to_string('registration_form_field.html', {'country': country})
    return HttpResponse(form_fields)