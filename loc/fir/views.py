from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,missing_obj,murder,miss_person
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




def fir_mo(request):
    if request.method =='POST':
        complainant=request.user
        objct_name = request.POST['obj_name']
        miss_date = request.POST['missing_date']
        location = request.POST['location']
        obj_descr = request.POST['obj_descr']

        
        cuser=missing_obj(complainant=complainant,missdate=miss_date,objectdescription=obj_descr,object_name=obj_name,location=location)
        cuser.save()
        return HttpResponse('MO')


    else:
    
        return render(request,"FIR1.html")
       







def fir_dp(request):
    if request.method =='POST':
        complainant=request.user
        dead_name = request.POST['dp_name']
        suspects = request.POST['suspects']
        location = request.POST['location']
        

        
        tuser=murder(complainant=complainant,dead_name=dead_name,suspects=suspects,location=location)
        tuser.save()
        return HttpResponse('DP')


    else:
    
        return render(request,"FIR2.html")




def fir_mp(request):
    if request.method =='POST':
        complainant=request.user
        p_name = request.POST['p_name']
        miss_date = request.POST['missing_date1']
        p_descr = request.POST['p_descr']
        location = request.POST['location']
        

        
        tuser=miss_person(complainant=complainant,pdescription=p_descr,miss_name=p_name,last_seen_loc=location,missdate=miss_date)
        tuser.save()
        return HttpResponse('MP')


    else:
    
        return render(request,"FIR3.html")

 
    
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
