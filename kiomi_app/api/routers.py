from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, ProductDetailViewSet, OrderItemGetViewSet, OrderItemPostViewSet

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

router.register(
    r'order-item-get',
    OrderItemGetViewSet,
    basename="order-item-get"
)

router.register(
    r'order-item-post',
    OrderItemPostViewSet,
    basename="order-item-post"
)

urlpatterns = router.urls
