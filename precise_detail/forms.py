from django import forms
from django.db import models
from .models import Estimate
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm



class EstimateForm(models.Model):
    class Meta:
        model = Estimate
        fields = ('first', 'last', 'email', 'phone', 'address', 'city', 'zip', 'bed', 'bath', 'sqft', 'pets', 'frequency')
        
    