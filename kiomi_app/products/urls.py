from django.urls import path
from products.views import StoreView, ProductDetailsView, CarView

urlpatterns = [
    path('', StoreView.as_view(), name="store"),
    path('product-details/', ProductDetailsView.as_view(), name="product-details"),
    path('car/', CarView.as_view(), name="car"),
]
