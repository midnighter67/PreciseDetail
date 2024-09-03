from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estimate', views.estimate, name='estimate'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
]
