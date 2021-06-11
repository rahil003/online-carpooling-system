from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from home.models import Contact, user_cps
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, logout,login
# Create your views here.
def index(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/offer_share")
        else:
            messages.success(request, 'invalid username or password.')

            return render(request,'index.html')
    return render(request,'index.html')




    return render(request,'index.html')
    #return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about")

def whycps(request):
    return render(request,'whycps.html')

def offer_share(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
            rides = Ride.objects.all()  
            return render(request,"offer_share.html",{'rides':rides})

        

def register_user(request):
    #return render(request,'register_user.html')
    if request.method=='POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name  = form1.cleaned_data['first_name']
            last_name  = form1.cleaned_data['last_name']
            email  = form1.cleaned_data['email']
            password  = form1.cleaned_data['password']
            User.objects.create_user(username = username,first_name=first_name,last_name=last_name,email=email,password=password)
            return HttpResponseRedirect('/')
    else:
        form1 = userform()
    return render(request,'register_user.html',{'frm':form1})

def addnew(request):
    if request.method=="POST":
        form = RideForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/offer_share')
            except:
                pass
    else:
        form = RideForm()
    return render(request,'addnew.html',{'form':form})

def logoutuser(request):
    logout(request)
    return redirect("/")

def edit(request, id):  
    ride = Ride.objects.get(id=id)  
    return render(request,'edit.html', {'ride':ride})  

def update(request, id):  
    ride = Ride.objects.get(id=id)  
    form = RideForm(request.POST, instance = ride)  
    if form.is_valid():  
        form.save()  
        return redirect("/offer_share")  
    return render(request, 'edit.html', {'ride': ride}) 

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pas = request.POST.get("password")
        
        u = user_cps(username=email,password=pas)
        u.save()
        print(u.password)
        messages.success(request, 'message sent .')


    return render(request,'contact.html')
    #return HttpResponse("this is contact")    
