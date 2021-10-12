from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import files 
from .models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta :
        model = Order
        fields = ['product','order_quantity']
        