from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Favorite, CartItem, Order, Product, OrderItem
from product.models import *
from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# --------- FAVORITES ---------

# @login_required(login_url='/user/login')
def favorite_list(request):
    if not request.user.is_authenticated:
        return render(request, 'favorites.html', {
            'favorites': [], 
            'message': 'Favoritlərinizi görmək üçün əvvəlcə daxil olun.'
        })
        
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Favorite.objects.get_or_create(user=request.user, product=product)
    
    return redirect(request.META.get('HTTP_REFERER', 'product:products'))

@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    favorite = Favorite.objects.filter(user=request.user, product=product)
    if favorite.exists():
        favorite.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'product:products'))


# --------- CART ---------

@login_required
def cart_list(request):
    cart_items = CartItem.objects.filter(user=request.user, product__isnull=False)

    total_price = 0
    for item in cart_items:
        if item.product.discount_price:
            total_price += item.product.discount_price * item.quantity
        else:
            total_price += item.product.price * item.quantity

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    selected_weight_value = request.POST.get('weight')

    if not selected_weight_value:
        return redirect('product:product_detail', product_slug=product.slug)

    try:
        selected_weight_value = Decimal(selected_weight_value)
        selected_weight = get_object_or_404(Weight, value=selected_weight_value)
    except (InvalidOperation, Weight.DoesNotExist):
        return redirect('product:product_detail', product_slug=product.slug)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        weight=selected_weight
    )

    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1

    cart_item.save()
    return redirect('shop:cart_list')

@login_required
def remove_from_cart(request, product_id, cart_item_id):
    try:
        cart_item = CartItem.objects.get(user=request.user, product_id=product_id, id=cart_item_id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        return redirect('shop:cart_list')
    
    return redirect('shop:cart_list')

@login_required
def update_cart_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    new_quantity = int(request.POST.get('quantity', 1))
    if new_quantity > 0:
        cart_item.quantity = new_quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shop:cart_list')


# --------- ORDERS ---------

@login_required
def orders_list(request):
    user_orders = Order.objects.filter(user=request.user)
    
    return render(request, 'orders.html', {'orders': user_orders})

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items:
        return redirect('shop:cart_list')
    
    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0
    
    for item in cart_items:
        order_item = OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity
        )
        total_price += order_item.total_price
    
    order.total_price = total_price
    order.save()
    cart_items.delete()

    return redirect('shop:orders_list')