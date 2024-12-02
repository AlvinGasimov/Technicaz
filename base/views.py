from django.shortcuts import render, redirect
from .forms import SubscribeForm
from .models import Feature, Home
from product.models import Product
from shop.models import Favorite
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def index(request):
    features = Feature.objects.all()
    homes = Home.objects.all()
    first_8_products = Product.objects.order_by('-created_at')[:8]
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user).values_list('product', flat=True)
    else:
        favorites = []  # İstifadəçi daxil olmayıbsa, boş siyahı qaytarın


    context = {
        "form" : SubscribeForm(),
        "features" : features,
        "homes" : homes,
        'first_8_products' : first_8_products,
        'favorites': favorites,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def set_language(request, language):
    # Yalnız dəstəklənən dilləri qəbul et
    if language not in dict(settings.LANGUAGES):
        return HttpResponseRedirect("/")

    referer = request.META.get("HTTP_REFERER", "/")
    try:
        view = resolve(urlparse(referer).path)
        translation.activate(language)
        app_name = view.app_name if hasattr(view, 'app_name') else None
        view_name = f"{app_name}:{view.url_name}" if app_name else view.url_name

        response = HttpResponseRedirect(
            reverse(view_name, args=view.args, kwargs=view.kwargs)
        )
    except Resolver404:
        response = HttpResponseRedirect("/")
    
    # Dil seçimini kukiyə yaz
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response