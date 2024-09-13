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
                message_first = request.POST['first']
                message_last = request.POST['last']
                message_email = request.POST['email']
                msg = "using precise_detail key" + "\n" + message_last + ', ' + message_first + "\n\n" + "\n" + message_email + "\n" + settings.EMAIL_HOST_USER
                send_mail(
                    "Precise Detail Estimate Request",
                    msg,
                    settings.EMAIL_HOST_USER,
                    ['precise.detail@yahoo.com', 'chetley3@yahoo.com'],
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
