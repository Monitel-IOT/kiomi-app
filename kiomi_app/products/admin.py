from products.models import Customer, Order, OrderItem, Product, ShippingAddress, CategoriaProd
from django.contrib import admin

admin.site.register(Customer)
admin.site.register(CategoriaProd)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
