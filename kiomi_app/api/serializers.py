from django.db.models import fields
from rest_framework import serializers
from products.models import Order, Product, Flavor, FlavorCoverage, FlavorBizcocho, OrderItem


class FlavorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flavor
    fields = ["id", "flavor"]


class FlavorCoverageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flavor
    fields = ["id", "flavor"]


class FlavorBizcochoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flavor
    fields = ["id", "flavor"]


class ProductSerializer(serializers.ModelSerializer):
  flavor = FlavorSerializer(many=True, read_only=True)
  flavorCoverage = FlavorCoverageSerializer(many=True, read_only=True)
  flavorBizcocho = FlavorBizcochoSerializer(many=True, read_only=True)

  class Meta:
    model = Product
    fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItem
    fields = "__all__"

  #  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  #order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  #quantity = models.IntegerField(default=0, null=True, blank=True)
  # orderFlavorCoverage = models.ForeignKey(
  #    FlavorCoverage, on_delete=models.CASCADE)
  # orderFlavorBizcocho = models.ForeignKey(
  #    FlavorBizcocho, on_delete=models.CASCADE)
  #orderFlavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
  #date_added = models.DateTimeField(auto_now_add=True)
