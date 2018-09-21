#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

from .forms import ContactForm


User = get_user_model()

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

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()