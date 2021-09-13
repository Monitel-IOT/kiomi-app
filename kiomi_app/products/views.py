from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from products.models import Product
from api.serializers import ProductSerializer

# Create your views here.
class StoreView(View):
    def get(self, request):
        return render(request,'products/store.html')
class ProductDetailsView(View):
	def get(self, request):
		return render(request, 'products/productDetails.html')