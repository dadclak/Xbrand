from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    return render(request, 'xbrand/index.html', {'banners': banner})

def product(request, pk, kind):
    if kind == 'women':     
        product = get_object_or_404(WomenProduct, pk=pk)
    elif kind == 'men':
        product = get_object_or_404(MenProduct, pk=pk)
    elif kind == 'bag':
        product = get_object_or_404(BagProduct, pk=pk)
    return render(request, 'xbrand/product.html', {'product': product})

def men(request):
    newProducts = MenProduct.objects.filter(date_created__range=[datetime.now() - timedelta(days=7), datetime.now()])
    products = MenProduct.objects.all()
    banner = Banner.objects.all()
    return render(request, 'xbrand/men.html', {'products': products, 'news': newProducts, 'banners': banner})

def women(request):
    newProducts = WomenProduct.objects.filter(date_created__range=[datetime.now() - timedelta(days=7), datetime.now()])
    products = WomenProduct.objects.all()
    banner = Banner.objects.all() 
    return render(request, 'xbrand/women.html', {'products': products, 'news': newProducts, 'banners': banner})

def jewelry(request):
    newProducts = BagProduct.objects.filter(date_created__range=[datetime.now() - timedelta(days=7), datetime.now()])
    products = BagProduct.objects.all()
    banner = Banner.objects.all() 
    return render(request, 'xbrand/bag.html', {'products': products, 'news': newProducts, 'banners': banner})

def contact(request):
    return render(request, 'xbrand/contact.html')