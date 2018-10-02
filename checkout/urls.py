#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', 
        views.create_cartItem, 
        name='create_cartitem'),
        url(
        r'^carrinho/$', 
        views.cart_item, 
        name='cart_item'),
        url(
        r'^finalizando/$', 
        views.checkout, 
        name='checkout'),        
]