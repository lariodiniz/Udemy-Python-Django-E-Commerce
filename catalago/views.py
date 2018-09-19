#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    context = {
        'product_list': Product.objects.all(),
    }
    return render(request, 'catalago/product_list.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalago/category.html', context)

def product(request, slug):
    

    product = Product.objects.get(slug=slug)

    context = {
        'product': product,        
    }
    
    return render(request, 'catalago/product.html', context)
