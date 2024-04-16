from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Khejas(models.Model):
    category = models.ForeignKey(Category, related_name='khejass', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rent = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='khejas_images', blank=True, null=True)
    is_vacant = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='khejass', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name