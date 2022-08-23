from django.db import models
from apps.category.models import SubCategory
# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=2500, blank=True)
    price           = models.IntegerField()
    mrp             = models.IntegerField(null= True, default= price)
    img1            = models.ImageField(upload_to='photos/products')
    img2            = models.ImageField(upload_to='photos/products')
    img3            = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sold_quantity   = models.IntegerField(default=0)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)


    def offer(self):
        product_offer = int(((self.mrp - self.price)/self.mrp) * 100)
        return product_offer
 
    def __str__(self): 
        return self.product_name

   

