from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/travello")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

@csrf_exempt
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created successfully')
                return redirect('login')
        else:
            print("password not matched")
            return redirect('/accounts/register')
        return redirect('/travello')
    else:
        return render(request,'register.html')
