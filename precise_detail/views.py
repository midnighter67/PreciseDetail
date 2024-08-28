from django.shortcuts import render


def home(request):
    """ Initial landing page  """
    return render(request, 'home.html', {})
