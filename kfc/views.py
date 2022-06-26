from django.shortcuts import render
from django.views.generic.base import View

from .models import *

class HomeView(View):
    def get(self, request):
        products = Products.objects.all()
        return render(request, "kfc/home.html")