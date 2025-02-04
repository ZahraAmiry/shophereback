from django.shortcuts import render, HttpResponse
from .models import Product, Category, Cart

def Helloword(request):
    all_product=Cart.objects.all()
    return HttpResponse(all_product )
    #return render(request, 'index.html')


