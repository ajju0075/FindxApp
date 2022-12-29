from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
USER = settings.AUTH_USER_MODEL


class CategoryModel(models.Model): # model for catogory creating and sorting only new catogry on admin page
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class ProductsModel(models.Model): #model for products. user can post adds 
    user = models.ForeignKey(USER, on_delete=models.CASCADE,) 
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=30, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, )
    image = models.ImageField(upload_to="product/images" , default="default/product.png",null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    created_date  = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        url = reverse("product:product_create", kwargs={"pk": self.id})    


    def __str__(self):
        return self.user.username

class PymentModel(models.Model):# model for tracking paymets history
    user = models.ForeignKey(USER, on_delete=models.CASCADE, default=1) 
    order_id = models.CharField( max_length=120, unique=True)
    pyment_id = models.CharField(max_length=120)
    product = models.ForeignKey(ProductsModel,on_delete=models.CASCADE,)
    status = models.BooleanField(default=False)



