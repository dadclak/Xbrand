from django.db import models
from django import forms
from django.conf import settings

# Create your models here.

class WomenProduct(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image_1 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=False)
    image_2 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_3 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_4 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_5 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    new = models.BooleanField(default=True)
    kind = models.CharField(max_length=10, default='jacket, pants, t-short, sweatshirt, dress, shoes', blank=False)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

class MenProduct(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image_1 = models.ImageField(upload_to='men_product', help_text='Men product image', blank=False)
    image_2 = models.ImageField(upload_to='men_product', help_text='Men product image', blank=True)
    image_3 = models.ImageField(upload_to='men_product', help_text='Men product image', blank=True)
    image_4 = models.ImageField(upload_to='men_product', help_text='Men product image', blank=True)
    image_5 = models.ImageField(upload_to='men_product', help_text='Men product image', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    new = models.BooleanField(default=True)
    kind = models.CharField(max_length=10, default='jacket, pants, t-short, sweatshirt, dress, shoes', blank=False)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title


class BagProduct(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image_1 = models.ImageField(upload_to='bag_product', help_text='Bag product image', blank=False)
    image_2 = models.ImageField(upload_to='bag_product', help_text='Bag product image', blank=True)
    image_3 = models.ImageField(upload_to='bag_product', help_text='Bag product image', blank=True)
    image_4 = models.ImageField(upload_to='bag_product', help_text='Bag product image', blank=True)
    image_5 = models.ImageField(upload_to='bag_product', help_text='Bag product image', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    women = models.BooleanField(default=True)
    new = models.BooleanField(default=True)
    kind = models.CharField(max_length=10, default='bag, belt, jewelry', blank=False)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=50, blank=False)
    tesis = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='banner/', help_text='Banner image', blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

    def __str__(self):
        return self.title