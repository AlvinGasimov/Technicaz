from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    
    path('favorites/', favorite_list, name='favorites_list'),
    path('favorites/add/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:product_id>/', remove_from_favorites, name='remove_from_favorites'),

    path('cart/', cart_list, name='cart_list'),
    path('add-to-cart/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:product_id>/', update_cart_quantity, name='update_cart_quantity'),

    path('orders/', orders_list, name='orders_list'),
    path('orders/create/', create_order, name='create_order'),
]