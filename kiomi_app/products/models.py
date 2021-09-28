from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
  """
  Cliente
  """
  user = models.OneToOneField(
      User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(max_length=200)

  class Meta:
    verbose_name = "Customer"
    verbose_name_plural = "Customers"
    ordering = ["user"]

  def __str__(self):
    return self.name


# Por el momento solo se han modificado el product y la categoriaProd
class CategoriaProd(models.Model):  # categoria del producto (galleta, torta, etc.)
  """
  Partes de un producto como cobertor, bizcocho, etc
  """
  nombre = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre


class Product(models.Model):
  """
  Partes de un producto como cobertor, bizcocho, etc
  """

  name = models.CharField(max_length=100)
  price = models.FloatField()
  description = models.CharField(max_length=1000)
  categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
  image_1 = models.ImageField(null=True, blank=True)
  image_2 = models.ImageField(null=True, blank=True)
  image_3 = models.ImageField(null=True, blank=True)

  class Meta:
    verbose_name = "Product"
    verbose_name_plural = "Products"
    ordering = ["name"]

  def __str__(self) -> str:
    return self.name


class FlavorBizcocho(models.Model):
  """
  Sabores de los productos
  """

  flavor = models.CharField("Sabor de bizcocho", max_length=50)
  product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE,
      related_name="flavorBizcocho",
      blank=True,
      null=True,
  )

  def __str__(self) -> str:
    return self.flavor


class FlavorCoverage(models.Model):
  """
  Sabores de los productos
  """

  flavor = models.CharField("Sabor de cobertura", max_length=50)
  product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE,
      related_name="flavorCoverage",
      blank=True,
      null=True,
  )

  def __str__(self) -> str:
    return self.flavor


class Flavor(models.Model):
  """
  Sabores de los productos
  """

  flavor = models.CharField("Sabor", max_length=50)
  product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE,
      related_name="flavor",
      blank=True,
      null=True,
  )

  def __str__(self) -> str:
    return self.flavor


class Order(models.Model):
  customer = models.ForeignKey(
      Customer, on_delete=models.SET_NULL, null=True, blank=True
  )
  date_ordered = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=100, null=True)

  class Meta:
    verbose_name = "order"
    verbose_name_plural = "orders"
    ordering = ["date_ordered"]

  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total

  @property
  def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total

  def __str__(self):
    return str(self.id)


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  orderFlavorCoverage = models.ForeignKey(
      FlavorCoverage, null=True, blank=True, on_delete=models.CASCADE)
  orderFlavorBizcocho = models.ForeignKey(
      FlavorBizcocho, null=True, blank=True, on_delete=models.CASCADE)
  orderFlavor = models.ForeignKey(
      Flavor, null=True, blank=True, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  # class Meta:
  #  verbose_name = "orderitem"
  #  verbose_name_plural = "orderitems"
  #  ordering = ["id"]

  # @property
  # def get_total(self):
  #  total = self.product.price * self.quantity
  #  return total

  def __str__(self):
    return str(self.product)


class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200, null=False)
  city = models.CharField(max_length=200, null=False)
  state = models.CharField(max_length=200, null=False)
  zipcode = models.CharField(max_length=200, null=False)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "shippingaddress"
    verbose_name_plural = "shippingaddresses"
    ordering = ["id"]

  def __str__(self):
    return self.address
