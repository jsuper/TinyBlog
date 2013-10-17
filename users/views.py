# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import simplejson as sjson

from users.models import UserForm
from users.models import User

def signup(request):
    form = UserForm()
    return render(request,'users/new-signup.html', {'form':form})

def login(request):
    user_mail = request.POST['email']
    password = request.POST['password']
    try:
        login_user = User.objects.get(email=user_mail)
        if login_user:
            request.session['nick_name'] = login_user.nick_name
            request.session['email'] = login_user.email 
            request.session['user_id'] = login_user.id
            return redirect('/')
        else:
            return render(request,'login.html', {'error':"Password not correct!"})
    except User.DoesNotExist:
        return render(request, 'login.html', {'error':"User not exist!"})

def create(request):
    user = UserForm(request.POST)
    if user.is_valid():
        user.save()
        return HttpResponse("Successfully create new account")
    else:
        return HttpResponse("Your input data is not valid </br>" + str(user._errors))
