from modeltranslation.translator import register, TranslationOptions
from .models import Favorite, CartItem, Order, OrderItem

@register(Favorite)
class FavoriteTranslationOptions(TranslationOptions):
    fields = ('product',)

@register(CartItem)
class CartItemTranslationOptions(TranslationOptions):
    fields = ('product',)

@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('status',)

@register(OrderItem)
class OrderItemTranslationOptions(TranslationOptions):
    fields = ('product',)
