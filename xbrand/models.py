from django.db import models
from django import forms
from django.conf import settings

# Create your models here.

class WomenProduct(models.Model):

    FRUIT_CHOICES = [
        ('jacket','Jacket'),
        ('pants','Pants'),
        ('t-short','T-short'),
        ('sweatshirt','Sweatshirt'),
        ('dress','Dress'),
        ('shoes','Shoes'),
    ]

    women_product_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    new = models.BooleanField(default=True)
    clothes = forms.CharField(label='What kind of clothes?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        self.date_created = datetime.datetime.now()
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='women/')
    women = models.ForeignKey(WomenProduct, related_name='women', on_delete=models.CASCADE)

class Banner(models.Model):
    title = models.CharField(max_length=50, blank=False)
    tesis = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='banner/', help_text='Banner image', blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

    def __str__(self):
        return self.title