from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Uğurla daxil oldunuz.")
                return redirect("base:index")
    else:
        form = LoginForm()
        
    context = {
        'form' : form,
    }
    
    return render(request, 'login.html', context)   

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
    
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
            )
            user.first_name = full_name
            user.save()
            UserProfile.objects.create(user=user, phone_number=phone_number, full_name=full_name)

            messages.success(request, "Qeydiyyat uğurla tamamlandı!")
            return redirect('account:login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('base:index')

@login_required
def account(request):
    full_name = f"{request.user.first_name} {request.user.last_name}"
    email = request.user.email
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        phone_number = user_profile.phone_number
    except UserProfile.DoesNotExist:
        phone_number = None

    context = {
        'full_name': full_name,
        'email': email,
        'phone_number': phone_number,
    }
    return render(request, 'myaccount.html', context)


# Password Processing

def change_password(request):
    return render(request, 'changePassword.html')

def send_email_code(request):
    return render(request, 'sendEmailCode.html')

def six_digit(request):
    return render(request, 'sixdigitsPassword.html')

def change_password(request):
    return render(request, 'changePassword.html')


def order(request):
    return render(request, 'orders.html')