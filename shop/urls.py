from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', Shop.as_view(), name='shop'),
    path('search/', Search.as_view(), name='search'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('create/', CreateProduct.as_view(), name='create'),
]

