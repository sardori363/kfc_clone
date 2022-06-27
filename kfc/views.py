from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class Home(ListView):
    model = Products
    template_name = 'kfc/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        products = Products.objects.all()
        context['cats'] = cats
        context['pros'] = products
        return context