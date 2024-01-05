from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.db.utils import IntegrityError
from login.models import Employees
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect


@never_cache
def HomePage(request):
    if 'username' not in request.session:
        return redirect('login')
    username = request.session['username']
    context = {
        'user': username,
    }
    return render(request, 'home.html', context)



@never_cache
def LoginPage(request):
    if 'adminname' in request.session:
        return redirect('table')
    if 'username' in request.session:
        return redirect('home')
    print('hai1')
    if request.method == 'POST':
        print('hai2')
        print('hai3')
        username = request.POST['username']
        password = request.POST['password']
        try:
            
            user = Employees.objects.get(username=username)
            print('hai4')
        except:
            user = None
    
        if user is not None:
            request.session['username'] = username
                # login(request,user)
            print('hai5')
            return redirect('home')
            
        else:
            print('hai6')
            context={'error':'Invalid user',}
            return render(request, 'login.html',context)
             #     return render(request, 'login.html', {'error_message': 'Invalid username or password'})
        #return render(request, 'login.html')
        
    return render(request, 'login.html')


def Logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')
    

def Signup(request):
    
    if 'username' in request.session:
        return redirect('home')
    
    if 'adminname' in request.session:
        return redirect('table')
    
    if request.method == 'POST':
        
        
        username = request.POST['username']
        password = request.POST['password1']
        conformpassword = request.POST['password2']
        email =request.POST['email']
        phone = request.POST['phone']
        
        if conformpassword != password:
            
            return render(request,'signup.html',{"error_message":"not same password"})
            
    
        if Employees.objects.filter(username=username,password=password).exists():
           
            return render(request,'signup.html',{"error_message":"Username is already exist"})

        user=Employees(
                username = username,
                password = password,
                email = email,
                phone = phone
         )
            
        user.save()
            # login(request, user)
        return redirect('login')
        
            
    return render(request, 'signup.html')
@never_cache
def Table(request):
    if 'adminname' in request.session:
        print('hello1')
        emp=Employees.objects.all()
        context ={
        'emp':emp,
        }
        return render(request, 'table.html',context)
    else:
        print('hello2')
        return redirect('adminlogin')

def ADD(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        emp=Employees(username=username,email=email,password=password)
        
        emp.save()
        return redirect('table')
    return redirect('adminlogin')
    
def Edit(request):
    emp=Employees.objects.all()
    context={
        'emp':emp,
    }
    return render(request,'table.html',context)


def Update(request,id):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        
        emp=Employees(id=id,
                      username=username,
                      email=email,
                      password=password,
                      phone=phone)
        emp.save()
        return redirect('table')
    return redirect("table.html")

@never_cache
def Delete(request,id):
    if request.method == 'POST':
        emp=Employees.objects.filter(id=id).delete()
        context ={
            'emp':emp,
        }
        return redirect("table")
    return HttpResponse("hai")

@never_cache
def AdminLogin(request):
    if 'username' in request.session:
        return redirect('home')
    if 'adminname' in request.session:
        
        return redirect('table')
    if request.method == 'POST':
        #if 'username' not in request.session:
            
        

        adminname = request.POST['username']
        password = request.POST['password']
            
        user=authenticate(username= adminname,password=password)
        print('hello5')
        if user is not None:
            print('hello6')
            request.session['adminname'] = adminname
            return redirect('table')
        else:
            print('hello7')
            return render(request,'admin.html',{'error':'Invalid admin'})
        
    
       # return render(request,'admin.html')
    else:
        print('hello8')

        return render(request,'admin.html')

@never_cache
def AdminLogout(request):
    
    print('hello9')
    if 'adminname' in request.session:
        del request.session['adminname']
        print('hello10')
    print('hello11')
    return redirect('adminlogin')

@never_cache
def Search(request):
   
    if request.method == 'POST':
        username=request.POST['search']
        try:
            user = Employees.objects.get(username=username)
            
        except:
            user=None
            
        if user:
            context={'user':user}
            return render(request,'search.html',context)
        
        else:
            
            messages.error(request, 'Invalid user')
            return render(request,'search.html')
    else:
        
        return redirect('table')
     