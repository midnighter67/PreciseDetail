from django.shortcuts import render, redirect
#from .forms import EstimateForm
from smtplib import SMTPException
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})

def estimate(request):
    """ Process form data and send alert email  """
    url = request.META.get('HTTP_REFERER')
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
