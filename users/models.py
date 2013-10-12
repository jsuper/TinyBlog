from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    genders = models.IntegerField(default=0)
    birth_date = models.DateField()
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    following = models.ManyToManyField('self', symmetrical=False)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'nick_name', 'password']
