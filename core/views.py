#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import TemplateView

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
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido.')

    context = {
        'form': form,
        'success': sucess
    }
    return render(request, 'contact.html', context)
