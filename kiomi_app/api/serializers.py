from django.db.models import fields
from rest_framework import serializers
from products.models import Product, Flavor, FlavorCoverage, FlavorBizcocho

class FlavorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flavor
		fields = ['id', 'flavor']

class FlavorCoverageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flavor
		fields = ['id', 'flavor']
class FlavorBizcochoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flavor
		fields = ['id', 'flavor']
class ProductSerializer (serializers.ModelSerializer):
	flavor = FlavorSerializer(many=True, read_only=True) 
	flavorCoverage = FlavorCoverageSerializer(many=True, read_only=True) 
	flavorBizcocho = FlavorBizcochoSerializer(many=True, read_only=True) 
	class Meta:
		model = Product
		fields = '__all__'
	