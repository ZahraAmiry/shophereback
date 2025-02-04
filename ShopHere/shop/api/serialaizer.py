from rest_framework import serializers
from shop.models import Product, Category, Customer, Cart, CartItem
#product---------------------------------------------------
class productserialaizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'
#category--------------------------------------------------
class categoryserialaizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'

#customer----------------------------------------------------
class customerserialaizer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields= '__all__'       

#Cart----------------------------------------------------
class cartserialaizer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    #user_name=serializers.CharField(source='user.username',read_only=True )
    class Meta:
        model=Cart
        fields=['user','total_price', 'user_name']

#cartItem----------------------------------------------------
class cartItemserialaizer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['cart', 'product','quantity','total_price']       
