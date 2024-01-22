from django.shortcuts import render, redirect
from users.models import User, Profile
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

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
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        user = User.objects.create(username=email, first_name=name, email=email)
        user.set_password(password)
        user.save()
        
        Profile.objects.create(user=user, contact_num=contact_num, address=address)
        return redirect('index')     
                
    return render(request, 'register.html')


def user_profile(request):
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
    return render(request, 'profile.html', context)
    