from django import forms
from django.db import models
from .models import Estimate
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


"""
class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ('first', 'last', 'email', 'phone', 'address', 'city', 'zip', 'bed', 'bath', 'sqft', 'pets', 'frequency')
"""

class EstimateForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput())
    email = forms.EmailField(widget= forms.Textarea())
    phone = forms.CharField(widget= forms.TextInput())
    address = forms.CharField(widget= forms.TextInput())
    city = forms.CharField(required=False, widget= forms.TextInput())
    zip = forms.CharField(widget=forms.TextInput())
    bed = forms.CharField(required=False, widget= forms.TextInput())
    bath = forms.CharField(required=False, widget= forms.TextInput())
    sqft = forms.CharField(required=False, widget= forms.TextInput())
    pets = forms.CharField(required=False, widget= forms.TextInput())
    frequency = forms.CharField(required=False, widget= forms.TextInput())
    comment = forms.CharField(required=False, widget= forms.Textarea())
    
    """
    name = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    email = forms.EmailField(widget= forms.Textarea(attrs={"class": "form-control", "rows": "5"}))
    phone = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    address = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    city = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    zip = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    bed = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    bath = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    sqft = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    pets = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    frequency = forms.CharField(widget= forms.TexTextInputarea(attrs={"class": "form-control", "rows": "5"}))
    comment = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "rows": "5"}))
    """
        
        
    