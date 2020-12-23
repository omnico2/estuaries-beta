from django.contrib import admin
from .models import Theme, Categories


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Theme, ThemeAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Categories, CategoriesAdmin)