from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, ProductDetailViewSet

router = DefaultRouter()

router.register(
	r'products', 
	ProductViewSet,
	basename="products"
)
router.register(
	r'products-detail', 
	ProductDetailViewSet,
	basename="products-details"
)

urlpatterns = router.urls