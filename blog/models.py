import datetime

from django.db import models
from django import forms

#import user
from users.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=140)
    write_time = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return '[' + self.content + ']'

class Comment(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=140)
    write_time = models.DateTimeField(default=datetime.datetime.now)
    post_id = models.ForeignKey(Post)
    
    def __unicode__(self):
        return '[' + self.content + ']'
