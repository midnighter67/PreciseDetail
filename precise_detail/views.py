from django.shortcuts import render


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})

def quote(request):
    """ Form for quote request  """
    return render(request, 'quote.html', {})
