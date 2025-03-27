from django.db import models
from django.utils.text import slugify

class NavigationItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    address = models.CharField(max_length=255, blank=True)
    navbar_img = models.ImageField(upload_to='navbar_images/', blank=True)
    footer_img = models.ImageField(upload_to='footer_images/', blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    map_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    main_img = models.ImageField(upload_to='home_images/')
    responsive_img = models.ImageField(upload_to='home_images/', blank=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    other_img = models.ImageField(upload_to='about_images/', blank=True)

    def __str__(self):
        return self.title
    
    
class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='promotion_images/')
    video_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    title = models.CharField(max_length=255)
    main_img = models.ImageField(upload_to='faq_images/')
    other_img = models.ImageField(upload_to='faq_images/', blank=True)

    def __str__(self):
        return self.title
    

class QuestionAnswer(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

    
class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partner_images/')
    
    def __str__(self):
        return self.name
    
class Statistic(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email


class CEO(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    og_title = models.CharField(max_length=200, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = models.ImageField(upload_to='og_images/', null=True, blank=True)
    favicon = models.ImageField(upload_to='favicons/', null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ceo/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'CEO'
        verbose_name_plural = 'CEO\'s'