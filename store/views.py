from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from  . utilss import cookieCart , cartData , guestOrder

from django.http import HttpResponse



def about(request):
    context = {}
    return render(request, 'store/about.html', context)


def blog_rightsidebar(request):
    context = {}
    return render(request, 'store/blog_rightsidebar.html', context)


def blog(request):
    context = {}
    return render(request, 'store/blog.html', context)


def brand_product(request):
    context = {}
    return render(request, 'store/brand_product.html', context)


def checkout(request):  # انا مش فاهم حاجة
   
    Data = cartData(request)
    cartItems = Data["cartItems"]
    order = Data["order"]
    items = Data["items"]

   
    context = {'items' : items, 'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)



def product_fullwidth(request):
    Data = cookieCart(request)
    cartItems = Data["cartItems"]
    order = Data["order"]
    
    items = Data["items"]
    products =Product.objects.all()

    # for i in range(len(items)):
    #     id=items[i]['product']['id']
    #     product=Product.objects.get(id=id)
    #     product.quantity =  items[i]['quantity']

    
    for product in products:
        for item in items:
            if product.id == item['product']['id']:
                # id=item['product']['id']
                # product=Product.objects.get(id=id)
                product.quantity =  item['quantity']
                
    context = {'items' : items,'products':products,'cartItems':cartItems, 'order':order}
    return render(request, 'store/product_fullwidth.html', context)

def product_leftsidebar(request):
    context = {}
    return render(request, 'store/product_leftsidebar.html', context)
def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def faq(request):
    context = {}
    return render(request, 'store/faq.html', context)

def home_default(request):
    context = {}
    return render(request, 'store/home_default.html', context)

def home_search(request):
    context = {}
    return render(request, 'store/home_search.html', context)

def home_slider(request):
    context = {}
    return render(request, 'store/home_slider.html', context)

def home_slider2(request):
    context = {}
    return render(request, 'store/home_slider2.html', context)


def index_icon(request):
    context = {}
    return render(request, 'store/index_icon.html', context)

def index(request):
    context = {}
    return render(request, 'store/index.html', context)
def order_details(request):
    context = {}
    return render(request, 'store/order_details.html', context)

def product_detail(request):
    context = {}
    return render(request, 'store/product_detail.html', context)
def product_list(request):
    context = {}
    return render(request, 'store/product_list.html', context)

def profile(request):
    context = {}
    return render(request, 'store/profile.html', context)

def single(request):
    context = {}
    return render(request, 'store/single.html', context)

def track_order_single(request):
    context = {}
    return render(request, 'store/track_order_single.html', context)

def track_order(request):
    context = {}
    return render(request, 'store/track_order.html', context)

def user_dashbord(request):
    context = {}
    return render(request, 'store/user_dashbord.html', context)

def wishlist(request):
    context = {}
    return render(request, 'store/wishlist.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action :',action)
    print('productId :',productId)

    
    customer = request.user.customer
    
    product =Product.objects.get(id=productId)

    order , created = Order.objects.get_or_create(customer=customer ,complete = False)
    orderItem,created =OrderItem.objects.get_or_create(order=order, product=product)
    
    

    if action == 'addd':
        orderItem.quantity=(orderItem.quantity +1)
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity -1)
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item was add', safe = False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer ,complete = False)
        
        
        print(order.complete)

     
    else :
        customer , order =guestOrder(request ,data)
    
   
   
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float (order.get_cart_total):
        print (order.complete)
        order.complete = True
        order.save()

    ShippingAddress.objects.create(
            customer=customer,
            order = order ,
            city = data['shipping']['city'],
            Region = data['shipping']['region'],
            street = data['shipping']['street'],
            place = data['shipping']['place']
        ) 
    return JsonResponse('Paymant complete', safe=False)






# 	else:
# 		customer, order = guestOrder(request, data)

# 	total = float(data['form']['total'])
# 	order.transaction_id = transaction_id

# 	if total == order.get_cart_total:
# 		order.complete = True
# 	order.save()

# 	if order.shipping == True:
# 		ShippingAddress.objects.create(
# 		customer=customer,
# 		order=order,
# 		address=data['shipping']['address'],
# 		city=data['shipping']['city'],
# 		state=data['shipping']['state'],
# 		zipcode=data['shipping']['zipcode'],
# 		)

# 	return JsonResponse('Payment submitted..', safe=False)


def bill(request):

    if request.user.is_authenticated:

        order=Order.objects.get(id=89)
        items = order.orderitem_set.all()
        


        total = 0
        for item in items:
            total = item.product.price * item.quantity + total




        
        products =Product.objects.all()

        context = {"items":items , "total":total}
        return render(request, 'store/bill.html', context)

    else:
        return HttpResponse('<h1> please login </h1>')