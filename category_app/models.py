from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Product(models.Model):  #SUBCATEGORY
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    

    def __str__(self):
        return self.product_name

class Create(models.Model):
    
    subcategory = models.ForeignKey(Product, on_delete=models.CASCADE)
    product =  models.CharField(max_length=100)
    price = models.CharField(max_length =20)
    is_active = models.BooleanField()

