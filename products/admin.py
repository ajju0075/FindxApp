from django.contrib import admin
from products import models as products_model

# Register your models here.

admin.site.register(products_model.ProductsModel)
admin.site.register(products_model.CategoryModel)