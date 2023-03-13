
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from sutkeriapp.models import KYC,health_parameter


# Create your views here.
@login_required(login_url="/")
def home1(request):
    health_data=health_parameter.objects.all()

    
    

    val="LOW RISK"
    email=request.user.email
    
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize(),
        'health_data':health_data,
        'val':val,
        

    }
   
    
    return render(request,'home1.html',context)

def home2(request):
    health_data=health_parameter.objects.all()
    val="LOW RISK"
    email=request.user.email
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize(),
        'mess1':"This week:     ",
        'mess2':"    Blood Sugar: " + str(B_S)+ " mmol/l     ",
        'mess3':"    Systolic BP: " + str(upper_bp)+ "     Diastolic BP: " + str(lower_bp),
        'mess4':"    Body Temperature: " + str(B_T)+ " °F     ",
        'mess5':"    Aproximate Calculated Risk: " + val,

    }
   
    
    return render(request,'home2.html',context)

def home3(request):
    upper_bp=health_parameter.objects.Systolic_BP()
    lower_bp=health_parameter.objects.Diastolic_BP()
    B_S=health_parameter.objects.Blood_Sugar()
    B_T=health_parameter.objects.Body_Temperature()
    val="LOW RISK"
    email=request.user.email
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize(),
        'mess1':"This week:     ",
        'mess2':"    Blood Sugar: " + str(B_S)+ " mmol/l     ",
        'mess3':"    Systolic BP: " + str(upper_bp)+ "     Diastolic BP: " + str(lower_bp),
        'mess4':"    Body Temperature: " + str(B_T)+ " °F     ",
        'mess5':"    Aproximate Calculated Risk: " + val,

    }
   
    
    return render(request,'home3.html',context)


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
                return redirect('home1 page')
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
                return redirect('home1 page')
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
            return redirect('/#popup1') 


    return render(request, "header.html")

def contact(request):
    return render(request, 'contact.html')



def logoutpage(request):
    logout(request)
    return redirect("/")

def loginpage(request):
    return redirect("/")

def kyc(request):
    if request.method=="POST":
        First_name=request.POST.get("first_name")
        Middle_name=request.POST.get("middle_name")
        Last_name=request.POST.get("last_name")
        Date_of_birth=request.POST.get("dob")
        Husband_name=request.POST.get("husband_name")
        Age=request.POST.get("age")
        Last_period_date=request.POST.get("lpd")
        Address=request.POST.get("address")
        print(First_name,Middle_name,Last_name,Date_of_birth,Husband_name,Age,Last_period_date,Address)
        epd=KYC(First_name=First_name, Middle_name=Middle_name, Last_name=Last_name, Husband_name=Husband_name,Date_of_birth=Date_of_birth,Age=Age,Last_period_date=Last_period_date,Address=Address)
        epd.save()
        return redirect("home1 page")


    return render(request, 'kyc.html')

def healthdata(request):
    if request.method=="POST":
        Systolic_BP=request.POST.get("upper_bp")
        Diastolic_BP=request.POST.get("lower_bp")
        Blood_Sugar=request.POST.get("bs")
        Body_Temperature=request.POST.get("bt")
        
       
        ehd=health_parameter(Systolic_BP=Systolic_BP, Diastolic_BP=Diastolic_BP, Blood_Sugar=Blood_Sugar, Body_Temperature=Body_Temperature)
        ehd.save()
        return redirect("home1 page")
    return render(request, 'healthdata.html')

