from django.shortcuts import render, redirect
from users.models import User, Profile, ConsumedCoffee
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from users.helper import get_url_from_file
from coffees.models import Coffee
from django.core.paginator  import Paginator
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index_page(request):
    search = request.GET.get('search')
    if search:
        coffees = Coffee.objects.filter(Q(name__icontains=search) | Q(description__contains=search))
    else:
        search = ''
        coffees = Coffee.objects.all().order_by("created_at")
    page = request.GET.get("page", 1)
    pagination = Paginator(coffees, 8)
    data_with_pagination = pagination.get_page(page)
    total_pages = list(pagination.page_range)
    data_with_pagination.after = 600
    context = {
        "coffees" : data_with_pagination,
        "total_pages": total_pages,
        "search" : search,
        "page" : int(page)
    }   

    return render(request, 'index.html', context)

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
        if User.objects.filter(email=email).exists():
            Valid_user = User.objects.filter(email=email)[0]
            check_user = authenticate(username=Valid_user.username, password=password)
            if check_user:
                messages.info(request, "you are logged in")
                login(request, check_user)
                profile  = Profile.objects.get(user_id=request.user.pk)
                request.session['name']= profile.user.first_name
               
                
                request.session['profile_pic'] = profile.profile_url
                return redirect('index')
            if not check_user:
                messages.error(request, 'Invalid email or password')
                return redirect('login')
        if not User.objects.filter(email=email).exists():
            messages.error(request, "email does not exists")
            return redirect('login')   
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    message = "You are Logged Out"
    messages.info(request, message)
    return redirect('index')

def user_register(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email= request.POST.get("email")
        contact_num = request.POST.get("contact_num")
        address = request.POST.get("address")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        
        if password != re_password:
            messages.error(request, "Password doesn't match")
            return redirect('register')
        
        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        user = User.objects.create(username=email, first_name=name, email=email)
        user.set_password(password)
        user.save()
        
        Profile.objects.create(user=user, contact_num=contact_num, address=address, profile_url="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp")
        return redirect('login')     
                
    return render(request, 'register.html')

@login_required
def user_profile(request):
    coffees = ConsumedCoffee.objects.filter(user_id = request.user.id)
    default_profile_pic = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.profile_url:
        profile_pic = profile.profile_url
    if not profile.profile_url:
        profile_pic = default_profile_pic
           
    context = {
        "profile" : profile,
        "profile_pic" : profile_pic,
        "coffees" : coffees
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    default_profile_pic = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.profile_url:
        profile_pic = profile.profile_url
    if not profile.profile_url:
        profile_pic = default_profile_pic
           
    context = {
        "profile" : profile,
        "profile_pic" : profile_pic
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        contact_num = request.POST.get("contact_num")
        address = request.POST.get("address")
        pic = request.FILES.get("pic")
        
            
        if pic:
            url = get_url_from_file(request, pic)   
            profile.profile_url = url     
            
        if name and name != profile.user.first_name:
            profile.user.first_name = name
        
        if contact_num and contact_num != profile.contact_num:
            profile.contact_num = contact_num
            
        if address and address != profile.address:
            profile.address = address
            
        profile.user.save()
        profile.updated_at = datetime.now() 
        profile.save()
        request.session['name']= profile.user.first_name
        request.session['profile_pic'] = profile.profile_url                        
        return redirect('profile')    
    
    return render(request, 'edit_profile.html', context)
    
    
def about_us(request):
    return render(request, 'about_us.html')