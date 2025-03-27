from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('send-email-code/', send_email_code, name='send_email_code'),
    path('six-digit/', six_digit, name='six_digit'),
    path('change-password/', change_password, name='change_password'),
    path('order/', order, name='order'),
    path('my-account/', account, name='account'),
]