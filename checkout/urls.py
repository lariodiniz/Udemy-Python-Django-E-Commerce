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
        url(
        r'^meus-pedidos/$', 
        views.order_list, 
        name='order_list'),
        url(
        r'^meus-pedidos/(?P<pk>\d+)/$', 
        views.order_detail, 
        name='order_detail'),
        url(
        r'^finalizando/(?P<pk>\d+)/pagseguro/$', 
        views.pagseguro, 
        name='pagseguro'),
        url(
        r'^notificacoes/pagseguro/$', 
        views.pagseguro_notification, 
        name='pagseguro_notification'),
          url(
        r'^finalizando/(?P<pk>\d+)/paypal/$', 
        views.paypal, 
        name='paypal'),             
]

