from django.shortcuts import render
from products import models as product_model
from django.views import generic as views
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


class PoductListApiView(views.View):
    model = product_model.ProductsModel

    def get(self, request):
        data = self.model.objects.all()
        data = serializers.serialize("json", self.model.objects.all())
        return JsonResponse(data, safe=False)
    
