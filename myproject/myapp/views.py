from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import User
from django.contrib import messages ,auth

# Create your views here.   
def index(request):
    product1=product.objects.all()
    return render(request,'index.html',{'use':product1})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['repeatpassword']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                User.objects.create_user(username=username,email=email,password=password)
                User.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:       
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request,'login.html')
    
def logout():
    auth.logout()
    return render('login')
def count(request):
    word=request.POST['words']
    returnval=len(word.split())
    return render(request,'count.html',{'ammount':returnval})

