# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from users.models import User
from blog.models import Post

def new_post(request):
    author_id = request.session._author_id
    user = get_object_or_404(User,id=author_id)
    post = Post(author = user, content=request.POST['content'])
    post.save()
    return HttpResponse('Create new post successfully')







