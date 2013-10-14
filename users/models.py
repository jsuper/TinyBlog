from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100)
    genders = models.IntegerField(default=0, blank=True)
    birth_date = models.DateField(null=True)
    password = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    following = models.ManyToManyField('self', symmetrical=False)
    
    def __unicode__(self):
        return "Nick Name: %s, Id: %s" % (self.nick_name, self.id)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['full_name', 'nick_name', 'password', 'email']
