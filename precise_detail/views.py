from django.shortcuts import render, redirect
from .forms import EstimateForm
from .models import Estimate
from smtplib import SMTPException
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})

def estimate(request):
    """ Process form data and send alert email  """
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = EstimateForm(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                first = request.POST['first']
                last = request.POST['last']
                email = request.POST['email']
                phone = request.POST['phone']
                address = request.POST['address']
                city = request.POST['city']
                zip = request.POST['zip']
                bed = request.POST['bed']
                bath = request.POST['bath']
                sqft = request.POST['sqft']
                pets = request.POST['pets']
                frequency = request.POST['frequency']
                msg = "User info:" + "\n" + \
                    "name:  " + last + ', ' + first + "\n"  + \
                    "email:  " + email + "\n" + \
                    "phone:  " + phone + "\n" + \
                    "address:  " + address + "\n" + \
                    "city:  " + city + "\n" + \
                    "zip:  " + zip + "\n" + \
                    "bedrooms:  " + bed + "\n" + \
                    "bathrooms:  " + bath + "\n" + \
                    "area:  " + sqft + "\n" + \
                    "pets:  " + pets + "\n" + \
                    "frequency:  " + frequency
                            
                send_mail(
                    "Precise Detail Estimate Request",
                    msg,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except SMTPException as e:
                print(e)
                messages.success(request, ('Submit failed'))
                return redirect(url)
            data = Estimate()
            data.first = form.cleaned_data.get('first') #['first']
            data.last = form.cleaned_data.get('last') #['last']
            data.email = form.cleaned_data.get('email') #['email']
            data.phone = form.cleaned_data.get('phone') #['phone']
            data.address = form.cleaned_data.get('address') #['address']
            data.city = form.cleaned_data.get('city') #['city']
            data.zip = form.cleaned_data.get('zip') #['zip']
            data.bed = form.cleaned_data.get('bed') #['bed']
            data.bath = form.cleaned_data.get('bath') #['bath']
            data.sqft = form.cleaned_data.get('sqft') #['sqft']
            data.pets = form.cleaned_data.get('pets') #['pets']
            data.frequency = form.cleaned_data.get('frequency') #['frequency']
            data.save()
            messages.success(request, ('estimate data saved'))
            
        else:
            print("form is invalid")
            messages.success(request, ('Missing required fields'))        
            return render(request, 'estimate.html', {})
    else:
        return render(request, 'estimate.html', {})
        
    return render(request, 'estimate.html', {})

def about(request):
    """ Form for quote request  """
    return render(request, 'about.html', {})

def services(request):
    """ Form for quote request  """
    return render(request, 'services.html', {})
