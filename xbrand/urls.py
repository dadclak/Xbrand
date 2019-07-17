from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name="product"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('jewelry/', views.jewelry, name="jewelry"),
    path('contact/', views.contact, name="contact"),
]