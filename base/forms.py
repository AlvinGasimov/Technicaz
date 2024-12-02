from django import forms
from .models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email adresi daxil edin",
                }
            )
        }