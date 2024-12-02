from .models import *
from blog.models import Blog
from .forms import SubscribeForm
from django.contrib import messages
from django.shortcuts import redirect
from product.models import ProductCategory, Product
from shop.models import *

def site_settings(request):
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('base:index')
    else:
        form = SubscribeForm()
        
    product_categories = ProductCategory.objects.all()
    selected_category_slug = request.GET.get('category')  # Kateqoriya filtri üçün
    if selected_category_slug:
        selected_category = ProductCategory.objects.filter(slug=selected_category_slug).first()
        products = Product.objects.filter(category=selected_category, discount_price__isnull=False)
    else:
        selected_category = None
        products = Product.objects.filter(discount_price__isnull=False)
        
    if request.user.is_authenticated:
        total_items = CartItem.objects.filter(user=request.user).aggregate(total=models.Sum('quantity'))['total'] or 0
    else:
        total_items = 0
  
    navigation_item = NavigationItem.objects.last()
    last_3_blogs = Blog.objects.order_by('-created_at')[:3]
    partners = Partner.objects.all()
    statistics = Statistic.objects.all()
    faq = FAQ.objects.first()
    promotion = Promotion.objects.first()
    about = About.objects.first()
    last_6_categories = ProductCategory.objects.order_by('-created_at')[:6]
    ceo = CEO.objects.last()

    context = {
        'navigation_item' : navigation_item,
        'last_3_blogs' : last_3_blogs,
        'partners' : partners,
        'statistics' : statistics,
        'faq' : faq,
        'promotion' : promotion,
        'form' : form,
        'about' : about,
        'product_categories' : product_categories,
        'products': products,
        'selected_category': selected_category,
        'total_items' : total_items,
        'last_6_categories' : last_6_categories,
        'ceo' : ceo
    }
    return context