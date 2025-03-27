from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Mesajınız uğurla göndərildi!")
            return redirect('contact:contact')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)