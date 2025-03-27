from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug',)
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
        


admin.site.register(Weight)


class ProductFeaturesInline(admin.TabularInline):
    model = ProductFeatures
    extra = 1
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
    

class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'price', 'category', 'image']
    inlines = [ProductFeaturesInline, ProductImagesInline]
    
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