from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib import auth



def index(request):
    return HttpResponse("INDEX")




def login(request):
    
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Galat")
   
   
   
    return render(request,'login.html')




def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        contact = request.POST['contact']
       

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
            
        else:
            if User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")

            else:

                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                email=email,password=password,contact=contact,Date_of_Birth=dob)
                user.save()
                return render(request,'index.html')


    else:
    
        return render(request,'signup.html')
       

 
    
        


def fir_mo(request):
    return HttpResponse("MO")
