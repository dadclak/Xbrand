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