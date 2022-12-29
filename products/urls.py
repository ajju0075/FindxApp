from django.urls import path
from products import views as products_views

app_name = "products"
urlpatterns = [
    path(
        "products/create",
        products_views.ProductCreateView.as_view(),
        name="products_create",
    ),
    path(
        "product_list/", products_views.ProductListView.as_view(), name="product_list"
    ),
    path(
        "product/<int:pk>/details/",
        products_views.ProductDetailView.as_view(),
        name="product_details",
    ),
    path(
        "profile/<int:pk>/products/",
        products_views.UserProfileProducts.as_view(),
        name="profile_products",
    ),
    path(
        "profile/your/products/",
        products_views.UserProductsInProfile.as_view(),
        name="products_in_profile",
    ),
    path(
        "products/<int:pk>/update",
        products_views.UserProductsUpdateView.as_view(),
        name="products_update",
    ),
    path(
        "products/<int:pk>/delete",
        products_views.UserProductsDeleteView.as_view(),
        name="products_delete",
    ),
    path(
        "category/<int:pk>/product/",
        products_views.ProductByCategoryView.as_view(),
        name="product_by_category",
    ),
        path(
        "search/",
        products_views.SearchView.as_view(),
        name="product_search",
    ),
    path(
        "pyment/success/", products_views.PymentSuccesspage.as_view(),
        name= "pyment_success"
    ),
    path('post/', products_views.paymentpost, name='post_pyment'),
    path('paymenthandler/', products_views.paymenthandler, name='paymenthandler'),


]
