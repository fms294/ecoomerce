from django.db import models
from django.db.models.base import ModelState


class Product(models.Model):
    name= models.CharField(max_length=2000)
    code = models.CharField(max_length=15, unique=True, default='NH')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name




# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(max_length=255, unique=True)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='category', blank=True)

#     class Meta:
#         ordering =('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(max_length=255, unique=True)
#     description = models.TextField(blank=True)
#     category = models.ForeignKey(Category, on_delete= models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='product', blank=True)
#     stock = models.IntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering =('name',)
#         verbose_name = 'product'
#         verbose_name_plural = 'products'
        
#     def __str__(self):
#         return self.name