from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(NavigationItem)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address',)


@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title','description', )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    
    
@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    
    
@register(Promotion)
class PromotionTranslationOptions(TranslationOptions):
    fields = ('title','description', )

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(QuestionAnswer)
class QuestionAnswerTranslationOptions(TranslationOptions):
    fields = ('question', 'answer', )


@register(CEO)
class CEOTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'og_title', 'og_description', 'author', 'position')