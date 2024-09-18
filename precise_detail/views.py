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
    if request.method == "POST":  # if submit button is clicked
        form = EstimateForm(request.POST or None)
        if form.is_valid():
            try: 
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                city = form.cleaned_data['city'] or ""
                zip = form.cleaned_data['zip'] or ""
                bed = form.cleaned_data['bed'] or ""
                bath = form.cleaned_data['bath'] or ""
                sqft = form.cleaned_data['sqft'] or ""
                pets = form.cleaned_data['pets'] or ""
                frequency = form.cleaned_data['frequency'] or ""
                comment = form.cleaned_data['comment'] or ""
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
            form.save()
            
            messages.success(request, ('You\'re estimate request has been sent!'))
            return redirect('home')
        else:
            messages.success(request, ('Missing required fields'))        
            return redirect('estimate')
    else:
        return render(request, 'estimate.html', {})
        

def about(request):

    return render(request, 'about.html', {})

def services(request):

    return render(request, 'services.html', {})
