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
    zip = forms.CharField(required=False, widget=forms.TextInput())
    bed = forms.CharField(required=False, widget= forms.TextInput())
    bath = forms.CharField(required=False, widget= forms.TextInput())
    sqft = forms.CharField(required=False, widget= forms.TextInput())
    pets = forms.CharField(required=False, widget= forms.TextInput())
    frequency = forms.CharField(required=False, widget= forms.TextInput())
    comment = forms.CharField(required=False, widget= forms.Textarea())
    
    """
    def clean_me(self):  # validate name field
        super(EstimateForm, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        zip = self.cleaned_data.get('zip')
        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        sqft = self.cleaned_data.get('sqft')
        pets = self.cleaned_data.get('pets')
        frequency = self.cleaned_data.get('frequency')
        comment = self.cleaned_data.get('comment')
        if (name == ''):
            raise forms.ValidationError('this field is required')
        if (phone == ''):
            raise forms.ValidationError('this field is required')
        if (address == ''):
            raise forms.ValidationError('this field is required')
        return self.cleaned_data
    """
    
        
        
    