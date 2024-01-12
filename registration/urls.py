from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('success_view/', views.success_view, name='success'),
    path('get_country_fields/', views.get_country_fields, name='get_country_fields'),
]
