from django.urls import path
from products.views import StoreView, ProductDetailsView

urlpatterns = [
    path('', StoreView.as_view(), name="store"),
    path('product-details/', ProductDetailsView.as_view(), name="product-details"),
]