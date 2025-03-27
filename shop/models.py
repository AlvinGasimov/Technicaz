from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from product.models import *

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')
    created_at_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self):
        product_name = self.product.name if self.product else "No Product"
        return f"{self.user.username} favorited {product_name}"
    
    
class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_carts')
    quantity = models.PositiveIntegerField(default=1)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"

    @property
    def product_price(self):
        if self.product.discount_price:
            return self.product.discount_price
        else:
            return self.product.price

    @property
    def total_price(self):
        if self.product.discount_price:
            return round(self.product.discount_price * self.weight.value, 2)
        return round(self.product.price * self.weight.value, 2)

    @property
    def total_weight(self):
        return self.weight.value * self.quantity if self.weight else 0
  
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.created_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.product:
            return f"{self.product.name} x {self.quantity}"
        return f"Unknown Product x {self.quantity}"