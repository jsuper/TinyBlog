# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from users.models import UserForm

def signup(request):
    form = UserForm()
    return render(request,'users/new-signup.html', {'form':form})

def create(request):
    user = UserForm(request.POST)
    if user.is_valid():
        user.save()
        return HttpResponse("Successfully create new account")
    else:
        return HttpResponse("Your input data is not valid </br>" + str(user._errors))
