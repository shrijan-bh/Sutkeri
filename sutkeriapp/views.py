from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

