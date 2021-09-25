from products.models import Customer, Order, OrderItem, Product, ShippingAddress, CategoriaProd, Flavor, FlavorBizcocho, FlavorCoverage 
from django.contrib import admin

class FlavorAdmin(admin.ModelAdmin):
	list_display = ('id', 'flavor')

admin.site.register(Customer)
admin.site.register(CategoriaProd)

admin.site.register(Flavor, FlavorAdmin)
admin.site.register(FlavorBizcocho)
admin.site.register(FlavorCoverage)
admin.site.register(Product)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
