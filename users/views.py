# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from users.models import UserForm

def signup(request):
    return render(request,'users/signup.html')

def add(request):
    user = UserForm(request.POST)
    if user.is_valid():
        return HttpResponse("Your nick name is %s" % user.cleaned_data['nick_name'])
    else:
        return HttpResponse("There is valid data in form")
