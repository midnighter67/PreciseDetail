from django.shortcuts import render, redirect
from .forms import EstimateForm
from .models import Estimate
from smtplib import SMTPException
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})

def estimate(request):
    """ Process form data and send alert email  """
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        message_first = request.POST['first']
        message_last = request.POST['last']
        message_email = request.POST['email']
        msg = message_last + ', ' + message_first + "\n\n" + "\n" + message_email
        
        send_mail(
            "Precise Detail Estimate Request",
            msg,
            'chetley3@yahoo.com',
            ['mikewooldridge67@gmail.com'],
            fail_silently=False,
        )
        
        """
        form = EstimateForm(request.POST)
        if form.is_valid():
            print("form is valid")
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
        """
    else:
        return render(request, 'estimate.html', {})
        
    """
    requestor = Estimate.objects.get(id=estimate_id)
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            try:    
                text = form.cleaned_data.get('text') 
                msg = text + "\n\n" + consumer.first + " " + consumer.last + "\n" + consumer.email
                send_mail(
                    "Happy Home Quote Request",
                    msg,
                    'chetley3@yahoo.com',
                    [provider.email],
                    fail_silently=False,
                )
                messages.success(request, ('Request sent successfully!'))
                return redirect(url)
            except SMTPException:
                messages.success(request, ('You must be logged in to get review list'))
                return redirect(url)
        else:
            messages.success(request, ('Submit failed.'))
            return render(request, 'quote.html', {"estimate":provider} )
    else:
        return render(request, 'quote.html', {'consumer':consumer, 'provider': provider} )
    """
    return render(request, 'estimate.html', {})

def about(request):
    """ Form for quote request  """
    return render(request, 'about.html', {})

def services(request):
    """ Form for quote request  """
    return render(request, 'services.html', {})
