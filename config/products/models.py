from django.db import models
from category.models import Category

class Product(models.Model):
    STOCK_CHOICES = (
    ('in_stock', 'в наличии!'),
    ('out_of_stock', 'нет в наличии')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveBigIntegerField(default=0)
    stock = models.CharField(max_length=25, choices=STOCK_CHOICES)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return f'{self.title}-{self.quantity}'
    
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='Product-Images/')

    def __str__(self) -> str:
        return f'Фото товара'
    

