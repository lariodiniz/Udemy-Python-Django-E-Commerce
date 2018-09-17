#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Word')