from django.db import models

# Create your models here.

class Category(models.Model):
    '''Model definition for Category.'''
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
      
class Product(models.Model):
    '''Model definition for Product.'''
    category = models.ForeignKey(Category, related_name='products' , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    
    class Meta:
        '''Meta definition for Product.'''

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
      