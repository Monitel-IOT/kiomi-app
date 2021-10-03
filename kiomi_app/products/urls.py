from django.urls import path
from products.views import StoreView, ProductDetailsView, CarView, AboutView, HomeView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('store/', StoreView.as_view(), name="store"),
    path('product-details/', ProductDetailsView.as_view(), name="product-details"),
    path('car/', CarView.as_view(), name="car"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
]
