from django.shortcuts import render, redirect
from coffees.models import Coffee,Cart
from datetime import datetime
from django.contrib.auth.decorators import login_required
from coffees.models import InternalData

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
        Cart.objects.create(user_id=request.user.id, item_id=coffee_id, quantity=1)
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