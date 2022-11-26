from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def demo(request):
    return render(request,"index.html")


def login(request):
    return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def button(request):
    return render(request,"button.html")

def form(request):
    if request.method=='POST':
        name=request.POST['name']
        dob = request.POST['date']
        email= request.POST['email']
        number = request.POST['number']
        user=User.objects.create_user(name=name,email=email,dob=dob,number=number)
        user.save();
    return render(request,"form.html")


def index(request):
    return render(request,"index.html")


# def register(request):
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             cpassword = form.cleaned_data['cpassword']
#             user=authenticate(username=username,password=password,cpassword=cpassword)
#             login(request,user)
#             messages.success(request,("Registration Success"))
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#
#     return render(request,"register.html",{'form':form})



# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('login')
#     return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']

        password= request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')

            else:

                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")