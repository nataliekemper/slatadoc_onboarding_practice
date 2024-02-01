from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUpWizard.as_view(), name='signup_wizard1'),
    path('step2/', views.SignUpWizard.as_view(), name='signup_wizard2'),
    path('step3/', views.SignUpWizard.as_view(), name='signup_wizard3'),
    path('signup_success/', views.signup_success, name='signup_success'),
    #path('get_country_fields/', views.get_country_fields, name='get_country_fields'),
]
