from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full name',
                'class': 'comment-form__input-box'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'comment-form__input-box'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'class': 'comment-form__input-box'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'from-control phone-mask',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'class': 'comment-form__input-box text-message-box'
            })
        }