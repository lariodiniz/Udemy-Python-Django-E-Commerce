#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from .models import Category
def categories(request):
    return {
        'categories': Category.objects.all()
    }