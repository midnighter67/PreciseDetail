from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quote', views.quote, name='quote'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
]
