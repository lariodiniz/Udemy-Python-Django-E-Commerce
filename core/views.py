#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    texts = ['Lorem ipsum dolor sit amet', 
             'consectetur adipisicing elit',
             'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    return render(request, 'product_list.html')

def product(request):
    return render(request, 'product.html')