from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/<str:kind>', views.product, name="product"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('jewelry/', views.jewelry, name="jewelry"),
    path('contact/', views.contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)