from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status 
from products.models import Product
from api.serializers import ProductSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins

class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	pagination_class = PageNumberPagination
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

# class PostPagination(PageNumberPagination):
# 	page_size=2

