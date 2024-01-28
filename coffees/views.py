from django.shortcuts import render, redirect
from coffees.models import coffee, cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def coffee_detail(request, coffee_id):
    coffee_obj = coffee.objects.get(id=coffee_id)  
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
    
    item = cart.objects.filter(user_id=request.user.pk)
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
        cart.objects.create(user_id=request.user.id, item_id=coffee_id, quantity=1)
    return redirect('cart')

@login_required
def shopping_cart(request):
    items = cart.objects.filter(user_id=request.user.id)
    total_items = len(items)
    context ={
        "items": items,
        "total_items": total_items,
    }
        
    return render(request, 'cart.html', context)