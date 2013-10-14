from django.contrib import admin
from users.models import User 

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','nick_name','email')


admin.site.register(User, UserAdmin)
