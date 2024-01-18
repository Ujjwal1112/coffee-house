from django.shortcuts import render, redirect
from users.models import User
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
                message = "you are logged in"
                messages.info(request, message)
                login(request, check_user)
                return redirect('index')
            if not check_user:
                message = 'Invalid email or password'
                messages.error(request, message)
                return redirect('login')
        if not User.objects.filter(email=email).exists():
            
            message = "email does not exists"
            messages.error(request, message)
            return redirect('login')   
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    message = "You are Logged Out"
    messages.info(request, message)
    return redirect('index')
    