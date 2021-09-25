from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from products.models import Product
from api.serializers import ProductSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins


class ProductViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
  pagination_class = PageNumberPagination
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


# class PostPagination(PageNumberPagination):
# 	page_size=2


class ProductDetailViewSet(viewsets.GenericViewSet):
  """
  Detalles del producto
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
