from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<slug:product_slug>/', Product.as_view(), name='product'),
]
