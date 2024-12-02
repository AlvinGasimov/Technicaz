from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)