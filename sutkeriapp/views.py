
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/")
def home(request):
    email=request.user.email
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize()
    }
   
    
    return render(request,'home.html',context)

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
                messages.success(request,"Login Sucessful.")
                return redirect('home page')
            else:
                messages.error(request,"Wrong Input.")
                return redirect('landingpage')

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
                messages.success(request,"Login Sucessful.")
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



def logoutpage(request):
    logout(request)
    return redirect("/")

def loginpage(request):
    return redirect("/")