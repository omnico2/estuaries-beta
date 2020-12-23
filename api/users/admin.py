from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username']
    ordering = ['-member_since']


admin.site.register(CustomUser, CustomUserAdmin)