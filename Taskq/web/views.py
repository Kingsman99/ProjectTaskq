from django.shortcuts import render
from .Forms import DataBaseForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):

    obj = DataBaseForm()
    return render(request, 'index.html', {"data": obj})

def Create_Task(request):
    if request.method == "POST":
        obj=DataBaseForm(request.POST)
        obj.save()
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/home')


def Proper_Login(request):
    return render(request, 'myhome.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        obj=authenticate(username=username, password=password)
        if obj is not None:
            print ("Successfull")
            return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/properlogin')


def proper_signup(request):
    return render(request, 'signup.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email,  password)
        user.save()
        print(user)
        return HttpResponseRedirect('/login')
    else:
        print("user already exists")
        return HttpResponseRedirect('/propersignup')




