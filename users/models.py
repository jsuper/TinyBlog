from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    genders = models.IntegerField(default=0)
    birth_date = models.DateField()
    nick_name = models.CharField(max_length=30)
    following = models.ManyToManyField('self', symmetrical=False)
