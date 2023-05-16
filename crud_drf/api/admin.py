from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list = ('id','name','email','phone','address')
    admin.site.register(User)