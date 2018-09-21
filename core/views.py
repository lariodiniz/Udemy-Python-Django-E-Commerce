#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView

from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


def contact(request):
    sucess = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucess = True

    context = {
        'form': form,
        'success': sucess
    }
    return render(request, 'contact.html', context)
