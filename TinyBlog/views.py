from django.shortcuts import render, redirect

def index(request):
    user_id = request.session.get('user_id')
    print request.session.get('nick_name')
    if not user_id:
        return render(request,'login.html')
    else:
        return render(request,'index.html', {"nick_name":request.session.get('nick_name')})
