from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', products, name='products'),
    path('<slug:product_slug>/', product_detail, name='product_detail'),
]