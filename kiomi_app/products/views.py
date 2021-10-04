from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from products.models import Product
from api.serializers import ProductSerializer

#import login register tools
from django.contrib import messages
from .form import UserRegisterForm

# Create your views here.


class StoreView(View):
  def get(self, request):
    return render(request, 'products/store.html')


class ProductDetailsView(View):
  def get(self, request):
    return render(request, 'products/productDetails.html')


class CarView(View):
  def get(self, request):
    return render(request, 'products/car.html')

class AboutView(View):
  def get(self, request):
    return render(request, 'products/about.html')

class HomeView(View):
  def get(self, request):
    return render(request, 'products/home.html')

class ContactView(View):
  def get(self, request):
    return render(request, 'products/contact.html')

#Crearemos las funciones de register login logout

def welcome(request):
  #return to cover page
  return render(request, "login/welcome.html")


def register(request):
  #creamos un formulario de autentificacion vacio
  form = UserRegisterForm()
  if request.method == "POST":
      #Añadimos los datos recibidos del formulario
      form = UserRegisterForm(request.POST)
      #Si el formulario es valido
      if form.is_valid():
          form.save()
          #creamos una nueva cuenta de usuario
          username = form.cleaned_data['username']
          messages.success(request, f'usuario{username}creado')
          return redirect('welcome')
      else:
          form = UserRegisterForm()
  context = {'form': form}
  return render(request, "login/register.html", context)