from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shop.models import Product, Category, Customer, Cart, CartItem
from shop.api.serialaizer import cartserialaizer, customerserialaizer, productserialaizer, categoryserialaizer,cartItemserialaizer 


#category---------------------------------------------------------------
@api_view(['GET'])
def categorylist(request):
    if request.method == "GET":
        query= Category.objects.all()
        serialaizer=categoryserialaizer(query, many=True)
        return Response(serialaizer.data)

@api_view(['POST'])
def creatcategory(request):
    serialaizer=categoryserialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_category(request, pk):
    try:
        category=Category.objects.get(pk= pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= categoryserialaizer(category)
        return Response(serialaizer.data)

#product----------------------------------------------------------------
@api_view(['GET'])
def productlist(request):
    if request.method == "GET":
        query= Product.objects.all()
        serialaizer=productserialaizer(query, many=True)
        return Response(serialaizer.data)
    
@api_view(['POST'])
def creatproduct(request):
    serialaizer=productserialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
@api_view(['GET'])
def api_product(request, pk):
    try:
        product=Product.objects.get(pk= pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= productserialaizer(product)
        return Response(serialaizer.data)

#customer---------------------------------------------------------------
@api_view(['GET'])
def customerlist(request):
    if request.method == "GET":
        query= Customer.objects.all()
        serialaizer=customerserialaizer(query, many=True)
        return Response(serialaizer.data)

@api_view(['POST'])
def creatcustomer(request):
    serialaizer=customerserialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_customer(request, pk):
    try:
        customer=Customer.objects.get(pk= pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= customerserialaizer(customer)
        return Response(serialaizer.data)
#Cart-----------------------------------------------------------
@api_view(['GET'])
def cartlist(request):
    if request.method == "GET":
        query=Cart.objects.all()
        serialaizer=cartserialaizer(query, many=True)
        return Response(serialaizer.data)

@api_view(['POST'])
def creatcart(request):
    serialaizer=cartserialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_cart(request, pk):
    try:
        cart=Cart.objects.get(pk= pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= cartserialaizer(cart)
        return Response(serialaizer.data)
        
#CartItem-----------------------------------------------------------
@api_view(['GET'])
def cartItemlist(request):
    if request.method == "GET":
        query=CartItem.objects.all()
        serialaizer=cartItemserialaizer(query, many=True)
        return Response(serialaizer.data)

@api_view(['POST'])
def creatItemcart(request):
    serialaizer=cartItemserialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_cartItem(request, pk):
    try:
        cartItem=CartItem.objects.get(pk= pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= cartItemserialaizer(cartItem)
        return Response(serialaizer.data)
    
"""
#---------------------------------------------------------------
@api_view(['GET'])
def list(request):
    if request.method == "GET":
        query= .objects.all()
        serialaizer=serialaizer(query, many=True)
        return Response(serialaizer.data)

@api_view(['POST'])
def creat(request):
    serialaizer=serialaizer(data=request.data)
    if serialaizer.is_valid():
        serialaizer.save()
        return Response(serialaizer.data, status=status.HTTP_201_CREATED)
    return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_(request, pk):
    try:
        =.objects.get(pk= pk)
    except .DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialaizer= serialaizer()
        return Response(serialaizer.data)
"""