
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from sutkeriapp.models import KYC,health_parameter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split as split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import os


# Create your views here.
@login_required(login_url="/")
def home1(request):
    
    health_data=health_parameter.objects.all()
    
    email=request.user.email
    username=request.user.username

    context={
        'email':email.title(),
        'username':username.capitalize(),
        'health_data':health_data,
    }
   
    
    return render(request,'home1.html',context)

def home2(request):
    
    health_data=health_parameter.objects.all()
    
    email=request.user.email
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize(),
        'health_data':health_data,
        
    }
   
    
    return render(request,'home2.html',context)

def home3(request):
    
    health_data=health_parameter.objects.all()
    
    email=request.user.email
    username=request.user.username
    context={
        'email':email.title(),
        'username':username.capitalize(),
        'health_data':health_data,
        
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
        request.session['Age']= Age
        

        
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
        request.session['upper_bp']= Systolic_BP
        request.session['lower_bp']= Diastolic_BP
        request.session['bs']= Blood_Sugar
        request.session['bt']= Body_Temperature
        Result=riskCalculator(request)
        
        
        request.session['upper_bp']= Systolic_BP
        request.session['lower_bp']= Diastolic_BP
        request.session['bs']= Blood_Sugar
        request.session['bt']= Body_Temperature
        

        ehd=health_parameter(Systolic_BP=Systolic_BP, Diastolic_BP=Diastolic_BP, Blood_Sugar=Blood_Sugar, Body_Temperature=Body_Temperature,Result=Result)
        ehd.save()
        
        return redirect("home1 page")
    return render(request, 'healthdata.html')

def riskCalculator(request):
    u_bp=request.session['upper_bp']
    l_bp=request.session['lower_bp']
    bs=request.session['bs']
    bt=request.session['bt']
    age=request.session["Age"]
    print(age,u_bp,l_bp,bs,bt)

    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))


    data = pd.read_csv('E:\\coding\\Maternal Health Risk Data Set.csv')
    data.head()

    print(f"There are {data.duplicated().sum()} duplicates data")
    data.loc[data.duplicated(keep=False)].sort_values(by=data.columns.to_list())


    data_proc = data.drop(data.index[data.HeartRate == 7])

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(data=data, x="HeartRate", kde=True, ax=ax[0])
    sns.histplot(data=data_proc, x="HeartRate", kde=True, ax=ax[1])
    ax[0].set_title("Original HeartRate Distribution")
    ax[1].set_title("Processed HeartRate Distribution")

    data_proc = data_proc.drop(["HeartRate"], axis=1)


    X = data.drop("RiskLevel", axis=1)
    y = data.RiskLevel
    x_train, x_test, y_train, y_test = split(X, y, test_size=0.2, random_state=1)


    X_proc = data_proc.drop("RiskLevel", axis=1)
    y_proc = data_proc.RiskLevel
    x_train_proc, x_test_proc, y_train_proc, y_test_proc = split(X_proc, y_proc, test_size=0.2, random_state=1)

    print(f"Original data has {x_train.shape[0]} train data and {x_test.shape[0]} test data\n")
    print(f"Processes data has {x_train_proc.shape[0]} train data and {x_test_proc.shape[0]} test data")


    rf2 = RandomForestClassifier(random_state=100)
    rf2.fit(x_train_proc.values, y_train_proc)
    y_pred = rf2.predict(x_test_proc.values)
    print(f"Processed Dataset Accuracy: {accuracy_score(y_test_proc, y_pred)}")

    params = {
        "n_estimators": [10, 20, 50, 100],
        "criterion": ["gini", "entropy"]
    }
    rf = RandomForestClassifier(random_state=100)
    grid = GridSearchCV(rf, params, cv=10)
    grid.fit(x_train_proc.values, y_train_proc)


    pd.DataFrame(grid.cv_results_).sort_values(by="rank_test_score")[["params", "mean_test_score", "rank_test_score"]]

    y_pred = grid.predict(x_test_proc.values)

    newdata=[age,u_bp,l_bp,bs,bt]

    riskans = grid.predict([newdata])[0].upper() 
    print(riskans)
    return(riskans)


