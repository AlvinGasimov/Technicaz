from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Adınız',
                'class': 'comment-form__input-box'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email ünvanı',
                'class': 'comment-form__input-box'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Mövzu',
                'class': 'comment-form__input-box'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Telefon Nömrəsi',
                'class': 'from-control phone-mask',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Mesaj yazın',
                'class': 'comment-form__input-box text-message-box'
            })
        }