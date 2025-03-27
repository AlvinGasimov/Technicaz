from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language
from unidecode import unidecode

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            current_language = get_language()
            
            if current_language == "az":
                self.slug = slugify(self.name, allow_unicode=True)
            else:
                self.slug = slugify(unidecode(self.name))
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Weight(models.Model):
    value = models.IntegerField()
    
    def __str__(self):
        return f"{self.value}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
    
class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')
    feature_name = models.CharField(max_length=255)
    feature_value = models.CharField(max_length=255)

    def __str__(self):
        return f"Feature for {self.product.name}"