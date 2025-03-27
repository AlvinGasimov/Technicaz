from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, verbose_name="Telefon Nömrəsi")
    full_name = models.CharField(max_length=150, verbose_name="Tam Ad")

    def __str__(self):
        return self.user.username