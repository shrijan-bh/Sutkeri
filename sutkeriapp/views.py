
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.


def landing(request):
    if request.method == 'POST':
        if  request.POST.get('form_type') == 'form2':
            email=request.POST.get('email') 
            pass1=request.POST.get('password')
            valv=request.POST.get('form_type')
            print(email,pass1,valv)
            valid_user=authenticate(request, username=email,password=pass1)
            if valid_user is not None:
                login(request,valid_user)
                return redirect('home page')
            else:
                return HttpResponse("login failed")

        else:
            uname=request.POST.get('email')
            email=request.POST.get('username')
            pass1=request.POST.get('password')
            phone=request.POST.get('phone')
            valv=request.POST.get('form_type')
            print(uname,email,pass1,phone,valv)
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.first_name = phone
            myuser.save()
            messages.success(request,"user created")
            return redirect('/#popup1')    
    return render(request, 'landing.html')


def services(request):
    return render(request, 'services.html')

def header(request):
    if request.method == 'POST':
        if  request.POST.get('form_type') == 'form2':
            email=request.POST.get('email') 
            pass1=request.POST.get('password')
            valv=request.POST.get('form_type')
            print(email,pass1,valv)
            valid_user=authenticate(request, username=email,password=pass1)
            if valid_user is not None:
                login(request,valid_user)
                return redirect('home page')
            else:
                return HttpResponse("login failed")

        else:
            uname=request.POST.get('email')
            email=request.POST.get('username')
            pass1=request.POST.get('password')
            phone=request.POST.get('phone')
            valv=request.POST.get('form_type')
            print(uname,email,pass1,phone,valv)
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.first_name = phone
            myuser.save()
            messages.success(request,"user created")
            return redirect('/#popup1') 


    return render(request, "header.html")

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request,'home.html')