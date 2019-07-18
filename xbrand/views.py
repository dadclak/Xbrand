from django.shortcuts import render
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    return render(request, 'xbrand/index.html')

def product(request):
    return render(request, 'xbrand/product.html')

def men(request):
    return render(request, 'xbrand/men.html')

def women(request):
    newProducts = WomenProduct.objects.filter(date_created = datetime.now() - timedelta(days=7))
    products = WomenProduct.objects.all() 
    return render(request, 'xbrand/women.html', {'products': products})

def jewelry(request):
    return render(request, 'xbrand/bag.html')

def contact(request):
    return render(request, 'xbrand/contact.html')