from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    extra = 1
    
@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    inlines = [BlogImagesInline]
    list_display = ('title', 'image', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    
    
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