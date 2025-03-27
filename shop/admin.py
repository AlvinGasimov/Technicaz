from django.contrib import admin
from .models import *
from django.utils import timezone
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

@admin.register(Favorite)
class FavoriteAdmin(TranslationAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')
    
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
@admin.register(CartItem)
class CartItemAdmin(TranslationAdmin):
    list_display = ('user', 'product', 'product_price', 'total_weight', 'total_price', 'get_created_at')
    readonly_fields = ('total_price', 'total_weight')

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d %B %Y')
    get_created_at.short_description = 'Created At'
    
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]
  
    def total_price(self, obj):
        return format_html('<b>{}</b> ₼', obj.total_price)
    total_price.short_description = 'Ümumi Qiymət'
    
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(OrderItem)
class OrderItemAdmin(TranslationAdmin):
    list_display = ('order', 'product', 'quantity', 'total_price')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')
    
    def total_price(self, obj):
        return format_html('<b>{}</b> ₼', obj.total_price)
    total_price.short_description = 'Ümumi Qiymət'
    
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
