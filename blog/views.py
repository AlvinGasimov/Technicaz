from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'blogs': blogs,
    }
    
    return render(request, 'blog.html', context)


def blog_details(request, blog_slug):
    blogs = Blog.objects.all()
    last_6_blogs = Blog.objects.order_by('-created_at')[:6]
    blog = get_object_or_404(Blog, slug=blog_slug)
    images = BlogImages.objects.filter(blog=blog)
    current_slug = blog.slug
    
    context = {
        'blog': blog,
        'images': images,
        'current_slug' : current_slug,
        'blogs' : blogs,
        'last_6_blogs' : last_6_blogs
    }
    
    
    return render(request, 'blog-single.html', context)