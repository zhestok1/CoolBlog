from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']
    list_display = ['username', 'email']
    
