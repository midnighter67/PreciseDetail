from django.shortcuts import render, redirect
from .forms import EstimateForm
from .models import Estimate
from smtplib import SMTPException
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})

def estimate(request):
    """ Process form data and send alert email  """
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = EstimateForm(request.POST)
        if form.is_valid():
            try: 
                name = form.cleaned_data['name']
                try:
                    email = form.cleaned_data['email']
                except ValidationError:
                    raise form.ValidationError("invalid email")
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                city = form.cleaned_data['city']
                zip = form.cleaned_data['zip']
                bed = form.cleaned_data['bed']
                bath = form.cleaned_data['bath']
                sqft = form.cleaned_data['sqft']
                pets = form.cleaned_data['pets']
                frequency = form.cleaned_data['frequency']
                comment = form.cleaned_data['comment']
                msg = "User info:" + "\n" + \
                    "name:  " + name + "\n"  + \
                    "email:  " + email + "\n" + \
                    "phone:  " + phone + "\n" + \
                    "address:  " + address + "\n" + \
                    "city:  " + city + "\n" + \
                    "zip:  " + zip + "\n" + \
                    "bedrooms:  " + bed + "\n" + \
                    "bathrooms:  " + bath + "\n" + \
                    "area:  " + sqft + "\n" + \
                    "pets:  " + pets + "\n" + \
                    "frequency:  " + frequency + "\n" + \
                    "comment:  " + comment
                send_mail(
                    "Precise Detail Estimate Request",
                    msg,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except SMTPException as e:
                messages.success(request, ('Submit failed'))
                return render(request, 'estimate.html', {'form': form})
            
            data = Estimate()
            data.name = name 
            data.email = email 
            data.phone = phone 
            data.address = address 
            data.city = city 
            data.zip = zip 
            data.bed = bed 
            data.bath = bath 
            data.sqft = sqft 
            data.pets = pets 
            data.frequency = frequency
            data.comment = comment 
            data.save()
            
            messages.success(request, ('request sent'))
        else:
            messages.success(request, ('Missing required fields'))        
            return render(request, 'estimate.html', {'form': form})
    else:
        form = EstimateForm()
        return render(request, 'estimate.html', {'form': form})
        
    return render(request, 'estimate.html', {})

def about(request):

    return render(request, 'about.html', {})

def services(request):

    return render(request, 'services.html', {})
