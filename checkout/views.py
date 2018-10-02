#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.core.urlresolvers import reverse_lazy
from django.forms import modelformset_factory
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from catalago.models import Product

from .models import CartItem, Order

class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()

        cart_item, created = CartItem.objects.add_item(
                        self.request.session.session_key,
                        product
                        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso.')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso.')   
        return reverse_lazy('checkout:cart_item')

class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_form_set(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=['quantity'], can_delete=True, extra=0
        )

        session_key = self.request.session.session_key
        if session_key: 
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key))                
            else:   
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None)
        else:
            formset = CartItemFormSet(
                queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        contexto = super(CartItemView, self).get_context_data(**kwargs)
        contexto['formset'] = self.get_form_set()

        return contexto
    
    def post(self, request, *args, **kwargs):
        formset = self.get_form_set()
        contexto = self.get_context_data(**kwargs)

        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com seucesso.')
            contexto['formset'] = self.get_form_set(clear=True)

        

        return self.render_to_response(contexto)

class CheckoutView(LoginRequiredMixin, TemplateView):

    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)

            order = Order.objects.create_order(
                user=request.user,
                cart_items=cart_items
            )

        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('checkout:cart_item')
        return super(CheckoutView, self).get(request, *args, **kwargs)

create_cartItem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()
checkout = CheckoutView.as_view()

