from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ad Soyadınız *',
            'class': 'form-control',
        }),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email *',
            'class': 'form-control',
        }),
        required=True
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': '(_ _) _ _ _-_ _-_ _',
            'class': 'form-control phone-mask',
            'style': 'padding-left: 3.6rem; font-size: 14px;',
            'maxlength': '14',
        }),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Şifrə *',
            'class': 'form-control',
        }),
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Təkrar şifrə *',
            'class': 'form-control',
        }),
        required=True
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email artıq istifadə olunur.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Şifrələr uyğun deyil.")
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'placeholder': 'Email *'
    }))
    password = forms.CharField(label="Şifrə", widget=forms.PasswordInput(attrs={
        'placeholder': 'Şifrə'
    }))