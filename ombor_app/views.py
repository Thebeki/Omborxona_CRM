from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .models import *

from statistika.models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        u = request.POST.get("login")
        p = request.POST["password"]
        users = authenticate(request, username=u, password=p)
        if users is None:
            return redirect("login")
        else:
            login(request, users)
            return redirect("bolim")

class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect("login")

class MahsulotView(View):
    def get(self, request):
        if request.user.is_authenticated:
            print(request.user)
            o = Ombor.objects.get(user=request.user)
            p = Mahsulot.objects.filter(ombor=o)
            return render(request, 'products.html', {"all_products":p})
        else:
            return redirect("login")
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            name=request.POST["pr_nom"],
            brend_name=request.POST["pr_brand"],
            kelgan_sum=request.POST["pr_price"],
            sale_sum=request.POST["pr_sale_sum"],
            quantity=request.POST["pr_amount"],
            ombor=ombor
        )
        return redirect("mahsulotlar")

class MahsulotEditView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=son)
            return render(request, 'product_update.html', {"product":mahsulot})
        else:
            return redirect("login")
    def post(self, request, son):
        if request.user.is_authenticated:
            product = Mahsulot.objects.get(id=son)
            product.name=request.POST["name"]
            product.brend_name=request.POST["brand_name"]
            product.kelgan_sum=request.POST["price"]
            product.sale_sum=request.POST["price2"]
            product.quantity=request.POST["amount"]
            product.save()
            return redirect("mahsulotlar")
        else:
            return redirect("login")


class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            clientlar = Client.objects.filter(ombor=o)
            return render(request, 'clients.html', {"all_clients":clientlar})
        else:
            return redirect("login")
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST["ism"],
            shop_name=request.POST["shop_name"],
            tel=request.POST["tel"],
            location=request.POST["location"],
            debt=request.POST["debt"],
            ombor=ombor
        )
        return redirect("clientlar")
        
        
class ClientEditView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            client = Client.objects.get(id=son)
            ombor = Ombor.objects.get(user=request.user)
            return render(request, 'client_update.html', { "ombor":ombor, "client":client})
        else:
            return redirect("login")
    def post(self, request, son):
        if request.user.is_authenticated:
            ombor = Ombor.objects.get(user=request.user)
            client = Client.objects.get(id=son)
            client.ism=request.POST["ism"]
            client.shop_name=request.POST["shop_name"]
            client.tel=request.POST["tel"]
            client.location=request.POST["location"]
            client.debt=request.POST["debt"]
            client.ombor=ombor
            client.save()
            
            
            return redirect("clientlar")
        else:
            return redirect("login")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

