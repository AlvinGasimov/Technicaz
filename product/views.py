from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from shop.models import Favorite

def products(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search', '')
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user).values_list('product', flat=True)
    else:
        favorites = []
    
    if category_slug:
        category = ProductCategory.objects.filter(slug=category_slug).first()
        products = products.filter(category=category) if category else Product.objects.none()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    paginator = Paginator(products.order_by('-created_at'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'products': products,
        'product_categories': ProductCategory.objects.all(),
        'selected_category': category_slug,
        'search_query': search_query,
        'favorites': favorites
    }
    
    return render(request, 'products.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    weights = Weight.objects.all().order_by('value')
    
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
    else:
        is_favorite = False
    

    context = {
        'product': product,
        'weights': weights,
        'is_favorite': is_favorite
    }
    return render(request, 'product-details.html', context)