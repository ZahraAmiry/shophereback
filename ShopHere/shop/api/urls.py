from django.urls import path
from shop.api.views import productlist,creatproduct, api_product
from shop.api.views import categorylist,creatcategory, api_category
from shop.api.views import customerlist, creatcustomer, api_customer
from shop.api.views import cartlist, creatcart, api_cart
from shop.api.views import cartItemlist, creatItemcart, api_cartItem


urlpatterns= [
    #category------------------------------------------
    path('category/', categorylist, name='categorylist'),
    path('category/creat/',creatcategory, name='creatcategory'),
    path('category/<int:pk>', api_category, name="api_category"),
    #product-------------------------------------------
    path('product/', productlist, name='productlist '), 
    path('product/creat/',creatproduct, name='creatproduct'),
    path('product/<int:pk>', api_product, name="api_product"),
    #customer------------------------------------------------
    path('customer/',customerlist , name='customerlist'),
    path('customer/creat/',creatcustomer , name='creatcustomer'),
    path('customer/<int:pk>', api_customer, name='api_customer'), 
    #cart-------------------------------------------------------
    path('cart/',cartlist , name='cartlist'),
    path('cart/creat/',creatcart, name='creatcart'),
    path('cart/<int:pk>', api_cart, name='api_cart'),
    #cartItem-------------------------------------------------------
    path('cartItem/',cartItemlist , name='cartItemlist'),
    path('cartItem/creat/',creatItemcart, name='creatItemcart'),
    path('cartItem/<int:pk>', api_cartItem, name='api_cartItem'), 

]
