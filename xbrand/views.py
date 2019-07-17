from django.shortcuts import render
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'xbrand/index.html')

def product(request):
    return render(request, 'xbrand/product.html')

def men(request):
    return render(request, 'xbrand/men.html')

def women(request):
    return render(request, 'xbrand/women.html')

def jewelry(request):
    return render(request, 'xbrand/bag.html')

def contact(request):
    return render(request, 'xbrand/contact.html')