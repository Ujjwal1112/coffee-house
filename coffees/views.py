from django.shortcuts import render, redirect
from coffees.models import Coffee,Cart, InternalData, Orders
from datetime import datetime
from django.contrib.auth.decorators import login_required
from users.models import Profile, ConsumedCoffee
import uuid
# Create your views here.

def coffee_detail(request, coffee_id):
    coffee_obj = Coffee.objects.get(id=coffee_id)  
    context = {
        "coffee" : coffee_obj
    }
    return render(request, "coffee_detail.html", context)


@login_required
def add_to_cart(request, coffee_id):
    # alternative way 
    # if cart.objects.filter(user_id=request.user.pk, item_id=coffee_id).exists():
    #     item = cart.objects.filter(user_id=request.user.pk, item_id=coffee_id)
    #     item_obj = item[0]
    #     item_obj.quantity = item_obj.quantity + 1
    #     item_obj.save()
    
    # if not cart.objects.filter(user_id=request.user.pk, item_id=coffee_id).exists():
    #     cart.objects.create(user_id=request.user.id, item_id=coffee_id, quantity=1)    
    
    item = Cart.objects.filter(user_id=request.user.pk)
    flag = False
    if item:
        for items in item:
            if items.item.id == coffee_id:
                flag = False
                items.quantity += 1
                items.save()
                break
            
            if items.item.id != coffee_id:
                flag = True
    if not item:
        flag=True
    if flag is True:
        item = Coffee.objects.get(id=coffee_id)
        
        Cart.objects.create(user_id=request.user.id, item_id=coffee_id, quantity=1, total_price=item.price_after_discount()*1 )
    return redirect('cart')



@login_required
def shopping_cart(request):
    items = Cart.objects.filter(user_id=request.user.id)
    data = InternalData.objects.all()[0]
    total_items = len(items)   
    total_price = sum([item.total_price for item in items]) 
    shipping_fee = data.shipping_fee
    tax = data.tax_percentage
    after_tax_amount = (total_price*((100+tax)/100)) + shipping_fee
    context ={
        "items": items,
        "total_items": total_items,
        "total_price": total_price,
        "shipping_fee" : shipping_fee,
        "tax" : tax,
        "after_tax_amount": after_tax_amount
        
    }
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        coffee_id = request.POST['coffee_id']
        item = Cart.objects.get(user_id = request.user.id, item_id = coffee_id)
        item.quantity = quantity
        item.total_price = item.quantity * item.item.price_after_discount()
        item.updated_at = datetime.now()
        item.save()
        return redirect('cart')       
    return render(request, 'cart.html', context)



@login_required
def remove_from_cart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    return redirect('cart')



@login_required
def checkout(request):
    items = Cart.objects.filter(user_id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.pk)
    context = {
        "items": items,
        "profile": profile,
        "total_items": request.GET['total_items'],
        "after_t_amount" : request.GET['after_tax']
    }
    return render(request, 'checkout.html', context)

@login_required
def order(request):
    orders = Orders.objects.filter(user_id=request.user.id).order_by('-created_at')
    data = InternalData.objects.all()[0]
    shipping_fee = data.shipping_fee
    tax = data.tax_percentage
    context = {
        'orders': orders,
        'total_orders': len(orders),
        "shipping_fee" : shipping_fee,
        "tax" : tax,
    }
    
    if request.method == 'POST':
        coffees = Cart.objects.filter(user_id=request.user.id).order_by('created_at')
        address = request.POST['address']
        district = request.POST['district']
        house_number = request.POST['house_number']
        street = request.POST['street']
        total_items = int(request.POST['total_items'])
        after_t_amount = float(request.POST['after_t_amount'])
        instructions = request.POST['instructions']
        order_id =uuid.uuid1()
        status = "Pending"

        coffee_json = []
        for coffee in coffees:
            coffee_json.append({
                "name" : coffee.item.name,
                "picture" : coffee.item.coffee_pic,
                "quantity" : coffee.quantity,
                "total_price" : coffee.total_price,
                "category" : coffee.item.category.name
            })
            if ConsumedCoffee.objects.filter(user_id=request.user.id, coffee_id=coffee.item.id).exists():
                item = ConsumedCoffee.objects.get(user_id=request.user.id, coffee_id=coffee.item.id)
                item.quantity = item.quantity + coffee.quantity
                item.save()
            else:
                ConsumedCoffee.objects.create(user_id=request.user.id, coffee_id=coffee.item.id, 
                                          quantity = coffee.quantity)

            
        data={
            "order_id" : order_id,
            "user_id" : request.user.id,
            "after_tax_amount" : after_t_amount,
            "house_number" : house_number,
            "street" : street,
            "other_addresses" : address,
            "district": district,
            "instructions" : instructions,
            "status" : status,
            "total_items": total_items,
            "coffees": coffee_json 
        }
        
        order = Orders.objects.create(**data)
        order.save()
        coffees.delete()
        return redirect('thank-you')        
        
    

    return render(request, 'order.html', context)

@login_required
def thank_you(request):
    return render(request, 'thank-you.html',) 
    