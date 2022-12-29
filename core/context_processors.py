from products.models import CategoryModel, ProductsModel
from django.conf import settings


def common_data(request):
    categories = CategoryModel.objects.all()

    context = {
        "categories": categories,
        'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY
        
    }
    return context


# def common_data(request):
#     product = ProductsModel.objects.all()
#     context = {
#         "product": product,
#     }
#     return context
