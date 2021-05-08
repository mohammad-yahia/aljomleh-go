from django.db import models
from django.contrib.auth.models import User

class Customer (models.Model):
    user = models.OneToOneField(User , null=True , blank=True , on_delete=models.CASCADE)
    name =models.CharField(max_length=50 , null=True)
    email = models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    
    def __str__(self):
        return str (self.name) 




class Category (models.Model):
    name = models.CharField(max_length=25)
   
    def __str__(self):
        return self.name

class Brand (models.Model):
    name = models.CharField(max_length=25)
   
    def __str__(self):
        return self.name

class Flavor (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    price =models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField(max_length=10)
    category =models.ForeignKey(Category, null=True ,  blank=True  , on_delete=models.SET_NULL)
    brand =models.ForeignKey(Brand, null=True ,  blank=True , on_delete=models.SET_NULL)

    flavor =models.ForeignKey(Flavor, null=True  , on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Order (models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        return True

    @property
    def get_cart_total (self):
        orderitems = self.orderitem_set.all()
        total =sum([item.get_total for item in orderitems ])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])
        return total 

class OrderItem (models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    quantity  =models.IntegerField(default=0, null=True, blank=True)
    flavor =models.ForeignKey('flavor', null=True  ,blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        # print ("price")
        # print (self.product.price)
        # print ("quantity")
        # print (self.quantity)
        # print (total)
        return total 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL,null=True)
    city = models.CharField(max_length=50,null=False)
    Region= models.CharField(max_length=50,null=False)
    street = models.CharField(max_length=50,null=False)
    place = models.CharField(max_length=50,null=False)

    def __str__(self):
        return str(self.place)


    

