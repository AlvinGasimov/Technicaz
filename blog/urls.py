from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<slug:blog_slug>', blog_details, name='blog-details')
]