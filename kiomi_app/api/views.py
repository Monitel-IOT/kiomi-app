from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status 
from products.models import Product
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
	def list(self, request):
		product_queryset = Product.objects.all()
		product_serializer = ProductSerializer(product_queryset, many=True)
		return Response(product_serializer.data, status=status.HTTP_200_OK)