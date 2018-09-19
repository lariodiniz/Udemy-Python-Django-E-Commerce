#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.http import HttpResponse

from catalago.models import Category

def index(request):    
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
