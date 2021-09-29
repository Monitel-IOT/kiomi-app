""" rest framework api """
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render

from products.models import Product
from products.models import OrderItem
from api.serializers import OrderItemSerializer, ProductSerializer



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


class OrderItemViewSet(
    viewsets.GenericViewSet
):
  """
  Lista de items que el cliente añadió a su carrito
  """
  queryset = OrderItem.objects.all()
  serializer_class = OrderItemSerializer

  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  def delete(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response()
######################
