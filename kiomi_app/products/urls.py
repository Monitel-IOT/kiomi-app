from django.urls import path
from products.views import StoreView

urlpatterns = [
    path('', StoreView.as_view()),
]