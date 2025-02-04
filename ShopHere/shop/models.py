from django.db import models
#category---------------------------------------------------------------
class Category(models.Model):
    name =models.CharField(max_length=20)
    description=models.CharField(max_length=100, blank=True)
    picture=models.CharField(max_length=500,  blank=True, null=True)
    #picture=models.ImageField(upload_to='upload/category/', blank=True, null=True)
    
    def __str__(self):
        return self.name

#producr------------------------------------------------------------------
class Product(models.Model):
    name=models.CharField(max_length=100)#نام محصول
    description=models.TextField() #توضیحات محصول
    price=models.DecimalField(max_digits=10, decimal_places=2)# قیمت محصول
    picture=models.CharField(max_length=500,  blank=True, null=True)
    #media=models.ImageField(upload_to='upload/product/', blank=True, null=True)#تصویر محصول
    category=models.ForeignKey(Category, on_delete=models.CASCADE) #دسته بندی

    def __str__(self):
        return self.name
    
#coustomer------------------------------------------------------------------
class Customer(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)
    date_login=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

#Cart------------------------------------------------------------------------
class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
    @property
    def get_user_name(self):
        return self.user  # برگرداندن نام کاربر
    

    def __str__(self):
        return f"Cart of {self.user}"  

  

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    @property
    def return_name(self):
        return self.cart.user

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"    

#product------------------------------------------------------------------
               