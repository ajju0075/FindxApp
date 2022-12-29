from django.urls import path
from api import views as api_views


app_name = "api"
urlpatterns = [
    path("products/", api_views.PoductListApiView.as_view(), name = "product_api_list"),

]


